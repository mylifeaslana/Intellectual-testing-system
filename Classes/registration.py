#from emal.massage import EmalMassage
import smtplib

from dataProcessing import users

EMAIL = "zeiwjfew@yandex.ru"
PASSWORD = "ooP123"
COUNT_OF_PASSWORD = 3


def check_login(login):
    
    if login in users:
        return False
    return True
    
def check_password(password):

    if password < 8:
        return False
    return True

def registration(login,password,name,surname,father_name,date_of_birth,group,secret_question,secret_answer,email,tel,photo=""):
    #login = input()
    while not check_login(login):
        print("Such name already exists \n Please, enter another")
        login = input()

    print("Your password should be larger than 8")
    #password = input()
    while not check_password(password):
        print("Try again")
        password = input()

    name = input()
    surname = input()
    father_name = input()
    group = input()
    secret_question = input()
    answer = input()
    main = input()
    tel = input()
    return True

''''
    #вынеси в отдельную функцию
    msg = EmalMassage()
    msg['Subject'] = "Подтверждение регистрации"
    msg['From'] = EMAIL
    msg['To'] = mail
    msg.set_content("Подтвердите регистрацию")
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_massage(msg)
    
    #make an object,нет,внести все данные в users
    
def reestablishPassword(login):
    
    print(users[login][secret_question])
    answer = input()
    if answer == users[login][secret_answer]:
        return True
    return False
    
'''''
def logIn(login, password): # вход

    count_of_passing = 0
    '''''
    while count < COUNT_OF_PASSWORD:
        login, password = input(), input()
        
        try:
            if login not in user:
                raise loginException("There are no such user")
            
            if user[login][password] != password:
                countOfPassing += 1 
                raise passwordException("Wrong password")
            
            else:
                
                break
        
        except:
            pass
        
    print("Do you wanna reestablish password (Y/N)")
    
    if input() == "Y":
        if reestablishPassword(login):
            #window for changing password
            print("Enter new password")
            
            newPassword = input()
            
            if newPassword == user[login][password]:
                
                raise passwordException("New password shouldn't be equal to old one")
                
                #отдельное окно в которое пользователь вводит указанные сведения 
                
            
            user[login][password] = newPassword
            
            
    else:
        pass
        #close the window
    
    templateUser = "" #
    return user

'''''
def tmpLogIn(login): #временный вход
    pass
