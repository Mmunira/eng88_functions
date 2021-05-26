# Fizzbuzz
# The Problem
#
# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
#
# NOTE -> Must be in class and method format

class Fizzbuzz:
    def buzz_of_the_fizz(self, required_range):
        for number in range(required_range + 1):
            if number % 3 == 0 and number % 5 == 0:
                print('FizzBuzz')
            elif number % 3 == 0:
                print('Fizz')
            elif number % 5 == 0:
                print('Buzz')
            else:
                print(number)
fizzbuzz_checker = Fizzbuzz()
fizzbuzz_checker.buzz_of_the_fizz(100)
