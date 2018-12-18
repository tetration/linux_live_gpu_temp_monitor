#!/usr/bin/env python2
import os 
import subprocess
import sys, select, time
def main():
	Welcome()
	select_gpu_manufacturer()


def Welcome():
	print("Welcome to live GPU temperature monitor for Linux Distributions")

def show_menu_options():
	print("What kind of GPU do you have?")
	print("1 - Nvidia")
	print("2 - AMD")
	print("3 - Exit program")


def select_gpu_manufacturer():
	loop=True
	while loop:## While loop which will keep going until loop = False
		show_menu_options()#print options avaliable for the user to opt for...
		choice = input("Enter your choice [1-3]: ")
		if choice==1:
			print "Nvidia has been selected"
			NVIDIA_GPU_Monitoring()
		elif choice==2:
			print "AMD has been selected"
			AMD_GPU_Monitoring()

		elif choice==3:
			print "Exiting the program..."
			exit()
			##loop=False # This will make the while loop to end as not value of loop is set to False
		else:
			raw_input("ERROR: Wrong choice please choose an option between 1 to 3 (Press ENTER to try again) \n")

def NVIDIA_GPU_Monitoring():
	while True:# Loop until user presses something
		print("Real-time updated GPU temperature of your NVIDIA Card :")
		os.system("nvidia-settings -q gpucoretemp")
		os.system("clear")
		time.sleep(1)
		print("Press enter whenever you wish to stop monitoring your GPU temperature and exit this program")
		i,o,e = select.select([sys.stdin],[],[],0.0001)
		if i == [sys.stdin]: break

def AMD_GPU_Monitoring():
	print("Under development coming soon...")
	exit()


main()