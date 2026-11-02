# Aria - Rule-Based Chatbot (Python)

A simple console chatbot named **Aria**, written in Python. It uses rule-based keyword matching (no AI model or internet connection needed) to respond to greetings, small talk, questions about the time and date, jokes, and more.

## Features

- Asks for your name and uses it in replies
- Understands greetings, "how are you", thanks, and goodbyes
- Tells the current time and date
- Tells random programming jokes
- Built-in `help` command
- Whole-word matching, so `hi` does not trigger inside words like `this`
- Ignores capitalization, punctuation, and extra spaces
- Handles empty input and `Ctrl+C` / `Ctrl+D` gracefully
- No external dependencies (standard library only)

## Requirements

- **Python 3.9 or newer** (the code uses the `list[str]` type hint)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Run the chatbot:

   ```bash
   python CHATBOT.py
   ```

   Use `python3` on some systems.

## What You Can Say

| Category | Example phrases |
|----------|-----------------|
| Greetings | `hello`, `hi`, `hey`, `good morning`, `good afternoon`, `good evening` |
| How are you | `how are you`, `how are you doing`, `whats up` |
| Name | `what is your name`, `who are you` |
| Time | `what time is it`, `time` |
| Date | `what day is it`, `date`, `today` |
| Jokes | `tell me a joke`, `make me laugh`, `funny` |
| Thanks | `thanks`, `thank you`, `thx` |
| Help | `help`, `what can you do` |
| Goodbye | `bye`, `goodbye`, `see you`, `exit`, `quit`, `good night` |

Anything the bot does not recognize gets a polite fallback message suggesting `help`.

### Example Conversation

```
====================================================
            CHATBOT  -  Aria
      (type 'bye' to end the conversation)
====================================================
Aria: Hi! What's your name?
You: sam
Aria: Nice to meet you, Sam! Type 'help' to see what I can do.
You: Hello!
Aria: Hi, Sam!
You: what time is it?
Aria: The time is 03:45 PM.
You: tell me a joke
Aria: Why do programmers prefer dark mode? Because light attracts bugs!
You: thanks
Aria: You're welcome!
You: bye
Aria: Goodbye, Sam! Have a great day!
```

## How It Works

1. `clean_text()` lowercases the input and strips punctuation and extra spaces.
2. `contains_phrase()` checks whether any known phrase appears in the message as whole words.
3. `get_response()` checks the message against each category in order and returns the first matching reply. Goodbyes are checked first, and the fallback reply is used if nothing matches.
4. The loop in `main()` keeps running until a goodbye is detected.

| Function | Purpose |
|----------|---------|
| `clean_text()` | Normalizes user input |
| `contains_phrase()` | Whole-word phrase matching |
| `get_response()` | Chooses the reply |
| `is_goodbye()` | Detects when to end the chat |
| `ask_user_name()` | Gets the user's name (defaults to "friend") |
| `main()` | Program entry point and conversation loop |

## Customizing

All keywords and replies are at the top of `CHATBOT.py`:

```python
BOT_NAME = "Aria"
JOKES = ["...", "..."]       # add your own jokes
GREETINGS = ["hello", "hi"]  # add more trigger phrases
```

To add a new topic, create a phrase list, then add an `elif contains_phrase(...)` branch in `get_response()`.

## Limitations

- It matches fixed keywords, so it does not truly understand language or remember earlier messages.
- The first matching category wins, so a message with several topics gets only one reply.

## Ideas for Improvement

- Remember context from earlier in the conversation
- Add weather, math, or a to-do list feature
- Load responses from a JSON file
- Use regular expressions or an NLP library for smarter matching
- Add unit tests for `clean_text()` and `get_response()`

## Contributing

Suggestions and pull requests are welcome.
