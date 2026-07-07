
# File Heandling Read a file 

def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


print(read_file("student.txt"))