# Pythonic Fundamentals: Daily One-Hour Review Guide

> "I wish I knew this earlier." — Every Python developer, eventually.

Review one section per day. Rotate through them. The goal is not to finish — it is to keep these ideas active in your mind.

---

## How to Use This Guide

- Spend **~60 minutes** per session
- Read the concept (10 min)
- Write an example from memory — no copying (20 min)
- Try a small variation or experiment (20 min)
- Write one sentence summarizing what you practiced (10 min)

---

## Day 1 — Naming Things Well

Bad names are one of the most common beginner regrets.

```python
# Regret version
x = [1, 2, 3]
def f(a, b):
    return a + b

# Better
prices = [1, 2, 3]
def add_prices(subtotal, tax):
    return subtotal + tax
```

**Wish I knew:** Code is read far more often than it is written. Name things for the reader, not the typist.

**Daily practice:** Pick one variable or function name you wrote recently and improve it.

---

## Day 2 — Understanding Mutability

One of the most common sources of bugs for beginners.

```python
# Dangerous default argument — a famous Python gotcha
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] — not what you expected

# Correct version
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```

**Wish I knew:** Never use a mutable object (list, dict) as a default argument.

**Daily practice:** Write a function with a `None` default and initialize inside.

---

## Day 3 — List Comprehensions Over Loops (When Appropriate)

```python
# Loop version
squares = []
for x in range(10):
    squares.append(x * x)

# Comprehension version
squares = [x * x for x in range(10)]

# With filtering
even_squares = [x * x for x in range(10) if x % 2 == 0]
```

**Wish I knew:** Comprehensions are not just shorter — they express *intent* more clearly. But if the logic gets complex, a loop is cleaner.

**Daily practice:** Rewrite one loop you've written before as a comprehension.

---

## Day 4 — `enumerate()` Instead of Manual Counters

```python
# Regret version
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

# Pythonic version
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

**Wish I knew:** `enumerate()` exists for exactly this. Manual index counters are a sign you haven't discovered it yet.

**Daily practice:** Find a place in your code where you used a counter. Replace it.

---

## Day 5 — `zip()` for Parallel Lists

```python
names = ["Alice", "Bob", "Carol"]
scores = [88, 95, 72]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Wish I knew:** Pairing two lists with an index is almost always a sign `zip()` should be used.

**Daily practice:** Create two related lists and combine them with `zip()`.

---

## Day 6 — f-Strings Are the Standard Now

```python
name = "Alice"
score = 95

# Old ways (avoid)
print("Name: " + name + ", Score: " + str(score))
print("Name: %s, Score: %d" % (name, score))
print("Name: {}, Score: {}".format(name, score))

# Modern and clean
print(f"Name: {name}, Score: {score}")
```

**Wish I knew:** f-strings (Python 3.6+) are readable, fast, and the community standard. Use them everywhere.

**Daily practice:** Rewrite any old string formatting you find using f-strings.

---

## Day 7 — Dictionary `.get()` Instead of Direct Access

```python
user = {"name": "Alice", "age": 30}

# This crashes if key doesn't exist
print(user["email"])  # KeyError

# Safe version
print(user.get("email", "no email on file"))
```

**Wish I knew:** Direct key access is fine when you *know* the key exists. Use `.get()` when you are not sure.

**Daily practice:** Write a dictionary lookup using `.get()` with a meaningful default.

---

## Day 8 — Functions Are Values (First-Class Objects)

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def deliver(func, message):
    print(func(message))

deliver(shout, "hello")    # HELLO
deliver(whisper, "HELLO")  # hello
```

**Wish I knew:** Once you understand that functions can be passed around like data, `map()`, `filter()`, and callbacks all make sense.

**Daily practice:** Write a function that takes another function as a parameter.

---

## Day 9 — `map()`, `filter()`, and When to Use Them

```python
products = [
    {"name": "pen", "price": 2},
    {"name": "notebook", "price": 5},
    {"name": "backpack", "price": 25},
]

# filter: keep only items costing 5 or more
filtered = list(filter(lambda item: item["price"] >= 5, products))

# map: extract just the names
names = list(map(lambda item: item["name"], filtered))

# sorted: order by name length
result = sorted(names, key=lambda name: len(name))
```

**Mental shortcut:**
- `map` → What should this become?
- `filter` → Should I keep this?
- `sorted` → What should I sort by?

**Daily practice:** Write one pipeline using all three on a list of your choosing.

---

## Day 10 — Lambda Is Just a Nameless Function

```python
# These are equivalent
lambda x: x * 2

def double(x):
    return x * 2
```

**Wish I knew:** A lambda is not magic. It is just a function with no name and no `return` keyword. The expression after `:` is returned automatically.

**Daily practice:** Write a lambda, then rewrite it as a `def`. Then decide which reads better.

---

## Day 11 — Unpacking

```python
# Basic unpacking
a, b, c = [1, 2, 3]

# Swap without a temp variable
x, y = 10, 20
x, y = y, x

# Star unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

**Wish I knew:** Python's unpacking eliminates a huge amount of index-based access. Use it.

**Daily practice:** Unpack a list or tuple in at least two different ways.

---

## Day 12 — `with` Statements for File Handling

```python
# Regret version — easy to forget to close
f = open("file.txt")
data = f.read()
f.close()

# Correct version
with open("file.txt") as f:
    data = f.read()
# File is automatically closed here, even if an error occurs
```

**Wish I knew:** Always use `with` for file operations. It handles cleanup even when things go wrong.

**Daily practice:** Open and read a file using `with`. Write something to a new file using `with`.

---

## Day 13 — Exceptions: Catch Specific Ones

```python
# Dangerous — hides all errors
try:
    result = int(user_input)
except:
    print("something went wrong")

# Correct — catch what you expect
try:
    result = int(user_input)
except ValueError:
    print("that was not a valid number")
```

**Wish I knew:** A bare `except` catches everything — including bugs you want to know about. Always name the exception.

**Daily practice:** Write a `try/except` block that handles two different specific exceptions.

---

## Day 14 — `any()` and `all()`

```python
scores = [88, 95, 72, 60]

print(any(s >= 90 for s in scores))   # True — at least one is 90+
print(all(s >= 60 for s in scores))   # True — all passed
print(all(s >= 90 for s in scores))   # False — not all are 90+
```

**Wish I knew:** These replace many manual loops. Once you know them, you reach for them constantly.

**Daily practice:** Replace a loop that checks a condition with `any()` or `all()`.

---

## Day 15 — Truthy and Falsy Values

```python
# These are all falsy in Python
False, None, 0, 0.0, "", [], {}, set()

# You do not need to write == [] or == ""
if not my_list:
    print("list is empty")

if username:
    print(f"welcome, {username}")
```

**Wish I knew:** Python evaluates most empty containers and zero-like values as `False`. Writing `if len(my_list) == 0` is longer and less Pythonic than `if not my_list`.

**Daily practice:** Rewrite three conditionals to use truthiness directly.

---

## Day 16 — String Methods Worth Memorizing

```python
text = "  Hello, World!  "

text.strip()           # remove whitespace from both ends
text.lower()           # all lowercase
text.upper()           # all uppercase
text.split(", ")       # split into list
", ".join(["a", "b"]) # join list into string
text.replace("World", "Python")
text.startswith("  He")
text.endswith("!  ")
"42".zfill(5)          # '00042' — pad with zeros
```

**Wish I knew:** These methods handle 90% of common string tasks. You rarely need to write character-by-character logic.

**Daily practice:** Take a messy string and clean it using at least three methods.

---

## Day 17 — Writing Functions That Do One Thing

```python
# Regret version — does too much
def process_order(order):
    # validates, calculates, prints, saves — all at once
    ...

# Better
def validate_order(order): ...
def calculate_total(order): ...
def print_receipt(order): ...
def save_order(order): ...
```

**Wish I knew:** A function that does one thing is easier to test, debug, reuse, and explain. If you cannot describe a function in one sentence, it probably does too much.

**Daily practice:** Find a long function you've written and split it into two smaller ones.

---

## Day 18 — `sorted()` vs `.sort()`

```python
numbers = [3, 1, 4, 1, 5]

# .sort() modifies the original list — returns None
numbers.sort()

# sorted() returns a new list — original unchanged
ordered = sorted(numbers)
ordered_desc = sorted(numbers, reverse=True)
```

**Wish I knew:** `.sort()` is in-place and returns `None`. Many beginners write `numbers = numbers.sort()` and wonder why they get `None`.

**Daily practice:** Use both and observe the difference clearly.

---

## Day 19 — Reading Error Messages Properly

```python
# When you see a traceback, read it bottom-up
# The last line is the actual error
# The lines above show where it came from

Traceback (most recent call last):
  File "main.py", line 10, in <module>
    result = divide(10, 0)
  File "main.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero
```

**Wish I knew:** The error type and message at the bottom tells you *what* went wrong. The traceback tells you *where*. Start at the bottom.

**Daily practice:** Deliberately cause three different errors and read each traceback carefully.

---

## Day 20 — Revisit and Consolidate

On this day, do not learn anything new.

1. Pick any three days from this guide at random.
2. Write the examples from memory — no looking.
3. If you struggle with one, that is your focus for the next cycle.

**Wish I knew:** Review is where learning becomes permanent. Most beginners only move forward. The ones who get good also look back.

---

## Closing Principle

> The goal is not to know Python. The goal is to think clearly in Python.

Every concept in this guide is just a sharper tool for expressing clear thinking. Keep rotating through this guide. Each pass will reveal something you missed before.
