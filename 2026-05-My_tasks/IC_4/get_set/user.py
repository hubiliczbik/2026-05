class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, new_first_name):
        clean = new_first_name.strip()
        if clean == "":
            raise ValueError("first name cannot be blank")
        else:
            self._first_name = clean.capitalize()

    @last_name.setter
    def last_name(self, new_last_name):
        clean = new_last_name.strip()
        if clean == "":
            raise ValueError("last name cannot be blank")
        else:
            self._last_name = clean.capitalize()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


u = User(" adam ", " kowalski ")

print(u.first_name)  # Adam
print(u.last_name)   # Kowalski
print(u.full_name)   # Adam Kowalski
