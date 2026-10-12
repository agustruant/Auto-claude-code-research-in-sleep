# Ronda 5 — respuesta del revisor (resumen fiel; subagente Claude, misma familia que el ejecutor)

Score: 6.5/10 (ronda 4: 6/10) · Verdict: not ready. El bloque Se/S agrega valor real, pero sus dos afirmaciones titulares se exceden. Lo que todavía impide "almost" son los pendientes de las rondas 2–4.

Confirmado:
- 3GZC (A 29–444, 403 residuos; D146 OD2–C388 SG 3,73 Å; D146–PLR 6,29 Å medido N del esqueleto → N1 del PLR; ASVGAACH desde 382; ligando PLR).
- Conteos por familia (300 filas).
- Las 32 llamadas eucariotas con C-H y ancla; columna inequívoca en el MSA de genes.
- Holozoa monofilético en el árbol de genes (0,999), C. elegans en la base; duplicados B8BXE3/A0A2K3DJ46.
- Mk reproducido exacto (q 0,110, raíz P 0,98, nodo D 0,94); código correcto.
- B2.1–B2.12 correctos.

Errado o parcial, no detectado por el ejecutor:
1. El ancla Glu-His no es invariante (NFS1: 19 D-H; NFS2: 1 D-H + 3 N-H).
2. El nodo "Holozoa" es Choanozoa (no hay Ichthyosporea/Filasterea; los hongos no tienen el gen): la ganancia está en el tallo Amorphea → Choanozoa.
3. El árbol de genes contradice al de especies más allá de C. elegans: Trypanosoma hermano de los holozoos (0,90), Acanthamoeba dentro de las algas (0,13), Salpingoeca dentro de Metazoa junto a Capitella (0,63). Hace falta declarar el supuesto de herencia vertical y hacer un test AU.
4. "Ramas iguales = conservador" es incorrecto. Con ramas realistas: raíz P 0,49–0,71; Amorphea 0,41–0,57; Choanozoa D 0,95–0,97. Con Acanthamoeba/Trypanosoma como posibles HGT, la raíz queda sin información; con Salpingoeca desconocido, Choanozoa queda D 0,49 / P 0,48.
5. El q = 0,025 no se reproduce (con 5 estados y q por ML ≈ 0,10); el árbol de especies no está depositado.
6. Lo más grave: la "predicción cumplida" de C. elegans contradice los datos propios. Pro aparece en ≥ 23 proteomas Sec_estricto (incluido O. lucimarinus 4/4); C. elegans conserva la maquinaria Sec para TrxR-1; Drosophila es el caso inverso.
7. Homología del Pro: el dipéptido P-A es compartido (Acanthamoeba, Trypanosoma, algas); C. elegans tiene P-S (reversión); el cambio es PA ↔ DS, hace falta el doble mutante.
8. Literatura que falta: Poliak 2009 FEBS J (SCL de T. brucei con Pro, RNAi); da Silva 2020 PLoS NTD.
9. La correlación estado del residuo ↔ Sec no es testeable (n efectivo = 1).
También: el Asp146 está en la interfaz del dímero (cadena B, residuos 284–287).

Afirmaciones excesivas que siguen en la bitácora: §10 "innovación holozoa de un solo paso"; §7 "predicción cumplida"; §9 posteriores sin la salvedad de las longitudes de rama; §11.4 "conservadora".

Prioridades: (1) ubicar las 11 C-H + 5 de Bolidophyceae y documentar la regla de `clase`; (2) sacar la "predicción cumplida" de C. elegans; (3) Choanozoa y tallo; (4) sensibilidad del ASR + árbol de especies depositado + test AU; (5) taxones baratos (Capsaspora, Sphaeroforma/Creolimax, Monosiga, Mnemiopsis, Thecamonas, Dictyostelium, otros nematodos, artrópodos con el gen, Naegleria, Euglena); (6) correcciones de texto; (7) barrido Sec y 5' de PABB004.
Camino: almost = 1–4 + 6; ready = además 5 y el barrido Sec. No hace falta trabajo de laboratorio si lo funcional se plantea como predicción.
