import os as os2, time, string, sys, platform

class OS:
	def GetOSInfo():
		print(f"OS Device Identifier : {os2.name}")
		print(f"OS : {platform.system()}")
	def ClearScreen():
		if os2.name.lower() == "nt":
			os2.system("cls")
		else:
			os2.system("clear")
class ANSI:
	def ListColors():
		for color in range(256):
			print(f"\033[38;5;{color}m{color}\033[0m ", end='')
	def ColoredOutput(color, text=""):
		print(f"\033[38;5;{color}m{text}")
	def ResetColors():
		print("\033[0m")
class Message:
	def Error(errtext="Unspecified Error"):
		print(f"\033[0;37m[\033[1;31mX\033[0;37m] \033[1;31m{errtext}\033[0m")
	def Warn(warntext="Unspecified Warning"):
		print(f"\033[0;37m[\033[1;33m!\033[0;37m] \033[1;33m{warntext}\033[0m")
	def Info(infotext="Unspecified Information"):
		print(f"\033[0;37m[\033[1;34mi\033[0;37m] \033[1;34m{infotext}\033[0m")
		

if __name__=="__main__":
	print("Ooops, you ran the wrong file.\n\nCreate a new file and import this one to use it. It will not work here.")
	sys.exit(1)
