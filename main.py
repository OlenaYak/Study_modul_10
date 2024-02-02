from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): 
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_valid()

    def phone_valid(self):
        if self.value is not None:
            if len(self.value) != 10 or not self.value.isdigit():
                raise ValueError("Incorrect number: phone must contain 10 digit!")
        
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)                 
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for element in self.phones:
            if element.value == phone_number:
                self.phones.remove(element)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                new_phone_check = Phone(new_phone)
                new_phone_check.phone_valid()
                phone.value = new_phone
                return
        raise ValueError(f'{old_phone} not exist')

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record): 
        self.data[record.name.value] = record

    def find(self, name):
        result = self.data.get(name)
        return result
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == '__main__':
    book = AddressBook()



    
