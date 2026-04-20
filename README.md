# ai-dev-workstation

Docker, Linux, Git을 활용한 AI 개발 워크스테이션 구축 실습 레포지토리

---

## 📌 프로젝트 개요

* **목표**: 터미널, Docker, Git을 활용한 개발 환경 구축
* **핵심 학습**:

  * Linux CLI
  * Docker 컨테이너
  * Git / GitHub 버전 관리

---

## 🔧 실행 환경

### 시스템 정보

* OS: macOS (Darwin 24.6.0)
* Shell: zsh (/bin/zsh)
* Docker: 28.5.2
* Git: 2.53.0

```zsh
uname -a
Darwin *** 24.6.0 Darwin Kernel Version 24.6.0: Mon Jan 19 22:00:10 PST 2026; root:xnu-11417.140.69.708.3~1/RELEASE_X86_64 x86_64

git --version
git version 2.53.0

docker --version
Docker version 28.5.2, build ecc6942

echo $SHELL
/bin/zsh
```

---

## 🧠 핵심 개념 정리

### 1. 이미지 vs 컨테이너

| 구분 | 이미지 | 컨테이너 |
|------|--------|----------|
| 정의 | 실행 환경의 설계도 | 이미지를 실행한 인스턴스 |
| 상태 | 변경 불가 (읽기 전용) | 변경 가능 (읽기/쓰기) |
| 비유 | 붕어빵 틀 | 실제 붕어빵 |
| 명령어 | `docker build` | `docker run` |
| 저장 | Docker Hub, 로컬 | 로컬에서만 실행 |

```zsh
# 이미지 목록 확인
docker images

# 이미지로 컨테이너 생성 및 실행
docker run nginx

# 하나의 이미지로 여러 컨테이너 생성 가능
docker run --name web-1 nginx
docker run --name web-2 nginx
docker run --name web-3 nginx
```

---

### 2. 포트 직접 접속이 불가능한 이유

컨테이너는 호스트(내 PC)와 격리된 네트워크를 가짐<br>
따라서 브라우저에서 직접 접근 불가

```
# 포트 매핑 없이 실행
docker run nginx
→ 브라우저에서 localhost:80 접속 불가 ❌

# 포트 매핑 후 실행
docker run -p 8080:80 nginx
→ 브라우저에서 localhost:8080 접속 가능 ✅
```

```
[브라우저] → localhost:8080
                  ↓ 포트 매핑 (-p 8080:80)
           [호스트 8080] → [컨테이너 80]
```

- `-p 호스트포트:컨테이너포트` 형식으로 연결
- 호스트 포트 : 내 PC에서 접속할 포트 번호
- 컨테이너 포트 : 컨테이너 내부 서비스 포트 번호

---

## ✅ 수행 항목 체크리스트

* [x] 터미널 조작 로그 기록
* [x] 파일 권한 실습
* [x] Docker 설치 및 점검
* [x] 컨테이너 기본 실행
* [x] 커스텀 이미지 제작
* [x] 포트 매핑 테스트
* [x] 볼륨 영속성 검증
* [x] Git 설정 및 GitHub 연동

---

## 📂 디렉토리 구조

```bash
ai-dev-workstation/
├── README.md
├── logs/                   # 실행 로그 및 스크린샷
│   ├── terminal-logs.md
│   ├── docker-logs.md
│   └── screenshots/
├── dockerfile/             # Docker 관련 파일
│   ├── Dockerfile
│   ├── index.html
│   └── app.py
└── evidence/               # 검증 증거 및 결과
    ├── permission-test.md
    ├── volume-test.md
    └── git-setup.md
```

---

## 🔍 검증 방법 및 결과

* **터미널 조작 로그 기록 완료** → [terminal-logs.md](logs/terminal-logs.md)<br>
mkdir -p 로 디렉토리 구조 생성<br>
절대경로 / 상대경로 실습 완료

* **파일 권한 실습 완료** → [permission-test.md](evidence/permission-test.md)<br>
chmod 755 실행 파일 권한 설정<br>
chmod 644 문서 파일 권한 설정<br>
permission denied 에러 vs 정상 실행 비교 확인

* **Docker 설치 점검 완료** → [docker-logs.md](logs/docker-logs.md)<br>
docker info 로 시스템 정보 확인<br>
docker run hello-world 정상 실행 확인

* **컨테이너 기본 실행 완료** → [docker-logs.md](logs/docker-logs.md)<br>
ubuntu 컨테이너 대화형 실행<br>
nginx 백그라운드 실행 → 중지 → 삭제

* **커스텀 이미지 제작 완료** → [Dockerfile](dockerfile/Dockerfile)<br>
ubuntu:22.04 기반 커스텀 이미지 빌드<br>
ai-workstation:v1 이미지 생성 완료

* **포트 매핑 테스트 완료** → [docker-logs.md](logs/docker-logs.md)<br>
`-p 8080:8080` 포트 매핑 설정<br>
`curl http://localhost:8080` 응답 확인

* **볼륨 영속성 검증 완료** → [volume-test.md](evidence/volume-test.md)<br>
docker volume create ai-data 볼륨 생성<br>
컨테이너 삭제 후 데이터 유지 확인

* **Git 설정 및 GitHub 연동 완료** → [git-setup.md](evidence/git-setup.md)<br>
전역 user.name / user.email 설정<br>
전체 커밋 이력 기록 및 push 완료

---

## 🐛 트러블슈팅

### 1. Git 커밋 작성자(author) 오류
- 문제:
  - GitHub에 push한 커밋의 작성자(name, email)가 의도한 값이 아니라 `username@hostname` 형태로 잘못 기록됨

- 원인 가설:
  - `git config user.name`, `git config user.email` 미설정
  - Git이 OS의 username, hostname 기반으로 자동 생성
  - 잘못된 author 상태로 commit 및 push 진행됨

- 해결 방법:
    ```zsh
    # 1. 사용자 정보 설정
    git config --global user.name "정확한 이름"
    git config --global user.email "GitHub 이메일"

    # 2. 기존 커밋 되돌리기 (내용 유지)
    git reset --soft HEAD~1

    # 3. 다시 커밋
    git commit -m "docs: README 기본 구조 작성"

    # 4. 원격 저장소 강제 반영
    git push origin main --force
    
    ```
- 결과:
  - 커밋 작성자가 정상적으로 수정됨
  - GitHub에서도 올바른 사용자로 표시됨

---

### 2. 컨테이너에서 한글 입력 시 글자가 깨지거나 지워지는 현상
- 문제:
  - Ubuntu 컨테이너 내부에서 echo "한글" 입력 시 글자가 깨지거나, 입력 도중 기존 텍스트가 지워지는 현상 발생

- 원인 가설:
  - 컨테이너의 기본 로케일(locale)이 UTF-8이 아닌 C 또는 POSIX로 설정되어 있어 한글(멀티바이트 문자)을 정상 처리하지 못함

- 확인 방법:
  ```zsh
  locale
  ```

- 해결 방법:
  ```zsh
  # 1. 임시 해결
  export LANG=C.UTF-8

  # 2. 영구 설정 (권장)
  apt update
  apt install -y locales
  locale-gen en_US.UTF-8
  update-locale LANG=en_US.UTF-8
  export LANG=en_US.UTF-8
  
  ```

---

### 3. 포트 충돌 오류
- 문제:
  - 동일한 호스트 포트(8080)로 컨테이너를 2개 실행하려 할 때 두 번째 컨테이너가 실행되지 않음

- 원인 가설:
  - 호스트의 8080 포트가 이미 첫 번째 컨테이너(web-first)에 점유됨
  - 하나의 포트는 동시에 하나의 프로세스만 사용 가능
  - 기존 컨테이너를 중지하지 않은 상태에서 동일 포트로 재실행 시도

- 확인 방법
  ```zsh
  # 실행 중인 컨테이너 및 포트 점유 확인
  docker ps

  # 호스트에서 포트 점유 프로세스 확인 (Mac/Linux)
  lsof -i :8080
  
  ```

- 오류 재현
  ```zsh
  # 첫 번째 컨테이너 실행 (8080 점유)
  docker run -d --name web-first -p 8080:80 nginx

  # 동일 포트로 두 번째 컨테이너 실행 시도
  docker run -d --name web-second -p 8080:80 nginx
  # 💥 Error response from daemon:
  # driver failed programming external connectivity on endpoint web-second:
  # Bind for 0.0.0.0:8080 failed: port is already allocated.

  ```

- 해결 방법
  ```zsh
  # 방법 1: 다른 포트 번호로 변경
  docker run -d --name web-second -p 8081:80 nginx

  # 방법 2: 기존 컨테이너 중지 후 동일 포트 재사용
  docker stop web-first
  docker rm web-first
  docker run -d --name web-second -p 8080:80 nginx

  ```

- 결과
  - docker ps로 각 컨테이너가 서로 다른 포트에 정상 실행됨을 확인
  - localhost:8080, localhost:8081 각각 브라우저 접속 성공

---

## 📚 학습 내용 정리

### 1. 절대 경로 vs 상대 경로

* **절대 경로**: 루트(/)부터 시작하는 전체 경로<br>
예: cd ~/ai-dev-workstation/logs<br>
어디서 실행해도 동일한 위치로 이동<br>

* **상대 경로**: 현재 위치 기준으로 작성하는 경로<br>
예: cd logs / cd ..<br>
현재 위치에 따라 결과가 달라짐<br>

* **핵심 명령어**: `pwd` (현재 위치 확인) / `cd` (디렉토리 이동) / `ls -la` (목록 확인)

---

### 2. 파일 권한 (r/w/x, 755, 644)

* `r`(읽기=4) / `w`(쓰기=2) / `x`(실행=1)<br>
`755` → rwxr-xr-x : 실행 파일, 스크립트에 사용<br>
`644` → rw-r--r-- : 문서, 설정 파일에 사용<br>
`chmod 755 파일명` 으로 권한 변경

---

### 3. Docker 포트 매핑

* -p 호스트포트:컨테이너포트 형식으로 지정<br>
예: -p 8080:8080 → localhost:8080 으로 컨테이너 접근<br>
포트 매핑 없으면 외부에서 컨테이너 접근 불가

---

### 4. Docker 볼륨

* 컨테이너 삭제 시 내부 데이터도 함께 삭제됨<br>
볼륨 사용 시 컨테이너 외부에 데이터 저장 → 영속성 보장<br>
-v 볼륨명:/컨테이너경로 형식으로 마운트

---

### 5. Git vs GitHub

* Git은 코드 변경사항을 추적하는 **도구**이고,<br>
GitHub는 그 코드를 저장하고 공유하는 **온라인 공간**이다.

* Git(도구) + GitHub(저장 공간) 함께 사용

---

## 🎁 보너스 과제

### 1. Docker Compose 기초
- `docker run ...` 명령어는 옵션이 길어지면 복잡하고, 매번 기억하기 어려움
- Docker Compose는 이 실행 설정을 [`compose.yml`](compose.yml)이라는 파일에 "문서화"해서 관리함
- 누가, 언제 실행하든 항상 동일한 환경을 만들 수 있음

#### ⭐ 배움 포인트: "문서화된 실행 설정"
  ```zsh
  # [Before] CLI 기반 실행 (일회성, 재사용 어려움)
  docker run --name my-nginx -p 8080:80 -d nginx:latest


  # [After] 선언적 설정 기반 실행 (재사용 가능, 협업 용이)
  docker compose up -d
  ```

---

### 2. Docker Compose 멀티 컨테이너
- `alpine` 리눅스 컨테이너를 보조 서비스로 두고, 웹 서버 컨테이너를 `ping`으로 호출해서 네트워크 통신 확인하기
- [`compose.yml`](compose.yml) 수정
- 실행 결과
  ```zsh
  # 실행
  docker compose up

  # 결과
  helper-1  | PING web (192.168.97.3): 56 data bytes
  helper-1  | 64 bytes from 192.168.97.3: seq=0 ttl=64 time=0.047 ms
  ...
  helper-1  | 64 bytes from 192.168.97.3: seq=1 ttl=64 time=0.082 ms
  helper-1  | 64 bytes from 192.168.97.3: seq=2 ttl=64 time=0.071 ms
  helper-1  | 64 bytes from 192.168.97.3: seq=3 ttl=64 time=0.087 ms
  helper-1  | 
  helper-1  | --- web ping statistics ---
  helper-1  | 4 packets transmitted, 4 packets received, 0% packet loss
  helper-1  | round-trip min/avg/max = 0.047/0.071/0.087 ms
  helper-1 exited with code 0

  ```
#### ⭐ 배움 포인트: 네트워크 & 서비스 디스커버리
- 서비스 디스커버리 → 서비스의 위치(IP, 포트)를 동적으로 찾아주는 메커니즘
- Docker Compose는 모든 서비스를 하나의 가상 네트워크로 자동 연결한다.
- 컨테이너 간 통신 시 IP 대신 서비스 이름을 사용할 수 있다.
- 내부적으로 Docker DNS가 서비스 이름 → 컨테이너 IP를 자동 매핑한다.
- 환경이 바뀌어도(IP 변경 등) 코드 수정 없이 통신 가능하다.
- 이는 MSA 환경에서 사용하는 서비스 디스커버리의 기본 개념이다.

### 3. Compose 운영 명령어 습득

---

### 4. 환경 변수 활용

---

### 5. GitHub SSH 키 설정

