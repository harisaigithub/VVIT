aList = [1, 2, 3, 4]
print(aList)
aList.append(5)
print("Updated List : ", aList)

# language list
language = ['French', 'English', 'German']
 
# another list of programing language
programing = ['python', 'Java']
 
language.extend(programing)
 
print('Extended List: ', language)

# List
list1 = [1, 2, 3, 4, 5, 6]
 
# Inserting value
list1.insert(0, 7)
 
print("New List: ", list1)

list1 = [3, 4, 1, 1, 8, 9]
list1.remove(4)
print(list1)

languages = ['Python', 'Java', 'C++', 'Kotlin']
 
# removing java
print(languages.pop(1))
print(languages)


oldlist = ["a", "b", "c", "d"]
newList = oldlist.clear()
print(newList)

nums = [14, 5, 4, 5, 7, 32]
 
x = nums.index(5)
 
print(x)


list1 = [1, 4, 3, 6, 7]
 
# Reversing List
list1.reverse()
 
print(list1)
