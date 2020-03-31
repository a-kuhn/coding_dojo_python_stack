#CHALLENGE 1    
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#CHALLENGE 2
def iterateDictionary(listOfDictionaries):
    for i in listOfDictionaries:
        result = []
        for key, val in i.items():
            result += [f"{key} - {val}"]
        print(', '.join(result))

students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students2)

#CHALLENGE 3 -- print value for each key
def iterateDictionary2(key_name, some_list):
    key_name = str(key_name)
    for i in some_list:
        for key, val in i.items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name',students2)
iterateDictionary2('last_name',students2)

#CHALLENGE 4 -- print name of each key, size of list, print values within each key's list
def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{str(len(v))} {k.upper()}")
        for item in v:
            print(item)
        print('\n')

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
printInfo(dojo)