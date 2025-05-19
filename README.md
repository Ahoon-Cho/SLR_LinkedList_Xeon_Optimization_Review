# SLR on Linked List Optimization for Intel Xeon Cache/Prefetchers
This project conducts a Systematic Literature Review (SLR) to analyze research trends in optimizing linked list performance concerning cache and hardware prefetchers on modern Intel Xeon server CPUs.

## Project Goal
1.  To identify and classify key trends (design principles, methodologies, results) in linked list cache/prefetcher optimization research targeting three major Intel Xeon generations (Skylake-SP, Cascade Lake-SP, Ice Lake-SP) over the last decade (2015-2025).
2.  To explore the primary **causal factors** influencing the selection and effectiveness of linked list optimization techniques across these CPU generations.
3.  To identify common limitations and unresolved research gaps in these studies, and critically analyze the **structural reasons** for recurrently observed limitations.
4.  To propose a concrete future research agenda, considering recent CPU architectural advancements and potential **paradigm shifts**.

## Review Questions (RQs - Protocol v3.0)
* **RQ1 (Trends, Techniques & Causal Factors):** In Intel Xeon Skylake-SP, Cascade Lake-SP, and Ice Lake-SP environments, regarding the optimization of linked list cache efficiency or interaction with major hardware prefetchers (L1D stream/IPP, L2 stream/Spatial):
    * (a) What core design principles and methodologies have been predominantly used, and what are their quantitative performance improvement effects?
    * (b) If the choice of these techniques and their effectiveness have varied across CPU generations, what are the primary **technical or methodological factors** driving these changes?
* **RQ2 (Limitations, Gaps & Meta-Analysis of Gaps):** Concerning the studies identified in RQ1:
    * (a) What are their common limitations and the major unresolved research gaps?
    * (b) **Why** do certain limitations (e.g., over-optimization for specific workloads, discrepancies with actual diverse prefetcher behaviors) repeatedly appear and remain fundamentally unresolved? (Exploring structural causes: e.g., academic benchmarking practices, industry's level of hardware information disclosure, limitations of research resources).
* **RQ3 (Future Agenda & Paradigm Shifts):** Considering advancements in next-generation Intel Xeon architectures (e.g., post-Granite Rapids tiled architectures, AI-based prefetchers) and memory technologies (e.g., CXL 2.0/3.0, DDR5/6, Processing-In-Memory):
    * (a) What are the pressing future research topics and technical challenges for linked list cache/prefetcher optimization?
    * (b) What fundamental **paradigm shifts** might these technological changes bring to existing linked list optimization paradigms (e.g., prefetcher-dependent designs), and what should be the research community's response strategy?

## Key Personnel
- Researcher: Ahoon Cho (email: 30526@cnsa.hs.kr)
- Supervisor: -NU-

## How to Run Scripts
1. Clone this repository: `git clone https://github.com/Ahoon-Cho/SLR_LinkedList_Xeon_Optimization_Review.git`
2.  Navigate to the project directory: `cd SLR_LinkedList_Xeon_Optimization_Review_v2`
3.  Set up the Conda environment: `conda env create -f environment.yml`
4.  Activate the environment: `conda activate slr_env`
5.  Navigate to the `scripts/` directory to run individual Python scripts for more options.

## Project Structure
- `/protocol`: Contains the SLR protocol documents (v2.0, v3.0, review logs).
- `/scripts`: Contains Python scripts for search, screening, data extraction, analysis.
  - `/scripts/utils`: Utility scripts like logger setup.
- `/data`: Contains raw search results, screening decisions, extracted data, codebooks.
  - `/data/codebooks`: Synonym lists, keyword dictionaries, workload taxonomies.
  - `/data/raw_search_results`: Raw output from database searches.
  - `/data/screening`: Files related to the screening process (pilot samples, decisions, disagreement logs).
  - `/data/extracted_data`: Final extracted dataset from selected papers.
- `/results`: Contains analysis outputs like charts, tables, and PRISMA diagrams.
- `/report`: Contains the LaTeX source (Overleaf project link below) or final PDF of the review paper.
- `/logs`: Contains execution logs for all scripts.
- `/appendices`: Supplementary materials for the protocol and final report.

## Report Writing (LaTeX on Overleaf)
The final report will be written using LaTeX on Overleaf.
**Overleaf Project Link:** [https://www.overleaf.com/project/682ae5c7631c330e77ca9f1e]

## Changelog
See `CHANGELOG.md` for a history of significant changes to the project and protocol.