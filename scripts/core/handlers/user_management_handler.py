import bcrypt
import logging
import traceback


from scripts.config.app_constants import password_hash


def hash_password(password):
    try:
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

        logging.info(password_hash.success)
        return hashed_password.decode("utf-8")
    
    except Exception as ex:
        logging.error(password_hash.error)
        traceback.print_exc()
        return {'message':password_hash.error, 'reason':ex}
    

def verify_password():
    hashed_password = b'$2b$12$...hashedpassword...'  # Replace with the actual hashed password
    password = "mypassword"  # Replace with the provided password

    # Verify the password
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        print("Password is correct")
    else:
        print("Password is incorrect")

