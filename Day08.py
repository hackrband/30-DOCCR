# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())
phonebook = {}

for _ in range(n):
    name, number = input().split()
    phonebook[name] = number

while True:
    try:
        query = input().strip()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except EOFError:
        break
