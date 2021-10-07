from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import cgi

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

timesheet = ['Time Entries:']

class reqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/timesheet'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            #self.wfile.write(self.path[1:].encode())

            output = ''
            output += '<html><body>'
            output += '<h1>Time Sheet</h1>'
            output += '<h3><a href="/timesheet/new">Add New Time</a></h3>'
            for task in timesheet:
                output += task
                output += '</br>'

            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Add New Time</h1>'

            output += '<form method="POST" enctype="multipart/form-data" action="/timesheet/new">'
            #output += '<input name="time" type="text" placeholder="Add New Time">'
            output += '<input name="getTime" type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_time = fields.get('getTime')

                timesheet.append(current_time)

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location','/timesheet')
            self.end_headers()


def main():
    PORT = 16321
    server = HTTPServer(('localhost',PORT), reqHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
