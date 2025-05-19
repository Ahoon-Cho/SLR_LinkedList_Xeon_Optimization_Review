# scripts/utils/logger_setup.py (setup_logger 함수 수정 부분)
import logging
import json
import datetime
import os

def setup_logger(script_name_for_log_file, log_dir_relative_to_root="logs", log_level_str="INFO"): # log_level_str 추가
    """
    Sets up a JSON logger for a given script.
    ... (이하 설명 동일) ...
    """
    # 로그 레벨 문자열을 logging 모듈의 실제 레벨 값으로 변환
    numeric_level = getattr(logging, log_level_str.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level_str}')

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) # scripts/utils 기준이므로 두 단계 위가 프로젝트 루트
    actual_log_dir = os.path.join(project_root, log_dir_relative_to_root) # 로그 디렉토리 경로 수정

    if not os.path.exists(actual_log_dir):
        os.makedirs(actual_log_dir)

    base_script_name = os.path.splitext(os.path.basename(script_name_for_log_file))[0]
    log_filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{base_script_name}.json"
    log_filepath = os.path.join(actual_log_dir, log_filename)

    logger = logging.getLogger(base_script_name)
    logger.setLevel(numeric_level) # 변환된 숫자 레벨 사용

    if not logger.handlers:
        fh = logging.FileHandler(log_filepath, encoding='utf-8')
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # 콘솔에도 INFO 레벨 이상은 출력 (디버깅에 용이)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO) # 콘솔에는 INFO 이상만 (DEBUG는 파일에만)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(console_formatter)
        logger.addHandler(ch)
            
    return logger

# log_event 함수는 변경 없음
def log_event(logger, event_type, data_dict):
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'event_type': event_type,
        **data_dict
    }
    logger.info(json.dumps(log_entry, ensure_ascii=False, indent=2))