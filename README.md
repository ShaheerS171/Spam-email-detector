<h1 align="center">📬 Spam Message Detector</h1>

<p align="center">
  🔍 A clean and simple ML project that detects spam messages using Logistic Regression and TF-IDF. Wrapped in a sweet Streamlit UI.
</p>

---

## 🚀 Overview

This is a **Spam Detection Web App** built using traditional Machine Learning. It takes in a text message and tells you if it's **Spam** or **Not Spam**, using a model trained on real-world SMS data (plus some spicy additions from me 😏).

---

## 🧠 What I Did

- 📄 Loaded and cleaned `spam.csv` dataset  
- 🔁 Mapped `spam` and `ham` to numerical values  
- ➕ Added 100 real-like spam messages to make the model sharper  
- 🧪 Vectorized text using **TF-IDF**  
- 🤖 Trained a **Logistic Regression** classifier  
- 💾 Saved the model + vectorizer using `joblib`  
- 🌐 Built a user-friendly interface with **Streamlit**

---

## 📷 App Preview

<p align="center">
  <img src="https://i.imgur.com/fakeimg.png" alt="App Screenshot" width="500"/>
</p>

---

## 🛠️ Tech Stack

| Tool         | Use Case                     |
|--------------|------------------------------|
| Python       | Core Language                |
| Pandas       | Data Manipulation            |
| Scikit-learn | ML Model & TF-IDF Vectorizer |
| Streamlit    | Web Interface                |
| Joblib       | Saving Model & Vectorizer    |

---

## 🧪 Try It Out

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open in your browser and test messages like:

```
"WINNER! You've won a free cruise. Call now!"
"Hey, can we reschedule our meeting?"
```

---

## 📁 Folder Structure

```
📦 NLP-Spam-Detector/
├── app.py                 # Main Streamlit App
├── spam.csv               # Dataset
├── logistic_model.pkl     # Trained ML Model
├── tfidf_vectorizer.pkl   # TF-IDF Vectorizer
├── requirements.txt       # Dependencies
└── README.md              # You're here
```

---

## 🚧 Future Upgrades

- [ ] Add Deep Learning Model (LSTM or BERT)
- [ ] Clean UI makeover with animations
- [ ] Add SMS/email integration
- [ ] Save prediction logs for review

---

## 🙌 Final Words

This project’s been a fun ride — old school ML still got some fire 🔥  
Clean results, fast predictions, and a setup anyone can run.

> Built with ☕, 💻, and way too many spam texts 😅

---

<p align="center"><b>Ready to catch some spam? 🚨</b></p>
