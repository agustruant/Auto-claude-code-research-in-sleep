# Barrido pan-algal de cisteína desulfurasas — hay material

Exploración de la **opción A** de la evaluación previa: tomar el pipeline pan-algal del proyecto y pasarlo con los tres cebos corregidos (NFS1, NFS2 y la "tercera línea" de HText / CHLRE_07g322000).

## Qué se corrió

- **119 proteomas de referencia de UniProt, 2.110.345 secuencias**: los 107 algales del barrido anterior (12 linajes) más 12 de contraste — 6 plantas terrestres (*Arabidopsis*, *Physcomitrium*, *Marchantia*, *Selaginella*, arroz, maíz), humano, *Drosophila*, levadura, *Dictyostelium*, *Tetrahymena* y *Plasmodium*.
- **10 cebos**, tres por familia (At + *Chlamydomonas* + *Scenedesmus* PABB) más las referencias bacterianas IscS, SufS.
- `phmmer` con *Z* igual al universo completo, corte E < 1e-10 → **617 proteínas** de la clase V.
- Clasificación por **bucle catalítico**, extraído alineando cada candidato contra su mejor cebo y mapeando la posición de la Cys catalítica.
- Dominio PF00266 recortado por `hmmsearch`, MSA con FAMSA, columnas con ocupación ≥ 0,35 (386 columnas de 768), árbol ML con VeryFastTree (LG + Γ, 1000 réplicas), enraizado en el clado del grupo II.

## Resultado principal: el clado existe, es monofilético y es hermano de SCLY

El árbol separa limpiamente tres clados:

| clado | n | soporte | firma del bucle |
|---|---|---|---|
| NFS2 / SufS (grupo II) | 116 | **1,00** | `R-x-G-H-H-C` |
| NFS1 / IscS (grupo I) | 134 | 0,79 | `S-S-G-S-A-C-T-S` |
| **SCLY-like** | **66** | **0,96** | `S-A-G-[A/S]-A-C-H-S` |

La firma del tercer clado es casi invariante: de los 66 miembros, **66/66 tienen G en la posición 4, Cys catalítica en la 7 y His inmediatamente después**. Esa His es el carácter diagnóstico — NFS1 lleva Thr en esa posición y NFS2 ni siquiera tiene el bucle extendido.

**El clado no es una familia nueva: es el brazo algal de la selenocisteína liasa (SCLY).** La SCLY humana cae dentro del clado, como rama hermana de los 66 miembros algales. Esto hay que decirlo así en el paper — "familia nueva" no se sostiene, "clado algal de SCLY, nunca descrito ni caracterizado en algas" sí.

Confirmaciones internas que dan confianza en el pipeline:
- Los controles caen donde deben: NFS1 y NFS2 de *Arabidopsis* en sus clados, NFS1 humana y de levadura en el grupo I, IscS y SufS de *E. coli* dentro de sus clados respectivos.
- **HText de *Scenedesmus* PABB cae como hermana de las dos copias de *Tetradesmus obliquus***, que es su pariente más cercano en el muestreo (ambos Scenedesmaceae). La secuencia recortada a mano del trabajo original se comporta filogenéticamente como corresponde.
- En UniProt, el miembro de *Chlamydomonas* (**A0A2K3DJ46**, `CHLRE_07g322000v5`, 491 aa) está anotado sólo como "Aminotransferase class V domain-containing protein", con PANTHER PTHR11601 (cisteína desulfurasa) pero **sin ninguna entrada de familia de InterPro** — ni IPR010240 (IscS) ni IPR010970 (SufS) ni IPR016454. Está literalmente sin asignar.

## Distribución: presente en seis linajes algales, ausente de plantas terrestres

| linaje | proteomas | con NFS1 | con NFS2 | con SCLY-like |
|---|---|---|---|---|
| Chlorophyta | 48 | 41 | 37 | **32** |
| Streptophyta (algas carofitas) | 2 | 2 | 2 | **2** |
| Embryophyta (plantas terrestres) | 6 | 6 | 6 | **0** |
| Rhodophyta | 12 | 12 | 10 | **0** |
| Bacillariophyta (diatomeas) | 16 | 15 | 13 | **14** |
| Haptophyta | 4 | 4 | 3 | **3** |
| Dinophyceae | 10 | 8 | 10 | **4** |
| Cryptophyceae | 1 | 1 | 0 | **1** |
| Xanthophyceae | 1 | 1 | 1 | **1** |
| Bolidophyceae / Pelagophyceae / Eustigmatophyceae / Phaeophyceae | 13 | 13 | 13 | **0** |
| no algales (Metazoa, Fungi, Amoebozoa, Ciliophora, Apicomplexa) | 6 | 6 | 2 | **1** (SCLY humana) |

Total: **66 proteínas en 56 especies de 8 linajes**; 46 especies con una copia y 10 con dos.

El patrón más fuerte es el del linaje verde: **las dos carofitas (*Klebsormidium nitens* y *Chara braunii*) lo tienen, y las seis plantas terrestres no** — hepática, licofita, musgo, dos monocotiledóneas y una dicotiledónea. Es una pérdida en la transición al medio terrestre, con muestreo decente a ambos lados. La segunda ausencia marcada son las algas rojas: 0 de 12, el linaje mejor muestreado después de las clorofitas.

## Lo que se probó y no dio

Se testeó la hipótesis obvia — que el clado acompañe a la maquinaria de selenocisteína, que las plantas terrestres también perdieron. Barriendo los 119 proteomas con cebos humanos de SEPHS2, SEPSECS, PSTK y EEFSEC, **la asociación no es significativa** (PSTK presente en 18 proteomas; Fisher OR = 1,54, p = 0,45). Además la detección de PSTK no es confiable: no recupera *Chlamydomonas reinhardtii*, que tiene selenoproteínas documentadas. La hipótesis queda **no evaluada**, no refutada: hace falta un marcador mejor (el motivo SECIS en los UTR, o el conteo directo de selenoproteínas por TGA interno), que es otro trabajo.

## Veredicto sobre si hay paper

Sí, y es más limpio de lo que esperaba. El armado natural:

1. **Hallazgo**: un clado monofilético de la familia de cisteína desulfurasas, hermano de SCLY animal, presente en seis linajes algales y perdido en plantas terrestres y algas rojas, sin asignación de familia en InterPro y sin ningún miembro caracterizado.
2. **Criterio diagnóstico**: la firma del bucle catalítico `SAGxAC-H`, que lo separa de NFS1 y NFS2 con una sola columna del alineamiento y es automatizable sobre proteomas enteros.
3. **Caso de estudio**: *Scenedesmus* PABB, con los tres genes en el mismo genoma, y el miembro SCLY-like enterrado en un ORF mal anotado de 3383 aa — que es de donde arrancó todo el trabajo.
4. **Consecuencia práctica**: bases de datos de algas etiquetan miembros de este clado como "NFS2" (el caso de `CHLRE_07g322000` en AlgaePath). Cuantificable sobre el set de 66.

Lo que le falta para no ser puramente descriptivo es una predicción funcional contrastable. Las dos más baratas: (a) localización subcelular de los 66 (DeepLoc/TargetP en batch, que ya sabés correr) — si dan plástido sería un dato fuerte, porque SCLY animal es citosólica; (b) co-ocurrencia con un marcador de selenoproteínas mejor elegido.

## Limitaciones a declarar

- Un proteoma de referencia por especie, de UniProt; linajes sin proteoma de referencia (glaucofitas, euglenofitas verdaderas, clorarachniofitas, crisofíceas, rafidofíceas) quedan sin evaluar, no en negativo.
- Cinco linajes están representados por una sola especie (Cryptophyceae, Xanthophyceae, Phaeophyceae y los dos ciliados/amebozoos de contraste): esas celdas no tienen replicación interna.
- El soporte de 0,79 del clado NFS1 refleja que incluye tanto NFS1 eucariotas como IscS; no afecta la delimitación del clado SCLY-like.
- El árbol está enraizado en el grupo II por convención, no por un grupo externo independiente.
- La asignación se hace por bucle catalítico y topología; no se verificó estructura 3D ni se buscó evidencia de expresión para los 66.

## Archivos

- `candidatos_desulfurasas.csv` — las 617 proteínas con clase asignada, bucle catalítico, scores contra los tres grupos de cebos y especie/linaje.
- `distribucion_por_especie.csv` y `presencia_por_proteoma.csv` — conteo de copias por especie.
- `arbol_desulfurasas.nwk`, `msa_desulfurasas_trim.fasta`, `dominios_desulfurasas.fasta` — árbol, alineamiento recortado y dominios PF00266 de entrada.
