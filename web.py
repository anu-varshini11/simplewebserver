from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>TOP 5 SOFTWARE COMPANIES REVENUE</title>
    </head>
    <body>
    <table border="4" cellspacing="5" cellpadding="5" width="40" height="50">
        <caption>REVENUE DATA</caption>
        <tr>
            <th>Name of the Company</th>
            <th>Period</th>
            <th>Revenue</th>
        </tr>
        <tr>
            <td>Cognizant Tech.</td>
            <td>2004-10</td>
            <td>39%</td>
        </tr>
        <tr>
            <td>Infosys</td>
            <td>2001-06</td>
            <td>45%</td>
        </tr>
        <tr>
            <td>L&T Infotech</td>
            <td>2004-08</td>
            <td>43%</td>
        </tr>
            <td>Mindtree</td>
            <td>2004-09</td>
            <td>29%</td>
        <tr>
        <tr>
            <td>Oracle India</td>
            <td>2007-12</td>
            <td>66%</td>
        </tr>
    </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()