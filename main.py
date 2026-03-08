import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st
import re

## Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

## Load the pre-trained model with ReLU activation
@st.cache_resource
def load_my_model():
    return load_model("simplernn_imdb.h5")

model = load_my_model()

## Function to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

## Function to preprocess user input
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()

    encoded_review = []
    for word in words:
        idx = word_index.get(word)
        if idx is not None and idx < 10000:
            encoded_review.append(idx + 3)
        else:
            encoded_review.append(2)

    padded_review = sequence.pad_sequences([encoded_review], maxlen=200)
    return padded_review

## Streamlit app
import streamlit as st

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment (positive or negative).")

# User input
user_input = st.text_area("Enter your movie review:")

if st.button("Predict"):
    preprocessed_input = preprocess_text(user_input)

    ## Make prediction
    prediction = model.predict(preprocessed_input)
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    ## Display the result
    st.write(f"Sentiment: {sentiment}")
    st.write(f"Prediction Score: {prediction[0][0]:.4f}")
else:
    st.write("Please enter a movie review and click 'Predict' to see the sentiment analysis result.")
