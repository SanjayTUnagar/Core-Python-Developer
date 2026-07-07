# Decorator 

def decor_result(result_func):
    def destinction (marks):
        for m in marks:
            if m>75:
                print("Destinction")
                return
            result_func(marks)
        return destinction

@decor_result
def result(marks):
    for m in marks:
        if m>33:
            print("Pass")
        else:
            print("Fail")
            break
    else:
        print("Pass")
result([50,40,30,80,60])
