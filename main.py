import os
import json

from googleapiclient.discovery import build

class Youtube:

    def __init__(self, channel_id):
        self.channel_id = channel_id

        api_key: str = os.environ.get('API_KEY')
        youtube = build('youtube', 'v3', developerKey = api_key)
        self.channel = youtube.channels().list(id = channel_id, part = 'snippet,statistics').execute()
