import cek

def main(args):
    print(args)
    clova = cek.Clova(
        application_id="net.clova.cafe",
        default_language="ja",
        debug_mode=True)

    try:
        if args["request"]["type"] == "LaunchRequest":
            open_message = "いらっしゃいませ。ご注文をどうぞ。"
            welcome_message = cek.Message(message=open_message, language="ja")
            response = clova.response([welcome_message])
            return response
        elif args["request"]["type"] == "SessionEndedRequest" :
            thanks_text = "ありがとうございました。またのご利用をお待ちしております。"
            bye_message = cek.Message(message=thanks_text, language="ja")
            response = clova.response([bye_message])
            return response
        elif args["request"]["type"] == "IntentRequest":
            if "Drink" in args["request"]["intent"]["slots"] and "number" in args["request"]["intent"]["slots"]:
                value = args["request"]["intent"]["slots"]["number"]["value"]
                menu = args["request"]["intent"]["slots"]["Drink"]["value"]
                rep_message = "{}を{}つですね。他にご注文はありますか？".format(menu, value)
            elif "Food" in args["request"]["intent"]["slots"] and "number" in args["request"]["intent"]["slots"]:
                value = args["request"]["intent"]["slots"]["number"]["value"]
                menu = args["request"]["intent"]["slots"]["Food"]["value"]
                rep_message = "{}を{}つですね。他にご注文はありますか？".format(menu, value)
            elif args["request"]["intent"]["name"] == "Clova.NoIntent":
                rep_message = "ありがとうございました。またのご利用をお待ちしております。"
            else:
                rep_message = "かしこまりました。他にご注文はありますか？"
            reply_speak = cek.Message(message=rep_message, language="ja")
            response = clova.response([reply_speak])
            return response
    except Exception as e:
        print(e)
        return {"status":500}
