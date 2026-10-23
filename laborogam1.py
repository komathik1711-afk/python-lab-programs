Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Student marks ,Percentage and Grade 
... name=input("Enter Student name:")
... n=int(input("Enter Number of subjects:"))
... total=0
... for i in range(1,n+1):
...     mark= float(input(f"Enter mark for Subject{i}:"))
...     total+=marks
...     percentage=total/n
... if percentage >=90:
...     grade="A+"
...     performance="Outstanding"
... elif percentage>=80:
...     grade="A"
...     performance="Execellent"
... elif percentage>=70:
...     grade="B"
...     performance="Very Good"
... elif percentage>=60:
...     grade="C"
...     performance="Good"
... elif percentage>=50:
...     grade="D"
...     performance="Average"
... else:
...     grade="F"
...     performance="Needs Improvement"
... 
... print("\n---Academic Performance---")
... print("Student Name:",name)
... print("Total Marks:",total)
... print("Percentage:",round(percentage,2),"%")
... print("Grade :",grade)
