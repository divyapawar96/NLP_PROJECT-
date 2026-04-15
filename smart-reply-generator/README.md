<div align="center">
  <h1>💡 Context-Aware Smart Reply Generator</h1>
  <p>An intelligent, beginner-friendly Natural Language Processing (NLP) tool to automatically generate context-aware smart replies for given user messages!</p>
</div>

---

## 🎯 About The Project

Ever wondered how platforms like Gmail and LinkedIn suggest those quick, relevant replies to incoming messages? This project emulates that exact functionality! 

It takes a user message, preprocesses the text, detects the underlying intent (e.g., Greetings, Meetings, Questions), and suggests **3 intelligent response options**.

### ✨ Features
- **🧠 Intent Detection:** Accurately classifies whether a message is an introduction, a meeting request, an apology, etc.
- **💬 Smart Replies:** Suggests 3 highly context-relevant replies based on the detected intent.
- **🛠️ NLP Preprocessing:** Handles text sanitization, tokenization, stop-word removal, and lemmatization using `spaCy`.
- **📊 Confidence Scores:** Calculates the system's certainty regarding the detected intent.
- **🎨 Beautiful UI:** Powered by Streamlit with an interactive layout and session history tracking.

---

## 💻 Tech Stack

- **Python:** Core programming language.
- **spaCy:** Advanced Natural Language Processing (NLP) functions.
- **scikit-learn:** Available for easily scaling up into machine learning models.
- **Streamlit:** Fast and beautiful interactive web applications.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites
Ensure you have Python (version `3.8+`) installed on your system.

### 2. Installation
Clone the repository and install the dependencies:

```bash
# Clone the repository
git clone https://github.com/divyapawar96/NLP_PROJECT-.git

# Navigate into the project folder
cd NLP_PROJECT-/smart-reply-generator

# Install all necessary Python libraries
pip install -r requirements.txt
```

### 3. Usage
Run the Streamlit app to start the UI:

```bash
streamlit run app.py
```

*This will open the application running on `http://localhost:8501` in your default web browser. On the first run, it will automatically install the spaCy language model requirement.*

---

## 📁 Project Structure

```text
smart-reply-generator/
│
├── app.py              # Main UI logic (Streamlit frontend)
├── model.py            # Intent classification and reply retrieval
├── utils.py            # NLP preprocessing helper functions (spaCy)
├── responses.json      # Mapping database for intents -> response lists
├── requirements.txt    # Python package dependencies
└── README.md           # Documentation (You are here!)
```

---

## 🖼️ Example Input & Output

**User Message:** *"Hey team, let's setup a sync tomorrow to discuss the new feature"*

* **Detected Intent:** `Meeting Request`
* **Confidence Score:** `80%`
* **Suggested Replies:**
  1. *Sure, let's schedule a meeting. What time works best for you? 📅*
  2. *I'd be happy to meet. Please share some available slots.*
  3. *Absolutely! Let me know your availability.*

---

## 🔮 Future Improvements
- [ ] Incorporate advanced `sklearn` TF-IDF Vectorizers for predictive Intent Detection.
- [ ] Connect with Transformer models (like BERT, RoBERTa) for contextual AI generation.
- [ ] Expand the `responses.json` corpus dynamically using external APIs.

---

## 👤 Author
**Divya Pawar** - [GitHub Profile](https://github.com/divyapawar96)

---
*If you liked this project, don't forget to ⭐ star the repository!*
