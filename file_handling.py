import os


def create_file():
    try:
        file_name = input("Enter file name to created: ").lower().strip()
        with open(file_name, "w") as file:
            print(f"File '{file_name}' created successfully. ")

    except Exception as e:
        print(f"Failed to create file.Error: {e} ")


def delete_file():
    file_path = "coding.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully. ")
    else:
        print("File not found. ")


while True:
    print("\nChoose Option")
    print("1. Create file")
    print("2. Delete file")
    print("3. Exit")

    choose_option = input("Enter an option: ").strip()
    if choose_option == "1":
        create_file()

    elif choose_option == "2":
        delete_file()

    elif choose_option == "3":
        print("exiting.. ")
        break
    else:
        print("Invalid input. ")

# ++++++++++++++++++++++++++++++++++++++++++++
name = input("Enter your name: ").capitalize()
age = input("Enter your age: ")

with open("example.txt", "w") as file:
    file.write(f"Name: {name}, Age: {age}")

with open("example.txt", "r") as f:
    print("Reading from file...")
    content = f.read()
    print(content)

# +++++++++++++++++++++++++++++++++++++++

m1 = input("Enter movie 1: ").title()
m2 = input("Enter movie 2: ").title()
m3 = input("Enter movie 3: ").title()
with open("movie.txt", "w") as file:
    file.write(f"{m1}\n{m2}\n{m3}")

with open("movie.txt", "r") as f:
    print("Reading from file...")
    for movie in f:
        print(movie.strip())

# ++++++++++++++++++++++++++++++++++++++++
st = []
count = 3
for i in range(count):
    student = input(f"Enter student {i + 1}: ").title().strip()
    st.append(student)

with open("student.txt", 'w') as f:
    f.write(f"{st}")

search = input("Enter name to search: ").capitalize()
with open('student.txt', 'r') as file:
    content = file.read()
    if search in content:
        print(f"{search} is in the list!")
    else:
        print("Not found.")

# +++++++++++++++++++++++++++++++++++++++++++

import os

nt = []
file_path = "notes.txt"
limit = int(input("Enter range: ").strip())
for i in range(limit):
    notes = input("Enter your notes: ").capitalize().strip()
    nt.append(notes)

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("\n".join(nt) + "\n")

else:
    with open(file_path, "a") as f:
        f.write("\n".join(nt) + "\n")


with open("notes.txt", 'r') as file:
    print("Reading all notes...")
    content = file.read()
    print(content)


# +++++++++++++++++++++++++++++++++++++++

print("File Content: ")
with open("data.txt", 'r') as f:
    content = f.read()
    words = content.split()
    print("Total words: ", len(words))

# ++++++++++++++++++++++++++++++++++++
import string
from collections import Counter

with open("data.txt", 'r') as f:
    content = f.read()

content = content.lower()
for p in string.punctuation:
    content = content.replace(p, "")

print(content)

words = content.split()
word_count = Counter(words)

most_count = word_count.most_common(1)[0]
print(f"Total most common word: '{most_count[0]}' {most_count[1]} time")

# ++++++++++++++++++++++++++++++++++++++++
import string
from collections import Counter

with open("data.txt", 'r') as f:
    content = f.read()

content = content.lower()
for p in string.punctuation:
    content = content.replace(p, "")

words = content.split()
word_count = Counter(words)

most_common = word_count.most_common(3)
print("Top 3 most common words: ")
for word, count in most_common:
    print(f".{word} ({count} time)")


## +++++++++++++++ CSV file handling +++++++++++++++++++++++++++
import csv

data = [
    ['Name', 'Age', 'Grade'],
    ['Ali', 80, 'A'],
    ['Ahmed', 79, 'B'],
    ['Hamza', 90, 'A+']
    ]
with open("student.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Data sent successfully. ")

with open("student.csv", 'r') as f:
    reader = csv.reader(f)
    for raw in reader:
        print(" _|_ ".join(raw))

# +++++++++++++++++++++++++++++++++++++++++++
import csv
with open('sales.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        price = int(row["Price"])
        quantity = int(row["Quantity"])
        total = price * quantity
        print(f"{row["Product"]} -> {total}")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++
import csv

highest_marks = 0
top_student = ""

with open("marks.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["Name"]
        math = int(row["Math"])
        science = int(row["Science"])
        eng = int(row["English"])
        total_marks = eng + math + science
        if total_marks > highest_marks:
            highest_marks = total_marks
            top_student = name
print(f"Highest scoring student name: {top_student} with {highest_marks} marks.")

# ++++++++++++++++++++++++++++++++++++++++++++

import csv
revenue = 0
with open("product.csv", 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
        price = int(row['Price'])
        quantity = int(row['Quantity'])
        total = price * quantity
        revenue += total
    print(f"Grand total: {revenue}")

# ++++++++++++++++++++++++++++++++++
import csv

total_temperature = 0
days_count = 0

with open('temperature.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        total_temperature += float(row['Temperature'])
        days_count += 1

avg_temp = total_temperature / days_count
print(f"Average Temperature for this week: {avg_temp:.2f}*C")