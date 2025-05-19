# scripts/utils/logger_setup.py
import logging
import json
import datetime
import os

def setup_logger(script_name_for_log_file, log_dir="../../logs"):
    """
    Sets up a JSON logger for a given script.

    Args:
        script_name_for_log_file (str): The name of the script, used for the log filename.
        log_dir (str): Directory to save log files. Defaults to '../../logs'
                       assuming this script is in scripts/utils/.
    Returns:
        logging.Logger: Configured logger instance.
    """
    # 로그 파일명을 위한 현재 스크립트 이름 (확장자 제외)
    base_script_name = os.path.splitext(os.path.basename(script_name_for_log_file))[0]

    # 로그 디렉토리 생성 (없으면)
    # utils 폴더 기준으로 상대 경로이므로, 실제 logs 폴더 위치에 맞게 조정 필요.
    # 이 setup_logger를 호출하는 스크립트의 위치를 기준으로 log_dir 경로를 잡는게 더 일반적일 수 있음
    # 여기서는 호출하는 스크립트가 직접 로그 파일 경로를 생성해서 넘겨주는 것을 가정하거나,
    # 또는 이 함수의 log_dir 기본값을 프로젝트 루트 기준으로 변경하는 것을 고려.
    # 현재는 utils 폴더 기준으로 두 단계 상위의 logs 폴더를 의미함.
    # 프로젝트 루트에 logs 폴더가 있다고 가정하고 경로 재설정:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    actual_log_dir = os.path.join(project_root, "logs")

    if not os.path.exists(actual_log_dir):
        os.makedirs(actual_log_dir)

    log_filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{base_script_name}.json"
    log_filepath = os.path.join(actual_log_dir, log_filename)

    logger = logging.getLogger(base_script_name) # 로거 이름도 스크립트 이름으로
    logger.setLevel(logging.INFO) # INFO 레벨 이상의 로그만 기록

    # 다른 핸들러가 중복 추가되는 것을 방지
    if not logger.handlers:
        # 파일 핸들러 설정: JSON 형식으로 로그 기록
        fh = logging.FileHandler(log_filepath, encoding='utf-8')
        # JSON 형식을 직접 만들 것이므로 포맷터는 기본으로 두거나, 아예 메시지만 남기도록.
        # 여기서는 log_event 함수에서 직접 json.dumps를 사용하므로, 메시지만 전달.
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # (선택 사항) 콘솔 핸들러: 터미널에도 로그 출력 (디버깅 시 유용)
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)
        # console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)')
        # ch.setFormatter(console_formatter)
        # logger.addHandler(ch)

    return logger

def log_event(logger, event_type, data_dict):
    """
    Logs an event as a JSON string.

    Args:
        logger (logging.Logger): The logger instance to use.
        event_type (str): Type of the event (e.g., 'script_start', 'data_processing', 'error').
        data_dict (dict): Dictionary containing data related to the event.
    """
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'event_type': event_type,
        **data_dict # data_dict의 모든 키-값 쌍을 log_entry에 추가
    }
    logger.info(json.dumps(log_entry, ensure_ascii=False, indent=2)) # indent로 보기 좋게