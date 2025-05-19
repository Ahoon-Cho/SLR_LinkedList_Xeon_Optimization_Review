# 1. 기본 이미지 설정 (Python 3.10 slim 버전 사용)
FROM python:3.10-slim

# 2. 작업 디렉토리 설정 (이미지 내부 경로)
WORKDIR /app

# 3. 시스템 라이브러리 설치 (필요한 경우)
# 예: git을 설치하거나, 특정 패키지가 의존하는 시스템 라이브러리 설치
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*
# 위 예시는 git을 설치하는 경우입니다. 특별히 필요한 시스템 라이브러리가 없다면 이 RUN 줄은 생략하거나 최소화 가능합니다.

# 4. requirements.txt 파일을 이미지 안으로 복사
COPY requirements.txt .

# 5. requirements.txt에 명시된 Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 6. 현재 디렉토리(로컬 프로젝트 폴더)의 모든 파일을 이미지 안의 작업 디렉토리(/app)로 복사
COPY . .

# 7. (선택 사항) 컨테이너 실행 시 기본적으로 실행될 명령어 설정
# 예: 모든 스크립트를 순차적으로 실행하는 메인 스크립트가 있다면
# CMD ["python", "scripts/main_workflow.py", "--step", "all"]
# 지금은 특정 CMD를 정하기 어려우므로 주석 처리하거나 비워둡니다.