import datetime ,os ,time

while True:

	def dtime():

		while True:
	
			DATE = datetime.datetime.now()
			TIME = DATE.replace (microsecond=0)
			os.system(f"figlet {TIME}|lolcat")
			time.sleep(.9)
			os.system("clear")
	
	def currentTime():
	
		while True:
	
			ctimez = datetime.datetime.now()
			ctime = ctimez.strftime("%H:%M:%S")
	
			os.system(f"figlet {ctime}|lolcat")
			time.sleep(.9)
			os.system("clear")
	
	
	def cd():
		a = int(input("Enter A number Value~: "))
		os.system("clear")
		#os.system("figlet "+ui+"|lolcat")
		
		while True: 
			a = a -1	
			
			os.system("figlet "+str(a)+"|lolcat")
			time.sleep(1)
			os.system("clear")
			
			if(a <= 0):
				os.system("figlet Timers Up! |lolcat")
				print("Timers up!\n")
			
	print(""" 
	CLOCK CLOCK CLOCK 
	BY: AL104 (a.k.a) Anikin Luke
	
	[1] === Date and Time >
	[2] === Current Time >
	[3] === CountDown >
	
	[!] remeber press ctrl + c to close it!.

	 """)
	print("Select From 1 to 3 , what would it be?\n")
	uis = str(input("AL104 >~: "))
	
	if(uis == "1"):
		dtime()

	elif(uis == "2"):
		currentTime()

	elif(uis == "3"):
		cd()
	elif(uis == "!"):
		print("quitting..")
		time.sleep(.3)
		os.system("clear")
		break

	else:
		print("ERROR! ")
		
	









