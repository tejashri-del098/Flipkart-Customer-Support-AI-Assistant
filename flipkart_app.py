# flipkart_app.py

import pandas as pd
import re
import string
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Customer_support_data.csv")
    df = df[['Customer Remarks', 'category']]
    df.dropna(inplace=True)
    df = df[df['Customer Remarks'].str.strip() != '']
    return df

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.strip()
    return text

# Load and preprocess
df = load_data()
df['cleaned'] = df['Customer Remarks'].apply(clean_text)

# Vectorize
tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
X = tfidf.fit_transform(df['cleaned'])
y = df['category']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Streamlit UI
st.title("🤖 Flipkart Customer Support AI Assistant")
st.markdown("Classify customer messages into issue categories.")

user_input = st.text_area("📝 Enter a customer remark:")
if st.button("Predict Category"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        prediction = model.predict(vectorized)
        st.success(f"📌 Predicted Category: **{prediction[0]}**")

