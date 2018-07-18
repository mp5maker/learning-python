from http.server import HTTPServer, CGIHTTPRequestHandler

port = 7800
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_http onport: " + str(httpd.server_port))
httpd.serve_forever()