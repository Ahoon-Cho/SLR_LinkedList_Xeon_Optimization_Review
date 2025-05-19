# Systematic Literature Review (SLR) Execution Plan: Analysis of Research Trends in Linked List Cache and Prefetcher Optimization in Intel Xeon Server Environments (v2.0)

**Document Version:** v2.0
**Last Updated:** May 19, 2025

## Execution Environment Container:
* **Dockerfile:** `docker/Dockerfile` (or `/Dockerfile` if at root)
* **Conda Environment File:** `environment.yml`
* **OS (Base Image):** Ubuntu 22.04 LTS
* **Python:** 3.10.x
* **Key Libraries:** pandas, numpy, scikit-learn, requests, beautifulsoup4, bibtexparser, openpyxl, matplotlib, seaborn, nltk (for text processing), zotero-py (or Zotero integration scripts)
* **Bibliographic Management:** Zotero (utilizing group library, regular snapshot backups)
* **Document Preparation:** LaTeX (Overleaf project, version control integration) and Markdown (protocol, logs, etc.)
* **Script Execution:** All scripts CLI-based, argument passing, standardized input/output file formats (CSV, JSON), detailed logging (using `scripts/utils/logger_setup.py`). Example: `python scripts/01_execute_search.py --db acm --output_dir data/raw_search_results --log_level INFO`

---

## Part 1: Planning the Review
*(Reference: Carrera-Rivera et al. (2022), Section 2 "Planning")*

### 1.1. Identification of Need, Objectives, and Research Questions

**1.1.1. Need for the Review:**
Intel Xeon server architectures are continuously evolving, leading to increasingly complex cache and prefetcher structures. There is a growing need to systematically synthesize research trends in optimizing fundamental data structures like linked lists in response to these hardware changes and to propose future research directions. Existing reviews often focus on specific generations or techniques, or may lack methodological rigor.

**1.1.2. Review Objectives:**
1.  To identify and classify key trends (design principles, methodologies, results) in linked list cache/prefetcher optimization research targeting three major Intel Xeon generations (Skylake-SP, Cascade Lake-SP, Ice Lake-SP) over the last decade (2015-2025).
2.  To identify common limitations and unresolved research gaps in these studies.
3.  To propose a concrete future research agenda considering recent CPU architectural advancements (e.g., next-generation prefetchers, CXL).

**1.1.3. Research Questions (RQs - Final Version):**
* **RQ1 (Trends & Techniques):** What core design principles (e.g., layout, allocation, prefetching control) and methodologies (experimental environments, simulator types/versions, workloads) have been predominantly used to optimize linked list cache efficiency or interactions with major hardware prefetchers (L1D stream/IPP, L2 stream/Spatial) in Intel Xeon Skylake-SP, Cascade Lake-SP, and Ice Lake-SP environments, and what are their quantitative performance improvement effects?
* **RQ2 (Limitations & Gaps):** What are the common limitations (e.g., dependency on specific workloads, simplification of prefetcher models, insufficient consideration of NUMA environments) of the studies identified in RQ1, and what are the major unresolved research gaps?
* **RQ3 (Future Agenda):** Considering advancements in next-generation Intel Xeon architectures (e.g., post-Granite Rapids) and memory technologies (e.g., CXL 2.0/3.0, DDR5/6), what are the pressing future research topics and technical challenges that need to be addressed for linked list cache/prefetcher optimization?

**1.1.4. PICOC Criteria (Detailed in Protocol Appendix A.1):**
* **Population:** Systems based on Intel Xeon Skylake-SP, Cascade Lake-SP, or Ice Lake-SP server CPUs.
* **Intervention:** Software or hardware-software co-design/optimization techniques to improve linked list (SLL, DLL, CLL, Unrolled List, Skip List, etc.) cache access patterns, prefetcher interactions, or NUMA locality.
* **Comparison:** Performance comparison against standard/default linked list implementations, optimization techniques from previous generations, or other optimization techniques within the same generation.
* **Outcome:** Quantitative performance changes such as cache miss rate, latency, throughput, IPC, prefetcher efficiency metrics. Qualitatively, design principles, methodologies, and architecture-specific considerations.
* **Context:** High-performance computing environments where linked list performance impacts overall system performance, such as datacenter workloads, HPC applications, in-memory databases, and operating system kernels.

**1.1.5. Synonym List and Keyword Dictionary (Protocol Appendix A.2):**
* Managed in `data/codebooks/Synonym_List_v1.2.csv` (version controlled), including diverse search terms for CPU generation names, prefetcher types, optimization techniques, etc.

### 1.2. Development and Validation of the Review Protocol

* **This Document (SLR Execution Plan v2.0):** Specifies all procedures, criteria, tools, and deliverables. Version controlled in the GitHub repository.
* **Peer Review of Protocol:**
    * **Internal Review:** Request protocol review from two peer researchers within the research team (by 2025-05-20).
    * **External Consultation (Optional):** Consider seeking advice from an expert in the field (other than the supervisor).
* **Review Feedback and Revision Log:** All feedback and corresponding protocol modifications will be detailed in `protocol/protocol_review_log_v2.0.md`.

### 1.3. Search Strategy (Maximizing Transparency and Reproducibility)

**1.3.1. Target Databases:**
* ACM Digital Library, IEEE Xplore, Scopus, DBLP.
* Google Scholar will be used補助arily and for snowballing.

**1.3.2. CPU Generation Scope Finalization (Execution Plan for Supervisor Feedback Item #1):**
* **Execution Plan:** Run `scripts/00_generation_frequency_analysis_v1.py` (Python + requests/BeautifulSoup/DB API wrapper) on 2025-05-20.
* **Targets:** ACM DL, IEEE Xplore. (Manual sampling for Scopus if API access is limited).
* **Collected Fields:** Publication count, publication year, conference/journal name, author keywords, CCS Concepts/IEEE Thesaurus Terms (if provided by DB).
* **Script Core Logic (Pseudocode for `scripts/00_generation_frequency_analysis_v1.py`):**
    ```python
    # For db in [ACM_API_WRAPPER, IEEE_API_WRAPPER]:
    #   For gen_keyword_set in [SKYLAKE_KEYWORDS, CASCADE_KEYWORDS, ICE_KEYWORDS, SAPPHIRE_KEYWORDS, ...]:
    #     query = construct_query(base_slr_keywords, gen_keyword_set, date_range="2015-2025")
    #     num_results, top_venues, top_keywords = db.execute_and_analyze(query)
    #     log_result(db_name, gen_keyword_set, num_results, top_venues, top_keywords)
    # Aggregate results and generate frequency table/chart.
    ```
* **Evidence of Results (To be updated with actual data in Protocol Appendix B.1):** By 2025-05-21, update the generation-specific publication frequency table, top publication venues, and keyword analysis results. This will serve to re-validate or adjust the decision to focus on Skylake-SP, Cascade Lake-SP, and Ice Lake-SP.

**1.3.3. Final Search Query Strings (Execution Plan for Supervisor Feedback Item #2 - Protocol Appendix B.2):**
* **Execution Plan:** By 2025-05-21, complete and document the finalized full query strings for each database (ACM DL and IEEE Xplore prioritized) in Appendix B.2. These strings will be in a copy-paste ready format, explicitly utilizing field specifications (TI, AB, AUFK, CCS, IEEE Terms), wildcards (*, ?), exact phrases ("..."), Boolean operators, parenthesis for precedence, and keyword groups from the synonym list (`Synonym_List_v1.2.csv`).
* **Query Example (ACM DL - To be presented immediately in the main document):**
    ```sql
    -- ACM Digital Library - FINALIZED QUERY EXAMPLE (Skylake-SP, Cascade Lake-SP, Ice Lake-SP) --
    (
      (
        (TI:( "linked list" OR "unrolled list" OR "skip list" OR "pointer chasing" OR "dynamic list" )) OR (AB:( "linked list" OR "unrolled list" OR "skip list" OR "pointer chasing" OR "dynamic list" ))
      ) AND (
        (TI:( cache OR L1D OR L2 OR "L3 cache" OR LLC OR prefetch* OR "stream prefetcher" OR "IP prefetcher" OR "DCU prefetcher" OR "spatial prefetcher" OR "memory hierarchy" OR "cache optimi*" OR "prefetch optimi*" )) OR (AB:( cache OR L1D OR L2 OR "L3 cache" OR LLC OR prefetch* OR "stream prefetcher" OR "IP prefetcher" OR "DCU prefetcher" OR "spatial prefetcher" OR "memory hierarchy" OR "cache optimi*" OR "prefetch optimi*" ))
      ) AND (
        (TI:( optimi* OR perform* OR efficien* OR aware OR friendly OR conscious OR layout OR placement OR tuning OR interact* OR strateg* OR polic* OR improvement OR speedup OR reduction )) OR (AB:( optimi* OR perform* OR efficien* OR aware OR friendly OR conscious OR layout OR placement OR tuning OR interact* OR strateg* OR polic* OR improvement OR speedup OR reduction ))
      )
    ) AND (
      (TI:( "Intel Xeon" OR Skylake OR "Cascade Lake" OR "Ice Lake" OR SKX OR CLX OR ICX OR "Xeon SP" OR "Xeon Scalable" )) OR (AB:( "Intel Xeon" OR Skylake OR "Cascade Lake" OR "Ice Lake" OR SKX OR CLX OR ICX OR "Xeon SP" OR "Xeon Scalable" )) OR (KW:( "Intel Xeon" OR Skylake OR "Cascade Lake" OR "Ice Lake" OR SKX OR CLX OR ICX OR "Xeon SP" OR "Xeon Scalable" )) /* KW for Author Keywords */
    ) AND (
      (ACMConcepts.concept_name:"Computer systems organization" -> ACMConcepts.concept_name:"Architectures" -> ACMConcepts.concept_name:"Parallel architectures") OR (ACMConcepts.concept_name:"Hardware" -> ACMConcepts.concept_name:"Memory and dense storage" -> ACMConcepts.concept_name:"Memory hierarch") /* Example CCS Filtering */
    )AND ( PublicationDate:[01/01/2015 TO 05/19/2025] )AND ( PublicationType:"Conference Proceedings" OR PublicationType:"Journal Articles" )
    // Execution Log: 2025-05-21 10:00 KST, [Your Name], Used ACM DL Advanced Search, direct input of the above query string.
    ```

**1.3.4. Search Execution and Logging (Reflecting Supervisor Feedback Item #8):**
* Execute `scripts/01_execute_search_v1.py` (scheduled for 2025-05-22).
* For each database query execution, automatically generate and commit to GitHub a JSON log file (e.g., `logs/search_execution_log_[DB_Name]_[QueryID]_[Timestamp].json`) containing timestamp, exact query used, number of results, and downloaded filename.

### 1.4. Study Selection Criteria (Execution Plan for Supervisor Feedback Item #3 - Protocol Appendix C)

* **Inclusion/Exclusion Criteria Table (Appendix C.1):** Based on the table from v1.0, with at least two concrete examples (actual paper titles or detailed hypothetical scenarios) for each criterion to ensure objective judgment.
* **Exception Handling Guidelines (Appendix C.2 - To be updated based on actual cases):**
    * **"List of Exceptionally Included Workshop Papers and Rationale" (Appendix C.2.1):** For actual candidate workshop papers identified during initial screening (e.g., OOPSLA'19 WS "Early Ideas..."), comprehensively review factors like "direct relevance to the research topic," "presentation of quantitative results," "absence of a subsequent full paper," and "community citation impact." If included, detail the rationale in a table in Appendix C.2.1. (Review and list actual candidates by 2025-05-28).
    * **"Ambiguous Paper Adjudication Case Analysis" (Appendix C.2.2):** Select 5 actual papers that caused significant disagreement or were difficult to judge during pilot screening (Section 2.2.2). For each paper, systematically record: (1) the point of ambiguity, (2) initial independent judgments and rationale from both reviewers, (3) summary of working group discussion, and (4) final consensus judgment and detailed rationale. This clarifies the practical application of selection criteria. (Target completion: 2025-06-05).
* **List of Permitted Simulators and Validation Criteria (Appendix C.3):** gem5 (v20.0-v24.0), ZSim (v1.0-v2.0), Sniper (v7.0-v8.0), Intel SDE (latest). Papers using other simulators will only be included if (1) they cite existing literature validating the simulator's cycle accuracy/effectiveness, or (2) the paper itself presents validation results (e.g., comparison with real hardware). Failure to meet these criteria will result in exclusion due to "inadequate research methodology."

### 1.5. Study Quality Assessment Criteria (Protocol Appendix D)

* **QA Checklist (Appendix D.1 - To be detailed referencing Carrera-Rivera et al., Table 5 and [22, 25, 164, 165, 169, 336, 337, 341]):**
    1.  **Reporting Clarity:** Are research objectives/questions clear? (Y/P/N)
    2.  **Rigor of Design:** Is the experimental/simulation environment (CPU model, memory, OS, compiler, etc.) detailed? Is the baseline clear and appropriate? Is workload selection justified and diverse?
    3.  **Methodological Reproducibility:** Is the core algorithm or design of the proposed technique detailed enough for another researcher to understand and (in principle) reimplement?
    4.  **Adequacy of Results Presentation:** Are key performance metrics presented quantitatively and clearly? Is statistical processing (mean, standard deviation, number of repetitions, etc.) mentioned?
    5.  **Validity of Conclusions:** Are conclusions logically derived from the presented results?
    6.  **Discussion of Limitations:** Did the authors acknowledge and discuss the limitations or threats to validity of their study?
* Each item scored 2 (Yes), 1 (Partially), 0 (No/Unclear). Max score: 12 points.
* **Minimum Quality Score (Cut-off):** 7 points (approx. 60%). (Possibility of adjustment based on score distribution will be noted).

### 1.6. Data Extraction Strategy (Execution Plan for Supervisor Feedback Item #5 - Protocol Appendix E)

* **Data Extraction Template/Codebook (Appendix E.1 - Based on v1.0, with clear automated tagging fields):**
    * For "Core Optimization Technique Classification (9A)" and "Detailed Technique Keywords (9B)," utilize a hierarchical codebook (`data/codebooks/optimization_keywords_v1.2.xlsx`) with defined Category -> Sub-Category -> Specific Keyword/Pattern and regular expression mapping rules.
* **Automated Tagging and Structuring Script (Appendix E.2 - `scripts/04_auto_tag_and_structure_data_v1.py`):**
    * **Execution Plan:** Input text extracted from PDFs (abstract, conclusion, methodology sections, etc.) will be processed. The script will use regular expressions from the codebook to primarily populate "Detailed Technique Keywords (9B)." These keywords will then be mapped to higher-level categories (9A). The "Tech. Detail" field will be completely removed.
    * **Pseudocode Example (Enhanced Version):**
        ```python
        # scripts/04_auto_tag_and_structure_data_v1.py
        # import pandas as pd; import re; import nltk # (nltk for tokenization/stemming if needed)
        # CODEBOOK_DF = pd.read_excel('data/codebooks/optimization_keywords_v1.2.xlsx')
        # def process_paper_text_for_tags(text_content, codebook_df):
        #   extracted_data = {'Opt_Tech_Main_Categories': set(), 'Opt_Tech_Specific_Keywords': set(), ...}
        #   text_normalized = text_content.lower() # (or more advanced NLP preprocessing)
        #   for index, row in codebook_df.iterrows():
        #     if re.search(row['RegexPattern'], text_normalized):
        #       extracted_data['Opt_Tech_Main_Categories'].add(row['MainCategory'])
        #       extracted_data['Opt_Tech_Specific_Keywords'].add(row['SpecificKeyword'])
        #       # Create dummy variables, e.g., extracted_data[f"DUMMY_{row['SpecificKeyword'].replace(' ','_')}"] = 1
        #   # ... (convert sets to lists/strings for CSV) ...
        #   return extracted_data
        ```
* **Data Extraction Evidence (To be updated with actual execution results in Protocol Appendix F):**
    * **Execution Plan:** By 2025-06-10, apply the above script (with manual verification/complementation) to 5 actual papers selected from the pilot screening.
    * **Results Presentation:** Present a complete data extraction results table for the 5 papers (all columns, especially 9A, 9B, 15A-D, 16A-C populated with structured values), the codebook version used, and a summary of the script execution log. (Utilize the table format from v1.0, but populate with actual extracted data).

---

## Part 2: Conducting the Review
*(Reference: Carrera-Rivera et al. (2022), Section 3 "Conducting")*

### 2.1. Execution of the Search
* **Execution:** Run `scripts/01_execute_search_v1.py` (starting 2025-05-22, expected 3 days duration). Consolidate all search results into the Zotero group library (`SLR_Xeon_LinkedList_Optimization`). Remove duplicates using Zotero's built-in features and manual review. Save final results as `data/raw_search_results/all_unique_studies_v1.0.bib` (BibTeX) and CSV.

### 2.2. Study Selection (PRISMA-based)

* **PRISMA Flow Diagram Plan (Execution Plan for Supervisor Feedback Item #6 - Protocol Appendix G):**
    * **Preliminary Screening Execution Report (Appendix G.1 - To be updated with actual data):** (As planned in v1.0, report actual filtering results for 200 items each from Google Scholar and ACM DL by 2025-05-21 (screenshots, numbers), and readjust overall PRISMA estimates accordingly.)
    * **PRISMA Stage-wise Estimated Numbers (Appendix G.2 - Very conservative, including sensitivity analysis):** (Further refine the numerical plan from v1.0 based on Appendix G.1 results. Include a sensitivity analysis plan for how variations in the final number of included papers (e.g., 20, 30, 40) might affect the scope/depth of analysis and the robustness of conclusions.)
* **Phase 1 Screening (Title/Abstract):** Use Rayyan QCRI. Two reviewers independently. (`data/screening/phase1_decisions_[reviewer_initials].csv`)
* **Reviewer Agreement Assessment (Pilot Actual Execution):** (Utilize results from Appendix H of Section 1.4) If κ < 0.8, re-discuss criteria and conduct full re-screening or third-party review for disagreements.
* **Phase 2 Screening (Full Text):** After PDF acquisition, two reviewers independently. (`data/screening/phase2_decisions_[reviewer_initials].csv`)
* **Final List of Included Studies:** `data/final_selection/included_studies_final_v1.0.xlsx` (Record reasons for exclusion at each stage using codes).

### 2.3. Quality Assessment
* For all finally included studies, two reviewers independently assess quality based on the QA checklist (Appendix D.1). Record results in `data/quality_assessment/QA_scores_v1.0.xlsx`. Total scores and individual item scores can be used for grouping papers during analysis.

### 2.4. Data Extraction
* For all finally included studies, two reviewers independently extract data using the data extraction template (Appendix E.1) and script (Appendix E.2). Consolidate results in `data/extracted_data/full_extracted_dataset_final_v1.0.xlsx`. Resolve all disagreements through discussion and record the rationale for final decisions.

---

## Part 3: Analysis and Reporting
*(Reference: Carrera-Rivera et al. (2022), Section 3.4 "Analysis and Report")*

### 3.1. Data Synthesis and Analysis

* **Descriptive Statistics:** Execute `scripts/05_descriptive_stats_v1.py`. Visualize distributions of publications by year/venue/CPU generation, frequency of major optimization techniques (tags), etc. (in `results/figures/`).
* **Taxonomy Development:** Use VOSviewer or Python (matplotlib, seaborn, scikit-learn clustering) for co-occurrence analysis of "Detailed Technique Keywords" and generate a visual taxonomy map.
* **Performance Comparison Analysis:** Use normalized performance results (15B) to visualize the distribution of performance improvement effects by technique classification/CPU generation (Box plots, etc.). (State that meta-analysis might be limited due to study heterogeneity).
* **Synthesis of Limitations and Gaps:** Code extracted limitations (author-stated + reviewer-identified) by theme and analyze frequency (nltk may be used).
* **Statistical Testing (if necessary):** (Maintain plan from v1.0).

### 3.2. Answering RQs and Discussion
* (Maintain plan from v1.0).

### 3.3. Proposing Future Research Agenda
* (Maintain plan from v1.0).

### 3.4. Report Writing and Dissemination

* **Report Structure (Based on v1.0 plan, emphasizing "Gap Analysis" section):** Within the "4. Results" section, include a sub-section "4.X Gap Analysis of Key Studies' Limitations," with in-depth narrative and a table (PaperID/CoreContribution/EvaluationEnv/MainResults/ExplicitLimitations/ReviewerIdentifiedGap_And_Rationale).
* **Re-evaluate Target Journals/Conferences:** Based on the depth and scope of analysis results, re-select target venues such as ACM Computing Surveys, IEEE TPDS (Survey Track), or top-tier computer architecture/systems conferences (ISCA, ASPLOS, MICRO - if surveys are publishable).
* **Data and Script Publication:** Provide GitHub repository link with final paper submission and, if necessary, archive dataset on Figshare/Zenodo.