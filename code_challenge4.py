print("Hello Welcome to the Manga Reader Recommender")
print("Answer a few question:")

genre = str(input("What genre that you type (action,horror,romance) --> "))
length = str(input("How long this should manga be?(short,medium,long) -->"))
decade = eval(input("Which decade(2000,2024) -->"))

"""
FOR ACTION

"""

#set1 for action
if genre == "action":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: All You Need Is Kill ")      
        else:
            print("We dont have a recommendations in a year you input")  

    elif length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: Sailer Moon ")  
        else:
            print("We dont have a recommendations in a year you input")  
        
    elif length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Naruto")
        else:
            print("We dont have a recommendations in a year you input")
    else:
        print("Sorry the volume you input in available")

#set2 for action
    if length == "short":
        if decade == 2024:
            print("WE RECOMMEND: MAD")
        else:
            print("We dont have a recommendations in a year you input")
       


    elif length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: Shinobi UnderCover")
        else:
            print("We dont have a recommendations in a year you input")
        

    elif length == "long":
        if decade == 2024:
            print("WE RECOMMEND: ONE PIECE")
        else:
            print("We dont have a recommendations in a year you input")
    else:
        print("Sorry the volume you input in available")

        


"""
FOR ROMANCE

"""

if genre == "romance":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: She The Ultimate Weapon")
        else:
            print("We dont have a recommendations in a year you input")  
       
    elif length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: Fruit Basket")
        else:
            print("We dont have a recommendations in a year you input")  
        
    elif length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Honey and Clover")
        else:
            print("We dont have a recommendations in a year you input")  
    else:
        print("Sorry the volume you input in available")


    if length == "short":
        if decade == 2024:
            print("WE RECOMMEND: Yakuza Fiance ")
        else:
            print("We dont have a recommendations in a year you input")  
        
    elif length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: Learning to Love My Cat-like Classmate")
        else:
            print("We dont have a recommendations in a year you input")  
       

    elif length == "long":
        if decade == 2024:
            print("WE RECOMMEND: A Condition Called Love")
        else:
            print("We dont have a recommendations in a year you input")  
    else:
        print("Sorry the volume you input in available")

        
"""
FOR HORROR

"""

if genre == "horror":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: Another ")
        else:
            print("We dont have a recommendations in a year you input")  
        

    elif length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: The Drifting Classroom: Perfect Edition")
        else:
            print("We dont have a recommendations in a year you input")  
        

    elif length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Higurashi no Naku Koro ni")
        else:
            print("We dont have a recommendations in a year you input")    

    elif length == "short":
        if decade == 2024:
            print("WE RECOMMEND: Jujutsu Kaisen Modulo")
        else:
            print("We dont have a recommendations in a year you input")  
        

    elif length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: The Summer Hikaru Died")   
        else:
            print("We dont have a recommendations in a year you input")     


    elif length == "long":
        if decade == 2024:
            print("WE RECOMMEND: Immortality and Punishment")
        else:
            print("We dont have a recommendations in a year you input")  
    else:
        print("Sorry the volume you input in available")
else:
    print("The genre you input is not available")

    



