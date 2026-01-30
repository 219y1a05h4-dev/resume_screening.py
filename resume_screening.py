resumes = [
    "Python SQL communication",
    "Java leadership",
    "Python ML SQL"
]

required_skills = ["Python", "SQL"]

print("Shortlisted Candidates:")

for i, resume in enumerate(resumes):
    score = 0
    for skill in required_skills:
        if skill.lower() in resume.lower():
            score += 1
    
    if score >= 2:
        print(f"Candidate {i+1} shortlisted")
