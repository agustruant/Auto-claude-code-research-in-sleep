"""Reconstrucción ancestral del residuo equivalente a Asp146 (SCLY humana) sobre una topología de especies estándar.
Recalcula Fitch y Mk (tasa única simétrica, longitudes iguales) y prueba sensibilidad.
Uso: python3 review-stage/scripts/asr_determinante.py"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar
from Bio import Phylo
from io import StringIO

MET = "(Amphimedon,(Trichoplax,((Nematostella,Hydra),(((Capitella,Crassostrea),Celegans),(Strongylocentrotus,(Branchiostoma,(Ciona,(Danio,(Xenopus,(Gallus,(Mus,Homo)))))))))))"
def topo(guill="(Chlamydomonas,Guillardia)", root="discoba"):
    hol = f"(Salpingoeca,{MET})"
    amo = f"(Acanthamoeba,{hol})"
    dia = f"({guill},((Thalassiosira,Phytophthora),Dinophyceae))"
    if root == "discoba":
        return f"(Trypanosoma,({amo},{dia}));"
    return f"({amo},(Trypanosoma,{dia}));"          # raíz Amorphea | Diaphoretickes (Discoba dentro de Diaphoretickes)

STATES = {"D": "D", "P": "P", "V": "V"}
base = dict(Amphimedon="D", Trichoplax="D", Nematostella="D", Hydra="D", Capitella="D", Crassostrea="D", Celegans="P",
            Strongylocentrotus="D", Branchiostoma="D", Ciona="D", Danio="D", Xenopus="D", Gallus="D", Mus="D", Homo="D",
            Salpingoeca="D", Acanthamoeba="P", Trypanosoma="P", Chlamydomonas="P", Thalassiosira="P", Phytophthora="V",
            Dinophyceae="V", Guillardia="PV")
S = ["D", "P", "V"]

def fitch(t, tips):
    cost = 0
    def go(c):
        nonlocal cost
        if c.is_terminal(): return set(tips[c.name])
        sets = [go(k) for k in c.clades]
        inter = set.intersection(*sets)
        if inter: return inter
        cost += len(sets) - 1
        return set.union(*sets)
    go(t.root); return cost

def mk(t, tips, q):
    k = len(S); Q = np.full((k, k), q / (k - 1)); np.fill_diagonal(Q, -q)
    Pm = {}
    def P_(c):
        if c not in Pm: Pm[c] = expm(Q * (c.branch_length if c.branch_length else 1.0))
        return Pm[c]
    L = {}
    def up(c):
        if c.is_terminal():
            v = np.array([1.0 if s in tips[c.name] else 0.0 for s in S]); L[c] = v; return v
        v = np.ones(k)
        for ch in c.clades: v *= P_(ch) @ up(ch)
        L[c] = v; return v
    r = up(t.root); lik = (r / k).sum()
    # marginal por doble pasada
    post = {}
    def down(c, outside):
        m = outside * L[c]; post[c] = m / m.sum()
        for ch in c.clades:
            others = np.ones(k)
            for o in c.clades:
                if o is not ch: others *= P_(o) @ L[o]
            down(ch, P_(ch).T @ (outside * others))
    down(t.root, np.ones(k) / k)
    return np.log(lik), post

def run(label, nwk, tips, deep=1.0):
    t = Phylo.read(StringIO(nwk), "newick")
    met = t.common_ancestor([t.find_any(name="Amphimedon"), t.find_any(name="Homo")])
    inside = set(met.find_clades())
    for c in t.find_clades():
        if c is not t.root: c.branch_length = 1.0 if c in inside else deep   # ramas profundas (fuera de Metazoa) más largas
    res = minimize_scalar(lambda q: -mk(t, tips, q)[0], bounds=(1e-4, 2), method="bounded")
    q = res.x; ll, post = mk(t, tips, q)
    def node(names): return t.common_ancestor([t.find_any(name=n) for n in names])
    nodes = {"raíz": t.root, "Amorphea": node(["Acanthamoeba", "Homo"]), "Choanozoa (Salpingoeca+Metazoa)": node(["Salpingoeca", "Homo"]),
             "Metazoa": node(["Amphimedon", "Homo"]), "Bilateria": node(["Celegans", "Homo"]), "Ecdysozoa+Lophotrochozoa": node(["Celegans", "Capitella"]),
             "Diaphoretickes": node(["Chlamydomonas", "Dinophyceae"]), "SAR": node(["Thalassiosira", "Dinophyceae"])}
    print(f"\n== {label}: Fitch = {fitch(t, tips)} cambios; q_ML = {q:.3f}; lnL = {ll:.2f}")
    for k_, n in nodes.items():
        print(f"  {k_:28s} " + "  ".join(f"{s}={p:.3f}" for s, p in zip(S, post[n]) if p > 0.005))

run("Guillardia polimórfica (P+V), raíz en Discoba", topo(), base)
run("Guillardia = V (sólo la copia L1J7X1)", topo(), {**base, "Guillardia": "V"})
run("Guillardia = P (sólo la copia L1J7A3)", topo(), {**base, "Guillardia": "P"})
run("raíz Amorphea | Diaphoretickes", topo(root="amorphea"), base)
run("Guillardia hermana de dinoflagelados (como en el árbol de genes)",
    topo(guill="Chlamydomonas").replace("Dinophyceae)", "(Dinophyceae,Guillardia))"), base)

print("\n######## Sensibilidad (pedida en la ronda 5) ########")
run("ramas profundas x5", topo(), base, deep=5)
run("ramas profundas x10", topo(), base, deep=10)
run("Acanthamoeba y Trypanosoma desconocidos (posible HGT)", topo(), {**base, "Acanthamoeba": "DPV", "Trypanosoma": "DPV"})
run("Salpingoeca desconocido (n = 1 coanoflagelado)", topo(), {**base, "Salpingoeca": "DPV"})
