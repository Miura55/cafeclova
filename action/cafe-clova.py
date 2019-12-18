import cek
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import requests

def main(args):
    print(args)
    clova = cek.Clova(
        application_id="net.clova.cafe",
        default_language="ja",
        debug_mode=True)
    userId = args["session"]["user"]["userId"]

    try:
        if args["request"]["type"] == "LaunchRequest":
            open_message = "いらっしゃいませ。ご注文をどうぞ。"
            welcome_message = cek.Message(message=open_message, language="ja")
            response = clova.response([welcome_message])
            return response
        elif args["request"]["type"] == "SessionEndedRequest" :
            # 注文の確認
            confirm_order = requests.get(args["URL"]+"/confilm?userId={}".format(userId))
            # メッセージを送信
            line_bot_api = LineBotApi(args["ACCESS_TOKEN"])
            try:
                line_bot_api.push_message(userId, TextSendMessage(text='Hello World!'))
                thanks_text = "ありがとうございました。またのご利用をお待ちしております。"
            except LineBotApiError as e:
                thanks_text = "注文を完了させるには、LINEで友だち追加してくださいね。"
            
            bye_message = cek.Message(message=thanks_text, language="ja")
            response = clova.response([bye_message])
            return response
        # intentのリクエストが来たときの判定
        elif args["request"]["type"] == "IntentRequest":
            if args["request"]["intent"]["name"] == "Clova.NoIntent":
                rep_message = "ありがとうございました。またのご利用をお待ちしております。"
                reply_speak = cek.Message(message=rep_message, language="ja")
                response = clova.response([reply_speak], end_session=True)
                return response
            # カスタムインテントの判定
            elif "Drink" in args["request"]["intent"]["slots"] and "number" in args["request"]["intent"]["slots"]:
                value = args["request"]["intent"]["slots"]["number"]["value"]
                menu = args["request"]["intent"]["slots"]["Drink"]["value"]
                # データ入力するAPIに登録
                call_db(args, menu, value)
                rep_message = "{}を{}つですね。他にご注文はありますか？".format(menu, value)
            elif "Food" in args["request"]["intent"]["slots"] and "number" in args["request"]["intent"]["slots"]:
                value = args["request"]["intent"]["slots"]["number"]["value"]
                menu = args["request"]["intent"]["slots"]["Food"]["value"]
                # データ入力するAPIに登録
                call_db(args, menu, value)
                rep_message = "{}を{}つですね。他にご注文はありますか？".format(menu, value)
            else:
                rep_message = "かしこまりました。他にご注文はありますか？"
    except Exception as e:
        print(e)
        return {"status":500}
    else:
        reply_speak = cek.Message(message=rep_message, language="ja")
        response = clova.response([reply_speak])
        return response

def call_db(args, menu, value):
    body = {
        "userId":args["session"]["user"]["userId"],
        "menu":menu,
        "value":value
    }

    response = requests.post(
            args["URL"] + "/order",
            json = body
        )

    return response.text
