import csv
import json
import os

JSON_PATH = os.path.join(os.getcwd(), 'Exercicios', 'contact_book', 'contacts.json')
CSV_PATH = os.path.join(os.getcwd(), 'Exercicios', 'contact_book', 'contacts.csv')

class Contact:

    def __init__(self, name, phone, email) -> None:
        self._name = name
        self._phone = phone
        self._email = email

    def __str__(self):
        return f'Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}'

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):  
        if not isinstance(value, str):
            raise TypeError('name must be a str')
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, int):
            raise TypeError('phone must be a int')
        self._phone = value


def contact_details():
    name = input('Name: ').capitalize()
    phone = input('Phone: ')
    email = input('Email: ')
    return Contact(name, phone, email)

def format_phone():
    phone = input('Phone: ')
    if phone.isdigit() is False:
        raise ValueError
    len_phone = len(phone)
    if len_phone == '9' or len_phone == '11':
        
    

def write_json(contacts):
    list_contacts = []
    for contact in contacts:
        list_contacts.append(contact.to_dict())
    with open(JSON_PATH, 'w', encoding='utf8') as f:
        json.dump(list_contacts, f, indent=2)

def read_json():
    try:
        with open(JSON_PATH, 'r', encoding='utf8') as f:
            file_data = json.load(f)
        contacts = [
            Contact(**item)
            for item in file_data
        ]
    except (FileNotFoundError, json.JSONDecodeError):
        write_json([])
        return []
    
    return contacts

def add_contact():
    write_json(read_json() + [contact_details()])

def list_contacts():
    contacts = read_json()
    if not contacts:
        print('No contacts found.')
        return

    print('Contacts: ')
    for index, contact in enumerate(contacts, start=1):
        print('=' * 40)
        print(f'{index}.\n{contact}')
    return

def search_contact():
    data = read_json()
    name_search =  input('Enter the name: ')
    for contact in data:
        if name_search in contact.name.capitalize():
            print('=' * 40)
            print(contact)
            return

def delete_contact():
    contacts = read_json()
    if not contacts:
        print('No contacts found!')
        return

    list_contacts()

    while True:
        try:
            index = int(input('Which contact do you want to delete? '))
            contacts.pop(index - 1)
            write_json(contacts)
            print('Contact deleted sucessfully!')
            break

        except IndexError:
            print('\nYou type out of range.')
            continue

def export_csv():
    contacts = read_json()
    with open(CSV_PATH, 'w', encoding='utf8') as f:
        columns = contacts[0].to_dict().keys()
        writer = csv.DictWriter(
            f,
            fieldnames=columns
        )
        writer.writeheader()

        for contact in contacts:
            writer.writerow(contact.to_dict())

def import_csv():
    with open(CSV_PATH, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        date = list(reader)
        contacts = [Contact(**contact) for contact in date]
        write_json(contacts)




while True:

        print('''==== CONTACT BOOK ====

    1 - Add contact
    2 - List contacts
    3 - Search contact  
    4 - Delete contact
    5 - Export to CSV
    6 - Import from CSV
    0 - Exit\n''')
        
        choice = input('Choice a option: ')

        if choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            export_csv()
        elif choice == '6':
            import_csv()
        elif choice == '0':
            break
        else:
            continue

