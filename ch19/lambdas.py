# sorting by a custom key
# sorts by length of name
names = ['Alice', 'Bob', 'Charlie']
names.sort(key=lambda name: len(name))

words = ["banana","pie","Washington","book","zebra"]
words.sort(key=lambda w: len(w))

print(words)

# filtering a list
# keeps only even numbers
nums = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0, nums))

numbers = [3, 10, 7, 2, 8, 1, 9, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

# finding the maximum by a property
students = [{'name': 'Ann', 'score': 90},{'name': 'Ben','score': 85}]
top_student = max(students, key=lambda s: s['score'])

# using map to square the same variable
numbers = [1,2,3,4,5,6]
squar = list(map(lambda x: x * x, numbers))

print(squar)