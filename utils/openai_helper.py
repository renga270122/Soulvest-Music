import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_soulful_reply(prompt):
    messages = [
        {"role": "system", "content": "You are Soulvest, a soulful guide blending spiritual wisdom, emotional wellness, and healing music. Respond with warmth, clarity, and empowerment."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
