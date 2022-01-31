from http.server import BaseHTTPRequestHandler, HTTPServer
import unicodedata
import unidecode

class Index(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World!</h1><button>Click</button>")


app = HTTPServer(("", 8000), Index)
app.serve_forever()

