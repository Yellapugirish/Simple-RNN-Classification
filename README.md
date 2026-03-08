# SimpleRNN IMDB Sentiment Analysis (Streamlit App)

## Project Overview
This project is a Sentiment Analysis web application built using **TensorFlow, SimpleRNN, and Streamlit**.

The model predicts whether a movie review is **Positive** or **Negative** based on user input text.

The model is trained on the **IMDB Movie Review Dataset**, which contains 50,000 labeled movie reviews for binary sentiment classification.

Users can enter any movie review in the web interface and instantly receive the predicted sentiment with confidence score.

---

## Tech Stack

- Python
- TensorFlow / Keras
- SimpleRNN
- Streamlit
- NumPy
- IMDB Dataset

---

## Project Structure

```
RNN Classification/
│
├── main.py                 # Streamlit application
├── simplernn_imdb.h5       # Trained SimpleRNN model
├── simplernn.ipynb         # Model training notebook
├── embedding.ipynb         # Word embedding exploration
├── prediction.ipynb        # Model testing notebook
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation
```

---

## Model Architecture

The model uses a **Simple Recurrent Neural Network (SimpleRNN)** to process sequential text data.

Architecture:

```
Embedding Layer
        ↓
SimpleRNN Layer
        ↓
Dense Layer (Sigmoid Activation)
```

- **Embedding Layer** converts words into dense vector representations.
- **SimpleRNN Layer** processes sequential text information.
- **Dense Layer** outputs the probability of positive or negative sentiment.

---

## Dataset

Dataset used:

**IMDB Movie Review Dataset**

Details:
- 50,000 movie reviews
- Binary sentiment labels (Positive / Negative)
- Vocabulary limited to the **top 10,000 most frequent words**
- Reviews padded to fixed sequence length

---

## Example Prediction

Input:

```
I loved this movie. The acting and storyline were amazing.
```

Output:

```
Sentiment: Positive
Prediction Score: 86%
```

Another Example:

```
I hated this movie. It was boring and poorly written.
```

Output:

```
Sentiment: Negative
Prediction Score: 15%
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

---

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the Streamlit App

```
streamlit run main.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Deployment

This application can be deployed using:

- Streamlit Cloud
- HuggingFace Spaces
- AWS / GCP / Azure
- Docker

---

## Future Improvements

- Upgrade model from **SimpleRNN → LSTM / GRU**
- Improve text preprocessing
- Add visualization of prediction confidence
- Use transformer-based models such as **BERT**
- Deploy with CI/CD pipeline

---


## License

This project is developed for **educational and learning purposes**.
