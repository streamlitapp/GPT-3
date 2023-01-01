import streamlit as st
import openai

st.subheader('GPT-3')

openai.api_key = st.text_input('API Key')

model_engine = st.selectbox('Engine', 
                            ('text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001',
                             'code-davinci-002', 'code-cushman-001'))

prompt = st.text_input('Prompt')

if openai.api_key and prompt:
  completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=4000)
  st.text(completion.choices[0].text)
