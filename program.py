import pyttsx3
import os
e=pyttsx3.init()
e.setProperty('rate',140)
e.say('enter the number to open the app')
e.runAndWait()
while True:
    print('enter the number to open the app')
    print('\n 1.MICROSOFT WORD \t 2.GOOGLE CHROME \t 3.FOR EXIT\n')
    
    p=input()
    p=p.upper()
    print(p)
    
    
    if ('DONT' in p) or ("DON'T" in p) or ('not' in p):
        e.setProperty('rate',140)
        e.say('type again')
        e.runAndWait()
        print('.')
        print('.')
        continue
    elif('1' in p):
        os.system("start winword")
    elif ('2' in p):
        os.system("start chrome")
    elif('3' in p):
        e.say("exiting")
        break 
    else:
        e.say(p)
        print('invalid')
        e.say('invalid')
        e.runAndWait()