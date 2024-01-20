# bibliotecas:
    # Flask – pip install flask
    # Socketio – pip install python-socketio / pip install flask-socketio
    # Simple Websocket – pip install simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__) # cria o site
app.config["SECRET"] = "123456789" # chave de seguranca
app.config["DEBUG"] = False
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") # define que a função abaixo vai ser acionada quando o evento de "message" acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem para todo mundo conectado no site

@app.route("/") # cria a página do site
def home():
    return render_template("index.html") # essa página vai carregar esse arquivo html que está aqui

if __name__ == "__main__":
    socketio.run(app, host='localhost')
