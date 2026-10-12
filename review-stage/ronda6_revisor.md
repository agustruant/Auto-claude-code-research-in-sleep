# Ronda 6 — respuesta del revisor (resumen fiel; subagente Claude, misma familia que el ejecutor)

Score: 7/10 · Verdict: not ready (cerca de almost).

Confirmado de forma independiente, sin volver a correr IQ-TREE:
- extracción de dominios (E ≤ 3e-22; 15 ≤ 4e-56; 10 ≤ 3,2e-110);
- HMM L3 en las 16 (margen 85–237 bits en las 15 ubicadas);
- split no enraizado de 82 hojas 95,8/99, sin depender de la raíz ({NFS1+IscS+L3} vs {NFS2+SufS} 100/100);
- 15/15 dentro del clado;
- subclados (Pelagophyceae 99,8/100; Monoraphidium+Raphidocelis 99,9/100; Nitzschia 100/100; Bolidophyceae 99,8/100);
- clado sólo algal 61,1/57;
- columna Asp146 (0 discrepancias con el MSA anterior); Pro en las 15; total del clado P 67 + HText, V 5, D 1, gap 8;
- exclusión de FWJ4 justificada (mismo locus que FZ61, deleción + corrimiento del marco);
- tabla 71/119;
- Fisher 2,68 / p 0,015; CMH 1,08 (0,35–3,33) p 0,90.

Correcciones:
- La quimera de Cladocopium está en la base del clado algal (hermana del núcleo de 79 hojas, 91,6/82), no "junto a prasinofitas" (artefacto del script).
- La salida II del script es un artefacto.
- Bolidophyceae son hermanas de las diatomeas (99,1/100): una sola pérdida de la His. Tienen las ramas más largas y Sec_estricto 0/6.
- El nodo de Phaeodactylum tiene como hermano un grupo de 7 pennadas rafídeas.

Problemas ordenados:
1. [NEW-ANALYSIS] Phaeophyceae 0/1 probablemente falso: Ectocarpus D8LEU7 con mejor cebo L3 (333 bits, E 3,6e-97, margen 129). Hay 30 "otro" con mejor cebo L3 sin examinar (Durusdinium ×2, Stephanodiscus, etc.).
2. [RECOMPUTE] Aplicar la regla HMM + árbol a los 617.
3. [TEXT] Afirmaciones viejas o contradictorias en todo el dossier: §0, §1, §4, §6, §7, §8, R1, R2, R4 (−6 en Bolidophyceae), R7.
4. [TEXT] U2.4 se excede: P 68/73 informativas, V 5; el desacople son dos eventos.
5. [TEXT] U2.5: el 0,855 no es comparable; el núcleo algal tiene 91,6/82.
6. [TEXT] CMH con sólo 3 estratos (62 proteomas); Breslow-Day 0,098.
7. [TEXT] Métodos del árbol (mset restringido, 650 parámetros, gaps, raíz); descripción de FWJ4.
8. [TEXT] Fuente del conteo de His; G-x-x-C no es diagnóstico.
9. Arrastrados: eucariotas en el árbol ML + test AU; barrido Sec; 5'; tBLASTn.

Camino:
- almost = ubicar D8LEU7 + Durusdinium, regla para los 617, consolidar el dossier;
- ready = además eucariotas en el árbol + AU, barrido Sec, tBLASTn.
