
def circarea(radio):
    pi = 3.1415
    return pi*radio**2

def cilindvolumen(radio, altura):
    return circarea(radio)*altura

print(cilindvolumen(7,9))