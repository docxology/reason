# R2a: reference-list verification, REVIEW.md "References", Aamodt through Hesp, plus works cited or named in the body without a list entry

Audited 2026-10-10. Source: `/Users/4d/.t3/projects/reason/REVIEW.md` (not modified). Part 1 range: Aamodt through Hesp, 27 entries, numbered below in list order. Part 2: every work, system, benchmark or tool that the body (everything before "## References") cites or names but the list does not contain.

The file was being edited by others while I worked. Line numbers ("L...") in this note refer to the version with md5 `6b0eb3911aa4872f85e902532c77d24c` (437 lines, 65,060 bytes, modified 13:08), which was the current version at the end of the audit. Section anchors are given too, since they survive edits better.

Method: arXiv IDs via `https://export.arxiv.org/api/query?id_list=<id>`; journal, chapter and proceedings metadata via the Crossref API (publisher-deposited records), cross-checked for the Part 1 DOIs against OpenAlex; proceedings via PMLR, NeurIPS, AAAI OJS, ACL Anthology, MLAnthology and ICLR/NeurIPS conference pages; books via Open Library, library-catalog records and publisher listings returned by web search; Zenodo records via the Zenodo REST API. Details of what could not be fetched are under "Caveats".

## Verdict key (same as R2b)

- **CORRECT**: every element stated in the entry matches the real publication. Suggested additions (pages of a conference paper, DOI, newer venue version) are listed as optional and do not change the verdict.
- **MINOR ERROR**: the work is unambiguously identifiable, but a stated element is slightly off or a normally required element is missing (subtitle, article number, editors).
- **MAJOR ERROR**: wrong author, year, title or venue, such that the entry misattributes or points to a different work.
- **NOT FOUND**: no such publication located.

# Part 1: Aamodt through Hesp

## Counts

| Verdict | Count |
|---|---|
| CORRECT | 24 |
| MINOR ERROR | 3 |
| MAJOR ERROR | 0 |
| NOT FOUND | 0 |
| Total | 27 |

Non-CORRECT items (one line each):

- 2 Alchourrón, Gärdenfors & Makinson (1985): MINOR ERROR, subtitle omitted (": Partial meet contraction and revision functions").
- 14 Erman et al. (1980): MINOR ERROR, subtitle omitted (": Integrating knowledge to resolve uncertainty"); venue, volume, issue and pages are right.
- 15 Falkenhainer, Forbus & Gentner (1989): MINOR ERROR, subtitle omitted (": Algorithm and examples").

Targeted checks requested in the brief:

- Golovin, Krause & Ray (2010): title exact ("Near-Optimal Bayesian Active Learning with Noisy Observations"); venue is NIPS 2010 = *Advances in Neural Information Processing Systems 23*, pp. 766–774 (NeurIPS is the later name of the same conference). CORRECT.
- Friston, Parr & Zeidman (2018): arXiv:1805.07092 resolves to "Bayesian model reduction" by exactly these three authors, v1 posted 2018-05-18. CORRECT.
- Greenblatt, Shlegeris, Sachan & Roger (2024), AI control: venue ICML 2024 (41st ICML, PMLR 235:16295–16336) is right. CORRECT.
- Erman et al. (1980): venue *ACM Computing Surveys*, 12(2), 213–253 is right; only the subtitle is missing. MINOR ERROR.
- Cox et al. (2016), MIDCA: AAAI-16 is right (Thirtieth AAAI Conference, Special Track on Cognitive Systems, pp. 3712–3718). CORRECT.
- Debenedetti et al. (2025), CaMeL: arXiv:2503.18813 is right. CORRECT, with an optional upgrade (a peer-reviewed SaTML 2026 version now exists).
- Butlin et al. (2023): arXiv:2308.08708 is right. CORRECT.
- Krakovna et al. (2019) is outside this range and was skipped as instructed.

## Table

| # | Entry (as in REVIEW.md) | Verdict | Correction / note | Verification URL |
|---|---|---|---|---|
| 1 | Aamodt & Plaza (1994), *AI Communications* 7(1), 39–59 | CORRECT | Title with subtitle, authors, volume, issue, pages confirmed (Mar 1994). | https://doi.org/10.3233/AIC-1994-7104 |
| 2 | Alchourrón, Gärdenfors & Makinson (1985), *J. Symbolic Logic* 50(2), 510–530 | MINOR ERROR | Authors, order, journal, volume, issue, pages, year confirmed (Jun 1985). Real title is "On the logic of theory change: Partial meet contraction and revision functions"; the entry stops before the colon. The list otherwise keeps subtitles (Aamodt & Plaza, Butlin), so this is inconsistent as well as incomplete. | https://doi.org/10.2307/2274239 |
| 3 | Arrow & Fisher (1974), *QJE* 88(2), 312–319 | CORRECT | Title, authors, volume, issue confirmed (May 1974). Crossref and OpenAlex give the first page only (312); the end page 319 comes from the RePEc record (`v88y1974i2p312-319`). | https://doi.org/10.2307/1883074 ; https://ideas.repec.org/a/oup/qjecon/v88y1974i2p312-319..html |
| 4 | Bratman (1987), *Intention, Plans, and Practical Reason*, Harvard University Press | CORRECT | Cambridge, MA: Harvard University Press, 1987 (viii + 200 pp.; LCCN 87008702). Reissued by CSLI Publications in 1999. | https://api.philpapers.org/rec/BRAIPA ; https://apice.unibo.it/xwiki/bin/view/Publication/Bratman87 |
| 5 | Butlin et al. (2023), arXiv:2308.08708 | CORRECT | ID resolves to "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness"; first author Patrick Butlin, 19 authors; v1 posted 2023-08-17 (v3 2023-08-22). No journal version of this report was found. (Search results mention a later, different paper by an overlapping author group, "Identifying indicators of consciousness in AI systems", in *Trends in Cognitive Sciences*; I did not verify it and it would not replace this report.) | https://arxiv.org/abs/2308.08708 |
| 6 | Conant & Ashby (1970), *Int. J. Systems Science* 1(2), 89–97 | CORRECT | Confirmed (Oct 1970); authors Roger C. Conant and W. Ross Ashby. | https://doi.org/10.1080/00207727008920220 |
| 7 | Cox et al. (2016), MIDCA, *AAAI-16* | CORRECT | Title exact. Venue: Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI-16), Special Track on Cognitive Systems, Phoenix, pp. 3712–3718 (pages optional in the list's conference style). Authors in order: Michael T. Cox, Zohreh Alavi, Dustin Dannenhauer, Vahid Eyorokon, Héctor Muñoz-Avila, Don Perlis; "Cox, M. T., et al." is right. | https://ojs.aaai.org/index.php/AAAI/article/view/9886 ; https://doi.org/10.1609/aaai.v30i1.9886 ; https://mlanthology.org/aaai/2016/cox2016aaai-midca/ |
| 8 | de Kleer (1986), *Artificial Intelligence* 28(2), 127–162 | CORRECT | Confirmed (Mar 1986). | https://doi.org/10.1016/0004-3702(86)90080-9 |
| 9 | de Kleer & Williams (1987), *Artificial Intelligence* 32(1), 97–130 | CORRECT | Confirmed (Apr 1987). | https://doi.org/10.1016/0004-3702(87)90063-4 |
| 10 | Debenedetti et al. (2025), arXiv:2503.18813 | CORRECT | ID resolves to "Defeating Prompt Injections by Design"; 10 authors, first Edoardo Debenedetti; v1 2025-03-24. "(CaMeL)" is the system's name, not part of the title (a harmless gloss). Optional upgrade: a peer-reviewed version exists in Crossref and resolves at doi.org to IEEE Xplore (document 11691650): 2026 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), Munich, pp. 587–618, doi:10.1109/SaTML68715.2026.00040. The arXiv-based entry remains a valid citation of the preprint. | https://arxiv.org/abs/2503.18813 ; https://doi.org/10.1109/SaTML68715.2026.00040 |
| 11 | Dewey (1938), *Logic: The Theory of Inquiry*, Henry Holt | CORRECT | New York: Henry Holt and Company, 1938 (viii + 546 pp.). | https://search.worldcat.org/oclc/229987 ; https://openlibrary.org/search.json?title=Logic%3A+The+Theory+of+Inquiry&author=Dewey |
| 12 | Doyle (1979), *Artificial Intelligence* 12(3), 231–272 | CORRECT | Confirmed (Nov 1979). | https://doi.org/10.1016/0004-3702(79)90008-0 |
| 13 | Endsley (1995), *Human Factors* 37(1), 32–64 | CORRECT | Confirmed (Mar 1995). | https://doi.org/10.1518/001872095779049543 |
| 14 | Erman, Hayes-Roth, Lesser & Reddy (1980), *ACM Computing Surveys* 12(2), 213–253 | MINOR ERROR | Authors (Lee D. Erman, Frederick Hayes-Roth, Victor R. Lesser, D. Raj Reddy), order, venue, volume, issue, pages, year confirmed (Jun 1980). Subtitle omitted: the title is "The Hearsay-II speech-understanding system: Integrating knowledge to resolve uncertainty". (Reprinted in *Readings in Artificial Intelligence*, 1981, pp. 349–389; the Surveys article is the right one to cite.) | https://doi.org/10.1145/356810.356816 |
| 15 | Falkenhainer, Forbus & Gentner (1989), *Artificial Intelligence* 41(1), 1–63 | MINOR ERROR | Authors, order, journal, volume, issue, pages confirmed (Nov 1989, so 1989 is right although volume 41 runs into 1990). Subtitle omitted: "The structure-mapping engine: Algorithm and examples". | https://doi.org/10.1016/0004-3702(89)90077-5 |
| 16 | Friston, Da Costa, Hafner, Hesp & Parr (2021), *Neural Computation* 33(3), 713–763 | CORRECT | Confirmed (Mar 2021); all five authors in this order. | https://doi.org/10.1162/neco_a_01351 |
| 17 | Friston, Parr & Zeidman (2018), arXiv:1805.07092 | CORRECT | ID resolves to "Bayesian model reduction" by Karl Friston, Thomas Parr, Peter Zeidman; v1 2018-05-18, v2 2019-10-14. Preprint only: Crossref finds no journal version. Easy to confuse with the 2016 *NeuroImage* paper "Bayesian model reduction and empirical Bayes for group (DCM) studies" (Friston, Litvak, Oswal, Razi, Stephan, van Wijk, Ziegler, Zeidman), which is a different work. | https://arxiv.org/abs/1805.07092 |
| 18 | Gentner (1983), *Cognitive Science* 7(2), 155–170 | CORRECT | Confirmed (Apr–Jun 1983). | https://doi.org/10.1207/s15516709cog0702_3 |
| 19 | Gershman, Blei & Niv (2010), *Psychological Review* 117(1), 197–209 | CORRECT | Confirmed (Jan 2010). | https://doi.org/10.1037/a0017808 |
| 20 | Golovin, Krause & Ray (2010), *NeurIPS* | CORRECT | Exact title "Near-Optimal Bayesian Active Learning with Noisy Observations" (the list uses sentence case). Venue: NIPS 2010 = *Advances in Neural Information Processing Systems 23*, pp. 766–774 (the conference was renamed NeurIPS in 2018, and the proceedings site now carries that name). Authors in order: Daniel Golovin, Andreas Krause, Debajyoti Ray. Preprint arXiv:1010.3091. This is the paper that introduces EC2 (Equivalence Class Determination), which is how the body uses it (L169). The page range is not in the NeurIPS BibTeX; it comes from the Google Research record and the ACM DL listing (doi:10.5555/2997189.2997275, which itself returned HTTP 403). | https://papers.nips.cc/paper_files/paper/2010/hash/1e6e0a04d20f50967c64dac2d639a577-Abstract.html ; https://research.google/pubs/near-optimal-bayesian-active-learning-with-noisy-observations/ ; https://arxiv.org/abs/1010.3091 |
| 21 | Greenblatt et al. (2024), Alignment faking, arXiv:2412.14093 | CORRECT | ID, title, year confirmed; 20 authors, first Ryan Greenblatt; posted 2024-12-18. No peer-reviewed version found. See list-level note 1: this and the next entry share the label "Greenblatt et al. (2024)". | https://arxiv.org/abs/2412.14093 |
| 22 | Greenblatt, Shlegeris, Sachan & Roger (2024), AI control, *ICML* | CORRECT | Authors and order confirmed (Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, Fabien Roger). Venue is right: ICML 2024, *Proceedings of the 41st International Conference on Machine Learning*, PMLR 235:16295–16336. Preprint arXiv:2312.06942 (its v5 comment points to the ICML version). | https://proceedings.mlr.press/v235/greenblatt24a.html ; https://arxiv.org/abs/2312.06942 |
| 23 | Greshake et al. (2023), *AISec* | CORRECT | Title exact. Venue: 16th ACM Workshop on Artificial Intelligence and Security (AISec '23), co-located with ACM CCS '23, Copenhagen, pp. 79–90. Six authors (Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz). Preprint arXiv:2302.12173. | https://doi.org/10.1145/3605764.3623985 ; https://arxiv.org/abs/2302.12173 |
| 24 | Hadfield-Menell, Dragan, Abbeel & Russell (2017), *IJCAI* | CORRECT | Title and author order confirmed. IJCAI-17 (Twenty-Sixth International Joint Conference on Artificial Intelligence, Melbourne), pp. 220–227. | https://doi.org/10.24963/ijcai.2017/32 |
| 25 | Hayes-Roth, B. (1985), *Artificial Intelligence* 26(3), 251–321 | CORRECT | Confirmed (Jul 1985). Author is Barbara Hayes-Roth (not Frederick, who is on the Erman entry). | https://doi.org/10.1016/0004-3702(85)90063-3 |
| 26 | Heins et al. (2022), *JOSS* 7(73), 4098 | CORRECT | Confirmed (May 2022); seven authors, first Conor Heins. | https://doi.org/10.21105/joss.04098 |
| 27 | Hesp et al. (2021), *Neural Computation* 33(2), 398–446 | CORRECT | Confirmed (Feb 2021); six authors, first Casper Hesp. (A 2019 PsyArXiv preprint is the earlier version.) | https://doi.org/10.1162/neco_a_01341 |

## Corrected references for the three MINOR ERROR entries (same style as the list)

- Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). On the logic of theory change: Partial meet contraction and revision functions. *Journal of Symbolic Logic*, 50(2), 510–530.
- Erman, L. D., Hayes-Roth, F., Lesser, V. R., & Reddy, D. R. (1980). The Hearsay-II speech-understanding system: Integrating knowledge to resolve uncertainty. *ACM Computing Surveys*, 12(2), 213–253.
- Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1–63.

## Optional upgrades for entries graded CORRECT (no change required)

- Debenedetti et al. (2025): "Debenedetti, E., et al. (2026). Defeating prompt injections by design. In *2026 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)* (pp. 587–618). arXiv:2503.18813." Keep the "(CaMeL)" gloss out of the title or put it after it in brackets.
- Greenblatt, Shlegeris, Sachan & Roger (2024): "... *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235, pp. 16295–16336). arXiv:2312.06942."
- Golovin, Krause & Ray (2010): "... In *Advances in Neural Information Processing Systems 23* (NIPS 2010), pp. 766–774." (Using "NIPS 2010" is more accurate for that year than "NeurIPS", but both are common.)
- Cox et al. (2016): "... In *Proceedings of the 30th AAAI Conference on Artificial Intelligence (AAAI-16)* (pp. 3712–3718)."
- Greshake et al. (2023): "... In *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec '23)* (pp. 79–90)."
- Hadfield-Menell et al. (2017): "... In *Proceedings of the 26th International Joint Conference on Artificial Intelligence (IJCAI-17)* (pp. 220–227)."
- DOIs can be added to the journal entries from the URLs in the table; none is wrong or missing in a way that affects identification.

## List-level observations (these do not change any verdict)

1. **Two entries share the label "Greenblatt et al. (2024)".** Alignment faking (20 authors) and AI control (4 authors) are different works. The body cites them as "Greenblatt et al. (2024)" (L301, alignment faking) and "Greenblatt et al. 2024, *AI Control*" (L309). The second is disambiguated only by an italic title. Suggest 2024a (alignment faking, listed first) and 2024b (AI control) in both the list and the body.
2. **Three list entries are cited in the body without a year**: Conant and Ashby (L60), Kant (L72, L92) and Stanovich (L92). All three resolve to a single list entry each, so nothing is missing, but a year would make the pointer explicit. Every other list entry in this range has an in-text author-year form that agrees with the list year (checked programmatically for all 60 list entries: no list entry is uncited, no year mismatch).
3. Body years for all 27 entries in this range agree with the list years.

# Part 2: works cited or named in the body that have no entry in the reference list

Scope rule: an item is listed if the body (before "## References") names it by author-year, by a system or benchmark name, or as a product or tool, and no list entry corresponds. Tier 1 (items 1–37) are explicit named works. Tier 2 (section B) are concept-level mentions where a reader would expect a source; they are optional. Section C lists tools, platforms and the reviewed documents themselves.

The "(cited)" tags in the body (Howard 1966, Kaelbling et al. 1998, Dehaene & Changeux 2011, CoALA, Kosmos, Darwin Gödel Machine, Cox et al.) mean "cited by Tkalic", not "cited in this review's list". Of those, only Cox et al. has a list entry here.

Reference style: all authors up to five, otherwise "First, I., et al." (the list's own practice is mixed; trim as preferred). "Where" gives the line and the section in the audited version.

## A. Tier 1: 37 items with no list entry

### A1. Author-year or author-named scholarly works

1. **Morris et al., "Levels of AGI"** (L92, §3; no year given in the text)
   - Reference: Morris, M. R., et al. (2024). Position: Levels of AGI for operationalizing progress on the path to AGI. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235, pp. 36308–36321). arXiv:2311.02462.
   - Authors: Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, Shane Legg. The arXiv v1 title was "Levels of AGI: Operationalizing Progress on the Path to AGI"; it was changed to the "for" form for ICML position-paper rules (arXiv v5 comment).
   - Verified at: https://proceedings.mlr.press/v235/morris24b.html ; https://arxiv.org/abs/2311.02462
2. **Howard 1966** (L202, §6 table, "value of information (Howard 1966, cited)")
   - Reference: Howard, R. A. (1966). Information value theory. *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26. https://doi.org/10.1109/TSSC.1966.300074
   - Verified at: Crossref record for 10.1109/tssc.1966.300074 (volume 2, issue 1, pages 22–26, 1966); doi.org resolves to IEEE Xplore document 4082064. Author is Ronald A. Howard.
3. **Kaelbling et al. 1998** (L206, §6 table, "Belief state (Kaelbling et al. 1998, cited)")
   - Reference: Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1–2), 99–134. https://doi.org/10.1016/S0004-3702(98)00023-X
   - Verified at: https://doi.org/10.1016/S0004-3702(98)00023-X (Crossref). Note for L363: the body's complaint that A.5 prints "Littman, L. M." is correct; this is Michael L. Littman.
4. **Dehaene & Changeux 2011** (L206, §6 table, "global workspace (Dehaene & Changeux 2011, cited)")
   - Reference: Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227. https://doi.org/10.1016/j.neuron.2011.03.018
   - Verified at: Crossref record for 10.1016/j.neuron.2011.03.018.
5. **Lakatos** (L324, §9, "In Lakatos's terms ... hard core ... protective belt ... positive heuristic")
   - Reference: Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press. https://doi.org/10.1017/CBO9781139171434.009
   - Verified at: Crossref record for the chapter (pages 91–196, CUP, 1970); editors from Open Library records for the volume (Lakatos and Musgrave, vol. 4 of the 1965 London colloquium proceedings).
6. **Gould** (L70, §2.3, "Gould and Conway Morris represent the poles ... most lineages show no such trend")
   - Reference: Gould, S. J. (1996). *Full House: The Spread of Excellence from Plato to Darwin*. Harmony Books.
   - The text names only "Gould". *Full House* is the book that argues there is no progress trend (the "drunkard's walk" argument), which matches the sentence "most lineages show no such trend". If the contingency pole is meant instead: Gould, S. J. (1989). *Wonderful Life: The Burgess Shale and the Nature of History*. W. W. Norton.
   - Verified at: https://www.publishersweekly.com/9780517703946 ; https://catalog.hathitrust.org/Record/003099985 (LC call number QH366.2 .G6593 1996); Open Library for *Wonderful Life*.
7. **Conway Morris** (L70, §2.3)
   - Reference: Conway Morris, S. (2003). *Life's Solution: Inevitable Humans in a Lonely Universe*. Cambridge University Press.
   - Verified at: catalog records returned by search (ISBN 0521827043): https://www.cambridgebookshop.co.uk/products/lifes-solution-inevitable-humans-in-a-lonely-universe ; https://stafforini.com/works/morris-2003-life-solution-inevitable/
8. **Leopold's land ethic** (L70, §2.3)
   - Reference: Leopold, A. (1949). *A Sand County Almanac, and Sketches Here and There*. Oxford University Press. (The essay "The Land Ethic" is in the final part.)
   - Verified at: https://en.wikipedia.org/wiki/A_Sand_County_Almanac ; Open Library record (first published 1949, Oxford University Press, New York).
9. **Vernadsky's noosphere** (L72, §2.3)
   - Reference: Vernadsky, V. I. (1945). The biosphere and the noosphere (G. Vernadsky, Trans.). *American Scientist*, 33(1), 1–12.
   - Verified at: https://monoskop.org/images/5/59/Vernadsky_WI_1945_The_Biosphere_and_the_Noosphere.pdf (scan with the journal's JSTOR header); search results give the same volume, issue and pages. The Russian original of the monograph is *Biosfera* (1926); the 1945 essay is the standard English source for the noosphere.
10. **Teilhard** (L72, §2.3)
    - Reference: Teilhard de Chardin, P. (1959). *The Phenomenon of Man* (B. Wall, Trans.). Harper & Brothers. (Original work published 1955 as *Le Phénomène humain*, Éditions du Seuil.)
    - Verified at: https://en.wikipedia.org/wiki/The_Phenomenon_of_Man ; https://search.worldcat.org/oclc/285906 ; Holy Cross Library record (New York: Harper, 1959, introduction by Julian Huxley, translation by Bernard Wall).
11. **Ashby's law of requisite variety** (L60, §2.2)
    - Reference: Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall. (The law is in chapter 11, "Requisite Variety".)
    - Verified at: http://pespmc1.vub.ac.be/ASHBBOOK.html (Principia Cybernetica full text: London, Chapman & Hall, 1956; chapter 11 is "Requisite Variety"); Open Library.
12. **Wood, Bruner & Ross** (concept only; the body uses "scaffold": L217, L234, L265, L328; the authors are named in `notes/reading-notes.md` but not in the review)
    - Reference: Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x
    - Verified at: Crossref record (Apr 1976, volume 17, issue 2, pages 89–100). Weakest item in this group: add only if the review wants to anchor "formation scaffold" in the origin of the term.

### A2. Named LLM-agent systems

13. **ReAct** (L273 §7, L338 §10)
    - Reference: Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *ICLR 2023*. arXiv:2210.03629.
    - Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao.
    - Verified at: https://arxiv.org/abs/2210.03629 (comment: "v3 is the ICLR camera ready version") ; https://mlanthology.org/iclr/2023/yao2023iclr-react/ ; https://iclr.cc/virtual/2023/poster/11003
14. **Reflexion** (L209 §6, L338 §10, L373 App. B)
    - Reference: Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. In *Advances in Neural Information Processing Systems 36* (NeurIPS 2023, pp. 8634–8652). arXiv:2303.11366.
    - Note: arXiv v4 adds Edward Berman as third author; the NeurIPS proceedings list the five authors above. Use one version consistently.
    - Verified at: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html ; https://arxiv.org/abs/2303.11366
15. **Voyager** (L209, L373)
    - Reference: Wang, G., et al. (2024). Voyager: An open-ended embodied agent with large language models. *Transactions on Machine Learning Research*. arXiv:2305.16291.
    - Authors: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar.
    - Verified at: https://jmlr.org/tmlr/papers/bib/ehfRiF0R3a.bib (TMLR record, 2024; OpenReview id ehfRiF0R3a) ; https://arxiv.org/abs/2305.16291
16. **Generative Agents** (L209, L373)
    - Reference: Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)* (pp. 1–22). https://doi.org/10.1145/3586183.3606763. arXiv:2304.03442.
    - Authors: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein.
    - Verified at: Crossref record for the DOI; https://arxiv.org/abs/2304.03442
17. **MemGPT** (L209, L373)
    - Reference: Packer, C., et al. (2023). MemGPT: Towards LLMs as operating systems. arXiv:2310.08560.
    - Authors (v2, Feb 2024): Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez (v1 had six authors, without Stoica). No peer-reviewed venue found in Crossref or search, so cite as a preprint.
    - Verified at: https://arxiv.org/abs/2310.08560
18. **ExpeL** (L209)
    - Reference: Zhao, A., et al. (2024). ExpeL: LLM agents are experiential learners. *Proceedings of the AAAI Conference on Artificial Intelligence*, 38(17), 19632–19642. https://doi.org/10.1609/aaai.v38i17.29936. arXiv:2308.10144.
    - Authors: Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang.
    - Verified at: Crossref record for the DOI (AAAI-24); https://arxiv.org/abs/2308.10144
19. **CoALA** (L209, "CoALA (cited)")
    - Reference: Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. arXiv:2309.02427.
    - Verified at: https://jmlr.org/tmlr/papers/bib/1i6ZCvflQJ.bib (TMLR record, 2024, with Survey and Featured Certification; OpenReview id 1i6ZCvflQJ) ; https://arxiv.org/abs/2309.02427 (v3 is the TMLR camera-ready)
20. **The AI Scientist** (L210, "AI Scientist and Kosmos (cited)")
    - Reference (original system paper): Lu, C., et al. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv:2408.06292. (Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha.)
    - Reference (version of record, 2026): Lu, C., et al. (2026). Towards end-to-end automation of AI research. *Nature*, 651(8107), 914–919. https://doi.org/10.1038/s41586-026-10265-5. (Preprint arXiv:2606.15497, which lists Yamada first; the Nature byline in Crossref is C. Lu, C. Lu, R. T. Lange, Y. Yamada, S. Hu, J. Foerster, D. Ha, J. Clune.)
    - The text does not say which version Tkalic cites. Cite the 2024 preprint for the system as first described, and the Nature paper if the 2026 version is meant; do not mix their author lists.
    - Verified at: https://arxiv.org/abs/2408.06292 ; Crossref record for 10.1038/s41586-026-10265-5 ; https://arxiv.org/abs/2606.15497 (abstract: "We present The AI Scientist ...", comment "Published in Nature 651, 914-919 (2026)"). The nature.com page itself required a login redirect.
21. **Kosmos** (L210 §6, L371 App. B)
    - Reference: Mitchener, L., et al. (2025). Kosmos: An AI scientist for autonomous discovery. arXiv:2511.02824.
    - 37 authors on arXiv (first Ludovico Mitchener); v1 2025-11-04, v2 2025-11-05. No journal or conference version found.
    - Verified at: https://arxiv.org/abs/2511.02824
22. **Darwin Gödel Machine** (L211 §6, L371 App. B)
    - Reference: Zhang, J., Hu, S., Lu, C., Lange, R., & Clune, J. (2025). Darwin Gödel Machine: Open-ended evolution of self-improving agents. arXiv:2505.22954. (Published at ICLR 2026.)
    - Verified at: https://arxiv.org/abs/2505.22954 (v1 2025-05-29; v3 2026-03-12; the arXiv API spells the title "Darwin Godel Machine") ; https://iclr.cc/virtual/2026/poster/10007327 (ICLR 2026 poster, same five authors in this order)

### A3. Named benchmarks

23. **BoxingGym** (L159 §5.2b, L336 §10)
    - Reference: Gandhi, K., et al. (2025). BoxingGym: Benchmarking progress in automated experimental design and model discovery. arXiv:2501.01540.
    - Authors: Kanishk Gandhi, Michael Y. Li, Lyle Goodyear, Agam Bhatia, Louise Li, Aditi Bhaskar, Mohammed Zaman, Noah D. Goodman. v1 2025-01-02, v2 2025-10-14. The only conference listing found is a NeurIPS 2025 workshop poster (Workshop on Scaling Environments for Agents), so cite the preprint.
    - Verified at: https://arxiv.org/abs/2501.01540 ; https://neurips.cc/virtual/2025/124548
24. **DiscoveryWorld** (L159, L336)
    - Reference: Jansen, P., et al. (2024). DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents. In *Advances in Neural Information Processing Systems 37* (NeurIPS 2024, Datasets and Benchmarks Track). arXiv:2406.06769.
    - Authors: Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord, Peter Clark. Spotlight poster.
    - Verified at: https://arxiv.org/abs/2406.06769 (comment: "Accepted to NeurIPS 2024 (Benchmark Track, Spotlight)") ; https://neurips.cc/virtual/2024/poster/97607
25. **ScienceWorld** (L159)
    - Reference: Wang, R., Jansen, P., Côté, M.-A., & Ammanabrolu, P. (2022). ScienceWorld: Is your agent smarter than a 5th grader? In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing* (pp. 11279–11298). https://doi.org/10.18653/v1/2022.emnlp-main.775. arXiv:2203.07540.
    - Verified at: Crossref record for the DOI (EMNLP 2022, Abu Dhabi); https://arxiv.org/abs/2203.07540
26. **ARC-AGI-3** (L159)
    - Reference: ARC Prize Foundation. (2026). ARC-AGI-3: A new challenge for frontier agentic intelligence. arXiv:2603.24621.
    - Canonical URL: https://arcprize.org/arc-agi/3 (the site footer reads "ARC Prize, Inc."; it links the technical report at https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf). arXiv v1 2026-03-24, v2 2026-04-17; group author. The site gives no citation guidance. If a conceptual anchor for the ARC family is also wanted: Chollet, F. (2019). On the measure of intelligence. arXiv:1911.01547.
    - Verified at: https://arxiv.org/abs/2603.24621 ; https://arcprize.org/arc-agi/3

### A4. Products and web resources

27. **Elicit** (L217 §6; also the unnamed "AI literature tool" at L18)
    - Canonical URL: https://elicit.com. No canonical paper exists. Elicit's own guidance (https://support.elicit.com/en/articles/549697) is to cite it like any other source, with author "Elicit", title "Elicit: The AI Research Assistant", the URL and an access date. I could not confirm the legal name of the operating company from the site.
    - Reference: Elicit. (2026). *Elicit: The AI research assistant* [Computer software]. https://elicit.com (accessed 2026-10-10).
    - Optional independent evaluation (not a description of the system): Bernard, N., et al. (2025). Using artificial intelligence for systematic review: The example of Elicit. *BMC Medical Research Methodology*, 25, Article 75. https://doi.org/10.1186/s12874-025-02528-y (Nathan Bernard, Yoshimasa Sagawa Jr, Nathalie Bier, Thomas Lihoreau, Lionel Pazart, Thomas Tannou; Crossref).
28. **OSF** (L344 §10, "Preregister on OSF")
    - Canonical URL: https://osf.io (Open Science Framework, Center for Open Science; registrations at https://osf.io/registries). Best paper for the platform: Foster, E. D., & Deardorff, A. (2017). Open Science Framework (OSF). *Journal of the Medical Library Association*, 105(2), 203–206. https://doi.org/10.5195/jmla.2017.88 (a resource review, not a system paper; PMC5370619). For the practice of preregistration itself see B6 below.
    - Verified at: https://osf.io (HTTP 200) ; Crossref record for 10.5195/jmla.2017.88 ; pages 203–206 from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5370619/

### A5. Found by sweep (not in the brief's expected list)

29. **MUSE** (L371 App. B, "2411.13537 (MUSE)")
    - Reference (preprint): Valiente, R., & Pilly, P. K. (2024). Competence-aware AI agents with metacognition for unknown situations and environments (MUSE). arXiv:2411.13537.
    - Published version: *Neural Networks*, 194, 108131 (Feb 2026), https://doi.org/10.1016/j.neunet.2025.108131, where Crossref gives the title as "Metacognition for unknown situations and environments (MUSE)". Two authors.
    - Verified at: https://arxiv.org/abs/2411.13537 ; Crossref record for the DOI.
30. **Liu & van der Schaar** (L371 App. B, "2506.05109")
    - Reference: Liu, T., & van der Schaar, M. (2025). Position: Truly self-improving agents require intrinsic metacognitive learning. In *Proceedings of the 42nd International Conference on Machine Learning* (PMLR 267, pp. 81714–81727). arXiv:2506.05109.
    - Verified at: https://proceedings.mlr.press/v267/liu25cw.html ; https://arxiv.org/abs/2506.05109
31. **MARS** (L371 App. B, "2601.11974")
    - Reference: Hou, X., et al. (2026). Learn like humans: Use meta-cognitive reflection for efficient self-improvement. In *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 28802–28824). https://doi.org/10.18653/v1/2026.acl-long.1329. arXiv:2601.11974.
    - "MARS" is the method's acronym (Metacognitive Agent Reflective Self-improvement, defined in the abstract), not the paper's title. Author order differs: arXiv v1 lists Hou, Gong, Qu, Wang, Guo, Liu; the ACL version lists Hou, Qu, Wang, Gong, Guo, Liu.
    - Verified at: https://arxiv.org/abs/2601.11974 ; https://aclanthology.org/2026.acl-long.1329/
32. **Duan et al.** (L371 App. B, "2609.11873")
    - Reference: Duan, Y., et al. (2026). The last AI built by humans: Toward genuine recursive self-improvement. arXiv:2609.11873.
    - 35 authors on arXiv, first Yi Duan; v1 2026-09-10, v3 2026-09-22; no venue found.
    - Verified at: https://arxiv.org/abs/2609.11873
33. **ACT-R** (L207 §6 table; L373 App. B)
    - Reference: Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060. https://doi.org/10.1037/0033-295X.111.4.1036 (John R. Anderson, Daniel Bothell, Michael D. Byrne, Scott Douglass, Christian Lebiere, Yulin Qin.)
    - This is the standard ACT-R citation; an alternative is Anderson, J. R. (2007), *How Can the Human Mind Occur in the Physical Universe?*, Oxford University Press.
    - Verified at: Crossref record for the DOI.
34. **LIDA** (L373 App. B)
    - Reference: Franklin, S., Madl, T., D'Mello, S., & Snaider, J. (2014). LIDA: A systems-level architecture for cognition, emotion, and learning. *IEEE Transactions on Autonomous Mental Development*, 6(1), 19–41. https://doi.org/10.1109/TAMD.2013.2277589
    - Verified at: Crossref record for the DOI.
35. **Cyc** (L125 §4.2b, "the knowledge-acquisition bottleneck that limited expert systems and Cyc")
    - Reference: Lenat, D. B. (1995). CYC: A large-scale investment in knowledge infrastructure. *Communications of the ACM*, 38(11), 33–38. https://doi.org/10.1145/219717.219745
    - Verified at: Crossref record for the DOI.
36. **Dennett** (L373 App. B; name only, no work given)
    - The review names "Dennett" in a list of precedents Vol. I does not mention, without a title. If the "Tower of Generate-and-Test" is meant (the reading notes tie Dennett to it): Dennett, D. C. (1995). *Darwin's Dangerous Idea: Evolution and the Meanings of Life*. Simon & Schuster. Otherwise name the intended work.
    - Verified at: Open Library record (first published 1995, Simon & Schuster). Count this as a "name only" gap.
37. **RAG** (L273 §7, "RAG and ReAct, in Chapter 7")
    - Reference: Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems 33* (NeurIPS 2020, pp. 9459–9474). arXiv:2005.11401. (Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela.)
    - This item was added to the body during the audit. The review does not say which RAG paper Vol. I cites; Lewis et al. is the standard one.
    - Verified at: https://arxiv.org/abs/2005.11401 (comment "Accepted at NeurIPS 2020") ; https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc26945df7481e5-Bibtex.bib

Appendix B check: the claim "All are genuine, with matching titles and authors" for the six arXiv IDs holds. I fetched each from the arXiv API: 2411.13537 is MUSE (Valiente & Pilly), 2506.05109 is Liu & van der Schaar, 2511.02824 is Kosmos, 2601.11974 is the MARS paper (Hou et al.), 2609.11873 is Duan et al., 2505.22954 is the Darwin Gödel Machine. Four of the six now have a venue version (MUSE, Liu & van der Schaar, MARS, Darwin Gödel Machine); Kosmos and Duan et al. are preprints only, as far as I could find.

## B. Tier 2: concept-level mentions (optional)

These are named concepts with no author given. Add them only if the review wants each concept anchored.

1. **Free-energy principle and active inference** (L236, L238, L242, §6.1 throughout). The list contains only specific active-inference papers. Foundational anchors: Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138. https://doi.org/10.1038/nrn2787 ; Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). Active inference: A process theory. *Neural Computation*, 29(1), 1–49. https://doi.org/10.1162/neco_a_00912 ; Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press. https://doi.org/10.7551/mitpress/12441.001.0001
2. **Epistemic value / expected free energy** (L230, L242): Friston, K., Rigoli, F., Ognibene, D., Mathys, C., FitzGerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187–214. https://doi.org/10.1080/17588928.2015.1020053
3. **Self-evidencing** (L236, "the free-energy principle's self-evidencing"): Hohwy, J. (2016). The self-evidencing brain. *Noûs*, 50(2), 259–285. https://doi.org/10.1111/nous.12062
4. **Adaptive submodularity** (L169, "near-optimal adaptive-submodular solutions"): Golovin, D., & Krause, A. (2011). Adaptive submodularity: Theory and applications in active learning and stochastic optimization. *Journal of Artificial Intelligence Research*, 42, 427–486. https://doi.org/10.1613/jair.3278 (volume, pages and title confirmed from the JAIR PDF header: "Journal of Artificial Intelligence Research 42 (2011) 427-486").
5. **Knowledge-acquisition bottleneck** (L125): Feigenbaum, E. A. (1977). The art of artificial intelligence: I. Themes and case studies of knowledge engineering. In *Proceedings of the 5th International Joint Conference on Artificial Intelligence (IJCAI-77)* (pp. 1014–1029). The bottleneck is commonly attributed to this line of work; pages from the MLAnthology record.
6. **Preregistration** (L145, L343–344 and throughout): Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114
7. **Global workspace theory** (L82, "global-workspace theory"; L206): Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press. (Dehaene & Changeux 2011, item 4 above, is already named for the same row.)
8. **Causal models "in the sense used in causal inference"** (L64): Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
9. **"One of the root-cause-analysis benchmarks for agents"** (L159): unnamed, so nothing is missing as such; name one or drop the phrase. Two candidates that exist (arXiv API; venues not checked): Pham, L., et al., RCAEval, arXiv:2412.17015; Chen, Y., et al., AIOpsLab, arXiv:2501.06706.

## C. Tools, platforms and the reviewed documents

1. **Zenodo and its REST API** (L5–6, L8, L276, L370): https://zenodo.org ; API docs https://developers.zenodo.org/ (HTTP 200). Tools are usually named in a footnote rather than listed.
2. **arXiv API** (L371): https://info.arxiv.org/help/api/index.html (HTTP 200).
3. **`pdftotext`** (L369): Poppler, https://poppler.freedesktop.org/ (HTTP 200).
4. **Python `difflib` and Python 3** (L374, L8): https://docs.python.org/3/library/difflib.html (HTTP 200).
5. **The reviewed documents are not in the list.** They appear only in the header (L5–6) with DOIs, and Volume III is named at L312 and L370 without a DOI. Verified against the Zenodo REST API on 2026-10-10:
   - Tkalic, M. (2026). *Superintelligence Technology (ASI): Foundations of Reason 8.0. From the Meaning of Life to Artificial Reason* (Vol. I, v8.0) [Report]. Zenodo. https://doi.org/10.5281/zenodo.23271702 (concept DOI 10.5281/zenodo.17957561)
   - Tkalic, M. (2026). *Engineering of Reason 3.5: ASI Technology* (Vol. II, v3.5) [Report]. Zenodo. https://doi.org/10.5281/zenodo.23271781 (concept DOI 10.5281/zenodo.22975036)
   - Tkalic, M. (2026). *Foundations of Reason Volume III: Civilization of Reason v1.8. An Architecture for Humans and Artificial Reason* [Report]. Zenodo. https://doi.org/10.5281/zenodo.22975357 (published 2026-09-26; concept DOI 10.5281/zenodo.22975356)

## D. Paste-ready block: Tier 1 references in list style, alphabetical

(Product and web items follow the list's plain style. Wood/Bruner/Ross and Dennett, items 12 and 36 above, are the weakest and may be dropped.)

- Anderson, J. R., et al. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060.
- ARC Prize Foundation. (2026). ARC-AGI-3: A new challenge for frontier agentic intelligence. arXiv:2603.24621. https://arcprize.org/arc-agi/3
- Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.
- Conway Morris, S. (2003). *Life's Solution: Inevitable Humans in a Lonely Universe*. Cambridge University Press.
- Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.
- Dennett, D. C. (1995). *Darwin's Dangerous Idea: Evolution and the Meanings of Life*. Simon & Schuster. [only if a specific work is intended]
- Duan, Y., et al. (2026). The last AI built by humans: Toward genuine recursive self-improvement. arXiv:2609.11873.
- Elicit. (2026). *Elicit: The AI research assistant* [Computer software]. https://elicit.com
- Foster, E. D., & Deardorff, A. (2017). Open Science Framework (OSF). *Journal of the Medical Library Association*, 105(2), 203–206. (Platform: https://osf.io)
- Franklin, S., Madl, T., D'Mello, S., & Snaider, J. (2014). LIDA: A systems-level architecture for cognition, emotion, and learning. *IEEE Transactions on Autonomous Mental Development*, 6(1), 19–41.
- Gandhi, K., et al. (2025). BoxingGym: Benchmarking progress in automated experimental design and model discovery. arXiv:2501.01540.
- Gould, S. J. (1996). *Full House: The Spread of Excellence from Plato to Darwin*. Harmony Books.
- Hou, X., et al. (2026). Learn like humans: Use meta-cognitive reflection for efficient self-improvement. *ACL 2026* (Long Papers), 28802–28824. arXiv:2601.11974.
- Howard, R. A. (1966). Information value theory. *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26.
- Jansen, P., et al. (2024). DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents. *NeurIPS 2024* (Datasets and Benchmarks Track). arXiv:2406.06769.
- Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1–2), 99–134.
- Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press.
- Lenat, D. B. (1995). CYC: A large-scale investment in knowledge infrastructure. *Communications of the ACM*, 38(11), 33–38.
- Leopold, A. (1949). *A Sand County Almanac, and Sketches Here and There*. Oxford University Press.
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 2020*, 9459–9474. arXiv:2005.11401.
- Liu, T., & van der Schaar, M. (2025). Position: Truly self-improving agents require intrinsic metacognitive learning. *ICML 2025* (PMLR 267), 81714–81727. arXiv:2506.05109.
- Lu, C., et al. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv:2408.06292. [or Lu, C., et al. (2026). Towards end-to-end automation of AI research. *Nature*, 651(8107), 914–919.]
- Mitchener, L., et al. (2025). Kosmos: An AI scientist for autonomous discovery. arXiv:2511.02824.
- Morris, M. R., et al. (2024). Position: Levels of AGI for operationalizing progress on the path to AGI. *ICML 2024* (PMLR 235), 36308–36321. arXiv:2311.02462.
- Packer, C., et al. (2023). MemGPT: Towards LLMs as operating systems. arXiv:2310.08560.
- Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *UIST '23*, 1–22. arXiv:2304.03442.
- Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*, 8634–8652. arXiv:2303.11366.
- Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. arXiv:2309.02427.
- Teilhard de Chardin, P. (1959). *The Phenomenon of Man* (B. Wall, Trans.). Harper & Brothers.
- Valiente, R., & Pilly, P. K. (2024). Competence-aware AI agents with metacognition for unknown situations and environments (MUSE). arXiv:2411.13537.
- Vernadsky, V. I. (1945). The biosphere and the noosphere. *American Scientist*, 33(1), 1–12.
- Wang, G., et al. (2024). Voyager: An open-ended embodied agent with large language models. *Transactions on Machine Learning Research*. arXiv:2305.16291.
- Wang, R., Jansen, P., Côté, M.-A., & Ammanabrolu, P. (2022). ScienceWorld: Is your agent smarter than a 5th grader? *EMNLP 2022*, 11279–11298.
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100.
- Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *ICLR 2023*. arXiv:2210.03629.
- Zhang, J., Hu, S., Lu, C., Lange, R., & Clune, J. (2025). Darwin Gödel Machine: Open-ended evolution of self-improving agents. arXiv:2505.22954.
- Zhao, A., et al. (2024). ExpeL: LLM agents are experiential learners. *AAAI 2024*, 38(17), 19632–19642. arXiv:2308.10144.

## Incidental observations for the lead

- **L92 vs L363.** L92 says of Russell & Wefald and Morris et al.: "The latter is cited; the others should be." L363 says Russell & Wefald (1991) appears twice in A.5, so it is already cited by Tkalic. "The others" cannot include it. Consider "The latter is cited; the others should be" restricted to Kant, Stanovich and Hintikka, or reword.
- **Counts.** Tier 1 has 37 items: the 28 expected examples in the brief (Morris, Howard, Kaelbling et al., Dehaene & Changeux, Lakatos, Gould, Conway Morris, Leopold, Vernadsky, Teilhard, ReAct, Reflexion, Voyager, Generative Agents, MemGPT, ExpeL, CoALA, AI Scientist, Kosmos, Darwin Gödel Machine, BoxingGym, DiscoveryWorld, ScienceWorld, ARC-AGI-3, Elicit, OSF, Ashby, Wood/Bruner/Ross) plus 9 found by sweep (MUSE, Liu & van der Schaar, MARS, Duan et al., ACT-R, LIDA, Cyc, Dennett, RAG). Two of the 37 are weak: Dennett (name only) and Wood/Bruner/Ross (concept only).
- **Version drift.** Several arXiv-only entries and named systems now have venue versions that postdate the arXiv year: CaMeL (SaTML 2026), Darwin Gödel Machine (ICLR 2026), MARS (ACL 2026), MUSE (Neural Networks 2026), AI Scientist (Nature 2026), Liu & van der Schaar (ICML 2025). Whether to cite preprint or venue version is a style choice, but be consistent within the list.

## Caveats

- DBLP sits behind a bot wall (Anubis), the OpenReview API demands a challenge, the ACM Digital Library returned HTTP 403, the Nature article page redirects to a login, and Semantic Scholar rate-limited. None of these was used as a source; Crossref, the arXiv API and proceedings or conference pages carried the checks instead.
- Page numbers for Golovin et al. (766–774) rest on the Google Research record and the ACM DL listing text returned by search, because the NeurIPS BibTeX omits pages. Page 319 for Arrow & Fisher rests on the RePEc record.
- Books (Bratman, Dewey, Gould, Conway Morris, Leopold, Teilhard, Ashby, Dennett, Baars, Pearl) were checked against Open Library, WorldCat and library-catalog records returned by search, not against copies of the books.
- Venue versions dated 2026 (SaTML, ICLR, ACL, Nature, Neural Networks) postdate my training data; they rest on the cited Crossref records and conference or proceedings pages only. The SaTML DOI resolves at doi.org to IEEE Xplore, but the IEEE page itself answered with a bot challenge (HTTP 202).
- The "Lakatos & Musgrave (Eds.)" editors come from Open Library records for the volume; Crossref's chapter record does not list editors.
- Tier 2 items 5, 7, 8 and 9 were checked less deeply than Tier 1 (catalog or MLAnthology records only; RCA benchmark venues unchecked).
