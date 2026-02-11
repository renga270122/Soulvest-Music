import streamlit as st
from utils.pin_storage import load_pins
from utils.voice_helper import render_voice_button
from collections import Counter

def render_soulprompt_pins():
    st.markdown("## 📌 My SoulPrompt Pins")
    pins = load_pins()

    if not pins:
        st.info("No pinned replies yet.")
        return

    tags = [pin['tag'] for pin in pins]
    tag_counts = Counter(tags)
    st.markdown("### 🏷️ Tag Cloud")
    for tag, count in tag_counts.items():
        st.markdown(f"- `{tag}` ({count})")

    st.markdown("### 🔍 Filter Pins")
    search_term = st.text_input("Search by tag or keyword")

    filtered = [
        pin for pin in pins
        if search_term.lower() in pin['tag'].lower() or
           search_term.lower() in pin['prompt'].lower() or
           search_term.lower() in pin['reply'].lower()
    ] if search_term else pins

    for i, pin in enumerate(reversed(filtered)):
        st.markdown(f"**Prompt {len(filtered)-i}:** {pin['prompt']}")
        st.markdown(f"**Reply:** {pin['reply']}")
        st.markdown(f"🏷️ **Tag:** `{pin['tag']}`")
        render_voice_button(pin['reply'], key=f"voice_{i}")
        st.markdown("---")
