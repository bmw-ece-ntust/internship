from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def handle_http_method(self):
        # Read the request body if any
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length:
            request_body = self.rfile.read(content_length)
        else:
            request_body = b''

        # Print request details
        print(f"Received {self.command} request at {self.path}")
        print("Headers:")
        for header, value in self.headers.items():
            print(f"{header}: {value}")
        print("Body:")
        print(request_body.decode('utf-8'))

        # Send a response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = f'{self.command} request received'.encode('utf-8')
        self.wfile.write(response_message)

    def do_GET(self):
        self.handle_http_method()

    def do_POST(self):
        self.handle_http_method()

    def do_PUT(self):
        self.handle_http_method()

    def do_DELETE(self):
        self.handle_http_method()

    def do_HEAD(self):
        self.handle_http_method()

    def do_OPTIONS(self):
        self.handle_http_method()

    def do_PATCH(self):
        self.handle_http_method()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8081):
    server_address = ('0.0.0.0', port)  # Bind to all network interfaces
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
