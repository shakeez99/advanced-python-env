class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age  

    def introduce(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self._age} years old."

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age <= 0:
            raise ValueError("Age must be positive.")
        self._age = new_age


class Student(Person):
    def __init__(self, name: str, age: int, major: str) -> None:
        super().__init__(name, age)
        self.major = major


    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, {self.get_age()} years old, and I study {self.major}."


def main() -> None:
    p = Person("Alex", 30)
    s = Student("Dana", 18, "Computer Science")


    people: list[Person] = [p, s]
    for obj in people:
        print(obj.introduce())

 
    s.set_age(19)
    print("Updated student age:", s.get_age())

if __name__ == "__main__":
    main()
