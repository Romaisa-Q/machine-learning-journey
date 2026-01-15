maths=int(input("Enter marks in Mathematics: "))
english=int(input("Enter marks in english: "))
science=int(input("Enter marks in Science: "))
total=maths+english+science
percentage=(total/300)*100
if percentage>=90:
    grade='A'
elif percentage>=80:
    grade='B'
elif percentage>=70:
    grade='C'
elif percentage>=60:
    grade='D'
else:
    grade='F'
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
