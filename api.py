from flask import Flask, request
from rubika import Client

app = Flask(__name__)

# توکن و آیدی گروه
TOKEN = "BDGIF0KHLNFLBKILZBRFBMKWDGLQEIIQYANZXYJEVEGRBQUTYMSMXKSGPMNDQLNJ"
GROUP_GUID = "g0IEHGFJAH0BOATUWWFZYXGCBBCWUNBXPZ"

bot = Client(TOKEN)

@app.route("/", methods=["POST", "GET"])
def main():
    try:
        updates = bot.get_messages(GROUP_GUID)
        if "messages" in updates:
            for msg in updates["messages"]:
                msg_id = msg["message_id"]
                text = msg.get("text", "")
                user_guid = msg["author_object_guid"]

                if "http" in text or "rubika.ir/" in text:
                    bot.delete_messages(GROUP_GUID, [msg_id])
                    bot.send_message(GROUP_GUID, "❌ ارسال لینک ممنوع است", msg_id)

                elif text == "/start":
                    bot.send_message(GROUP_GUID, "✅ ربات مدیریت فعال است", msg_id)

                elif text == "/help":
                    bot.send_message(GROUP_GUID, "📌 دستورات:
/start
/help
/rules", msg_id)

                elif text == "/rules":
                    bot.send_message(GROUP_GUID, "📜 قوانین:
1. بدون توهین
2. بدون لینک
3. احترام", msg_id)

                elif "سلام" in text:
                    bot.send_message(GROUP_GUID, "سلام دوست عزیز! 🌹", msg_id)

        return "OK"
    except Exception as e:
        print("خطا:", e)
        return str(e)