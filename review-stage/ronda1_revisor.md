# Ronda 1 — respuesta del revisor (copia fiel; subagente Claude, misma familia que el ejecutor)

Score: 4/10 (for GBE/BMC Genomics, as described now)
Verdict: not ready

Method: I read all 1,119 lines of paper_texto.txt, recomputed every localization number from scly_like_localizacion.csv (73 rows) with pandas, and viewed fig_localizacion_scly.png. Tree/alignment/RNA-seq claims are judged on internal consistency only. No files modified.

## Ranked weaknesses (most severe first)

1. The headline "not plastidial" (§2.10, §6.19, §7, figure title) is contradicted by the CSV. [RECOMPUTE]+[TEXT]; proper fix [NEW-ANALYSIS]
- Of the 61 "reliable" SCLY-like, the text says "only 2 of 61 predicted plastidial" — that counts only the bare "Plastid" label. 7/61 have Plastid in the DeepLoc label (2 Plastid, 3 Mito|Plastid, 2 Cyto|Mito|Plastid), and 13/61 (21%) have plastid probability > 0.5, clustered in green algae/prasinophytes: Chloropicon 0.96, Elliptochloris 0.93 (TargetP cTP), Cymbomonas 0.86 (TargetP cTP), Ostreococcus 0.78, Micromonas 0.76, C. eustigma 0.74, and the C. reinhardtii PNW80545/A0A2K3DJ46 itself 0.52. The figure's left panel visibly shows ~13 points above the 0.5 line under the title "Las 61 SCLY-like no van al plástido".
- The control panel failed mainly on plastid, the opposite of what the text says ("only thing the panel never failed on"): Chlamydomonas NFS2 (A0A2K3D4F5), a true plastid protein, got DeepLoc Mito 0.93 / Plastid 0.34 and TargetP mTP (TargetP failing here is not mentioned in the text); NFS2_PABB got TargetP OTHER. So for green-algal plastid controls: DeepLoc 1/2 missed, TargetP 2/2 missed. The only cyto/mito failure is NFS1_PABB — §6.19 "failed 3 of 7 on cyto vs mito" inverts what happened. Arabidopsis controls are likely in the predictors' training data (easy cases).
- Secondary-plastid lineages (diatoms, haptophytes, cryptophytes, dinoflagellates) use bipartite SP+transit targeting; DeepLoc/TargetP-Plant are not built for this. The 5 TargetP "SP" calls are 2 Cylindrotheca, 1 Fistulifera, 1 Diacronema (+Chara) — in secondary-plastid algae an SP call is what a bipartite plastid-targeting sequence looks like, not evidence against plastid.
- Minimum fix: [RECOMPUTE] report all DeepLoc categories (the table's 25+15+13+2 = 55 omits 6: 3 Mito|Plastid, 2 Cyto|Mito|Plastid, 1 Extracellular) and the 13/61 > 0.5 per lineage; [TEXT] drop "blindado: no es plastidial", say "plastid targeting not predicted for most; unresolved in prasinophytes/Chlorophyceae"; [NEW-ANALYSIS] ASAFind/HECTAR for secondary-plastid lineages, PredAlgo for Chlorophyta, algal cytosolic controls.

2. Sequence and species counts do not reconcile. [RECOMPUTE]+[TEXT]
- CSV: 67 SCLY-like rows = 66 algal (including the manual HText crop, aa 1900–2400, 501 aa — not the curated 421 aa protein) + human Q96I15. Dossier says variously "66 proteins in 56 species of 7 algal lineages" (§1, §2.9), "human sister to the 65 algal sequences" (§2.7, i.e. 66 includes human), HText "sister to the two Tetradesmus copies" (so HText is in the tree → 67?), "9 of 67 aberrant" (§4), and entropy "66/66" (in the CSV the 66 with loop data include human and exclude HText). Pick one definition and use it everywhere.
- §2.9 table numerators sum to 57 species (32+14+4+3+2+1+1), not 56. CSV has 31 Chlorophyta species (not 32), and that 31 includes Scenedesmus PABB004 whose sequence is a manual crop, apparently not from the 119-proteome sweep — if so it should not count in "x/48".
- "Absent in 14 non-diatom stramenopile proteomes" (§1): Bolido 6 + Pelago 4 + Eustig 2 + Phaeo 1 = 13 absent; the 14th (Xanthophyceae) has the gene.
- Clade sizes 134 NFS1 / 116 NFS2 in the tree (§2.7) vs 124/110 in the conservation alignment (§2.12), unexplained. Conservation columns 353 vs 348 vs 386.
- Control panel: CSV has 6 controls (+ human SCLY marked rol=SCLY-like); the figure's own markers show 5 filled of 7 (DeepLoc-only accuracy) while its title says "4 de 7" — 4/7 only works if TargetP is combined, which the text does inconsistently. Human Q96I15 is counted among "the 61 SCLY-like" localization results.

3. Circularity of the "invariant signature" (§2.6–2.8, §7). [TEXT], ideally [NEW-ANALYSIS]
- §2.6 and §3 table say the catalytic loop (the His) is "the primary criterion for family assignment". If clade membership/curation used the His, entropy = 0.000 at that His is true by construction. State explicitly whether the 66 were defined purely by tree bipartition, and report (a) how many sequences inside the tree clade lack C-H (apparently 0, if true) and (b) how many of the 301 unassigned + NFS1/NFS2 carry C-H. That 2×2 table is the real diagnostic test.
- Only G, C, H are invariant; "SAGxACH" is not: CSV gives S at pos2 63/66, A at pos3 61/66, A at pos6 64/66 (2 have S). §7 "identified by the SAGxACH loop — blindado" should be "G-x-x-C-H". Zero entropy at fully conserved catalytic residues across 66 sequences is unremarkable for an active site; "not one substitution in a billion years" is rhetoric.

4. Catalytic-loop biochemistry is internally inconsistent and partly wrong (§1, §2.6, §2.12). [TEXT]
- §1 says the residue after the catalytic Cys is Ser/Thr in NFS1 and Ser in NFS2; §2.12 says the equivalent position is "Thr 100%" in NFS1/NFS2. My recollection (fairly confident, please verify): group II SufS/CsdB motif is R-x-G-H-H-C-A, i.e. residue after Cys is Ala, not Ser/Thr; E. coli IscS reads …S-G-S-A-C-T-S…, so Thr there is right. Group I and II loops differ in length, so "equivalent position" is alignment-dependent — show the actual alignment.
- The group II "R-x-G-H-H-C" places a His before the Cys; state precisely the His position relative to Cys so it is clear the His itself is not unique to SCLY.
- Human SCLY: CSV gives ASVGAACHSDHGDQ, so His-after-Cys is supported for human (I recall human Cys388; rat SCLY Cys375).
- "Grupo III" naming collides with Mihara's group I/II literature; my uncertain recollection is that mammalian SCLY has been grouped with group I NifS-like proteins — check and cite.
- The "specificity subsite" (Asn25 of rat) ignores the literature residue: Omi et al. 2010 (3A9Z paper) and Collins et al. 2012 identified Asp146 (rat/human) as the key Sec-vs-Cys discriminator (moderately confident). The dossier must discuss Asp146 conservation in the algal clade.
- PDB/residue facts look right: IscS Cys328, SufS/CsdB Cys364, 1KMK = CsdB perselenide (Lima 2003), 1P3W = IscS with Lys206, 3A9Z = rat SCLY with selenopropionate.

5. "It is the algal ortholog of SCLY — blindado" is a non sequitur (§7). [TEXT]+[NEW-ANALYSIS]
- The supporting "TM 0.99 with 3A9Z" is human SCLY model vs rat SCLY crystal — trivial, says nothing about the algal clade. Orthology is argued from a single metazoan sequence being sister. Drosophila was in the contrast set but its result is never reported (absence row lists only fungi, amoebozoa, ciliates, apicomplexans). Fix: add more animal/other-eukaryote SCLY homologs and show the algal clade nests with eukaryotic SCLY under a proper outgroup; until then "SCLY-related clade".

6. Tree methodology (§2.7, §3). [TEXT], proper fix [NEW-ANALYSIS]
- VeryFastTree (like FastTree) reports SH-like local supports from 1,000 resamplings, not bootstrap replicates; "1000 réplicas de soporte" misleads, and 0.96/0.79 are not bootstrap percentages. FastTree-type "LG+Γ" is CAT-approximation + Gamma20 rescale, not full ML optimisation. "Gives the same result as RAxML/IQ-TREE" is asserted without having been run.
- Rooting on group II is arbitrary; the 301 unassigned class-V sequences are the natural outgroup. 0.35 occupancy trim fine but needs a sensitivity check.
- Minimum fix: IQ-TREE with ModelFinder (LG+C20/C60 class), UFBoot2 + SH-aLRT, outgroup rooting; cheap on 316–617 sequences.

7. Evolutionary-rate test is invalid as framed (§2.14, §7 "blindado"). [TEXT]+[NEW-ANALYSIS]
- Root-to-tip distance from each clade's own MRCA confounds rate with clade depth; MRCAs differ in age/composition (SCLY includes the human lineage; NFS2 in secondary-plastid algae may come from EGT).
- Tips share internal branches, so the 38 pairs are phylogenetically non-independent; Wilcoxon p-values anti-conservative. p = 7×10⁻¹² is exactly the exact two-sided minimum for n = 38 (2/2³⁸ = 7.28×10⁻¹²): 38/38 pairs go the same way, which is what a systematic depth artifact would produce.
- Unspecified: how paralogs (species with 2 copies) were paired; whether NFS1 membership is reliable given its 0.79 support. The table labels SCLY "(citosólico)", contradicting §2.10.
- Minimum fix: demote to descriptive; better: per-species terminal branch lengths, a relative-rate test against a common outgroup, or dN/dS. Remove from §7 "blindado".

8. Conservation statistics (§2.12, §7). [TEXT]+[RECOMPUTE-able from the authors' own tables]
- ρ = −0.54, p = 2×10⁻²⁷ treats 348 structurally autocorrelated positions as independent; that p is meaningless. "Conserved near the cofactor" is a generic property of enzymes. §7 uses that ρ to support "discriminating positions are near the cofactor" — a different claim.
- Right test: 46/348 positions (13.2%) are < 8 Å; binomial P(≥4 of 6 | p = 0.132) ≈ 0.004 — genuinely supportive, but caveat spatial non-independence / use permutation.
- Two of the 6 "discriminating" positions have "—" for NFS: under the stated definition (conserved in both, different consensus) they do not qualify → 4, not 6. Pooling NFS1+NFS2 as one "family" contradicts "H ≤ 0.5 in both".

9. RNA-seq k-mer validation is overclaimed (§2.13, §7). [TEXT]+[NEW-ANALYSIS]
- Exact 32-mer junction counting is a sound minimal method, provided each junction k-mer is checked to be unique in genome/transcriptome and overhang placement (single centred k-mer vs all tiling k-mers) is stated.
- The zero is informative relative to 29 on the curated junction (Poisson expectation ~20–30 → P(0) tiny), so "the annotator's junction is not the major isoform" is fair; it cannot exclude a minor alternative isoform (< ~5–10%). "No es poca evidencia: es ninguna" over 21.9 M reads is rhetorically wrong — locus depth matters (internal control exon = 9 reads), not library size.
- The 53 "read-through" reads are not splicing evidence — unspliced pre-mRNA and gDNA contamination produce the same k-mers.
- Junction 29 and read-through 53 exceed the internal SCLY exon (9) — explain (counting per k-mer vs per read?). Only 21.9 M of a 60.2 M-pair run, one run/condition.
- "The curated model is the correct one" (§7) is overclaimed: 5′ end/start codon unresolved, ~60 N-terminal residues missing, and the curated gene has 2 exons vs 9 in the NREL ortholog — losing 7 introns between congeners is unusual and suggests upstream exons are still missed. Say "the 3′ structure (last intron and recovered C-terminus) is supported".
- Factual error: "HISAT2 and STAR are Linux-only" is wrong (macOS via bioconda/source; Windows via WSL). Remove and do the alignment (HISAT2/STAR + StringTie).

10. Loss inferences (§2.9, §9 "two independent losses"). [TEXT]+[NEW-ANALYSIS]
- "Loss at terrestrialization" needs Zygnematophyceae (sister to land plants); Chara/Klebsormidium are not sisters. Reference proteomes exist (Mesotaenium, Spirogloea, Penium, Zygnema).
- "Independent loss in reds" assumes the archaeplastid ancestor had it; needs ancestral-state reconstruction; glaucophytes absent.
- "7 linajes" mixes ranks: Chlorophyta with paraphyletic "charophytes"; Bacillariophyta with Xanthophyceae (both Ochrophyta).
- §9 lists "two independent losses" as an asset while §7 calls it partial — be consistent.

11. Sec-machinery association (§2.15). [TEXT]
- Pseudoreplication reading is fair. Within-Chlorophyta OR = 1.00 arithmetically right (18·7 / 14·9) but low power; use Cochran–Mantel–Haenszel across lineages or Pagel's test. Define "Sec+" (all 4 markers? ≥3?) given PSTK under-detection.

12. Minor. [TEXT]
- The §2.4 failed prediction was on the HText crop and the CSV still uses the crop rather than the curated 421 aa protein; rerun on the curated protein [NEW-ANALYSIS, trivial].
- §9 "Opción A … ya es un paper completo" and "con 1 y 2 alcanza para enviar" overstated given 1–9.

## Correct and well done
- CSV values reported correctly: medians on the 61 (cyto 0.65, mito 0.64, plastid 0.13, ER 0.17); TargetP 48 OTHER/5 SP/4 mTP/4 cTP; SignalP 60/61 without SP; 0 TM; length median 438 (IQR 410–470); 9/67 aberrant lengths; G4/C7/H8 invariant in all 66 loops.
- Gene-model arithmetic consistent: exons 740 + 526 = 1,266 nt = 421 aa + stop; intron 107 bp; 39 recovered codons (1,180,754–1,180,870); model numbering offsets (+125 table→model, +101 model→curated: K335→K234, C461→C360).
- Proteome bookkeeping (107 + 12; 617 − 316 = 301) and within-Chlorophyta OR consistent.
- Chimeric-ORF diagnosis convincing, supported by CD-Search and NREL synteny (histidinol dehydrogenase neighbour).
- Accession/PDB choices (P0A6B7, P77444, Q96I15, 1KMK, 1P3W, 3A9Z) look right.
- Self-audits excellent and correct: docking (Se→S, apo receptor without PLP), fabricated ConSurf table (empty grades 4–8), synthetic NFS2 = 1.2×NFS1 expression data, the codeml/MCMCTree package that never ran (MAFFT citation is Katoh, not "Kurihara"), Bangiomorpha calibration critique, flexible-loop caveat on AlphaFold distances, dropping docking for Cys-vs-Sec.
