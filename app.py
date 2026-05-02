import streamlit as st
from openai import OpenAI

# Streamlit Secrets ကနေ Key ကိုယူမယ်
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title(" Logistics Expert (Zaw x ChatGPT)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat History ပြသခြင်း
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ဆီက အချက်အလက်ယူခြင်း
if prompt := st.chat_input("Logistics အကြောင်း မေးမြန်းပါ Zaw..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ဆီက အဖြေတောင်းခြင်း
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # ဒါမှမဟုတ် gpt-4o-mini
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
