"""Recalcula desde scly_like_localizacion.csv todos los números de localización del dossier.
Uso: python3 review-stage/scripts/recalculo_localizacion.py scly_like_localizacion.csv"""
import sys, collections
import pandas as pd

d = pd.read_csv(sys.argv[1], encoding="utf-8-sig")
scly = d[d.rol == "SCLY-like"]
alg = scly[scly.linaje != "Metazoa"]
fia = alg[alg.N_terminal_fiable]            # algales con N-terminal fiable (sin SCLY humana)
ctl = d[d.rol == "control"]

print("== Conteos ==")
print(f"filas SCLY-like: {len(scly)} (algales {len(alg)}, humana {len(scly)-len(alg)})")
print(f"especies algales: {alg.especie.nunique()}")
print(alg.groupby("linaje").agg(secuencias=("id", "size"), especies=("especie", "nunique")).to_string())
print(f"algales con N-terminal fiable: {len(fia)}")

print("\n== DeepLoc, etiquetas completas (algales fiables) ==")
print(fia.Localizations.value_counts().to_string())
print(f"con 'Plastid' en la etiqueta: {fia.Localizations.str.contains('Plastid').sum()}")
print(f"P(plástido) > 0,5: {(fia.Plastid > 0.5).sum()} / {len(fia)}")
print(fia.groupby("linaje").apply(lambda x: f"{(x.Plastid > 0.5).sum()}/{len(x)}").to_string())
print("\nMedianas:", {c: round(fia[c].median(), 2) for c in ["Cytoplasm", "Mitochondrion", "Plastid", "Endoplasmic reticulum"]})
print("TargetP:", fia.targetp.value_counts().to_dict())
print("TargetP SP por linaje:", fia[fia.targetp == "SP"].linaje.value_counts().to_dict())
print(f"SignalP Eukarya sin SP: {(fia.sp_euk == 'OTHER').sum()} / {len(fia)}; n_TM>0: {(fia.n_TM > 0).sum()}")

print("\n== Secuencias con P(plástido) > 0,5 ==")
print(fia[fia.Plastid > 0.5][["id", "especie", "linaje", "Plastid", "Mitochondrion", "targetp", "cTP", "SP"]]
      .sort_values("Plastid", ascending=False).to_string(index=False))

print("\n== Panel de control ==")
print(ctl[["id", "especie", "Localizations", "Plastid", "Mitochondrion", "Cytoplasm", "targetp"]].to_string(index=False))

print("\n== Bucle catalítico (14 posiciones) ==")
L = scly.bucle.dropna()
print(f"secuencias con bucle: {len(L)} (incluye humana: {'Q96I15' in set(scly[scly.bucle.notna()].id)})")
for i in range(14):
    c = collections.Counter(x[i] for x in L)
    print(i + 1, dict(c.most_common(3)))
