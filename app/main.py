from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Отключаем CORS — разрешаем все origins, методы и заголовки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_get():
    return {"message": "GET handler working"}

@app.post("/")
def read_post():
    return {"message": "POST handler working"}