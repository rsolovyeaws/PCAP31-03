domain = [1, 2, 3, 4, 5]

our_range = map(lambda num: num * 2, domain)
print(f"map(): {list(our_range)}")


evens = filter(lambda num: num % 2 == 0, domain)
print(f"filter(): {list(evens)}")

# reduce iterable into a single list
from functools import reduce
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(f"reduce(): {the_sum}")

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a .sort() method(will return new list)")
words.sort(key=str.lower)
print(words)
