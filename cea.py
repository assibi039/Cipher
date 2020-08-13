text=input("enter ciper text")
#shift=input("enter shift if no shift enter 0")
shift=0
while(shift<25):
	shift=shift+1
	for i in range(len(text)):
		ch=text[i]
		a=chr((ord(ch)+int(shift)-97)%26+97)
		print(a,end="")
	print("")