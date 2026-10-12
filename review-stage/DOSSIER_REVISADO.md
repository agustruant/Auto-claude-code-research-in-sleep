# Dossier SCLY-like — versión revisada (auto-review loop, rondas 1–4)

Este archivo **no reemplaza** al PDF original: reescribe las secciones que la revisión encontró incorrectas o sobreafirmadas. Lo que no aparece acá queda como en el original. Cada cambio remite a la debilidad numerada en la revisión de la ronda 1 (`ronda1_revisor.md`, puntos 1–12 = D1–D12) o de la ronda 2 (`ronda2_revisor.md`, N1–N8).

Etiquetas:
- **[CORREGIDO]**: corregido con datos que ya existen (CSV o bibliografía verificada).
- **[REFORMULADO]**: la afirmación se rebajó a lo que los datos sostienen.
- **[PENDIENTE-DATOS]**: requiere archivos que no están en el repo (árbol, alineamientos, conteos). Hay que verificarlo contra esos archivos antes de escribir el paper.
- **[PENDIENTE-ANÁLISIS]**: hace falta correr un análisis nuevo.

Los recálculos sobre el CSV están en `review-stage/recalculo_localizacion.txt` y salen de `review-stage/scripts/recalculo_localizacion.py`.

## ★ Resultados con los datos del proyecto (ronda 4)

Fuente: archivos del Drive (`candidatos_desulfurasas.csv`, `arbol_desulfurasas.nwk`, `msa_desulfurasas_trim.fasta`, `dominios_desulfurasas.fasta`, `conservacion_scly_por_posicion.csv`, `sec_vs_scly_por_proteoma.csv`, `tasas_relativas_pareadas.csv` y tablas chicas), copiados en `review-stage/datos/`. Script: `scripts/recalculo_datos_proyecto.py`. Salida completa: `recalculo_datos_proyecto.txt`. **Donde esta sección contradice al resto del documento, vale esta sección.**

### R1. La His en +1 es diagnóstica, de forma independiente del bucle

- Sobre los 617 candidatos:
  - SCLY-like: 66/66 con C-H;
  - NFS1: 0/134 (Thr en +1 en el 100 %);
  - NFS2: 0/116;
  - "otro": 11/301.
- **Asignación por mejor cebo** (score phmmer contra cebos de cada familia, sin mirar el bucle), contra His en +1:
  - de las 77 secuencias con C-H, 75 tienen como mejor cebo uno SCLY-like; las 2 restantes son las quimeras largas de dinoflagelados;
  - de las 507 cuyo mejor cebo es NFS1 o NFS2, sólo 2 tienen C-H.

  Los dos criterios coinciden casi por completo. La His es un carácter diagnóstico real, no un artefacto de cómo se definió el grupo.
- El clasificador automático de bucles del propio CSV (`clase_loop`) etiquetó 58 de las 66 SCLY-like como "I IscS/NFS1". La asignación final, entonces, **no** salió de ese clasificador. Hay que documentar en Métodos qué regla produjo la columna `clase`.

### R2. ⚠ Once secuencias con firma SCLY-like quedaron afuera del clado

Son 11 secuencias de "otro" con C-H, mejor cebo SCLY-like (E-value entre 10⁻⁹² y 10⁻¹¹⁶), longitudes normales (370–501 aa, salvo una quimera de *Cladocopium* de 2654 aa) y Cys catalítica en posición normal. Son indistinguibles de las 66 y no están en el árbol:

| Especie | Linaje | Accesión |
|---|---|---|
| *Monoraphidium neglectum* | Chlorophyta | A0A0D2N0J3 |
| *Raphidocelis subcapitata* | Chlorophyta | A0A2V0PAY6 |
| *Phaeodactylum tricornutum* | Bacillariophyta | B7G8F0 |
| *Nitzschia inconspicua* (2) | Bacillariophyta | A0A9K3KRJ2, A0A9K3LVN3 |
| *Aureococcus anophagefferens* (3, 2 proteomas) | **Pelagophyceae** | F0XXL4, A0ABR1FZ61, A0ABR1FWJ4 |
| *Pelagomonas calceolata* | **Pelagophyceae** | A0A8J2WTZ1 |
| *Chrysophaeum taylorii* | **Pelagophyceae** | A0AAD7XJ29 |
| *Cladocopium goreaui* | Dinophyceae | A0A9P1FCD2 (quimera) |

Si se confirman, cambia la distribución:
- **Pelagophyceae pasa de 0/4 a 4/4 proteomas.** La "ausencia en estramenopilas no diatomeas" se reduce a Bolidophyceae (0/6), Eustigmatophyceae (0/2) y Phaeophyceae (0/1).
- Bacillariophyta pasa de 14/16 a **16/16**.
- Chlorophyta pasa de 32/48 a **34/48** proteomas.

Embryophyta y Rhodophyta siguen en 0: ningún candidato de esos linajes tiene C-H.

**Antes de escribir:** hay que bajar las 11 secuencias de UniProt, extraer el dominio, agregarlas al alineamiento y verificar que caigan dentro del clado. Es la verificación más urgente de todo el proyecto, porque toca la tabla de distribución y una afirmación de ausencia.

### R3. Asp146 no se conserva en el clado algal

Numeración verificada sobre la secuencia humana del propio dominio: H145, **D146**, K259 (Lys del PLP), C388 (Cys catalítica), H389 (His diagnóstica).

| Grupo | Residuo en la posición de Asp146 (MSA) |
|---|---|
| SCLY humana | **Asp** |
| SCLY-like algales | **Pro 52**, Val 5 (4 dinoflagelados + *Guillardia*), gap 8 |
| NFS1 | Lys 113, Arg 1 |
| NFS2 | His 106 |

- Asp146 es el residuo que da a la SCL humana su especificidad por Sec (Collins et al. 2012, [doi:10.1371/journal.pone.0030581](https://doi.org/10.1371/journal.pone.0030581)). Ninguna secuencia algal lo tiene: en su lugar hay una Pro conservada. Coincide con la tabla de conservación (posición 231 del modelo HText: Pro, f = 0,90).
- **Interpretación:** sigue siendo un dato *no informativo* sobre la especificidad, porque la SclA bacteriana prefiere Sec con His en esa posición (Johnstone et al. 2021, [doi:10.1016/j.biochi.2021.01.002](https://doi.org/10.1016/j.biochi.2021.01.002)). Pero es una **divergencia clara respecto de la SCLY de mamífero** en el residuo funcional mejor caracterizado.
- Refuerza que el clado se presente como "relacionado con SCLY" y no como "selenocisteína liasas algales". Es también una predicción comprobable: la Pro conservada hace al clado algal mecanísticamente distinto de la SCLY animal.

### R4. Bucle catalítico de los tres grupos (alineamiento real)

| Posición respecto de la Cys | −5 | −4 | −3 | −2 | −1 | **0** | **+1** | +2 |
|---|---|---|---|---|---|---|---|---|
| NFS1 (124) | S | S | G | S | A | C | **T** (100 %) | S |
| NFS2 (110) | R | S/A | G | H | H | C | **T 58 / A 32 / C 19** | Q |
| SCLY-like (66) | S | A | G | A/S | A | C | **H** (100 %) | S |

- El +1 de NFS2 **no** es "Thr 100 %" ni "Ser": es variable.
- En NFS2 hay His en −2 y −1. La exclusividad de SCLY-like es una **His en +1**.
- El −6 también distingue: Ala/Cys en SCLY-like, Val/Ile en NFS1 y NFS2.

### R5. Posiciones discriminantes: el enriquecimiento cerca del cofactor no se sostiene

Con la definición del propio dossier (conservada en las dos familias, H ≤ 0,5, con consenso distinto):

| Comparación | Conservadas en todas | A < 8 Å (base) | Discriminantes | A < 8 Å | Binomial |
|---|---|---|---|---|---|
| SCLY vs NFS1 **y** NFS2 | 38 | 15 (39,5 %) | **2** (S159, G197) | 1 | p = 0,63 |
| SCLY vs NFS1 | 65 | 23 (35,4 %) | 6 (S159, G197, A232, T330, N431, H462) | 4 | p = 0,12 |

- Las "6 posiciones discriminantes" del dossier son discriminantes **sólo contra NFS1**. Contra NFS2, A232, T330, N431 y H462 no están conservadas (H_II = 0,77–1,47).
- Con la base correcta, **no hay enriquecimiento significativo** cerca del cofactor. Esa afirmación sale del paper.
- S159 sí es discriminante contra las dos familias (en la tabla original figuraba "—").

### R6. Asociación con la maquinaria Sec: CMH confirma la pseudorreplicación

- "Sec+" en el CSV (`Sec_estricto`) = PSTK **y** SEPSECS **y** EEFSEC. Depende de PSTK, que se detecta mal.
- Fisher global: OR = 3,36, p = 0,0018 (se reproduce).
- **Cochran-Mantel-Haenszel por linaje** (4 estratos informativos: diatomeas, Chlorophyta, dinoflagelados, haptofitas): **OR_MH = 1,26, p = 0,65**.
- La asociación desaparece al controlar por linaje. La lectura de pseudorreplicación del dossier original era correcta: ahora tiene el test que la respalda.

### R7. Árbol y conteos reconciliados

- El árbol tiene **304 hojas**, no 617: 124 NFS1 + 110 NFS2 + 66 SCLY-like (65 algales del barrido + la humana del barrido) + 4 referencias (IscS, SufS, SCLY humana, HText).
  - Las 301 "otro" no están en el árbol.
  - Faltan 16 NFS1/NFS2 de proteomas de contraste (*Drosophila*, *Marchantia*, maíz, arroz, *Selaginella*, *Dictyostelium*, *Plasmodium*, *Tetrahymena*, *Polarella*). Eso explica 134/116 en el CSV contra 124/110 en el árbol y en la conservación.
  - **Corregir "árbol de 617 secuencias"** en el texto y en la figura.
- **Las hojas ya llevaban la etiqueta de clase** (prefijos `I__`, `II__`, `L3__`). El árbol se hizo *después* de asignar, así que es una verificación de monofilia, no un descubrimiento ciego.
- **Soportes SH-like:**
  - clado con SCLY humana + HText (68 hojas): 0,965;
  - **clado sólo algal + HText (66 hojas): 0,855**;
  - la SCLY humana es efectivamente hermana del grupo algal.
- **PABB004 no está entre los 119 proteomas.** El barrido da **65 SCLY-like algales**. Chlorophyta: **32/48 proteomas = 30/44 especies** (hay especies con 2 proteomas). Los "32/48" del dossier eran proteomas, no especies, y no incluían PABB004.
- *Drosophila*: 0 SCLY-like. Coincide con que los insectos no tienen SCLY reportada, pero no lo verifiqué en la literatura.

### R8. Tasas relativas

Se reproduce lo del dossier: 38/38 pares con SCLY > NFS1 y 38/38 con NFS2 > NFS1 (p = 7,3 × 10⁻¹², el mínimo exacto). SCLY contra NFS2: 17/38, p = 0,12. Las objeciones metodológicas del §2.14 siguen en pie.

### Cómo cambian las afirmaciones

| Afirmación | Antes | Ahora |
|---|---|---|
| His en +1 diagnóstica | Pendiente / circular | **Sólido**: concuerda 75/77 con la asignación por cebo; 0/250 NFS con C-H |
| Clado hermano de SCLY humana | Provisorio | Topología confirmada en el árbol; soporte sólo-algal 0,855 (SH). Sigue faltando muestreo eucariota y grupo externo |
| Ausente en Pelagophyceae | Dato | **Probablemente falso**: 4/4 proteomas con candidatos C-H. Verificar |
| Diatomeas 14/16 | Dato | Probablemente 16/16 |
| Asp146 | Sin analizar | **Pro conservada en algas; Asp sólo en humana** |
| Discriminantes cerca del cofactor | Pendiente | **Retirado**: p = 0,12–0,63 con la base correcta |
| SCLY ↔ Sec es pseudorreplicación | No demostrada | **Apoyado**: CMH OR 1,26, p = 0,65 |
| Árbol de 617 | Dato | **Falso**: 304 hojas, ya etiquetadas |

---

## Secciones del original que quedan reemplazadas (ronda 2)

Estas partes del PDF original contradicen la revisión y **no deben usarse** tal como están:

- **§2.4 y §5.1** — "sólo 2 de 61 plastidiales, mediana 0,13" y la predicción plastidial de HText (0,9477) como "artefacto". Se reemplaza por: *"predicción no interpretable: los límites de la secuencia eran inciertos"*. No se puede afirmar que fuera un artefacto, porque en Chlorophyta 10/31 SCLY-like completas tienen P(plástido) > 0,5 (§2.10).
- **§2.6 (tabla) y §2.12** — "grupo III" y "SAGxACH". Se reemplazan por "clado SCLY-like" y "G-x-x-C-H" (§2.6 revisada).
- **§2.7** — "1000 réplicas", "mismo resultado que RAxML/IQ-TREE". Ver §2.7 revisada.
- **§3 (tabla de herramientas)** — "TargetP falló los dos controles de PABB004". En realidad falló 3: NFS2_PABB (OTHER), NFS1_PABB (OTHER) y NFS2 de *C. reinhardtii* (mTP). "DeepLoc falló 2 de 7" se mantiene.
- **§4 (tabla maestra)** — reemplazada por la tabla de abajo.
- **§2.14 (tabla)** — se saca la etiqueta "(citosólico)".
- **§2.4, nota de recortes** — la predicción 0,9477 se hizo sobre el recorte del modelo de AlphaFold (aa 1811–2288 del ORF), no sobre el recorte del CSV (aa 1900–2400, que además se pasa ~100 aa del stop real). Hay que nombrar el recorte cada vez que se cite.
- **§2.15 y §5.2(c)** — usan 32 Chlorophyta con SCLY-like (18+14 en la tabla de contingencia; "32/48 = 67 %"). Con la corrección del §0 son 31/48 (65 %) o 30/48 (63 %). Hay que recalcular el OR dentro de Chlorophyta desde `sec_vs_scly_por_proteoma.csv`. "Desaparece al controlar por linaje" se apoya en un solo estrato (Chlorophyta) de baja potencia, mientras que diatomeas (OR 3,67) va en la dirección global. Pasa a *"no demostrada; CMH pendiente"*.
- **§9 completo** — "tercer clado", "firma diagnóstica invariante", "dos pérdidas independientes", "GBE si se incluye … pérdidas independientes y tasas", la figura de conservación con 6 posiciones y las referencias a "puntos 1 y 2 / punto 3 de §8" (numeración vieja). Se reemplaza por la §9 de abajo.
- **§10** — "las 6 posiciones discriminantes" pasa a 4 (y H462 pendiente).

### §4 — Tabla maestra (reemplazo)

| Dato | Valor |
|---|---|
| Proteomas barridos | 119 (107 algales + 12 de contraste) |
| Secuencias en el universo | 2.110.345 |
| Clase V recuperadas | 617 |
| Columnas retenidas | 386 de 768 (ocupación ≥ 0,35) |
| Clados (soporte SH-like local, VeryFastTree) | NFS2 116 (1,00) · NFS1 134 (0,79) · SCLY-like incl. humana (0,96) |
| SCLY-like algales | 65 en 55 especies del barrido; 66 en 56 con HText (§0) |
| Residuos invariantes del bucle | G, C, H en 66/66 (descriptivo; circular, §2.8) |
| Longitud mediana | 438 aa (IQR 410–470); 9/67 aberrantes (sobre S_tot, incluye la humana y el recorte HText de 501 aa) |
| Localización (algales con N-terminal fiable) | n = 60; mediana P(plástido) 0,14; 13/60 > 0,5 (Chlorophyta 10/31) |
| Panel de control | DeepLoc 5/7; DeepLoc + TargetP 4/7; plastidiales de algas verdes: DeepLoc 1/2, TargetP 0/2 |
| TM-score núcleo HText vs SCLY / IscS / SufS | 0,948 / 0,911 / 0,871 |
| Posiciones discriminantes | 4 (G197, A232, T330, H462); H462 pendiente de +1 en NFS2; test de enriquecimiento pendiente |
| Spearman conservación–distancia | ρ = −0,54 (sin p: posiciones no independientes) |
| RNA-seq | 21.890.509 lecturas de SRR12973628; intrón curado 29; unión automática 0 (excluye isoforma > ~10 %) |
| Proteína curada PABB004 | 421 aa (parcial, 5' sin resolver); K234, C360, H361 |
| Distancias raíz-hoja | NFS1 < NFS2 ≈ SCLY (descriptivo; Wilcoxon no válido, §2.14) |
| SCLY ↔ Sec | global OR 3,36 (p 0,0018); dentro de Chlorophyta OR 1,00 (calculado con 32 SCLY+, a recalcular con 31 o 30); diatomeas OR 3,67 (p 0,45). Pseudorreplicación **no demostrada**: CMH pendiente |

### Localización de la proteína curada

El CSV usa el recorte HText (aa 1900–2400 del ORF quimérico), no la proteína curada de 421 aa. A la curada le faltan ~60 residuos N-terminales, que es justo donde estaría el péptido de tránsito, así que **no se puede predecir su localización** hasta resolver el 5'. Correrla con el N-terminal incompleto repetiría el error del §2.4.

---

## 0. Definiciones de conjunto (nuevo, D2)

La versión anterior usaba 65, 66 y 67 para conjuntos distintos sin decir cuál era cuál. De acá en adelante:

| Símbolo | Definición | n |
|---|---|---|
| **S_alg** | SCLY-like algales del barrido + HText (PABB004) | 66 secuencias, 56 especies |
| **S_tot** | S_alg + SCLY humana (Q96I15) | 67 |
| **S_loc** | S_alg con extremo N-terminal fiable (excluye 3 fragmentos, 2 quimeras de dinoflagelados y el recorte HText) | 60 |
| **S_bucle** | Secuencias con el bucle de 14 posiciones extraído en el CSV | 66 = 65 algales + humana (falta HText en el CSV; su bucle, LAASAGAACHSTGGPSVS, está en §2.6 y también lleva C-H) |

**[PENDIENTE-DATOS]** HText es un recorte manual, no una entrada de proteoma de referencia. Hay que confirmar si Scenedesmus sp. PABB004 está entre los 119 proteomas. Si no está, no puede contar en el "x/48" de Chlorophyta, y el conteo del barrido queda en 65 secuencias / 55 especies.

Composición de S_alg recalculada del CSV:

| Linaje | Secuencias | Especies |
|---|---|---|
| Chlorophyta | 34 | 31 |
| Bacillariophyta | 19 | 14 |
| Dinophyceae | 4 | 4 |
| Haptophyta | 4 | 3 |
| Streptophyta no embriofitas (Chara, Klebsormidium) | 2 | 2 |
| Cryptophyceae | 2 | 1 |
| Xanthophyceae | 1 | 1 |
| **Total** | **66** | **56** |

**[CORREGIDO]** La tabla del §2.9 decía Chlorophyta 32/48. El CSV tiene 31 especies, así que los numeradores sumaban 57 y no 56. Lo correcto es **31/48** si PABB004 está en el barrido, o **30/48** si no está.

**[CORREGIDO]** El §1 decía "14 proteomas de estramenopilas no diatomeas". Los ausentes son Bolidophyceae 6 + Pelagophyceae 4 + Eustigmatophyceae 2 + Phaeophyceae 1 = **13**. Xanthophyceae (1) es estramenopila no diatomea pero *tiene* el gen.

**[PENDIENTE-DATOS]** Hay tres tamaños que no coinciden entre secciones y hay que explicarlos o unificarlos:
- clados NFS1/NFS2: 134/116 en el árbol (§2.7) contra 124/110 en la conservación (§2.12);
- posiciones del alineamiento: 386 (§2.7), 348 (§2.12) y 353 (tabla descartada);
- Drosophila estaba en el set de contraste, pero su resultado no aparece en la fila de ausencias del §2.9. Hay que reportarlo.

---

## 1. Resumen ejecutivo (reescrito)

1. El cebo PNW80545.1 de *Chlamydomonas reinhardtii*, anotado "NFS2" en AlgaePath, no es NFS2. Pertenece a un clado de aminotransferasas clase V distinto de NFS1 (ISC) y de NFS2 (SUF), relacionado con la selenocisteína liasa (SCLY) animal.
2. En todas las secuencias de ese clado hay una **His inmediatamente después de la Cys catalítica** (motivo **G-x-x-C-H**). En IscS (grupo I) esa posición es Thr. **[PENDIENTE-DATOS]** En SufS/CsdB (grupo II) hay que confirmar el residuo en el alineamiento: la versión previa decía Ser en §1 y Thr en §2.12, y no puede ser ambas cosas. Ver §2.6.
3. *Scenedesmus* sp. PABB004 tiene NFS1 (KAF8057853.1), NFS2 (KAF8071197.1) y un gen SCLY-like que estaba oculto en un ORF quimérico de 3383 aa (KAF8071094.1).
4. El extremo 3' del modelo curado (último intrón y los 39 codones C-terminales recuperados) está respaldado por lecturas de RNA-seq de la propia cepa. Hay 29 lecturas que cruzan el intrón curado y 0 que soportan la unión del modelo automático. El extremo 5' sigue sin resolver.
5. El barrido sobre 119 proteomas de referencia (2.110.345 secuencias) recupera 65 secuencias SCLY-like en 55 especies si PABB004 no está entre los 119 proteomas, o 66 en 56 si está (pendiente, ver §0). Junto con la SCLY humana forman un clado con soporte SH-like 0,96. No se reportó el soporte del clado sólo-algal.
6. El clado no se detecta en los proteomas de referencia de 6 embriofitas, 12 rodofitas y 13 estramenopilas no diatomeas.
7. Gly, Cys e His del motivo G-x-x-C-H están conservadas en las 66 secuencias con bucle. La tabla de herramientas del original declara que el bucle fue el **criterio primario de asignación**, así que la invariancia es circular hasta que se demuestre lo contrario (§2.8).

**Titular defendible:** primera descripción sistemática de un clado de cisteína desulfurasas relacionado con SCLY en algas, con un caso de reparación de un modelo génico quimérico respaldado por RNA-seq.

**Lo que no se puede decir:**
- que es una familia nueva;
- que actúa sobre selenocisteína;
- que es el *ortólogo* de SCLY en sentido estricto (todavía falta muestreo de otros eucariotas, §2.7);
- que no es plastidial (§2.10).

---

## 2.6 — Bucle catalítico (correcciones)

**[REFORMULADO] Nomenclatura (D4).** "Grupo III" choca con la nomenclatura de grupos I/II de Mihara y Esaki. En la literatura, la SCL de mamífero se describió como "distantly related in primary structure to NifS" (Mihara et al. 2000, J Biol Chem 275:6195, [doi:10.1074/jbc.275.9.6195](https://doi.org/10.1074/jbc.275.9.6195)). La propuesta es llamar al grupo **"clado SCLY-like"** y no numerarlo. **[PENDIENTE-ANÁLISIS]** Hay que verificar en la literatura de grupos I/II (Mihara & Esaki 2002, Appl Microbiol Biotechnol) si SCLY ya fue asignada a alguno de los dos grupos. Si está en el grupo I, el texto lo tiene que decir.

**[CORREGIDO] Firma.** La firma invariante es **G-x-x-C-H**, no SAGxACH. Recalculado sobre S_bucle (66):

| Posición del bucle | Residuo | Frecuencia |
|---|---|---|
| 2 | S | 63/66 |
| 3 | A | 61/66 |
| 4 | **G** | **66/66** |
| 5 | A / S | 49 / 17 |
| 6 | A | 64/66 |
| 7 | **C** | **66/66** |
| 8 | **H** | **66/66** |

"SAGxACH" vale como consenso, no como firma invariante.

**[PENDIENTE-DATOS] Residuo equivalente en NFS1/NFS2.**
- La tabla del §2.6 da para el grupo II el motivo R-x-G-H-H-C. Eso pone una His *antes* de la Cys, así que la His en sí no es exclusiva de SCLY: lo diagnóstico es la **posición +1** respecto de la Cys.
- §1 y §2.12 se contradicen sobre el residuo en +1 en NFS1/NFS2 (Ser/Thr contra "Thr 100 %"). Hay que mostrar el alineamiento de los tres grupos alrededor de la Cys (±8 posiciones) como figura o tabla suplementaria, y corregir el texto según lo que diga ese alineamiento.
- El revisor recuerda que en SufS/CsdB el +1 es Ala ("…HHCA…"). No está verificado.

**[CORREGIDO] Literatura funcional que faltaba (D4).**
- **Asp146 de la SCL humana** es el residuo que da la especificidad por Sec. La variante D146K pierde esa especificidad y gana actividad cisteína desulfurasa (Collins et al. 2012, PLoS One 7:e30581, [doi:10.1371/journal.pone.0030581](https://doi.org/10.1371/journal.pone.0030581)).
- **Cys375 de la SCL de rata**, en el bucle flexible, forma el intermediario selenopersulfuro y orienta la Sec, pero no la Cys (Omi et al. 2010, J Biol Chem 285:12133, [doi:10.1074/jbc.M109.084475](https://doi.org/10.1074/jbc.M109.084475)).
- **[PENDIENTE-ANÁLISIS]** El dossier tiene que reportar qué residuo ocupa la posición equivalente a Asp146 en las 66 SCLY-like algales. Si está conservado como Asp, es el argumento estructural más fuerte a favor de especificidad por Sec. Si no es Asp, el dato **no es informativo** en ninguna dirección: la SclA bacteriana tiene His en esa posición y aun así prefiere Sec (Johnstone et al. 2021). Hay que reportarlo en los dos casos; hoy no se menciona.
- En la bacteria *Enterococcus faecalis* (SclA), el residuo análogo (His100) **no** es necesario para la especificidad (Johnstone et al. 2021, Biochimie 182:166, [doi:10.1016/j.biochi.2021.01.002](https://doi.org/10.1016/j.biochi.2021.01.002)). El mecanismo de discriminación no es universal.
- Las mutantes Cys→Ala de CSD, CsdB e IscS pierden casi toda la actividad sobre Cys, pero mucho menos sobre Sec (Mihara et al. 2000, J Biochem 127:559, [doi:10.1093/oxfordjournals.jbchem.a022641](https://doi.org/10.1093/oxfordjournals.jbchem.a022641)). Ojo: en la SCL de rata, en cambio, la Cys375 sí es esencial (Omi et al. 2010). En las NifS-like bacterianas, entonces, la competencia geométrica de la Cys para atacar al Se (§2.11) no predice especificidad por Sec.
- El subsitio "Asn25 de rata" del §2.11 se mantiene como observación, pero subordinado a Asp146.

---

## 2.7 — Árbol (correcciones de texto, D5, D6)

**[CORREGIDO]**
- VeryFastTree, como FastTree, da **soportes locales SH-like** calculados con 1000 remuestreos. **No son réplicas de bootstrap.** Reemplazar "1000 réplicas de soporte" por "soporte SH-like local (1000 remuestreos)".
- Reemplazar "LG+Γ" por "LG con aproximación CAT y reescalado Γ (20 categorías)".

**[REFORMULADO]** Se elimina "da el mismo resultado que RAxML/IQ-TREE", porque no se corrió. Hasta que se corra:
- "El clado SCLY-like recibe soporte SH-like 0,96 en un árbol aproximado de máxima verosimilitud."
- El enraizamiento en el grupo II es arbitrario. Hay que decirlo, o enraizar con las 301 clase V no asignadas como grupo externo.

**[REFORMULADO] Ortología (D5).** "Es el ortólogo algal de SCLY — blindado" pasa a: *"forma un clado con la SCLY humana como rama hermana. La relación de ortología con SCLY de metazoos requiere muestreo de otros eucariotas."*

El TM-score 0,99 entre el modelo de SCLY humana y el cristal de rata (3A9Z) es trivial: son ortólogos de mamífero. No dice nada del clado algal y **sale como argumento de ortología**. El que sí aporta es el del núcleo de HText contra SCLY (0,948), comparado con IscS (0,911) y SufS (0,871). Con la salvedad del §2.6, la diferencia es chica y TM-score no discrimina bien dentro del plegamiento.

**[PENDIENTE-ANÁLISIS]** Prioridad alta y barato:
- IQ-TREE 2 con ModelFinder (incluir LG+C20/C60), UFBoot2 + SH-aLRT;
- grupo externo = clase V no asignadas;
- más SCLY de metazoos (Drosophila, *Nematostella*, *Capsaspora*) y de otros eucariotas;
- sensibilidad al filtro de ocupación (0,25 / 0,35 / 0,5).

---

## 2.8 — Firma invariante (reformulado, D3; actualizado en la ronda 2)

**[REFORMULADO]** La tabla de herramientas del original (§3) dice: "Bucle catalítico — criterio primario de asignación de familia". Entonces la entropía 0,000 en la His es **verdadera por construcción** y **se saca como resultado**. Queda como dato descriptivo: G, C e H conservadas en las 66 secuencias con bucle.

Lo publicable es la prueba **independiente** del bucle:

| | His en +1 | Otra en +1 |
|---|---|---|
| Clado SCLY-like **definido sólo por la bipartición del árbol** | ? | ? |
| NFS1 + NFS2 + 301 no asignadas | ? | ? |

**[PENDIENTE-DATOS]** Sale de `candidatos_desulfurasas.csv` + el árbol. Si da ~66/0 contra ~0/551, la His es diagnóstica sin circularidad.

Se elimina "ni una sola sustitución en mil millones de años": es retórica.

## 2.9 — Distribución y pérdidas (correcciones, D2, D10)

**[CORREGIDO]** Tabla con Chlorophyta 31/48 (o 30/48, §0). Agregar fila de Metazoa con el resultado de Drosophila.

**[REFORMULADO] "Siete linajes".** Mezcla rangos: Bacillariophyta y Xanthophyceae son ambas Ochrophyta, y "carofitas" es parafilético. Hay dos opciones:
- presentar los grupos sin numerarlos como "linajes";
- agruparlos en supergrupos (Archaeplastida, Stramenopila, Alveolata, Haptista, Cryptista) y decir "presente en cinco supergrupos eucariotas".

**[REFORMULADO] Pérdidas.**
- "En la terrestrialización" requiere muestrear **Zygnematophyceae**, el grupo hermano de las embriofitas (*Mesotaenium*, *Spirogloea*, *Penium*, *Zygnema*). Con Chara y Klebsormidium sólo se puede decir: *"perdido en el linaje de las embriofitas después de su divergencia de Klebsormidiophyceae/Charophyceae"*.
- "Pérdida independiente en rodofitas" supone que el ancestro de Archaeplastida tenía el gen. No hay glaucofitas en el muestreo. Hasta reconstruir el estado ancestral, decir *"ausente en rodofitas"* y no "pérdida independiente".
- §9 y §7 tienen que coincidir: es "parcial", no un activo cerrado del paper.

---

## 2.10 — Localización subcelular (reescrito, D1)

**[CORREGIDO]** Recalculado sobre S_loc (60 algales, sin la humana). La versión previa contaba la SCLY humana entre "las 61".

Etiqueta DeepLoc completa (la tabla previa sumaba 55 y omitía 6):

| Etiqueta | n |
|---|---|
| Citoplasma | 24 |
| Mitocondria | 15 |
| Citoplasma + mitocondria | 13 |
| Mitocondria + plástido | 3 |
| Plástido | 2 |
| Citoplasma + mitocondria + plástido | 2 |
| Extracelular | 1 |
| **Total** | **60** |

- Con "Plastid" en la etiqueta: **7/60**, no 2.
- Con P(plástido) > 0,5: **13/60 (22 %)**. Por linaje: Chlorophyta **10/31**, Bacillariophyta 1/18, Haptophyta 1/4, Streptophyta 1/2, resto 0.
- Los casos altos son de Chlorophyta (prasinofitas, clorofíceas y una trebouxiofícea): *Chloropicon* 0,96, *Elliptochloris* 0,93 (TargetP cTP), *Cymbomonas* 0,86 (cTP), *Ostreococcus* 0,78, *Micromonas* 0,76, *C. eustigma* 0,74, y el propio PNW80545/A0A2K3DJ46 de *C. reinhardtii* con 0,52.

Medianas: citoplasma 0,65 · mitocondria 0,64 · plástido 0,14 · RE 0,17.

TargetP: 47 OTHER, 5 SP, 4 mTP, 4 cTP. SignalP: 59/60 sin péptido señal. DeepTMHMM: 0 hélices TM.

**[CORREGIDO] Panel de control.** El CSV tiene 6 controles. El séptimo es la SCLY humana, que DeepLoc predice citoplasma (0,79), lo que concuerda con la SCL de ratón citosólica (Mihara et al. 2000, J Biol Chem, [doi:10.1074/jbc.275.9.6195](https://doi.org/10.1074/jbc.275.9.6195)).

| Control | Destino real | DeepLoc | TargetP |
|---|---|---|---|
| NFS2 *A. thaliana* (Q93WX6) | plástido | ✔ plástido | ✔ cTP |
| NFS2 PABB004 | plástido | ✔ plástido | ✘ OTHER |
| NFS2 *C. reinhardtii* (A0A2K3D4F5) | plástido | ✘ mitocondria 0,93 | ✘ mTP |
| NFS1 *A. thaliana* (O49543) | mitocondria | ✔ | ✔ mTP |
| NFS1 *C. reinhardtii* (A0A2K3E3W0) | mitocondria | ✔ | ✔ mTP |
| NFS1 PABB004 | mitocondria | ✘ citoplasma 0,84 | ✘ OTHER |
| SCLY humana (Q96I15) | citosol | ✔ | ✔ OTHER |

- DeepLoc acierta 5/7; DeepLoc y TargetP juntos, 4/7.
- **En los controles plastidiales de algas verdes, DeepLoc acierta 1 de 2 y TargetP 0 de 2.**
- La versión previa decía exactamente lo contrario ("el plástido es lo único en que el panel no falló").

**[REFORMULADO] Conclusión.**
- *Estos predictores no resuelven la localización del clado en algas.*
- La mayoría de las secuencias no muestran señal plastidial fuerte (mediana 0,14).
- En Chlorophyta, 10/31 secuencias (32 %) tienen P(plástido) > 0,5; las otras 3 de las 13 son *Klebsormidium*, *Diacronema* y *Pseudo-nitzschia*. En los 2 controles plastidiales de algas verdes, DeepLoc falló 1 y TargetP falló 2; DeepLoc además falló 1 de 3 controles mitocondriales (NFS1_PABB). Con n tan chico no se puede estimar el sentido del sesgo: el resultado es **indeterminado**, no "probablemente plastidial".
- La afirmación "no es plastidial" **se retira** del §7.

**[REFORMULADO] Algas con plástido secundario.** En diatomeas, haptofitas, criptofitas y dinoflagelados, la importación al plástido usa una presecuencia bipartita (péptido señal + péptido de tránsito). Ni DeepLoc ni TargetP (modo Plant) están hechos para eso.
- Las 5 predicciones "SP" de TargetP son 3 diatomeas (2 *Cylindrotheca*, 1 *Fistulifera*), 1 haptofita (*Diacronema*) y *Chara braunii* (A0A388KLW8). En las cuatro de plástido secundario, un SP es **compatible con** destino plastidial, no evidencia en contra.
- **[PENDIENTE-ANÁLISIS]** Correr ASAFind o HECTAR en Stramenopila/Haptophyta/Cryptophyta y PredAlgo en Chlorophyta, y agregar controles citosólicos algales.

---

## 2.12 — Conservación (correcciones, D8)

**[CORREGIDO] Posiciones discriminantes.**
- La definición del propio texto es "conservada en ambas familias (H ≤ 0,5) con consenso distinto". Las posiciones N431 y S159 tienen "—" para NFS, así que **no la cumplen**. Son **4 posiciones discriminantes**, las 4 a menos de 8 Å del cofactor. N431 y S159 pasan a "conservadas sólo en SCLY-like".
- **[PENDIENTE-DATOS]** El texto agrupa NFS1+NFS2 como una "familia" y a la vez exige "H ≤ 0,5 en las dos". Hay que aclarar si el criterio se aplicó a NFS1 y a NFS2 por separado o al pool.

**[REFORMULADO] Test de enriquecimiento (corregido en la ronda 2).**
- La pregunta es si las discriminantes caen cerca del cofactor más de lo esperado por azar. La versión de la ronda 1 usaba como base el 13,2 % de *todas* las posiciones (46/348) a < 8 Å, y daba P(4/4) ≈ 3 × 10⁻⁴.
- **Esa base está mal.** Para ser discriminante, una posición tiene que estar conservada en las dos familias, y las posiciones conservadas ya se concentran cerca del cofactor: la conservación mediana es 0,924 a < 8 Å contra 0,363 a ≥ 15 Å. La base correcta es la fracción de posiciones a < 8 Å **entre las conservadas en ambas familias** (H ≤ 0,5 en SCLY-like y en NFS). **[PENDIENTE-DATOS]** Sale de `conservacion_scly_por_posicion.csv` + distancias.
- **H462 se excluye del test.** Es la His del bucle, contigua a la Cys catalítica: está cerca del cofactor por construcción y, si el bucle se usó para asignar familia, es circular. Además, su condición de "discriminante" depende del residuo en +1 de NFS2, que está pendiente (§2.6).
- Con las 3 restantes (G197, A232, T330) y la base condicional, el test puede no ser significativo. Si es así, se reporta descriptivamente.

**[REFORMULADO] Spearman ρ = −0,54.** Que los residuos cercanos al cofactor estén más conservados es una propiedad general de las enzimas, no un hallazgo sobre SCLY-like. El p = 2 × 10⁻²⁷ trata 348 posiciones autocorrelacionadas como independientes, así que se reporta ρ sin p o con p por permutación. **Se saca del §7.**

---

## 2.13 — RNA-seq (reformulado, D9)

**[CORREGIDO]** Se elimina "HISAT2 y STAR son sólo Linux". Es falso: corren en macOS vía bioconda o compilados, y en Windows vía WSL. Se reemplaza por la razón real (si la hubo) o se corre el alineamiento (**[PENDIENTE-ANÁLISIS]**: HISAT2 + StringTie sobre SRR12973628, que además resuelve el 5').

**[REFORMULADO] Lo que prueba el conteo de k-meros:**
1. **El intrón curado (1.180.241–1.180.347) se empalma:** 29 lecturas con k-meros exactos de 32 nt que cruzan la unión. Se sostiene.
2. **La unión del modelo automático no es la isoforma mayoritaria:** 0 lecturas, cuando la unión curada tiene 29. Bajo Poisson, si la unión automática representara aunque sea el 10 % de las lecturas (~3,2 esperadas), P(0) ≈ e^−3,2 ≈ 0,04. Se puede excluir una isoforma alternativa que sea más del ~10 %, pero **no una isoforma minoritaria**. Lo que importa es la profundidad en el locus, no el tamaño de la librería (21,9 M lecturas). Se elimina "no es poca evidencia: es ninguna".
3. Las 53 lecturas "corridas" en 1.180.754 y las 21 del exón recuperado muestran que esa región está transcrita. **No son evidencia de empalme**: el pre-ARNm sin procesar o el ADN genómico contaminante dan los mismos k-meros.
4. El gen se expresa en PABB004 en las condiciones del run. Se sostiene.

**[PENDIENTE-DATOS]**
- Explicar por qué la unión curada (29) y la lectura corrida (53) superan al control interno de SCLY (9). Puede ser que se contaron k-meros y no lecturas, o que se usaron distintos números de k-meros por unión. Hay que reportar cuántos k-meros por unión se usaron y si se verificó que cada uno es único en el genoma.
- Se procesaron 21,9 M de 60,2 M pares: hay que decir por qué.

**[REFORMULADO] Alcance de la curación.** "El modelo curado es el correcto — blindado" pasa a: *"la estructura 3' del modelo curado (último intrón y extremo C-terminal recuperado) está respaldada por RNA-seq. El extremo 5', el codón de inicio y el número de exones no están resueltos."*

El modelo curado tiene 2 exones y el ortólogo NREL 46B-D3 tiene 9. Perder 7 intrones entre especies congéneres sería raro: es más probable que falten exones 5'. Esto es consistente con los ~60 residuos N-terminales que faltan.

---

## 2.14 — Tasas relativas (reformulado, D7)

**[REFORMULADO]** La distancia raíz-hoja medida desde la raíz de *cada* clado confunde tasa con profundidad del clado:
- los MRCA de los tres clados no tienen la misma edad;
- el clado SCLY incluye la rama humana;
- en algas con plástido secundario, NFS2 puede venir de transferencia endosimbiótica.

Las 38 especies comparten ramas internas, así que los pares no son independientes y el Wilcoxon es anticonservador. Además, p = 7 × 10⁻¹² es exactamente el mínimo posible del test exacto con n = 38 (2/2³⁸ = 7,3 × 10⁻¹²): los 38 pares van en la misma dirección, que es lo que produciría un artefacto sistemático de profundidad.

**Se saca del §7 "blindado".** Queda como descriptivo: *"las distancias raíz-hoja son menores en NFS1. Esto es compatible con mayor restricción, pero no la demuestra."*

**[CORREGIDO]** La tabla etiquetaba SCLY-like como "(citosólico)", lo que contradice §2.10. Se saca la etiqueta.

**[PENDIENTE-ANÁLISIS]** Test de tasa relativa de Tajima contra un grupo externo común, o comparar longitudes de rama terminales por especie, o dN/dS (§8). **[PENDIENTE-DATOS]** Explicar cómo se emparejaron las especies con 2 copias.

---

## 2.15 — Maquinaria Sec (ajustes, D11)

- **[PENDIENTE-DATOS]** Definir "Sec+": ¿los 4 marcadores, o ≥ 3? Dado que PSTK se detecta mal, se propone ≥ 3 de 4, o SEPSECS + EEFSEC.
- **[PENDIENTE-ANÁLISIS]** Cochran-Mantel-Haenszel estratificado por linaje (barato, sale de la tabla de contingencia existente) y test de Pagel sobre árbol de especies.
- La pseudorreplicación es la lectura más probable, pero **no está demostrada**: descansa en un solo estrato de baja potencia (Chlorophyta, calculado además con 32 en vez de 31/30 SCLY+), y diatomeas va en la dirección global. CMH pendiente.

---

## 6. Limitaciones (lista actualizada)

1. Ausencia en proteomas ≠ ausencia en genomas (sin cambio).
2. **Localización no resuelta.** Los predictores fallan en controles de algas verdes, tanto plastidiales (DeepLoc acierta 1/2, TargetP 0/2) como mitocondriales (DeepLoc falla NFS1_PABB). 13/60 (22 %) del clado, y 10/31 (32 %) de Chlorophyta, tienen P(plástido) > 0,5. En algas con plástido secundario se usaron predictores no adecuados.
3. Los bucles de AlphaFold no sostienen distancias (sin cambio).
4. Especificidad Cys/Sec no resuelta. No se evaluó el equivalente de Asp146.
5. Asociación con la maquinaria Sec: pseudorreplicación (sin cambio).
6. Distancia raíz-hoja ≠ tasa: confundida con la profundidad del clado y con pares no independientes.
7. Extremo 5' sin resolver; probablemente faltan exones (2 contra 9 en NREL).
8. 301 clase V sin asignar (sin cambio).
9. Árbol aproximado (VeryFastTree, soportes SH-like), raíz arbitraria, sin IQ-TREE.
10. Muestreo de SCLY fuera de algas: un solo metazoo. Zygnematophyceae y glaucofitas ausentes.
11. n chicos en varios grupos (sin cambio).
12. Spearman conservación-distancia sin corrección por autocorrelación espacial.

---

## 7. Qué está blindado y qué no (reescrito)

| Afirmación | Estado |
|---|---|
| Existe en algas un clado de clase V distinto de NFS1 y NFS2 | **Sólido**, con la salvedad de que el árbol es aproximado. Confirmar con IQ-TREE/UFBoot |
| La His en +1 de la Cys catalítica es diagnóstica | **Pendiente** de la tabla de contingencia del §2.8 |
| G, C e H invariantes en 66 secuencias | **Sólido como dato**; trivial si la pertenencia se definió por el bucle |
| Clado hermano de la SCLY humana | **Provisorio**: el 0,96 es el soporte del clado *con* la humana; falta reportar el soporte de la bipartición sólo-algal, y con un único metazoo y raíz en el grupo II la topología no está cerrada |
| PNW80545.1 está mal anotado como NFS2 | **Sólido** |
| PABB004 tiene los tres genes | **Sólido** |
| El ORF de 3383 aa es quimérico y la estructura 3' curada es correcta | **Sólido**: CD-Search, sintenia con NREL y 29 contra 0 lecturas |
| El modelo curado completo es el correcto | **No**: 5' sin resolver |
| El gen se expresa en PABB004 | **Sólido** |
| No es plastidial | **Retirado**: los predictores no son fiables en algas verdes (fallan controles plastidiales y mitocondriales) y 10/31 Chlorophyta dan P(plástido) > 0,5 |
| Citosólica y/o mitocondrial | **No resuelto** |
| NFS1 está bajo mayor restricción | **Descriptivo**: confundido con profundidad del clado |
| Las discriminantes están cerca del cofactor | **Pendiente**: el test binomial usa una base incorrecta (ver §2.12) y H462 entra por construcción |
| Dos pérdidas independientes | **No resuelto**: sin Zygnematophyceae ni glaucofitas |
| Pérdida ligada al selenoproteoma | Hipótesis |
| Actividad sobre Sec | No demostrado. Falta como mínimo el análisis de Asp146 |

---

## 8. Lo que falta (reordenado según la revisión)

**Estado tras la ronda 4.**
- Resueltos con los datos del proyecto: 1 (Asp146 → Pro), 2 (tabla His), 4 (alineamiento del bucle) y la mayor parte del 6 (conteos), más el CMH del 9.
- **Bloqueante nuevo y prioritario:** verificar las 11 secuencias C-H excluidas (R2). Hay que bajarlas de UniProt, extraer el dominio PF00266, alinearlas y ubicarlas en el árbol.

**Para poder enviar (bloqueantes):**
1. **Asp146**: qué residuo hay en la posición equivalente en las 66 secuencias. Sale del alineamiento existente; es una tarde de trabajo.
2. **Tabla de contingencia de la His** (§2.8). Sale de `tabla_asignacion_familia_NFS.csv` y `candidatos_desulfurasas.csv`.
3. **IQ-TREE 2** (ModelFinder, UFBoot2 + SH-aLRT, grupo externo = clase V no asignadas) con más SCLY de eucariotas no algales y Zygnematophyceae.
4. **Alineamiento del bucle** de los tres grupos (±8 posiciones), para resolver la contradicción Ser/Thr/Ala.
5. **HISAT2 + StringTie** sobre SRR12973628: resuelve el 5' y reemplaza el argumento de los k-meros por uno estándar.
6. Unificar todos los conteos (§0) y explicar 134/116 contra 124/110 y 386/348.

**Fortalecen:**
7. tBLASTn genómico + sintenia en embriofitas y rodofitas (era el ítem 1 del plan anterior).
8. Localización con ASAFind/HECTAR/PredAlgo y controles citosólicos algales; o retirar la localización del paper principal.
9. Cochran-Mantel-Haenszel o Pagel para la hipótesis del selenio.
10. Dinoflagelados quiméricos (sin cambio).
11. dN/dS real (sin cambio).

---

## 9. Opción A — reescrita

**Qué es.** Descripción de un clado de cisteína desulfurasas clase V en algas, relacionado con la SCLY animal, con:
- la His en +1 de la Cys catalítica como carácter candidato a diagnóstico (pendiente del test no circular, §2.8);
- distribución en cinco supergrupos eucariotas y ausencia en los proteomas de embriofitas y rodofitas;
- un caso de modelo génico quimérico reparado en su extremo 3' con respaldo de RNA-seq.

**Antes de enviar.** Los bloqueantes 1–6 del §8 revisado.

**Dónde.** BMC Genomics si el eje es el barrido + la reparación génica. GBE sólo si se agregan IQ-TREE con muestreo eucariota amplio, la evidencia genómica de las pérdidas (tBLASTn + sintenia, con Zygnematophyceae) y un análisis de tasas válido.

**Figuras.**
1. Alineamiento del bucle de los tres grupos (±8 posiciones), con la His en +1 y la tabla de contingencia.
2. Árbol IQ-TREE enraizado con las clase V no asignadas.
3. Distribución por supergrupo.
4. Locus curado y evidencia de RNA-seq (3').
5. Conservación: posiciones discriminantes (≤ 4) y residuo equivalente a Asp146.
6. Sitio activo por transferencia de ligando, presentado como compatibilidad geométrica, no como ranking.
- Suplementaria: localización, presentada como **no resuelta**.
- **No** va la figura de tasas mientras no haya un test válido.

**Riesgo a anticipar.** Un revisor va a pedir actividad. La respuesta es que el trabajo es comparativo y genómico, y que Asp146 + ensayo enzimático son la continuación.
