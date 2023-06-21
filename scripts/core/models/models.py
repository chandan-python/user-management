from pydantic import BaseModel

class login_model(BaseModel):
    username : str 
    password : str


class signup_model(BaseModel):
    user_name :str
    email : str = None
    phone_number : str = None
    password : str
    confirm_password : str 
