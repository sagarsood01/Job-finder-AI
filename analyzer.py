def analyze_resume(text):
    """Analyze resume text and extract key information"""
    if not text:
        return "No text to analyze"
    
    skills = extract_skills(text)
    experience = extract_experience(text)
    
    analysis = f"""
    **Resume Summary:**
    - Skills found: {', '.join(skills) if skills else 'None detected'}
    - Experience detected: {experience if experience else 'None detected'}
    """
    return analysis

def extract_skills(text):
    """Extract common skills from resume"""
    common_skills = ['python', 'java', 'javascript', 'sql', 'aws', 'docker', 'git', 'react', 'node']
    found_skills = [skill for skill in common_skills if skill.lower() in text.lower()]
    return found_skills

def extract_experience(text):
    """Extract years of experience from resume"""
    import re
    years = re.findall(r'(\d{1,2})\s*\+?\s*years?', text.lower())
    if years:
        return f"{max(years)} years"
    return None
