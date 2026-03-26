import streamlit as st
from ai_engine import analyze_with_ai
from pdf_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Analyzer", layout="centered", page_icon="🦅")

# CUSTOM CSS CODE
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #0A66C2;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    margin-bottom: 20px;
}

.nav-title {
    font-size: 22px;
    font-weight: bold;
}

.profile-icon {
    font-size: 24px;
}



/* Hero Section */
.hero {
    text-align: center;
    margin-top: 40px;
}

.hero h1 {
    font-size: 48px;
}

.hero p {
    color: #94a3b8;
    font-size: 18px;
}

/* Upload Box */
.upload-box {
    border: 2px dashed #3b82f6;
    padding: 40px;
    text-align: center;
    border-radius: 12px;
}

/* Input box */
textarea {
    border-radius: 12px !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #9333ea);
    color: white;
    border-radius: 10px;
    padding: 12px 25px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px #3b82f6;
}

/* Chips */
.chip {
    display: inline-block;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 20px;
    background-color: #1e293b;
}

.chip.red {
    background-color: #7f1d1d;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <div class="nav-title">🚀 AI Resume Analyzer</div>
    <div class="profile-icon">👤</div>
</div>
""", unsafe_allow_html=True)

# st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("", ["Home", "Dashboard", "History"])

st.sidebar.markdown("---")
st.sidebar.write("👤 **User:** Sagar")
st.sidebar.write("💼 Plan: Free")

if menu == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Job Finder AI</h1>
        <p>Boost your chances with AI-powered resume insights 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- UPLOAD ----------------
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📂 Drag & Drop Resume", type=["pdf", "doc", "docx"])
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- JOB DESCRIPTION ----------------
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    job_desc = st.text_area("📝 Paste Job Description")
    st.markdown('</div>', unsafe_allow_html=True)


if st.button("🔍 Analyze Resume"):

    if uploaded_file is None or job_desc.strip() == "":
        st.warning("⚠️ Please upload resume and enter job description")

    else:
        with st.spinner("AI is analyzing your resume... 🤖"):
            
            text = extract_text_from_pdf(uploaded_file)

            result = analyze_with_ai(text, job_desc)

        score = result["score"]
        matched = result["matched_skills"]
        missing = result["missing_skills"]
        suggestions = result["suggestions"]

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("📊 Match Score")
        st.progress(score / 100)
        st.write(f"### {score}% Match")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("🧠 Matched Skills")
        for skill in matched:
            st.markdown(f'<span class="chip">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("❌ Missing Skills")
        for skill in missing:
            st.markdown(f'<span class="chip red">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # -------- SUGGESTIONS --------
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.write(f"👉 {s}")
        st.markdown('</div>', unsafe_allow_html=True)
     


        # ---------------- RESULTS ----------------
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            st.subheader("📄 Resume Analysis")
            st.write("✔️ Strong experience section")
            st.write("✔️ Good formatting")
            st.write("⚠️ Improve keywords")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            st.subheader("📊 Match Score")
            st.progress(75)
            st.write("75% Match with Job Description")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("🧠 Skills Match")
        skills = ["Python", "Machine Learning", "SQL"]
        for skill in skills:
            st.markdown(f'<span class="chip">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("❌ Missing Skills")
        missing = ["Deep Learning", "NLP", "Docker"]
        for skill in missing:
            st.markdown(f'<span class="chip red">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("💡 Suggestions")
        st.write("👉 Add more relevant keywords")
        st.write("👉 Include measurable achievements")
        st.write("👉 Optimize for ATS systems")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Dashboard":
    st.title("📊 Dashboard")
    st.write("Coming Soon...")

elif menu == "History":
    st.title("📜 History")
    st.write("No past records found.")