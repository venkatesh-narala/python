
#dict_using grade calculate 

marks ={}

# enter no of subjects

n = int ( input( "enter no of subjects :"))

# define subjects and marks

for _ in range(n ):
    subject = (input("enter the subject name :"))
    score= float(input(f"enter the marks of {subject}:"))

    marks [subject]=score # define dictnary into subject name and score 

#calculate the total marks and average marks

total_marks=sum(marks.values())
average_marks=total_marks/n

#define grades

if average_marks>=90:
    grade = "A"
elif average_marks>=80:
    grade = "B"
elif average_marks>=70:
    grade = "C"
elif average_marks>=60:
    grade = "D"
else :
    grade = "f"

# ----------grade print---------
print(f"grade calculate")
for subject , score in marks.items():
        print(f"{subject} : {score}")


print(f"total marks : {total_marks}")
print(f"average marks: {average_marks:.2f}")
print(f"grade : {grade}")