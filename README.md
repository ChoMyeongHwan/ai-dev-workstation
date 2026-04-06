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

## ✅ 수행 항목 체크리스트

* [x] 터미널 조작 로그 기록
* [ ] STEP 4: 파일 권한 실습
* [ ] STEP 5: Docker 설치 및 점검
* [ ] STEP 6: 컨테이너 기본 실행
* [ ] STEP 7: 커스텀 이미지 제작
* [ ] STEP 8: 포트 매핑 테스트
* [ ] STEP 9: 볼륨 영속성 검증
* [ ] STEP 10: Git 설정 및 GitHub 연동

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

* 터미널 조작 로그 기록 완료 → [terminal-logs.md](logs/terminal-logs.md)<br>
mkdir -p 로 디렉토리 구조 생성<br>
절대경로 / 상대경로 실습 완료

* STEP 4: (작성 예정)
* STEP 5: (작성 예정)
* STEP 6: (작성 예정)
* STEP 7: (작성 예정)
* STEP 8: (작성 예정)
* STEP 9: (작성 예정)
* STEP 10: (작성 예정)

---

## 🐛 트러블슈팅

> 문제 발생 시 아래 형식으로 기록합니다.

### 예시

* 문제:
* 원인 가설:
* 확인 방법:
* 해결 방법:

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

* (STEP 4 완료 후 작성)

---

### 3. Docker 포트 매핑

* (STEP 8 완료 후 작성)

---

### 4. Docker 볼륨

* (STEP 9 완료 후 작성)

---

### 5. Git vs GitHub

* (STEP 10 완료 후 작성)
