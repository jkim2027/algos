# reverse a list of numbers
def reverse_list(numbers):
    new_list = []
    for num in range (len(numbers)-1, -1, -1):
        new_list.append(numbers[num])
    return new_list

numbers = [3, 4, 5]
result = reverse_list(numbers)
print("The reversed list is", result)


# remove duplicates from list of numbers
def remove_duplicates(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

numbers = [1, 1, 3, 5, 5, 7]
result = remove_duplicates(numbers)
print("The list with duplicates removed is", result)

# count frequency of elements in list
def count_frequency(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key, val in count.items():
        print(key, " = ", val)

numbers = [1, 1, 3, 5, 5, 7]
result = count_frequency(numbers)
print("The frequency of each element is", result)


# Write a function that takes in a list of integers and returns the sum of all even numbers in the list.
def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_numbers)
print(result) # Output: 30



# Most repeated letter: Write a function that accepts an array of letters and returns the most repeated letter
def most_repeated(array):
    letter_count = {}
    most_repeated = 0
    for letter in array:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    for key, val in letter_count.items():
        if val > most_repeated:
            most_repeated = val
    return key



array = ['a', 'a', 'b', 'c', 'd', 'd', 'd']
print(most_repeated(array))

# Given a string containing space separated words
#   Reverse each word in the string.
#   If you need to, use .split to start, then try to do it without.

#   Input: Hello world
#   Output: olleH dlrow

def reverse_word(string):
    list = string.split()
    reversed_words = []
    for word in list:
        for x in range (len(word), 0, -1):
            reversed_words.append(word[x-1])

    print (reversed_words)




string = "Hello world"
reverse_word(string)


# Write a program that takes in a dictionary of stock prices and returns the name of the stock with the highest price.

def highest_stock(stocks):
    max_val = 0
    max_key = ""
    for key, val in stocks.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key

stocks = {
    "Microsoft": 120,
    "Amazon": 140,
    "Netflix": 130,
    "Tesla": 150,
    "Google": 120,
}
print(highest_stock(stocks))

# Expected output: Tesla


# Write a program that takes in a dictionary of student names and their corresponding test scores, and returns the 2 student names with the highest score.
def highest_scores(student_dict):
    


students = {
    "Jax": 8,
    "Janna": 7.5,
    "Ahri": 9,
    "Oriana": 9.5,
    "Caitlyn": "8.7"
}




# Given an array of ailements (illnesses), and an array of medication objects that have a nested array of treatedSymptoms
#   return the medication name(s) that treats the most given symptoms
# '''

medications = [
    {
        "name": "Sulforaphane",
        "treatableSymptoms": [
            "dementia",
            "alzheimer's",
            "cancer",
            "inflammation",
            "neuropathy",
        ],
    },
    {
        "name": "Longvida Curcumin",
        "treatableSymptoms": [
            "pain",
            "inflammation",
            "depression",
            "arthritis",
            "anxiety",
        ],
    },
    {
        "name": "Hericium erinaceus",
        "treatableSymptoms": ["anxiety", "cognitive decline", "depression"],
    },
    {
        "name": "Nicotinamide mononucleotide",
        "treatableSymptoms": [
            "ageing",
            "low NAD",
            "obesity",
            "mitochondrial myopathy",
            "diabetes",
        ],
        },
    {
        "name": "PainAssassinator",
        "treatableSymptoms": [
            "pain",
            "inflammation",
            "cramps",
            "headache",
            "toothache",
            "back pain",
            "fever",
        ],
    },
]

# ailments1 = ["pain"]
# expected1 = ["PainAssassinator", "Longvida Curcumin"]

ailments2 = ["pain", "inflammation", "depression"]
expected2 = ["Longvida Curcumin"]

# ailments3 = ["existential dread"]
# expected3 = []

# ailments4 = []
# expected4 = []

def getMeMyMeds(ailments, medications):
    new_list = []
    for medicine in medications:
        for val in medicine['treatableSymptoms']:
            if val in ailments:
                new_list.append(medicine['name'])
    return new_list

print(getMeMyMeds(ailments2, medications)) # Output: ["PainAssassinator", "Longvida Curcumin"]
