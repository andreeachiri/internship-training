def say_hello(name, shout=False):
    greeting = 'Hello ' + name
    if shout:
        greeting = greeting.upper()
    return greeting


print(say_hello('world'))
print(say_hello('jimmy', True))
print(say_hello(name='bond', shout=True))
