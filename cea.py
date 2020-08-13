text=input("enter ciper text")
shift=input("enter shift if no shift enter 0")
s=int(shift)
if(s==0):
	while(s<25):
		s=s+1
		for i in range(len(text)):
			ch=text[i]
			a=chr((ord(ch)+s-97)%26+97)
			print(a,end="")
		print("")
else:
	for i in range(len(text)):
		ch=text[i]
		a=chr((ord(ch)+s-97)%26+97)
		print(a,end="")
	print("")