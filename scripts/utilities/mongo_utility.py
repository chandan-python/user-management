import logging 


from conf.db_conf import user_collection
from scripts.config.app_constants import store_user_status, response_status
from scripts.core.handlers.user_management_handler import hash_password

def store_user(user):
    try:
        user_data = dict(user)
        user_data['password'] = hash_password(user.password)
        user_collection.insert_one(user_data)
        return {'message':store_user_status.success, 'status':response_status.success}
    
    except Exception as ex:
        logging.error()
        return {'message':store_user_status.error, 'status':response_status.failed, 'reason':ex}


def verify_username(user_name):
    try:
        user = user_collection.find_one({'user_name':user_name})
        if user:
            return user
        return None

    except Exception as ex:
        logging.error()
        return {'message':store_user_status.error, 'status':response_status.failed, 'reason':ex}