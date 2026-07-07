# File Heandling Write a file 

def writing (filename,text):
    f=open(filename,"w")
    f.write(text)
    f.close()
writing("student.txt", "Hello World")