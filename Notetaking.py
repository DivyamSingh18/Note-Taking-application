print("\n\n            THE NOTETAKING Application..........")
user_input = input("\nEnter The Mode For Which You Want To Open The File Write(i.e read , write , append) :")
if(user_input=="write"):
    notes=open('Notepad.txt','w')
    n=int(input("\nHow Many Notes You Want to add ? =>"))
    for i in range(1,n+1):
        data=input("\nEnter The Data :")
        notes.write("Note ")
        notes.write(str(i))
        notes.write(":  ")
        notes.write(data+"\n")
        
        record= open('rec.txt','w')
        record.write(str(i))
    print("\nThe Data Was Successfully Stored In The File !! \n ")
    notes.close

elif(user_input=="read"):
    notes=open('Notepad.txt','r')
    print("\nThe Data That Was Stored in Your File =>\n")
    content = notes.read()
    print(content)
    notes.close()
elif(user_input=="append"):
    notes = open('Notepad.txt','a')
    add=int(input("\nHow Many Notes You Want to add ? =>"))
    record=open('rec.txt','r')
    ct=int(record.read())
    
    for i in range(ct+1,add+1+ct):
        data=input("\nEnter The Data You Want To Add : ")
        notes.write("Note ")
        notes.write(str(i))
        notes.write(":  ")
        notes.write(data+"\n")
    print("\nYour Data Has Been Updated.....\n ")
    notes.close()
    record.close()
else:
    print("\nInvalid Command.....\n")

