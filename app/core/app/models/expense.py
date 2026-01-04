from pydantic import BaseModel

class Expense(BaseModel):
    user_id: str
    amount: float
    category: str
    description: str = ""
    date: str
