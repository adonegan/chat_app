import os
from flask import Flask

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a messge use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    """Display chat message"""
    return "Welcome {0}".format(username)


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    return "{0}: {1}".format(username, message)   


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '127.0.0.1'), port=os.getenv('PORT', '5000'), debug=False)