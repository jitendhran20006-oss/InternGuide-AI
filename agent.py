import os
from dotenv import load_dotenv
from google import genai
from tools import search_internships
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=API_KEY) if API_KEY else None
SYSTEM="""You are InternGuide AI, a student-first internship and career guidance assistant. Give practical, clear advice. Explain opportunities, skill gaps, application steps, and preparation plans. Do not claim demo opportunities are real or verified."""
def run_agent(name,education,skills,location,query):
    opportunities=search_internships(skills,location)
    prompt=f"""{SYSTEM}\n\nStudent:\nName: {name}\nEducation: {education}\nSkills: {', '.join(skills)}\nLocation: {location}\nQuestion: {query}\n\nDemo opportunities:\n{opportunities}\n\nProvide:\n1. Relevant opportunities\n2. Why they match\n3. Skill gaps\n4. How to apply\n5. A practical preparation plan\n"""
    if client:
        response=client.models.generate_content(model="gemini-3.6-flash",contents=prompt)
        answer=response.text
    else:
        answer="Gemini API key is not configured. The demo opportunity matching still works. Add GEMINI_API_KEY to your .env file to enable AI guidance."
    return {"profile":{"name":name,"education":education,"skills":skills,"location":location},"opportunities":opportunities,"answer":answer}
