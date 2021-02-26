def main():
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
    sum = 0
    fib1 = 1
    fib2 = 0
    fib3 = 0
    while fib3 < 4000000:
        fib3 = fib2 + fib1
        fib1 = fib2
        fib2 = fib3

        if fib3 % 2 == 0:
            sum += fib3

    print("By considering the terms in the Fibonacci sequence whose values do not exceed four million, the sum of the even-valued terms is: {}".format(sum))

if __name__ == "__main__":
    main()