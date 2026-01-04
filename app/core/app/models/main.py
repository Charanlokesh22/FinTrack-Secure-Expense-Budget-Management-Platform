from fastapi import FastAPI
from app.routes.expense_routes import router as expense_router

app = FastAPI(title="FinTrack API")

app.include_router(expense_router)

@app.get("/")
def health_check():
    return {"status": "FinTrack backend running"}
