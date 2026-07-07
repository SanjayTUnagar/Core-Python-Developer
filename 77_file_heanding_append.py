# File Heandling Append a file 

def append_file(filename, text):
    f = open(filename, "a")
    f.write(text)
    f.close()

append_file("student.txt", "\nWelcome to Python")