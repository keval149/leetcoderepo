# My First Program
#
# def main():
#     print("Hello World!")
#
# if __name__ == "__main__":
#     main()

class hello:
    def __init__(self, s: str, year: int) -> None:
        self.greeting = s
        self.year = year

    def printHello(self) -> str:
        return self.greeting + " {}".format(self.year)

obj = hello("Hello World!",2022)
result = obj.printHello()
print(result)
