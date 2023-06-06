# Certified Associate in Python Programming Certification (PCAP 31-03)

## Defining and Using Lambdas

Sometimes we want to group some lines of code so that they can be reused, but creating a named function feels unnecessary. In these situations, such as when we're acting on the items of a collection, we can use lambdas or "lambda expressions" to create anonymous functions. In this lesson, we'll learn how to create and use lambdas.

Documentation For This Video
Lambda Expressions (https://docs.python.org/3/reference/expressions.html#lambda)

An anonymous function refers to a function that doesn't have a name. If we try to classify what makes a function, we can break it into a few requirements:

A name
A list of parameters
A function body
An optional return value

The name portion is only a requirement so that we can reference it later. But if we want a "function" that isn't useful anywhere else besides the current context, we can define a function without a name by using the lambda keyword to create a "lambda expression". We could still assign it to a variable if we want. There is one catch: the lambda's body can only be one expression.

```
lambda name: expression
```



### map() / reduce() / sorted() Using Collection Functions


When thinking of times where we might want to use a lambda function, we’ll also want to think about when we might want to repeat a single expression. The most common example is when we want to process a collection using a function that can also take a function as an argument. Some examples of functions like these are:

map (https://docs.python.org/3/library/functions.html#map)
filter (https://docs.python.org/3/library/functions.html#filter)
reduce (https://docs.python.org/3/library/functions.html#reduce)
reversed (https://docs.python.org/3/library/functions.html#reversed)
sorted (https://docs.python.org/3/library/functions.html#sorted)


There's also the sort method (https://docs.python.org/3/library/stdtypes.html#list.sort) on the list type.

Documentation For This Video

Lambda Expressions (https://docs.python.org/3/reference/expressions.html#lambda)


What are "Higher-Order Functions"?
When a function or method takes a function as an argument (or returns a function), it is called a "higher-order function". This term isn't explicitly mentioned anywhere in the PCAP syllabus, but it is worth knowing. Most of the higher-order functions that we'll be working with take a collection and a function as parameters so that each item in the collection can be processed by the function argument.

Let's start digging into some of these functions.


The map Function
In mathematics, a list of potential arguments for a function is called a "domain" and for each domain there's a corresponding "range" of the same length that is the return value of the function given each item in the domain. The map function (https://docs.python.org/3/library/functions.html#map) takes a function as the first argument and a collection that acts as the domain. It returns the range. Now that we have the math talk out of the way, let's see this in practice by creating a file called collection_funcs.py:

~/lambdas-and-collections/collection_funcs.py

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain)
print(list(our_range))


Note that the result of map is an iterable, but it is not a list, so it wouldn't print out the way we'd like. So we need to first convert it to a list.

The function we're mapping over doubles the provided number. Let's run this file to see what is printed.

$ cd ~/lambdas-and-collections
$ python3.7 collection_funcs.py
[2, 4, 6, 8, 10]


The filter Function
Like map, the filter function takes a function and a collection. However, instead of returning the result of the function argument for each item, it returns an iterator that contains only the values from the list if the function returns a true result when using that value as an argument. This allows us to filter the collection based on a specific condition.

Let's give it a shot by filtering a list down to only return results that are even:

~/lambdas-and-collections/collection_funcs.py

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))


Now we can run this and we should see the two even values returned:

$ python3.7 collection_funcs.py
[2, 4, 6, 8, 10]
[2, 4]


The reduce Function
The reduce function (https://docs.python.org/3/library/functions.html#reduce)is not quite as straight forward as map and filter. When we reduce a collection, we're going to utilize the values within the collection to eventually create a final single result. An example of a function that reduces the list is the sum function, which returns the result of all the items in a list being added together. To make this possible, we need an extra argument: a starting value. We also need the function that we pass to the reduce function to take two arguments: the accumulated value and the current item from the collection.

To help solidify these ideas, let's reimplement sum by using reduce. The reduce function used to be a built-in function but was moved into the functools module in Python 3, so we'll need to import that module to use the function. We haven't covered importing modules yet, but we will in the coming section. For the time being, just copy the from ... line of code and know that it gives us access to the reduce function:

~/lambdas-and-collections/collection_funcs.py

from functools import reduce

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)


Let's break down our lambda. Whatever is returned by the lambda's expression will be used as the acc value of the next iteration. For this to work, we need to have an initial value for acc, and that's what the third argument is. By setting our initial value to 0, we can perform the addition on the first iteration. From that point on, we'll be able to continue adding to the previous result.


Sorting Functions and Methods

In the PCEP course, we covered the sorted and reversed functions, but we never talked about the key parameter. While not entirely obvious based on the parameter name, the key parameter takes a function that each item in the collection will be processed with before the comparison is run to determine the order. The list.sort method also has a key parameter, but unlike the sorted function, the list will be changed in-place.

To demonstrate how the key parameter can be useful, let's take a look at how it can be used to alphabetize a list of words:

~/lambdas-and-collections/collection_funcs.py

from functools import reduce

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))


We can see here that the default sorted result is:

['Alfred', 'Boss', 'Daemon', 'a', 'dig', 'fig']


This isn't quite what we're wanting. By passing in a key function that converts strings to lowercase before making the comparison, we're able to get a more accurate result:

['a', 'Alfred', 'Boss', 'Daemon', 'dig', 'fig']


Finally, let's sort the words list in place using the list.sort method:

~/lambdas-and-collections/collection_funcs.py

from functools import reduce

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)


This last example shows us passing the str.lower method as the key, instead of creating a lambda that does this. While they are a little confusing, the following lines are equivalent:

'my_STR'.lower()
str.lower('my_STR')


Now we have a better idea of how we can pass functions and lambdas to other functions.