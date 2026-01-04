from app.db.mongo import expenses_collection
from app.db.redis import redis_client

def add_expense(expense: dict):
    expenses_collection.insert_one(expense)
    # Clear cache for this user analytics
    redis_client.delete(f"analytics:{expense['user_id']}")

def get_expenses(user_id: str):
    return list(expenses_collection.find({"user_id": user_id}, {"_id": 0}))

def get_analytics(user_id: str):
    cache_key = f"analytics:{user_id}"
    if redis_client.exists(cache_key):
        return redis_client.get(cache_key)
    
    expenses = get_expenses(user_id)
    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    redis_client.set(cache_key, str(summary), ex=300)
    return summary
