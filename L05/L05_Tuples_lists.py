####====9.1-----
###1, 2, 3, 4, 5
##cardinals_numb = ('first', 'second', 'third')
##print(cardinals_numb[1])
##pos1, pos2, pos3 = cardinals_numb
##print(f"{pos1}\n{pos2}\n{pos3}")
##
##my_name = tuple('Pawel')
##print(my_name)
##print(tuple('MaStoDOnt'.lower()))
##
##
##print('a' in my_name)
##print('d' in my_name)
##
##
##new_NM = my_name[1:(len(my_name))]
##
##
###---9.2--------
###1 - 8
##food = ['rice', 'beans']
##food.append('broccoli')
##food.extend(['bread', 'pizza'])
##print(food[0:2])
##print(food[len(food)-1])
##
##breakfast = 'eggs, fruit, orange juice'
##breakfast_list = breakfast.split(', ')
##len(breakfast_list)
##for n in breakfast_list:
##    print(len(n))
##
###-----9.4 Challenge======
##

uni = [['CIT', 2175, 37704], ['Harvard', 19627, 39849],
       ['MIT', 10566, 40732], ['Priceton', 7802, 37000],
       ['Rice', 5879, 35551],['Stanford', 19535, 40569], ['Yale', 11701, 40500]]
##def get_Uni_name(item):
##    return item[0]
##list_of_names = []
##for n in uni:
##    list_of_names.append(get_Uni_name(n))
##
##print(list_of_names)
##
number_of_students = []
def get_nr_of_stud(uni):
    for n in uni:
        number_of_students.append(n[1])
    return (sum(number_of_students))
    
list_of_fees = []
def get_list_of_fees(uni):
    for n in uni:
        list_of_fees.append(n[2])
    return (sum(list_of_fees))
    
def enrollment_stats(uni):
    
    
    print(f"Number of students: {get_nr_of_stud(uni)}, value of fees: {get_list_of_fees(uni)}")

    
    
##def enrollment_stats(uni):
##    for n in uni:
##        number_of_students.append(get_nr_of_stud(n))
##print(number_of_students)
    
