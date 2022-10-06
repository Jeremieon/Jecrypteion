#the main class aka the brain box
from tabnanny import check


class Machine:
    def __init__(self):
        pass

crypo = Machine()

if crypo.mode == 'e':
    print(check.encrypt())
else:
    print(check.decrypt())