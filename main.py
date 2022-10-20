#the main class
class Machine:
    #initializing 
    def __init__(self):
        self.msg = input("Enter your secret message: ")
        self.mode = input("Select crypto mode: encode(e) OR decrypt as default:")
        self.keys= "ab7cd1ef8gh2ij9kl3mn0op4qr!st5uvwx6yz@#"
        self.val =  self.keys[-1] +  self.keys[0:-1]

    def encrypt(self):
        key_zipper = zip(self.keys,self.val)
        dict_encrypt =dict(key_zipper)
        new_message = ''.join([dict_encrypt[letter] for letter in "".join(self.msg.split()).lower()])
        return new_message
      

    def decrypt(self):
        key_zipper = zip(self.val,self.keys)
        dict_decrypt =dict(key_zipper)
        new_message = ''.join([dict_decrypt[letter] for letter in self.msg.lower().strip()])
        return new_message
#obje
crypo = Machine()


if __name__ == "__main__":
    if crypo.mode == 'e':
        print(crypo.encrypt())
    else:
        print(crypo.decrypt())

    

