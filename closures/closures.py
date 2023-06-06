def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Robert")
goodbye("Chad")
