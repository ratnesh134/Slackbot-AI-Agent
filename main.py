from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llm import chat
from dotenv import load_dotenv
import os

load_dotenv()
app_token = os.getenv("APP_TOKEN")
bot_token = os.getenv("BOT_TOKEN")
groq_key = os.getenv("GROQ_API_KEY")


app = App(token=bot_token)

@app.event("app_mention")
def handle_mentions(event, client, say):
    client.reactions_add(
        channel=event["channel"],
        timestamp=event["ts"],
        name="eyes"
    )

    response = chat(event["text"])

    client.chat_postMessage(
        channel=event["channel"],
        timestamp=event["ts"],
        thread_ts=event["ts"],
        text=response
    )
    client.reactions_remove(
        channel=event["channel"],
        timestamp=event["ts"],
        name="eyes"
    )

    

handler = SocketModeHandler(app,app_token)
handler.start()