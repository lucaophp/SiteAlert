# _*_ coding: utf-8 _*_
import urllib2
import time
from pygame import mixer # Load the required library
from plyer import notification
import threading
import thread
ant = ''
parar = False
mudou = False
url = 'http://'
timer = 60
timeInit = 0
def service():
	global parar
	global url
	global timer
	global timeInit
	global ant
	global mudou
	while not(parar):
		req = urllib2.Request(url)
		req.add_header('Referer', 'https://www.google.com/')
		req.add_header('User-Agent', 'Mozilla/5.0')
		try:
			r = urllib2.urlopen(req)
		except:
			continue
		novo = r.read()
		print r.getcode()
		if ant == '': ant = novo
		if ant != novo and r.getcode() == 200 and ant != '':
			print 'MUDOU'
			
			notification.notify(
				title='Houve mudanca no site',
				message='Site monitorado com mudança no conteudo...',
				app_name='Alarm Site',
				app_icon='icon.ico',
				ticker='r'
			)
			mixer.init()
			mixer.music.load('aviso.mp3')
			mixer.music.play()
			ant = novo
		
		timeInit = time.time()
		while time.time()-timeInit<timer and not(parar) and not(mudou): pass
		if mudou:
			ant = ''
			mudou = False
		
		
def control():
	global parar
	global url
	global timer
	global mudou
	
	while True:
		import os.path
		if os.path.isfile('com.ps'):
			try:
				os.remove('com.ps')
			except:
				pass
			with open('yes.ps','w') as fp:
				fp.write('yes')
				
		if os.path.isfile('start.ps'):
			with open('start.ps','r') as fp:
				linha = fp.readline()
				if linha.strip() == 'PARAR':
					parar = True
				else:
					url = linha
					timer = int(fp.readline())
					mudou = True
			try:
				os.remove('start.ps')
			except:
				pass
		if parar:
			break
		
	

threadPrincipal = threading.Thread(target= control,args = ())
t = threading.Thread(target= service,args = ())
t.start()
threadPrincipal.start()
threadPrincipal.join()
t.join()


