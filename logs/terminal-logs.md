# Terminal Logs

```zsh
# 1. 현재 위치 확인 (절대 경로)
pwd

# 2. 프로젝트 폴더로 이동
cd ~/ai-dev-workstation

# 3. 디렉토리 구조 생성
# -p 중간 경로 자동 생성, 이미 있어도 에러 없음
mkdir -p logs/screenshots dockerfile evidence

# 4. 파일 목록 확인
ls -la

# 5. 절대경로 vs 상대경로 체험
cd logs          # 상대 경로
pwd              # 현재 위치 확인
cd ..            # 상위로 이동
cd ~/ai-dev-workstation/logs  # 절대 경로
pwd

# 6. logs에 terminal-logs.md 파일 생성
touch terminal-logs.md

# 7. 파일 내용 확인
cat app.log -> (아무 내용 없음)

# 8. 파일 복사
cp app.log app_copy.log

# 9. 이름 변경
mv app_copy.log renamed.log

# 10. 디렉토리로 이동
mv renamed.log ../ -> 상위 디렉토리로 이동

# 11. 파일 삭제
rm renamed.log

# 12. 디렉토리 삭제
# -r → 디렉토리 내부까지 삭제
rm -r logs

```

## 핵심 요약
```
pwd        → 현재 위치
ls -al     → 목록 확인(숨김 포함)
cd         → 이동
mkdir      → 생성
cp         → 복사
mv         → 이동/이름변경
rm         → 삭제
cat/less   → 내용 확인
touch      → 빈 파일 생성
```

## 주요 명령어 실행 확인
![terminal-logs.png](screenshots/terminal-logs.png)