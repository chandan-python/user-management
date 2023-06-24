import bcrypt
import logging
import traceback

from scripts.config.app_constants import response_status
from scripts.config.app_constants import password_hash

class User_handler:
    async def hash_password(password):
        try:
            salt = bcrypt.gensalt()

            hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

            logging.info(password_hash.success)
            return hashed_password.decode("utf-8")
        
        except Exception as ex:
            logging.error(password_hash.error)
            traceback.print_exc()
            return {'message':password_hash.error, 'reason':ex}
        

    async def verify_password(password, hashed_password):
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            return {'status':response_status.success}
        else:
            return {'status':response_status.failed}

