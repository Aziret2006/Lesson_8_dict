# Lesson about data type dict (Dictionary)
contacts = {'Call-Center MegaCom': '6666', 'Moi balans': '*500#'}

print(contacts)
print(contacts['Moi balans'])

contacts['Moi balans'] = '*100#'
print(contacts)

print(contacts.get('Call-Center MegaCom'))

contacts['Aibek Baike'] = '+996555111222'

print(contacts)

del contacts['Aibek Baike']

print(contacts)

########################################################

# Lesson abput data type set

first_set = set()
student_names = ['Aibek', 'Turatbek', 'Mira', 'Jide', 'Aibek']
teacher_names = ['Turatbek', 'Bibigul']
second_set = {1, 2, 3, 2}
print(first_set)
print(second_set)

print(student_names)
student_names = set(student_names)
teacher_names = set(teacher_names)
print(student_names.intersection(teacher_names))
print(student_names.difference(teacher_names))

########################################################


########################################################
# Practice

# Goal
# Project goal is save contacts and get contacts whe i want

my_contacts = {}

while True:
    action = input("""
                   Press 1 to create contact
                   Press 2 to get contact
                   Press 3 to edit contact
                   Press 4 to delete contact
                   Press 5 to exit
                   """)

    if action == '1':
        contact_name = input('Please enter contact name: ')
        contact_phone_number = input('Please enter phone number: ')

        my_contacts[contact_name] = [contact_phone_number]
        print(f'It`s okay! Contact {contact_name} was added! Thanks to use our platform!')
        print('It`s your contacts ->', ', '.join(my_contacts.keys()))

    elif action == '2':
        get_contact_name = input('Please enter contact name: ')
        contact = my_contacts.get(get_contact_name)

        if contact is not None:
            print(contact)
        else:
            print(f'It`s contact {get_contact_name} not found!')
    elif action == '3':
        find_contact = input('Please enter which contact do you want to change : ')
        contact = my_contacts.get(find_contact)
        if contact is not None:
            print(contact)
            edit_contact = input('Enter contact changes :')
            my_contacts[find_contact] = edit_contact
            print(f"Contact {find_contact} was changes")
        else:
            print('Please enter correct contact')

    elif action == '4':
        del_contact = input('Please enter contact do you want delete:')
        del my_contacts[del_contact]
        print('Your contact was removed')

    elif action == '5':
        print('See you')
        print(f'Your contacts {my_contacts}')
        break