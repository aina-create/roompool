from fastapi import FastAPI
from routes.user_routes import router as user_router
from database import engine, Base

app = FastAPI()

# Include user routes
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "User Service Running"}

# Create database tables
Base.metadata.create_all(bind=engine)
