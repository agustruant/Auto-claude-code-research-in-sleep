"""Versión genérica de ubicacion16.py: extrae dominio, asigna familia por HMM, realinea con FAMSA y lee bucle/Asp146.
1) extrae el dominio con un HMM construido del MSA del proyecto; 2) asigna familia por HMMs de cada clado;
3) realinea todo (FAMSA), recorta por ocupación >= 0,35 y escribe el alineamiento para IQ-TREE; 4) lee el bucle y la posición Asp146.
Uso: python3 review-stage/scripts/ubicacion_generica.py review-stage/datos <subcarpeta> <fasta>"""
import sys, os, re, collections
import pyhmmer
from pyhmmer.easel import Alphabet, TextSequence, TextMSA, SequenceFile
from pyfamsa import Aligner, Sequence
from Bio import SeqIO

N_ = lambda x: x.decode() if isinstance(x, bytes) else x
D = sys.argv[1]; U = os.path.join(D, sys.argv[2] if len(sys.argv) > 2 else "ubicacion16"); aa = Alphabet.amino()
msa = [(r.id, str(r.seq).upper()) for r in SeqIO.parse(os.path.join(D, "msa_desulfurasas_trim.fasta"), "fasta")]

def build(name, recs):
    m = TextMSA(name=name, sequences=[TextSequence(name=n, sequence=s) for n, s in recs]).digitize(aa)
    hmm, _, _ = pyhmmer.plan7.Builder(aa).build_msa(m, pyhmmer.plan7.Background(aa)); return hmm

H_all = build("PF00266_proyecto", msa)
H = {f: build(f, [(n, s) for n, s in msa if n.startswith(f + "__")]) for f in ("I", "II", "L3")}

with SequenceFile(os.path.join(U, (sys.argv[3] if len(sys.argv) > 3 else "nuevas16.fasta")), digital=True, alphabet=aa) as fh: seqs = fh.read_block()
raw = {r.id.split("|")[1]: (str(r.seq), r.description) for r in SeqIO.parse(os.path.join(U, (sys.argv[3] if len(sys.argv) > 3 else "nuevas16.fasta")), "fasta")}
dom = {}
for hits in pyhmmer.hmmsearch([H_all], seqs, E=1e-5):
    for h in hits:
        acc = N_(h.name).split("|")[1]; best = max(h.domains, key=lambda d: d.score)
        a, b = best.env_from, best.env_to; dom[acc] = raw[acc][0][a - 1:b]
        print(f"{acc}: dominio {a}-{b} ({b - a + 1} aa), score {best.score:.0f}, E {best.i_evalue:.1e}")
print("sin dominio:", sorted(set(raw) - set(dom)))

dseq = [TextSequence(name=k, sequence=v).digitize(aa) for k, v in dom.items()]
blk = pyhmmer.easel.DigitalSequenceBlock(aa, dseq)
sc = collections.defaultdict(dict)
for f, hm in H.items():
    for hits in pyhmmer.hmmsearch([hm], blk, E=10, Z=1):
        for h in hits: sc[N_(h.name)][f] = h.score
print("\n== Asignación por HMM de clado (bits)")
for k in dom:
    s = sc[k]; best = max(s, key=s.get) if s else "-"
    print(f"  {k:12s} {raw[k][1].split('OS=')[1].split(' OX')[0][:32]:32s} I={s.get('I',0):6.0f} II={s.get('II',0):6.0f} L3={s.get('L3',0):6.0f} -> {best}")

# realineamiento conjunto
orig = [(r.id, str(r.seq).upper()) for r in SeqIO.parse(os.path.join(D, "dominios_desulfurasas.fasta"), "fasta")]
orig = [(n, s) for n, s in orig if n != "REF_SCLY_human"]          # duplicado exacto de L3__Q96I15
sp = lambda k: re.sub(r"\W+", "_", raw[k][1].split("OS=")[1].split(" OX")[0])[:28]
new = [(f"NEW__{k}__{sp(k)}", v) for k, v in dom.items()]
allr = orig + new
aln = Aligner(guide_tree="upgma").align([Sequence(n.encode(), s.encode()) for n, s in allr])
rows = [(N_(x.id), N_(x.sequence)) for x in aln]
L = len(rows[0][1]); keep = [j for j in range(L) if sum(r[1][j] != "-" for r in rows) / len(rows) >= 0.35]
with open(os.path.join(U, "aln_trim.fasta"), "w") as f:
    for n, s in rows: f.write(f">{n}\n{''.join(s[j] for j in keep)}\n")
print(f"\nalineamiento: {len(rows)} secuencias, {L} columnas -> {len(keep)} con ocupación >= 0,35")

# columna Asp146 y bucle catalítico, sobre el alineamiento completo (sin recortar)
R = dict(rows); hum = R["L3__Q96I15__Homo_sapiens"]
def col(row, motif, k):
    s = row.replace("-", ""); i = s.index(motif) + k; n = -1
    for j, ch in enumerate(row):
        if ch != "-":
            n += 1
            if n == i: return j
cD = col(hum, "VEHDSIR", 3); cC = col(hum, "GAACHSD", 3)
print("\n== Nuevas: residuo en Asp146 (contexto) y bucle catalítico (Cys-6..Cys+2)")
for n, s in new:
    r = R[n]; ctx = r[cD - 3:cD + 3]; loop = r[cC - 6:cC + 3]
    print(f"  {n:52s} Asp146={r[cD]}  ctx={ctx}  bucle={loop}")
