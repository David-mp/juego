import time
from operator import itemgetter
from random import randint
import pygame
import threading
from threading import Lock
import time
import json
import sys

CONSTbg_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_1.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_2.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_3.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_4.jpg'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/bg_end_7.jpg')]
CONSTc_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin4.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin5.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin6.png')]
CONSTp_sprites = [[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up4.png')]]]
CONSTcoin_diameter = 24
CONSTroom_width = 700
CONSTroom_height = 500
CONSTplayer_speed = 125
invoker=None
cloudbook_sync_timeout=False

def f0():
#Automated code for global var:
 #fun_name: f0 final fun name: f0 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f0, "game_status"):
		f0.game_status = None

	if not hasattr(f0, "ver_game_status"):
		f0.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f0.ver_game_status),'f0')
	if aux_game_status != "None":
		f0.game_status = aux_game_status
	game_status=f0.game_status
	f0.ver_game_status= aux_ver
	ver_game_status= f0.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	print("Game started")
	game_aux = game_status
	aux_coin = []
	for i in range(10):
		x_coin = randint(CONSTcoin_diameter, CONSTroom_width-CONSTcoin_diameter)
		y_coin = randint(CONSTcoin_diameter, CONSTroom_height-CONSTcoin_diameter)
		aux_coin.append((x_coin, y_coin))
	for i in range(10):
		x_coin = randint(CONSTroom_width+CONSTcoin_diameter, 2*CONSTroom_width-CONSTcoin_diameter)
		y_coin = randint(CONSTcoin_diameter, CONSTroom_height-CONSTcoin_diameter)
		aux_coin.append((x_coin, y_coin))
	for i in range(10):
		x_coin = randint(CONSTcoin_diameter, CONSTroom_width-CONSTcoin_diameter)
		y_coin = randint(CONSTroom_height+CONSTcoin_diameter, 2*CONSTroom_height-CONSTcoin_diameter)
		aux_coin.append((x_coin, y_coin))
	for i in range(10):
		x_coin = randint(CONSTroom_width+CONSTcoin_diameter, 2*CONSTroom_width-CONSTcoin_diameter)
		y_coin = randint(CONSTroom_height+CONSTcoin_diameter, 2*CONSTroom_height-CONSTcoin_diameter)
		aux_coin.append((x_coin, y_coin))
	game_aux[0] = aux_coin
	invoker(['du_0'], 'f1','"f1.game_status='+str(game_aux)+' ", '+str(ver_game_status),'f0')#[0] = game_aux
	game_status=game_aux
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_default'], 'f6',str(1),'f0')#
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_default'], 'f6',str(2),'f0')#
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_default'], 'f6',str(3),'f0')#
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_default'], 'f6',str(4),'f0')#
	while json.loads(cloudbook_th_counter("")) > 0: #This was sync
			time.sleep(0.01)
	print("Game ended")


	return json.dumps('cloudbook: done') 

def f12(status):
#Automated code for global var:
 #fun_name: f12 final fun name: f12 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f12, "game_status"):
		f12.game_status = None

	if not hasattr(f12, "ver_game_status"):
		f12.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f12.ver_game_status),'f12')
	if aux_game_status != "None":
		f12.game_status = aux_game_status
	game_status=f12.game_status
	f12.ver_game_status= aux_ver
	ver_game_status= f12.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	aux_status = game_status
	players = []
	for i in range(1,5):
		players.append(aux_status[i])
	for i in range(0,len(players)):
		players[i][9] = aux_status[6][i]
	players = sorted(players,key=itemgetter(9),reverse=True)
	sorted_status = []
	sorted_status.append(aux_status[0])
	for i in range(0,4):
		sorted_status.append(players[i])
	for i in range(5,len(aux_status)):
		sorted_status.append(aux_status[i])
	print()
	print(sorted_status)
	return json.dumps(sorted_status)


	return json.dumps('cloudbook: done') 

def f1(op, old_ver):
	if not hasattr(f1, "game_status"):
		f1.game_status=[[],[100,350,0,0,0,0,1,0,0,0,0],[250,350,0,0,0,0,1,0,0,5,1],[400,350,0,0,0,0,1,0,0,10,2],[550,350,0,0,0,0,1,0,0,0,3],0,[0,0,0,0],0]
	if not hasattr(f1, "ver_game_status"):
		f1.ver_game_status= 1
	if not hasattr(f1, "lock_game_status"):
		f1.lock_game_status = threading.Lock()
	if op == "None":
		if old_ver == f1.ver_game_status:
			return json.dumps(("None", old_ver))
		else:
			try:
				return json.dumps((f1.game_status,f1.ver_game_status)) 
			except:
				return json.dumps((str(f1.game_status),f1.ver_game_status))
	else:
		try:
			f1.ver_game_status+=1
			return json.dumps((eval(op),f1.ver_game_status))
		except:
			with f1.lock_game_status:
				exec(op)
				f1.ver_game_status+=1
			return json.dumps(("done",f1.ver_game_status))
	return json.dumps('cloudbook: done') 

def cloudbook_print(element):
	print (element)
	return "cloudbook: done"
	
def cloudbook_th_counter(value):
	if not hasattr(cloudbook_th_counter, "val"):
		cloudbook_th_counter.val = 0
	if not hasattr(cloudbook_th_counter, "cerrojo"):
		cloudbook_th_counter.cerrojo = Lock()
	if value == "++":
		with cloudbook_th_counter.cerrojo:
			cloudbook_th_counter.val += 1
	if value == "--":
		with cloudbook_th_counter.cerrojo:
			cloudbook_th_counter.val -= 1
	return json.dumps(cloudbook_th_counter.val)

def main():
	#f0()
	#return "cloudbook: done"
	return f0()

if __name__ == '__main__':
	f0()
			