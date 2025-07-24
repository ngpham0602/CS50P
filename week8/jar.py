class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("There's more cookies than the jar needed!")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("You take way too many cookies that the jar have!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    try:
        jar = Jar()
        user1 = int(input("How many cookies do you want to add in: "))
        jar.deposit(user1)
        user = int(input("How many cookies that you want to take out: "))
        jar.withdraw(user)
    except ValueError as e:
        print(f"{e}")
    return jar


if __name__ == "__main__":
    main()