import sys

list_of_fizzbuzz = []
list_of_fizz = []
list_of_buzz = []


def fizzbuzz(range_from: int, range_to: int) -> dict:
    for i in range(range_from, range_to):
        if (i % 15 == 0):
            list_of_fizzbuzz.append(i)
        elif (i % 3 == 0):
            list_of_fizz.append(i)
        elif (i % 5 == 0):
            list_of_buzz.append(i)

    return {'fizzbuzz': list_of_fizzbuzz,
            'fizz': list_of_fizz,
            'buzz': list_of_buzz}


def show_results(func: dict):
    for title, numbers in func.items():
        print("\n" + title.upper())
        for number in numbers:
            print(number, end=" ")


if __name__ == "__main__":
    range_from = int(sys.argv[0])
    range_to = int(sys.argv[1])
    show_results(fizzbuzz(range_from,
                          range_to))
