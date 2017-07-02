import ftplib

""" Check anonymous login available """
def anonLogin(hostName):
	try:
		ftp = ftplib.FTP(hostName)
		ftp.login('anonymous','hello@world.com')
		print '\n[*] ' + str(hostName) + 'FTP anonymous login succeeded'
		ftp.quit()
		return True
	except:
		print '\n[-] '+str(hostName) + ' FTP anonymous login failed'
		return False

def main():
	host = '138.128.187.194'
	anonLogin(host)


if __name__ == '__main__':
	main()
