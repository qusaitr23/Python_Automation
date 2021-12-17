class Family:
    family_name = 'Flenner'


class Child1(Family):
    first_name = 'Yoni'


class Child2(Family):
    first_name = 'Guy'


child1 = Child1()
print(child1.family_name + ' ' + child1.first_name)

child2 = Child2()
print(child2.family_name + ' ' + child2.first_name)