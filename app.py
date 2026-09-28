from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from agent import run_agent
app=FastAPI(title="InternGuide AI")
templates=Jinja2Templates(directory="templates")
class StudentRequest(BaseModel):
    name:str
    education:str
    skills:str
    location:str
    query:str
@app.get("/",response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})
@app.post("/api/intern-guide")
def intern_guide(data:StudentRequest):
    skills=[s.strip() for s in data.skills.split(",") if s.strip()]
    return run_agent(data.name,data.education,skills,data.location,data.query)
@app.get("/health")
def health(): return {"status":"ok"}
if __name__=="__main__":
    import uvicorn
    uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)
