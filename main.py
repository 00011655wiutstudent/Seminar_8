#Seminar 8 Tuples
"""
student_1 = ( '00011655', 21, "Turkkurgan 5")
student_2 = ( '00011155', 20, "Turkkurgan 1")
if student_1 > student_2:
    print("First student is older")
else:
    print("Second student is older")


addr = 'info@wiut.uz'
uname, domain = addr.split('@')
print(uname +"\n" + domain)

my_tuple = ( 'A', 'B', 'C')

for i in enumerate(my_tuple):
 print(i)
"""
def get_longest_word(list_of_words):
    dictionary = dict()
    for word in list_of_words:
        i = 0
        for character in word:
            i = i + 1
        dictionary[word] = i
    values = []
    for word in list_of_words:
        values.append(dictionary[word])
    values.sort(reverse=True)
    for word in list_of_words:
        if dictionary[word] == values[0]:
            biggest = word
    print(biggest, values[0])

list_a = ('madina', 'Tolibjonova', 'and')
get_longest_word(list_a)


