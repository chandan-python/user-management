import logging 

from conf.db_conf import user_collection
from scripts.config.app_constants import store_user_status, response_status, get_user_status
from scripts.core.handlers.user_management_handler import hash_password

class Mongo_operation:
    @staticmethod
    async def store_user(user):
        try:
            user_data = dict(user)
            user_data['password'] = hash_password(user.password)
            user_collection.insert_one(user_data)
            return {'message':store_user_status.success, 'status':response_status.success}
        
        except Exception as ex:
            logging.error()
            return {'message':store_user_status.error, 'status':response_status.failed, 'reason':ex}

    @staticmethod
    async def verify_username(user_name):
        try:
            user = user_collection.find_one({'user_name':user_name})
            if user:
                return user
            return None

        except Exception as ex:
            logging.error()
            return {'message':store_user_status.error, 'status':response_status.failed, 'reason':ex}
        

    @staticmethod
    async def get_user(user):
        try:
            user_details = user_collection.find_one({'email':user.email})
            if user_details :
                user_details.pop('_id')
                user_details.update({'status':response_status.success})
                return user_details.update()
            return {'message':get_user_status.error, 'status':response_status.failed}
        except:
            logging.error(get_user_status.error)
            return {'message':get_user_status.error, 'status':response_status.failed}
