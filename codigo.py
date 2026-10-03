import streamlit as st
from openai import OpenAI

aiModel = OpenAI(api_key="AQ.Ab8RN6KOh0fb-lpIqZRim7kfiX0drRqXDpBYP0i9xWNCFUJAtQ",
                 base_url="https://generativelanguage.googleapis.com/v1beta/openai")


st.write("## ChatBot de AI")

if not "lstMsg" in st.session_state:
    st.session_state["lstMsg"] = []

msgUsr=st.chat_input("Escreva sua mensagem aqui")

for msg in st.session_state["lstMsg"]:
    sentBy=msg["role"]
    txtMsg=msg["content"]
    st.chat_message(sentBy).write(txtMsg)

if msgUsr: 
    st.chat_message("human").write(msgUsr)
    msg1 = {"role": "user", "content":msgUsr}
    st.session_state["lstMsg"].append(msg1)

    iaMdl = aiModel.chat.completions.create(
        messages=st.session_state["lstMsg"],
        model="gemini-flash-lite-latest"
    )

    iaQuest = iaMdl.choices[0].message.content

    st.chat_message("assistant").write(iaQuest)
    msg2 = {"role": "assistant", "content":iaQuest}
    st.session_state["lstMsg"].append(msg2)
    
