import streamlit as st
from utils.openai_helper import get_soulful_reply
from utils.voice_helper import render_voice_controls, render_voice_button
from utils.history_tracker import save_to_history, render_history, auto_tag
from utils.pin_storage import save_pin

def render_soulprompt():
    st.markdown("## 🧘🏽 SoulPrompt: Ask Soulvest Anything Soulful")

    mode = st.sidebar.radio("🧭 SoulPrompt Mode", ["💬 Text", "🎙️ Voice", "📜 History"])

    if mode == "🎙️ Voice":
        render_voice_controls()
        return
    elif mode == "📜 History":
        render_history()
        return

    user_prompt = st.text_area("💬 Your prompt", height=150)
    submit = st.button("Receive Soulful Guidance")

    if submit and user_prompt:
        with st.spinner("Soulvest is tuning into your energy..."):
            try:
                reply = get_soulful_reply(user_prompt)
                tag = auto_tag(reply)
                save_to_history(user_prompt, reply, tag)

                st.markdown("### ✨ Soulvest Responds:")
                st.markdown(reply)
                st.markdown(f"🏷️ **Tag:** `{tag}`")
                render_voice_button(reply)

                if st.button("📌 Pin this reply"):
                    save_pin(user_prompt, reply, tag)
                    st.success("Reply pinned to your SoulPrompt dashboard!")
            except Exception as e:
                st.error("⚠️ Soulvest is momentarily silent. Please check your API key or connection.")

    with st.expander("💡 Prompt Inspiration"):
        st.markdown("- Suggest a morning ritual for clarity")
        st.markdown("- What’s a healing affirmation for anxiety?")
        st.markdown("- Create a soulful Tamil playlist for Sunday")
        st.markdown("- Explain the meaning of Dakshinamurthy stotram")
