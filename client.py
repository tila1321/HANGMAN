import socket
import random

HMAN = ['''
    +-----+
    |     |
    |
    |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |     |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / 
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / \ 
    |
    ======= ''' ,'''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / \ 
    |     DEAD
    ======= ''']

def ClientProg():

    CS = socket.socket()
    host = '192.168.56.105'
    port = 0

    print("\n[[ Available port is 1024 to 65535 ]]")

    while port < 1024 or port > 65535:
        try:
           port = int(input("\nEnter a port: "))
        except ValueError:
           pass

    CS.connect((host, port))

    print("\n")
    print("\t\t--------------------------------------------------------")
    print("\t\t（＾・ω・＾✿） Hello! Welcome to Hangman! （＾・ω・＾✿）")
    print("\t\t--------------------------------------------------------")
    print("\t\t-------------------------------------------")
    print("\t\t The goal is to guess as much as you can ")
    print("\t\t-------------------------------------------")
    print("\n")
    print("/t************************")
    print("/t The category is COLOUR ")
    print("/t************************")

    login = input("Already sign up to the game (y or n) ?:")

    if login == 'y' or login == 'Y':

        Username = input(" username: ")
        password = input(" password: ")
        sendinfString = Username + "|" + password
        while Username.lower().strip() != 'bye' and password.lower().strip() != 'bye':

            CS.send(bytes(sendinfString,'utf-8'))

            Data = CS.recv(1024)
            print('Received from server: ' + str(Data, 'utf-8'))
            if str(Data, 'utf-8') == str("Login Successfull!"):
                pass
            else:
                CS.close()
                ClientProg()

    elif login == 'n' or login == 'N':
        Username = input(" username: ")
        exist(Username,CS)
    else:
        pass

def exist(Username,CS):

    while Username.lower().strip() != 'bye':
        CS.send(bytes(Username,'utf-8'))
        Data = CS.recv(1024)
        print('Received from server: ' + str(Data,'utf-8'))
        if str(Data,'utf-8') == str("Already exists,please try another username:"):
            Username = input(" Username: ")
            exist(Username,CS)
        else:
            Password = input(" password: ")
            CS.send(bytes(Password, 'utf-8'))
            while Password.lower().strip() != 'bye':
                Data = CS.recv(1024)
                strData = str(Data, 'utf-8')

                if str(Data,'utf-8') == str("firstUser"):
                    size = input("\nHow many players will join?:")
                    CS.send(bytes(size,'utf-8'))
                elif str(Data, 'utf-8') == str("Login Successfull!"):
                    print("Logged In!")
                    CS.send(bytes("OK", 'utf-8'))
                elif strData.isdigit():
                    print(HMAN[int(strData)])
                elif str(Data,'utf-8') == str("It is your Turn"):
                    Guess =input("/nPlease enter your guess:")
                    CS.send(bytes(Guess,'utf-8'))
                else:
                    print('Received from server: ' + str(Data, 'utf-8'))

    while password.lower().strip() != 'bye':

        CS.send(bytes(password,'utf-8'))
        Data = CS.recv(1024)

        print('Received from server: ' + str(Data, 'utf-8'))
        if str(Data, 'utf-8') == str("Login Successfull!"):
            pass
        else:
           pass

    CS.close()


if __name__ == "__main__":

      ClientProg()

