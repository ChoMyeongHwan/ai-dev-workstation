from http.server import HTTPServer, SimpleHTTPRequestHandler
# → 파이썬 내장 HTTP 서버 모듈
# → HTTPServer     : 서버 소켓 생성 및 요청 수신 담당
# → SimpleHTTPRequestHandler : HTTP 요청 처리 기본 클래스

import os
# → 운영체제 기능 사용 모듈
# → os.getenv() 로 환경 변수를 읽기 위해 import

# ❌ 기존: PORT = 8080  (하드코딩)
# ✅ 변경: 환경 변수에서 PORT 값을 읽어옴, 없으면 기본값 8080 사용
PORT = int(os.getenv('PORT', 8080))
# → os.getenv('PORT', 8080) : 환경 변수 PORT를 읽음, 없으면 8080 반환
# → int(...) : 환경 변수는 항상 문자열로 전달되므로 정수로 변환
# → docker-compose.yml의 environment 섹션에서 값을 주입받음

class Handler(SimpleHTTPRequestHandler):
# → SimpleHTTPRequestHandler를 상속받아 커스텀 핸들러 정의
# → 상속 덕분에 HTTP 기본 동작은 그대로 유지하면서 do_GET만 재정의

    def do_GET(self):
    # → GET 요청이 들어올 때 자동으로 호출되는 메서드
    # → 브라우저 주소창에 URL 입력 = GET 요청

        self.send_response(200)
        # → HTTP 상태 코드 200 (OK) 응답
        # → 200 : 성공 / 404 : 없음 / 500 : 서버 에러

        self.send_header('Content-type', 'text/html')
        # → 응답 헤더 설정
        # → "내가 보내는 내용은 HTML이야" 라고 브라우저에게 알려줌

        self.end_headers()
        # → 헤더 전송 완료 선언
        # → 이 이후부터 실제 본문(body) 데이터 전송

        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())
        # → index.html 파일을 바이너리(rb) 모드로 열어서 읽음
        # → wfile : 클라이언트(브라우저)로 데이터를 보내는 출력 스트림
        # → with 문 : 파일을 자동으로 닫아줌 (메모리 누수 방지)

print(f"서버 시작: http://localhost:{PORT}")
# → 서버 실행 시 콘솔에 접속 주소 출력
# → docker compose up 실행 시 로그에서 확인 가능

httpd = HTTPServer(('', PORT), Handler)
# → HTTPServer 인스턴스 생성
# → '' : 모든 네트워크 인터페이스에서 요청 수신 (0.0.0.0 과 동일)
# → PORT : 위에서 설정한 포트 번호
# → Handler : 요청을 처리할 핸들러 클래스 지정

httpd.serve_forever()
# → 서버를 계속 실행 상태로 유지
# → Ctrl+C 또는 컨테이너 종료 전까지 무한 대기
# → 요청이 들어올 때마다 Handler.do_GET() 호출