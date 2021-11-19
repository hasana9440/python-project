'''m=int(input("enter value"))
n=m
rem=0
sum=0
while(n!=0):
	rem=n%10
	sum=sum*10+rem
	n=n/10
if sum==n:
	print(m,"is a palindrome")
else
	print(m,"not a palindrome")'''

m=input()
if m==m[::-1]:
	print(m,"is a palindrome")
else
	print(m,"not a palindrome")