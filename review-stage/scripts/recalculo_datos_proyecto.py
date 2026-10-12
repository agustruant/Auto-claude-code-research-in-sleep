"""Recálculos sobre los archivos del proyecto (carpeta review-stage/datos, bajados del Drive).
Uso: python3 review-stage/scripts/recalculo_datos_proyecto.py review-stage/datos
Requiere: pandas, scipy, statsmodels, biopython."""
import sys, os, collections
import pandas as pd
from scipy import stats
from statsmodels.stats.contingency_tables import StratifiedTable
from Bio import Phylo, SeqIO

D = sys.argv[1]; P = lambda f: os.path.join(D, f)
fam = lambda n: n if n.startswith("REF") else n.split("__")[0]

# 1. Tabla His +1 sobre los 617 candidatos
c = pd.read_csv(P("candidatos_desulfurasas.csv"), encoding="utf-8-sig")
L = c.loop.fillna("")
c["C7"] = (L.str.len() >= 8) & (L.str[6] == "C")
c["CH"] = c.C7 & (L.str[7] == "H")
print("== 1. His en +1 de la Cys catalítica, por clase (617 candidatos)")
print(pd.crosstab(c.clase, [c.C7.rename("Cys en pos 7"), c.CH.rename("His en +1")]).to_string())
for k, g in c[c.C7].groupby("clase"):
    print(f"  residuo +1 en {k.strip()}: {dict(collections.Counter(g.loop.str[7]).most_common(5))}")
best = c[["s_I", "s_II", "s_L3"]].idxmax(axis=1)
print("  mejor cebo vs His +1 (independiente del bucle):")
print(pd.crosstab(best, c.CH).to_string())
ex = c[(c.clase == "otro") & c.CH]
print(f"  'otro' con C-H: {len(ex)}")
print(ex[["acc", "especie", "grupo", "cebo", "evalue", "blen", "loop"]].to_string(index=False))

# 2. Árbol
t = Phylo.read(P("arbol_desulfurasas.nwk"), "newick")
tips = t.get_terminals()
print("\n== 2. Árbol: hojas", len(tips), dict(collections.Counter(fam(x.name) for x in tips)))
l3 = [x for x in tips if x.name.startswith("L3__")]
m = t.common_ancestor(l3)
print("  MRCA de L3: n =", len(m.get_terminals()), "soporte SH =", m.confidence,
      [x.name for x in m.get_terminals() if not x.name.startswith("L3__")])
alg = [x for x in l3 if "Homo_sapiens" not in x.name] + [t.find_any(name="REF_HText_Spabb")]
m2 = t.common_ancestor(alg)
print("  MRCA sólo algal (+HText): n =", len(m2.get_terminals()), "soporte SH =", m2.confidence)
ids = {x.name.split("__")[1] for x in tips if "__" in x.name}
c["u"] = c.acc.str.split("|").str[1]
fuera = c[c.clase.str.startswith(("I ", "II")) & ~c.u.isin(ids)]
print(f"  NFS1/NFS2 del CSV que no están en el árbol: {len(fuera)} ({', '.join(sorted(fuera.especie.unique()))})")

# 3. Asp146 (SCLY humana) y bucle en el MSA
A = [(r.id, str(r.seq)) for r in SeqIO.parse(P("msa_desulfurasas_trim.fasta"), "fasta")]
hum = dict(A)["REF_SCLY_human"]
def col(row, motif, k):
    s = row.replace("-", ""); i = s.index(motif) + k; n = -1
    for j, ch in enumerate(row):
        if ch != "-":
            n += 1
            if n == i: return j
dom = {r.id: str(r.seq) for r in SeqIO.parse(P("dominios_desulfurasas.fasta"), "fasta")}["L3__Q96I15__Homo_sapiens"]
st = 37 - dom.index("NATT")
print("\n== 3. Numeración humana: dominio empieza en", st, "| H145", dom[145 - st], "D146", dom[146 - st], "K259", dom[259 - st], "C388", dom[388 - st], "H389", dom[389 - st])
cD = col(hum, "VEHDSIR", 3); cC = col(hum, "GAACHSD", 3)
for nm, cc in [("posición Asp146", cD)] + [(f"Cys{off:+d}", cC + off) for off in range(-6, 3)]:
    by = collections.defaultdict(collections.Counter)
    for n, s in A: by[fam(n)][s[cc]] += 1
    print(f"  {nm}: " + " | ".join(f"{k}: {dict(v.most_common(4))}" for k, v in by.items() if k in ("I", "II", "L3")))
print("  L3 sin Pro en Asp146:", [(n.split('__')[1], s[cD]) for n, s in A if n.startswith("L3") and s[cD] != "P"])

# 4. Posiciones discriminantes y enriquecimiento con base condicional
t2 = pd.read_csv(P("conservacion_scly_por_posicion.csv"), encoding="utf-8-sig")
t2["near"] = t2.d_ligando < 8
print(f"\n== 4. Conservación: {len(t2)} posiciones, {t2.near.sum()} a < 8 Å")
for nm, base, extra in [("SCLY vs NFS1 y NFS2", (t2.H_L3 <= .5) & (t2.H_I <= .5) & (t2.H_II <= .5), (t2.cons_L3 != t2.cons_I) & (t2.cons_L3 != t2.cons_II)),
                        ("SCLY vs NFS1", (t2.H_L3 <= .5) & (t2.H_I <= .5), t2.cons_L3 != t2.cons_I)]:
    b = t2[base]; x = t2[base & extra]; p0 = b.near.mean()
    print(f"  {nm}: conservadas {len(b)} ({b.near.sum()} cerca, p0={p0:.3f}); discriminantes {len(x)} {x.res_model.tolist()}, cerca {x.near.sum()}; "
          f"binomial p = {stats.binomtest(int(x.near.sum()), len(x), p0, alternative='greater').pvalue:.3f}")
print("  Spearman f_L3 vs distancia:", stats.spearmanr(t2.f_L3, t2.d_ligando))

# 5. Maquinaria Sec: Fisher global y CMH por linaje
s = pd.read_csv(P("sec_vs_scly_por_proteoma.csv"), encoding="utf-8-sig"); s["S"] = s.SCLY_like > 0
print("\n== 5. Sec_estricto = PSTK y SEPSECS y EEFSEC:",
      ((s.PSTK & s.SEPSECS & s.EEFSEC) == s.Sec_estricto).all())
print("  Fisher global:", stats.fisher_exact(pd.crosstab(s.Sec_estricto, s.S).values[::-1, ::-1]))
tabs = []
for lin, g in s.groupby("linaje"):
    tt = pd.crosstab(g.Sec_estricto, g.S).reindex(index=[True, False], columns=[True, False], fill_value=0).values
    if (tt.sum(0) > 0).all() and (tt.sum(1) > 0).all(): tabs.append(tt.astype(float)); print("  estrato", lin, tt.tolist())
st_ = StratifiedTable(tabs)
print(f"  CMH: OR_MH = {st_.oddsratio_pooled:.2f}, p = {st_.test_null_odds().pvalue:.3f}")
ch = s[s.linaje == "Chlorophyta"]
print(f"  Chlorophyta: {ch.S.sum()}/{len(ch)} proteomas, {ch[ch.S].especie.nunique()}/{ch.especie.nunique()} especies con SCLY-like")
print("  PABB004 en los 119:", s.especie.str.contains("PABB").any(), "| Drosophila SCLY-like:", int(s[s.especie.str.contains("Drosophila")].SCLY_like.iloc[0]))

# 6. Tasas relativas
r = pd.read_csv(P("tasas_relativas_pareadas.csv"), encoding="utf-8-sig")
print("\n== 6. Tasas: n =", len(r))
for a, b in [("SCLY", "NFS1"), ("NFS2", "NFS1"), ("SCLY", "NFS2")]:
    d = r[a] - r[b]
    print(f"  {a}-{b}: {int((d > 0).sum())}/{len(d)} pares positivos, mediana {d.median():.3f}, Wilcoxon p = {stats.wilcoxon(r[a], r[b]).pvalue:.3g} (mínimo exacto 2/2^38 = {2/2**38:.2g})")
