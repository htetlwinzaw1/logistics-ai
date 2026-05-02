import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Logistics AI Pro", page_icon="")
st.title(" Logistics Expert (Zaw's Pro)")

# API Key ကို Secrets ကနေယူမယ်
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Secrets ထဲမှာ GOOGLE_API_KEY ထည့်ဖို့ လိုနေပါတယ်ဗျ!")

# Model ကို အသစ်ဆုံး version နဲ့ ချိတ်မယ် (v1beta မဟုတ်ဘဲ တိုက်ရိုက်ခေါ်နည်း)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

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
            # အဖြေထုတ်ပေးမယ့်နေရာ
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
