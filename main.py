import http.server
import socketserver
from pynput.keyboard import Key, Controller

keyboard = Controller()
key = "a"

#here you create a new handler, you had a new way to handle get request
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body><form><input type='hidden' name='Teste' value='true' text='Teste'><input type='submit'></form></body>", "utf-8"))
       #this code execute when a GET request happen, then you have to check if the request happenned because the user pressed the button
        if self.path.find("Teste=true") != -1:
            print("Button clicked")
            keyboard.press(key)
            keyboard.release(key)
            #do whatever you want
        return super().do_GET()


PORT = 8080
myHandler = Handler


with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    