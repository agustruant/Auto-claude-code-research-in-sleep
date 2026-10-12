# Dossier SCLY-like — versión revisada (auto-review loop, rondas 1–6)

Este archivo **no reemplaza** al PDF original: reescribe las secciones que la revisión encontró incorrectas o sobreafirmadas. Lo que no aparece acá queda como en el original. Cada cambio remite a la debilidad numerada en la revisión de la ronda 1 (`ronda1_revisor.md`, puntos 1–12 = D1–D12) o de la ronda 2 (`ronda2_revisor.md`, N1–N8).

Etiquetas:
- **[CORREGIDO]**: corregido con datos que ya existen (CSV o bibliografía verificada).
- **[REFORMULADO]**: la afirmación se rebajó a lo que los datos sostienen.
- **[PENDIENTE-DATOS]**: requiere archivos que no están en el repo (árbol, alineamientos, conteos). Hay que verificarlo contra esos archivos antes de escribir el paper.
- **[PENDIENTE-ANÁLISIS]**: hace falta correr un análisis nuevo.

Los recálculos sobre el CSV están en `review-stage/recalculo_localizacion.txt` y salen de `review-stage/scripts/recalculo_localizacion.py`.

## ★★★ Ubicación de las 16 secuencias candidatas (ronda 6)

Fuente: FASTA de las 16 accesiones de UniProt aportado por el autor (`datos/ubicacion16/nuevas16.fasta`). Scripts:
- `scripts/ubicacion16.py`: extracción del dominio, asignación por HMM, realineamiento con FAMSA, bucle y Asp146;
- `scripts/leer_arbol318.py`: lectura del árbol.

Árbol: **IQ-TREE 2.3.6**, modelo **Q.pfam+I+R9** (BIC), **1000 UFBoot + 1000 SH-aLRT**, 318 dominios, 386 columnas con ocupación ≥ 0,35. Salidas en `datos/ubicacion16/iq318.*`. Es el primer árbol ML completo del proyecto, que hasta ahora sólo tenía la aproximación de VeryFastTree. Además se sacó la SCLY humana duplicada y se excluyó A0ABR1FWJ4. Es el **mismo locus que A0ABR1FZ61** (mismo proteoma, GN=SCLY, primeros ~90 aa y extremo C idénticos), pero le faltan ~135 aa del dominio, reemplazados por un segmento rico en R/G/P típico de un corrimiento del marco. Excluirla no saca ningún proteoma.

**Métodos del árbol, a declarar:**
- set de modelos restringido (`-mset LG,WAG,JTT,Q.pfam`);
- 650 parámetros para 386 columnas (IQ-TREE lo advierte);
- 10 secuencias con más de 50 % de gaps;
- árbol sin raíz, enraizado para leerlo en NFS2 + SufS (el split {NFS1 + IscS + SCLY} contra {NFS2 + SufS} es 100/100);
- las únicas referencias bacterianas son IscS y SufS de *E. coli*.

El 95,8/99 del clado SCLY-like es un split no enraizado, así que no depende de la raíz.


> **Precedencia (ronda 6).** Este bloque ★★★ reemplaza todas las afirmaciones anteriores del documento sobre:
> - conteos del clado (65, 66 o 67 secuencias; 56 especies);
> - "G-x-x-C-H / G, C, H invariantes" (§1, §2.8, §4, §7, R1);
> - "estramenopilas no diatomeas ausentes" (§1.6, §2.9, R2);
> - soporte 0,96 / 0,855 (§1.5, R7);
> - "sin IQ-TREE" (§6.9, §7);
> - "no se evaluó Asp146" (§6.4);
> - los bloqueantes 1–4 del §8, que ya están hechos.
>
> La consolidación en un único texto queda como tarea pendiente.

### U1. Resultado

| | |
|---|---|
| Extracción del dominio | las 16 con E ≤ 10⁻²² (15 con E ≤ 10⁻⁵², 10 con E ≤ 10⁻¹¹⁰) |
| Mejor HMM de clado (construido con cada clado del MSA del proyecto) | **SCLY-like en las 16**. Margen sobre NFS1 de **85–237 bits en las 15 ubicadas** (64 en A0ABR1FWJ4). No hay filtración: las 16 no se usaron para entrenar los HMM. Pero los HMM heredan la membresía de la columna `clase`, así que la evidencia que decide es el árbol ML; el HMM sólo coincide con él |
| Ubicación en el árbol | **15/15 dentro del clado SCLY-like**. Clado SCLY-like + humana: SH-aLRT 95,8 / UFBoot 99 (82 hojas, sin intrusos de NFS1/NFS2) |
| Residuo en la posición de Asp146 | **Pro en las 15**, todas con el dipéptido P-A (`[VI]EH-PA[IVT]`) |

**Subclados:**
- **Pelagophyceae** (*Aureococcus* ×2, *Pelagomonas*, *Chrysophaeum*): monofilético, 99,8/100.
- ***Monoraphidium* + *Raphidocelis***: 99,9/100.
- ***Nitzschia* ×2**: 100/100, junto a *Phaeodactylum*, *Fragilariopsis* y *Pseudo-nitzschia*. Este nodo tiene soporte bajo (7,6/87).
- **Bolidophyceae** (*Triparma* ×4 + *Tetraparma*): monofilético, 99,8/100, **dentro** del clado SCLY-like.
- **La quimera de *Cladocopium*** (A0A9P1FCD2) queda en la **base del clado algal**: hermana de un núcleo de 79 hojas (91,6/82), con soporte **0/45**. Ubicación no resuelta. Corrección: la ronda anterior decía "junto a las prasinofitas", que era un artefacto del script. La otra secuencia de *Cladocopium* (CGG1) está dentro de los dinoflagelados (100/100). Como los otros SCLY-like de dinoflagelados tienen Val y ésta tiene Pro, conviene descartar contaminación o un error de ensamblado antes de usarla.

### U2. Consecuencias

**1. La exclusión de las 11 secuencias era un error de asignación, confirmado.** El clado SCLY-like pasa a tener **81 secuencias algales** (66 + 15) más la humana.

**2. La tabla de distribución cambia** (proteomas de referencia con SCLY-like):

| Linaje | Antes | Ahora |
|---|---|---|
| Bacillariophyta | 14/16 | **16/16** |
| Chlorophyta | 32/48 (30/44 especies) | **34/48 (32/44 especies)** |
| Pelagophyceae | 0/4 | **4/4** |
| Bolidophyceae | 0/6 | **5/6** (falta *T. retinervis*) |
| Eustigmatophyceae | 0/2 | 0/2 |
| Phaeophyceae | 0/1 | 0/1 |
| Embryophyta | 0/6 | 0/6 |
| Rhodophyta | 0/12 | 0/12 |
| **Total** | 58/119 | **71/119** |

⚠ **Phaeophyceae 0/1 es probablemente falso.** *Ectocarpus* D8LEU7 (426 aa) tiene como mejor cebo uno SCLY-like: score 333, E 3,6 × 10⁻⁹⁷, margen de 129 bits sobre NFS1. Está en la mediana de los miembros aceptados. *Ectocarpus* ya tiene su propia NFS1 y su propia NFS2, así que este sería un tercer gen clase V. Su bucle no se pudo extraer. Además quedan **30 secuencias "otro" con mejor cebo SCLY-like sin examinar**. Las más relevantes:
- dos de *Durusdinium* (A0ABP0KTI6, A0ABP0RUF2), con bucle raro;
- *Stephanodiscus* A0ABD3QSF5;
- tres de *Tetrabaena* (bucle `GVGGCAC`);
- el resto, proteínas multidominio largas de Chlorophyta (50–150 bits), probablemente del tipo MOCOS.

**Hasta ubicarlas, la tabla es provisoria y no se afirma ninguna ausencia en estramenopilas.**

- **"Ausente en estramenopilas no diatomeas" queda sin efecto.** Eustigmatophyceae (0/2) tiene n muy chico, y Phaeophyceae probablemente tiene el gen (ver arriba).
- **Las ausencias en embriofitas y rodofitas se mantienen**, y ahora son las únicas ausencias de linaje bien muestreado.

**3. La His en +1 no es invariante en el clado** (conteo sobre la columna `loop` del CSV más las 16 nuevas; en el MSA hay ~6 miembros con gap en esa posición). Las 5 de Bolidophyceae tienen `[IV]AAGSAC-[ED]`: conservan G en −3 y la Cys, pero tienen Glu/Asp en +1. Como forman un subclado monofilético (99,8/100) dentro de SCLY-like, es una **pérdida única de la His en Bolidophyceae**.
- La His sigue siendo **diagnóstica en una sola dirección**: ninguna de las 250 NFS1/NFS2 la tiene.
- Pero **no es invariante**: está en 77 de las 82 SCLY-like del árbol.
- Hay que cambiar "G-x-x-C-H invariante" por "**His en +1 en 77/82, perdida una vez en Bolidophyceae**". G-x-x-C no es diagnóstico, porque NFS1 también lo tiene (VSSGSAC).
- **Las Bolidophyceae son hermanas de las diatomeas (99,1/100)**, igual que en el árbol de especies, lo que apoya una única pérdida en el tallo de Bolidophyceae. Tienen además las ramas más largas del clado (raíz-hoja 4,0–4,6 contra una mediana de 3,0).
- Su bucle es un mosaico: en −6 tienen I/V, como NFS1/NFS2. Por eso el "−6 distingue" de R4 tiene esta excepción.
- *Hipótesis, n = 1:* las 6 Bolidophyceae no tienen PSTK (`Sec_estricto` 0/6). La pérdida de la His coincide con un linaje sin maquinaria Sec detectada, con la salvedad de que los dos barridos Sec no coinciden.

**4. Asp146: Pro en 68 de 73 secuencias algales informativas**, Val en 5 y gap en 8. Las 15 nuevas tienen Pro con P-A, incluidas las Bolidophyceae sin His. La His y el estado de la posición 146 se desacoplan en **dos eventos**: Bolidophyceae (pierden la His y conservan Pro) y dinoflagelados + una copia de *Guillardia* (conservan la His y tienen Val).
- La única excepción son los Val de dinoflagelados y una de las copias de *Guillardia*.
- La quimera de *Cladocopium* tiene Pro, a diferencia de los otros dinoflagelados.

**5. Soportes del clado:**
- Clado SCLY-like + humana: 95,8/99.
- **Clado sólo algal: SH-aLRT 61,1 / UFBoot 57: no es robusto en el árbol ML.** El 0,855 de VeryFastTree no es comparable (otro método y otro set de taxones). Lo que debilita ese nodo es que *Guillardia* L1J7A3 y la quimera de *Cladocopium* quedan en la base. El **núcleo algal de 79 hojas tiene 91,6/82**.
- Que la SCLY humana sea hermana de las algas sigue siendo la topología obtenida, pero con poco soporte. Muestrear eucariotas (bloque Se/S) y hacer un test AU sigue siendo necesario.

**6. Selenio, con la distribución nueva:**
- Fisher global: OR 2,68, p = 0,015.
- CMH por linaje: **OR_MH 1,08, IC 0,35–3,33, p = 0,90**. Con la distribución nueva quedan sólo **3 estratos informativos (62 proteomas)**, porque las diatomeas pasaron a 16/16. El resultado lo maneja Chlorophyta. Breslow-Day p = 0,098.
- La asociación dentro de linajes desaparece. Sigue valiendo la advertencia de dos barridos Sec que no coinciden (R6).

**7. Asignación de familia.** La regla que generó la columna `clase` sigue sin documentar. Se puede reemplazar por la de esta ronda: **HMM de clado + ubicación en el árbol ML**, reproducible con los scripts.

---

## ★★ Bloque "determinante Se/S" (bitácora del 12/10, ronda 5)

Fuente: `datos/bloque_SeS/` (bitácora + 10 archivos del Drive, carpeta `bloque_determinante_SeS`). Verificación: `scripts/asr_determinante.py` → `asr_determinante.txt`, más los recálculos de R3.

### B1. Se confirma con datos propios

| Afirmación de la bitácora | Verificación |
|---|---|
| 3GZC: cadena A, residuos 29–444 | ✔ (403 residuos resueltos) |
| Asp146 → ligando PLR: 6,29 Å; → SG de Cys388: 3,73 Å | ✔ exacto |
| Bucle `ASVGAACH` desde el 382 | ✔ |
| NFS1 Lys 113 / NFS2 His 106 / SCLY-like algal Pro 51 / dinos + *Guillardia*: Val 5, Pro 1 | ✔ exacto (300 filas). También coincide con el cálculo independiente de R3, que llegó a la columna por otro camino |
| 32 llamadas eucariotas, todas con el ancla Glu-His; Metazoa 14 Asp + *C. elegans* Pro; *Salpingoeca* Asp; *Acanthamoeba*, *Trypanosoma*, *Thalassiosira* y *Chlamydomonas* Pro; *Phytophthora* Val | ✔ |
| *C. elegans* Q19434 es SCLY-like real | ✔ Bucle `ASTGAACHK` (C-H) y contexto `TTNIEH-P` |
| Holozoa monofilético en el árbol de genes | ✔ 16 hojas, soporte 0,999. *C. elegans* sale en la base: artefacto de atracción de ramas largas, como dice la bitácora |
| ASR: raíz Pro; Holozoa Asp; Asp → Pro en el linaje de *C. elegans* | ✔ **Reproducido** sobre una topología estándar reconstruida (el árbol de especies de 23 taxones no está entre los archivos): raíz P 0,90–0,98, Holozoa D 0,93–0,95, Metazoa D 0,99. Robusto a la raíz (Discoba o Amorphea/Diaphoretickes) y a cómo se codifique *Guillardia* |
| Citas: Lobanov 2007, Taskov 2005, Mihara 1999, Collins 2012, Omi 2010 | ✔ en PubMed |

### B2. A corregir

1. **Val: "dos orígenes independientes" no se sostiene en la topología de especies.**
   - *Guillardia* (Cryptista) no es hermana de los dinoflagelados (Alveolata). Agruparlos sale del árbol de genes, donde además el soporte del nodo es 0,000.
   - Sobre la topología estándar, el SAR queda **ambiguo**: P 0,46–0,48 / V 0,52–0,54. Un solo origen de Val en el SAR, con reversión en *Thalassiosira*, es tan parsimonioso como dos orígenes.
   - *Guillardia* tiene **dos copias**: L1J7A3 con Pro y L1J7X1 con Val. Si se la codifica sólo como V, la parsimonia pasa a 5 cambios.
   - **Redacción correcta:** "el estado Val aparece en el SAR (*Phytophthora*, dinoflagelados) y en una de las dos copias de *Guillardia*; el número de orígenes no se resuelve con este muestreo".
2. **"Asp → Pro en la rama terminal de *C. elegans*"** es lo que da *este* muestreo, pero *C. elegans* es el **único ecdisozoo** con el gen (*Drosophila* no lo tiene). La reversión puede estar en cualquier punto entre el MRCA de Ecdysozoa y *C. elegans*. Además, el nodo Ecdysozoa + Lophotrochozoa tiene D 0,91–0,94, no 0,97–0,99. Hay que sumar otros nematodos y algún artrópodo o priapúlido que tenga el gen; la bitácora ya lo propone en el §12.2.
3. **Mk:** la bitácora reporta q = 0,025 con 5 estados; con los 3 estados observados y q por máxima verosimilitud, q = 0,11. Los posteriores bajan un poco (Holozoa 0,973 → 0,94–0,95), pero la conclusión no cambia. Hay que declarar el espacio de estados y cómo se fijó q.
4. **Árbol de especies:** no está entre los archivos. Hay que depositarlo en Newick, con la fuente de la topología.
5. **Que NFS1 lleve Lys "confirma que la columna controla la discriminación Se/S en toda la familia"** es demasiado fuerte. Confirma que es la columna homóloga a la del mutante D146K. Que controle la especificidad en NFS1/NFS2 no está probado, y la SclA bacteriana prefiere Sec con His en esa posición (Johnstone et al. 2021).
6. **"SCLY es suficiente pero no necesaria para usar selenio"** está mal planteado. Que *Tetrahymena*, *Plasmodium* y *Drosophila* usen Sec sin SCLY-like muestra que no es necesaria. "Suficiente" no tiene sentido acá: tener la enzima no hace que un organismo use selenio, y hay proteomas con SCLY-like y sin `Sec_estricto` (23 en el CSV). Mejor: "la presencia de SCLY no es necesaria para usar Sec".
7. **"Una prolina rompe el esqueleto"** → "restringe la conformación del esqueleto (φ fijo, sin donor de puente H)".
8. **Mihara 1999:** los autores son Mihara, Maeda, Fujii, Kurihara, Hata y Esaki ([doi:10.1074/jbc.274.21.14768](https://doi.org/10.1074/jbc.274.21.14768)). **Lobanov 2007:** las 3 selenoproteínas son de *D. pseudoobscura* ([doi:10.1186/gb-2007-8-9-r198](https://doi.org/10.1186/gb-2007-8-9-r198)).
9. **El ligando de 3GZC es PLR** (análogo de PLP), no PLP. La distancia de 6,29 Å es a PLR.
10. **"`SAGxACH` invariante"** (§0, §5, §10 de la bitácora) → **G-x-x-C-H** (R4).
11. **La tabla del §5 se armó sobre las 300 secuencias del árbol.** Le faltan las 11 C-H de R2 y los 5 candidatos de Bolidophyceae (`AAGSAC-E/D`). Antes de escribir "Pro 100 % en algas" hay que ver qué residuo tienen.
12. **Duplicados en `asr_tree.nwk`:** *Thalassiosira* B8BXE3 y *Chlamydomonas* A0A2K3DJ46 aparecen dos veces (ALG y EUK). Igual que con la SCLY humana en el árbol principal, hay que deduplicar.

### B4. Correcciones de la ronda 5 (revisión + verificación propia)

**Ancla Glu-His.** Sólo la His es invariante:
- NFS1: 95 E-H y 19 D-H;
- NFS2: 102 E-H, 1 D-H y 3 N-H;
- SCLY-like: 58/58 E-H.

Decir "ancla (E/D/N)-H, His invariante".

**El nodo de ganancia es Choanozoa, no Holozoa.** El nodo que se reconstruye es *Salpingoeca* + Metazoa, y no hay Ichthyosporea ni Filasterea en el muestreo. Lo único que se puede decir es que el Asp aparece en algún punto del tallo entre Amorphea y Choanozoa. "Innovación holozoa de un solo paso" queda fuera.

**La reconstrucción ancestral depende de supuestos** (`scripts/asr_determinante.py`, sección de sensibilidad):

| Supuesto | Raíz P | Amorphea P | Choanozoa D |
|---|---|---|---|
| Ramas iguales (bitácora) | 0,98 | 0,92 | 0,94 |
| Ramas profundas ×5 | 0,84 | 0,71 | 0,97 |
| Ramas profundas ×10 | 0,73 | 0,58 | 0,98 |
| *Acanthamoeba* y *Trypanosoma* desconocidos (posible HGT) | **0,32** | 0,17 | 0,98 |
| *Salpingoeca* desconocido | 0,98 | 0,95 | **0,49** |

Qué se lee de la tabla:
- **Asp en el linaje animal** es robusto.
- **Pro en la raíz** depende de dos especies, *Acanthamoeba* y *Trypanosoma*. Los grupos externos (NFS1 K, NFS2 H) no ayudan a polarizar P contra D.
- **El momento de la ganancia** depende de un solo coanoflagelado.
- Igualar todas las ramas **no es una elección conservadora**: hace que los nodos profundos parezcan más seguros de lo que son.
- Hay que reportar la parsimonia como resultado principal y el Mk con esta tabla de sensibilidad.

**El árbol de genes tiene más conflictos con el de especies, no sólo *C. elegans*:**
- *Trypanosoma* sale hermano de los holozoos (0,90).
- *Acanthamoeba* cae dentro de las algas (0,13).
- *Salpingoeca* cae dentro de Metazoa, junto a *Capitella* (0,63).

Reconstruir sobre el árbol de especies supone herencia vertical, y ese supuesto hay que declararlo. Para testearlo: árbol de genes restringido a la topología de especies + test AU.

**⚠ *C. elegans* no es una "predicción cumplida".**
- Mi cálculo: el estado Pro aparece en **32 de 47 proteomas** con SCLY-like Pro que pasan `Sec_estricto`, entre ellos *Ostreococcus lucimarinus* (4/4 marcadores, uno de los selenoproteomas eucariotas más grandes), *Micromonas*, *Chlamydomonas* y *Tetradesmus*. El revisor contó ≥ 23 con otro criterio.
- Entonces Pro no marca un uso reducido del selenio, y que *C. elegans* tenga Pro no confirma la hipótesis.
- Además, *C. elegans* **no** desmanteló el sistema: conserva toda la maquinaria de inserción de Sec para TrxR-1 (Taskov et al. 2005, [doi:10.1093/nar/gki507](https://doi.org/10.1093/nar/gki507)).
- **Redacción correcta:** "reversión Asp → Pro en el linaje de *C. elegans*, un organismo de selenoproteoma mínimo. Es anecdótica, porque Pro coexiste con selenoproteomas grandes en algas".

**Correlación estado del residuo ↔ maquinaria Sec:** con estos datos no se puede testear. Asp aparece en un solo evento filogenético, así que el n efectivo es 1. Se reporta como descripción.

**Homología del estado Pro:**
- *Acanthamoeba* y *Trypanosoma* tienen el dipéptido P-A, igual que las algas (P-A[V/I]). Es consistente con un único estado Pro homólogo.
- *C. elegans* tiene P-S: conserva la Ser en +1 de los holozoos (D-S), lo que encaja con una reversión secundaria.
- El cambio es de **dos sitios (PA ↔ DS)**, no de uno. El experimento propuesto tiene que incluir el doble mutante P→D / A→S.

**Literatura que faltaba:**
- **Poliak et al. 2009** (FEBS J 277:383, [doi:10.1111/j.1742-4658.2009.07489.x](https://doi.org/10.1111/j.1742-4658.2009.07489.x)) estudió la SCL de *T. brucei* (Q38DC4), **una enzima con Pro**.
  - Es monofilética con las SCL eucariotas y está en núcleo y citoplasma.
  - Al silenciarla bajan las actividades cisteína desulfurasa y selenocisteína liasa en las fracciones celulares.
  - Es el único precedente funcional de una SCL con Pro, y hay que discutirlo.
  - Por el abstract no se sabe si midieron la especificidad sobre la enzima purificada; hay que leer el paper completo.
- Da Silva et al. 2020 (PLoS NTD, [doi:10.1371/journal.pntd.0008091](https://doi.org/10.1371/journal.pntd.0008091)), sobre la interacción SPS–SCLY en tripanosomátidos, la aportó el revisor y **no la verifiqué**.

**Estructura:** el Asp146 está además a 3,7–4 Å de los residuos 284–287 de la cadena B, en la interfaz del dímero (dato del revisor). La distancia de 6,29 Å al PLR es la mínima entre átomos (N del esqueleto de Asp146 → N1 del PLR), no un contacto de cadena lateral.

**Encuadre para el abstract.** "El estado Asp de la SCLY animal es derivado y el estado Pro está ampliamente distribuido en eucariotas", en lugar de "innovación holozoa de un solo paso".

### B3. Cómo cambia la evaluación global

- La relación con SCLY deja de apoyarse en una sola secuencia humana duplicada: hay 14 metazoos y un coanoflagelado, todos con Asp, en un clado con soporte 0,999 (Choanozoa: no hay holozoos no coanozoos en el muestreo).
- Aparece un **segundo carácter diagnóstico, funcional**: Asp146 (Collins 2012, D146K). Su estado está **polarizado**: Asp es derivado en Holozoa sobre un fondo Pro.
- El encuadre defendible (ver B4) es: el estado Asp de la SCLY animal es derivado (ganado en el tallo Amorphea → Choanozoa) y el estado Pro está ampliamente distribuido. Las limitaciones del §11 de la bitácora están bien declaradas. La predicción experimental (núcleo algal con Pro contra mutante P→D) es concreta y comprobable.
- Sigue pendiente lo de antes: las 11 secuencias C-H, la regla de `clase`, el barrido Sec y el extremo 5'.

---

## ★ Resultados con los datos del proyecto (ronda 4)

Fuente: archivos del Drive (`candidatos_desulfurasas.csv`, `arbol_desulfurasas.nwk`, `msa_desulfurasas_trim.fasta`, `dominios_desulfurasas.fasta`, `conservacion_scly_por_posicion.csv`, `sec_vs_scly_por_proteoma.csv`, `tasas_relativas_pareadas.csv` y tablas chicas), copiados en `review-stage/datos/`. Script: `scripts/recalculo_datos_proyecto.py`. Salida completa: `recalculo_datos_proyecto.txt`. **Donde esta sección contradice al resto del documento, vale esta sección.** En particular:
- Chlorophyta se cuenta como **32/48 proteomas = 30/44 especies** (34/48 y 32/44 si se confirman las 11 de R2). Los "31/48" y "30/48" de §0, §2.9 y §2.15 quedan reemplazados.
- **Los "66" del documento son conjuntos distintos:**
  - **66 del barrido** = 65 algales + SCLY humana (columna `clase` = L3);
  - **66 algales** = 65 del barrido + HText;
  - **66 hojas L3** del árbol = las 66 del barrido.
- Falta documentar en Métodos la regla que produjo la columna `clase`. Sin ella, el paso 617 → 66 no es reproducible.

### R1. La His en +1 es diagnóstica, de forma independiente del bucle

- Sobre los 617 candidatos:
  - SCLY-like: 66/66 con C-H;
  - NFS1: 0/134 (Thr en +1 en el 100 %);
  - NFS2: 0/116;
  - "otro": 11/301.
- **Asignación por mejor cebo** (score phmmer contra cebos de cada familia, sin mirar el bucle), contra His en +1:
  - de las 77 secuencias con C-H, 75 tienen como mejor cebo uno SCLY-like. Las otras 2 son la quimera de *Symbiodinium* (A0A1Q9EC91, 3530 aa) y *Guillardia theta* L1J7X1 (356 aa);
  - en la dirección inversa, sólo 75/110 (68 %) de las secuencias cuyo mejor cebo es SCLY-like tienen C-H: 24 no tienen bucle extraíble y 9 tienen otro residuo en +1 (E/D/S/P);
  - de las 507 cuyo mejor cebo es NFS1 o NFS2, sólo 2 tienen C-H.

  Los dos criterios coinciden en gran medida, pero no son estrictamente independientes: el bucle se extrajo alineando cada candidato contra su mejor cebo, y los cebos SCLY-like llevan C-H. Son *aproximadamente* independientes (el bucle son ~8 de ~390 columnas). La His es un carácter diagnóstico robusto, no sólo un artefacto de la definición del grupo.
- El clasificador automático de bucles del propio CSV (`clase_loop`) etiquetó 58 de las 66 SCLY-like como "I IscS/NFS1". La asignación final, entonces, **no** salió de ese clasificador. Hay que documentar en Métodos qué regla produjo la columna `clase`.

### R2. ⚠ Once secuencias con firma SCLY-like quedaron afuera del clado

Son 11 secuencias de "otro" con C-H, mejor cebo SCLY-like (E-value entre 10⁻³⁴ y 10⁻¹¹⁶; 9 de 11 por debajo de 10⁻⁹²), longitudes de 370–501 aa (salvo una quimera de *Cladocopium* de 2654 aa) y Cys catalítica en posición normal. El hit débil es A0ABR1FWJ4 de *Aureococcus*: score 125, E = 3,7 × 10⁻³⁴, Cys en la posición 235. En el CSV no hay ningún criterio que explique la exclusión: tienen las mismas etiquetas `clase1`/`clase_loop` que miembros aceptados y márgenes de score dentro del rango de las 66. Parece un error del paso de asignación. No están en el árbol:

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

**Bolidophyceae (0/6) es una ausencia blanda.** Hay 5 proteínas de *Triparma*/*Tetraparma* con mejor cebo SCLY-like (E = 10⁻²⁴ a 10⁻⁴⁶). Su bucle es `[IV]AAGSAC-[ED]`: Gly en −3 y Ala en −1, como SCLY-like, pero Glu/Asp en vez de His en +1. El propio CSV las etiqueta "L3 tercera linea". Hay dos lecturas posibles: miembros divergentes del clado que perdieron la His, u otra cosa. En cualquier caso, para Bolidophyceae "ausente" significa "sin la firma C-H", no "sin homólogo del clado". Hay que ubicarlas en el árbol junto con las 11 de R2.

**Antes de escribir:** hay que bajar las 11 secuencias de UniProt, extraer el dominio, agregarlas al alineamiento y verificar que caigan dentro del clado. Es la verificación más urgente de todo el proyecto, porque toca la tabla de distribución y una afirmación de ausencia.

### R3. Asp146 no se conserva en el clado algal

Numeración verificada sobre la secuencia humana del propio dominio: H145, **D146**, K259 (Lys del PLP), C388 (Cys catalítica), H389 (His diagnóstica).

| Grupo | Residuo en la posición de Asp146 (MSA) |
|---|---|
| SCLY humana | **Asp** |
| SCLY-like algales | **Pro 52**, Val 5 (4 dinoflagelados + *Guillardia*), gap 8 (Pro = 52/57 informativas, 91 %; H_L3 = 0,547, apenas por encima del umbral de "conservada") |
| NFS1 | Lys 113, Arg 1, gap 10 |
| NFS2 | His 106, gap 4 |

- Asp146 es el residuo que da a la SCL humana su especificidad por Sec (Collins et al. 2012, [doi:10.1371/journal.pone.0030581](https://doi.org/10.1371/journal.pone.0030581)). Ninguna secuencia algal lo tiene: en su lugar hay una Pro conservada. Coincide con la tabla de conservación (posición 231 del modelo HText: Pro, f = 0,90).
- **Interpretación:** sigue siendo un dato *no informativo* sobre la especificidad, porque la SclA bacteriana prefiere Sec con His en esa posición (Johnstone et al. 2021, [doi:10.1016/j.biochi.2021.01.002](https://doi.org/10.1016/j.biochi.2021.01.002)). Pero es una **divergencia clara respecto de la SCLY de mamífero** en el residuo funcional mejor caracterizado.
- Refuerza que el clado se presente como "relacionado con SCLY" y no como "selenocisteína liasas algales". *(Especulativo: la Pro podría implicar un mecanismo de discriminación distinto; sin datos que lo respalden.)*

### R4. Bucle catalítico de los tres grupos (alineamiento real)

| Posición respecto de la Cys | −5 | −4 | −3 | −2 | −1 | **0** | **+1** | +2 |
|---|---|---|---|---|---|---|---|---|
| NFS1 (124) | S | S | G | S | A | C | **T** (100 %) | S |
| NFS2 (110) | R | S/A | G | H | H | C | **T 58 / A 32 / C 19** | Q |
| SCLY-like (66) | S | A | G | A/S | A | C | **H** (100 %) | S |

- El +1 de NFS2 **no** es "Thr 100 %" ni "Ser": es variable. Esto contradice también al informe del barrido ("NFS2 ni siquiera tiene el bucle extendido"): NFS2 tiene +1 y +2 alineables.
- Fuentes: la fila SCLY-like "H (100 %)" sale de la columna `loop` del CSV (66/66). En el MSA son 60 H + 6 gaps. La fila NFS2 sale del MSA (110).
- En NFS2 hay His en −2 y −1. La exclusividad de SCLY-like es una **His en +1**.
- El −6 también distingue: Ala/Cys en SCLY-like, Val/Ile en NFS1 y NFS2.

### R5. Posiciones discriminantes: el enriquecimiento cerca del cofactor no se sostiene

Con la definición del propio dossier (conservada en las dos familias, H ≤ 0,5, con consenso distinto):

| Comparación | Conservadas en todas | A < 8 Å (base) | Discriminantes | A < 8 Å | Binomial |
|---|---|---|---|---|---|
| SCLY vs NFS1 **y** NFS2 | 38 | 15 (39,5 %) | **2** (S159, G197) | 1 | p = 0,63 |
| SCLY vs NFS1 | 65 | 23 (35,4 %) | 6 (S159, G197, A232, T330, N431, H462) | 4 | p = 0,12 |

- Las "6 posiciones discriminantes" del dossier son discriminantes **sólo contra NFS1**. Contra NFS2, A232, T330, N431 y H462 no están conservadas (H_II = 0,77–1,47).
- Sacando H462 (circular, §2.12): 3 de 5 cerca, p = 0,24.
- Con la base correcta **no hay evidencia** de enriquecimiento cerca del cofactor. El test tiene poca potencia (n = 2–6; el IC 95 % para 4/6 es 0,22–0,96), así que es "no demostrado", no "refutado". La afirmación sale del paper.
- Lo que sí se sostiene es descriptivo: la conservación en SCLY-like decrece con la distancia al ligando (Spearman ρ = −0,48 con f_L3; el p no vale por autocorrelación espacial).
- S159 sí es discriminante contra las dos familias (en la tabla original figuraba "—"), pero está a 23,5 Å del ligando. La tabla original aplicaba sólo diferencia de consenso, sin exigir conservación en NFS2.

### R6. Asociación con la maquinaria Sec: confundida por linaje, sin decidir

- "Sec+" en el CSV (`Sec_estricto`) = PSTK **y** SEPSECS **y** EEFSEC.
- ⚠ **Hay dos barridos de marcadores Sec que no coinciden:**
  - En `sec_vs_scly_por_proteoma.csv`, PSTK está presente en 55/119 proteomas, *C. reinhardtii* incluida. Es el que usa el dossier: OR 3,36, p = 0,0018.
  - En `barrido_desulfurasas_informe.md`, PSTK aparece en 18 proteomas, no recupera *Chlamydomonas* y da OR 1,54, p = 0,45.
  - Hay que decidir cuál es el válido y documentarlo. Mientras tanto, se retira la frase "PSTK se detecta mal" referida al CSV.
- Con el barrido del CSV:
  - Fisher global: OR = 3,36, p = 0,0018.
  - Sólo en algas (sin embriofitas ni no algales, n = 107): OR = 2.87, p = 0.011.
  - **CMH por linaje** (4 estratos informativos, 78/119 proteomas): OR_MH = 1,26, **IC 95 % 0,45–3,52**, p = 0,65. Homogeneidad (Breslow-Day) p = 0,17.
- **Lectura:** la asociación global está en parte confundida por el linaje. Dentro de los linajes el OR agrupado es ~1,3, pero el IC es demasiado ancho para decidir: incluye tanto 1 como el OR global. La pseudorreplicación es plausible, **no demostrada**. Hace falta un test filogenético (Pagel) y un marcador mejor del selenoproteoma (SECIS / TGA internos).

### R7. Árbol y conteos reconciliados

- El árbol tiene **304 hojas**, no 617: 124 NFS1 + 110 NFS2 + 66 SCLY-like (65 algales del barrido + la humana del barrido) + 4 referencias (IscS, SufS, SCLY humana, HText).
  - Las 301 "otro" no están en el árbol.
  - Faltan 16 NFS1/NFS2 de proteomas de contraste (*Drosophila*, *Marchantia*, maíz, arroz, *Selaginella*, *Dictyostelium*, *Plasmodium*, *Tetrahymena*, *Polarella*). Eso explica 134/116 en el CSV contra 124/110 en el árbol y en la conservación.
  - **Corregir "árbol de 617 secuencias"** en el texto y en la figura.
- **Las hojas ya llevaban la etiqueta de clase** (prefijos `I__`, `II__`, `L3__`). El árbol se hizo *después* de asignar, así que es una verificación de monofilia, no un descubrimiento ciego.
- ⚠ **La SCLY humana está dos veces en el árbol** (REF_SCLY_human y L3__Q96I15, secuencias idénticas). "Hermana del clado algal" descansa, entonces, en una sola secuencia de metazoo. Hay que sacar el duplicado y agregar SCLY de otros eucariotas y un grupo externo.
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
| His en +1 diagnóstica | Pendiente / circular | **Sólido con matices**: 0/250 NFS con C-H; 75/77 C-H con mejor cebo SCLY-like, pero sólo 75/110 en la otra dirección; criterios aproximadamente independientes |
| Clado hermano de SCLY humana | Provisorio | Topología presente en el árbol (soporte sólo-algal 0,855, SH), pero con un único metazoo duplicado; sigue faltando muestreo eucariota y grupo externo |
| Ausente en Pelagophyceae | Dato | **Probablemente falso**: 4/4 proteomas con candidatos C-H. Verificar. Bolidophyceae: candidatos sin His (`AAGSAC-E/D`) |
| Diatomeas 14/16 | Dato | Probablemente 16/16 |
| Asp146 | Sin analizar | **Pro conservada en algas; Asp sólo en humana** |
| Discriminantes cerca del cofactor | Pendiente | **Retirado**: p = 0,12–0,63 con la base correcta |
| SCLY ↔ Sec es pseudorreplicación | No demostrada | **Sigue sin decidir**: CMH OR 1,26 (IC 0,45–3,52); en algas solas Fisher sigue siendo significativo; dos barridos Sec no coinciden |
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
