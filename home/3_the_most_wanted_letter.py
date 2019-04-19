
def checkio(text: str) -> str:
    text = text.lower()
    total = 0
    most_wanted = ''
    for x in text:
        if x.isalpha():
            if text.count(x) > total:
                total = text.count(x)
                most_wanted = x
            elif text.count(x) == total:
                if x < most_wanted:
                    most_wanted = x
                    total = text.count(x)
    return most_wanted


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
