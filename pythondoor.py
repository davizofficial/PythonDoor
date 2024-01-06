import marshal, os, time

banner=("""\033[1;32m
    ____       ________                   ____                             ___
   / __ \__  _/_  __/ /_  ____  ____     / __ \____  ____  _____   _   __ <  /
  / /_/ / / / // / / __ \/ __ \/ __ \   / / / / __ \/ __ \/ ___/  | | / / / /
 / ____/ /_/ // / / / / / /_/ / / / /  / /_/ / /_/ / /_/ / /      | |/ / / /
/_/    \__, //_/ /_/ /_/\____/_/ /_/  /_____/\____/\____/_/       |___(_)_/
      /____/

                        \033[1;32mPyThon Door v.1 (Beta)\033[1;32m
                        
             \033[1;32mGithub : https://github.com/davizofficial/PythonDoor\033[1;32

""")

def py1():
	try:
		os.system('clear')
		print(banner)
		a=input("\033[1;37mInput Path File [Example : C:/Fakepath/pythoncode.py]  >>> \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mSuccess!: \033[1;36mResult_"+a)
		print()
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR")
		exit()
	
def py2():
	try:
		os.system('clear')
		print(banner)
		a=raw_input("\033[1;37mInput Path File [Example : C:/Fakepath/pythoncode.py]  >>> \033[1;32m")
		x=open(a).read()
		b=compile(x,'','exec')
		c=marshal.dumps(b)
		d=open("Hasil_"+a,'w')
		d.write('import marshal\n')
		d.write('exec(marshal.loads('+repr(c)+'))')
		d.close()
		time.sleep(1.5)
		print("\033[1;32mSuccess!: \033[1;36mResult_"+a)
		print
	except KeyboardInterrupt:
		print("\n\033[1;31m[!] ERROR: PASTIKAN FILE YANG MAU DI COMPILE BERADA DI FOLDER YANG SAMA DAN PASTIKAN ANDA MENGINPUT FILE DENGAN BENAR")
		exit()

os.system('clear')
print(banner)
print("[[!]BOT[!] : Select Number For Compile Python")
print("")
print("\033[1;32m/1/ Python3")
print("/2/ Python2")
print("")
ask=input("\033[1;32mroot@PythonDoor~: \033[1;32m")
if ask == 1:
	py1()
elif ask == 2:
	py2();
else:
	print("\n\033[1;31m[!] Wrong Alert!!!")
