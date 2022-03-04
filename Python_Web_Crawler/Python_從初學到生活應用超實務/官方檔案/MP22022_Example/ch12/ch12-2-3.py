from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage

channel_token  = "Ik5HdGgbEiiWxVemtKydXLV2LE0o5YKx1ttA6uHRtyw4bp2huUkxqSrsC0cbVeYYC0fAaLgDGn9IzXCQY0fwRAfjJ0Kc8/CcGqUelZBMY34xBgB9Nc/BPeIXemlcYbGyGUD/1UW3rVxBJ745lSjyxgdB04t89/1O/w1cDnyilFU="
channel_secret = "d11e898d85ec89c00179ba6e4dc965d5"

app = Flask(__name__)
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(port=8080)