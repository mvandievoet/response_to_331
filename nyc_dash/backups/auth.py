def get_user(request): #request is tornado object
    username_value = request.get_argument('username')
    password_value = request.get_argument('password') 
    if username_value == 'nyc' and password_value == 'iheartnyc':
        return 1
    else:
        return None

password_url = '/password'
username_url = '/username'
