#the main class
#Work in progress!!
class Machine:
    #initializing 
    def __init__(self,msg,mode,keys,val):
        pass
#declaring object variables
message = input("Enter your secret : ")
mode = input("Select crypto mode: encode(e) OR decrypt as default:")
keywords = "ab7cd1ef8gh2ij9kl3mn0op4qr!st5uvwx6yz@#"
values = keywords[-1] + keywords[0:-1]
#Main Object
crypo = Machine(message,mode,keywords,values)

if crypo.mode == 'e':
    print(check.encrypt())
else:
    print(check.decrypt())