# AI Resume Builder

Resume building sucks. Simple.

Every time I apply for a job, I spend 2-3 hours formatting the same content. One version for Google, one for Amazon, one for some startup that never replied. 

Canva templates cost money after 3 downloads. MS Word formatting breaks when you open it on a different laptop. LaTeX is overkill.

So  let AI do it. Works 80% of the time. Good enough.

## What it does

You enter your name, skills, achievements. AI writes your resume. Download in HTML, PDF, Word, or TXT.

| Feature | Works? |
|---------|--------|
| Resume generation | Yes |
| 3 templates (Classic/Professional/Modern) | Yes |
| PDF download | Mostly yes (sometimes text cuts off) |
| Word download | Yes somehow |
| Cover letter | Yes but edit once |
| Portfolio website | Yes, HTML file |
| Cold messages | Yes for LinkedIn DMs |


## Tech stack (what I used)


| Python | effective for ai|
| Streamlit | Fastest way to build web apps |
| Grok API | Free AI credits |
| ReportLab | PDF generation (painful) |
| python-docx | Word export (easy) |

## ✅ Pros (What's actually good)

| Pro | Why I like it |
|-----|---------------|
| **100% Free** | No credit card. No subscription. No "pay to download" |
| **Works offline** | Mock mode runs without internet |
| **3 Templates** | Classic, Professional, Modern. Pick your vibe |
| **4 Export formats** | HTML, PDF, Word, TXT. Share anywhere |
| **Fast enough** | 15-20 seconds approx. |
| **Editable** | Preview and edit before download |
| **No signup required** | Just open and use |
| **ATS friendly** | AI adds keywords automatically |
| **Portfolio included** | One click portfolio website |


## ❌ Cons (Being honest)

| Con | Why it's a problem |
|-----|---------------------|
| **API needs internet** | Real AI won't work without connection |
| **Network issues** | Grok/Hugging Face blocked in some colleges/offices |
| **No mobile app** | Web only. Use laptop |
| **No database** | Can't save your resumes. Download immediately |
| **Slow sometimes** | API takes 10-20 seconds |
| **PDF formatting** | Long bullet points get cut sometimes |
| **Session resets** | Refresh the page = lose your data |
| **Basic UI** | Streamlit limitations. Not a fancy  |
| **No multi-language** | English only for now |

## Future Scope 

- **Save progress** - Browser storage so data doesn't disappear on refresh
- **Dark mode** - Because 2024
- **Better PDF** - Fix the text cutting issue
- **Mobile friendly** - Make it work on phones properly
- **LinkedIn import** - Auto-fill your profile with one click
- **5 new templates** - More design options
- **ATS score** - Check if your resume passes automated filters
- **PNG export** - Share directly on social media
- **User accounts** - Save multiple resumes
- **Cloud sync** - Access from anywhere

## How to run
   
 1. Install Python 3.10 or 3.11

 2. Clone and install

### bash
git clone https://github.com/username/AI-Resume-Builder.git
cd AI-Resume-Builder
pip install -r requirements.txt