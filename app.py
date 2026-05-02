import streamlit as st
import google.generativeai as genai

# Page setting
st.set_page_config(page_title="Logistics AI Pro", page_icon="")
st.title(" Logistics Expert (Zaw's Pro)")

# API Key ကို Secrets ကနေ လုံခြုံစွာယူမယ်
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Please add your GOOGLE_API_KEY in Streamlit Secrets!")

# Model ကို အတည်ငြိမ်ဆုံး version ဖြစ်တဲ့ gemini-1.5-flash သုံးမယ်
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat history ကို သိမ်းထားဖို့
if "messages" not in st.session_state:
    st.session_state.messages = []

# အရင်ပြောထားတဲ့ စာတွေကို ပြန်ပြဖို့
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ဆီက အမေးကို လက်ခံဖို့
if prompt := st.chat_input("Logistics အကြောင်း မေးမြန်းနိုင်ပါပြီ Zaw..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ဆီက အဖြေတောင်းဖို့
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
