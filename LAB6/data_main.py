from data_package import analyzer
from data_package import cleaner

print("Enter a comma-separated list of numbers: ")

numbers = input()

numbers = numbers.split(",")

numbers = cleaner.strip_whitespaces(numbers)
numbers = cleaner.remove_duplicates(numbers)


try:
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Data error, make sure you only enter numbers separated by commas")
    exit()

print("Cleaned and unique data: ", numbers)
print("---------------")

print("Mean: ", analyzer.calculate_mean(numbers))
print("Maximum: ", analyzer.find_maximum(numbers))
print("Minimum: ", analyzer.find_minimum(numbers))