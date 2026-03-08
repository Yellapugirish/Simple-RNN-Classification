# 🎬 IMDB Sentiment Analysis using SimpleRNN

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![License](https://img.shields.io/badge/License-Educational-green)

A **Deep Learning NLP project** that classifies movie reviews as **Positive** or **Negative** using a **Simple Recurrent Neural Network (SimpleRNN)** trained on the IMDB movie review dataset.

The project also includes a **Streamlit web application** where users can enter their own review and instantly see the predicted sentiment.

---

# 🚀 Project Demo

Example Input

```
I loved this movie. The acting and storyline were amazing.
```

Prediction

```
Sentiment: Positive
Prediction Score: 86%
```

Another Example

```
I hated this movie. It was boring and poorly written.
```

Prediction

```
Sentiment: Negative
Prediction Score: 15%
```

---

# 🧠 Model Architecture

The model processes sequential text data using a **SimpleRNN network**.

```
Text Input
     ↓
Embedding Layer
     ↓
SimpleRNN Layer
     ↓
Dense Layer (Sigmoid)
     ↓
Sentiment Prediction
```

### Layers Explained

**Embedding Layer**
- Converts words into dense vector representations

**SimpleRNN Layer**
- Processes the sequence of word embeddings

**Dense Layer**
- Outputs probability of Positive vs Negative sentiment

---

# 📊 Dataset

Dataset Used: **IMDB Movie Review Dataset**

Dataset Details

- 50,000 movie reviews
- Binary sentiment classification
- 25,000 training samples
- 25,000 testing samples
- Vocabulary limited to **10,000 most frequent words**

Source  
https://keras.io/api/datasets/imdb/

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
Python | Programming language |
TensorFlow / Keras | Deep learning framework |
SimpleRNN | Sequence modeling |
Streamlit | Web application interface |
NumPy | Numerical operations |

---

# 📂 Project Structure

```
Deep Learning NLP/
│
├── RNN Classification/
│   ├── main.py
│   ├── simplernn_imdb.h5
│   ├── simplernn.ipynb
│   ├── embedding.ipynb
│   ├── prediction.ipynb
│   └── README.md
│
├── ANN Classification/
│   └── (ANN project files)
│
└── requirements.txt
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run Streamlit App

Navigate to project folder

```
cd "RNN Classification"
```

Run the application

```
streamlit run main.py
```

Application will open in browser:

```
http://localhost:8501
```

---

# 📈 Model Limitations

Because the model uses **SimpleRNN**, it may sometimes struggle with:

- Very short sentences
- Complex grammar
- Negations such as "not bad"
- Sarcasm

Future models like **LSTM, GRU, or Transformers** handle these cases better.

---

# 🔮 Future Improvements

- Replace **SimpleRNN → LSTM**
- Add **GRU architecture**
- Implement **BERT transformer model**
- Improve preprocessing pipeline
- Deploy application to **Streamlit Cloud**
- Add model explainability tools

---

# 📜 License

This project is developed for **educational and research purposes**.
