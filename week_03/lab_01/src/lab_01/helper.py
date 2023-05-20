import requests
import urllib.parse

URL_LINE = "https://notify-api.line.me/api/notify"


class LineNotify:
    def __init__(self, LINE_ACCESS_TOKEN):
        self.LINE_ACCESS_TOKEN = LINE_ACCESS_TOKEN

    def line_pic(self, message, path_file):
        file_img = {"imageFile": open(path_file, "rb")}
        msg = {"message": message}
        LINE_HEADERS = {"Authorization": "Bearer " + self.LINE_ACCESS_TOKEN}
        session = requests.Session()
        session_post = session.post(
            URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg
        )

    def line_text(self, message):
        msg = urllib.parse.urlencode({"message": message})
        LINE_HEADERS = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + self.LINE_ACCESS_TOKEN,
        }
        session = requests.Session()
        session_post = session.post(URL_LINE, headers=LINE_HEADERS, data=msg)
