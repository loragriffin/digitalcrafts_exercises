class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = 0

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        self.count += 1
        print('Hello {}, I\'m {}!'.format(other_person.name, self.name))

    def greeting_count(self):
        print(self.count)

    def print_info(self):
        print(self.name + "'s email: " + self.email + ', ' + self.name + "'s phone: " + self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(self.name + "'s friends:", len(self.friends))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greeting_count()
sonny.greet(jordan)
sonny.greeting_count()
jordan.greet(sonny)

print(sonny)
print(jordan)

# jordan.friends.append(sonny)

# jordan.add_friend(sonny)
# sonny.add_friend(jordan)

# print("Jordan's friends:", len(jordan.friends))
# print("Sonny's friends:", len(sonny.friends))

# jordan.num_friends()
# sonny.num_friends()

# print("Sonny's email: ", sonny.email, "\nSonny's phone: ", sonny.phone)
# print("Jordan's email: ", jordan.email, "\nJordan's phone: ", jordan.phone)

# sonny.print_info()

class Vehicle:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def print_info(self):
        print(self.year, self.make, self.model)

cooper1 = Vehicle('2013', 'Mini', 'Cooper S')

cooper1.print_info()
