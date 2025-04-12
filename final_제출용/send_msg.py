import requests

def send_push_notification(title, message, url):
    data = {
        "token": "pushover_api_token",
        "user": "pushover_user_key",
        "title": title,
        "message": message,
        "url": url
    }
    res = requests.post("https://api.pushover.net/1/messages.json", data=data)

    if res.status_code == 200:
        print("알림 전송 성공")
    else:
        print("전송 실패:", res.text)