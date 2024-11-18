from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__,)

socketio = SocketIO(app)

# Route to serve the front end
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint for sending a custom message from the backend
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message", "No message provided")
    # Emit the message event to the front end
    socketio.emit("display_message", {"message": message})
    return {"status": "success", "message": message}, 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
