try:
    file=open("week-4 Assignment/files/example.txt","r")
    data=file.read()
    print(file.readline())
    print(file.readlines())
    print(data)
    
  

except FileNotFoundError:
    print("file not found")
    
finally:
    file.close()   
    
    