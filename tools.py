INTERNSHIPS = [
    {"title":"Python AI/ML Intern","company":"Demo AI Labs","location":"Remote","skills":["python","machine learning","pandas","scikit-learn"],"link":"https://example.com"},
    {"title":"Data Science Intern","company":"Demo Data Labs","location":"Remote","skills":["python","pandas","numpy","data science"],"link":"https://example.com"},
    {"title":"Backend Python Intern","company":"Demo Software","location":"Hyderabad","skills":["python","fastapi","api","sql"],"link":"https://example.com"},
    {"title":"Machine Learning Intern","company":"Demo ML Labs","location":"Remote","skills":["python","machine learning","numpy","scikit-learn"],"link":"https://example.com"}
]

def search_internships(skills, location=""):
    user_skills = {s.strip().lower() for s in skills if s.strip()}
    results=[]
    for job in INTERNSHIPS:
        job_skills={s.lower() for s in job["skills"]}
        matched=user_skills & job_skills
        score=round((len(matched)/max(len(job_skills),1))*100)
        results.append({**job,"match_percentage":score,"matched_skills":sorted(matched)})
    return sorted(results,key=lambda x:x["match_percentage"],reverse=True)
