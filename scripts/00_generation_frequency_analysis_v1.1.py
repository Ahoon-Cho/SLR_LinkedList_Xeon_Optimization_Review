# scripts/00_generation_frequency_analysis_v1.1.py
import argparse
import json
import os
import datetime
import csv
import sys
import pandas as pd # Synonym_List.csv를 읽기 위해 pandas 사용

# --- 로거 설정 (이전과 동일) ---
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
project_root = os.path.dirname(current_dir)
utils_dir_path = os.path.join(current_dir, "utils")
if current_dir not in sys.path:
    sys.path.append(current_dir)
from utils.logger_setup import setup_logger, log_event
logger = None
# --- 로거 설정 끝 ---

# --- 상수 정의 (이전과 동일) ---
CPU_KEYWORDS_FILE_DEFAULT = "../data/codebooks/cpu_generation_keywords_v1.0.json"
SYNONYM_LIST_FILE_DEFAULT = "../data/codebooks/Synonym_List_v1.3.csv" # Synonym_List 파일 경로 추가
OUTPUT_DIR_DEFAULT = "../results/00_generation_frequency_analysis_output"
# --- 상수 정의 끝 ---

def load_cpu_keywords(filepath):
    # (이전과 동일한 함수 내용)
    global logger
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        log_event(logger, "file_loaded", {"file_type": "CPU Keywords", "path": filepath, "generations_found": len(data)})
        return data
    except FileNotFoundError:
        log_event(logger, "file_not_found_error", {"file_type": "CPU Keywords", "path": filepath})
        print(f"ERROR: CPU keywords file not found at {filepath}")
        return None
    except json.JSONDecodeError as e:
        log_event(logger, "json_decode_error", {"file_type": "CPU Keywords", "path": filepath, "error": str(e)})
        print(f"ERROR: Could not decode JSON from {filepath}. Error: {e}")
        return None
    except Exception as e:
        log_event(logger, "generic_error_loading_cpu_keywords", {"file_type": "CPU Keywords", "path": filepath, "error": str(e)})
        print(f"ERROR: An unexpected error occurred while loading {filepath}. Error: {e}")
        return None

def load_synonyms_for_categories(filepath, categories_map):
    """
    지정된 경로의 Synonym_List CSV 파일에서 특정 카테고리에 해당하는 모든 용어(Main_Term 및 Synonyms)를 로드합니다.
    categories_map: {'query_component_name': ['Category_in_CSV_1', 'Category_in_CSV_2'], ...}
    """
    global logger
    synonyms_data = {key: set() for key in categories_map.keys()} # 각 쿼리 구성요소별로 set 초기화
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        log_event(logger, "file_loaded", {"file_type": "Synonym List", "path": filepath, "rows_loaded": len(df)})

        for query_component, csv_categories in categories_map.items():
            for category in csv_categories:
                category_df = df[df['Term_Category'] == category]
                for _, row in category_df.iterrows():
                    terms_to_add = [row['Main_Term']]
                    # Synonym 컬럼들이 있는지 확인하고 추가 (Synonym_1, Synonym_2, ...)
                    for i in range(1, 6): # Synonym_5 까지 있다고 가정
                        syn_col = f'Synonym_{i}'
                        if syn_col in row and pd.notna(row[syn_col]):
                            terms_to_add.append(row[syn_col])
                    
                    for term in terms_to_add:
                        if pd.notna(term) and term.strip(): # NaN 이 아니고 빈 문자열이 아니면 추가
                             # 검색어 최적화를 위해, 여러 단어로 된 구문은 따옴표로 묶기
                            if ' ' in term.strip() and not (term.startswith('"') and term.endswith('"')):
                                synonyms_data[query_component].add(f'"{term.strip()}"')
                            else:
                                synonyms_data[query_component].add(term.strip())
        
        # set을 list로 변환
        final_synonyms = {key: list(value) for key, value in synonyms_data.items()}
        log_event(logger, "synonyms_processed_for_categories", {"categories_map": categories_map, "num_terms": {k: len(v) for k,v in final_synonyms.items()}})
        return final_synonyms

    except FileNotFoundError:
        log_event(logger, "file_not_found_error", {"file_type": "Synonym List", "path": filepath})
        print(f"ERROR: Synonym List file not found at {filepath}")
        return {key: [] for key in categories_map.keys()} # 빈 리스트 반환
    except Exception as e:
        log_event(logger, "synonym_load_error", {"file_type": "Synonym List", "path": filepath, "error": str(e)})
        print(f"ERROR: Could not load or process Synonym List from {filepath}. Error: {e}")
        return {key: [] for key in categories_map.keys()}

# get_acm_manual_search_results 함수 (이전과 동일, base_query_parts를 인자로 받음)
def get_acm_manual_search_results(cpu_generation_data, base_query_parts, start_year, end_year):
    # (내용은 이전 답변과 동일하게 유지, base_query_parts['data_structure'] 등으로 접근)
    global logger
    results_data = []
    print("\n--- ACM Digital Library Manual Search Instructions ---")
    print(f"Please use the Advanced Search feature on the ACM Digital Library website (dl.acm.org).")
    print(f"Ensure the search period is set from: {start_year}-01-01 TO {end_year}-12-31 (or current month/day for end_year if applicable)")
    print(f"Ensure Document Types are filtered to: Conference Proceedings, Journal Articles")
    
    print("\nBase query components to combine (use AND logic between groups):")
    # base_query_parts 딕셔너리의 각 키에 대해 OR로 묶인 문자열을 생성하여 출력
    # 예시: base_query_parts = {'data_structure': ['"linked list"', ...], 'optimization_target': [...], ...}
    if base_query_parts.get('data_structure'):
        print(f"  1. Data Structures (e.g., in Abstract): ({' OR '.join(base_query_parts['data_structure'])})")
    if base_query_parts.get('optimization_target'):
        print(f"  2. Optimization Target (e.g., in Abstract): ({' OR '.join(base_query_parts['optimization_target'])})")
    if base_query_parts.get('optimization_goal_method'):
        print(f"  3. Optimization Goal/Method (e.g., in Abstract): ({' OR '.join(base_query_parts['optimization_goal_method'])})")
    print(f"  4. General CPU Term (e.g., in Abstract): \"Intel Xeon\"") # 이것은 고정

    log_event(logger, "manual_search_start", {"database": "ACM DL", "num_generations_to_query": len(cpu_generation_data)})

    for gen_name, keywords in cpu_generation_data.items():
        print(f"\n--- Input results for Generation: {gen_name} ---")
        # 각 키워드에 따옴표 추가 (공백이 있는 경우)
        gen_keywords_quoted = [f'"{k}"' if ' ' in k else k for k in keywords]
        gen_keyword_string_for_search = f"({' OR '.join(gen_keywords_quoted)})"
        print(f"  5. Specific Generation Keywords (e.g., in Abstract): {gen_keyword_string_for_search}")
        # ... (이하 수동 입력 안내 및 로직 동일) ...
        while True:
            try:
                count_str = input(f"   Enter the total number of results found for '{gen_name}': ")
                count = int(count_str)
                if count >= 0:
                    break
                else:
                    print("   Please enter a non-negative integer.")
            except ValueError:
                print("   Invalid input. Please enter an integer (e.g., 123).")
        
        entry = {
            "Database": "ACM DL",
            "CPU_Generation": gen_name,
            "Search_Keywords_Generation_Used": ', '.join(keywords),
            "Publication_Count": count,
            "Search_Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Search_Period_Start": f"{start_year}-01-01",
            "Search_Period_End": f"{end_year}-12-31", # 실제 검색 시 사용한 종료일
            "Notes": "Manual search on ACM DL Advanced Search. User input."
        }
        results_data.append(entry)
        log_event(logger, "manual_search_data_entered", {"database": "ACM DL", "generation": gen_name, "count": count})
    
    print("\n--- ACM Digital Library Manual Search Data Collection Complete ---")
    log_event(logger, "manual_search_end", {"database": "ACM DL", "total_entries_collected": len(results_data)})
    return results_data


# save_to_csv 함수 (이전과 동일)
def save_to_csv(data_list, filepath):
    # (내용은 이전 답변과 동일하게 유지)
    global logger
    if not data_list:
        log_event(logger, "save_to_csv_nodata", {"file_path": filepath, "message": "No data provided to save."})
        print("No data to save.")
        return
    
    if isinstance(data_list, dict): 
        data_list = [data_list]

    header = []
    if data_list:
        header = list(data_list[0].keys())
        for item in data_list:
            for key in item.keys():
                if key not in header:
                    header.append(key)
    else: 
        log_event(logger, "save_to_csv_empty_data_no_header", {"file_path": filepath})
        print(f"Cannot save CSV: data list is empty, unable to determine header for {filepath}")
        return

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=header)
            dict_writer.writeheader()
            dict_writer.writerows(data_list)
        log_event(logger, "csv_file_saved", {"file_path": filepath, "records_saved": len(data_list)})
        print(f"Results successfully saved to {filepath}")
    except IOError as e:
        log_event(logger, "csv_save_io_error", {"file_path": filepath, "error": str(e)})
        print(f"IOError: Could not write to CSV file at {filepath}. Error: {e}")
    except Exception as e:
        log_event(logger, "csv_save_generic_error", {"file_path": filepath, "error": str(e)})
        print(f"ERROR: An unexpected error occurred while saving CSV to {filepath}. Error: {e}")


def main(args):
    global logger
    logger = setup_logger(os.path.basename(__file__), log_level_str=args.log_level)
    
    log_event(logger, "script_execution_started", {
        "script_name": os.path.basename(__file__),
        "arguments": vars(args)
    })

    if not os.path.exists(args.output_dir):
        try:
            os.makedirs(args.output_dir)
            log_event(logger, "output_directory_created", {"path": args.output_dir})
            print(f"Output directory created: {args.output_dir}")
        except OSError as e:
            log_event(logger, "output_directory_creation_error", {"path": args.output_dir, "error": str(e)})
            print(f"ERROR: Could not create output directory {args.output_dir}. Error: {e}")
            return

    cpu_keywords = load_cpu_keywords(args.cpu_keywords_file)
    if not cpu_keywords:
        log_event(logger, "critical_error_cpu_keywords_not_loaded", {})
        print("Critical error: CPU keywords could not be loaded. Exiting.")
        return

    # --- Synonym_List에서 기본 쿼리 구성 요소 로드 ---
    # categories_map: base_query_components의 키가 될 이름과, Synonym_List.csv의 Term_Category 값(들)을 매핑
    categories_to_load_map = {
        "data_structure": ["Data Structure"], # Synonym_List.csv의 'Data Structure' 카테고리 사용
        "optimization_target": ["Cache System", "Hardware Prefetcher", "Prefetcher Type"], # 여러 카테고리 조합 가능
        "optimization_goal_method": ["Optimization Technique", "Optimization"] # 'Optimization'은 일반적인 용어
    }
    base_query_components = load_synonyms_for_categories(args.synonym_list_file, categories_to_load_map)
    
    if not all(base_query_components.values()): # 하나라도 빈 리스트면 오류 처리
        log_event(logger, "critical_error_base_query_components_not_loaded", {"loaded_components": base_query_components})
        print("Critical error: Could not load base query components from Synonym List. Exiting.")
        return
    # --- 기본 쿼리 구성 요소 로드 끝 ---
        
    current_processing_year = datetime.datetime.now().year
    actual_end_year = args.end_year if args.end_year <= current_processing_year else current_processing_year
    if args.end_year > current_processing_year:
        log_event(logger, "year_adjustment_notice", {"input_end_year": args.end_year, "adjusted_end_year": actual_end_year, "reason": "Input end year is in the future."})

    all_results = []

    if "acm" in args.databases:
        log_event(logger, "database_processing_start", {"database": "ACM DL"})
        acm_data = get_acm_manual_search_results(cpu_keywords, base_query_components, args.start_year, actual_end_year)
        
        if acm_data:
            all_results.extend(acm_data)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"ACM_DL_generation_frequency_manual_{timestamp}.csv"
            output_filepath = os.path.join(args.output_dir, output_filename)
            save_to_csv(acm_data, output_filepath)
        log_event(logger, "database_processing_end", {"database": "ACM DL", "records_collected": len(acm_data) if acm_data else 0})
    
    log_event(logger, "script_execution_finished", {"script_name": os.path.basename(__file__)})
    print("Script finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Collects publication frequency for CPU generations from ACM DL (manual) and other DBs (future).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--databases", nargs="+", 
        default=["acm"], 
        choices=["acm", "ieee", "scopus"],
        help="List of databases to process. Currently, only 'acm' triggers manual input mode."
    )
    parser.add_argument(
        "--cpu_keywords_file", type=str, 
        default=CPU_KEYWORDS_FILE_DEFAULT,
        help="Path to the JSON file containing CPU generation keywords."
    )
    parser.add_argument( # Synonym_List 파일 인자 추가
        "--synonym_list_file", type=str,
        default=SYNONYM_LIST_FILE_DEFAULT,
        help="Path to the CSV file containing synonym list for query construction."
    )
    parser.add_argument(
        "--output_dir", type=str, 
        default=OUTPUT_DIR_DEFAULT,
        help="Directory to save output CSV files and logs."
    )
    parser.add_argument(
        "--start_year", type=int, default=2015,
        help="Start year for the search period (inclusive)."
    )
    parser.add_argument(
        "--end_year", type=int, default=datetime.datetime.now().year,
        help="End year for the search period (inclusive). Defaults to the current year."
    )
    parser.add_argument(
        "--log_level", default="INFO", 
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level for the script."
    )
    
    args = parser.parse_args()
    main(args)