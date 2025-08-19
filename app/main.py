from fastapi import FastAPI
from .schemas import AnalysisRequest, AnalysisResponse
from .services import analysis_service

app = FastAPI(
    title="Career Mentor",
    description="An API to analyze resumes against job descriptions using AI.",
    version="0.1.0"
)

@app.post("/analyze", response_model=AnalysisResponse, tags=["Analysis"])
def analyze_context(analysis_request: AnalysisRequest):
    analysis_text = analysis_service.generate_analysis(
        resume_text=analysis_request.resume_text,
        job_description=analysis_request.job_description
    )
    return {"analysis": analysis_text}

@app.get("/", tags=["API Check"])
def read_root():
    return {"status": "API is running!"}