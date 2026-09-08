# CodeAlpha - Basic Rule-Based Chatbot (PyBot)

A lightweight, interactive, rule-based **Chatbot** built in Python. **PyBot** utilizes predefined patterns, conditional logic, and Python's standard library to hold natural console-based conversations, answer common questions, tell jokes, and report the real-time date and time.

---

## 📝 Project Description

The **Basic Rule-Based Chatbot (`PyBot`)** is a console-based conversational agent developed in Python as part of the CodeAlpha Python Development Internship. It serves as a practical introduction to conversational AI principles, demonstrating how automated communication systems can be built without relying on heavy external machine learning libraries.

At its core, the chatbot functions through an **if-elif-else rule engine** paired with **keyword and substring pattern matching**. When a user types a message, the chatbot sanitizes and normalizes the input, evaluates it against a collection of predefined conversational intents, and returns an appropriate, context-aware reply. In addition to static conversational replies, PyBot incorporates dynamic functionalities—such as querying the host machine's live clock/calendar and randomizing responses from a pool of jokes—delivering an engaging, responsive user experience.

---

## 📌 Project Overview

This project showcases fundamental software engineering practices in Python, emphasizing clean code modularity, state management, and defensive input validation:
- **Rule Engine**: Pre-programmed logic routes user queries to the appropriate response branch.
- **Dynamic Content**: Uses Python's native `datetime` and `random` libraries to generate dynamic, real-time outputs.
- **Fail-Safe Design**: Incorporates defensive exception handling (`KeyboardInterrupt`, `EOFError`) and whitespace sanitation to ensure uninterrupted operation.

### ✨ Key Features

- **Multi-Intent Recognition**: Identifies user intent using keyword and phrase matching across a variety of conversational domains:
  - **Greetings**: Friendly welcomes (`hello`, `hi`, `hey`, `good morning`, etc.).
  - **Bot Identity**: Inquiries about the bot's name and creator (`who are you`, `your name`, `who made you`).
  - **Well-Being**: Inquiries about mood and status (`how are you`, `how are things`).
  - **Real-Time Date & Time**: Dynamic, live timestamp reporting using Python's `datetime` module.
  - **Humor & Jokes**: Random programming jokes selected from a predefined joke pool via `random.choice()`.
  - **Fun Persona**: Responses for bot age, origin, favorite color, and favorite food.
  - **Assistance & Guidance**: A built-in `help` command listing sample prompts.
  - **Polite Farewells**: Clean session termination on goodbye phrases (`bye`, `quit`, `exit`, `see you`).
- **Robust Input Handling**:
  - Automatically trims whitespace and standardizes casing for case-insensitive matching.
  - Detects empty or whitespace-only inputs without crashing or producing generic fallbacks.
  - Gracefully catches terminal interruption signals (`Ctrl+C` / `Ctrl+D` via `KeyboardInterrupt` and `EOFError`).
- **Modular & Clean Architecture**:
  - `get_response()`: Pure logic function mapping input strings to a `(response, should_exit)` tuple.
  - `chatbot()`: Interactive CLI loop managing user input and terminal output.
  - Fully typed with type annotations (`str`, `tuple[str, bool]`, `None`) and docstrings.

---

## 🛠️ Key Concepts & Technologies Used

- **Python 3**
- **Functions & Modularity**: Separation of conversation logic (`get_response`) from I/O loop (`chatbot`).
- **Control Flow**: `if-elif-else` conditional branching and list comprehensions with `any()`.
- **String Manipulation**: Normalization via `.strip()` and `.lower()`, substring containment checks (`in`).
- **Standard Library Modules**:
  - `datetime.datetime`: For live clock time and calendar date queries.
  - `random.choice`: For randomized joke selection.
- **Exception Handling**: `try-except` block safeguarding against abrupt terminal interruptions.

---

## 📂 Project Structure

```text
.
├── basic_chatbot.py   # Main rule-based chatbot script
├── hangman.py         # Hangman game script
├── read.md            # Comprehensive documentation for the basic chatbot
└── README.md          # Hangman game documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your computer. You can check your version in your terminal:
```bash
python --version
```

### Running the Chatbot

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/Python
   ```
3. Run the script:
   ```bash
   python basic_chatbot.py
   ```

---

## 💬 Supported Intents & Example Prompts

| Category | Example User Inputs | PyBot Response Type |
| :--- | :--- | :--- |
| **Greeting** | `"hi"`, `"hello"`, `"good morning"` | Friendly greeting & prompt to help |
| **Status** | `"how are you?"`, `"how are things"` | Inquires about the user's day |
| **Identity** | `"what is your name?"`, `"who are you?"` | Introduces PyBot |
| **Creator** | `"who created you?"`, `"who made you"` | Explains Python origin and logic |
| **Help** | `"help"`, `"what can you do"`, `"features"` | Lists available sample queries |
| **Time** | `"what time is it?"`, `"current time"` | Live formatted time (e.g., `04:30 PM`) |
| **Date** | `"what is today's date?"`, `"what day is it"` | Live formatted date (e.g., `Tuesday, September 08, 2026`) |
| **Jokes** | `"tell me a joke"`, `"make me laugh"` | Random programmer-themed joke |
| **Persona** | `"how old are you?"`, `"where do you live?"` | Humorous computer/memory persona answers |
| **Favorites** | `"what is your favorite color / food?"` | Fun persona preferences |
| **Weather** | `"what's the weather like?"` | Polite placeholder response |
| **Gratitude** | `"thank you"`, `"thanks"` | Polite acknowledgment |
| **Exit** | `"bye"`, `"quit"`, `"exit"`, `"see you"` | Farewell message and terminates session |
| **Fallback** | *(Any unrecognized query)* | Polite fallback suggesting the `'help'` command |

---

## 📝 Example Interaction

```text
============================================================
Welcome to PyBot (Rule-Based Chatbot)!
Type 'help' to see questions you can ask, or 'bye' to exit.
============================================================

You: Hello!
Chatbot: Hi! How can I help you today?

You: What is your name?
Chatbot: I am PyBot, a rule-based chatbot running on Python!

You: What time is it?
Chatbot: The current time is 10:35 PM.

You: Tell me a joke
Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!

You: What is your favorite color?
Chatbot: My favorite color is electric blue! It reminds me of glowing circuits.

You: Thanks for the help!
Chatbot: You're very welcome! Let me know if you need anything else.

You: bye
Chatbot: Goodbye! Have a wonderful day!
```

---

## 📄 License

This project is open-source and created for educational purposes under the CodeAlpha Python Development Internship.
