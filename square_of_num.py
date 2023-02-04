def square(n):
	list=[]
	for i in range(1,n+1):
		if i%2==0:
			x=i*i
			list=list.append(x)
			# list.append(x)
		else:
			x=i*i*i
			# list.append(x)
			list=list.append(x)
	print(list)


num=int(input("Enter number till which square you want to print:"))
square(num)
