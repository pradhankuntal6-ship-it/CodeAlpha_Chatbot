import random
import string
from datetime import datetime

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
BOT_NAME = "Aria"

GREETINGS = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
HOW_ARE_YOU = ["how are you", "how are you doing", "how do you do", "whats up"]
GOODBYES = ["bye", "goodbye", "see you", "exit", "quit", "good night"]
THANKS = ["thanks", "thank you", "thx"]
NAME_QUESTIONS = ["your name", "who are you"]
HELP_REQUESTS = ["help", "what can you do"]
TIME_QUESTIONS = ["time", "what time is it"]
DATE_QUESTIONS = ["date", "today", "what day is it"]
JOKE_REQUESTS = ["joke", "make me laugh", "funny"]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "There are 10 kinds of people: those who know binary and those who don't.",
]

HELP_TEXT = (
    "I can chat with you! Try saying: hello, how are you, what is your name, "
    "what time is it, what is the date, tell me a joke, thanks, or bye."
)


# --------------------------------------------------------------------------- #
# Helper functions
# --------------------------------------------------------------------------- #
def clean_text(text: str) -> str:
    """Lowercase the text, remove punctuation and extra spaces.

    "  How are YOU?! " -> "how are you"
    """
    text = text.lower().replace("'", "")  # "what's" -> "whats"
    for mark in string.punctuation:
        text = text.replace(mark, " ")
    return " ".join(text.split())


def contains_phrase(message: str, phrases: list[str]) -> bool:
    """Return True if any phrase appears in the message as whole word(s).

    Matching on whole words stops "hi" from matching inside "this".
    """
    padded_message = f" {message} "
    for phrase in phrases:
        if f" {phrase} " in padded_message:
            return True
    return False


def get_response(message: str, user_name: str) -> str:
    """Return the chatbot's reply to a cleaned-up user message."""
    if message == "":
        return "Say something and I'll reply!"
    elif contains_phrase(message, GOODBYES):
        return f"Goodbye, {user_name}! Have a great day!"
    elif contains_phrase(message, HOW_ARE_YOU):
        return "I'm fine, thanks! How about you?"
    elif contains_phrase(message, GREETINGS):
        return f"Hi, {user_name}!"
    elif contains_phrase(message, NAME_QUESTIONS):
        return f"My name is {BOT_NAME}. Nice to meet you, {user_name}!"
    elif contains_phrase(message, THANKS):
        return "You're welcome!"
    elif contains_phrase(message, HELP_REQUESTS):
        return HELP_TEXT
    elif contains_phrase(message, TIME_QUESTIONS):
        return f"The time is {datetime.now():%I:%M %p}."
    elif contains_phrase(message, DATE_QUESTIONS):
        return f"Today is {datetime.now():%A, %d %B %Y}."
    elif contains_phrase(message, JOKE_REQUESTS):
        return random.choice(JOKES)
    elif contains_phrase(message, ["fine", "good", "great", "okay", "ok"]):
        return "Glad to hear that!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def is_goodbye(message: str) -> bool:
    """Return True if the user wants to end the conversation."""
    return contains_phrase(message, GOODBYES)


def ask_user_name() -> str:
    """Ask for the user's name (falls back to 'friend' if left blank)."""
    name = input(f"{BOT_NAME}: Hi! What's your name?\nYou: ").strip()
    return name.title() if name else "friend"


# --------------------------------------------------------------------------- #
# Program entry point
# --------------------------------------------------------------------------- #
def main() -> None:
    """Run the chatbot conversation loop."""
    print("=" * 52)
    print(f"            CHATBOT  -  {BOT_NAME}")
    print("      (type 'bye' to end the conversation)")
    print("=" * 52)

    try:
        user_name = ask_user_name()
        print(f"{BOT_NAME}: Nice to meet you, {user_name}! Type 'help' to see "
              "what I can do.")

        while True:
            message = clean_text(input("You: "))
            print(f"{BOT_NAME}: {get_response(message, user_name)}")

            if is_goodbye(message):
                break
    except (KeyboardInterrupt, EOFError):
        print(f"\n{BOT_NAME}: Goodbye!")


if __name__ == "__main__":
    main()