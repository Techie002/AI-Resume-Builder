def generate_portfolio_html(name, title, skills, projects):
    """Generate HTML portfolio"""
    skills_html = "".join([f'<span class="skill">{s}</span>' for s in skills[:8]])
    projects_html = "".join([f'<div class="project"><h3>{p}</h3><p>Project description and impact</p></div>' for p in projects[:4]])
    
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{name} - Portfolio</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .header {{ background: white; border-radius: 20px; padding: 40px; text-align: center; margin-bottom: 30px; }}
        .section {{ background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; }}
        .skill {{ display: inline-block; background: linear-gradient(90deg, #FFD700, #FFA500); padding: 8px 20px; border-radius: 25px; margin: 5px; font-weight: bold; }}
        .project {{ background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 15px; }}
        h1 {{ color: #667eea; }}
        .gradient-text {{ background: linear-gradient(120deg, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="gradient-text">{name}</h1>
            <h2>{title}</h2>
            <p>Building amazing things with code</p>
        </div>
        
        <div class="section">
            <h2>🛠️ Technical Skills</h2>
            <div>{skills_html}</div>
        </div>
        
        <div class="section">
            <h2>🚀 Featured Projects</h2>
            {projects_html}
        </div>
        
        <div class="section">
            <h2>📫 Contact</h2>
            <p>Email: {name.lower().replace(' ', '.')}@example.com</p>
            <p>GitHub: github.com/{name.lower().replace(' ', '')}</p>
            <p>LinkedIn: linkedin.com/in/{name.lower().replace(' ', '')}</p>
        </div>
    </div>
</body>
</html>
    """