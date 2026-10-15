import re

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge_base import KNOWLEDGE_BASE

# Replies for greetings and thanks (checked before searching the knowledge base)
SMALL_TALK = {
    "greeting": (
        {"hi", "hello", "hey", "hii", "hola", "good morning", "good evening", "good afternoon"},
        "Hello! 👋 I'm your Python helper. Ask me anything about Python, "
        "for example *'How does a for loop work?'*",
    ),
    "thanks": (
        {"thanks", "thank you", "thx", "thank u", "ok thanks", "great thanks"},
        "You're welcome! Ask me another Python question whenever you like. 🙂",
    ),
    "bye": (
        {"bye", "goodbye", "see you", "exit", "quit"},
        "Goodbye! Happy coding! 🐍",
    ),
    "about": (
        {"who are you", "what are you", "what can you do", "help"},
        "I'm a Python Q&A chatbot. I search my knowledge base of Python topics "
        "(variables, loops, lists, functions, classes, files and more) and give you "
        "the closest answer. Just type your question!",
    ),
}


def tokenize(text):
    """Split text into lowercase words, drop filler words (the, is, how...) and
    turn plurals into singular so that 'errors' matches 'error' and 'classes' matches 'class'."""
    words = re.findall(r"\w+", text.lower())
    tokens = []
    for w in words:
        if w in ENGLISH_STOP_WORDS:
            continue
        if w.endswith("ies") and len(w) > 4:
            w = w[:-3] + "y"            # dictionaries -> dictionary
        elif w.endswith("sses"):
            w = w[:-2]                  # classes -> class
        elif w.endswith("s") and not w.endswith("ss") and len(w) > 3:
            w = w[:-1]                  # lists -> list
        tokens.append(w)
    return tokens


class PythonChatbot:
    def __init__(self, threshold=0.25):
        # If the best match scores below this, the bot says it is not sure.
        self.threshold = threshold

        # Text used for matching: the question (twice, so it counts more)
        # plus the extra phrasings from "variants".
        self.documents = [
            f"{e['question']} {e['question']} {e['variants']}" for e in KNOWLEDGE_BASE
        ]

        # Turn every entry into TF-IDF numbers (done once, when the bot starts).
        self.vectorizer = TfidfVectorizer(tokenizer=tokenize, token_pattern=None, ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.documents)

    def _small_talk(self, text):
        cleaned = re.sub(r"[^a-z ]", "", text.lower()).strip()
        for phrases, reply in SMALL_TALK.values():
            if cleaned in phrases:
                return reply
        return None

    def ask(self, user_question, top_n=3):
        """Return a dictionary describing the bot's reply."""
        text = user_question.strip()
        if not text:
            return {"type": "empty", "answer": "Please type a question first.",
                    "matched_question": None, "confidence": 0.0, "suggestions": [], "top_matches": []}

        # 1. greetings, thanks, goodbye
        reply = self._small_talk(text)
        if reply:
            return {"type": "smalltalk", "answer": reply,
                    "matched_question": None, "confidence": 1.0, "suggestions": [], "top_matches": []}

        # 2. compare the question with every entry (cosine similarity)
        query_vec = self.vectorizer.transform([text])
        scores = cosine_similarity(query_vec, self.matrix)[0]
        ranked = scores.argsort()[::-1]          # best match first
        best = ranked[0]

        # 3. suggestions = the next best questions (only if they are somewhat related)
        suggestions = [KNOWLEDGE_BASE[i]["question"]
                       for i in ranked[1:top_n + 1] if scores[i] > 0.05]

        top_matches = [(KNOWLEDGE_BASE[i]["question"], float(scores[i])) for i in ranked[:top_n]]

        # 4. too low a score means "I don't know"
        if scores[best] < self.threshold:
            return {"type": "unknown",
                    "answer": "Sorry, I'm not sure about that. 🤔 Try rephrasing, "
                              "or ask about a basic Python topic like loops, lists or functions.",
                    "matched_question": None,
                    "confidence": float(scores[best]),
                    "suggestions": [KNOWLEDGE_BASE[i]["question"] for i in ranked[:top_n]],
                    "top_matches": top_matches}

        return {"type": "answer",
                "answer": KNOWLEDGE_BASE[best]["answer"],
                "matched_question": KNOWLEDGE_BASE[best]["question"],
                "confidence": float(scores[best]),
                "suggestions": suggestions,
                "top_matches": top_matches}
