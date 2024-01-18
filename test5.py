from datetime import datetime

class Exception_Error(Exception):
    
    def __init__(self, topic):
        super().__init__(topic)
        self.topic = topic
        self.message = ''
        self.error_code()

    def error_code(self):
        self.topic
        error = {
            'error#1' : "File not found in sharepoint ...",
            'error#2' : "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            'error#3' : "ccccccccccccccccccccccccccccccccccccccccccc",
            'error#4' : "ddddddddddddddddddddddddddddddddddddddddddd",
            'error#5' : "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        }
        
        for err, msg in error.items():
            if err == self.topic:
                self.message = msg
        
        return self.message
    
    @property
    def get_message(self):
        return f'( {self.topic} | # {self.message} # )'


err = Exception_Error('error#1')
print(err.get_message)