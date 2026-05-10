import os
import requests
from post_generator import generate_post

PAGE_ID = os.getenv("1020689164470492")
ACCESS_TOKEN = os.getenv("EAASttWO1sVoBRUp168ONQIM7jiWetHfyCkdStomzzUhORAYvmcvPhCZA8WmSVMJre54brpMpNLgiIzgu1ZBZCDY9lSLum3OifNOwKZBL91oK0EXDuoBSnP0TEZANAX6IWhUEGfJUZCZAgw0ciZCuTPEUnEJYKoSKxjYZBY3VYOivzqzTpFrqCF6T82NhXgeJXsZAU50g4ASTLBMSSV47xXSbMRjj5D1K71aUTSIs1tEFT5iVok9XMZBLeV2ywsZD")

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
