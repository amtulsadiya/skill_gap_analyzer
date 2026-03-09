import pdfplumber
import nltk
import re
from nltk.corpus import stopwords

def extract_resume_text(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text
nltk.download('stopwords')

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]', '', text)

    words = text.split()

    words = [w for w in words if w not in stopwords.words("english")]

    return " ".join(words)

resume = extract_resume_text("resumes/resume.pdf")

clean_resume = clean_text(resume)

print(clean_resume)