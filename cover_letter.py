def generate_cover_letter(job_title, company, job_desc, tone, skills, call_ai):
    tone_instructions = {
        "Formal": "Use professional, respectful language",
        "Enthusiastic": "Show excitement and passion",
        "Confident": "Focus on achievements and capabilities"
    }
    
    prompt = f"""<s>[INST] Write a {tone} cover letter for {job_title} position at {company}.
    
Job Description: {job_desc[:300]}
My Key Skills: {', '.join(skills)}

{ tone_instructions.get(tone, "Be professional") }

Write a complete cover letter with: opening, body paragraphs, closing. 200-250 words. [/INST]"""
    
    return call_ai(prompt)