
def check_login(login):
    
    if login in users:
        return False
    return True
    
def check_password(password):

    if password < 8:
        return False
    return True

def registration():
    
    login = input()
    while !check_login(login):
        print("Such name already exists \n Please, enter another")
        login = input()
        
    print("Your password should be larger than 8")
    password = input()
    while !check_password(password):
        print("Try again")
        password = input()
    
    
    

def logIn(login, password): # вход
    a = False
    if(a):
        raise Exception("что не так")
    template_user = "" #
    return user


def tmpLogIn(login): #временный вход
    pass