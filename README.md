# 💬 Conversational Chatbot — Python

> A Python-based chatbot that understands and responds to user questions in natural language using multi-turn conversational flow logic.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![NLP](https://img.shields.io/badge/NLP-Keyword%20Matching-purple?style=flat)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=flat&logo=windowsterminal)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📸 Demo

> _(Terminal screenshot ya GIF add karo yahan)_

```
Bot  > Hello! I am your assistant. How can I help you today?

You  > What is Python?
Bot  > Python is a high-level, beginner-friendly programming language widely
       used in web development, AI, and data science.

You  > Tell me more about Django
Bot  > Django is a powerful Python web framework that follows the
       MVT (Model-View-Template) pattern. It helps build web apps fast!

You  > Thanks, bye!
Bot  > Goodbye! Have a great day. Feel free to come back anytime!
```

---

## 📋 About The Project

A **Python-based conversational chatbot** that handles multi-turn conversations using keyword detection and rule-based flow logic. Unlike single-response bots, this chatbot maintains conversation context and responds naturally across multiple exchanges.

**Key Highlights:**
- Multi-turn conversation support — remembers context within a session
- Natural language input parsing with keyword-based intent detection
- Covers topics like programming, general knowledge, greetings, and small talk
- Lightweight — no external ML model required, pure Python

---

## ✨ Features

- ✅ Multi-turn conversational flow — not just single Q&A
- ✅ Natural language understanding via keyword & intent detection
- ✅ Handles greetings, farewells, and small talk naturally
- ✅ Covers programming topics — Python, Django, web development
- ✅ Unknown input handling with helpful fallback responses
- ✅ Easy to extend — add new intents in minutes
- ✅ Runs entirely from terminal — zero dependencies on heavy ML frameworks

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Core Libraries | `re`, `random`, `string` |
| Logic | Rule-based intent matching |
| Interface | Command Line (CLI) |
| Version Control | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/conversational-chatbot.git
cd conversational-chatbot

# 2. Install dependencies (minimal)
pip install -r requirements.txt

# 3. Run the chatbot
python chatbot.py
```

---

## 🧠 How It Works

```
User Input
    │
    ▼
Text Preprocessing
(lowercase, strip punctuation)
    │
    ▼
Intent Detection
(keyword matching against intents)
    │
    ▼
Context Check
(is this part of an ongoing topic?)
    │
    ▼
Response Generation
(pick best matching response)
    │
    ▼
Output to User
```

---

## 💬 Supported Intents

| Intent | Example Input |
|--------|--------------|
| Greeting | "Hi", "Hello", "Hey there" |
| Farewell | "Bye", "Goodbye", "See you" |
| About Python | "What is Python?", "Tell me about Python" |
| About Django | "What is Django?", "Explain Django" |
| About Web Dev | "How to build a website?", "What is HTML?" |
| General Knowledge | "What is AI?", "Tell me about machine learning" |
| Small Talk | "How are you?", "What's your name?" |
| Fallback | _(anything unrecognized)_ → helpful default reply |

---

## 📁 Project Structure

```
conversational-chatbot/
│
├── chatbot.py           # Main entry point — run this
├── intents.py           # All intents, keywords & responses
├── processor.py         # Text preprocessing & intent matching
├── context.py           # Conversation context manager
├── requirements.txt
└── README.md
```

---

## 🔧 How to Add a New Intent

```python
# In intents.py — add new topics easily

intents = [
    {
        "tag": "about_python",
        "keywords": ["python", "what is python", "tell me about python"],
        "responses": [
            "Python is a high-level programming language great for web dev and AI!",
            "Python is beginner-friendly and widely used in data science and automation."
        ]
    },
    {
        # Add your new intent here
        "tag": "your_topic",
        "keywords": ["your keyword", "another keyword"],
        "responses": [
            "Your response here!"
        ]
    }
]
```

---

## 🔮 Future Improvements

- [ ] Integrate a free AI API for smarter AI responses
- [ ] Add GUI using Python `tkinter` for a desktop chat window
- [ ] Build a web interface using Django
- [ ] Add memory — remember user name across sessions
- [ ] Learn and apply basic ML for better intent detection (future goal)
- [ ] Deploy as a web chatbot using Django + WebSockets

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-intent`)
3. Add your intent in `intents.py`
4. Commit your changes (`git commit -m 'Add new intent: about_databases'`)
5. Push and open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar yeh project helpful laga toh **star** zaroor karo!
