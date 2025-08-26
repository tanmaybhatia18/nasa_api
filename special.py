import pyfiglet
import random
import time
import os 

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def bday():
    color=['red','green','blue','yellow','magenta','rose','cyan','white']
    art=pyfiglet.figlet_format('SORRY I BACK OF IT',font='slant')
    while True:
        for i in color:
            clear()
            print(pyfiglet.figlet_format('SORRY I BACK OF IT',font='slant',justify='center'))
            print('\033[{}m'.format(random.randint(31,37)),end='')
            clear()
            
bday()