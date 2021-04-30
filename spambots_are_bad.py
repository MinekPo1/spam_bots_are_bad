import requests
import threading

nr = 0
print_every = 100
last_print = 0

threads = 10

do = True

def spam():
	global nr
	while do:
		nr += 1
		requests.post("https://steamcommnunitty.com/login/dologin",data={"username":"abcd","password":"1234"})

for i in range(threads):
	t = threading.Thread(target=spam)
	t.start()
try:
	while True:
		if nr%print_every == 0 and nr != last_print:
			last_print = nr
			print("did %i requests"%nr)
except KeyboardInterrupt: do = False
print("made %i requests!"%nr)