#the main class
#Work in progress!!
class Machine:
    #initializing 
    def __init__(self,msg,mode,keys,val):
        self.msg = msg
        self.mode = mode
        self.keys = keys
        self.values = values 
    
    def encrypt(self):
        key_zipper = (self.keys,self.values)
        dict_encrypt =dict(key_zipper)
        new_message = ''.join([dict_encrypt[letter] for letter in "".join(self.msg.split()).lower()])
        return new_message
      

    def decrypt(self):
        key_zipper = zip(self.values,self.keys)
        dict_decrypt =dict(key_zipper)
        new_message = ''.join([dict_decrypt[letter] for letter in self.msg.lower().strip()])
        return new_message
#declaring object variables
message = input("Enter your secret message: ")
mode = input("Select crypto mode: encode(e) OR decrypt as default:")
keywords = "ab7cd1ef8gh2ij9kl3mn0op4qr!st5uvwx6yz@#"
values = keywords[-1] + keywords[0:-1]
#Main Object
crypo = Machine(message,mode,keywords,values)

if crypo.mode == 'e':
    print(crypo.encrypt())
else:
    print(crypo.decrypt())

    

