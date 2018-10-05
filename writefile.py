import io 
import sys 
import os
file=None
mdata="""This is shubham kanungo from college IIPS pursuing M.C.A and belong  to barwani"""
try:
    file=open("F:\sagarshubham.txt",'w')
    if file!=None:
        print("Data in file to write")
        data=str(input("Enter the data :"))
        file.write(data)      
        file.writelines(mdata)
        print("YOur file write is completed")
   # os.rename(file,"rohit.txt")
except IOError as er:
    print("This is an error :%s"%er)
finally:
    try:
        file.flush()
        file.close()
    except IOError as e:
        print("THis is another error : %s"%e)
print("We are at 0 ident")