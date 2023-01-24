try:
    myFile = open("mydata2.txt", encoding="utf-8")       #opening a remote file
       
except FileNotFoundError as bam:
    print("The file does not exist")
    print(bam.args)                                         #explains error

else:
    print("File :", myFile.read())                          #prints file content
    myFile.close()                                          #closes file

finally:
    print("Level Complete!")                                #default output