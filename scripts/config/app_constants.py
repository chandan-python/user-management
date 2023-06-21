class password_hash:
    success = "succesfully hashed password"
    error = "Failed to hash password"

class sign_up_status:
    password_error = "The password and confirm password fields do not match"
    store_user_error = "Something went wrong, Please try agaain once"
    success = "successfully create user"
    user_name_error = "The username is already taken."

class response_status:
    failed = 'failed'
    success = 'success'

class store_user_status:
    error = "Failed to store user data"
    success = "SUccesfully stored user data to db"
