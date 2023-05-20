from pydantic import BaseModel

class login_model(BaseModel):
    username : str
    password : str