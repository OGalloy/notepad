##
from note import Note

class Notepad:
    def __init__(self, file):
        self.notes_list = []
        notes = open(file, "r")
        lines = notes.readlines()
        for line in lines:
            line = line.split("|")
            new_note = Note(int(line[0]), line[1], line[2], line[3])
            self.notes_list.append(new_note)
        notes.close()

    def show_all_notes(self):
        if len(self.notes_list) == 0:
            print("Notepad is empty!!!")
        else:
            print("********List of Notes***********")
            for n in self.notes_list:
                print(f"ID: {n.id} | Title: {n.title}")
    #            
    def create_note(self, title, body):
        new_note = Note(len(self.notes_list)+1, title, body,)
        self.notes_list.append(new_note)
        print("New note was created")

    #read note by id    
    def read_note(self, id):
        for n in self.notes_list:
            if n.id == id:
                print("*"*30)
                print(f"ID: {n.id} | Title: {n.title}")
                print("*"*30)
                print(f"{n.body}")
                print(f"LastChange: {n.time_last_edition}")

    #            
    def update_note(self, id, title, body):
        for n in self.notes_list:
            if n.id == id:
                n.set_title(title)
                n.set_body(body)
        print("Note was update.")

    def delete_note(self, id):
        for n in self.notes_list:
            if n.id == id:
                self.notes_list.remove(n)
        print("Note was deleted.")
        counter = 1
        for n in self.notes_list:
            n.id = counter
            counter+=1
    
    def find_note(self,sub_string):
        result = [] 
        for n in self.notes_list:
            if n.title.find(sub_string) >=0 or n.body.find(sub_string) >=0:
                result.append(n)
        for n in result:
            self.read_note(n.id)

    def save_notes(self):
        file = open("notes.txt", "w")
        for n in self.notes_list:
            file.write(f"{n.id}|{n.title}|{n.body}|{n.time_last_edition}")
        print("Notes was saved.")


if __name__ == "__main__":
    #Code for test
    np = Notepad("notes.txt")
    np.show_all_notes()
    print(np.notes_list[0].id)
    np.create_note("second note", "hello, world")
    np.show_all_notes()
    np.read_note(1)
    np.read_note(2)
    np.read_note(3)
