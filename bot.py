import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], 
    '/slack/events', 
    app
)

client = WebClient(token=os.environ['SLACK_TOKEN'])

if __name__ == "__main__":
    app.run(debug=True)