import os
import requests
from post_generator import generate_post

PAGE_ID = os.getenv("1020689164470492")
ACCESS_TOKEN = os.getenv("EAAVgnsVw2koBRVad0KwAGl0xChyUTqPvouneU3btstnaoXpKMwCJwUxl0hls7GYJ10bKihZAuy8BTcYXYY0GJ3KSd8bsMfCtceibfUHF76r1ZBzrBHRZAYTJcj3NKDt4O9r6LwkZACkFtJtSG8L86XijZCNPVhCKqqtp4vsky2WzrZBgIo7rW0ZBGFfg2FnVo9ifMjfD3XWMb3uW67HaF6o8Dv4d4R3ajFckjuepJEGXNC9v9ctg59KX0yNQSiNSkZAiJ0EMiu59giU1sbbAfnMEuC5X")

def post_to_facebook(message):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
    
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    content = generate_post()
    result = post_to_facebook(content)
    print(result)
