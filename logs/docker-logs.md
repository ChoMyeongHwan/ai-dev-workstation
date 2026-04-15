# Docker Logs

##  1. Docker 설치 점검

### 버전 정보
- Docker version 28.5.2, build ecc6942

### docker info 주요 항목
- Server Version: `28.5.2`
- Storage Driver: `overlay2`
- Total Memory: `15.67GiB`

### hello-world 실행 결과
docker run hello-world<br>
→ Hello from Docker!<br>
→ 이미지 pull → 컨테이너 실행 → 출력 → 종료 정상 확인

## 스크린샷
![docker info](screenshots/docker-info.png)
![hello-world](screenshots/hello-world.png)


## 2. 컨테이너 기본 실행

### 주요 명령어 정리
| 명령어 | 설명 |
|--------|------|
| docker run -it ubuntu bash | 대화형 컨테이너 실행 |
| docker run -d --name [이름] [이미지] | 백그라운드 실행 |
| docker ps | 실행 중인 컨테이너 목록 |
| docker ps -a | 전체 컨테이너 목록 |
| docker stop [이름] | 컨테이너 중지 |
| docker rm [이름] | 컨테이너 삭제 |

### 실행 결과
- ubuntu 컨테이너 진입 및 내부 명령어 실행 확인
- nginx 백그라운드 실행 → 중지 → 삭제 완료

## 스크린샷
![ubuntu 컨테이너](screenshots/ubuntu-container.png)
![docker ps](screenshots/docker-ps.png)


## 3. 커스텀 이미지 제작

### Dockerfile 구조
| 명령어 | 역할 |
|--------|------|
| FROM | 베이스 이미지 지정 |
| LABEL | 메타데이터 추가 |
| RUN | 빌드 시 명령어 실행 |
| WORKDIR | 작업 디렉토리 설정 |
| COPY | 파일 복사 |
| ENV | 환경변수 설정 |
| EXPOSE | 포트 노출 선언 |
| CMD | 컨테이너 시작 시 실행 명령어 |

### 빌드 결과
- 이미지명: ai-workstation:v1
- 베이스: ubuntu:22.04
- 설치 패키지: python3, pip, curl

## 스크린샷
![Dockerfile](screenshots/dockerfile.png)
![docker build](screenshots/build.png)


## 4. 포트 매핑 테스트

### 포트 매핑 개념
호스트(Mac) 컨테이너<br>
8080 →→→→→ 8080<br>
localhost:8080 으로 접속하면 컨테이너 내부 8080 포트로 연결됨

### 명령어
```zsh
docker run -d --name ai-web -p 8080:8080 ai-workstation:v1
```

### 실행 결과
- curl http://localhost:8080 → HTML 응답 확인
- docker logs ai-web → 접속 로그 확인

## 스크린샷
![포트 매핑](screenshots/port-mapping.png)
![curl 결과](screenshots/curl.png)

