class Error:
    def __init__(self, cmd):
        self.cmd = cmd

    def spit_error(self, id):
        if self.cmd == "set":
            if id == 0:
                print("[!] Invalid arguments. Use 'set db [database.jdb]'")
            elif id == 1:
                print("[!] Invalid arguments. File extension must be '.jdb'!")
        