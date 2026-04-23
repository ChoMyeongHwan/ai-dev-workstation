# Volume Test

## 볼륨 개념

### 컨테이너는 삭제되면 내부 데이터도 사라짐
→ 볼륨(Volume)을 사용하면 컨테이너 외부에 데이터 저장<br>
→ 컨테이너가 삭제되어도 데이터 유지!

---

## 실습 흐름

```
1. docker volume create ai-data       # 볼륨 생성
2. 컨테이너 실행 + 볼륨 마운트              # -v ai-data:/data
3. /data/test.txt 파일 생성             # 컨테이너 내부
4. 컨테이너 삭제                         # docker rm vol-test
5. 새 컨테이너에서 같은 볼륨 마운트          # 데이터 유지 확인!
```

```zsh
# 실습 명령어
# bind mount
mkdir -p ~/docker-practice/bind/html
echo "<h1>hello bind</h1>" > ~/docker-practice/bind/html/index.html

docker run -d \
  --name bind-test \
  -p 8080:80 \
  --mount type=bind,source=$HOME/docker-practice/bind/html,target=/usr/share/nginx/html \
  nginx



# volume
docker volume create my_volume

docker run -d \
  --name volume-test \
  -p 8081:80 \
  --mount type=volume,source=my_volume,target=/usr/share/nginx/html \
  nginx

docker exec -it volume-test sh
echo "<h1>hello volume</h1>" > /usr/share/nginx/html/index.html
exit


# tmpfs
docker run -d \
  --name tmpfs-test \
  -p 8082:80 \
  --mount type=tmpfs,target=/usr/share/nginx/html \
  nginx

docker exec -it tmpfs-test sh
echo "<h1>hello tmpfs</h1>" > /usr/share/nginx/html/index.html
exit

```

---

## 마운트 종류

| 구분           | 바인드 마운트 (Bind Mount) | 네임드 볼륨 (Named Volume) | tmpfs 마운트 (tmpfs Mount) |
|----------------|-----------------------------|-----------------------------|-----------------------------|
| 저장 위치      | 호스트 경로 직접 지정        | Docker가 경로 관리          | 메모리 (RAM)                |
| 데이터 지속성  | 유지됨                      | 유지됨                      | 컨테이너 종료 시 삭제        |
| 관리 주체      | 사용자                      | Docker                      | Docker                      |
| 주요 용도      | 개발 시 코드 공유            | DB, 로그 등 영구 데이터     | 민감한 임시 데이터          |
| 성능           | 보통                        | 보통                        | 매우 빠름 (메모리 기반)     |

---

## 핵심 정리
### bind mount
- 호스트 경로를 직접 컨테이너에 연결
- 개발 중 소스코드/설정파일 연결에 적합
- 수정 즉시 반영 가능
- 호스트 의존성이 큼

### volume
- Docker가 관리하는 저장소
- 영속 데이터 저장에 적합
- 컨테이너 재생성 후에도 데이터 유지
- DB, 업로드 파일에 적합

### tmpfs mount
- 메모리 기반 저장소
- 컨테이너 종료 시 데이터 소멸
- 임시/민감 데이터 처리에 적합
- 영속 데이터에는 부적합

---

## 검증 결과
- vol-test 컨테이너 삭제 후
- vol-test2 에서 /data/test.txt 내용 그대로 확인
- → 볼륨 영속성 검증 완료 ✅

---

## 스크린샷
![볼륨 생성](../logs/screenshots/volume-create.png)
![데이터 유지](../logs/screenshots/volume-persist.png)
