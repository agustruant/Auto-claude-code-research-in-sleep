"""Lee el árbol IQ-TREE (318 dominios) y reporta: monofilia de cada clado, dónde caen las 15 nuevas y soportes (SH-aLRT/UFBoot).
Uso: python3 review-stage/scripts/leer_arbol318.py review-stage/datos/ubicacion16/iq318.treefile"""
import sys, collections
from Bio import Phylo
t = Phylo.read(sys.argv[1], "newick")
fam = lambda n: n.split("__")[0]
tips = t.get_terminals(); name = {x: x.name for x in tips}
# enraizar con el clado II (como en el análisis original)
II = [x for x in tips if x.name.startswith("II__") or x.name == "REF_SufS_Ecoli"]
try:
    t.root_with_outgroup(t.common_ancestor(II))
except Exception as e:
    print("no se pudo enraizar en II:", e)
def sup(c):
    s = c.confidence if c.confidence is not None else (c.name or "")
    return s
def clade_of(names):
    return t.common_ancestor([t.find_any(name=n) for n in names])
for f in ("I", "L3"):   # II se usa como raíz: su "MRCA" no es informativo
    mem = [x for x in tips if fam(x.name) == f]
    m = t.common_ancestor(mem); inside = [x.name for x in m.get_terminals()]
    extra = collections.Counter(fam(n) for n in inside if fam(n) != f)
    print(f"{f}: {len(mem)} miembros; MRCA contiene {len(inside)} hojas; intrusos {dict(extra)}; soporte '{m.name or m.confidence}'")
L3 = [x.name for x in tips if fam(x.name) == "L3"]
m = clade_of(L3); inside = set(x.name for x in m.get_terminals())
new = [x.name for x in tips if x.name.startswith("NEW__")]
print("\nNuevas dentro del MRCA de L3:", sum(n in inside for n in new), "/", len(new))
for n in new:
    leaf = t.find_any(name=n); path = t.get_path(leaf)
    # hermano más cercano: hojas del nodo padre
    parent = path[-2] if len(path) > 1 else t.root
    sis = [x.name for x in parent.get_terminals() if x.name != n]
    sis = sis[:4] + ([f"... (+{len(sis)-4})"] if len(sis) > 4 else [])   # nodo padre completo, no sólo las primeras hojas
    print(f"  {n:50s} {'DENTRO' if n in inside else 'FUERA'} de L3 | nodo padre '{parent.name or parent.confidence}' | junto a: {sis}")
L3n = L3 + new
m2 = clade_of(L3n); ins2 = [x.name for x in m2.get_terminals()]
print("\nMRCA(L3 + nuevas):", len(ins2), "hojas; intrusos:", [n for n in ins2 if n not in L3n][:10], "; soporte", m2.name or m2.confidence)
