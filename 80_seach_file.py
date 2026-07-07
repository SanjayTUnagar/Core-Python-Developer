# Search a word in the file 

def search(filename,word):
    try:
        f=open(filename,'r')
        line_count = 0
        for line in f.readline():
            line_count +=1;
            strlist=line.split('')
    word_count = 0
    for w in strlist:
        word_count +=1
        if word==w:
            return(line_count,word_count)
        else:
            return None
    except FileNotFoundError:
    print("File not Found...")
finally:
f.close()
