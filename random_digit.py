import random

class RandomDigitGenerator:
    def __init__(self, n):
        self._n = n
        self._digits = list(map(lambda digit: str(digit), list(range(10))))
        while self._digits[0] == '0':
            random.shuffle(self._digits)

    def get_random_digits(self):
        return list(self._digits[:self._n])

if __name__ == '__main__':
    digit_generator = RandomDigitGenerator(3)
    print(digit_generator.get_random_digits())
    print()
    
    for index, i in enumerate(range(10), start=1):
        print(index, RandomDigitGenerator(3).get_random_digits())
    print()
