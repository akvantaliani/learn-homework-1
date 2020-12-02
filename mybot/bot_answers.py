def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


if __name__ == "__main__":
    talk_to_me()
