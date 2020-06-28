from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        tuple = self.client_address
        self.wfile.write(b'Hello world to: ')
        self.wfile.write(tuple[0].encode("utf-8"))
        print ("Sent response")

httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
