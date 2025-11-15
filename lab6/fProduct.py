import sys

GPA_MAP = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0.00
}

n = int(sys.stdin.readline())
students = []

for _ in range(n):
    data = sys.stdin.readline().split()

    last = data[0]
    first = data[1]
    m = int(data[2])
    grades = data[3:]

    total_weight = 0.0
    total_credits = 0

    for i in range(0, len(grades), 2):
        g = GPA_MAP[grades[i]]
        c = int(grades[i + 1])
        total_weight += g * c
        total_credits += c

    gpa = total_weight / total_credits
    students.append((gpa, last, first))

# ✅ Самая быстрая сортировка: Timsort (встроенная)
students.sort(key=lambda x: (x[0], x[1], x[2]))

for gpa, last, first in students:
    print(f"{last} {first} {gpa:.3f}")
