import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="Jahanvi Dave | Data Science Portfolio", layout="wide")

# ---- HEADER ----
st.title("👩‍💻 Jahanvi Dave")
st.subheader("Aspiring Data Scientist | Python • SQL • ML • NLP")

# ---- CALL TO ACTION ----
st.success("💼 Actively exploring entry-level roles in Data Science and Machine Learning.")

st.write("Aspiring data scientist skilled in Python, SQL, and machine learning with hands-on experience in real-world projects involving NLP, clustering, and time series forecasting. Committed to continuous learning and contributing data-driven solutions in a professional environment.")

with st.container():
    st.write("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - 📍 **Preferred Location**: Europe, India (Bangalore, Pune, Mumbai, Ahmedabad), Remote  
        - 📧 **Email**: jahanvi08dave@gmail.com  
        - 📱 **Phone**: +91 81413 00801  
        - 🔗 [GitHub](https://github.com/Jahanvi3008)  
        - 🔗 [LinkedIn](https://www.linkedin.com/in/jahanvi-8271a7214)  
        """)
    with col2:
        st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=120)  # Placeholder logo

# ---- PROJECTS ----
st.write("---")
st.header("📊 Projects")

st.subheader("1. Credit Card Fraud Detection")
st.image("https://miro.medium.com/v2/resize:fit:1200/format:webp/1*rw3eRCdD9h9NqGnWTYeB1w.png", caption="ROC Curve Example", use_column_width=True)
st.markdown("""
Built a machine learning pipeline to detect fraudulent transactions using imbalanced data techniques like SMOTE.  
Achieved 91% precision using Random Forest and Logistic Regression.  
🔗 [View on GitHub](https://github.com/Jahanvi3008)
""")

st.subheader("2. Employee Attrition Prediction")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Shap_example.png/800px-Shap_example.png", caption="SHAP Summary Plot", use_column_width=True)
st.markdown("""
Used HR analytics and explainable models (SHAP + XGBoost) to predict employee turnover.  
Delivered clear insights for HR policy decisions and retention strategies.  
🔗 [View on GitHub](https://github.com/Jahanvi3008)
""")

st.subheader("3. Movie Recommendation System")
st.image("https://static.javatpoint.com/tutorial/recommendation-system/images/content-based-recommendation-system.png", caption="Content-Based Filtering Overview", use_column_width=True)
st.markdown("""
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
with open("Jahanvi_Resume.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Jahanvi_Dave_Data_Scientist_Resume.pdf",
        mime="application/pdf"
    )

# ---- CONTACT ----
st.write("---")
st.header("📬 Contact Me")
st.markdown("Whether you have something valuable to share, know someone hiring for data roles, or simply want to connect over common interests in data science, feel free to reach out!")
