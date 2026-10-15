from chatbot import PythonChatbot

bot = PythonChatbot()

print("Python chatbot ready! Type 'quit' to stop.\n")
while True:
    question = input("You: ")
    if question.lower() in ("quit", "exit"):
        break
    reply = bot.ask(question)
    print(f"\nBot ({reply['type']}, confidence {reply['confidence']:.2f}):")
    if reply["matched_question"]:
        print("Matched:", reply["matched_question"])
    print(reply["answer"])
    if reply["suggestions"]:
        print("\nRelated:", " | ".join(reply["suggestions"]))
    print("-" * 50)