name = 'bob'
greeting = f"hello, {name}"

print(greeting)

name = 'rolf'

print(greeting)

name = 'bob'

print(f"hello, {name}")

name = 'rolf'

print(f"hello, {name}")


name = 'bob'
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hell, {}. Today is {}"
formatted = longer_phrase.format("rolf", "thursday")

print(formatted)