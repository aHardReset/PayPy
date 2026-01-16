from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
import database
import repository

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database on startup
    database.init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    nickname: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Hello World from Python Backend!"}

@app.post("/api/login")
def login(request: LoginRequest):
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, legal_name, nickname, country_id
        FROM users
        WHERE nickname = ? AND password = ?
    """, (request.nickname, request.password))

    user = cursor.fetchone()
    conn.close()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "id": user[0],
        "legal_name": user[1],
        "nickname": user[2],
        "country_id": user[3]
    }

@app.get("/api/users/{user_id}")
def get_user_info(user_id: int):
    """
    TODO for students: Calculate balance from transactions
    Currently returns user info with balance = 0
    """
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # TODO for students:
    # 1. Get all transactions using repository.get_all_transactions_for_user(user_id)
    # 2. Calculate balance by summing all transaction amounts
    # 3. Update the balance field below with the calculated value

    user['balance'] = 0  # Placeholder - students need to calculate this

    return user

@app.get("/api/users/{user_id}/transactions")
def get_user_transactions(user_id: int):
    """
    TODO for students: Add sender and recipient nicknames
    Currently returns empty list
    """
    # transactions = repository.get_all_transactions_for_user(user_id)

    # TODO for students:
    # 1. Uncomment the line above to get transactions
    # 2. For each transaction, get sender_id and recipient_id
    # 3. Use repository.get_user_by_id() to get user info for each ID
    # 4. Add 'sender_nickname' and 'recipient_nickname' fields to each transaction
    # 5. Handle None values (when sender_id or recipient_id is None)

    return []  # Placeholder - students need to return actual transactions
