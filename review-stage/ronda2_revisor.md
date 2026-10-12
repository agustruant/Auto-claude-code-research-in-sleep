# Ronda 2 — respuesta del revisor (copia fiel; subagente Claude, misma familia que el ejecutor)

Score: 5/10 (GBE/BMC Genomics, as revised now)
Verdict: not ready

Verification done: read round-1 review, all of DOSSIER_REVISADO.md, and original sections not rewritten (§2.4, §2.6 table, §2.7, §2.11–2.12, methods table, §4 master table, §5.1); recomputed from scly_like_localizacion.csv with own pandas code; checked all 5 new references in PubMed.

Numbers verified correct against CSV: 67 SCLY-like rows = 66 algal + human; 56 algal species; lineage table 34/31, 19/14, 4/4, 4/3, 2/2, 2/1, 1/1; S_loc = 60 (the 6 excluded = 3 fragments [Cyclotella, Chloropicon, Haematococcus], 2 dinoflagellate chimeras, HText); DeepLoc labels 24/15/13/3/2/2/1; 7/60 with Plastid in label; 13/60 P(plastid) > 0.5; by lineage Chloro 10/31, Bacill 1/18, Hapto 1/4, Strepto 1/2; medians 0.65/0.64/0.14/0.17; TargetP 47/5/4/4; SignalP 59/60; 0 TM; controls DeepLoc 5/7, combined 4/7, green-algal plastid controls DeepLoc 1/2 and TargetP 0/2; human SCLY Cytoplasm 0.79/OTHER; loop frequencies S63, A61, G66, A/S 49/17, A64, C66, H66; arithmetic 0.132^4 = 3.0e-4, P(≥4/6) = 0.0037, e^-3.2 = 0.041, 29/0.9 → 3.2 expected; 0/29 gives one-sided 95% upper bound ≈ 9.8% so "excludes >~10%" holds; 2/2^38 = 7.3e-12.

Literature (all 5 DOIs resolve in PubMed to the stated papers): Collins 2012 (Asp146, D146K loses Sec specificity and gains CD activity) correct; Omi 2010 (selenopersulfide on catalytically essential Cys375; flexible loop positions Sec not Cys) correct; Mihara 2000 JBC (mouse SCL distantly related to NifS, cytosolic) correct; Mihara 2000 J Biochem (Cys→Ala mutants of CSD/CsdB/IscS lose almost all Cys activity, much less Sec) correct — nuance: Omi shows the Cys is essential for rat SCL itself, so the text should not imply SCL's Cys is dispensable; Johnstone 2021 (His100 = Asp146-equivalent of SclA, not required for Sec specificity) correct.

Round-1 items:
1 Localization — fixed (recompute + text); new-analysis pending; untouched sections contradict (N2, N3).
2 Counts — partial: §0 definitions, 31/48, 13 stramenopiles fixed; tree clade "n = 66" (§2.7/§4 = 65 algal + human, HText inside) not reconciled with S_alg = 66 / S_tot = 67; 134/116 vs 124/110, 386 vs 348, Drosophila pending; §4 master table untouched.
3 Circularity — partial: reframed and contingency table requested, but the original methods table already states "Bucle catalítico = criterio primario de asignación de familia", so it should be resolved now (N5).
4 Loop biochemistry — partial: Asp146/literature added, "grupo III" dropped in revised text; +1 residue in NFS1/NFS2 pending, yet "Thr 100%" in §2.12 kept as basis for a discriminating position (N4).
5 Orthology — fixed (text); analysis pending.
6 Tree methods — fixed (text); IQ-TREE pending.
7 Rate test — fixed (text); §4 master table still lists p = 7e-12.
8 Conservation — mostly fixed (4 positions, ρ dropped from §7); enrichment test wrong baseline (N1).
9 RNA-seq — fixed (text); Poisson reasoning sound; counting details and 21.9 M vs 60.2 M pending.
10 Losses / "7 lineages" — fixed (text).
11 Sec association — partial: CMH/Pagel/Sec+ definition pending; CMH needs no new data.
12 Minor — partial: §9 overclaims fixed; CSV still uses HText crop and the dossier never says the curated protein (missing ~60 N-terminal residues) cannot be localized at all.

New issues, ranked:
N1. Enrichment test uses the wrong null and includes a circular position [RECOMPUTE]+[TEXT]. "Discriminating" requires conservation in both groups, and the dossier shows conserved positions are strongly enriched near the cofactor (median 0.924 < 8 Å vs 0.363 ≥ 15 Å), so p = 0.132 (share of all 348 within 8 Å) is anticonservative. Correct baseline: share of < 8 Å positions among positions conserved in both families (computable from the entropy + distance tables). H462 is the loop His adjacent to the catalytic Cys — near the cofactor by construction and circular if assignment used the loop. Fix: drop H462 or justify, recompute with conditional baseline, lower §7 "Apoyado" until then.
N2. Untouched original sections now contradict the revision [TEXT]: §2.4 "sólo 2 de 61 plastidiales, mediana 0,13" and HText plastid call (0.95) as "artefacto", repeated in §5.1 — under revised §2.10, "artefacto" no longer supported; call it "uninterpretable (boundaries uncertain)". Methods table "TargetP falló los dos controles de PABB004" — it also failed CrNFS2 (mTP). §4 master table still lists 61/73, 0.13, 6 discriminating positions, ρ with p, TM 0.99 as evidence, rate p, "7 linajes". §2.12 text and §2.6 table still say "SAGxACH" and "grupo III". Fix: edit every untouched section or mark superseded.
N3. Small factual errors in revised §2.10/§6 [TEXT]: the 5th TargetP "SP" is Chara braunii (A0A388KLW8), not Klebsormidium; §6.2 "22 % del clado (10/31 Chlorophyta)" — 22% is 13/60, 10/31 is 32%; "prasinofitas y clorofíceas, un tercio" — the 10 include Elliptochloris (Trebouxiophyceae) and the 13 include Klebsormidium, Diacronema, Pseudo-nitzschia; say "Chlorophyta 10/31".
N4. +1 residue "pending" yet used as a result [TEXT]: §1.2 states IscS Thr at +1 (likely correct, …ACTS…), SufS unresolved; §2.12 still counts H462 (His vs pooled "Thr 100%") as discriminating; if SufS has Ala there the pooled Thr 100% is wrong (my SufS-Ala recollection unverified). Flag H462 pending until ±8 alignment exists.
N5. Circularity already answerable [TEXT]: methods table names the loop as primary assignment criterion; unless Methods show membership came only from tree bipartition, remove §2.8 entropy now.
N6. Overcorrection on localization [TEXT]: "predictores subestiman el plástido: un falso negativo y ningún falso positivo" rests on 1 FN among 3 green-algal plastid controls; only non-plastid controls are NFS1s. Say "may under-call plastid; n too small to estimate bias direction"; keep neutral.
N7. Asp146 framing contradicts own citation [TEXT]: "if not Asp, argument against Sec specificity" conflicts with Johnstone 2021 (non-Asp His SclA still Sec-preferring); non-Asp is uninformative.
N8. Sister-to-human / count mismatches [TEXT], resolvable with [NEW-ANALYSIS]: 0.96 SH is for the clade including human; algal-only bipartition support unreported; with one metazoan and group-II root, "Sólido como topología" overstated. §1.5 still says sweep recovers 66/56 while §0 says it may be 65/55.

What is now correct: all CSV-derived localization numbers and control table; G-x-x-C-H signature and frequencies; corrected Chlorophyta and stramenopile counts; SH-like/CAT terminology; withdrawal of "same as IQ-TREE", "ortholog — blindado", "no es plastidial", rate test and ρ from §7; Poisson treatment of 0 vs 29; read-through demoted; HISAT2 error removed; 3′-only scope of curation; loss claims restricted; §9 overclaims removed; 5 citations real and essentially correctly characterized; revised §7 honest.

Why 5/10: defensible core = clade with SH 0.96 in an approximate tree, sister to one human sequence, plus misannotation fix and 3′ gene-model repair backed by RNA-seq — sound but thin for GBE/BMC Genomics. Four essential blockers remain (Asp146 equivalent, His contingency table, outgroup-rooted IQ-TREE with more non-algal SCLY, three-group loop alignment) plus unfinished count reconciliation. Score rose from 4 because claims were correctly cut back, not because new evidence was added.
