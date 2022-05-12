import socket                

# Socket oluşturulması
s = socket.socket()          

# Bağlanılacak adres ve port
host = "localhost"
port = 12345                

try:
    # Bağlantıyı yap
    s.connect((host, port)) 

    # serverden yanıtı al
    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))

    # bağlantıyı kapat
    s.close() 
except socket.error as msg:
    print("[Server aktif değil.] Mesaj:", msg)