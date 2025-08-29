t = int(input().strip())
for _ in range(t):
    s = input().strip()
    even_chars = s[0::2]  # Start at 0, take every 2nd character
    odd_chars = s[1::2]   # Start at 1, take every 2nd character
    print(f"{even_chars} {odd_chars}")
