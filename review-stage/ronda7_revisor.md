# Ronda 7 — respuesta del revisor (resumen fiel; subagente Claude, misma familia que el ejecutor)

Score: 8/10 · Verdict: almost. Los puntos 1 y 3 de la ronda 6 están hechos; conteos y estadística se reproducen.

Confirmado:
- ubicaciones en iqfinal: Ectocarpus–Tribonema 87,6/81; Durusdinium dentro de los dinoflagelados; Stephanodiscus QSF5 dentro; Tetrabaena ZVZ7/ZID8 fuera (78,2/78);
- truncado de Ectocarpus, pérdida de la Cys en Stephanodiscus, corrimiento en Durusdinium;
- N_ALG 85 = 65 + 15 + 4 + HText; 73 proteomas algales (74/119);
- Fisher 2,61 / 0,022; CMH 1,41 (0,45–4,37) p 0,549, BD 0,125;
- His 0/250 NFS; ASR, localización y RNA-seq.

Problemas:
1. La interpretación de Tetrabaena está mal: el fragmento ZMY6 es el ortólogo (71 % con Gonium, Pro en 146); ZVZ7/ZID8 son una familia divergente propia de 5 copias (GVGGCAC). Contarla da 75/119, Chlorophyta 35/48, CMH 1,17 (0,37–3,70) p 0,78.
2. §1.4 y §3.3 listan a Tetrabaena como pérdida de His dentro del clado, lo que contradice §3.2.
3. Las etiquetas de iqfinal están mal descritas: los valores viejos están desplazados (el nodo sólo algal es 61,1/57, no 91,6/82) y los nuevos están inflados por la restricción. "86 hojas algales" debería ser 85 + humana.
4. El título del §8 exagera.
5. "Pro en 32 de 47 con Sec" no se reproduce; recalcular y aclarar que depende del barrido Sec en discusión.
6. Durusdinium RUF2 es una subcadena exacta de KTI6 (duplicado entre proteomas); los dos proteomas tienen Sec_estricto opuesto.
7. Detalles: bucle de Stephanodiscus `CSAGSISIL`; "84 + HText"; la localización cubre sólo a los originales; nota sobre la D de los fragmentos de Symbiodinium.
8. La regla para los 617 sigue abierta (cubre 112); las 505 restantes tienen como mejor cebo NFS y ninguna tiene C-H. No bloquea "almost" si se documenta; sí bloquea "ready".

Camino:
- almost: arreglos de texto 1–3, 5, 6 y resumen de las 505.
- ready: HMM sobre las 505, eucariotas + AU, barrido Sec, tBLASTn, 5' de PABB004.
