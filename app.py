import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="Jahanvi Dave | Data Science Portfolio", layout="wide")

# ---- CUSTOM THEME ----
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #0f1117, #1c1f2e);
        color: #f1f1f1;
    }
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #ff8a65;
    }
    .stDownloadButton>button {
        background-color: #0077cc;
        color: white;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6em 1.2em;
        transition: background-color 0.3s ease;
    }
    .stDownloadButton>button:hover {
        background-color: #3399ff;
    }
    h1, h2, h3 {
        color: #ffcc00;
    }
    a {
        color: #66d9ef;
        font-weight: 600;
    }
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.title("👩‍💻 Jahanvi Dave")
st.subheader("Aspiring Data Scientist | Python • SQL • ML • NLP")

# ---- CALL TO ACTION ----
st.success("💼 Actively exploring entry-level roles in Data Science and Machine Learning.")

st.write("Aspiring data scientist skilled in Python, SQL, and machine learning with hands-on experience in real-world projects involving NLP, clustering, and time series forecasting. Committed to continuous learning and contributing data-driven solutions in a professional environment.")

# ---- PROJECTS ----
st.write("---")
st.header("📊 Projects")

st.subheader("1. Credit Card Fraud Detection 🔐")
st.markdown("""
📌 **Key Snippet:**
```python
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
preds = clf.predict(X_test)
```
📈 **Metric**: 91% Precision on Imbalanced Data

Built a machine learning pipeline to detect fraudulent transactions using imbalanced data techniques like SMOTE.  
Achieved 91% precision using Random Forest and Logistic Regression.  
🔗 [View on GitHub](https://github.com/Jahanvi3008)
""")

st.subheader("2. Employee Attrition Prediction 🧑‍💼")
st.markdown("""
📌 **Key Snippet:**
```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values, X)
```
📉 **Insight**: SHAP reveals Work-Life Balance as top factor

Used HR analytics and explainable models (SHAP + XGBoost) to predict employee turnover.  
Delivered clear insights for HR policy decisions and retention strategies.  
🔗 [View on GitHub](https://github.com/Jahanvi3008)
""")

st.subheader("3. Movie Recommendation System 🎬")
st.markdown("""
📌 **Key Snippet:**
```python
from sklearn.metrics.pairwise import cosine_similarity
sim_scores = cosine_similarity(tfidf_matrix)
recommendations = get_top_movies(sim_scores)
```
🎯 **Use Case**: Personalized movie suggestions based on genre & plot

Built a content-based recommender system using TF-IDF vectorization and cosine similarity.  
Suggested movies based on genres, descriptions, and cast.  
🔗 [View on GitHub](https://github.com/Jahanvi3008)
""")

# ---- ABOUT ----
st.write("---")
st.header("👋 About Me")
st.write("""
I'm a former iOS developer turned data science enthusiast. After gaining software experience, I transitioned to the data field where I could combine my analytical mindset with real-world problem solving.

I gained global exposure and sharpened my focus on building a career grounded in data, learning, and impact. I'm currently exploring opportunities to begin my career in the data science field, where I can apply my skills and grow professionally.

I love asking questions, cleaning messy data, and turning models into actionable insights.
""")

# ---- CERTIFICATIONS ----
st.write("---")
st.header("📜 Certifications")
st.markdown("""
- ✅ AI-Data Scientist v3.0 – NASSCOM  
- ✅ Tools for Data Science – Coursera  
- ✅ Data Science Methodology – Coursera  
""")

# ---- RESUME DOWNLOAD ----
st.write("---")
st.header("📄 Resume")

st.download_button(
    label="📄 Download My Resume",
    data="https://raw.githubusercontent.com/Jahanvi3008/portfolio-assets/main/Jahanvi_CV_CoverLetter.pdf",
    file_name="Jahanvi_CV_CoverLetter.pdf",
    mime="application/pdf"
)
        label="📄 Download My Resume",
        data=file,
        file_name="Jahanvi_CV_CoverLetter.pdf",
        mime="application/pdf"
    )



# ---- CONTACT ----
st.write("---")
st.header("📬 Contact Me")
st.markdown("Whether you have something valuable to share, know someone hiring for data roles, or simply want to connect over common interests in data science, feel free to reach out!")
