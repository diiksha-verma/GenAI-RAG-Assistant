import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Meeting Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: #0a0a0f;
    font-family: 'DM Mono', monospace;
}

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* ── Hero Header ── */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
    position: relative;
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(99,220,180,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: #63dcb4;
    border: 1px solid rgba(99,220,180,0.3);
    padding: 0.3rem 0.9rem;
    border-radius: 2px;
    margin-bottom: 1.2rem;
    text-transform: uppercase;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    font-weight: 800;
    color: #f0f0f0;
    line-height: 1.1;
    margin: 0 0 0.8rem;
    letter-spacing: -0.02em;
}
.hero-title span { color: #63dcb4; }
.hero-sub {
    font-size: 0.85rem;
    color: #555;
    letter-spacing: 0.05em;
}

/* ── Input Card ── */
.input-card {
    background: #111118;
    border: 1px solid #1e1e2e;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    position: relative;
    overflow: hidden;
}
.input-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #63dcb4, transparent);
}
.card-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    color: #63dcb4;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

/* ── Streamlit input overrides ── */
.stTextInput > div > div > input,
.stSelectbox > div > div > div {
    background: #0d0d15 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 8px !important;
    color: #e0e0e0 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.9rem !important;
    padding: 0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #63dcb4 !important;
    box-shadow: 0 0 0 2px rgba(99,220,180,0.1) !important;
}
.stTextInput label, .stSelectbox label {
    color: #555 !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    font-family: 'DM Mono', monospace !important;
}

/* ── Button ── */
.stButton > button {
    background: #63dcb4 !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.05em !important;
    padding: 0.7rem 2rem !important;
    width: 100% !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: #7ff5cc !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(99,220,180,0.2) !important;
}

/* ── Result Section ── */
.section-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 2rem 0 1rem;
}
.section-icon {
    width: 32px; height: 32px;
    background: rgba(99,220,180,0.1);
    border: 1px solid rgba(99,220,180,0.2);
    border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #e0e0e0;
    letter-spacing: 0.02em;
}

/* ── Result Cards ── */
.result-card {
    background: #111118;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    position: relative;
}
.result-card.accent {
    border-left: 3px solid #63dcb4;
}
.result-text {
    color: #b0b0c0;
    font-size: 0.85rem;
    line-height: 1.8;
    white-space: pre-wrap;
}
.title-display {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #f0f0f0;
    line-height: 1.3;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #111118 !important;
    border-bottom: 1px solid #1e1e2e !important;
    gap: 0 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 0 1rem !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    color: #555 !important;
    padding: 0.9rem 1.2rem !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #63dcb4 !important;
    border-bottom-color: #63dcb4 !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: #111118 !important;
    border: 1px solid #1e1e2e !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
    padding: 1.5rem !important;
}

/* ── Chat ── */
.chat-container {
    background: #0d0d15;
    border: 1px solid #1e1e2e;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 2rem;
    min-height: 200px;
    max-height: 500px;
    overflow-y: auto;
}
.chat-msg {
    margin-bottom: 1rem;
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
}
.chat-avatar {
    width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    flex-shrink: 0;
    margin-top: 2px;
}
.chat-avatar.user { background: rgba(99,220,180,0.15); color: #63dcb4; border: 1px solid rgba(99,220,180,0.3); }
.chat-avatar.bot  { background: rgba(255,255,255,0.05); color: #888; border: 1px solid #1e1e2e; }
.chat-bubble {
    background: #161622;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 0.75rem 1rem;
    color: #c0c0d0;
    font-size: 0.84rem;
    line-height: 1.7;
    flex: 1;
}
.chat-bubble.user { background: rgba(99,220,180,0.05); border-color: rgba(99,220,180,0.15); }

/* ── Status ── */
.status-bar {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.75rem;
    color: #555;
    font-family: 'DM Mono', monospace;
    margin-bottom: 1rem;
}
.status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #63dcb4;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* ── Divider ── */
.fancy-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e1e2e, transparent);
    margin: 2rem 0;
}

/* ── Metric chips ── */
.metrics-row {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
    flex-wrap: wrap;
}
.metric-chip {
    background: #111118;
    border: 1px solid #1e1e2e;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    font-size: 0.72rem;
    color: #555;
    letter-spacing: 0.05em;
}
.metric-chip span { color: #63dcb4; font-weight: 600; }

/* ── Chat input ── */
.stChatInput > div {
    background: #111118 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 10px !important;
}
.stChatInput textarea {
    background: transparent !important;
    color: #e0e0e0 !important;
    font-family: 'DM Mono', monospace !important;
}
.stChatMessage {
    background: #111118 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# ── Session State ─────────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "processing" not in st.session_state:
    st.session_state.processing = False


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">AI · RAG · NLP</div>
    <h1 class="hero-title">Meeting <span>Intelligence</span></h1>
    <p class="hero-sub">Drop a YouTube URL or audio file. Get insights instantly.</p>
</div>
""", unsafe_allow_html=True)


# ── Input Panel ───────────────────────────────────────────────────────────────
st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="card-label">Source</p>', unsafe_allow_html=True)
    source = st.text_input(
        label="source_hidden",
        placeholder="https://youtube.com/watch?v=... or /path/to/audio.wav",
        label_visibility="collapsed",
        key="source_input"
    )
with col2:
    st.markdown('<p class="card-label">Language</p>', unsafe_allow_html=True)
    language = st.selectbox(
        label="lang_hidden",
        options=["english", "hinglish"],
        label_visibility="collapsed",
        key="lang_select"
    )

st.markdown('</div>', unsafe_allow_html=True)

run_btn = st.button("⚡  Analyze Meeting", key="run_btn")


# ── Processing ────────────────────────────────────────────────────────────────
if run_btn and source:
    st.session_state.chat_history = []
    st.session_state.result = None

    with st.status("🔄 Processing your meeting...", expanded=True) as status:
        try:
            from utils.audio_processor import process_input
            from core.transcriber import transcribe_all
            from core.summarize import summarize, generate_title
            from core.extractor import extract_action_items, extract_key_decisions, extract_questions
            from core.rag_engine import build_rag_chain

            st.write("📥 Downloading & processing audio...")
            chunks = process_input(source)

            st.write(f"🎙️ Transcribing {len(chunks)} chunk(s) with Whisper...")
            transcript = transcribe_all(chunks, language)

            st.write("🧠 Running AI analysis...")
            title     = generate_title(transcript)
            summary   = summarize(transcript)
            actions   = extract_action_items(transcript)
            decisions = extract_key_decisions(transcript)
            questions = extract_questions(transcript)

            st.write("🔗 Building RAG chain...")
            rag_chain = build_rag_chain(transcript)

            st.session_state.result = {
                "title": title,
                "transcript": transcript,
                "summary": summary,
                "action_items": actions,
                "key_decisions": decisions,
                "open_questions": questions,
                "rag_chain": rag_chain,
            }
            status.update(label="✅ Analysis complete!", state="complete")

        except Exception as e:
            status.update(label="❌ Error occurred", state="error")
            st.error(f"```\n{str(e)}\n```")

elif run_btn and not source:
    st.warning("Please enter a YouTube URL or file path.")


# ── Results ───────────────────────────────────────────────────────────────────
if st.session_state.result:
    r = st.session_state.result

    st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

    # Title
    st.markdown(f'<div class="result-card"><div class="title-display">📌 {r["title"]}</div></div>', unsafe_allow_html=True)

    # Metrics row
    word_count = len(r["transcript"].split())
    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-chip">Words: <span>{word_count:,}</span></div>
        <div class="metric-chip">Language: <span>{language.title()}</span></div>
        <div class="metric-chip">Status: <span>Complete</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋  SUMMARY",
        "✅  ACTIONS",
        "🔑  DECISIONS",
        "❓  QUESTIONS",
        "📝  TRANSCRIPT",
    ])

    with tab1:
        st.markdown(f'<div class="result-text">{r["summary"]}</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown(f'<div class="result-text">{r["action_items"]}</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown(f'<div class="result-text">{r["key_decisions"]}</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown(f'<div class="result-text">{r["open_questions"]}</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown(f'<div class="result-text" style="max-height:400px;overflow-y:auto">{r["transcript"]}</div>', unsafe_allow_html=True)

    # ── Chat Section ──────────────────────────────────────────────────────────
    st.markdown('<hr class="fancy-divider">', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-header">
        <div class="section-icon">💬</div>
        <div class="section-title">Chat with your meeting</div>
    </div>
    <div class="status-bar">
        <div class="status-dot"></div>
        RAG chain active — ask anything about the meeting
    </div>
    """, unsafe_allow_html=True)

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask about the meeting..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    from core.rag_engine import ask_question
                    answer = ask_question(r["rag_chain"], prompt)
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                except Exception as e:
                    err = f"Error: {str(e)}"
                    st.error(err)
                    st.session_state.chat_history.append({"role": "assistant", "content": err})

else:
    # Empty state
    st.markdown("""
    <div style="text-align:center; padding: 4rem 2rem; color: #2a2a3a;">
        <div style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.3;">🎙️</div>
        <div style="font-family: 'DM Mono', monospace; font-size: 0.8rem; letter-spacing: 0.1em;">
            PASTE A URL ABOVE TO GET STARTED
        </div>
    </div>
    """, unsafe_allow_html=True)