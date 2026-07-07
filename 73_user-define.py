# User Define Exception 

class InssuffucuentBalanceError(Exception):
    pass
try:
    raise InssuffucuentBalanceError("Low Balance")

except InssuffucuentBalanceError as e:
    print(e)