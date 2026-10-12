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

