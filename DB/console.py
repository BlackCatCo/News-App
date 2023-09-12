from error_console import Error
import datetime
from user import User

logo = """                                                
          / /                 //    ) ) //   ) ) 
         / / ( )  _   __     //    / / //___/ /  
        / / / / // ) )  ) ) //    / / / __  (    
       / / / / // / /  / / //    / / //    ) )   
 ((___/ / / / // / /  / / //____/ / //____/ /    

"""


print(logo)

db_filename = None

while True:
    cmd = input("[>] ").split(' ')

    if cmd[0] == "exit" or cmd[0] == "quit":
        quit()
    
    elif cmd[0] == "set":
        err = Error(cmd="set")
        try:
            if cmd[1] == "db":
                db_filename = cmd[2]
                if ".jdb" in cmd[2]:
                    
                    with open(db_filename, 'w') as f:
                        f.write("")
                    print(f"[+] Successfully set the database to '{db_filename}'")

                else:
                    err.spit_error(id=1)
    
        except Exception as e:
            err.spit_error(id=0)
        
    elif cmd[0] == "add":

        if db_filename == None:
            print("[!] Select a database first with the command 'set'!")
        
        else:

            print(f"         [+] Add Session - {datetime.datetime.now()}")
            print(" ")
            usr = input("   [username > ] ")
            email = input("   [email >] ")
            passwrd = input("   [password > ] ")
            id = None
            print(" ")
            decision = input(f"[?] Confirm addition (y/n) > ")      

            if decision == "y":

                current = User(id=id,usr=usr,email=email,passwrd=passwrd, db=db_filename)
                current.add_user()

                print(" ")
                print(f"[+] Successfully added user on '{db_filename}'!")
                print(" ")

            else:
                print("[+] Cancelled addition")
    
    elif cmd[0] == "show":
        if cmd[1] == "db":
            if db_filename != None:
                print(f"[+] The current database is set to '{db_filename}'!")
            else:
                print("[!] You haven't selected a database, select one with the command 'set'!")
            
               
    else:
        if cmd[0] == "":
            pass
        else:
            print(f'[!] Unrecognized command, type "help" for help')