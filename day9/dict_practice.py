dict = {
    "Jerrick": 14,
    "Fio": 11,
}

# print(dict)
# print(dict["Jerrick"])

# add new element
dict["Sam"] = 9
# print(dict)

# overriding value
dict["Fio"] = 10
# print(dict)

# loop through dictionary
for key in dict:
    print(f"key: {key}, value: {dict[key]}")


fruits = ["Apple", "Mango"]
print(fruits[1])

fruits_dict = {
    0: "Apple",
    1: "Mango"
}
print(fruits_dict[1])

fruits_dict[2] = "Pears"
print(f"fruits: {fruits_dict}")

