print("Hello Welcome to the Manga Reader Recommender")
print("Answer a few question:")

genre = str(input("What genre that you type (action,horror,romance) --> "))
length = str(input("How long this should manga be?(short,medium,long) -->"))
decade = eval(input("Which decade(2000,2024) -->"))
#

"""
FOR ACTION

"""

#set1 for action
if genre == "action":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: All You Need Is Kill ")
        # else:
        #     print("Not available for to now")

if genre == "action":
    if length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: Sailer Moon ")
        # else:
        #     print("Not available for to now")

if genre == "action":
    if length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Naruto")
        # else:
        #     print("Not available for to now")

#set2 for action
if genre == "action":
    if length == "short":
        if decade == 2024:
            print("WE RECOMMEND: MAD")
        # else:
        #     print("Not available for to now")

if genre == "action":
    if length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: Shinobi UnderCover")
        # else:
        #     print("Not available for to now")

if genre == "action":
    if length == "long":
        if decade == 2024:
            print("WE RECOMMEND: ONE PIECE")
        # else:
        #     print("Not available for to now")


"""
FOR ROMANCE

"""


#set1 for ROMANCE
if genre == "romance":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: She The Ultimate Weapon")
        # else:
        #     print("Not available for to now")

if genre == "romance":
    if length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: Fruit Basket")
        # else:
        #     print("Not available for to now")

if genre == "romance":
    if length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Honey and Clover")
        # else:
        #     print("Not available for to now")

#set2 for adventure
if genre == "romance":
    if length == "short":
        if decade == 2024:
            print("WE RECOMMEND: Yakuza Fiance ")
        # else:
        #     print("Not available for to now")

if genre == "romance":
    if length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: Learning to Love My Cat-like Classmate")
        # else:
        #     print("Not available for to now")

if genre == "romance":
    if length == "long":
        if decade == 2024:
            print("WE RECOMMEND: A Condition Called Love")
        # else:
        #     print("Not available for to now")

"""
FOR HORROR

"""

#set1 for HORROR
if genre == "horror":
    if length == "short":
        if decade == 2000:
            print("WE RECOMMEND: Another ")
        # else:
        #     print("Not available for to now")

if genre == "horror":
    if length == "medium":
        if decade == 2000:
            print("WE RECOMMEND: The Drifting Classroom: Perfect Edition")
        # else:
        #     print("Not available for to now")

if genre == "horror":
    if length == "long":
        if decade == 2000:
            print("WE RECOMMEND: Higurashi no Naku Koro ni")
        # else:
        #     print("Not available for to now")

# set2 for HORROR
if genre == "horror":
    if length == "short":
        if decade == 2024:
            print("WE RECOMMEND: Jujutsu Kaisen Modulo")
        # else:
        #     print("Not available for to now")

if genre == "horror":
    if length == "medium":
        if decade == 2024:
            print("WE RECOMMEND: The Summer Hikaru Died")

        # else:
        #      print("Not available for to now")

if genre == "horror":
    if length == "long":
        if decade == 2024:
            print("WE RECOMMEND: Immortality and Punishment")
    



