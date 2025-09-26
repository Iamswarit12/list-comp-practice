num = int(input("\nEnter a number that is > -1 : "))
if num <= -1:
    print("No negative numbers numbers!")

odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_work = [x for x in odd_list if x < num]
print("\nbefore =", odd_list)
print("after =", odd_work)

even_work = [x for x in even_list if x < num]
print("\nbefore =", even_list)
print("after =", even_work)

f = input("\nEnter 'next' to see what is next : ")
if f == 'next' or 'Next' or 'NEXT':
    print("\nfruit conversion")
else:
    print("Do you no want to see what is next?")

fruits = ["apple", "watermelon", "banana"]

fruit_conversion = [x.capitalize() for x in fruits]

print("\n")
print("The original fruits")
print(["apple", "watermelon", "banana"])
print()
print("The new upper-case fruits")
print(fruit_conversion)
print("\n")