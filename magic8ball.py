import random

def magic_8_ball():
    responses = [
        "Yes, definitely!", "No way!", "Maybe...", "Ask again later.",
        "Absolutely!", "I don't think so.", "Signs point to yes!",
        "Very doubtful.", "It is certain!", "Better not tell you now."
    ]

    print("🎱 Welcome to the Magic 8-Ball Game! 🎱")
    print("Ask a yes-or-no question, and I'll reveal your fate!")

    while True:
        question = input("\nAsk a question (or type 'quit' to exit): ")

        if question.lower() == 'quit':
            print("Goodbye! Come back when you need more wisdom. 😊")
            break
        elif question.strip() == "":
            print("Please ask a question!")
        else:
            print("Thinking... 🤔")
            response = random.choice(responses)
            print(f"🎱 Magic 8-Ball says: {response}")

magic_8_ball()

