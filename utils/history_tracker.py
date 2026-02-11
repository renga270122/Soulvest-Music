import streamlit as st

def save_to_history(prompt, reply, tag):
    if "soulprompt_history" not in st.session_state:
        st.session_state.soulprompt_history = []
    st.session_state.soulprompt_history.append({"prompt": prompt, "reply": reply, "tag": tag})

def render_history():
    st.markdown("## 📜 SoulPrompt History")
    if "soulprompt_history" in st.session_state:
        for i, entry in enumerate(reversed(st.session_state.soulprompt_history[-10:])):
            st.markdown(f"**Prompt {len(st.session_state.soulprompt_history)-i}:** {entry['prompt']}")
            st.markdown(f"**Reply:** {entry['reply']}")
            st.markdown(f"🏷️ **Tag:** `{entry['tag']}`")
            st.markdown("---")
    else:
        st.info("No history yet.")

def auto_tag(reply):
    reply_lower = reply.lower()
    if "ritual" in reply_lower:
        return "ritual"
    elif "affirmation" in reply_lower:
        return "affirmation"
    elif "playlist" in reply_lower or "song" in reply_lower:
        return "playlist"
    elif "chant" in reply_lower or "mantra" in reply_lower:
        return "chant"
    else:
        return "reflection"
