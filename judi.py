import requests
import json
import time

# Headers for the requests
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization' : 'query',
    'cache-control': 'no-cache',
    'content-type': 'application/octet-stream',
    'origin': 'https://game.chickcoop.io',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://game.chickcoop.io/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

import random
# ... existing code ...

while True:
    # Bet request
    bet_data = {
        "type": "Clucky Mystery",
        "bet": 300
    }
    bet_response = requests.post('https://api.chickcoop.io/minigame/bet', headers=headers, data=json.dumps(bet_data))
    bet_result = bet_response.json()
    # print(bet_result)
    # Print initial gem count
    # print(f"judi ready | gem : {bet_result['data']['gem']} ")

    # Predict request
    predict_data = {
        "type": "Clucky Mystery",
        # "predict": random.choice(["egg.1", "egg.2"])
        "predict" : "egg.1"
    }
    predict_response = requests.post('https://api.chickcoop.io/minigame/predict', headers=headers, data=json.dumps(predict_data))
    predict_result = predict_response.json()
   
    # Process prediction result
    reward = predict_result['data']['result']['reward']
    if reward['gem'] > 0:
        accumulated_wons = predict_result['data']['state']['miniGame']['daily']['accumulatedWons'].get("Clucky Mystery", 0)
        accumulated_losts = predict_result['data']['state']['miniGame']['daily']['accumulatedLosts'].get("Clucky Mystery", 0)
        winrate = (accumulated_wons / (accumulated_wons + accumulated_losts)) * 100 if (accumulated_wons + accumulated_losts) > 0 else 0
        print(f"you won : {reward['gem']} gem | winrate : {winrate:.2f}% | sisa gems {predict_result['data']['state']['gem']}")
    else:
        print(f"you lost | sisa gems {predict_result['data']['state']['gem']}")

    # Optional: Add a delay to avoid spamming the server
    time.sleep(1)