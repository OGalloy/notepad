from notepad import Notepad

user_help = """
Put help
Put add for add new note.
Put read for read note.
Put update for update note.
Put delete for delete note.
Put find for find substring in notes.
Put all. Output : note id and note title.  
""" 

def main():
	np = Notepad("notes.txt")
	print("Hello!!! This is simple notepad!!!")
	print("Puts ? for help!!! ")
	command = ""
	while command != "exit":
		command =input("***")
		if command == "exit":
			np.save_notes()
			exit()
		elif command == "help":
			print(user_help)
		elif command == "add":
			title = input("enter new note title: ")
			body = input("enter new note body: ")
			np.create_note(title, body)
		elif command == "read":
			id = input("enter note id: ")
			np.read_note(int(id))
		elif command == "update":
			id = input("enter note id: ")
			title = input("enter new note title: ")
			body = input("enter new note body: ")
			np.update_note(int(id), title, body)
		elif command == "delete":
			id = input("enter note id: ")
			np.delete_note(int(id))
		elif command == "find":
			sub_string = input("enter string for searching: ")
			np.find_note(sub_string)
		elif command == "all":
			np.show_all_notes()
		else:
			print("Unknown command!")


if __name__ == "__main__":
	main()