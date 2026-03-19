
import streamlit as st 
import requests as req 
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

api_key = os.getenv("api_key")
txt=st.text_input("enter the text")

btn=st.button("submit")


if btn:
    data={
    "contents": [
      {
        "parts": [
          {
            "text": f"{txt}"
          }
        ]
      }
    ]
    }
    headers= {"x-goog-api-key": api_key,
  "Content-Type": "application/json" }
    with st.spinner("....loading"):
      res=req.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",json=data,headers=headers)
    data=res.json()
    st.markdown(data)
    # st.markdown(data["candidates"][0]["content"]["parts"][0]["text"])