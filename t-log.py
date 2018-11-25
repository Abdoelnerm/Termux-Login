import os
import time
from getpass import getpass

def login():
    os.system('clear')
    print("\033[1;96m")
    print ("<-------------------{ Termux Login Script v1.0 }-------------------->")
    print ("<-------------------{     By Abdallah X1L      }-------------------->")
    print ("<-------------------{ Hope This Tcript Likes U }-------------------->")
    x = input('\033[1;92mUsername \033[1;93m: ')
    e = input('\033[1;92mPassword \033[1;93m: ')
    if x=="root" and e=="root":
        os.system("clear")
        print ("Welcome Sir")
        os.system("clear")
        os.system('cowsay -f eyes Abdallah X1L | lolcat')
        os.system('figlet -f big Abdallah X1L | lolcat')
    else:
        print ("""
                                 .   
                              .  !\  _ 
                              l\/ ( /(_ 
                             _ \`--" _/ .  
                             \~")   (_,/)  
                             _)/.   ,\,/   
                    _____,-"~    \ /   "~"-._____   
                ,-~"     "~-.  .  "  .  ,-~"     "~-.  
              ,^             ^. `. .' ,^             ^.   
             /                 \  ^  /                 \  
            Y___________________Y   Y___________________Y  
            | |^~"|^   _ ^|"~^| |   | |"~"|^ _   ^|"~"| |  
            | !   l   (_) !   ! l   | !   l (_)   !   ! |  
            l  \  `\.___,/'  /  !   l  \  `\.___,/'  /  !  
             \  ^.         ,^  /!   !\  ^.         ,^  /   
              ^.  ~-------~  ,^\`v-v'/^.  ~-------~  ,^   
              _)~-._______,-~   }---{   ~-._______,-~(_    
         .--"~           ,-^7' /     \ `Y^-,           ~"--.    
        /               (_,/ ,/'     `\. \._)    ___        \  
        \_____.,--"~~~"--..,__        ___,..--<"~   ~"-.,___/   
            / (    __,--~ _.._""~~~~"" ,-"  "-.`\     /~.-"   
            `._"--~_,.--"~    \       /        \ `---' /    
               "~""            \     /          "-.__,/ 
                               `L   ]'   
                                l   !   
                                j___L              -Row
                               (_____)  
                                |   |   
                 You Can't access my Termux.Good Bye!
""")
        time.sleep(2)
        os.system('ps')
        os.system('killall -9 com.termux')

login()

