"""A small sample script to practice editing and pushing to git."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    return a + b


def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def main() -> None:
    print(greet("World"))
    print("2 + 3 =", add(2, 3))
    print(", ".join(fizzbuzz(15)))


if __name__ == "__main__":
    main()
