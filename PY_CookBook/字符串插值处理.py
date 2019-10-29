import sys


class safesub(dict):
    def __missing__(self, key):
        print(key)
        return "{" + key + "}"


def sub(text):
    print(sys._getframe(1).f_locals)
    return text.format_map(safesub(sys._getframe(1).f_locals))


if __name__ == "__main__":
    s = "{name} has {n} messages."
    print(s.format(name="Guido", n=37))
    name = "GUIDE"
    n = 37
    print(sub("hello {name}"))
    print(sub("you have {n} messages."))
    print(sub("Your favorite color is {color}"))
    print(s.format_map(vars()))
