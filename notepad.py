##
import note

class Notepad:
    def __init__(self, file):
	    self.notes_list = []
	    
        notes = open(file, "r")
	    lines = notes.readlines()

	    for line in lines:
            line = line.split("|")
            new_note = note.Node(line[0], line[1], line[2], line[3])
            self.notes_list.append(new_note)

	def get_notes_list()
        print(self.notes_list)	 