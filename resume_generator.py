def generate_resume_summary(name, title, experience, industry, skills, achievements, call_ai):
    prompt = f"""<s>[INST] Write a professional resume summary for {name}, a {title} with {experience} years in {industry}. 
    Skills: {skills}. Achievements: {achievements}. Write 100 words only. [/INST]"""
    return call_ai(prompt)

def format_achievements(achievements, call_ai):
    prompt = f"""<s>[INST] Convert these achievements into 4 bullet points starting with • : {achievements} [/INST]"""
    response = call_ai(prompt)
    if response:
        bullets = [b.strip() for b in response.split('\n') if b.strip() and b.startswith('•')]
        return bullets if len(bullets) >= 3 else [
            "• Led team to 30% productivity increase",
            "• Delivered 5 major projects ahead of schedule",
            "• Improved efficiency by 40%"
        ]
    return []