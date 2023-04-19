output = "Hello world"
print(output.upper())
print(output.lower())

print(output.startswith("Hello"))  # prints out True
print(output.startswith("hello"))  # prints out False
print(output.endswith("d"))  # prints out True
print(output.startswith("World"))  # prints out False

print(output.find("orl"))


splitted = output.split(" ")  # returns a list
print(splitted)
type(splitted)

print(splitted[0])

ip_address = "10.10.10.10"
ips_split = ip_address.split(".")
print(ips_split[3])
