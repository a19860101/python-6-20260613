import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import requests
import bs4


#########################################
# 讀取.env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

############################################
# 處理 /start 指令
async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "你好，我是 RSS激起人！\n"
        "你可以傳送任何文字給我。"
    )
#################
async def greeting_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "我是RSS激起人"
        "就這樣!!"
        "BYE"
    )

######################################################
# 處理一般文字訊息
async def echo_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    # 取得使用者輸入的文字
    user_text = update.message.text

    print("使用者輸入：", user_text)

    # 將相同的文字回覆給使用者
    await update.message.reply_text(
        f"你說了：{user_text}"
    )

##############################################
# 主程式
def main():
    if not TELEGRAM_BOT_TOKEN:
        print("找不到TOKEN")
        print("請檢查.env")
        return

    # 建立Telegram Bot應用程式
    application = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    # 加入 /start指令處理器
    application.add_handler(
        CommandHandler("start", start_command)
    )
    # 加入 /greeting
    application.add_handler(
        CommandHandler("greeting", greeting_command)
    )

    # 加入一般文字訊息處理器
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            echo_message
        )
    )

    print("Telegram Bot 已啟動")
    print("按下 Ctrl + C 可以停止程式")

    # 持續接收 Telegram 訊息
    application.run_polling()


if __name__ == "__main__":
    main()