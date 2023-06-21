from fastapi import FastAPI
import uvicorn
from scripts.core.services import user_management

app = FastAPI()
app.include_router(user_management.router)
# app.include_router(file_services.router)

if __name__ =='__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)