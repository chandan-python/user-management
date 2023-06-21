from fastapi import APIRouter
from fastapi.responses import JSONResponse

import logging
logging.basicConfig(level = logging.INFO)

from scripts.utilities.mongo_utility import store_user, verify_username
from scripts.core.models.models import login_model, signup_model
from scripts.config.app_constants import sign_up_status, response_status

router = APIRouter()

@router.post('/signup')
def sign_up(user:signup_model):
    try:
        if verify_username(user.user_name):
            logging.erro(sign_up_status.user_name_error)
            return JSONResponse(status_code=409, content={'message':sign_up_status.user_name_error})
        
        if user.password != user.confirm_password:
            return JSONResponse(status_code=400, content={'message':sign_up_status.password_error})
        
        stored_user = store_user(user)
        if stored_user['status'] == response_status.failed:
            return JSONResponse(status_code=500, content={'message':sign_up_status.store_user_error})
        
        return_data = {'message':sign_up_status.success}
        return return_data
        
    except Exception as ex:
        logging.error(ex)
        return JSONResponse(status_code=500, content={'message':sign_up_status.store_user_error})




@router.post('/login')
def login(logindetail:login_model):
    try:
        print()
        

    except:
        return JSONResponse
