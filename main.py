#the main class aka the brain box
class Machine:
    def __init__(self):
        pass
    
    def decrypt(self):
        key_zipper = zip(self.values,self.keys)
        dict_decrypt =dict(key_zipper)
        new_message = ''.join([dict_decrypt[letter] for letter in self.msg.lower().strip()])
        return new_message
crypo = Machine()

