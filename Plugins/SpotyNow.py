import subprocess
from yandex_music import Client
def SpotyNow():
    artist = subprocess.getoutput('playerctl metadata xesam:artist')
    title = subprocess.getoutput('playerctl metadata xesam:title')
    url = subprocess.getoutput('playerctl metadata xesam:url')
    url2 = send_search_request_and_print_result(f"{artist} {title}")
    return f"у меня сейчас играет {artist} ─ {title} \" -M Ctrl -P Return -m Ctrl -p Return \"Spotify: {url} \" -M Ctrl -P Return -m Ctrl -p Return \"Yandex.Music: {url2}"

def send_search_request_and_print_result(query):
    client = Client().init()
    search_result = client.search(query)

    if search_result.best:
        type_ = search_result.best.type
        best = search_result.best.result
        return f"https://music.yandex.ru/track/{best.id}"
    else:
        return "Сорри"
