import base64

class TextProcesser:

    def __init__(self, text):
        self.text = text
    
    def encrypt(self):
        
        return base64.b64encode(bytes(self.text, 'utf-8'))
    
    

        