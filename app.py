import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Logistics AI Pro", page_icon="")
st.title(" Logistics Expert (Zaw's Pro)")

# API Key ကို Streamlit Cloud ရဲ့ Secrets ထဲကနေ ယူမှာပါ
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception:
    st.error("API Key ထည့်ရန် လိုအပ်နေပါသည် Zaw။")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Logistics အကြောင်း မေးမြန်းနိုင်ပါပြီ Zaw..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {str(e)}")
