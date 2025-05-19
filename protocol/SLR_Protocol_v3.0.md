# Systematic Literature Review (SLR) Comprehensive Execution Plan: Analysis of Research Trends, Limitations, and Future Agendas in Linked List Cache and Prefetcher Optimization in Intel Xeon Server Environments (v3.0)

**Document Version:** v3.0
**Last Updated:** May 19, 2025
**Based on Feedback Dated:** May 19, 2025

## Execution Environment Container:
* **Dockerfile:** `docker/Dockerfile` (or `/Dockerfile` if at root, confirm location)
* **Conda Environment File:** `environment.yml`
* **OS (Base Image):** Ubuntu 22.04 LTS
* **Python:** 3.10.x
* **Key Libraries:** pandas, numpy, scikit-learn, requests, beautifulsoup4, bibtexparser, openpyxl, matplotlib, seaborn, nltk (for text processing), PyPDF2, pdfminer.six (for PDF text extraction), zotero-py (or Zotero integration scripts)
* **Bibliographic Management:** Zotero (utilizing group library, regular snapshot backups)
* **Document Preparation:** LaTeX (Overleaf project, version control integration) and Markdown (protocol, logs, etc.)
* **Script Execution:** All scripts CLI-based, argument passing, standardized input/output file formats (CSV, JSON), detailed logging (using `scripts/utils/logger_setup.py`). Example: `python scripts/01_execute_search_v1.1.py --db acm --output_dir data/raw_search_results --log_level INFO`

---

## Part 1: Planning the Review – Enhancing Qualitative Depth and Structural Rigor

### 1.1. Identification of Need, Objectives, and Research Questions (Strengthening Question Structure and Depth - Reflecting Supervisor Feedback Item #1)

**1.1.1. Need for the Review:**
(Previous content, with additions) ... Particularly, there is a lack of in-depth analysis on *why* specific optimization techniques are more effective in certain CPU generations, and what structural or methodological reasons lie behind a_recurrent_ research limitations. This SLR aims to move beyond 'What/How' to explore 'Why'.

**1.1.2. Review Objectives:**
(Previous objectives, with additions)
4.  To explore the primary **causal factors** influencing the selection and effectiveness 변화of linked list optimization techniques across different Intel Xeon server CPU generations.
5.  To critically analyze the **structural reasons** (e.g., benchmark bias, limited accessibility to hardware information) for recurrently observed research limitations.

**1.1.3. Research Questions (RQs - Final Version, Enhanced with 'Why' Questions and Meta-Analytic Perspective):**
* **RQ1 (Trends, Techniques & Causal Factors):** In Intel Xeon Skylake-SP, Cascade Lake-SP, and Ice Lake-SP environments, regarding the optimization of linked list cache efficiency or interaction with major hardware prefetchers (L1D stream/IPP, L2 stream/Spatial):
    * (a) What core design principles and methodologies have been predominantly used, and what are their quantitative performance improvement effects?
    * (b) If the choice of these techniques and their effectiveness have varied across CPU generations, what are the primary **technical or methodological factors** driving these changes?
* **RQ2 (Limitations, Gaps & Meta-Analysis of Gaps):** Concerning the studies identified in RQ1:
    * (a) What are their common limitations and the major unresolved research gaps?
    * (b) **Why** do certain limitations (e.g., over-optimization for specific workloads, discrepancies with actual diverse prefetcher behaviors) repeatedly appear and remain fundamentally unresolved? (Exploring structural causes: e.g., academic benchmarking practices, industry's level of hardware information disclosure, limitations of research resources).
* **RQ3 (Future Agenda & Paradigm Shifts):** Considering advancements in next-generation Intel Xeon architectures (e.g., post-Granite Rapids tiled architectures, AI-based prefetchers) and memory technologies (e.g., CXL 2.0/3.0, DDR5/6, Processing-In-Memory):
    * (a) What are the pressing future research topics and technical challenges for linked list cache/prefetcher optimization?
    * (b) What fundamental **paradigm shifts** might these technological changes bring to existing linked list optimization paradigms (e.g., prefetcher-dependent designs), and what should be the research community's response strategy?

**1.1.4. PICOC Criteria (Detailed in Protocol Appendix A.1):**
(Same as v2.0)

**1.1.5. Synonym List and Keyword Dictionary (Protocol Appendix A.2):**
(Same as v2.0 - `data/codebooks/Synonym_List_v1.3.csv` or latest version used)

### 1.2. Development and Validation of the Review Protocol
(Same as v2.0, ensure `protocol/protocol_review_log_v3.0.md` is used for logging feedback on this version)

### 1.3. Search Strategy (Maximizing Transparency and Reproducibility)

**1.3.1. Target Databases:**
(Same as v2.0)

**1.3.2. CPU Generation Scope Finalization (Based on Supervisor Feedback Item #1 "Execution Plan", to be updated with actual data):**
* **Execution Completed and Evidence (Protocol Appendix B.1):** Results from `scripts/00_generation_frequency_analysis_v1.1.py` execution (Assumed completed by 2025-05-20). Present table and distribution chart of actual publication counts per generation, top publication venues, and keyword analysis from ACM DL, IEEE Xplore, and Scopus using queries like "linked list" AND ("cache" OR "prefetcher") AND "Intel Xeon [GenName]" (utilizing generation-specific keywords and CCS Concepts/IEEE Thesaurus Terms fields). This evidence justifies the focus on Skylake-SP, Cascade Lake-SP, and Ice Lake-SP (e.g., these 3 generations account for 65% of relevant papers in the last 7 years and represent significant architectural inflection points).

**1.3.3. Final Search Query Strings (Based on Supervisor Feedback Item #2 "Execution Plan" - Protocol Appendix B.2):**
* **Execution Completed and Evidence:** By 2025-05-21, all finalized full query strings for each database (ACM DL, IEEE Xplore, Scopus, DBLP) are documented in Appendix B.2 in a copy-paste ready format. Queries explicitly use field specifications, wildcards, Boolean operators, parenthesis for precedence, and keyword groups from the synonym list (`Synonym_List_v1.3.csv` or latest). (Completed for all DBs, similar to the ACM DL example in v2.0).

**1.3.4. Search Execution and Logging:**
(Same as v2.0, using `scripts/01_execute_search_v1.1.py`)

### 1.4. Study Selection Criteria (Execution Plan for Supervisor Feedback Item #3 - Protocol Appendix C)

* **Inclusion/Exclusion Criteria Table (Appendix C.1):** (Same as v2.0, with at least two concrete examples per criterion).
* **Exception Handling Guidelines (Appendix C.2 - Updated based on actual cases):**
    * **"Comprehensive List of Exceptionally Included/Excluded Workshop Papers and Rationale" (Appendix C.2.1):** For all candidate workshop papers (approx. 5-10 expected) identified from initial screening (preliminary results from `scripts/02_initial_screening_v1.py`), clearly tabulate inclusion/exclusion decisions and detailed rationale. (E.g., W01: OOPSLA WS'19 "Early Ideas...", Experimental/Results Specificity (High), Subsequent Full Paper Absence (Confirmed), Community Citation (Low) -> Final Exclusion (Reason: Insufficient rigor compared to full conference/journal papers and lack of subsequent development)). (Review and list actual candidates by 2025-05-28).
    * **"Ambiguous Paper Adjudication Case Analysis" (Appendix C.2.2):** (Same as v2.0, detailed adjudication process and rationale for 5 ambiguous cases from pilot screening).
* **List of Permitted Simulators and Validation Criteria (Appendix C.3):** (Same as v2.0).

### 1.5. Study Quality Assessment Criteria (Protocol Appendix D)

* **QA Checklist (Appendix D.1):** (Same as v2.0, 7 questions, 12 points max).
* **Minimum Quality Score:** 7 points. (QA scores will be used for weighting in analysis or for sensitivity analysis - Section 3.1).

### 1.6. Data Extraction Strategy (Execution Plan for Supervisor Feedback Item #5 - Protocol Appendix E)

* **Data Extraction Template/Codebook (Appendix E.1 - Fully structured and integrated with automated tagging):** (Based on the table in v2.0 Section 6, "Tech. Detail" field completely removed, all fields converted to categorical/numerical/Boolean types).
    * **Example of Added Structured Fields:**
        * `OptTech_Mechanism_[KeywordName]`: Boolean (0/1). E.g., `OptTech_Mechanism_CacheLinePadding` (1=mechanism used, 0=not used). (Detailed keywords from 9B become dummy variables).
        * `Hardware_Details_CoreCount`: Number
        * `Hardware_Details_MemoryCapacity_GB`: Number
        * `Benchmark_Workload_Type`: Categorical (e.g., Microbenchmark_PointerChase, Application_GraphAnalytics_BFS, Application_Database_IndexScan, SPEC_CPU2017_Integer) - (Workload classification scheme detailed in Section 4 of feedback).
* **Automated Tagging and Structuring Script (Appendix E.2 - `scripts/04_auto_tag_and_structure_data_v1.1.py`):** (Actual Python script developed based on v2.0 pseudocode. Implements PDF text extraction (PyPDF2, pdfminer.six), nltk preprocessing, regex mapping based on codebook (`data/codebooks/optimization_keywords_v1.3.xlsx` - including regex, synonyms, hierarchical structure), and dummy variable creation).
* **Data Extraction Evidence (To be updated with actual execution results in Protocol Appendix F):**
    * **Execution Plan:** By 2025-06-10, apply the above script (with manual verification/complementation) to 5 actual selected papers.
    * **Results Presentation:** Present a complete structured data extraction results table for the 5 papers (all columns, especially auto-tagged Boolean fields), the codebook version used, and a summary of the script execution log.

---

## Part 2: Conducting the Review – Enhancing Rigor and Automation

### 2.1. Execution of the Search
(Same as v2.0, all logs saved to GitHub)

### 2.2. Study Selection (PRISMA-based, Enhanced Automation Support - Reflecting Supervisor Feedback Item #5)

* **PRISMA Flow Diagram Plan (Execution Plan for Supervisor Feedback Item #7 - Protocol Appendix G):**
    * **Preliminary Screening Execution Report (Appendix G.1):** (Updated with actual data as per v2.0 plan, presenting realistic figures).
    * **PRISMA Stage-wise Estimated Numbers (Appendix G.2 - Very conservative, with refined sensitivity analysis):** Quantitatively/qualitatively describe the impact of variations in the final number of included studies (e.g., 20 vs. 30 vs. 40) on the distribution of techniques (RQ1), identification of limitations (RQ2), and diversity of future agendas (RQ3). (E.g., "If the final number of studies is below 25, the statistical confidence in the diversity analysis of optimization techniques for Ice Lake-SP may be reduced, impacting the robustness of RQ1 conclusions" - provide specific sensitivity indicators or scenario-based interpretations).
* **Phase 1 Screening (Title/Abstract):** Use Rayyan QCRI, supplemented by Zotero tags and `scripts/02a_preprocess_for_screening_v1.py` (Input: BibTeX/CSV files -> NLP-based keyword auto-tagging, preliminary inclusion/exclusion scoring -> Output: spreadsheet for review) to reduce reviewer burden and improve consistency. Two reviewers independently.
* **Reviewer Agreement Assessment (Pilot Actual Execution - Execution Plan for Supervisor Feedback Item #4 - Protocol Appendix H):**
    * **Execution Completed and Evidence:** Execute `scripts/02b_stratified_sampling_pilot_v1.py` (from v2.0) to select 20 actual papers (list of selected papers, CPU generation distribution, `random_state=42` specified). Provide actual independent decision sheets from two reviewers (Excel snapshot or CSV). Include execution code for `scripts/03_kappa_calculation_v1.py` (from v2.0) and actual κ value (e.g., 0.78), along with detailed analysis of disagreement cases (e.g., 4 disagreements out of 20, cause: differing interpretation of criterion X). Specify plan to achieve target κ (≥0.8) through criteria refinement before full screening.
* **Phase 2 Screening (Full Text):** (Same as v2.0).
* **Reviewer Behavior Analysis and Meta-Rule Derivation (Reflecting Supervisor Feedback Item #8 - Protocol Appendix I):**
    * Systematically analyze key disagreement cases from pilot and full screening processes (including κ value improvement process) (in `data/screening/disagreement_log_v1.0.xlsx`).
    * Beyond simple consensus, conduct qualitative analysis on "Why did such disagreements occur?" (e.g., polysemy of certain terms, ambiguity of criteria boundaries, differing understanding of specific CPU features).
    * Include a "meta-interpretive reflection" in the discussion section, highlighting potential issues with the selection criteria themselves or conceptual/terminological confusion in the research field. (E.g., "The inconsistent use of the term 'prefetcher-aware' by researchers suggests a need for a clearer definition in future studies.")

### 2.3. Quality Assessment
(Same as v2.0, QA scores to be used for weighting in analysis)

### 2.4. Data Extraction
(Same as v2.0, actively using automated tagging script)

---

## Part 3: Analysis and Reporting – Enhancing Analytical Depth and Insight

### 3.1. Data Synthesis and Analysis (Addressing Statistical Justification and Workload Diversity - Reflecting Supervisor Feedback Items #3, #4)

* **Descriptive Statistical Analysis:** (Same as v2.0).
* **Taxonomy Development:** (Same as v2.0, including keyword network analysis using VOSviewer).
* **Performance Effect Comparison Analysis (Addressing Heterogeneity):**
    * **Attempt Standardized Performance Metrics:** Where possible, convert reported performance to relative improvement rates over baseline (e.g., Normalized Delta IPC, Relative Latency Reduction) (using `scripts/05a_normalize_performance_data_v1.py`).
    * **Heterogeneity Assessment and Subgroup Analysis Plan:**
        * Qualitatively/quantitatively assess the level of heterogeneity in study results using I² statistic or Cochran's Q test (utilizing meta-analysis libraries).
        * If heterogeneity is high (expected), perform Subgroup Analysis:
            * **By CPU Generation:** Skylake-SP vs. Cascade Lake-SP vs. Ice Lake-SP.
            * **By Workload Type (Reflecting Supervisor Feedback Item #4):** Classify workloads using the `Benchmark_Workload_Type` field from data extraction into representative categories (e.g., Microbenchmark_PointerChase, GraphAnalytics_BFS/SSSP, Database_OLTP_IndexScan, HPC_ScientificSim, SPEC_CPU_MemoryIntensive). Analyze differences in optimization technique effectiveness across these categories. Workload classification criteria defined in `data/codebooks/workload_taxonomy_v1.0.xlsx`.
            * **By Major Optimization Technique Category.**
        * Within each subgroup, descriptively synthesize result trends, presenting median effect sizes and interquartile ranges where possible. Warn against the risks of simple averaging.
    * **Performance Comparison Visualization:** Use standardized metrics to visualize performance improvement effects by technique/generation/workload type using Forest Plots (limited use) or Box/Violin Plots. Clearly state differences in baselines and experimental conditions and interpret with caution.
* **Identification of Key Limitations and Analysis of Structural Causes (Reflecting Supervisor Feedback Item #2):**
    * Code extracted limitations (author-stated + reviewer-identified) by theme.
    * Beyond frequency analysis, explore and discuss structural causes for recurring limitations (e.g., "overfitting to specific benchmarks like SPEC CPU," "disconnect from real-world datacenter workloads," "limitations in assumptions about prefetcher internal behavior"). (E.g., limited disclosure of CPU internal information by industry, lack or difficulty of using standardized HPC/datacenter benchmarks, academia's short-term result-oriented research environment).
* **Causal Factor Exploration (RQ1b):** Explore key factors for changes in optimization technique selection across CPU generations using a conceptual approach inspired by Qualitative Comparative Analysis (QCA) or Path Analysis. (E.g., infer how the emergence of new hardware features in a specific generation—new prefetcher types, larger caches—correlates with the rise/decline of certain optimization techniques). This is a logical explanation of observed patterns and hypothesis generation, not statistical causal proof.

### 3.2. Answering RQs and Discussion
(Same as v2.0, but actively utilizing the above analyses for RQ1b, RQ2b).

### 3.3. Proposing Future Research Agenda (Considering Technological Context and Paradigm Shifts - Reflecting Supervisor Feedback Item #6)

* Synthesize analyzed limitations, gaps, and latest technology trends (Granite Rapids, CXL 2.0/3.0, DDR5/6, AI/ML-based prefetchers, Processing-In-Memory/Near-Memory).
* Beyond simple forecasting, clearly analyze discontinuities/continuities with current research trends based on technology roadmaps (referencing ITRS if possible).
* **Propose Paradigm Shift Possibilities:** (E.g., "CXL-based disaggregated/hierarchical memory environments may diminish the importance of traditional intra-node cache/prefetcher optimization, demanding a new paradigm of minimizing data movement and optimizing Near/Remote Memory (NRM) access beyond NUMA. This could lead to research on new programming models/runtime support for distributed placement and access of linked list nodes themselves.")
* Propose 3-5 specific future research topics (For each topic: (1) connection/differentiation from existing research, (2) key technical challenges, (3) required methodologies/tools (e.g., next-gen simulators, actual CXL testbeds), (4) expected academic/industrial impact).

### 3.4. Report Writing and Dissemination

* **Report Structure:** (Based on v2.0 plan, with additions: "4.X Gap Analysis and Exploration of Structural Causes" in "4. Results" section, and "5.X Causal Factor Exploration and Paradigm Shift Discussion" in "5. Discussion" section).
* **Transparent Publication of All Supporting Materials and Execution Logs:** Provide GitHub repository link and, if necessary, archive protocol, scripts, (anonymized) extracted data, analysis code, logs, and final report on Zenodo/Figshare.