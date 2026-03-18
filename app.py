import streamlit as st
from langchain_core.messages import HumanMessage, AIMessageChunk
from dental_agent.agent import dental_graph

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Dental Assistant",
    page_icon="🦷",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.chat-bubble-user {
    background-color: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    max-width: 70%;
    margin-left: auto;
}

.chat-bubble-bot {
    background-color: #e2e8f0;
    color: black;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    max-width: 70%;
}

.header {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subheader {
    color: gray;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="header">🦷 Dental Appointment Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Book, reschedule, or check appointments instantly</div>', unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.title("⚙️ Controls")

    if st.button("🧹 Clear Chat"):
        st.session_state.history = []
        st.rerun()

    st.markdown("---")

    st.markdown("### ℹ️ About")
    st.write("AI-powered dental assistant using LangGraph + OpenRouter.")

    st.markdown("### 🧠 Example Queries")
    st.write("""
    - Show available slots for orthodontist  
    - Book appointment with Dr. John Doe tomorrow  
    - Cancel my appointment  
    - Reschedule my booking  
    """)

# ------------------ SESSION STATE ------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------ CHAT DISPLAY ------------------
for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        st.markdown(
            f'<div class="chat-bubble-user">{msg.content}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-bubble-bot">{msg.content}</div>',
            unsafe_allow_html=True
        )

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Ask about appointments...")

# ------------------ PROCESS INPUT ------------------
if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))

    # Display user message
    st.markdown(
        f'<div class="chat-bubble-user">{user_input}</div>',
        unsafe_allow_html=True
    )

    # Assistant response
    response_container = st.empty()
    full_response = ""
    final_messages = None

    try:
        with st.spinner("🤖 Thinking..."):
            for event_type, data in dental_graph.stream(
                {"messages": st.session_state.history},
                stream_mode=["messages", "values"],
                config={"recursion_limit": 20},
            ):
                if event_type == "messages":
                    chunk, meta = data

                    if (
                        isinstance(chunk, AIMessageChunk)
                        and chunk.content
                        and not getattr(chunk, "tool_calls", None)
                    ):
                        full_response += chunk.content
                        response_container.markdown(
                            f'<div class="chat-bubble-bot">{full_response}</div>',
                            unsafe_allow_html=True
                        )

                elif event_type == "values":
                    final_messages = data.get("messages", [])

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.session_state.history.pop()

    if final_messages:
        st.session_state.history = final_messages

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit + LangGraph</center>",
    unsafe_allow_html=True
)
