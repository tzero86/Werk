from sys import exit
import pyautogui
import sys
import time

# Helper functions

pyautogui.FAILSAFE = False

logo = '''
                  _       __          __            ____   ___
                 | |     / /__  _____/ /__   _   __/ __ \ <  /
                 | | /| / / _ \/ ___/ //_/  | | / / / / / / / 
                 | |/ |/ /  __/ /  / ,<     | |/ / /_/ / / /  
                 |__/|__/\___/_/  /_/|_|    |___/\____(_)_/   
                                                    by @tzero86

'''


def render(size, position):
	return "[" + (" " * position) + "=" + (" " * (size - position - 1)) + "]"


def draw(size, iterations, channel=sys.stdout, waittime=0.2):
	for index in range(iterations):
		n = index % (size * 2)
		position = (n if n < size else size * 2 - n - 1)
		bar = render(size, position)
		channel.write(bar + '\r')
		channel.flush()
		time.sleep(waittime)


try:
	print(logo)
	print('[*] Werk is starting, press CRTL+C at any time to stop the script')
	while True:

		# time.sleep(t) is used to give a break of
		# specified time t seconds so that its not
		# too frequent
		draw(6, 14, channel=sys.stdout, waittime=0.5)
		# time.sleep(15)

		# This for loop is used to move the mouse
		# pointer to 500 pixels in this case(5*100)
		for i in range(0, 50):
			pyautogui.moveTo(0, i * 5)

		# This for loop is used to press keyboard keys,
		# in this case the harmless key ctrl key is
		# used. You can change it according to your
		# requirement. This works with all keys.
		for i in range(0, 3):
			pyautogui.press('ctrl')

except KeyboardInterrupt:
	# User interrupt the program with ctrl+c
	print('[-] User Pressed CTRL+C, Stopping the Script.')
	exit()
