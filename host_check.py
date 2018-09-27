import os, socket, sys
import platform
import ctypes

def get_platform_name():
	if platform.mac_ver()[0]:
		return 'mac'
	if platform.win32_ver()[0]:
		return 'windows'
	if any(platform.dist()):
		return 'unix'
	if platform.java_ver()[0] or platform.java_ver()[1]:
		return 'java'
	return 'unknown OS'

#Windows admin cmd
def is_admin():
	try:
		# print("ADMIN")
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		# print("NO ADMIN")
		return False


base_url = str(sys.argv[1])
hosts_file = str(sys.argv[2])
OS = get_platform_name()
	
if (OS == 'mac' and os.geteuid() != 0):
	raw_input('ROOT ACCESS REQUIRED!')
	print('ROOT ACCESS REQUIRED!')
	sys.exit(0)
if (OS == 'windows' and ctypes.windll.shell32.IsUserAnAdmin() == 0):
	raw_input('ROOT ACCESS REQUIRED!')
	print('ROOT ACCESS REQUIRED!')
	sys.exit(0)

with open(hosts_file, "a+") as f:
	f.write('\n127.0.0.1 ' + base_url + '\n')
	f.write('localhost ' + base_url + '\n')

print("HOST ADDED!")