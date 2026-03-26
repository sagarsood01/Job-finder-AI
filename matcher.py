def match_resume(resume_text, job_description):
    """Match resume against job description"""
    if not resume_text or not job_description:
        return "Missing resume or job description"
    
    # Simple keyword matching
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    
    matches = resume_words.intersection(job_words)
    
    if len(job_words) > 0:
        match_percentage = (len(matches) / len(job_words)) * 100
    else:
        match_percentage = 0
    
    result = f"""
    **Job Match Analysis:**
    - Match Score: {match_percentage:.1f}%
    - Matching Keywords: {', '.join(list(matches)[:10]) if matches else 'None'}
    - Status: {'✅ Good Match!' if match_percentage >= 50 else '⚠️ Partial Match' if match_percentage >= 20 else '❌ Low Match'}
    """
    return result
