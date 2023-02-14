#Заметка
from datetime import datetime

def parse_time(date):
    time_last_edition = f"{date.year}-{date.month}-{date.hour}-{date.minute}-{date.second}"
    return time_last_edition

class Note:
    def __init__(self, note_id, title, body, time=parse_time(datetime.now())):
        self.id = note_id
        self.title = title
        self.body = body
        self.time_last_edition = time 

    def set_title(self, new_title):
        self.title = new_title
        self.time_last_edition = parse_time(datetime.now())

    def set_body(self, new_body):
        self.body = new_body
        self.time_last_edition = parse_time(datetime.now())

    def get_time(self):
        return self.time_last_edition

if __name__ == "__main__":
    ##code for testing
    import time
    n1 = Note(1, "first", "hello")
    print(n1.id)
    print(n1.title)
    print(n1.body)
    print(n1.time_last_edition)
    time.sleep(1)
    n1.set_body("note was changed!!!")
    print(n1.get_time())