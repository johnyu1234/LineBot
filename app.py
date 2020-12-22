import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message ,push_message ,send_image_carousel,send_button_message,send_button_carousel,send_image_url,send_button_budget

load_dotenv()


machine = TocMachine(
    states=["user","start","budget","fsm","range","laptop","high_game","mid_game","program","search_laptop","gpu","cpu","cpu_info","laptop_search"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "cpu",
            "conditions": "is_going_top_cpu_laptop", 
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "budget",
            "conditions": "is_going_budget", 
        },
        {
            "trigger": "advance",
            "source": "budget",
            "dest": "range",
            "conditions": "is_going_range", 
        },
        {
            "trigger": "advance",
            "source": "range",
            "dest": "laptop",
            "conditions": "is_going_to_find_laptop", #have to go another state 
        },
         {
            "trigger": "advance",
            "source": "start",
            "dest": "gpu",
            "conditions": "is_going_top_gpu_laptop", 
        },
         {
            "trigger": "advance",
            "source": "start",
            "dest": "high_game",
            "conditions": "is_going_to_high_game", 
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "program",
            "conditions": "is_going_to_program", 
        },
         {
            "trigger": "advance",
            "source": "start",
            "dest": "mid_game",
            "conditions": "is_going_to_mid_game", 
        },

         {
            "trigger": "advance",
            "source": ["mid_game","high_game","program"],
            "dest": "search_laptop",
            "conditions": "is_going_to_search_laptop",# for the gaming laptops
        },
     
         {
            "trigger": "advance",
            "source": "cpu",
            "dest": "cpu_info",
            "conditions": "is_going_cpu_info",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "laptop",
            "conditions": "is_going_to_find_laptop",
        },
         {
            "trigger": "advance",
            "source": "laptop",
            "dest": "laptop_search",
            "conditions": "is_going_to_laptop_search",
        },
         {
            "trigger": "advance",
            "source": ["laptop_search","cpu_info","gpu","search_laptop"],
            "dest": "start",
            "conditions": "is_going_back",
        },
         {
            "trigger": "advance",
            "source": "start",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {"trigger": "go_laptop",
         "source": ["laptop_search"],
          "dest": "laptop"},
         
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
#print(channel_access_token)
print(channel_secret)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")


    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
