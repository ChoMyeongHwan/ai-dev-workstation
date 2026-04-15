# Git Setup

## Git 전역 설정
```zsh
git config --global user.name "이름"
git config --global user.email "이메일"
```

## 주요 Git 명령어 정리

| 명령어 | 설명 |
|--------|------|
| git init | 저장소 초기화 |
| git status | 변경사항 확인 |
| git add . | 전체 스테이징 |
| git commit -m "메시지" | 커밋 |
| git push origin main | 원격 저장소에 push |
| git log --oneline | 커밋 이력 확인 |
| git remote -v | 원격 저장소 확인 |

## 실습
```zsh
# 1. Git 전역 설정 확인
git config --list

# 2. 설정 안 되어 있으면 등록
git config --global user.name "본인 이름"
git config --global user.email "본인 이메일"

# 3. 현재 브랜치 확인
git branch

# 4. 원격 저장소 확인
git remote -v

# 5. 전체 커밋 로그 확인
git log --oneline

# 6. 변경사항 확인 후 최종 push
git status
git add .
git commit -m "[메세지]"
git push origin main

```

## Git vs GitHub

| 구분 | 설명 |
|------|------|
| Git | 로컬 버전 관리 도구 (내 컴퓨터) |
| GitHub | Git 원격 저장소 호스팅 서비스 (클라우드) |

## 커밋 이력
```
edc21d2 (HEAD -> main, origin/main, origin/HEAD) update: terminal-logs.md
9f8cff6 docs: 파일 권한 실습 완료  (chmod 755/644)
6187fd2 docs: 터미널 로그 및 경로 실습 기록
609837f docs: README 기본 구조 작성
3d4fddf Initial commit
```
