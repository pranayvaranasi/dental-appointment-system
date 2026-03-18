import streamlit as st
from langchain_core.messages import HumanMessage, AIMessageChunk
from dental_agent.agent import dental_graph

st.set_page_config(page_title="Dental Assistant", layout="wide")

st.title("🦷 Dental Appointment Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask about appointments...")

if user_input:
    st.session_state.history.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        final_messages = None

        try:
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
                        response_placeholder.markdown(full_response)

                elif event_type == "values":
                    final_messages = data.get("messages", [])

        except Exception as e:
            st.error(f"Error: {e}")
            st.session_state.history.pop()

        if final_messages:
            st.session_state.history = final_messages
