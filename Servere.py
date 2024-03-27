# Importăm modulul http.server
import http.server
import socketserver

# Definim o clasă care va gestiona cererile HTTP
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Suprascriem metoda do_GET pentru a gestiona cererile GET
    def do_GET(self):
        # Răspundem cu un mesaj și un cod de stare 200 OK
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Salut! Acesta este serverul meu HTTP.")

# Specificăm adresa IP și portul pe care va asculta serverul
host = 'localhost'
port = 8000

# Creăm o instanță a serverului, folosind clasa noastră de gestionare a cererilor
with socketserver.TCPServer((host, port), MyHttpRequestHandler) as server:
    print(f"Serverul rulează la adresa {host} și portul {port}.")
    # Serverul va rula în mod continuu, ascultând cereri și răspunzând la acestea
    server.serve_forever()
