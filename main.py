from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.config import settings

app = FastAPI(
    title = "Enterprise Ai Business Copilot",
    description = "AI powered Business intelligence Platform",
    version = "1.0.0")

#attach router to the main application
app.include_router(router, prefix='/api/v1')

@app.get("/")
def root():
    return {
        "message":"Enterprise AI Business Copilot API is Running"
        }





# Only for testing
# print(settings.APP_NAME)
# print(settings.APP_VERSION)
