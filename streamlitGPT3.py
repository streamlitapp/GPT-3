import streamlit as st
import openai

st.subheader('GPT-3')

openai.api_key = "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"

model_engine = st.selectbox('Engine', 
                            ('text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001',
                             'code-davinci-002', 'code-cushman-001'))

prompt = st.text_input('Prompt')

completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=4000)
st.text(completion.choices[0].text)
