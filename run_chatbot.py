from chatbot.chatbot import ChatBot

def main():
    bot = ChatBot()
    conversation = []
    sentiments = []

    print("Chatbot Started! Type 'exit' to finish.\n")

    while True:
        user_msg = input("You: ")
        if user_msg.lower() == "exit":
            break

        # Sentiment for user message
        user_sentiment = bot.analyzer.analyze(user_msg)
        conversation.append(f'User: "{user_msg}"')
        conversation.append(f"→ Sentiment: {user_sentiment}")
        sentiments.append(user_sentiment)

        # Chatbot response
        bot_reply, bot_sent = bot.reply(user_msg)
        conversation.append(f'Chatbot: "{bot_reply}"')

        print(f"\nChatbot: {bot_reply}")
        print(f"→ Sentiment: {bot_sent}\n")

    # ------ FINAL OUTPUT ------
    print("\nFinal Output:\n")

    for line in conversation:
        print(line)

    # final conversation sentiment:
    score = sentiments.count("Positive") - sentiments.count("Negative")

    if score > 0:
        overall = "Positive – overall satisfaction"
    elif score < 0:
        overall = "Negative – general dissatisfaction"
    else:
        overall = "Neutral – mixed experience"

    print(f"\nOverall conversation sentiment: {overall}")

if __name__ == "__main__":
    main()
