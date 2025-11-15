import sys 

GPA_MAP = {
    "A+": 4.0 , 
    "A": 3.75,
    "A-": 3.67,
    "B+": 3.33 ,
    "B": 3.00 ,
    "B-": 2.67,
    "C+": 2.33 ,
    "C": 2.0,
    "C-":1.67 ,
    "D+": 1.33 ,
    "D":1.00 ,
    "F":0.00,
}
#So I have n lines of Students 
#where first name and last name as keys 
#then I have mark of gpa's as dictionary where A = 4.0 
#and before that I have number of credits 
#first sub task I mean known subtask is to calculate gpa 

def calculate_GPA(credits , gpa_of_one_Subject , amount_of_subjects ):
    curr_gpa = (credits * gpa_of_one_Subject) // amount_of_subjects 
    return curr_gpa 

#and every time I receive gpa I collect them 
#so lets make an arr or dictionary maybe would 
#where I save by name and gpa 
#have no idea unfornately( 
#also I have to sort them in asc order so let's sort by gpa 

def quick_sort(arr):
    if len(arr) < 2:
        return arr 
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x[0] , x[1] , x[2]) < (pivot[0] , pivot[1] , pivot[2])]
    mid = [x for x in arr if (x[0] , x[1] , x[2]) == (pivot[0] , pivot[1] , pivot[2])]
    right = [x for x in arr if (x[0] , x[1] , x[2]) > (pivot[0] , pivot[1] , pivot[2])]
    return quick_sort(left) + mid + quick_sort(right)

#actually the Algo part here is done but I have some troubles with reading and getting info and also returning part(( 
#I mean if it would be GOalang I would definetly use structres to handle everythign of that 

n = int(sys.stdin.readline().strip())
students = []

for _ in range (n):
    data = sys.stdin.readline().strip()
    
    lastname = data[0]
    firstname = data[1]
    m = int(data[2])

    grades = data[3:]
    total_weight = 0
    toal_credits = 0 

    for i in range(0 , len(grades) , 2):
        g = GPA_MAP[grades[i]]
        c = int(grades[i+1])
        total_weight = g * c 
        total_credits += c 

    gpa = total_weight / toal_credits 
    students.append((gpa , lastname , firstname)) 

students = quick_sort(students)

for gpa , last , first in students:
    print(f"{last} {first} {gpa:.3f}")
