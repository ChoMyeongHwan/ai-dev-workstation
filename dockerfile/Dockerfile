# ① 베이스 이미지 (어떤 OS 위에서 시작할지)
FROM ubuntu:22.04
# → "우분투 22.04를 기반으로 시작할게"
# → 마치 빈 컴퓨터에 OS 설치하는 것과 같음

# ② 메타데이터 (이미지 정보 태그)
LABEL maintainer="first-image"
LABEL description="AI Dev Workstation Practice Image"
# → 이미지에 붙이는 이름표 (없어도 동작함)

# ③ 패키지 설치 (OS에 프로그램 설치)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*
# → "apt-get update"  : 패키지 목록 최신화
# → "apt-get install" : python3, pip, curl 설치
# → "rm -rf ..."      : 설치 후 캐시 삭제 (이미지 용량 줄이기)
# → && 로 연결하면 하나의 레이어로 합쳐짐 (최적화!)

# ④ 작업 디렉토리 설정
WORKDIR /app
# → 컨테이너 내부에서 기본으로 위치할 폴더
# → 없으면 자동 생성됨
# → 이후 COPY, CMD 명령어는 이 경로 기준으로 실행됨

# ⑤ 파일 복사 (내 컴퓨터 → 컨테이너 내부)
COPY index.html .
COPY app.py .
# → "내 컴퓨터의 index.html을 컨테이너 /app/index.html로 복사"
# → . 은 WORKDIR(/app) 을 의미

# ⑥ 환경변수 설정
# ❌ 기존: ENV APP_ENV=development
# ✅ 변경: PORT 환경 변수 기본값 설정
ENV APP_ENV=development
ENV PORT=8080
# → Dockerfile에서 기본값을 설정해두는 것
# → docker-compose.yml에서 덮어쓰기(override) 가능

# → Python 출력 버퍼링 해제 (실시간 로그 확인 위해)
ENV PYTHONUNBUFFERED=1 

# ⑦ 포트 노출 선언
EXPOSE 8080
# → "이 컨테이너는 8080 포트를 사용할 거야" 라는 선언
# → 실제 포트 연결은 docker run -p 에서 함

# ⑧ 컨테이너 시작 시 실행할 명령어
CMD ["python3", "app.py"]
# → 컨테이너가 실행될 때 자동으로 실행되는 명령어
# → "python3 app.py" 를 실행해서 웹서버 시작