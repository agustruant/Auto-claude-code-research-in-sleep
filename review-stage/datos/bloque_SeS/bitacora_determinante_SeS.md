# Bitácora — el determinante de especificidad selenio/azufre

**Agustín Truant** · registro del bloque de trabajo sobre el residuo que decide el sustrato en la familia SCLY
Continuación del expediente `dossier_SCLY_like.md`. Este documento cubre **sólo** este tramo: por qué se buscó, qué se encontró y qué queda abierto.

---

## 0. De dónde se parte

El expediente cerraba con tres resultados firmes —el clado SCLY-like en algas, la firma `SAGxACH` invariante y la curación del locus de PABB004 validada por RNA-seq— y una debilidad conocida: **la hipótesis del selenio se caía al controlar por filogenia**. Dentro de Chlorophyta la asociación entre tener SCLY-like y tener maquinaria Sec daba OR = 1,00, p = 1,00. El efecto global (OR = 3,36) lo generaba la comparación entre linajes, no una asociación real dentro de ellos.

La propuesta inicial para arreglarlo fue ampliar el eje: barrer ~500 proteomas eucariotas para conseguir diez o quince eventos de pérdida independientes en vez de uno, y reencuadrar el paper como "co-eliminación recurrente de la liasa y del selenoproteoma en eucariotas".

**Esa propuesta estaba mal.** Lo detectó el director de este trabajo antes de que se gastara una sola hora de cómputo en ella.

---

## 1. El encuadre propuesto ya estaba publicado

**Lobanov, Fomenko, Zhang, Sengupta, Hatfield y Gladyshev (2007), *Genome Biology* 8:R198**, doi 10.1186/gb-2007-8-9-r198.

El trabajo analiza los selenoproteomas de varios eucariotas modelo, detecta 26 y 29 selenoproteínas en *Ostreococcus tauri* y *O. lucimarinus*, 16 en la diatomea *Thalassiosira pseudonana*, 5 en *Dictyostelium* y 3 en *Drosophila*, y concluye que hubo pérdidas masivas e independientes de selenoproteínas en plantas terrestres, hongos, nematodos, insectos y algunos protistas, con los organismos acuáticos reteniendo selenoproteomas grandes y varios grupos terrestres reduciéndolos.

Es decir: el contraste acuático/terrestre, las pérdidas independientes y el marco macroevolutivo completo están publicados desde 2007, en una revista mejor que las que se estaban apuntando. Insistir por ahí era reescribir un trabajo de hace dieciocho años con más especies.

---

## 2. Relevamiento bibliográfico sistemático

Antes de proponer cualquier otra cosa se hizo el relevamiento que correspondía hacer primero. Consultas sobre Europe PMC (que indexa PubMed, PMC y preprints):

| Consulta | Resultados | Lectura |
|---|---|---|
| `TITLE:"selenocysteine lyase"` | **45** | la familia completa tiene 45 papers en toda la historia |
| idem + evolución / filogenia / distribución | **3** | uno de *Trypanosoma brucei* (2010) y dos de 1982–83 |
| selenoproteoma + pérdida + eucariotas | 7 | dominado por Lobanov 2007 |
| selenoproteínas + algas | 8 | *Chlamydomonas* bien estudiada: Novoselov 2002, SelW1, SelT |
| `TITLE:"cysteine desulfurase"` + algas | **0** | campo virgen |
| misanotación de cisteína desulfurasas | **0** | nadie lo trató |
| co-eliminación de Sec | 0 con ese término | pero Lobanov 2007 lo cubre en sustancia |

**Conclusión del relevamiento.** Los 45 papers de "selenocysteine lyase" son casi todos de fisiología de ratón: knockouts, acumulación de lípidos en adipocitos pardos, dietas, estatinas. **No existe ningún relevamiento filogenético ni de genómica comparada de SCLY como familia génica.**

El motivo es el hallazgo del propio expediente: veinte años de genómica del selenio se ocuparon de las **selenoproteínas** (las que llevan Sec en la cadena) y de la **maquinaria de inserción** (SPS2, SEPSECS, PSTK, eEFSec, tRNA-Sec). **La enzima que recicla el selenio nunca entró en ningún survey**, porque se anota como "cysteine desulfurase" o "aminotransferase class V" y desaparece dentro del montón de las NFS. Era invisible porque no había criterio para separarla.

---

## 3. El trabajo que abre el hueco

Rastreando la literatura mecanística apareció el que importaba:

**Collins, Johansson, Karlberg, Markova, van den Berg, Olesen, Hammarström, Flores, Schüler, Schiavone, Brzezinski, Arnér y Högbom (2012), *PLoS ONE* 7(1):e30581**, doi 10.1371/journal.pone.0030581 — *"Biochemical discrimination between selenium and sulfur 1: a single residue provides selenium specificity to human selenocysteine lyase"*.

Del abstract: las liasas de Sec y las desulfurasas de Cys generalmente actúan sobre ambos sustratos, pero la humana es específica de Sec pese a que la única diferencia entre Sec y Cys es la identidad de un átomo; resuelven la estructura cristalográfica de la enzima humana e identifican **Asp146 como el residuo clave que provee la especificidad por Sec**, y la variante **D146K pierde la especificidad por Sec y aparece actividad de cisteína desulfurasa**.

**Por qué esto es decisivo.** Es el único punto de toda la enzima donde existe una relación causal probada en el banco entre **un residuo** y **qué sustrato come la proteína**. Leerlo en una secuencia no es medir una similitud: es leer una propiedad funcional con respaldo experimental.

Un segundo trabajo del mismo año complementa el mecanismo: **Omi, Kurokawa, Mihara, Hayashi, Goto, Miyahara, Kurihara, Hirotsu y Esaki (2010), *J. Biol. Chem.* 285:12133**, doi 10.1074/jbc.M109.084475, sobre la SCLY de rata (PDB `3A9Z`), que muestra que la reacción pasa por un intermediario selenopersulfuro sobre la Cys375 catalítica y que la cisteína forma un aducto improductivo.

---

## 4. Verificación estructural

Se bajó **PDB `3GZC`** (la estructura de la SCLY humana de ese trabajo) y se midió directamente sobre las coordenadas, en vez de confiar en la numeración del texto.

| Medida | Valor |
|---|---|
| Cadena A | residuos 29–444, numeración de 445 aa |
| Residuo 146 | **Asp**, confirmado |
| Asp146 → PLP (ligando `PLR`) | **6,29 Å** |
| Asp146 → Cys388 catalítica | **3,73 Å** |
| Bucle catalítico | `ASVGAACH` desde el residuo 382 → Cys388, His389 |

El Asp146 está dentro del sitio activo, a distancia de contacto de la cisteína catalítica. Y el bucle de la enzima humana es `ASVGAACH`, que es exactamente la firma `SAGxACH` definida en el expediente. Las dos piezas —la firma de familia y el determinante de sustrato— están en el mismo sitio activo pero en posiciones distintas de la secuencia.

---

## 5. Mapeo sobre las tres familias

Se alinearon los 304 dominios del barrido pan-algal (124 NFS1 + 110 NFS2 + 66 SCLY-like + 4 referencias) con FAMSA y se localizó la columna del Asp146 humano.

**La columna es inequívoca**: en las 304 secuencias hay un **ancla Glu-His invariante** inmediatamente antes de la posición. El alineamiento local tiene 93 % de ocupación en toda la ventana. No es una columna interpretada: es una columna anclada.

| Grupo | Residuo | n | Contexto |
|---|---|---|---|
| NFS1 / IscS (grupo I) | **Lys** 99 % | 114 | `...TEH-K-CVLD...` |
| NFS2 / SufS (grupo II) | **His** 100 % | 106 | `...AEH-H-SCIV...` |
| SCLY humana | **Asp** | 1 | `...VEH-D-SIRL...` |
| SCLY-like algal | **Pro** 100 % | 51 | `...IEH-P-AVIE...` |
| SCLY-like de dinoflagelados y *Guillardia* | **Val** 83 % | 6 | `...ATEH-V-AVLE...` |

Separación perfecta. Cero solapamiento entre grupos.

**El detalle que valida todo el razonamiento:** NFS1 lleva de forma natural **exactamente la misma lisina** que Collins introdujo artificialmente para convertir la SCLY humana en desulfurasa. La mutagénesis de laboratorio recapituló el estado natural del grupo I. Eso confirma, sin asumir nada, que esa columna es la correcta y que controla la discriminación Se/S en toda la familia.

**El clado algal tiene prolina**, no aspártico. Una prolina no es una sustitución cualquiera de cadena lateral: rompe el esqueleto peptídico. Es un estado estructuralmente distinto y nunca caracterizado por nadie.

---

## 6. Barrido eucariota

Para saber si el Asp es ancestral o derivado se amplió el muestreo a **38 proteomas de referencia eucariotas**, recuperando todos los dominios PF00266 de cada uno vía la API de UniProt: metazoos desde esponjas hasta humano, coanoflagelados, hongos (incluidos los quitridios basales *Spizellomyces*, *Batrachochytrium* y *Allomyces*, y el glomeromicete *Rhizophagus*), amebozoos, Discoba, alveolados, estramenópilas y dos controles de Viridiplantae. **330 secuencias clase V** recuperadas.

La identificación de SCLY-like se hizo por **posición en el alineamiento** (el par Cys-His en la columna del bucle catalítico), y cada llamada del determinante se validó exigiendo el ancla Glu-His: **32 de 33 la tienen**. La única que no —`A9V3R6` de *Monosiga brevicollis*— se descartó por falso positivo del motivo.

| Linaje | Asp | Pro | Val | Sin SCLY-like |
|---|---|---|---|---|
| Metazoa | **14** | 1 | 0 | 2 |
| Coanoflagelados | **1** | 0 | 0 | 1 |
| Amebozoos | 0 | 1 | 0 | 1 |
| Discoba | 0 | 1 | 0 | 2 |
| Alveolados | 0 | 0 | 0 | 3 |
| Estramenópilas | 0 | 1 | 1 | 1 |
| Hongos | 0 | 0 | 0 | **6** |
| Viridiplantae | 0 | 1 | 0 | 1 |

Las 14 especies de Metazoa con Asp cubren todo el árbol animal: la esponja *Amphimedon queenslandica*, *Trichoplax adhaerens*, los cnidarios *Nematostella* e *Hydra*, el anélido *Capitella*, el molusco *Crassostrea*, el erizo *Strongylocentrotus*, *Branchiostoma*, *Ciona*, pez cebra, *Xenopus*, gallina, ratón y humano. Y el coanoflagelado *Salpingoeca rosetta* —el pariente unicelular más cercano de los animales— también lo tiene.

**Fuera de ese clado el Asp no aparece en ninguna parte.** Afuera hay Pro: *Acanthamoeba castellanii*, *Trypanosoma brucei*, *Thalassiosira pseudonana*, *Chlamydomonas reinhardtii* y las 45 especies algales del barrido previo. Val en *Phytophthora infestans* y en los cuatro dinoflagelados más *Guillardia theta*.

---

## 7. La excepción, que es el mejor dato del bloque

Dentro de Metazoa hay **una sola especie con Pro en vez de Asp: *Caenorhabditis elegans***.

Y *C. elegans* es, de lejos, el metazoo con el selenoproteoma más reducido que se conoce: conserva **una sola selenoproteína**, la tiorredoxina reductasa TRXR-1. Es el único animal que desmanteló casi por completo el sistema del selenio (Taskov *et al.*, 2005, *Nucleic Acids Res.* 33:2227 — "Nematode selenoproteome: the use of the selenocysteine insertion system to decode one codon in an animal genome").

El único animal que revirtió el determinante de especificidad es el único animal que perdió el selenoproteoma. Es **n = 1** y hay que escribirlo así, pero es exactamente la predicción que hace la hipótesis, cumplida en el caso límite y en un linaje completamente independiente de las algas.

---

## 8. Los contraejemplos, que hay que declarar

La co-ocurrencia **no es estricta**, y conviene decirlo antes de que lo diga un revisor:

- ***Tetrahymena thermophila*** y ***Plasmodium falciparum*** tienen maquinaria Sec y selenoproteínas documentadas, y **no** tienen SCLY-like.
- ***Drosophila melanogaster*** tiene tres selenoproteínas y tampoco la tiene.

La formulación defendible es: **SCLY es suficiente pero no necesaria para usar selenio.** Probablemente porque las desulfurasas convencionales pueden hacer el trabajo con menor eficiencia — está documentado desde **Mihara, Kurihara, Watanabe, Yoshimura y Esaki (1999), *J. Biol. Chem.* 274:14768**, que muestra que CsdB de *E. coli* (= SufS) es la contraparte bacteriana de la liasa de selenocisteína de mamífero.

Las ausencias que sí refuerzan el cuadro: **los seis hongos**, incluidos los quitridios basales, no tienen SCLY-like por ninguno de los dos criterios (columna alineada y barrido de motivo permisivo). Los hongos perdieron Sec y perdieron la liasa. *Arabidopsis thaliana*, el control, tampoco la tiene.

---

## 9. Reconstrucción ancestral — y el árbol de genes que mentía

Se construyó un árbol de máxima verosimilitud del clado con **100 secuencias** (65 dominios algales + 21 eucariotas no algales + 14 de grupo externo), alineadas con FAMSA, recortadas a 374 columnas con ocupación ≥ 0,5, y VeryFastTree con LG+Γ y 1000 réplicas.

**El árbol de genes colocó a *C. elegans* como rama hermana de todos los demás holozoos, incluido el coanoflagelado, con soporte 0,999.**

Eso es filogenéticamente imposible: un nematodo es un bilaterio, no puede ser hermano de un clado que contiene un coanoflagelado. Es **atracción de ramas largas** — las secuencias de nematodo son notoriamente divergentes y se van a la base del árbol. Y la reconstrucción sobre ese árbol daba la historia equivocada: Pro en la raíz de Holozoa y el Asp apareciendo recién después de que divergieran los nematodos.

**Por eso la reconstrucción se hizo sobre la topología de especies aceptada**, que para ortólogos 1:1 es lo que corresponde: la filogenia animal no es algo que haya que inferir de estas 100 secuencias. Se armó un árbol de 23 taxones con la topología estándar de eucariotas (Amorphea con amebozoos y holozoos, Diaphoretickes con Archaeplastida y TSAR, Discoba en la base) y la topología animal estándar (coanoflagelados hermanos de Metazoa; poríferos, placozoos, cnidarios, bilaterios).

**Parsimonia de Fitch:** 4 cambios mínimos en 23 taxones, raíz eucariota en Pro.

**Modelo Mk** (tasa única simétrica entre cinco estados, q = 0,025, reconstrucción marginal por doble pasada):

| Nodo | Estado | Posterior |
|---|---|---|
| Raíz eucariota | **Pro** | 0,994 |
| MRCA Amorphea | Pro | 0,969 |
| **MRCA Holozoa** | **Asp** | **0,973** |
| MRCA Metazoa | Asp | 0,999 |
| MRCA Bilateria | Asp | 0,999 |
| Rama madre de *C. elegans* | Asp | 0,971 |
| MRCA Diaphoretickes | Pro | 0,983 |

**Cuatro eventos, cada uno único:**

1. **Pro → Asp, una sola vez, en el tronco de los holozoos**, antes de la separación entre coanoflagelados y animales.
2. **Asp → Pro, una sola vez, en la rama terminal de *C. elegans***. El nodo padre es Asp con p = 0,971, así que el cambio está en esa rama y en ninguna otra.
3 y 4. **Dos orígenes independientes de Val** del lado SAR/Hacrobia: uno en *Phytophthora* y otro en el grupo dinoflagelados + *Guillardia*.

---

## 10. Qué cambia para el paper

**Antes de este bloque** había un clado de proteínas que se parecen a la SCLY humana y que caen al lado de ella en un árbol. A eso un revisor contesta en una línea: parecerse no es hacer lo mismo.

**Después de este bloque hay cuatro cosas que antes no estaban:**

1. **Un segundo carácter diagnóstico, independiente del primero.** El bucle `SAGxACH` dice a qué familia pertenece la proteína; este residuo dice qué sustrato prefiere. Dos posiciones distintas del mismo sitio activo, con respaldos distintos. Hay que tumbar las dos.
2. **Una corrección que evita una afirmación de más.** Las algas tienen Pro, no el Asp humano. Escribir "descubrimos selenocisteína liasas en algas" era exponerse a que un revisor que conoce ese paper lo marcara. La versión correcta es más interesante: son del clado SCLY pero con un estado propio en el residuo de especificidad, nunca caracterizado.
3. **Un evento evolutivo puntual y polarizado**, con posterior, en vez de un mapa de presencia y ausencia. Y con un correlato metabólico independiente en el caso límite.
4. **Una predicción falsable con dos construcciones.** Expresar el núcleo algal con Pro y su variante P→D, y medir actividad sobre cisteína y sobre selenocisteína. Si el Pro da especificidad relajada y el Asp la vuelve estricta, la predicción se cumple.

Y el resultado más vistoso para el abstract: **la especificidad estricta por selenio de la SCLY humana —el marco de toda la literatura de la enzima desde los años ochenta— no es la condición por defecto de la familia. Es una innovación holozoa, de un solo paso, sobre un fondo eucariota de especificidad relajada.**

---

## 11. Limitaciones, declaradas

1. **No se demostró que las enzimas algales degraden selenocisteína.** Lo que se sabe es que no tienen el determinante de especificidad estricta de los mamíferos. El estado Pro no está caracterizado por nadie. Es un dato, no una conclusión funcional.
2. **La cobertura de holozoos basales es fina.** Un solo coanoflagelado con la enzima, una esponja, un placozoo. El nodo de ganancia tiene p = 0,973 pero descansa en pocos taxones a cada lado.
3. **El árbol de genes y la topología de especies no coinciden** en la posición de *C. elegans*, y la reconstrucción se hizo sobre la segunda. Hay que decirlo explícitamente en métodos.
4. **El modelo Mk usa una tasa única simétrica** y longitudes de rama iguales dentro del árbol de especies. Es la elección conservadora para un carácter discreto cuando la pregunta es de polaridad, no de tasas, pero es una elección y hay que declararla. La parsimonia, que no usa longitudes de rama, da la misma respuesta.
5. **La co-ocurrencia con la maquinaria Sec no es estricta** (§8).
6. **El estado Val tiene n = 6** y aparece en dos linajes no relacionados. Puede ser convergencia real o un artefacto de muestreo escaso.
7. **Falta la tercera línea de Archaeplastida:** no hay ni una glaucofita en todo el análisis. *Cyanophora paradoxa* tiene genoma pero no proteoma anotado en UniProt.

---

## 12. Qué sigue

**Prioridad alta**

1. **Densificar los holozoos basales.** Sumar un par de coanoflagelados más, un ctenóforo (*Mnemiopsis*), *Capsaspora owczarzaki* e *Ichthyosporea*. Es lo que blinda el nodo de ganancia, y son proteomas disponibles.
2. **Verificar el estado en más nematodos.** Si otras especies de nematodo con selenoproteoma reducido también tienen Pro, el caso de *C. elegans* deja de ser n = 1 y pasa a ser un patrón de linaje.
3. **El selenoproteoma de PABB004** por TGA en marco y horquillas SECIS, sobre el genoma y el RNA-seq propios. Sigue siendo el mejor ancla funcional a nivel de organismo.
4. **Modelar el entorno del Pro** en la estructura algal: ver si la prolina desplaza el esqueleto de manera que agrande o achique el subsitio respecto del Asp humano. Es barato con los modelos que ya existen.

**Prioridad media**

5. Correlacionar el **estado del residuo** (carácter de tres o cuatro estados) con la presencia de maquinaria Sec, en vez de la presencia/ausencia binaria del gen. Tiene mucha más información filogenética.
6. **Glaucofitas y rodofitas ampliadas** vía tBLASTn sobre ensamblados, ya que no hay proteomas.
7. Revisar si el estado **Val** en *Phytophthora* y en dinoflagelados/criptofita es convergencia real.

**No hacer**

- Reencuadrar el paper como pérdida recurrente del selenoproteoma. Ese es el terreno de Lobanov 2007 y el trabajo pierde por comparación.
- Docking de Cys contra Sec. La diferencia energética está muy por debajo del error de las funciones de puntuación empíricas.

---

## 13. Referencias del bloque

| Trabajo | DOI / referencia | Para qué se usa |
|---|---|---|
| Collins *et al.* 2012, *PLoS ONE* 7:e30581 | 10.1371/journal.pone.0030581 | Asp146 como determinante de especificidad Se; variante D146K; estructura `3GZC` |
| Omi *et al.* 2010, *J. Biol. Chem.* 285:12133 | 10.1074/jbc.M109.084475 | mecanismo de la SCLY de rata; intermediario selenopersulfuro; `3A9Z` |
| Lobanov *et al.* 2007, *Genome Biology* 8:R198 | 10.1186/gb-2007-8-9-r198 | pérdidas independientes del selenoproteoma; contraste acuático/terrestre |
| Mihara *et al.* 1999, *J. Biol. Chem.* 274:14768 | — | CsdB de *E. coli* como contraparte bacteriana de la liasa de Sec |
| Taskov *et al.* 2005, *Nucleic Acids Res.* 33:2227 | — | selenoproteoma de nematodos: una sola selenoproteína en *C. elegans* |
| Novoselov *et al.* 2002, *EMBO J.* 21:3681 | — | selenoproteínas y maquinaria Sec en *Chlamydomonas* |

---

## 14. Archivos de este bloque

| Archivo | Contenido |
|---|---|
| `fig_determinante_SeS.png` | los cuatro estados del determinante en las tres familias, con el ancla Glu-His |
| `fig_determinante_eucariotas.png` | el estado por linaje eucariota en los 38 proteomas |
| `fig_reconstruccion_ancestral.png` | la reconstrucción sobre la topología de especies |
| `determinante_especificidad_Se.csv` | residuo y contexto para las 304 secuencias del barrido pan-algal |
| `determinante_eucariotas.csv` | las 32 llamadas eucariotas con bucle, contexto y validación del ancla |
| `determinante_por_especie_eucariotas.csv` | el estado consolidado por especie |
| `asr_resultados.json` | posteriores por nodo y parámetro del modelo Mk |
| `asr_tree.nwk` | el árbol de genes de 100 secuencias, con el artefacto documentado |
| `asr_msa.fasta` | el alineamiento recortado de las 100 secuencias |
| `3GZC.pdb` | la estructura de la SCLY humana, de donde salen las distancias |
| `relevamiento_bibliografico.csv` | las consultas de Europe PMC con sus recuentos |

---

*Fin de la bitácora.*
