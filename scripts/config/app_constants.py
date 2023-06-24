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

class Login_status:
    user_not_found = 'User does not exist'
    incorrect_password = "Incorrect passowrd"
    login_success = 'Successfully logged in'
    login_error = 'Failed to login please try again'

class store_user_status:
    error = "Failed to store user data"
    success = "SUccesfully stored user data to db"


class Endpoint:
    signup = '/signup'
    login = '/login'
    forgot_password = '/forgot_password'
    reset_password = '/reset_password'

class get_user_status:
    error = 'User Not FOund'