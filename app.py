import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
vectorizer = joblib.load(os.path.join(base_dir, "tfidf_vectorizer.pkl"))
model = joblib.load(os.path.join(base_dir, "logistic_model.pkl"))
label_map = joblib.load(os.path.join(base_dir, "label_map.pkl"))

st.markdown("<h1 style='text-align: center; color: #e91e63;'>🔥 Spam Detector 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Drop your message below and let's see if it's spam or ham 🕵️‍♂️</p>", unsafe_allow_html=True)


def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([char for char in text if not char.isdigit()])
    words = text.split()
    words = [word for word in words if not (word.startswith('http') or word.startswith('www.'))]
    text = ' '.join(words)
    text = ''.join([char for char in text if char.isascii()])
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    cleaned = [word for word in tokens if word not in stop_words]
    return ' '.join(cleaned)


user_input = st.text_area("Enter your message here 👇", height=150)

if st.button("Analyze 🔍"):
    if user_input.strip() == "":
        st.warning("Come on bro, type something first 😅")
    else:
        cleaned_text = preprocess(user_input)
        vec = vectorizer.transform([cleaned_text])
        pred = model.predict(vec)[0]
        result = "Spam 🚫" if pred == 1 else "Ham ✅"

        st.markdown(f"<h3 style='text-align: center; color: #4caf50;'>Result: {result}</h3>", unsafe_allow_html=True)

        if pred == 1:
            st.image("https://media.giphy.com/media/hXxKtPmspCv4U/giphy.gif", caption="This looks suspicious, bro 👀", use_column_width=True)
        else:
            st.image("https://media.giphy.com/media/xUOxfgvWUmq3fTjdzK/giphy.gif", caption="Chill, you're safe 😎", use_column_width=True)
