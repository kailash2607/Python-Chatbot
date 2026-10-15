import random
import re
import time
from html import escape

import streamlit as st

from chatbot import PythonChatbot
from knowledge_base import KNOWLEDGE_BASE

st.set_page_config(page_title="PyBot | Python Helper", page_icon="🐍", layout="wide")

CATEGORIES = {
    "🚀 Basics": [
        "What is Python?",
        "What is a variable in Python?",
        "How do I take input from the user?",
        "How does the if else statement work?",
        "How does a for loop work?",
        "What are f-strings?",
    ],
    "🧱 Data structures": [
        "What is a list in Python?",
        "What is a dictionary in Python?",
        "What is a tuple?",
        "What is a set in Python?",
        "What is list comprehension?",
        "What is slicing in Python?",
    ],
    "🧩 Functions & OOP": [
        "How do I define a function in Python?",
        "What is a lambda function?",
        "What is recursion?",
        "What are classes and objects?",
        "What is inheritance in Python?",
        "What is a decorator in Python?",
    ],
    "🛠️ Files, errors & tools": [
        "How do I read and write files in Python?",
        "How does exception handling work?",
        "What are modules and how do I import them?",
        "What is pip?",
        "What is a virtual environment?",
        "What is a generator and the yield keyword?",
    ],
    "📊 Data libraries": [
        "What is pandas?",
        "What is NumPy?",
        "What do map and filter do?",
        "What are enumerate and zip?",
    ],
}

WELCOME = {
    "role": "assistant",
    "content": "Hey there! 👋 I'm **PyBot**, your Python study buddy. Ask me anything about Python, "
               "like variables, loops, lists, functions, classes or files, and I'll dig out the best answer.",
    "meta": None,
}

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

/* ----- page + animated background ----- */
.stApp {background: #070B1A; font-family: 'Inter', sans-serif; color: #E5E7EB;}
.stApp::before {content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background:
      radial-gradient(620px circle at 12% 18%, rgba(124,58,237,.38), transparent 60%),
      radial-gradient(520px circle at 88% 8%, rgba(219,39,119,.28), transparent 60%),
      radial-gradient(720px circle at 72% 92%, rgba(56,189,248,.22), transparent 60%);
    animation: drift 18s ease-in-out infinite alternate;}
@keyframes drift {to {transform: translate3d(-40px, 25px, 0) scale(1.1);}}
#MainMenu, footer {visibility: hidden;}
[data-testid="stHeader"] {background: transparent;}
.block-container {position: relative; z-index: 1; padding-top: 1.5rem; max-width: 940px;}
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] h5 {color: #E5E7EB;}
[data-testid="stCaptionContainer"] * {color: #94A3B8 !important;}

/* ----- hero ----- */
.hero {position: relative; overflow: hidden; padding: 2.1rem 2.5rem; border-radius: 26px; margin-bottom: 1.3rem;
       background: rgba(255,255,255,.05); border: 1px solid rgba(167,139,250,.35);
       backdrop-filter: blur(14px); box-shadow: 0 0 60px rgba(124,58,237,.25);}
.hero::after {content: ""; position: absolute; inset: 0; border-radius: 26px; padding: 1.5px; pointer-events: none;
       background: linear-gradient(120deg, #7C3AED, #DB2777, #38BDF8, #7C3AED); background-size: 300% 300%;
       animation: borderflow 6s linear infinite;
       -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
       -webkit-mask-composite: xor; mask-composite: exclude;}
@keyframes borderflow {to {background-position: 300% 0;}}
.hero-eyebrow {font-family: 'JetBrains Mono', monospace; font-size: .75rem; letter-spacing: .14em;
       color: #34D399; margin: 0 0 .5rem 0;}
.hero-eyebrow::before {content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%;
       background: #34D399; margin-right: 8px; box-shadow: 0 0 10px #34D399; animation: pulse 1.6s infinite;}
@keyframes pulse {50% {opacity: .25;}}
.hero-title {font-size: 2.6rem; font-weight: 800; margin: 0; line-height: 1.15;
       background: linear-gradient(90deg, #FFFFFF, #C4B5FD, #F9A8D4, #FFFFFF); background-size: 250% auto;
       -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
       animation: shine 6s linear infinite;}
@keyframes shine {to {background-position: 250% center;}}
.hero-sub {font-family: 'JetBrains Mono', monospace; font-size: .98rem; color: #C7D2FE; margin: .7rem 0 0 0;}
.hero-sub::before {content: "> "; color: #F472B6;}
.typing {display: inline-block; overflow: hidden; white-space: nowrap; vertical-align: bottom; width: 0;
       border-right: 2px solid #C4B5FD;
       animation: typing 2.8s steps(49) .4s forwards, blink .8s step-end infinite;}
@keyframes typing {to {width: 49ch;}}
@keyframes blink {50% {border-color: transparent;}}
.hero-badges span {display: inline-block; padding: 5px 14px; margin: 16px 8px 0 0; border-radius: 999px;
       font-size: .8rem; font-weight: 500; color: #E0E7FF; background: rgba(139,92,246,.2);
       border: 1px solid rgba(167,139,250,.45);}

/* ----- chat bubbles ----- */
@keyframes pop {from {opacity: 0; transform: translateY(10px);} to {opacity: 1; transform: none;}}
[data-testid="stChatMessage"] {background: rgba(255,255,255,.045); border: 1px solid rgba(255,255,255,.09);
       border-radius: 22px; padding: 1rem 1.4rem; margin-bottom: .9rem; backdrop-filter: blur(10px);
       box-shadow: 0 6px 24px rgba(0,0,0,.25); animation: pop .35s ease;}
[data-testid="stChatMessage"]:has(.msg-user) {background: linear-gradient(120deg, rgba(124,58,237,.7), rgba(219,39,119,.6));
       border: none; margin-left: 16%; flex-direction: row-reverse; box-shadow: 0 8px 28px rgba(124,58,237,.35);}
[data-testid="stChatMessage"]:has(.msg-user) p {color: #FFFFFF; font-weight: 500; text-align: right;}

/* code blocks */
.stApp pre {background: #0A1020 !important; border: 1px solid rgba(139,92,246,.4); border-radius: 14px;
       box-shadow: inset 0 0 20px rgba(124,58,237,.12);}
.stApp code {font-family: 'JetBrains Mono', monospace !important; font-size: .86rem;}
.stApp p code {background: rgba(139,92,246,.22) !important; color: #E9D5FF !important; padding: 2px 6px; border-radius: 6px;}

/* ----- confidence meter + chips ----- */
.meter {height: 7px; border-radius: 999px; background: rgba(255,255,255,.1); overflow: hidden; margin: .9rem 0 .6rem;}
.meter-fill {height: 100%; border-radius: 999px; box-shadow: 0 0 12px currentColor;}
.chips {display: flex; flex-wrap: wrap; gap: 8px;}
.chip {padding: 3px 12px; border-radius: 999px; font-size: .75rem; font-weight: 600; color: #CBD5E1;
       border: 1px solid rgba(255,255,255,.18); background: rgba(255,255,255,.05);}

/* ----- "how I found this" panel ----- */
[data-testid="stExpander"] {background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.1) !important;
       border-radius: 14px; margin-top: .7rem;}
[data-testid="stExpander"] summary {color: #C7D2FE;}
.tm {display: grid; grid-template-columns: 1fr 120px 46px; gap: 12px; align-items: center; margin: 7px 0;
     font-size: .82rem; color: #CBD5E1;}
.tm-bar {height: 8px; border-radius: 999px; background: rgba(255,255,255,.1); overflow: hidden;}
.tm-bar div {height: 100%; background: linear-gradient(90deg, #7C3AED, #F472B6); border-radius: 999px;}
.tm-s {font-family: 'JetBrains Mono', monospace; text-align: right; color: #F9A8D4;}
.tm-note {font-size: .76rem; color: #94A3B8 !important; margin-top: .6rem;}

/* ----- buttons ----- */
.stButton > button {background: rgba(255,255,255,.06); border: 1px solid rgba(167,139,250,.45); color: #E0E7FF;
       border-radius: 14px; font-weight: 500; text-align: left; transition: .2s;}
.stButton > button:hover {border-color: #F472B6; background: rgba(255,255,255,.13); color: #FFFFFF;
       transform: translateY(-2px); box-shadow: 0 8px 22px rgba(124,58,237,.4);}

/* ----- tabs ----- */
[data-baseweb="tab-list"] {gap: 6px;}
[data-baseweb="tab"] {color: #A5B4FC; border-radius: 10px;}
[data-baseweb="tab"][aria-selected="true"] {color: #FFFFFF;}

/* ----- chat input ----- */
[data-testid="stBottom"], [data-testid="stBottom"] > div, [data-testid="stBottomBlockContainer"] {background: transparent !important;}
[data-testid="stChatInput"] {background: rgba(255,255,255,.08); border: 1px solid rgba(167,139,250,.55);
       border-radius: 20px; box-shadow: 0 0 30px rgba(124,58,237,.25);}
[data-testid="stChatInput"] textarea {color: #FFFFFF;}

/* ----- sidebar ----- */
[data-testid="stSidebar"] {background: rgba(9,12,32,.9); border-right: 1px solid rgba(255,255,255,.08);}
[data-testid="stSidebar"] * {color: #E0E7FF;}
[data-testid="stSidebar"] hr {border-color: rgba(255,255,255,.12) !important;}
[data-testid="stSidebar"] [role="slider"] {background-color: #FFFFFF !important; box-shadow: 0 0 0 4px rgba(244,114,182,.5) !important;}
[data-testid="stSidebar"] [data-testid="stSliderThumbValue"] {color: #FFFFFF !important; font-weight: 700;}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * {color: #A5B4FC !important; font-size: .78rem;}
.sb-brand {display: flex; align-items: center; gap: 12px; padding: .4rem 0 .8rem;}
.sb-logo {width: 48px; height: 48px; border-radius: 15px; font-size: 1.6rem;
          background: linear-gradient(135deg, #7C3AED, #DB2777);
          display: flex; align-items: center; justify-content: center; box-shadow: 0 0 22px rgba(219,39,119,.55);}
.sb-name {font-size: 1.3rem; font-weight: 800; color: #FFFFFF !important; margin: 0; line-height: 1.2;}
.sb-tag {font-size: .78rem; color: #A5B4FC !important; margin: 0;}
.sb-label {font-size: .7rem; font-weight: 700; letter-spacing: .14em; color: #A5B4FC !important; margin: 1.1rem 0 .4rem;}
.stats {display: flex; gap: 8px;}
.stat {flex: 1; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.12);
       border-radius: 14px; padding: .6rem .3rem; text-align: center;}
.stat b {display: block; font-size: 1.25rem; color: #FFFFFF !important;}
.stat span {font-size: .66rem; color: #A5B4FC !important; letter-spacing: .06em;}
.sb-foot {text-align: center; font-size: .72rem; color: #818CF8 !important; margin-top: 1.2rem;}

/* ----- fixes ----- */
.hero .hero-title {font-size: 2.7rem !important; font-weight: 800 !important; line-height: 1.15 !important;
       margin: 0 0 .2rem 0 !important;}
.block-container {padding-bottom: 8rem !important;}
[data-testid="stChatMessage"]:has(.msg-user) {width: fit-content; max-width: 80%; margin-left: auto;}
[data-testid="stBottomBlockContainer"] {max-width: 940px; margin: 0 auto;}
[data-testid="stChatInput"] > div, [data-testid="stChatInput"] [data-baseweb="textarea"],
[data-testid="stChatInput"] [data-baseweb="base-input"], [data-testid="stChatInput"] textarea {
       background: transparent !important; color: #FFFFFF !important;}
[data-testid="stChatInput"] textarea::placeholder {color: #A5B4FC !important; opacity: 1;}
[data-testid="stChatInput"] button {background: linear-gradient(120deg, #7C3AED, #DB2777) !important;
       color: #FFFFFF !important; border-radius: 12px !important;}
</style>
""", unsafe_allow_html=True)


# ---------- Load the bot once ----------
@st.cache_resource
def load_bot():
    return PythonChatbot()


bot = load_bot()

if "messages" not in st.session_state:
    st.session_state.messages = [WELCOME]


# ---------- Helper functions ----------
def queue_question(question):
    """Called when a button is clicked: remember the question to ask on the next run."""
    st.session_state["pending"] = question


def surprise_me():
    st.session_state["pending"] = random.choice(KNOWLEDGE_BASE)["question"]


def clear_chat():
    st.session_state.messages = [WELCOME]


def stream_words(text):
    """Feed the answer word by word so it looks like the bot is typing."""
    for chunk in re.findall(r"\S+\s*", text):
        yield chunk
        time.sleep(0.015)


def answer_meta(meta):
    conf = meta["confidence"] * 100
    if conf >= 60:
        label, color, grad = "High confidence", "#34D399", "linear-gradient(90deg,#34D399,#22D3EE)"
    elif conf >= 40:
        label, color, grad = "Good match", "#60A5FA", "linear-gradient(90deg,#60A5FA,#A78BFA)"
    else:
        label, color, grad = "Possible match", "#FBBF24", "linear-gradient(90deg,#FBBF24,#FB923C)"
    ms = meta.get("elapsed_ms", 0)
    return (
        f'<div class="meter"><div class="meter-fill" style="width:{min(conf, 100):.0f}%;background:{grad};color:{color}"></div></div>'
        f'<div class="chips"><span class="chip" style="color:{color};border-color:{color}">{label} · {conf:.0f}%</span>'
        f'<span class="chip">🎯 {escape(meta["matched_question"])}</span>'
        f'<span class="chip">⚡ {ms:.1f} ms</span></div>')


def match_panel(meta):
    rows = "".join(
        f'<div class="tm"><div>{escape(q)}</div>'
        f'<div class="tm-bar"><div style="width:{min(s * 100, 100):.0f}%"></div></div>'
        f'<div class="tm-s">{s:.2f}</div></div>'
        for q, s in meta["top_matches"])
    note = ('<p class="tm-note">Every entry in the knowledge base gets a cosine-similarity score from 0 to 1. '
            'The highest score wins. If it is below the strictness setting, the bot says it is not sure.</p>')
    return rows + note


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown(
        '<div class="sb-brand"><div class="sb-logo">🐍</div>'
        '<div><p class="sb-name">PyBot</p><p class="sb-tag">Your Python study buddy</p></div></div>',
        unsafe_allow_html=True)

    st.markdown('<p class="sb-label">📊 THIS SESSION</p>', unsafe_allow_html=True)
    stats_slot = st.empty()   # filled in below, after the new question has been handled

    st.markdown('<p class="sb-label">🎚️ ANSWER STRICTNESS</p>', unsafe_allow_html=True)
    bot.threshold = st.slider("Strictness", 0.10, 0.50, 0.25, 0.05, label_visibility="collapsed")
    st.caption("Higher = more 'not sure' replies. Lower = the bot tries to answer more questions.")

    show_details = st.toggle("🔍 Show how answers are matched", value=True)

    st.markdown('<p class="sb-label">🎲 FEELING CURIOUS?</p>', unsafe_allow_html=True)
    st.button("🎲  Surprise me with a topic", on_click=surprise_me)
    st.button("🗑️  Clear chat", on_click=clear_chat)

    st.divider()
    st.caption(f"📚 {len(KNOWLEDGE_BASE)} topics in the knowledge base · TF-IDF + cosine similarity")
    st.markdown('<p class="sb-foot">Built with Python · scikit-learn · Streamlit</p>', unsafe_allow_html=True)

# ---------- Header ----------
st.markdown(
    '<div class="hero">'
    f'<p class="hero-eyebrow">ONLINE · {len(KNOWLEDGE_BASE)} TOPICS LOADED</p>'
    '<p class="hero-title">Python Helper Bot</p>'
    '<p class="hero-sub"><span class="typing">ask anything about python. get answers with code.</span></p>'
    '<div class="hero-badges"><span>⚡ TF-IDF</span><span>📐 Cosine Similarity</span>'
    '<span>🧠 NLP</span><span>🎯 Confidence scores</span></div></div>',
    unsafe_allow_html=True)

# ---------- Get the new question (typed or clicked) ----------
prompt = st.chat_input("Ask a Python question, e.g. how do I sort a list?")
question = prompt or st.session_state.pop("pending", None)

if question:
    st.session_state.messages.append({"role": "user", "content": question, "meta": None})
    start = time.perf_counter()
    reply = bot.ask(question)
    reply["elapsed_ms"] = (time.perf_counter() - start) * 1000
    st.session_state.messages.append(
        {"role": "assistant", "content": reply["answer"], "meta": reply, "animate": True})

# ---------- Update the session stats (after the new question is included) ----------
replies = [m["meta"] for m in st.session_state.messages
           if m["meta"] and m["meta"]["type"] in ("answer", "unknown")]
answered = [r for r in replies if r["type"] == "answer"]
avg_conf = f"{sum(r['confidence'] for r in answered) / len(answered) * 100:.0f}%" if answered else "-"
stats_slot.markdown(
    f'<div class="stats"><div class="stat"><b>{len(replies)}</b><span>ASKED</span></div>'
    f'<div class="stat"><b>{len(answered)}</b><span>ANSWERED</span></div>'
    f'<div class="stat"><b>{avg_conf}</b><span>AVG MATCH</span></div></div>',
    unsafe_allow_html=True)

# ---------- Show the conversation ----------
messages = st.session_state.messages
last = len(messages) - 1

for i, msg in enumerate(messages):
    avatar = "😎" if msg["role"] == "user" else "🐍"
    with st.chat_message(msg["role"], avatar=avatar):
        if msg["role"] == "user":
            # the hidden span lets the CSS recognise user bubbles
            st.markdown(f'<span class="msg-user"></span>{escape(msg["content"])}', unsafe_allow_html=True)
            continue

        if msg.get("animate"):
            st.write_stream(stream_words(msg["content"]))
            msg["animate"] = False
        else:
            st.markdown(msg["content"])

        meta = msg["meta"]
        if meta and meta["type"] == "answer":
            st.markdown(answer_meta(meta), unsafe_allow_html=True)

        if meta and show_details and meta["type"] in ("answer", "unknown") and meta.get("top_matches"):
            with st.expander("🔍 How I found this answer"):
                st.markdown(match_panel(meta), unsafe_allow_html=True)

        # clickable related questions, only under the newest reply
        if meta and i == last and meta["suggestions"]:
            st.caption("Try one of these:" if meta["type"] == "unknown" else "Related questions:")
            for j, suggestion in enumerate(meta["suggestions"]):
                st.button(suggestion, key=f"sug_{i}_{j}", on_click=queue_question, args=(suggestion,))

# ---------- Topic explorer on an empty chat ----------
if len(messages) == 1:
    st.markdown("##### 🧭 Explore a topic")
    tabs = st.tabs(list(CATEGORIES.keys()))
    for tab_index, (tab, questions) in enumerate(zip(tabs, CATEGORIES.values())):
        with tab:
            cols = st.columns(2)
            for j, q in enumerate(questions):
                cols[j % 2].button(q, key=f"cat_{tab_index}_{j}", on_click=queue_question, args=(q,))
