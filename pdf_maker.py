from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_resume_pdf(filename, name, title, email, phone, summary, bullets, skills):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, 
                                  textColor=colors.HexColor('#FF8C00'), spaceAfter=12)
    heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=16,
                                     textColor=colors.HexColor('#333'), spaceBefore=12, spaceAfter=6)
    
    story.append(Paragraph(name, title_style))
    story.append(Paragraph(title, styles['Heading2']))
    story.append(Paragraph(f"Email: {email} | Phone: {phone}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Professional Summary", heading_style))
    story.append(Paragraph(summary, styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Key Achievements", heading_style))
    for b in bullets:
        story.append(Paragraph(b.replace('•', '•'), styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Technical Skills", heading_style))
    story.append(Paragraph(", ".join(skills[:10]), styles['Normal']))
    
    doc.build(story)
    return filename