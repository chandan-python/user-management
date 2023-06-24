from fastapi import APIRouter
from fastapi.responses import JSONResponse

import logging
logging.basicConfig(level = logging.INFO)

from scripts.utilities.mongo_utility import Mongo_operation
from scripts.core.models.models import login_model, signup_model
from scripts.config.app_constants import sign_up_status, response_status, Endpoint, Login_status
from scripts.core.handlers.user_management_handler import User_handler
router = APIRouter()


@router.post(Endpoint.signup)
async def sign_up(user:signup_model):
    try:
        if Mongo_operation.verify_username(user.user_name):
            logging.error(sign_up_status.user_name_error)
            return JSONResponse(status_code=409, content={'message':sign_up_status.user_name_error})
        
        if user.password != user.confirm_password:
            return JSONResponse(status_code=400, content={'message':sign_up_status.password_error})
        
        stored_user = await Mongo_operation.store_user(user)
        if stored_user['status'] == response_status.failed:
            return JSONResponse(status_code=500, content={'message':sign_up_status.store_user_error})
        
        return_data = {'message':sign_up_status.success}
        return return_data
        
    except Exception as ex:
        logging.error(ex)
        return JSONResponse(status_code=500, content={'message':sign_up_status.store_user_error})


@router.post(Endpoint.login)
async def login(logindetail:login_model):
    try:
        user = await Mongo_operation.get_user(logindetail)
        if user['status'] == response_status.failed:
            return JSONResponse(status_code=404, content={'message':Login_status.user_not_found, 'status':response_status.failed})
        user_verify = User_handler.verify_password(logindetail.password, user['password'])
        if user_verify['status'] == response_status.failed:
            return JSONResponse(status_code=403, content={'message':Login_status.incorrect_password})
        logging.info(Login_status.login_success)
        return JSONResponse(status_code=200, content=user)
    except:
        logging.error(Login_status.login_error)
        return JSONResponse(status_code=404, content={'message':Login_status.user_not_found, 'status':response_status.failed})


@router.post(Endpoint.reset_password)
async def login(logindetail:login_model):
    try:
        user = await Mongo_operation.get_user(logindetail)
        if user['status'] == response_status.failed:
            return JSONResponse(status_code=404, content={'message':Login_status.user_not_found, 'status':response_status.failed})
        
        logging.info(Login_status.login_success)
        return JSONResponse(status_code=200, content=user)
    except:
        logging.error(Login_status.login_error)
        return JSONResponse(status_code=404, content={'message':Login_status.user_not_found, 'status':response_status.failed})
