# 📦 Flipkart Customer Support AI Assistant

An end-to-end Machine Learning project that classifies Flipkart customer complaints into predefined categories using Natural Language Processing (NLP). This project includes:

- Data cleaning and preprocessing  
- Text vectorization using TF-IDF  
- Model training with Logistic Regression  
- Model evaluation  
- A user-friendly **Streamlit GUI** to interact with the model in real time

---

## 🚀 Demo

Use the Streamlit app to input a customer complaint (e.g., _"My order hasn't arrived yet"_) and the model will predict the issue category.

---

## 🧠 Tech Stack

| Tool / Library        | Purpose                              |
|-----------------------|--------------------------------------|
| `Python`              | Programming language                 |
| `Pandas`              | Data handling                        |
| `Scikit-learn`        | Machine learning                     |
| `Matplotlib & Seaborn`| Data visualization                   |
| `TF-IDF Vectorizer`   | Text vectorization                   |
| `Logistic Regression` | Classification model                 |
| `Streamlit`           | Frontend GUI                         |

---

## 📁 Project Structure

Flipkart-Customer-Support-AI-Assistant/
├── Flipkart_Customer_Support_Project.ipynb # Jupyter Notebook version
├── flipkart_app.py # Streamlit app file
├── Customer_support_data.csv # Dataset
├── requirements.txt # List of dependencies
└── README.md # This file

yaml
Copy
Edit

---

## 📊 Model Performance

Achieved high accuracy on the test set using logistic regression with TF-IDF features. Includes a classification report with precision, recall, and F1-score.

---

## ⚙️ How to Run the Project

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/Flipkart-Customer-Support-AI-Assistant.git
cd Flipkart-Customer-Support-AI-Assistant
✅ 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 3. Run the Streamlit App
bash
Copy
Edit
streamlit run flipkart_app.py
📝 Sample Input
"I want to return my damaged phone."

✅ Output:
Predicted Issue Category: Return or Replacement

📂 Dataset
The project uses a CSV file containing Flipkart customer remarks and manually labeled issue categories.

💡 Future Improvements
Add more advanced NLP models (e.g., BERT)

Use a larger dataset for training

Save and load trained model with joblib or pickle

Export predictions to Excel or CSV

Add authentication to the Streamlit app

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
This project is inspired by real-world customer support scenarios at e-commerce platforms like Flipkart and Amazon.


