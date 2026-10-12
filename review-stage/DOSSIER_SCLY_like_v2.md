# Clado SCLY-like en algas — dossier consolidado (v2)

**Agustín Truant** · versión del 12/10/2026, después de 7 rondas de revisión adversarial.

Este documento **reemplaza** al expediente original (`PAPER TENTATIVO ### dossier_SCLY_like para leer ###.pdf`), a `DOSSIER_REVISADO.md` (que queda como registro de cambios por ronda) y a la bitácora del bloque Se/S.

Cada número de este texto se recalculó desde los archivos del proyecto con los scripts de `review-stage/scripts/`. Las referencias se verificaron en PubMed. Lo que no se pudo verificar está marcado como tal.

---

## 0. Estado

| | |
|---|---|
| Evaluación de la última ronda | **{{SCORE}}** |
| Lo sólido | el clado, su firma, la reasignación del cebo, el modelo quimérico de PABB004, el estado Pro en la posición equivalente a Asp146 |
| Lo que todavía no está | muestreo eucariota dentro del árbol ML con test AU, barrido Sec válido, extremo 5' del gen de PABB004, tBLASTn de las ausencias |
| Revisor | subagente de Claude: **misma familia de modelos que el ejecutor**, independencia no verificada |

---

## 1. Resumen

1. El cebo **PNW80545.1** de *Chlamydomonas reinhardtii* (A0A2K3DJ46), anotado "NFS2" en AlgaePath, **no es NFS2**. Pertenece a un clado de cisteína desulfurasas clase V distinto de NFS1 (ISC) y de NFS2 (SUF), relacionado con la selenocisteína liasa (SCLY) animal.
2. ***Scenedesmus* sp. PABB004 tiene los tres genes**: NFS1 (KAF8057853.1), NFS2 (KAF8071197.1) y un SCLY-like escondido en un ORF quimérico de 3383 aa (KAF8071094.1).
3. **El clado SCLY-like es monofilético en un árbol ML** (IQ-TREE, Q.pfam+I+R9): SCLY-like + SCLY humana con **SH-aLRT 95,8 / UFBoot 99**, sin intrusos de NFS1 ni de NFS2. Tiene **{{N_ALG}} secuencias algales** en **{{N_PROT}} de 119 proteomas** de referencia.
4. **Firma del bucle catalítico:**
   - una His en la posición +1 de la Cys catalítica que **ninguna** de las 250 NFS1/NFS2 tiene;
   - la His está en casi todo el clado, pero se perdió en linajes puntuales: Bolidophyceae (una pérdida en el tallo del grupo), *Tetrabaena* y un parálogo de *Stephanodiscus* que además perdió la Cys.
5. **Residuo equivalente a Asp146** (el que da a la SCLY humana su especificidad por Sec):
   - es **Pro (dipéptido Pro-Ala)** en prácticamente todo el clado algal, Val en dinoflagelados y Asp **sólo en Choanozoa** (14 metazoos + *Salpingoeca*);
   - el Asp de la SCLY animal es un **estado derivado**, ganado en algún punto entre Amorphea y Choanozoa, y la Pro es un estado ampliamente distribuido. La polaridad depende del muestreo (§3.4).
6. **El clado no se detecta en embriofitas (0/6) ni en rodofitas (0/12)**, y está en las carofitas *Chara* y *Klebsormidium*. Es ausencia en proteomas de referencia, no en genomas.
7. **El gen SCLY-like de PABB004 estaba mal anotado.** La estructura 3' corregida (último intrón y 39 codones C-terminales) tiene respaldo de RNA-seq: 29 lecturas cruzan el intrón curado y 0 la unión del modelo automático. El extremo 5' sigue sin resolver.

**Lo que no se puede afirmar:**
- que es una familia nueva;
- que estas enzimas actúan sobre selenocisteína;
- que son plastidiales o que no lo son;
- que su presencia se asocia con la maquinaria de Sec dentro de cada linaje;
- que "la especificidad estricta de la SCLY animal es una innovación holozoa de un solo paso".

---

## 2. Datos y métodos

**Universo de búsqueda.** 119 proteomas de referencia de UniProt (107 algales + 12 de contraste), 2.110.345 secuencias. Búsqueda con phmmer usando 10 cebos de las tres familias, Z fijado al universo y corte E < 10⁻¹⁰: **617 proteínas clase V** (`candidatos_desulfurasas.csv`).

**Asignación de familia.**
- La columna `clase` del CSV no tiene regla documentada y **dejó afuera 11 miembros del clado** (§3.2).
- Regla que la reemplaza (reproducible, `scripts/ubicacion_generica.py`):
  1. extracción del dominio con un HMM construido del alineamiento del proyecto;
  2. asignación por el mejor HMM de clado (NFS1, NFS2 o SCLY-like, construidos con los miembros de cada clado);
  3. **confirmación por ubicación en el árbol ML**. Es el árbol el que decide: los HMM heredan la membresía original.
- **Pendiente:** aplicar esta regla a los 617 candidatos. Hoy se aplicó a 46: las 16 de la ronda 6 y las 30 de la ronda 7.

**Árboles.**
1. Árbol original: VeryFastTree, 304 hojas. **Las hojas ya llevaban la etiqueta de clase**, así que es una verificación de monofilia y no un descubrimiento a ciegas. Los soportes son SH-like locales, no bootstrap.
2. **Árbol ML de referencia (ronda 6):**
   - IQ-TREE 2.3.6, 318 dominios, alineados con FAMSA y recortados a ocupación ≥ 0,35 (386 columnas);
   - modelo **Q.pfam+I+R9** elegido por BIC entre LG, WAG, JTT y Q.pfam;
   - 1000 UFBoot + 1000 SH-aLRT;
   - la SCLY humana duplicada se sacó.
3. **Árbol final (ronda 7):** las 6 secuencias adicionales, con la topología del árbol 2 como restricción y el mismo modelo.

**Advertencias del árbol ML:**
- 650 parámetros para 386 columnas;
- 10 secuencias con más del 50 % de gaps;
- es un árbol sin raíz: se lee enraizado en NFS2 + SufS (el split {NFS1 + IscS + SCLY-like} contra {NFS2 + SufS} tiene 100/100);
- las únicas referencias bacterianas son IscS y SufS de *E. coli*.

**Otros métodos:**
- localización: DeepLoc 2.1, TargetP 2.0, SignalP 6.0 y DeepTMHMM;
- RNA-seq: conteo de k-meros exactos de 32 nt en las uniones, sobre lecturas crudas (SRR12973628);
- estructura: AlphaFold y transferencia de ligando por superposición con TM-align (3A9Z, 1KMK, 1P3W);
- 3GZC para medir distancias en la SCLY humana;
- reconstrucción ancestral: parsimonia de Fitch y modelo Mk sobre una topología de especies estándar (`scripts/asr_determinante.py`).

---

## 3. Resultados

### 3.1 Reasignación del cebo y los tres genes de PABB004

Los bucles catalíticos de los cebos y referencias (`tabla_asignacion_familia_NFS.csv`) separan tres grupos:
- IscS/NFS1: `…SSGSACTS…`;
- SufS/NFS2: `…RxGHHC…`;
- SCLY-like: `…SAGxACHS…`.

PNW80545.1 (A0A2K3DJ46) y el tramo de PABB004 caen en el tercero. La NFS2 verdadera de *Chlamydomonas* es A0A2K3D4F5 y la NFS1, A0A2K3E3W0.

PABB004 tiene:
- NFS1: KAF8057853.1, 64,2 % de identidad con *A. thaliana*;
- NFS2: KAF8071197.1, 58,1 %;
- SCLY-like: dentro de KAF8071094.1, un ORF de 3383 aa con cinco bloques de dominios no relacionados (lipasa, NDPK, histidinol deshidrogenasa, aminotransferasa clase V, LamG).

En *Scenedesmus* sp. NREL 46B-D3, el gen SCLY está a 393 pb del de histidinol deshidrogenasa. El anotador de PABB004 fusionó ese mismo par de genes vecinos.

### 3.2 El clado: composición y soporte

| Conjunto | n |
|---|---|
| Miembros originales (`clase` = L3) | 65 algales + SCLY humana |
| HText (PABB004, curado a mano; PABB004 **no** está en los 119 proteomas) | +1 |
| Excluidos por error y reubicados (ronda 6) | +15 |
| Adicionales (ronda 7) | +{{N_ADD}} |
| **Total algal** | **{{N_ALG}}** |

**Soportes en el árbol ML:**
- SCLY-like + humana: **95,8 / 99**;
- **sólo algal: 61,1 / 57**, débil. Lo debilitan dos secuencias que quedan en la base: una de las dos copias de *Guillardia* (L1J7A3) y una quimera de *Cladocopium* (A0A9P1FCD2) con ubicación sin resolver (0/45). Sin ellas, el núcleo algal de 79 hojas tiene 91,6/82;
- que la SCLY humana sea **hermana** del clado algal es la topología obtenida, pero apoyada por una sola secuencia de metazoo dentro de este árbol. Muestrear eucariotas lo resuelve (§3.4, §7).

**Subclados bien soportados:**
- Pelagophyceae: 99,8/100;
- Bolidophyceae: 99,8/100, hermanas de las diatomeas (99,1/100), igual que en el árbol de especies;
- *Monoraphidium* + *Raphidocelis*: 99,9/100.

{{UBICACION_R7}}

**Secuencias descartadas:**
- A0ABR1FWJ4 (*Aureococcus*): mismo locus que A0ABR1FZ61, pero le falta el dominio y tiene un corrimiento del marco.
- 21 de las 30 revisadas en la ronda 7 no tienen dominio clase V: son proteínas con pentraxina o lectina que el cebo pescó por error.
- Tres fragmentos de unos 110 aa (*Tetrabaena* A0A2J7ZMY6 y dos de *Symbiodinium*, A0A812J8T9 y A0A1Q9ECG7) no son ubicables.

### 3.3 Bucle catalítico

Alineamiento de los tres grupos alrededor de la Cys catalítica (MSA del proyecto):

| Posición respecto de la Cys | −6 | −5 | −4 | −3 | −2 | −1 | **0** | **+1** | +2 |
|---|---|---|---|---|---|---|---|---|---|
| NFS1 (124) | V/I | S | S | G | S | A | C | **T** (100 %) | S |
| NFS2 (110) | V/I/M | R | S/A | G | H | H | C | **T 58 / A 32 / C 19** | Q |
| SCLY-like (66 originales) | A/C | S | A | G | A/S | A | C | **H** | S |

- **La His en +1 es diagnóstica en una sola dirección:** la tienen **0 de 250** NFS1/NFS2. Dentro del clado está en casi todos los miembros, con estas pérdidas:
  - **Bolidophyceae (5)**: `[IV]AAGSAC-[ED]`, una sola pérdida en el tallo. Además tienen I/V en −6, igual que NFS1/NFS2;
  - ***Tetrabaena*** (2): `GVGGCAC-S`;
  - ***Stephanodiscus* A0ABD3QSF5**: `VACSAGSIS`, sin la Cys catalítica. Es un parálogo probablemente inactivo; la especie tiene otros dos SCLY-like con Cys e His.
- G-x-x-C no es diagnóstico, porque NFS1 también lo tiene.
- La His no se puede usar como criterio de pertenencia, porque eso sería circular. Lo correcto es tratarla como un carácter que se superpone casi exactamente con el clado definido por árbol y HMM: de las 77 secuencias con C-H, 75 tienen como mejor cebo uno SCLY-like.

### 3.4 El residuo equivalente a Asp146

**Estructura 3GZC (SCLY humana)**, medido sobre las coordenadas:
- Asp146: 3,73 Å del SG de la Cys388 catalítica (OD2–SG) y 6,29 Å del ligando PLR, un análogo de PLP;
- el bucle `ASVGAACH` empieza en el residuo 382;
- Asp146 queda además cerca de la interfaz del dímero (cadena B, residuos 284–287).

**Collins et al. 2012:** Asp146 es el residuo que da la especificidad por Sec; el mutante D146K la pierde y gana actividad cisteína desulfurasa.

**Estado de la columna** (anclada en His145; el residuo previo es E/D/N, no siempre Glu):

| Grupo | Residuo |
|---|---|
| NFS1 | Lys 113, Arg 1 (gap 10) |
| NFS2 | His 106 (gap 4) |
| SCLY-like algales | **Pro** en todas las informativas salvo los Val. Incluye las 15 de la ronda 6 y {{PRO_R7}} |
| Dinoflagelados + una copia de *Guillardia* | **Val** (5, más *Durusdinium* ×2 en la ronda 7) |
| Choanozoa (14 metazoos + *Salpingoeca*) | **Asp** |
| *Acanthamoeba*, *Trypanosoma*, *Thalassiosira*, *Chlamydomonas* | Pro |
| *Phytophthora* | Val |
| *C. elegans* | Pro |

- El cambio es de **dos sitios**: Pro-Ala en algas, *Acanthamoeba* y *Trypanosoma*, contra Asp-Ser en holozoos. *C. elegans* tiene Pro-Ser, lo que encaja con una reversión. El experimento propuesto tiene que incluir el **doble mutante P→D / A→S**.
- Que NFS1 tenga la Lys del mutante D146K confirma que es la **posición homóloga**. **No** prueba que esa posición controle la especificidad en NFS1/NFS2. Además, la SclA bacteriana prefiere Sec con His en esa posición (Johnstone et al. 2021).
- **Precedente funcional de una SCL con Pro:** en *T. brucei* (Q38DC4), silenciar la SCL baja tanto la actividad cisteína desulfurasa como la selenocisteína liasa en fracciones celulares (Poliak et al. 2009). Por el abstract no se sabe si midieron la especificidad sobre la enzima purificada.

**Reconstrucción ancestral** (topología de especies estándar; Fitch = 4 cambios):

| Supuesto | Raíz Pro | Amorphea Pro | Choanozoa Asp |
|---|---|---|---|
| Ramas iguales | 0,98 | 0,92 | 0,94 |
| Ramas profundas ×5 | 0,84 | 0,71 | 0,97 |
| Ramas profundas ×10 | 0,73 | 0,58 | 0,98 |
| *Acanthamoeba* y *Trypanosoma* desconocidos | 0,32 | 0,17 | 0,98 |
| *Salpingoeca* desconocido | 0,98 | 0,95 | 0,49 |

Qué se lee de la tabla:
- **Asp en el linaje animal es robusto.** Que Pro sea el estado de la raíz depende de dos especies, y que la ganancia esté en Choanozoa depende de un solo coanoflagelado.
- No hay Ichthyosporea ni Filasterea en el muestreo, así que la ganancia está en algún punto del tallo **Amorphea → Choanozoa**.
- **La reversión en *C. elegans*** sólo se puede ubicar en algún punto entre el ancestro de Ecdysozoa y *C. elegans*, porque es el único ecdisozoo con el gen. **No es una predicción cumplida.** El estado Pro aparece en 32 de 47 proteomas con SCLY-like Pro que sí tienen maquinaria Sec, entre ellos *Ostreococcus lucimarinus*, con uno de los selenoproteomas más grandes que se conocen. Además *C. elegans* conserva la inserción de Sec para TrxR-1.
- **Val:** cuántas veces apareció no se resuelve. Con la topología de especies el SAR queda ambiguo (P 0,46 / V 0,54), y *Guillardia* tiene dos copias, una con Pro y otra con Val.
- El árbol de genes contradice al de especies en varios puntos (*Trypanosoma*, *Acanthamoeba*, *Salpingoeca*, *C. elegans*). La reconstrucción **supone herencia vertical**; falta un test AU.

### 3.5 Distribución

Proteomas de referencia con SCLY-like:

{{TABLA_DISTRIB}}

- **Ausencias firmes:** Embryophyta (0/6) y Rhodophyta (0/12). Es ausencia en proteomas: falta tBLASTn genómico y sintenia.
- Las dos carofitas tienen el gen, pero sin Zygnematophyceae en el muestreo **no se puede ubicar la pérdida en la terrestrialización**. Sin glaucofitas, "pérdida independiente en rodofitas" no se puede afirmar.
- *Drosophila*: 0. Los hongos no lo tienen.

### 3.6 El gen de PABB004

- **Modelo curado:** 1.179.501–1.180.873 (+); dos exones (740 + 526 nt), intrón de 107 pb GT-AG; 421 aa. Lys del PLP K234, Cys catalítica C360, His diagnóstica H361.
- **RNA-seq** (SRR12973628, 21.890.509 lecturas de 60,2 M pares, k = 32):

| Unión o región | Lecturas |
|---|---|
| Intrón curado | 29 |
| Unión del modelo automático | 0 |
| Lectura corrida en 1.180.754 | 53 |
| Exón C-terminal recuperado | 21 |
| Exón interno de SCLY (control) | 9 |
| Exón de NFS2 (control) | 201 |

- **Qué prueba:**
  - el intrón curado se empalma;
  - la unión automática no es la isoforma mayoritaria. Si fuera ≥ 10 % de las lecturas, se esperarían ~3,2 y P(0) ≈ 0,04; no se puede excluir una isoforma minoritaria;
  - el gen se expresa;
  - las lecturas "corridas" no prueban empalme: el pre-ARNm o el ADN contaminante darían lo mismo.
- **Qué no prueba:** el extremo 5'. Faltan ~60 residuos N-terminales, y el ortólogo de NREL tiene 9 exones contra 2. Para resolverlo: HISAT2 + StringTie.
- Pendiente: explicar por qué la unión curada (29) supera al control interno (9). Puede ser conteo por k-mero o por lectura.

### 3.7 Localización

Sobre 60 SCLY-like algales con N-terminal fiable (DeepLoc 2.1):

| Etiqueta | n |
|---|---|
| Citoplasma | 24 |
| Mitocondria | 15 |
| Citoplasma + mitocondria | 13 |
| Mitocondria + plástido | 3 |
| Plástido | 2 |
| Citoplasma + mitocondria + plástido | 2 |
| Extracelular | 1 |

- P(plástido) > 0,5: **13/60**, de las cuales 10 son Chlorophyta (10/31).
- **Panel de control:** en los 2 controles plastidiales de algas verdes, DeepLoc acierta 1 y TargetP ninguno. DeepLoc además falla 1 de 3 mitocondriales. En las algas con plástido secundario se usaron predictores no adecuados.
- **Conclusión:** la localización **no se resuelve** con estos predictores. La proteína curada de PABB004 tampoco se puede predecir, porque le falta el N-terminal.

### 3.8 Conservación y posiciones discriminantes

- Con la definición "conservada en las dos familias (H ≤ 0,5) y con consenso distinto":
  - **contra NFS1 y NFS2**, sólo 2 posiciones: S159 y G197;
  - contra NFS1 sola, 6.
- **No hay evidencia de enriquecimiento cerca del cofactor** usando la base correcta (fracción a < 8 Å entre las posiciones conservadas): p = 0,12–0,63. El test tiene poca potencia.
- La conservación cae con la distancia al ligando (Spearman ρ ≈ −0,48 con f_L3). Es una propiedad general de las enzimas, y el p no vale porque las posiciones no son independientes.

### 3.9 Tasas relativas

- Distancias raíz-hoja pareadas por especie (38): NFS1 < NFS2 ≈ SCLY (38/38, 38/38 y 17/38 pares).
- El p = 7 × 10⁻¹² es el mínimo exacto del test con n = 38.
- **Descriptivo:** está confundido con la profundidad de cada clado y los pares no son independientes. No es ω.

### 3.10 Selenio

- "Sec+" en el CSV = PSTK **y** SEPSECS **y** EEFSEC.
- **Hay dos barridos que no coinciden:** el del CSV tiene PSTK en 55/119; el informe del barrido, en 18. Hay que decidir cuál vale.
- Con el CSV y la distribución nueva:
  - Fisher global: OR 2,68, p = 0,015;
  - **CMH por linaje: OR 1,08 (IC 0,35–3,33), p = 0,90**, con 3 estratos informativos y dominado por Chlorophyta.
- La asociación no se sostiene dentro de los linajes. La correlación entre el estado del residuo 146 y la maquinaria Sec no se puede testear, porque Asp es un único evento.
- Hipótesis, n = 1: las Bolidophyceae (pérdida de la His) no tienen PSTK (Sec_estricto 0/6).

---

## 4. Material descartado

| Material | Motivo |
|---|---|
| Docking con AutoDock Vina | El ligando era Cys (`sed 's/Se$/S /g'`), el receptor no tenía PLP, la caja era de 22 Å, la exhaustividad no coincidía con lo declarado y no hay salidas guardadas. Además, el docking no resuelve Cys contra Sec |
| Tabla "ConSurf" de 353 posiciones | No es una salida real de ConSurf (grados 4–8 vacíos, 87 % de residuos expuestos), el test es circular y el p no coincide entre figura y texto |
| `MSA_73_panalgal.fasta` | 88,6 % de gaps |
| Paquete "Archaeplastida" | Datos sintéticos (NFS2 = 1,2 × NFS1); codeml y MCMCTree nunca corrieron; la figura macroevolutiva contradice los datos |
| Predicción plastidial de HText (DeepLoc 0,95) | **No interpretable**: los límites del recorte eran inciertos. No se puede llamarla "artefacto" |
| Clasificación por `clase_loop` del CSV | Etiquetó 58/66 SCLY-like como "I IscS/NFS1" |

---

## 5. Limitaciones

1. Ausencia en proteomas no es ausencia en genomas.
2. Localización sin resolver.
3. Especificidad Cys/Sec sin demostrar. El estado Pro no está caracterizado bioquímicamente; sólo existe el antecedente de *T. brucei*.
4. El soporte del clado sólo algal es débil (61/57), y que la SCLY humana sea hermana se apoya en un único metazoo dentro del árbol ML.
5. La reconstrucción ancestral depende de pocos taxones y supone herencia vertical.
6. Hay dos barridos Sec inconsistentes, y la asociación no se sostiene dentro de los linajes.
7. El extremo 5' del gen de PABB004 está sin resolver.
8. La regla de asignación no se aplicó todavía a los 617 candidatos.
9. Faltan Zygnematophyceae y glaucofitas.
10. La validación de este documento la hizo un revisor de la misma familia de modelos que el ejecutor.

---

## 6. Estado de cada afirmación

| Afirmación | Estado |
|---|---|
| Existe un clado clase V distinto de NFS1/NFS2 en algas | **Sólido**: ML 95,8/99 |
| PNW80545.1 está mal anotado como NFS2 | **Sólido** |
| PABB004 tiene los tres genes; el ORF de 3383 aa es quimérico | **Sólido** |
| Estructura 3' del gen curado | **Sólida**: 29 contra 0 lecturas |
| Gen curado completo | **No**: 5' sin resolver |
| His en +1 como marcador del clado | **Sólido en una dirección** (0/250 NFS); con pérdidas puntuales dentro del clado |
| Pro en la posición de Asp146 en el clado algal | **Sólido** |
| El Asp de la SCLY animal es derivado | **Apoyado**, con dependencia del muestreo |
| Ortólogo de SCLY / hermano de la SCLY humana | **Provisorio** |
| Ausente en embriofitas y rodofitas | **Sólido a nivel de proteoma**; falta el genoma |
| Pérdida en la terrestrialización | **No resuelto** (faltan Zygnematophyceae) |
| No plastidial / citosólica | **Retirado** / no resuelto |
| Asociación con la maquinaria Sec | **No se sostiene** dentro de los linajes |
| Discriminantes cerca del cofactor | **Retirado** |
| NFS1 más restringida | **Descriptivo** |
| Actividad sobre Sec | **No demostrado** |

---

## 7. Pendientes, por prioridad

**Para "almost":**
1. Aplicar la regla HMM + árbol a los 617 candidatos y documentarla en Métodos.
2. Decidir cuál barrido Sec vale, o declarar la maquinaria "no evaluada".
3. Depositar el árbol de especies usado en la reconstrucción y hacer el test AU (árbol de genes restringido a la topología de especies).

**Para "ready":**
4. SCLY eucariotas dentro del árbol ML: *Capsaspora*, *Sphaeroforma*/*Creolimax*, *Monosiga*, *Mnemiopsis*, otros nematodos, artrópodos con el gen, *Naegleria*, *Euglena*.
5. tBLASTn + sintenia para las ausencias (embriofitas, rodofitas, Zygnematophyceae).
6. HISAT2 + StringTie sobre SRR12973628 para resolver el 5'.
7. Localización con ASAFind/HECTAR/PredAlgo, o pasarla a material suplementario como "no resuelta".

---

## 8. Encuadre para publicar

**Título posible:** *An algal clade of selenocysteine lyase-related cysteine desulfurases with a conserved non-animal state at the substrate-specificity position.*

Ejes:
1. un clado clase V que pasó desapercibido por mala anotación, con un caso documentado de modelo génico quimérico;
2. una firma de bucle diagnóstica en una dirección;
3. el residuo de especificidad: Pro en algas y Asp sólo en Choanozoa;
4. una predicción experimental concreta: núcleo algal con Pro-Ala contra el doble mutante P→D/A→S, midiendo actividad sobre Cys y sobre Sec.

**Revista:** BMC Genomics, si el eje es el barrido + la curación. GBE, si se agregan el punto 4 de §7 y el test AU.

---

## 9. Referencias verificadas (PubMed)

| Trabajo | DOI |
|---|---|
| Collins et al. 2012, *PLoS ONE* 7:e30581 | [10.1371/journal.pone.0030581](https://doi.org/10.1371/journal.pone.0030581) |
| Omi et al. 2010, *J Biol Chem* 285:12133 | [10.1074/jbc.M109.084475](https://doi.org/10.1074/jbc.M109.084475) |
| Mihara et al. 2000, *J Biol Chem* 275:6195 (SCL de ratón, citosólica) | [10.1074/jbc.275.9.6195](https://doi.org/10.1074/jbc.275.9.6195) |
| Mihara et al. 2000, *J Biochem* 127:559 (mutantes Cys→Ala de NifS) | [10.1093/oxfordjournals.jbchem.a022641](https://doi.org/10.1093/oxfordjournals.jbchem.a022641) |
| Mihara, Maeda, Fujii, Kurihara, Hata, Esaki 1999, *J Biol Chem* 274:14768 (CsdB) | [10.1074/jbc.274.21.14768](https://doi.org/10.1074/jbc.274.21.14768) |
| Johnstone et al. 2021, *Biochimie* 182:166 (SclA) | [10.1016/j.biochi.2021.01.002](https://doi.org/10.1016/j.biochi.2021.01.002) |
| Lobanov et al. 2007, *Genome Biol* 8:R198 | [10.1186/gb-2007-8-9-r198](https://doi.org/10.1186/gb-2007-8-9-r198) |
| Taskov et al. 2005, *Nucleic Acids Res* 33:2227 | [10.1093/nar/gki507](https://doi.org/10.1093/nar/gki507) |
| Poliak et al. 2009, *FEBS J* 277:383 (SCL de *T. brucei*) | [10.1111/j.1742-4658.2009.07489.x](https://doi.org/10.1111/j.1742-4658.2009.07489.x) |

La cita de da Silva et al. 2020 (*PLoS NTD*, SPS–SCLY en tripanosomátidos) la aportó el revisor y no está verificada.

---

## 10. Reproducibilidad

| Script | Qué hace |
|---|---|
| `scripts/recalculo_localizacion.py` | localización, composición y bucle desde el CSV |
| `scripts/recalculo_datos_proyecto.py` | tabla de la His, árbol, Asp146, discriminantes, CMH, tasas |
| `scripts/asr_determinante.py` | Fitch, Mk y sensibilidad |
| `scripts/ubicacion_generica.py` | extracción del dominio, HMM de clado, FAMSA, bucle y Asp146 |
| `scripts/leer_arbol318.py` | lectura del árbol ML |

- Árboles: `datos/ubicacion16/iq318.*` (referencia) y `datos/ubicacion_final/iqfinal.*` (con las 6 adicionales).
- Registro de rondas: `AUTO_REVIEW.md`. Respuestas del revisor: `ronda1_revisor.md` a `ronda7_revisor.md`.
