# 🐍 Personal Python Question-Answering Chatbot

A simple chatbot that answers Python programming questions typed in natural language. It looks up the closest match in a predefined Python knowledge base using NLP (TF-IDF and cosine similarity) and replies with an explanation and a code example.

## Problem Statement

Develop a simple personal chatbot that can answer questions related to Python programming. The user enters a question in natural language, and the chatbot provides an appropriate answer based on a predefined Python knowledge base.

## Features

- Understands differently worded questions ("how do I make a loop?" and "for loop syntax" reach the same answer)
- Knowledge base of 53 Python topics: variables, loops, lists, dictionaries, functions, OOP, files, exceptions, libraries and more
- Answers include formatted code examples
- Confidence score and the matched question shown with every answer
- "I'm not sure" reply for questions outside Python, with suggested topics
- Handles greetings, thanks and goodbye
- Clickable related questions and quick-topic buttons
- Adjustable strictness slider
- Clean chat interface built with Streamlit

## How It Works

1. **Knowledge base:** each entry holds a question, alternative phrasings and an answer (`knowledge_base.py`).
2. **Text processing:** the question is lowercased, filler words are removed and plurals are reduced to singular form ("errors" becomes "error").
3. **TF-IDF:** every knowledge base entry and the user's question are converted to numeric vectors. Words that are rare across entries but present in a question get a higher weight.
4. **Cosine similarity:** the question vector is compared with every entry, giving a score from 0 to 1.
5. **Answer selection:** the highest-scoring entry is returned. If the best score is below the threshold (0.25 by default), the bot says it is not sure instead of guessing.

## Tech Stack

- Python 3
- scikit-learn (TF-IDF, cosine similarity)
- Streamlit (web interface)

## Project Structure

```
chatbot/
├── knowledge_base.py   # Python Q&A entries
├── chatbot.py          # matching engine (TF-IDF + cosine similarity)
├── app.py              # Streamlit chat interface
├── test_chatbot.py     # terminal test version
└── README.md
```

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install scikit-learn streamlit
python -m streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Example Questions

| Question | Matched topic |
|---|---|
| how do i make a loop in python | How does a for loop work? |
| difference between list and tuple | What is the difference between a list and a tuple? |
| how to catch errors | How does exception handling work? |
| how to take user input | How do I take input from the user? |
| who won the cricket world cup | Not sure (outside the knowledge base) |

## Screenshots

_Add 2-3 screenshots here: the welcome screen, an answer with a code example, and the "not sure" reply._

## Limitations and Future Work

- The bot only knows the topics in its knowledge base. Adding more entries expands what it can answer.
- It matches words, not meaning, so a question using completely different vocabulary may not match.
- Possible improvements: sentence embeddings for meaning-based matching, remembering earlier messages in the conversation, and a way to add new entries from the interface.
