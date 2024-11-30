try:
    
    
    file=open("week-4 Assignment/files/example.txt","w")
    
    data=file.write('hello there brenny make good use of the opportunity')
   
    print(data)

except FileNotFoundError:
    print("file not found")
    
finally:
    file.close()   
    