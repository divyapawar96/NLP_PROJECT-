import streamlit as st
import time
from model import IntentClassifier

# Set up beautiful and simple page configurations
st.set_page_config(
    page_title="Smart Reply Generator",
    page_icon="💡",
    layout="centered"
)

# Initialize Session State Variables to save history dynamically
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

@st.cache_resource
def load_intent_classifier():
    """Caches the model so we don't reload heavy structures upon every UI interaction."""
    return IntentClassifier()

# Load our NLP classification Model
classifier = load_intent_classifier()

# Build the UI Layout Header
st.title("💡 Context-Aware Smart Reply Generator")
st.markdown("""
Welcome! Type a message below, and this AI will detect the *intent* of your text 
and generate **3 smart, context-aware reply suggestions**. Just like Gmail or LinkedIn!
""")
st.divider()

# Interactive Input Area
user_message = st.text_input(
    "Enter a message you received:", 
    placeholder="e.g., Hi! Let's schedule a meeting for tomorrow."
)

if st.button("✨ Generate Smart Replies", use_container_width=True, type="primary"):
    if user_message.strip():
        with st.spinner("Analyzing message intent..."):
            # Simulate a mini delay for visual impact and processing feel
            time.sleep(0.5) 
            
            # Predict intent and confidence
            intent, confidence = classifier.detect_intent(user_message)
            replies = classifier.get_replies(intent)
            
            st.success("✅ Analysis Complete!")
            
            # Show Informational Metrics
            col1, col2 = st.columns(2)
            col1.metric("🧠 Detected Intent", intent.replace("_", " ").title())
            col2.metric("📊 Confidence Score", f"{confidence * 100:.0f}%")
            
            st.write("") # Whitespace
            
            # Highlight Suggestions
            st.markdown("### 💬 Suggested Replies:")
            for i, reply in enumerate(replies, 1):
                st.info(f"**{i}.** {reply}")
                
            # Log successful hits dynamically into Session history
            st.session_state.chat_history.append({
                "msg": user_message,
                "intent": intent.replace("_", " ").title(),
                "replies": replies
            })
    else:
        st.warning("⚠️ Please enter a valid message!")

# Display Historical Queries as an Optional feature block
if st.session_state.chat_history:
    st.divider()
    with st.expander("📂 View Session History"):
        for entry in reversed(st.session_state.chat_history):
            st.markdown(f"**🗨️ You Received:** {entry['msg']}")
            st.markdown(f"*📝 Predicted Intent:* {entry['intent']}")
            st.markdown("---")

st.markdown("<br><hr><center><small>Built with ❤️ using Streamlit, spaCy & Python | Machine Learning & NLP Basics</small></center>", unsafe_allow_html=True)
