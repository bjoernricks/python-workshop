output = "Hello world"

print(output[0:5])  # prints out Hello
print(output[6:11])  # prints out world
print(output[0:1])  # prints out H
print(output[6:7])  # prints out w

print(output[6:-1])  # prints out worl
print(output[-11:-5])  # prints out Hello

print(output[6 : len(output)])  # prints out world
print(output[6:])  # prints out world

print(output[:5])  # prints out Hello

print(output[:])  # prints out Hello world

print(output[0:100])  # no exception, prints out Hello world
print(output[100:])  # no exception, prints out empty string
