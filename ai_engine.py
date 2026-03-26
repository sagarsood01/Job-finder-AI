import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key="AIzaSyB3TAqaseaO1euprtG9Oe1W8-uav_krlc8")

model = genai.GenerativeModel("gemini-2.5-flash")

from google import genai

client = genai.Client(api_key="AIzaSyB3TAqaseaO1euprtG9Oe1W8-uav_krlc8")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
def analyze_with_ai(resume_text, job_desc):

    prompt = f"""
    Analyze the resume and job description.

    Return ONLY valid JSON in this format:

    {{
        "score": number (0-100),
        "matched_skills": [list],
        "missing_skills": [list],
        "suggestions": [list]
    }}

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = model.generate_content(prompt)

    try:
        data = json.loads(response.text)
    except:
    
        data = {
            "score": 50,
            "matched_skills": [],
            "missing_skills": [],
            "suggestions": ["AI response parsing failed"]
        }

    return data