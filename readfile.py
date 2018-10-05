import io
import sys
import os
file=None
try:
    file=open("F:\sagarshubham.txt")
    content=file.readlines()
    print(content)
except IOError as er:
    print("This is an error :"%er)
finally:
    try:
        file.flush()
        file.close()
        if file.closed:
            print("Successfully closed")
        else:
            print("Not closed")
    except IOError as e:
        print("This is another error :%s"%e)
print("We are at 0 ident")
