# 🤖 TechAssist — AI-Powered Technical Support Chatbot

TechAssist is an NLP-based technical support chatbot that helps users find solutions to common technical problems.

The chatbot uses **Natural Language Processing (NLP)**, **TF-IDF vectorization**, and **Cosine Similarity** to understand a user's question and retrieve the most relevant answer from a structured FAQ knowledge base.

---

🔗 **Live Demo:** 
https://techassist-cl88.onrender.com

🔗 **GitHub Repository:**  
https://github.com/tanvi-jpeg/TechAssist

---

## 📌 Features

- 💬 Interactive chatbot interface
- 🧠 NLP-based question preprocessing
- 🔤 Lowercase and punctuation normalization
- 🛑 Stopword removal using NLTK
- 🌱 Word lemmatization
- 📊 TF-IDF text vectorization
- 🔍 Cosine similarity-based FAQ matching
- 🎯 Similarity threshold for handling unknown questions
- 📚 Categorized technical-support FAQ knowledge base
- ⚡ Flask REST API
- 🎨 Responsive dark-themed UI
- ⌨️ Enter key support for sending messages
- 👋 Exit command support (`quit`, `exit`, `bye`, `goodbye`)

---

## 🧠 How It Works

TechAssist follows a retrieval-based NLP approach.


User Question
      ↓
Text Preprocessing
      ↓
Stopword Removal
      ↓
Lemmatization
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Best FAQ Match
      ↓
Similarity Threshold Check
      ↓
Return Relevant Answer
