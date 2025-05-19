# SLR on Linked List Optimization for Intel Xeon Cache/Prefetchers
This project conducts a Systematic Literature Review (SLR) to analyze research trends in optimizing linked list performance concerning cache and hardware prefetchers on modern Intel Xeon server CPUs.

## Project Goal
To identify, synthesize, and evaluate techniques for linked list optimization on selected Intel Xeon generations (Skylake-SP, Cascade Lake-SP, Ice Lake-SP), focusing on cache/prefetcher interactions and their impact on linked list traversal.

## Review Question
1. What are the key design principles (e.g., layout, allocation, prefetching control) and methodologies (experimental environments, simulator types/versions, workloads) that were mainly used to optimize the cache efficiency of linked lists or their interaction with major hardware prefetchers (L1D streams/IPP, L2 streams/Spatial) in Intel Xeon Skylake-SP, Cascade Lake-SP, and Ice Lake-SP environments, and what are their quantitative performance improvements?
2. What are the common limitations of the studies identified in RQ1 (e.g., dependence on specific workloads, simplification of the prefetcher model, lack of consideration of NUMA environment) and what are the major research gaps that have not been addressed to date?
3. Considering the advancement of next-generation Intel Xeon architectures (e.g., Granite Rapids and beyond) and memory technologies (e.g., CXL 2.0/3.0, DDR5/6), what are the urgent future research topics and technical challenges that need to be addressed for linked list cache/prefetcher optimization?


## Key Personnel
- Researcher: Ahoon Cho (email: 30526@cnsa.hs.kr)
- Supervisor: -NU-

## How to Run Scripts
1. -NU-

## Project Structure
- `/protocol`: Contains the SLR protocol documents.
- `/scripts`: Contains Python scripts for search, screening, data extraction, analysis.
- `/data`: Contains raw search results, screening decisions, extracted data, codebooks.
- `/results`: Contains analysis outputs like charts, tables.
- `/report`: Contains the LaTeX source or final PDF of the review paper.
- `/logs`: Contains execution logs for all scripts.
- `/appendices`: Contains supplementary materials for the report.

## Report Writing (LaTeX on Overleaf)
The final report will be written using LaTeX on Overleaf.
Project Link: [https://www.overleaf.com/project/682ae5c7631c330e77ca9f1e]