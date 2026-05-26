# Given a list of integer, create a function that returns an object with the amount of odd, even and total

class Numbers:
    def __init__(self, array_):
        self._odd_numbers = [n for n in array_ if self._is_odd(n)]
        self._total_odd_numbers = len(self._odd_numbers)
        self._even_numbers = [n for n in array_ if not self._is_odd(n)]
        self._total_even_numbers = len(self._even_numbers)
        self._total_numbers = self._total_odd_numbers + self._total_even_numbers

    def _is_odd(self, n):
        return n % 2 == 0

    def __str__(self):
        print(
            f"Total numbers: {self._total_numbers} | "
            f"Total odd numbers: {self._total_odd_numbers} | "
            f"Total even numbers: {self._total_even_numbers}"
        )

def main():
    array = range(1, 101)
    print(Numbers(array))


if __name__ == '__main__':
    main()