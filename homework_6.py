array = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]

n = 6
arrayy = []

def group(array, n):
    if n == '':
        n = 3
        for i in range(0, len(array), n):
            arrayy.append(array[i:i+n])
        print(arrayy)

    else:
        for i in range(0, len(array), n):
            arrayy.append(array[i:i+n])
        print(arrayy)

group(array, n)