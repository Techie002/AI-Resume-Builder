import streamlit as st
from utils.api_client import call_ai
from utils.resume_generator import generate_resume_summary, format_achievements
from utils.pdf_maker import create_resume_pdf

def show():
    st.markdown("### 📝 AI Resume Builder")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", key="r_name")
        title = st.text_input("Job Title", key="r_title")
        email = st.text_input("Email", key="r_email")
        phone = st.text_input("Phone", key="r_phone")
    with col2:
        experience = st.selectbox("Experience", ["Fresher", "0-2", "3-5", "6-9", "10+"], key="r_exp")
        industry = st.selectbox("Industry", ["Technology", "Finance", "Healthcare", "Marketing"], key="r_ind")
        skills = st.text_area("Skills (comma separated)", key="r_skills", height=80)
        achievements = st.text_area("Your Achievements", key="r_achievements", height=80)
    
    if st.button("🚀 Generate Resume", use_container_width=True):
        if name:
            with st.spinner("AI is creating your resume..."):
                summary = generate_resume_summary(name, title, experience, industry, skills, achievements, call_ai)
                if not summary:
                    summary = f"Dynamic {title} with {experience} years experience in {industry}."
                
                bullets = format_achievements(achievements, call_ai)
                if not bullets:
                    bullets = ["• Led team to 30% increase", "• Delivered 5 projects ahead of schedule"]
                
                st.session_state['resume_data'] = {
                    'name': name, 'title': title, 'email': email, 'phone': phone,
                    'summary': summary, 'skills': [s.strip() for s in skills.split(',')] if skills else ["Python"],
                    'bullets': bullets
                }
                st.success("✅ Resume generated!")
                st.balloons()
    
    if 'resume_data' in st.session_state:
        data = st.session_state['resume_data']
        st.markdown("---")
        st.markdown(f"### {data['name']}")
        st.markdown(f"**{data['title']}** | 📧 {data['email']} | 📞 {data['phone']}")
        st.info(data['summary'])
        for b in data['bullets']:
            st.markdown(b)
        
        if st.button("📥 Download PDF"):
            filename = create_resume_pdf(f"resume_{data['name']}.pdf", data['name'], data['title'], 
                                          data['email'], data['phone'], data['summary'], data['bullets'], data['skills'])
            with open(filename, "rb") as f:
                st.download_button("Download PDF", f, file_name=filename)