from flask import Flask, render_template, request
import datetime
import json

app = Flask(__name__)

DB_FILE = "./data/db.json"
db = open(DB_FILE, "rb")
data = json.load(db)
messages = data["messages"]

def save_messages_to_file():
    db = open(DB_FILE, "w")
    data = {
        "messages": messages
    }
    json.dump(data, db)

def add_message(text, sender):
    now = datetime.datetime.now()
    new_message = {
        "text": text,
        "sender": sender,
        "time": now.strftime("%H: %M")
    }
    while True:
        if len(sender) < 3 or len(sender) > 100:
            print("ERROR")
            return "ERROR"
        else:
            break
    while True:
        if len(text) < 1 or len(text) > 3000:
            print("ERROR")
            return "ERROR"
        else:
            break
    messages.append(new_message)
    save_messages_to_file()

def print_message(message):
    print(f"[{message['sender']}]: {message['text']} / {message['time']} ")

@app.route("/")
def index_page():
    return "Greetings, you are welcomed in SkillChat "

@app.route("/get_messages")
def get_messages():
    return {"messages": messages}

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send_message")
def send_message():
    sender = request.args["sender"]
    text = request.args["text"]
    add_message(text, sender)
    return "OK"

app.run()
