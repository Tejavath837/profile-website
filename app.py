import streamlit as st

st.set_page_config(page_title="Rohith", page_icon="👨‍💻")

# ── SIDEBAR ───────────────────────────────────
with st.sidebar:
    st.header("Navigation")
    st.markdown("About Me")
    st.markdown("Skills")
    st.markdown("Projects")
    st.markdown("Contact")
    st.divider()

st.title("👨‍💻 Hi, I'm Rohith")
st.write("Python & ML Student | Interested in Cloud Computing & Networking")
st.divider()

st.header("About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://media.licdn.com/dms/image/v2/D4E03AQH4cL5n3X9r5Q/profile-displayphoto-crop_800_800/B4EZl0p_ZVHgAM-/0/1758598790296?e=1785974400&v=beta&t=-I1kyXrdMTMjKA8Et5tIu17LSIECm6QgT69Oip5kym4",
             width=150, caption="Rohith")

with col2:
    st.write("""
    I'm a student from khammam, Telangana currently completing
    the Enduro'26 Python and Machine Learning.

    My main interest is in cloud computing and networking.
    Through this course I learned Python, data analysis, and how
    to build and deploy machine learning models.

    I built a Crop Recommendation System.
    """)

st.divider()

st.header("Skills")
st.write("Here are the skills I picked up during Enduro'26:")

st.write("**Python**")
st.progress(70)

st.write("**Pandas**")
st.progress(60)

st.write("**Scikit-Learn**")
st.progress(60)

st.write("**Streamlit**")
st.progress(65)

st.write("**GitHub**")
st.progress(50)

st.divider()

st.header("Projects")

with st.expander("🌾 Crop Recommendation System"):
    st.write("Built an ML model that recommends the best crop based on soil and climate inputs.")
    st.write("Tech:  Python, Scikit-Learn, Streamlit, joblib")
    st.write("Accuracy:  99.32% using Random Forest")

with st.expander("📊 EDA Dashboard"):
    st.write("Created distribution plots and a correlation heatmap for the crop dataset.")
    st.write("Tech:   Python, Pandas, Matplotlib, Seaborn")
    st.write("Finding:   Humidity was the strongest predictor — clear bimodal distribution")

with st.expander("👤 Developer Profile Page"):
    st.write("This page! Built as Mini-Project 4 for Enduro'26.")
    st.write("Tech:  Python, Streamlit")
    st.write("Learning:  How Streamlit reruns the script on every interaction")

st.divider()

st.header("Contact")

st.link_button("GitHub","https://github.com/Tejavath837")
st.link_button("LinkedIn","https://linkedin.com/in/rohith-tejavath-923093376")
st.link_button("Email","mailto:rohithtejavath837@gmail.com")

st.divider()