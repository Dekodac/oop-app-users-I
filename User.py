class User():
    def __init__(self, name, dl, email):
        self.name = name
        self.email = email
        self.dl = dl

    def __str__(self):
        return f"Name: {self.name}, DL: {self.dl}, Email: {self.email}"

person1 = User("Matt", "23rhai3HD", "MattBleater394@aol.com")
person2 = User("Pete", "2grrga3HD", "Peteskete@hotmail.com")
person3 = User("S1mple", "2s4rfw23f", "S1mpleCsgo@microsoft.com")

print(person1)
print(person2)
print(person3)
