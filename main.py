#the main class aka the brain box
class Machine:
    def __init__(self):
        pass
    
    def encrypt(self):
        key_zipper = (self.keys,self.values)
        dict_encrypt =dict(key_zipper)
        new_message = ''.join([dict_encrypt[letter] for letter in "".join(self.msg.split()).lower()])
        return new_message
crypo = Machine()

