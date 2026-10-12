# Auto Review Loop — Dossier SCLY-like

- Run: run_20261012_8ed5232f
- Inicio: 2026-10-12T18:28Z
- Objeto: `PAPER TENTATIVO ### dossier_SCLY_like para leer ###.pdf` (texto extraído en `review-stage/paper_texto.txt`)
- MAX_ROUNDS = 4 · umbral de corte: score ≥ 6/10 **y** veredicto ∈ {ready, almost}
- **Revisor:** subagente de Claude dentro de la sesión (sin Codex/GPT ni APIs pagas).
  ⚠ Es un revisor de la **misma familia de modelos** que el ejecutor: la independencia NO está verificada.
  El skill original exige un revisor de otra familia; acá se adaptó por las restricciones del entorno.
- Datos crudos disponibles: sólo `scly_like_localizacion.csv` y `fig_localizacion_scly.png`. Sin red a UniProt/NCBI.
  Las correcciones posibles son de texto, de recálculo sobre el CSV y de verificación bibliográfica (PubMed).

## Ronda 1 (2026-10-12)

### Evaluación
- Score: **4/10** · Veredicto: **not ready**
- Críticas principales: "no es plastidial" contradicho por el CSV (13/60 con P(plástido)>0,5; el panel de control falla justo en plástido); conteos inconsistentes (65/66/67, 56/57 especies, 13 vs 14 estramenopilas); circularidad de la firma invariante; contradicción Ser/Thr/Ala en el bucle de NFS; falta Asp146; soportes SH-like presentados como bootstrap; test de tasas confundido por profundidad de clado (p = mínimo exacto con n=38); Spearman con posiciones no independientes; RNA-seq sobreafirmado (5' sin resolver, 2 vs 9 exones); "HISAT2/STAR sólo Linux" es falso.
- Respuesta completa del revisor: [`ronda1_revisor.md`](ronda1_revisor.md)

### Acciones
- Recalculados desde el CSV todos los números de localización, composición y bucle (`scripts/recalculo_localizacion.py` → `recalculo_localizacion.txt`). Los hallazgos del revisor se confirmaron con un recálculo independiente.
- Verificación bibliográfica vía PubMed: Asp146 (Collins et al. 2012), Cys375 rata (Omi et al. 2010), SCL de ratón citosólica (Mihara et al. 2000), mutantes Cys→Ala de CsdB/IscS (Mihara et al. 2000 J Biochem), SclA bacteriana (Johnstone et al. 2021).
- Redactado `DOSSIER_REVISADO.md`: definiciones de conjunto (§0), resumen reescrito, §2.6–2.15 corregidas, nuevo §6/§7/§8, y ajuste del §9. Lo que no se puede resolver sin los archivos del proyecto quedó marcado [PENDIENTE-DATOS] / [PENDIENTE-ANÁLISIS].
- Recálculo propio: con 4 discriminantes válidas, binomial P(4/4 | p=46/348) ≈ 3×10⁻⁴.

### Estado
- Sigue a la ronda 2.

## Ronda 2 (2026-10-12)

### Evaluación
- Score: **5/10** · Veredicto: **not ready**
- Todos los números del CSV y las 5 citas nuevas fueron verificados por el revisor de forma independiente.
- Problemas nuevos: test de enriquecimiento con base incorrecta y H462 circular (N1); secciones originales sin tocar que contradicen la revisión (N2); errores chicos en §2.10/§6 (N3); +1 de NFS2 pendiente pero usado (N4); circularidad ya resoluble por el propio texto (N5); sobrecorrección "subestiman plástido" (N6); marco de Asp146 contradictorio con Johnstone 2021 (N7); "sólido como topología" y 66/56 contra 65/55 (N8).
- Respuesta completa: [`ronda2_revisor.md`](ronda2_revisor.md)

### Acciones
- N1: test reformulado con base condicional; H462 excluido; §7 bajado a "Pendiente".
- N2: nueva sección "Secciones del original que quedan reemplazadas" con la §4 (tabla maestra) reescrita entera; §2.4/§5.1 "artefacto" pasa a "no interpretable"; §3 TargetP 3 fallos.
- N3: SP de *Chara*; 13/60 (22 %) y 10/31 (32 %); sin "prasinofitas y clorofíceas".
- N4/N5: §2.8 reescrita (la entropía sale como resultado; queda la tabla de contingencia como test).
- N6: localización "indeterminada".
- N7: Asp no conservado pasa a "no informativo".
- N8: hermano de humana "Provisorio"; §1.5 dice 65/55 (+HText = 66/56).
- Se agregó la nota de que la proteína curada no es localizable hasta resolver el 5'.

### Estado
- Sigue a la ronda 3.

## Ronda 3 (2026-10-12)

### Evaluación
- Score: **5/10** · Veredicto: **not ready**
- El revisor declara **saturado el trabajo sólo de texto**: el techo estimado es ~5,5–6/10. Lo que falta es evidencia nueva, no redacción.
- Respuesta completa: [`ronda3_revisor.md`](ronda3_revisor.md)

### Acciones (post-ronda 3)
- §2.10/§6/§7: conteo de controles corregido (2 plastidiales de algas verdes: DeepLoc 1/2, TargetP 0/2; DeepLoc además falla 1/3 mitocondriales). Se quitó "prasinofitas y clorofíceas"; ahora dice Chlorophyta con trebouxiofícea. (En la ronda 2 este cambio se había reportado como hecho y no lo estaba; quedó corregido acá.)
- §1.5: el 0,96 se atribuye al clado con la humana; 65/55 contra 66/56 condicionado a PABB004.
- §2.15, §5.2(c), §4: Chlorophyta 32→31/30; OR dentro de Chlorophyta a recalcular; pseudorreplicación "no demostrada, CMH pendiente".
- §9 reescrita entera; §10 "6 posiciones" → 4; encabezado y referencias D/N aclarados; set de "9/67 aberrantes" definido; recorte de la predicción 0,9477 identificado.

## Terminación

**El loop se detiene tras la ronda 3 (de 4) sin evaluación positiva.** Una cuarta ronda sin datos nuevos repetiría la misma nota: el revisor determinó que la mejora por texto está saturada.

Progresión: 4 → 5 → 5 (techo estimado por texto: ~6).

### Bloqueantes restantes y esfuerzo estimado
| # | Tarea | Tipo | Esfuerzo |
|---|---|---|---|
| 1 | Tabla de contingencia His +1 (bipartición del árbol vs NFS1/NFS2/301) | recálculo con archivos del proyecto | 1–2 h |
| 2 | Enriquecimiento con base condicional para G197/A232/T330 | recálculo | 1 h |
| 3 | Reconciliar conteos (65/66 en el árbol, 134/116 vs 124/110, 386/348, Drosophila, Chlorophyta 31/30) | recálculo | 2 h |
| 4 | CMH (y definir Sec+) sobre `sec_vs_scly_por_proteoma.csv` | recálculo | 1 h |
| 5 | Residuo equivalente a Asp146 en las 66 | análisis sobre el alineamiento existente | ½ día |
| 6 | Alineamiento ±8 alrededor de la Cys en los tres grupos | análisis | ½ día |
| 7 | IQ-TREE 2 (ModelFinder C20/C60, UFBoot2 + SH-aLRT), grupo externo = clase V no asignadas, más SCLY de eucariotas no algales, Zygnematophyceae | análisis | 1–2 días (cómputo local, sin costo) |
| 8 | HISAT2 + StringTie sobre SRR12973628 (5') | análisis | 1 día |
| 9 | tBLASTn genómico + sintenia en embriofitas/rodofitas/Zygnematophyceae | análisis | 2–3 días |
| 10 | Localización con ASAFind/HECTAR/PredAlgo + controles citosólicos, o pasarla a suplementaria como "no resuelta" | análisis o decisión | ½–1 día |

Con 1–7 resueltos, el revisor estima "almost" (~7). Para "ready" hacen falta además 8–10.

**Recomendación:** no seguir iterando sobre el texto. Hay que correr 1–4 (son recálculos sobre archivos que ya existen en el proyecto pero no se subieron a este repo) y 5–7. Después, relanzar el loop con esos resultados.

### Descripción del método (para figuras)
Pipeline: barrido phmmer de 10 cebos sobre 119 proteomas de referencia de UniProt → extracción PF00266 (hmmsearch) → FAMSA → filtro de ocupación 0,35 → VeryFastTree → asignación de clado y bucle catalítico. Rama genómica: diagnóstico del ORF quimérico (CD-Search, sintenia con NREL 46B-D3) → reparación manual del extremo 3' → validación por k-meros de unión en RNA-seq crudo. Rama estructural: modelos AlphaFold + transferencia de ligando desde 3A9Z/1KMK/1P3W con TM-align.

### Notas sobre el proceso
- **Revisor de la misma familia** (subagente de Claude): independencia no verificada; el skill original pide Codex/GPT. No se usó ninguna API paga.
- Pasos del skill omitidos por no aplicar o no estar disponibles: `/result-to-claim`, `/render-html`, notificación Feishu, trazas de `.aris/`.

---

## Ronda 4 (2026-10-12) — con los datos crudos del proyecto

El usuario dio acceso a los archivos del proyecto (Google Drive), que se copiaron en `datos/`. Antes de la ronda se recalculó todo con `scripts/recalculo_datos_proyecto.py` (salida en `recalculo_datos_proyecto.txt`) y se agregó la sección ★ R1–R8 al dossier.

### Evaluación
- Score: **6/10** · Veredicto: **not ready**. Pasa a "almost" cuando se ubiquen en el árbol las 11 secuencias de R2 y se apliquen los arreglos de texto.
- El revisor reprodujo de forma independiente todos los números R1–R8.
- Respuesta completa: [`ronda4_revisor.md`](ronda4_revisor.md)

### Acciones (post-ronda 4)
- R1: corregida la identidad de las 2 C-H con otro cebo (*Symbiodinium* + *Guillardia*); agregada la dirección 75/110; independencia rebajada a "aproximada".
- R2: rango de E-value corregido (10⁻³⁴–10⁻¹¹⁶) y hit débil identificado; exclusión descrita como probable error; agregados los 5 candidatos de Bolidophyceae sin His (`AAGSAC-E/D`).
- R3: gaps de NFS1/NFS2, H_L3 = 0,547 y la especulación marcada como tal.
- R4: fuentes aclaradas; contradicción con el informe del barrido señalada.
- R5: test sin H462 (3/5, p = 0,24) y reformulado como "con poca potencia".
- R6: reescrita. Dos barridos Sec inconsistentes; CMH con IC 0,45–3,52; en algas solas OR 2,87, p = 0,011 (verificado). Pseudorreplicación "no demostrada".
- R7: declarado el duplicado de la SCLY humana en el árbol; *Polarella* reclasificada.
- Definidos los tres "66" y el conteo de Chlorophyta.

## Terminación (ronda 4 de 4 — MAX_ROUNDS)

**El loop termina por llegar al máximo de rondas, sin evaluación positiva.** Progresión: **4 → 5 → 5 → 6**. La subida a 6 vino de evidencia nueva sacada de los datos crudos, no de redacción.

### Lo que falta, en orden
| # | Tarea | Para |
|---|---|---|
| 1 | Bajar de UniProt las 11 secuencias C-H excluidas y las 5 de Bolidophyceae; extraer PF00266, alinear y ubicarlas en el árbol; rehacer la tabla de distribución | almost |
| 2 | Documentar la regla que generó la columna `clase` (617 → 66) | almost |
| 3 | Decidir cuál de los dos barridos de marcadores Sec es el válido | almost |
| 4 | Sacar la SCLY humana duplicada; agregar SCLY de otros eucariotas y grupo externo; IQ-TREE con UFBoot/SH-aLRT | ready |
| 5 | HISAT2 + StringTie (5' de PABB004); tBLASTn + sintenia para las pérdidas (Zygnematophyceae) | ready |
| 6 | Marcador de selenoproteoma (SECIS / TGA) o declarar "no evaluado"; test de Pagel | ready |
| 7 | Predicción funcional: localización con predictores adecuados, o el argumento estructural Pro146 | ready |

### Notas
- Revisor de la misma familia de modelos (subagente de Claude); independencia no verificada. No se usó ninguna API paga.
- Pasos del skill omitidos: `/result-to-claim`, `/render-html`, Feishu, trazas `.aris/`.

---

## Ronda 5 (2026-10-12, extensión pedida por el usuario) — bloque determinante Se/S

Insumos: la bitácora `bitacora_determinante_SeS.md` y la carpeta `bloque_determinante_SeS` del Drive (copiadas en `datos/bloque_SeS/`).

### Evaluación
- Score: **6,5/10** · Veredicto: **not ready**
- Respuesta del revisor: [`ronda5_revisor.md`](ronda5_revisor.md)

### Acciones
- Verificados de forma independiente la estructura 3GZC, los conteos, las 32 llamadas eucariotas y el árbol de genes.
- Reconstrucción ancestral reimplementada con análisis de sensibilidad (`scripts/asr_determinante.py`).
- Nueva sección ★★ B1–B4 en el dossier:
  - B2: 12 correcciones;
  - B4: Choanozoa, sensibilidad, conflicto entre árbol de genes y de especies, retiro de la "predicción cumplida" de *C. elegans* (verificado: Pro en 32 de 47 proteomas que pasan `Sec_estricto`), ancla (E/D/N)-H, dipéptido PA ↔ DS, Poliak 2009 verificado en PubMed.

### Estado
Progresión: 4 → 5 → 5 → 6 → **6,5**.

Para llegar a "almost":
1. Ubicar en el árbol las 11 secuencias C-H y los 5 candidatos de Bolidophyceae, y documentar la regla de `clase`.
2. Aplicar las correcciones de texto a la bitácora.
3. Depositar el árbol de especies y hacer el test AU.

Para "ready", además:
- sumar los taxones holozoos basales y los nematodos;
- resolver el barrido Sec;
- resolver el extremo 5' de PABB004.

---

## Ronda 6 (2026-10-12) — ubicación de las 16 secuencias candidatas

### Evaluación
- Score: **7/10** · Veredicto: **not ready**, cerca de "almost".
- Respuesta del revisor: [`ronda6_revisor.md`](ronda6_revisor.md)

### Acciones
- Primer árbol ML completo del proyecto: IQ-TREE 2.3.6, Q.pfam+I+R9, UFBoot + SH-aLRT, 318 dominios.
- Las 15 secuencias ubicables caen dentro del clado SCLY-like; tabla de distribución rehecha (71/119).
- Aplicados los arreglos de texto 4–8 en ★★★ y la nota de precedencia. Corregido el script de lectura del árbol.
- Identificadas **30 secuencias más** con mejor cebo SCLY-like sin examinar; la principal es *Ectocarpus* D8LEU7, que probablemente da Phaeophyceae 1/1.

### Para "almost"
1. Ubicar las 30 (como mínimo D8LEU7 y las dos de *Durusdinium*). Hace falta su FASTA.
2. Aplicar la regla HMM + árbol a los 617.
3. Consolidar el dossier en una sola versión.

---

## Ronda 7 (2026-10-12) — 30 secuencias más y dossier consolidado

- Score: **8/10** · Veredicto: **almost**. Respuesta del revisor: [`ronda7_revisor.md`](ronda7_revisor.md)
- Filtradas las 30 secuencias: 21 sin dominio clase V; 6 ubicadas con IQ-TREE restringido; 3 fragmentos.
- Distribución final: **75/119**. Se suman Phaeophyceae 1/1 y *Tetrabaena* (por el fragmento ortólogo).
- Dossier consolidado: [`DOSSIER_SCLY_like_v2.md`](DOSSIER_SCLY_like_v2.md), con las correcciones 1–8 del revisor aplicadas.
- Pendientes para "ready": HMM sobre los 505 candidatos restantes (hace falta el FASTA de los 617), eucariotas en el árbol ML + test AU, barrido Sec, tBLASTn de las ausencias, 5' de PABB004.
