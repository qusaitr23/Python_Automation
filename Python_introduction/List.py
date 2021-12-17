countries = ["Greece", "India", "USA", "England", "Austria"]

# solution 01
print(countries[:3])

# solution 02
country = countries[0]
countries[0] = countries[1]
countries[1] = country
print(countries)

# solution 03
countries.reverse()
print(countries)

# solution 04
countries.sort()
print(countries)

# solution 05
last_index = len(countries) - 1
last_country = countries[last_index]
# Use pop
countries.pop(last_index)
# Use Remove
countries.remove(last_country)
print(countries)

# solution 06
middle_index = len(countries) / 2
countries.insert(int(middle_index), "Israel")
print(countries)