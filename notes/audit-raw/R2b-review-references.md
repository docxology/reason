# R2b: reference-list verification, REVIEW.md "References", Hintikka through Turner

Audited 2026-10-10. Source: `/Users/4d/.t3/projects/reason/REVIEW.md`, section "References" (not modified). Range: Hintikka through Turner, 33 entries, numbered below in list order.

Method: arXiv IDs via `https://export.arxiv.org/api/query?id_list=<id>` (1806.01186, 2501.16946, 2411.00986, plus 1902.09725 and 1402.5886 as cross-checks); journal and chapter metadata via the Crossref API (DOI records); proceedings via PMLR, AAAI, CEUR-WS and publisher pages; books via Library of Congress records (LCCN), Crossref book DOIs and OUP/MIT listings; PsyArXiv record via the OSF API. Where a site blocks automated fetches (OpenReview, Springer link pages, MIT Press) I used a secondary source and say so.

## Verdict key

- **CORRECT**: every element stated in the entry matches the real publication. Suggested additions (pages of a conference paper, DOI, version) are listed as optional and do not change the verdict.
- **MINOR ERROR**: the work is unambiguously identifiable, but a stated element is slightly off or a normally required element is missing (subtitle, article number, chapter editors).
- **MAJOR ERROR**: wrong author, year, title or venue such that the entry misattributes or points to a different work.
- **NOT FOUND**: no such publication located.

## Counts

| Verdict | Count |
|---|---|
| CORRECT | 29 |
| MINOR ERROR | 4 |
| MAJOR ERROR | 0 |
| NOT FOUND | 0 |
| Total | 33 |

Non-CORRECT items (one line each):

- 6 Keeney & Raiffa (1976): MINOR ERROR, subtitle omitted ("Preferences and Value Tradeoffs").
- 19 Metzinger (2003): MINOR ERROR, subtitle omitted ("The Self-Model Theory of Subjectivity").
- 27 Sandved-Smith et al. (2021): MINOR ERROR, article number omitted (niab018).
- 28 Schmidhuber (2007): MINOR ERROR, book editors (B. Goertzel & C. Pennachin) and pages (199–226) omitted.

## Table

| # | Entry (as in REVIEW.md) | Verdict | Correction / note | Verification URL |
|---|---|---|---|---|
| 1 | Hintikka (1999), *Inquiry as Inquiry: A Logic of Scientific Discovery*, Kluwer | CORRECT | Title, year, publisher confirmed (Kluwer Academic Publishers, Dordrecht/Boston; Jaakko Hintikka Selected Papers vol. 5). | https://www.loc.gov/item/98047228/ ; https://doi.org/10.1007/978-94-015-9313-7 |
| 2 | Hyafil & Rivest (1976), IPL 5(1), 15–17 | CORRECT | Exact title "Constructing optimal binary decision trees is NP-complete"; Information Processing Letters 5(1), May 1976, pp. 15–17; authors Laurent Hyafil, Ronald L. Rivest. | https://doi.org/10.1016/0020-0190(76)90095-8 |
| 3 | Javdani et al. (2014), AISTATS | CORRECT | Venue is AISTATS 2014 (Reykjavik), PMLR 33:430–438; title exact. Full author list: Javdani, S., Chen, Y., Karbasi, A., Krause, A., Bagnell, J. A. (PMLR prints "Drew Bagnell"), & Srinivasa, S. S. "et al." is acceptable. Extended version: arXiv:1402.5886. | https://proceedings.mlr.press/v33/javdani14.html ; https://arxiv.org/abs/1402.5886 |
| 4 | Johnson & Raye (1981), Psych Rev 88(1), 67–85 | CORRECT | All elements confirmed. | https://doi.org/10.1037/0033-295X.88.1.67 |
| 5 | Kant (1781/1787), CPR, Transcendental Dialectic, Appendix | CORRECT | A (1781) and B (1787) editions. The Appendix to the Transcendental Dialectic opens with "On the regulative use of the ideas of pure reason" (Kemp Smith: "The regulative employment of the ideas of pure reason"), followed by "The final purpose of the natural dialectic of human reason". Optional: name a translation and add A/B pagination (the Appendix begins at A642/B670, per secondary literature). | https://humanum.arts.cuhk.edu.hk/humftp/E-text/Kant/cpr.kemp-smith/19dia-ap.htm |
| 6 | Keeney & Raiffa (1976), *Decisions with Multiple Objectives*, Wiley | MINOR ERROR | Subtitle omitted. Fix: Keeney, R. L., & Raiffa, H. (1976). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley. (New York: Wiley, c1976; reprinted by Cambridge University Press, 1993.) | https://www.loc.gov/item/76007895/ |
| 7 | King et al. (2004), Nature 427, 247–252 | CORRECT | Pages confirmed: Nature 427(6971), 247–252 (Jan 2004). First author Ross D. King (8 authors). Title exact. | https://doi.org/10.1038/nature02236 |
| 8 | King et al. (2009), Science 324(5923), 85–89 | CORRECT | Pages confirmed: Science 324(5923), 85–89 (3 Apr 2009). First author Ross D. King (13 authors). Title "The automation of science" exact. | https://doi.org/10.1126/science.1165620 |
| 9 | Klyubin, Polani & Nehaniv (2005), IEEE CEC | CORRECT | 2005 IEEE Congress on Evolutionary Computation (Edinburgh), vol. 1, pp. 128–135; title exact. Pages are optional in the list's conference style. | https://doi.org/10.1109/CEC.2005.1554676 |
| 10 | Kolodner (1993), *Case-Based Reasoning*, Morgan Kaufmann | CORRECT | San Mateo, CA: Morgan Kaufmann Publishers, c1993. | https://www.loc.gov/item/93035703/ |
| 11 | Krakovna et al. (2019), arXiv:1806.01186 | CORRECT | First author, ID and title confirmed. **First-version year is 2018** (v1 posted 4 Jun 2018, then titled "Measuring and avoiding side effects using relative reachability", four authors, "Preprint. Work in progress"). The cited title exists from **v2 (8 Mar 2019)**, which adds R. Kumar, so 2019 is right for the cited title (arXiv's own BibTeX export also uses the latest-revision year). **Published venue:** short version in the IJCAI-19 Workshop on Artificial Intelligence Safety (AISafety 2019, Macao, 11–12 Aug 2019), CEUR-WS Vol-2419, paper 1, four authors (Krakovna, Orseau, Martic, Legg; no Kumar). No journal or archival-conference version found; the authors' own later paper cites it as "arXiv preprint arXiv:1806.01186, 2019" (arXiv:2010.07877). Observation: it is the only arXiv entry in the list whose year differs from its ID's year; optional fix is to pin "v2" or cite the workshop version. | https://arxiv.org/abs/1806.01186 ; https://export.arxiv.org/api/query?id_list=1806.01186 ; https://ceur-ws.org/Vol-2419/ ; https://ceur-ws.org/Vol-2419/paper_1.pdf |
| 12 | Kulveit et al. (2025), arXiv:2501.16946 | CORRECT | ID, title ("Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development") and year confirmed; v1 28 Jan 2025, v2 29 Jan 2025; authors Kulveit, Douglas, Ammann, Turan, Krueger, Duvenaud. Note: a peer-reviewed ICML 2025 position-paper version exists under a different title ("Position: Humanity Faces Existential Risk from Gradual Disempowerment", PMLR 267:81678–81688). The entry is correct as a preprint citation. | https://arxiv.org/abs/2501.16946 ; https://export.arxiv.org/api/query?id_list=2501.16946 ; https://proceedings.mlr.press/v267/kulveit25a.html |
| 13 | Laird, Newell & Rosenbloom (1987), AI 33(1), 1–64 | CORRECT | All elements confirmed (Sep 1987). | https://doi.org/10.1016/0004-3702(87)90050-6 |
| 14 | Langley, Simon, Bradshaw & Zytkow (1987), *Scientific Discovery: Computational Explorations of the Creative Processes*, MIT Press | CORRECT | Library of Congress record (LCCN 86010258) gives "Creative Processes" (plural) as printed, MIT Press, c1987. MIT Press's web listing and its e-book DOI use singular "Creative Process"; the entry's plural is the printed title. | https://www.loc.gov/item/86010258/ ; https://doi.org/10.7551/mitpress/6090.001.0001 |
| 15 | Lau (2019), "Consciousness, metacognition, and perceptual reality monitoring", PsyArXiv | CORRECT | It is a single-author PsyArXiv preprint (v1, posted 10 Jun 2019, DOI 10.31234/osf.io/ckbyf). The OSF record carries no published-article DOI or publication citation, and the UCLA BRI faculty page still lists it as a 2019 PsyArXiv preprint; no journal version found. The 2022 OUP book "In Consciousness We Trust" is a separate work. Title on OSF uses "&" ("Consciousness, Metacognition, & Perceptual Reality Monitoring"); "and" is a harmless normalization. Optional: add the DOI. | https://doi.org/10.31234/osf.io/ckbyf ; https://api.osf.io/v2/preprints/ckbyf_v1/ |
| 16 | LeCun (2022), "A path towards autonomous machine intelligence", OpenReview | CORRECT | Venue "OpenReview" is accurate: a self-posted position paper hosted on OpenReview (forum id BZ5a1r-kVsf); no conference or journal version found. **Version is 0.9.2, dated 27 Jun 2022** (the version line on p. 1). OpenReview blocks automated fetches, so the version was corroborated from two secondary pages. Optional: add "(Version 0.9.2)" and the URL. | https://openreview.net/forum?id=BZ5a1r-kVsf ; https://mafr.fr/en/article/a-path-towards-autonomous-machine-intelligence/ |
| 17 | Long, Sebo et al. (2024), arXiv:2411.00986 | CORRECT | ID, title ("Taking AI Welfare Seriously"), year confirmed. Author list in order: Robert Long, Jeff Sebo, Patrick Butlin, Kathleen Finlinson, Kyle Fish, Jacqueline Harding, Jacob Pfau, Toni Sims, Jonathan Birch, David Chalmers; so "Long, R., Sebo, J., et al." is right. v1 only (4 Nov 2024); no journal version found. | https://arxiv.org/abs/2411.00986 ; https://export.arxiv.org/api/query?id_list=2411.00986 |
| 18 | MacAskill, Bykvist & Ord (2020), *Moral Uncertainty*, OUP | CORRECT | Oxford University Press, published 10 Sep 2020; authors and order confirmed. | https://doi.org/10.1093/oso/9780198722274.001.0001 |
| 19 | Metzinger (2003), *Being No One*, MIT Press | MINOR ERROR | Subtitle omitted. Fix: Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press. (Hardcover Jan 2003; paperback 2004.) | https://doi.org/10.7551/mitpress/1551.001.0001 |
| 20 | Molineaux, Klenk & Aha (2010), AAAI | CORRECT | Main conference, not a workshop: *Proc. AAAI Conf. Artif. Intell.* 24(1), AAAI-10 (Twenty-Fourth AAAI Conference on Artificial Intelligence), Integrated Intelligence Special Track, pp. 1548–1554, 5 Jul 2010. Title and author order confirmed. | https://ojs.aaai.org/index.php/AAAI/article/view/7576 ; https://doi.org/10.1609/aaai.v24i1.7576 |
| 21 | Muñoz-Avila, Jaidee, Aha & Carter (2010), ICCBR | CORRECT | ICCBR 2010 (18th International Conference on Case-Based Reasoning, Alessandria, 19–22 Jul 2010), LNCS 6176, Springer, pp. 228–241; proceedings editors Bichindaritz & Montani. Authors: Héctor Muñoz-Avila, Ulit Jaidee, David W. Aha, Elizabeth Carter. | https://doi.org/10.1007/978-3-642-14274-1_18 |
| 22 | Omohundro (2008), AGI-08 | CORRECT | "AGI-08" = *Artificial General Intelligence 2008: Proceedings of the First AGI Conference* (Memphis, Mar 2008), eds. P. Wang, B. Goertzel, S. Franklin; Frontiers in AI and Applications vol. 171, IOS Press, **pp. 483–492**. (The 2018 CRC Press reprint, pp. 47–55, is a different publication.) Pages are optional in the list's conference style. | https://stafforini.com/works/omohundro-2008-basic-aidrives/ |
| 23 | Peirce (1877), *Popular Science Monthly* 12, 1–15 | CORRECT | Vol. 12, Nov 1877, pp. 1–15 (first paper of "Illustrations of the Logic of Science"). | https://cspeirce.omeka.net/items/show/2 |
| 24 | Rao & Georgeff (1995), ICMAS | CORRECT | Venue is the First International Conference on Multiagent Systems (ICMAS-95, San Francisco, Jun 1995), pp. 312–319. The AAAI copy's page marker reads "312 ICMAS-95" and the paper is 8 pages. | https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf ; https://apice.unibo.it/xwiki/bin/view/Publication/BdiIcmas95 |
| 25 | Reiter (1987), AI 32(1), 57–95 | CORRECT | All elements confirmed (Apr 1987). | https://doi.org/10.1016/0004-3702(87)90062-2 |
| 26 | Russell & Wefald (1991), AI 49, 361–395 | CORRECT | Journal, volume and pages confirmed: *Artificial Intelligence* 49(1–3), 361–395 (May 1991). Issue omitted (optional). | https://doi.org/10.1016/0004-3702(91)90015-C |
| 27 | Sandved-Smith et al. (2021), *Neuroscience of Consciousness* 2021(1) | MINOR ERROR | Journal, volume 2021, issue 1 and title confirmed; **article number missing**. Fix: Sandved-Smith, L., et al. (2021). Towards a computational phenomenology of mental action: Modelling meta-awareness and attentional control with deep parametric active inference. *Neuroscience of Consciousness*, 2021(1), niab018. (Full author list: Sandved-Smith, Hesp, Mattout, Friston, Lutz, Ramstead.) | https://doi.org/10.1093/nc/niab018 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC8396119 |
| 28 | Schmidhuber (2007), In *Artificial General Intelligence*, Springer | MINOR ERROR | Book and publisher are right (Springer, Cognitive Technologies series, 2007); **editors and pages missing**. Fix: Schmidhuber, J. (2007). Gödel machines: Fully self-referential optimal universal self-improvers. In B. Goertzel & C. Pennachin (Eds.), *Artificial General Intelligence* (pp. 199–226). Springer. | https://doi.org/10.1007/978-3-540-68677-4_7 ; https://doi.org/10.1007/978-3-540-68677-4 |
| 29 | Seth (2013), TiCS 17(11), 565–573 | CORRECT | All elements confirmed (Nov 2013). | https://doi.org/10.1016/j.tics.2013.09.007 |
| 30 | Smith, Schwartenbeck, Parr & Friston (2020), *Front Comput Neurosci* 14, 41 | CORRECT | Volume 14, article number 41 (19 May 2020); title and authors confirmed. | https://doi.org/10.3389/fncom.2020.00041 |
| 31 | Soares, Fallenstein, Yudkowsky & Armstrong (2015), AAAI Workshop on AI and Ethics | CORRECT | Venue confirmed: AAAI-15 Workshop on AI and Ethics, published in *Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence*, Austin, TX, 25–26 Jan 2015. Author order matches the paper's byline (Soares, Fallenstein, Yudkowsky, Armstrong); FHI's web listing reorders Armstrong before Yudkowsky, which should not be copied. | https://intelligence.org/wp-content/uploads/2024/10/Corrigibility.pdf ; https://aaai.org/ocs/index.php/WS/AAAIW15/paper/view/10124 |
| 32 | Stanovich (2009), *What Intelligence Tests Miss*, Yale University Press | CORRECT | Publisher confirmed: New Haven: Yale University Press, c2009; full title with subtitle matches. | https://www.loc.gov/item/2008037325/ |
| 33 | Turner, Hadfield-Menell & Tadepalli (2020), AIES | CORRECT | AIES '20 (AAAI/ACM Conference on AI, Ethics, and Society, New York, Feb 2020), pp. 385–391; authors Alexander Matt Turner, Dylan Hadfield-Menell, Prasad Tadepalli; title exact. arXiv:1902.09725 carries the comment "Published in AI, Ethics, and Society 2020". | https://doi.org/10.1145/3375627.3375851 ; https://arxiv.org/abs/1902.09725 |

## Corrected references for the four MINOR ERROR entries (same style as the list)

- Keeney, R. L., & Raiffa, H. (1976). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley.
- Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.
- Sandved-Smith, L., et al. (2021). Towards a computational phenomenology of mental action: Modelling meta-awareness and attentional control with deep parametric active inference. *Neuroscience of Consciousness*, 2021(1), niab018.
- Schmidhuber, J. (2007). Gödel machines: Fully self-referential optimal universal self-improvers. In B. Goertzel & C. Pennachin (Eds.), *Artificial General Intelligence* (pp. 199–226). Springer.

## Optional upgrades for entries graded CORRECT (no change required)

- Krakovna et al. (2019): "Krakovna, V., Orseau, L., Kumar, R., Martic, M., & Legg, S. (2019). Penalizing side effects using stepwise relative reachability. arXiv:1806.01186 (v2)." Or cite the workshop version: "Krakovna, V., Orseau, L., Martic, M., & Legg, S. (2019). Penalizing side effects using stepwise relative reachability. In *Proceedings of the IJCAI-19 Workshop on Artificial Intelligence Safety (AISafety 2019)*, CEUR Workshop Proceedings 2419."
- Kulveit et al. (2025): keep the preprint if the arXiv framing is intended; the peer-reviewed version is Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D., & Duvenaud, D. (2025). Position: Humanity faces existential risk from gradual disempowerment. In *Proceedings of the 42nd International Conference on Machine Learning* (PMLR 267, pp. 81678–81688).
- LeCun (2022): "LeCun, Y. (2022). A path towards autonomous machine intelligence (Version 0.9.2). OpenReview. https://openreview.net/forum?id=BZ5a1r-kVsf"
- Lau (2019): add "https://doi.org/10.31234/osf.io/ckbyf".
- Omohundro (2008): "In P. Wang, B. Goertzel, & S. Franklin (Eds.), *Artificial General Intelligence 2008: Proceedings of the First AGI Conference* (pp. 483–492). IOS Press."
- Rao & Georgeff (1995): "In *Proceedings of the First International Conference on Multiagent Systems (ICMAS-95)* (pp. 312–319)."
- Javdani et al. (2014): "Javdani, S., Chen, Y., Karbasi, A., Krause, A., Bagnell, J. A., & Srinivasa, S. S. (2014). ... *AISTATS*" if full author lists are preferred.

## Caveats

- OpenReview, Springer link pages and MIT Press pages blocked automated fetches; the LeCun version line was corroborated from two secondary pages, and the Schmidhuber chapter editors from the Crossref record of the parent book.
- The "A642/B670" start of Kant's Appendix is taken from secondary literature, not checked against a printed A/B edition.
- No in-text mismatch found: the author-year forms used in the body of REVIEW.md for these 33 works agree with the list years.
