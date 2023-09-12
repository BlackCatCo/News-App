class User:
    def __init__(self, id, usr, email, passwrd, db):
        self.id = id
        self.usr = usr
        self.email = email
        self.passwrd = passwrd
        self.db = db

    def add_user(self):

        with open(self.db, 'r') as db:
            lines = db.readlines()
            line_count = len(lines)
            self.id = line_count + 1
        
        db.close()

        with open(self.db, 'a') as db:  # mode 'w' overwrites, I want to append so I right 'a'
            if self.id == 1:
                db.write(str(self.id)+":"+self.usr+":"+self.email+":"+self.passwrd)
            else:
                db.write('\n' + str(self.id)+":"+self.usr+":"+self.email+":"+self.passwrd)
        
        db.close()