#leap year
a=int(input("Enter year: "))

if a%100==0 and a%400!=0 :
    print("It is not leap year")
elif a%4==0:
    print("It is leap year")
else:
    print("It is not leap year")        







#find the largest numbers
#a=int(input("Enter the number: "))
#b=int(input("Enter the number: "))
#c=int(input("Enter the number: "))

#if a>b and a>c:
 #   print("a is largest number")
#elif b>c:
 #   print("b is largest number")
#else:
#    print("c is largest number")        







#palindrome checker
#a=input("Enter string: ")

#reverse=a[::-1]
#if reverse == a:
 #   print("It is palindrome")
#else:
 #   print("It is not palindrome")    







#grade calculator
#math=int(input("Enter Math Marks: "))
#science=int(input("Enter Science Marks: "))
#english=int(input("Enter English Marks: "))

#total=math+science+english
#avg=total/3

#if avg>90:
 #   print("Grade:A")
#lif avg>75 and avg<90:
 #   print("Grade:B")
#elif avg>50 and avg<75:
 #   print("Grade:C")
#elif avg>36 and avg<50:
#    print("Grade:D")
#else:
 #   print("Grade:F")       

#print(f"Total Marks: {total}\nAverage marks:{avg}")






#novel counter
#a=input('Enter word: ')
#a2=a.lower()

#a=a2.count('a')
#e=a2.count('e')
#i=a2.count('i')
#o=a2.count('o')
#u=a2.count('u')

#print(f"Number of vowels:{a+e+i+o+u}")