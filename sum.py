import openai
import streamlit as st

openai.api_key = "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"

st.header('GPT-3 Demo')
input = st.text_area("Please enter the text", value="")

if st.button("Submit"):
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=input,
    temperature=0.7, #controls how much randomness is in the output
    max_tokens=150, #maximum number of tokens
    top_p=0.90,#how many of the highest-probability words are selected to be included in the generated text
    frequency_penalty=0.0,#how much frequency of tokens in the source material will influence the output of the model.
    presence_penalty=0.0,
    ##stop=["\n"]
  )
    st.write(response.choices[0].text)