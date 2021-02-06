def fizzbuzz(start, end):
    for x in range(start, end + 1):
        result = ""
        if x % 3 == 0:
            result += "Fizz"
        if x % 5 == 0:
            result += "Buzz"
        if result == "":
            result = str(x)
        yield result
