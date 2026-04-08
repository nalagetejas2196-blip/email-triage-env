from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmailInput(BaseModel):
    subject: str
    body: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(email: EmailInput):
    text = (email.subject + " " + email.body).lower()

    if "job" in text or "interview" in text:
        category = "Important"
    elif "offer" in text or "discount" in text:
        category = "Promotions"
    else:
        category = "General"

    return {"category": category}
