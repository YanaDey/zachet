line = input("Введите строку:").lower()
count = 0
count_vowels = set("УЕЫАОЭЯИЮуеыаоэяию")
for letter in line:
    if letter in count_vowels:
        count += 1
print("")
print(count)
