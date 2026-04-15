from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = 8080

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as f:
            self.wfile.write(f.read())

print(f"서버 시작: http://localhost:{PORT}")
httpd = HTTPServer(('', PORT), Handler)
httpd.serve_forever()
