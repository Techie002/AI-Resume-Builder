import streamlit as st
from utils.portfolio_generator import generate_portfolio_html

def show():
    st.markdown("### 🎨 Portfolio Website Generator")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", key="p_name")
        title = st.text_input("Your Title", key="p_title")
    with col2:
        skills_input = st.text_area("Skills (comma separated)", key="p_skills", height=80)
        projects_input = st.text_area("Projects (one per line)", key="p_projects", height=100)
    
    if st.button("🌐 Generate Portfolio", use_container_width=True):
        if name:
            skills = [s.strip() for s in skills_input.split(',')] if skills_input else ["Python", "React", "AWS"]
            projects = [p.strip() for p in projects_input.split('\n') if p.strip()] if projects_input else ["E-commerce Platform", "AI Chatbot", "Mobile App"]
            
            html = generate_portfolio_html(name, title, skills, projects)
            st.session_state['portfolio_html'] = html
            st.success("✅ Portfolio generated!")
    
    if 'portfolio_html' in st.session_state:
        st.markdown("---")
        st.download_button("📥 Download Portfolio HTML", st.session_state['portfolio_html'], 
                          file_name=f"{name.lower().replace(' ', '_')}_portfolio.html", 
                          mime="text/html")
        st.components.v1.html(st.session_state['portfolio_html'], height=500)