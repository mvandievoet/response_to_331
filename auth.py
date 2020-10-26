def get_user(request): #request is tornado object
    login_value1= request.get_argument('username')
    login_value2= request.get_argument('password')

    if login_value1 == 'nyc':
        if login_value2 == 'iheartnyc':
            return 1
    return None

login_url = '/login'
