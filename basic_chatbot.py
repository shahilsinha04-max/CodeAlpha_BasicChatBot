"""
Basic Rule-Based Chatbot
------------------------
Key Concepts Used:
- Functions: Modular code organization (get_response, chatbot)
- Loops: Continuous conversation loop until user chooses to exit
- if-elif-else: Pattern matching rules for incoming user queries
- Input/Output: Interaction via console input() and print()
- Standard Libraries: datetime and random for dynamic replies
"""

from datetime import datetime
import random

# Predefined pool of jokes
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why do Java developers wear glasses? Because they don't C#!",
]


def get_response(user_input: str) -> tuple[str, bool]:
    """
    Determines the chatbot's reply based on predefined rules.

    Returns:
        tuple[str, bool]: A tuple containing the response message and a boolean
                          flag indicating whether to end the conversation.
    """
    cleaned_input = user_input.strip().lower()

    # Rule 1: Greetings
    if any(greet in cleaned_input for greet in ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"]):
        return "Hi! How can I help you today?", False

    # Rule 2: Inquiries about well-being
    elif "how are you" in cleaned_input or "how're you" in cleaned_input or "how are things" in cleaned_input:
        return "I'm doing great, thank you for asking! How about yourself?", False

    # Rule 3: Chatbot identity & creator
    elif "your name" in cleaned_input or "who are you" in cleaned_input:
        return "I am PyBot, a rule-based chatbot running on Python!", False

    elif "who made you" in cleaned_input or "who created you" in cleaned_input:
        return "I was built with Python using if-elif statements, functions, and loops!", False

    # Rule 4: Chatbot capabilities / Help
    elif "what can you do" in cleaned_input or "help" in cleaned_input or "features" in cleaned_input:
        return (
            "Here are some things you can ask me:\n"
            "  - 'What time is it?' or 'What is today's date?'\n"
            "  - 'Tell me a joke'\n"
            "  - 'How old are you?' or 'Where are you from?'\n"
            "  - 'What is your favorite color?'\n"
            "  - 'What is the weather like?'\n"
            "  - 'Bye' to exit"
        ), False

    # Rule 5: Time and Date queries
    elif "time" in cleaned_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}.", False

    elif "date" in cleaned_input or "what day is it" in cleaned_input:
        today_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today_date}.", False

    # Rule 6: Jokes & Entertainment
    elif "joke" in cleaned_input or "make me laugh" in cleaned_input:
        return random.choice(JOKES), False

    # Rule 7: Age & Location
    elif "how old are you" in cleaned_input or "your age" in cleaned_input:
        return "I don't have a biological age, but I was created recently in Python!", False

    elif "where do you live" in cleaned_input or "where are you from" in cleaned_input:
        return "I live right here inside your computer's memory!", False

    # Rule 8: Favorites
    elif "favorite color" in cleaned_input:
        return "My favorite color is electric blue! It reminds me of glowing circuits.", False

    elif "favorite food" in cleaned_input:
        return "I consume bytes and data, but I hear pizza is very popular among humans!", False

    # Rule 9: Weather
    elif "weather" in cleaned_input:
        return "I can't check live satellite weather yet, but I hope it's pleasant where you are!", False

    # Rule 10: Gratitude & Politeness
    elif "thank you" in cleaned_input or "thanks" in cleaned_input:
        return "You're very welcome! Let me know if you need anything else.", False

    # Rule 11: Farewells / Exit
    elif any(farewell in cleaned_input for farewell in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "Goodbye! Have a wonderful day!", True

    # Rule 12: Catch-all / Fallback response
    else:
        return (
            "I'm not sure how to answer that yet. Type 'help' to see what questions you can ask me!",
            False,
        )


def chatbot() -> None:
    """Runs the main interactive chatbot loop."""
    print("=" * 60)
    print("Welcome to PyBot (Rule-Based Chatbot)!")
    print("Type 'help' to see questions you can ask, or 'bye' to exit.")
    print("=" * 60)

    while True:
        try:
            user_text = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nChatbot: Goodbye!")
            break

        # Handle empty or whitespace-only inputs
        if not user_text.strip():
            print("Chatbot: Please type something so we can chat!")
            continue

        reply, should_exit = get_response(user_text)
        print(f"Chatbot: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    chatbot()
