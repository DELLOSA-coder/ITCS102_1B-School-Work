juice1 = "Nestea"
juice2 = "Tang"
#List with default values

juice = ['Lychee', 'Nestea', 'Tang', 'Citrus', 'Pomelo', 'Mango', 'Grapes']
            #0         1       2        3         4        5         6
print(juice)

#Every list has an index value / address
print(juice[3])
print(juice[2 : 5]) #List slicing

#Appending or adding items on the end of the list
juice.append("Nestea")
print(juice)

juice.append("Tang")
print(juice)

#Inserts item at specified index
juice.insert(4, "Pomelo")
print(juice)

#Remove first occurence of item
juice.remove("Mango")
print(juice)

#Removes and returns item at index
juice .pop()
print(juice)

#Returns number of elements
print(len(juice))


#Sorts the list(ascending by default)
juice.sort()
print(juice)

#Reverses the list order
juice.reverse()
print(juice)