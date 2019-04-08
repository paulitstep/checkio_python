
def say_hi(name: str, age: int) -> str:

    return f'Hi. My name is {name} and I\'m {age} years old'


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    assert say_hi("Paul", 27) == "Hi. My name is Paul and I'm 27 years old", "Third"
    print('Done. Time to Check.')
