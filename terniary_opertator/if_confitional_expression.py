# my_var = 1 if CONDITION else 2
# This syntax isn't restricted to variable assignment, but it is a common usage. If we wanted to print a different message based on a condition we can also do that using a conditional expression:

print("something") if 1 > 2 else print("something else")

# Or if we want to simplify this further, we could let the conditional expression return the value directly to the print function:
print("something" if 2 > 1 else "something else")