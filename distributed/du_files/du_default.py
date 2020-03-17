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

def f3():
#Automated code for global var:
 #fun_name: f3 final fun name: f3 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f3, "game_status"):
		f3.game_status = None

	if not hasattr(f3, "ver_game_status"):
		f3.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f3.ver_game_status),'f3')
	if aux_game_status != "None":
		f3.game_status = aux_game_status
	game_status=f3.game_status
	f3.ver_game_status= aux_ver
	ver_game_status= f3.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	photogram_counter = 0
	while True:
		photogram_counter = photogram_counter + 1
		invoker(['du_0'], 'f1','"f1.game_status['+str(7)+']%3d'+str(photogram_counter)+' ", '+str(ver_game_status),'f3')#[0] = photogram_counter
		game_status[7]=photogram_counter
		time.sleep(0.05)


	return json.dumps('cloudbook: done') 

def f9(player_selected, status, keys_last_cycle, keys, joystick_input, last_joystick_input, window, speed, photogram_counter):
	my_player = status[player_selected]
	my_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
	my_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
	v_x = status[player_selected][2]
	v_y = status[player_selected][3]
	test_counter = 4
	player_has_moved = False
	if v_x == 0 and v_y == 0:
		if (keys[pygame.K_d] or joystick_input[0] == 1) and my_player[0] < (2*CONSTroom_width-64-speed):
			status[player_selected][2] = 1
			status[player_selected][3] = 0
			status[player_selected][4] = 0
			status[player_selected][6] = 0
			status[player_selected][7] = status[7]
			status[player_selected][8] = 1
			aux_player = status[player_selected]
			player_has_moved = True
			if(aux_player[0] < CONSTroom_width and aux_player[0] + speed >= CONSTroom_width):
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
				status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if aux_player[1] < CONSTroom_height:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,1,0)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,1,0)
		elif (keys[pygame.K_a] or joystick_input[0] == -1) and my_player[0] > speed:
			status[player_selected][2] = -1
			status[player_selected][3] = 0
			status[player_selected][4] = 1
			status[player_selected][6] = 0
			status[player_selected][7] = status[7]
			status[player_selected][8] = 1
			aux_player = status[player_selected]
			player_has_moved = True
			if(aux_player[0] - speed < CONSTroom_width and aux_player[0] >= CONSTroom_width):
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
				status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if aux_player[1] < CONSTroom_height:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,-1,0)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,-1,0)
				status[player_selected][0] = status[player_selected][0] - speed
		elif (keys[pygame.K_s] or joystick_input[1] == 1) and my_player[1] < (2*CONSTroom_height-64-speed):
			status[player_selected][2] = 0
			status[player_selected][3] = 1
			status[player_selected][4] = 2
			status[player_selected][6] = 0
			status[player_selected][7] = status[7]
			status[player_selected][8] = 1
			aux_player = status[player_selected]
			player_has_moved = True
			if(aux_player[1] < CONSTroom_height and aux_player[1] + speed >= CONSTroom_height):
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
				status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if aux_player[0] < CONSTroom_width:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,1)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,1)
				status[player_selected][1] = status[player_selected][1] + speed
		elif (keys[pygame.K_w] or joystick_input[1] == -1) and my_player[1] > speed:
			status[player_selected][2] = 0
			status[player_selected][3] = -1
			status[player_selected][4] = 3
			status[player_selected][6] = 0
			status[player_selected][7] = status[7]
			status[player_selected][8] = 1
			aux_player = status[player_selected]
			player_has_moved = True
			if(aux_player[1] - speed < CONSTroom_height and aux_player[1] >= CONSTroom_height):
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
				status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if aux_player[0] < CONSTroom_width:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,-1)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,-1)
				status[player_selected][1] = status[player_selected][1] - speed
	elif v_x == 1:
		if ((keys_last_cycle[pygame.K_d] or last_joystick_input[0] == 1) and not (keys[pygame.K_d] or joystick_input[0] == 1)) or not (my_player_x < (2*CONSTroom_width-64-speed)):
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			nonblockingf2(player_selected,aux_player)
		else:
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
			player_has_moved = True
			current_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			current_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			if(current_player_x - speed < CONSTroom_width and current_player_x >= CONSTroom_width):
				status[player_selected][0] = current_player_x
				status[player_selected][1] = current_player_y
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if current_player_y < CONSTroom_height:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,1,0)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,1,0)
	elif v_x == -1:
		if ((keys_last_cycle[pygame.K_a] or last_joystick_input[0] == -1) and not (keys[pygame.K_a] or joystick_input[0] == -1)) or not (my_player_x > speed):
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			nonblockingf2(player_selected,aux_player)
		else:
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
			player_has_moved = True
			current_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			current_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			if(current_player_x < CONSTroom_width and current_player_x + speed >= CONSTroom_width):
				status[player_selected][0] = current_player_x
				status[player_selected][1] = current_player_y
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if current_player_y < CONSTroom_height:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,-1,0)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,-1,0)
	elif v_y == 1:
		if ((keys_last_cycle[pygame.K_s] or last_joystick_input[1] == 1) and not (keys[pygame.K_s] or joystick_input[1] == 1)) or not (my_player_y < (2*CONSTroom_height-64-speed)):
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			nonblockingf2(player_selected,aux_player)
		else:
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
			player_has_moved = True
			current_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			current_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			if(current_player_y - speed < CONSTroom_height and current_player_y >= CONSTroom_height):
				status[player_selected][0] = current_player_x
				status[player_selected][1] = current_player_y
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if current_player_x < CONSTroom_width:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,1)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,1)
	elif v_y == -1:
		if ((keys_last_cycle[pygame.K_w] or last_joystick_input[1] == -1) and not (keys[pygame.K_w] or joystick_input[1] == -1)) or not (my_player_y > speed):
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			nonblockingf2(player_selected,aux_player)
		else:
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
			player_has_moved = True
			current_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			current_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			if(current_player_y < CONSTroom_height and current_player_y + speed >= CONSTroom_height):
				status[player_selected][0] = current_player_x
				status[player_selected][1] = current_player_y
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf2(player_selected,aux_player)
				if current_player_x < CONSTroom_width:
					f8(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,-1)
				else: 
					f8(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,-1)
	if player_has_moved:
		my_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
		my_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
		hitbox = pygame.Rect(my_player_x, my_player_y, 64, 64)
		coins = status[0]
		for c in coins:
			if hitbox.collidepoint(c[0] + CONSTcoin_diameter/2, c[1] + CONSTcoin_diameter/2):
				status[0].remove(c)
				#__CLOUDBOOK:NONBLOCKING__
				nonblockingf7(player_selected,c)
	return status


	return json.dumps('cloudbook: done') 

def f8(player, player_sprite, room_sprite1, room_sprite2, window, x_dir, y_dir):
	clock = pygame.time.Clock()
	if x_dir == 1:
		for x in range(0,CONSTroom_width,4):
			window.blit(room_sprite1,(-x,0))
			window.blit(room_sprite2,(CONSTroom_width-x,0))
			window.blit(player_sprite,(CONSTroom_width - x,player[1]%CONSTroom_height))
			pygame.display.update()
			clock.tick(100)
	elif x_dir == -1:
		for x in range(0,CONSTroom_width,4):
			window.blit(room_sprite1,(-CONSTroom_width+x,0))
			window.blit(room_sprite2,(x,0))
			window.blit(player_sprite,(x,player[1]%CONSTroom_height))
			pygame.display.update()
			clock.tick(100)
	elif y_dir == 1:
		for y in range(0,CONSTroom_height,3):
			window.blit(room_sprite1,(0,0-y))
			window.blit(room_sprite2,(0,CONSTroom_height-y))
			window.blit(player_sprite,(player[0]%CONSTroom_width, CONSTroom_height-y))
			pygame.display.update()
			clock.tick(100)
	elif y_dir == -1:
		for y in range(0,CONSTroom_height,3):
			window.blit(room_sprite2,(0,y))
			window.blit(room_sprite1,(0,-CONSTroom_height+y))
			window.blit(player_sprite,(player[0]%CONSTroom_width, y))
			pygame.display.update()
			clock.tick(100)


	return json.dumps('cloudbook: done') 

def f2(index, player):
#Automated code for global var:
 #fun_name: f2 final fun name: f2 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f2, "game_status"):
		f2.game_status = None

	if not hasattr(f2, "ver_game_status"):
		f2.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f2.ver_game_status),'f2')
	if aux_game_status != "None":
		f2.game_status = aux_game_status
	game_status=f2.game_status
	f2.ver_game_status= aux_ver
	ver_game_status= f2.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	invoker(['du_0'], 'f1','"f1.game_status['+str(index)+']%3d'+str(player)+' ", '+str(ver_game_status),'f2')#[0] = player
	game_status[index]=player


	return json.dumps('cloudbook: done') 

def f7(player_selected, coin):
#Automated code for global var:
 #fun_name: f7 final fun name: f7 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f7, "game_status"):
		f7.game_status = None

	if not hasattr(f7, "ver_game_status"):
		f7.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f7.ver_game_status),'f7')
	if aux_game_status != "None":
		f7.game_status = aux_game_status
	game_status=f7.game_status
	f7.ver_game_status= aux_ver
	ver_game_status= f7.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	aux_status = game_status
	my_player = aux_status[player_selected]
	if coin in aux_status[0]:
		aux_status[0].remove(coin)
		aux_status[6][player_selected - 1] = aux_status[6][player_selected - 1] + 1
		CONSTcoinSound1 = pygame.mixer.Sound('/home/pi/cloudbook/juego/distributed/Sprites/Music/coin2.wav')
		CONSTcoinSound1.set_volume(0.2)
		CONSTcoinSound1.play()
		if len(aux_status[0]) == 0:
			aux_status[5] = 1
			invoker(['du_0'], 'f1','"f1.game_status['+str(5)+']%3d'+str(1)+' ", '+str(ver_game_status),'f7')#[0] = 1
			game_status[5]=1
			print("ENDGAME")
		invoker(['du_0'], 'f1','"f1.game_status['+str(0)+']%3d'+str(aux_status[0])+' ", '+str(ver_game_status),'f7')#[0] = aux_status[0]
		game_status[0]=aux_status[0]
		invoker(['du_0'], 'f1','"f1.game_status['+str(6)+']%3d'+str(aux_status[6])+' ", '+str(ver_game_status),'f7')#[0] = aux_status[6]
		game_status[6]=aux_status[6]


	return json.dumps('cloudbook: done') 

def f6(player_selected):
	threadf6 = threading.Thread(target= parallel_f6, daemon = False, args = [player_selected])
	threadf6.start()
	return json.dumps("thread launched")

def parallel_f6(player_selected):
	if not hasattr(parallel_f6, "lock"):
		parallel_f6.lock = threading.Lock()
	with parallel_f6.lock:
		if player_selected == 1:
			#__CLOUDBOOK:NONBLOCKING__
			nonblockingf3()
		pygame.init()
		pygame.display.set_caption("Game Window " + str(player_selected))
		pygame.mixer.init()
		music = pygame.mixer.music.load('/home/pi/cloudbook/juego/distributed/Sprites/Music/music.mp3')
		time.sleep(0.5)
		pygame.mixer.music.set_volume(0.2)
		pygame.mixer.music.play(-1)
		status = f5()
		last_cycle_positions = [0, [100,350,0], [250,350,0], [400,350,0], [550,350,0]]
		time_measures = []
		refresh_local_counter = 0
		movement_counter = 0
		coin_sprite_counter = 0
		photogram_counter = -1
		run = True
		sorted_status = False
		window = pygame.display.set_mode((CONSTroom_width, CONSTroom_height))
		CLOCK_FPS = 20
		clock = pygame.time.Clock()
		keys = pygame.key.get_pressed()
		if not pygame.joystick.get_init():
			pygame.joystick.init()
		n_joysticks = pygame.joystick.get_count()
		joystick_input = (0,0)
		last_joystick_input = (0,0)
		if n_joysticks != 0:
			my_joystick = pygame.joystick.Joystick(0)
			my_joystick.init()
		ping_measures = []
		clk = 1/CLOCK_FPS
		T1 = time.time()
		T2 = time.time() - clk
		for i in range(1,10):
			P1_start = time.time()
			status = f5()
			P1_end = time.time()
			resta = P1_end - P1_start
			ping_measures.append(resta)
		print("------------------------")
		print("RESULTS player",player_selected)
		print(ping_measures)
		print("MAX =",max(ping_measures))
		mean = sum(ping_measures)/len(ping_measures)
		print("MEAN =", mean)
		print("CLOCK INTERVAL = ",clk)
		time.sleep(1)
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.JOYAXISMOTION:
					last_joystick_input = joystick_input
					axis0 = round(my_joystick.get_axis(0))
					axis1 = round(my_joystick.get_axis(1))
					joystick_input = (axis0,axis1)
			clock.tick(CLOCK_FPS)
			if not status[5]:
				T1 = T2
				T2 = time.time()
				resta = T2 - T1
				if len(time_measures) <= 12:
					if resta < 2:
						time_measures.append(resta)
				else:
					if player_selected == 1:
						CLOCK_FPS = f13(time_measures)
					time_measures = []
				status[7] = status[7] + 1
				refresh_local_counter = refresh_local_counter + 1
				if refresh_local_counter >= 5:
					#__CLOUDBOOK:NONBLOCKING__
					nonblockingf4(player_selected,status)
					refresh_local_counter = 0
				coin_sprite_counter = coin_sprite_counter + 1
				if coin_sprite_counter >= 36:
					coin_sprite_counter = 0
				status[player_selected][5] = status[player_selected][5] + 1
				if status[player_selected][5] >= 24:
					status[player_selected][5] = 0
				if status[player_selected][6]:
					status[player_selected][5] = 0
				keys_last_cycle = keys
				keys = pygame.key.get_pressed()
				speed = round(CONSTplayer_speed/CLOCK_FPS)
				status = f9(player_selected,status,keys_last_cycle,keys,joystick_input,last_joystick_input,window,speed,photogram_counter)
				now = time.time()
				last_cycle_positions = f11(player_selected,status,now,CLOCK_FPS,last_cycle_positions,photogram_counter)
				f10(player_selected,status,coin_sprite_counter,window,CLOCK_FPS,last_cycle_positions,photogram_counter)
				pygame.display.update()
			else:
				if not sorted_status:
					sorted_status = True
					status = invoker(['du_0'], 'f12',str(status),'f6')
				f14(status,window)
				pygame.display.update()
	

		invoker(['du_0'], 'cloudbook_th_counter',"'--'")

		return json.dumps('cloudbook: done') 

def f5():
#Automated code for global var:
 #fun_name: f5 final fun name: f5 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f5, "game_status"):
		f5.game_status = None

	if not hasattr(f5, "ver_game_status"):
		f5.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f5.ver_game_status),'f5')
	if aux_game_status != "None":
		f5.game_status = aux_game_status
	game_status=f5.game_status
	f5.ver_game_status= aux_ver
	ver_game_status= f5.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	aux_status = game_status
	return aux_status


	return json.dumps('cloudbook: done') 

def f14(status, window):
	window.blit(CONSTbg_sprites[4], (0,0))
	for i in range(1,5):
		window.blit(CONSTp_sprites[status[i][10]][2][0], (60+(i-1)*40,55+(i-1)*95))


	return json.dumps('cloudbook: done') 

def f13(time_measures):
	mean = sum(time_measures) / (len(time_measures))
	fps_mean = round(1/mean)
	new_fps = (fps_mean + 20) / 2
	return new_fps


	return json.dumps('cloudbook: done') 

def f11(player_selected, status, now, CLOCK_FPS, last_cycle_positions, photogram_counter):
	for n_player in range(1,len(last_cycle_positions)):
		player = status[n_player]
		time_passed = now - player[7]
		movement_counter = player[8]
		speed = round(CONSTplayer_speed/CLOCK_FPS)
		if n_player == player_selected:
			x = player[0] + player[2]*speed*movement_counter
			y = player[1] + player[3]*speed*movement_counter
			last_cycle_positions[n_player][2] = movement_counter
		else:
			unkown_cycles = status[7] - player[7]
			x = player[0] + round(player[2]*speed*unkown_cycles)
			y = player[1] + round(player[3]*speed*unkown_cycles)
			if player[2] == 0 and player[3] == 0:
				playerWalkCount = 0
			else:
				playerWalkCount = int(time_passed/(1/CLOCK_FPS)%24)
			x_dif = abs(x - last_cycle_positions[n_player][0])
			y_dif = abs(y - last_cycle_positions[n_player][1])
			if x_dif > 10:
				x = int((x + last_cycle_positions[n_player][0])/2)
			if y_dif > 10:
				y = int((y + last_cycle_positions[n_player][1])/2)
			last_cycle_positions[n_player][2] = playerWalkCount
		last_cycle_positions[n_player][0] = x
		last_cycle_positions[n_player][1] = y
	return last_cycle_positions	


	return json.dumps('cloudbook: done') 

def f10(player_selected, aux_status, aux_coin_count, window, CLOCK_FPS, last_cycle_positions, photogram_counter):
	coins = aux_status[0]
	speed = round(CONSTplayer_speed/CLOCK_FPS)
	my_player = aux_status[player_selected]
	my_player_x = my_player[0] + my_player[2]*speed*my_player[8]
	my_player_y = my_player[1] + my_player[3]*speed*my_player[8]
	now = time.time()
	if my_player_x < CONSTroom_width and my_player_y < CONSTroom_height:
		bg0 = CONSTbg_sprites[0]
		window.blit(bg0,(0,0))
		for c in coins:
			if c[0] < CONSTroom_width and c[1] < CONSTroom_height:
				i = min(aux_coin_count // 6,5)
				c_sprite = CONSTc_sprites[i]
				window.blit(c_sprite, (c[0] % CONSTroom_width, c[1] % CONSTroom_height))
		for k in range(1,5):
			if k != player_selected:
				p = last_cycle_positions[k]
				if p[0] < CONSTroom_width and p[1] < CONSTroom_height:
					i = last_cycle_positions[k][2] // 6
					j = aux_status[k][4]
					p_sprite = CONSTp_sprites[k - 1][j][i]
					window.blit(p_sprite, (p[0], p[1]))
	elif my_player_x < CONSTroom_width and my_player_y >= CONSTroom_height:
		bg1 = CONSTbg_sprites[1]
		window.blit(bg1,(0,0))
		for c in coins:
			if c[0] < CONSTroom_width and c[1] >= CONSTroom_height:
				i = min(aux_coin_count // 6,5)
				c_sprite = CONSTc_sprites[i]
				window.blit(c_sprite, (c[0] % CONSTroom_width, c[1] % CONSTroom_height))
		for k in range(1,5):
			if k != player_selected:
				p = last_cycle_positions[k]
				if p[0] < CONSTroom_width and p[1] >= CONSTroom_height:
					i = last_cycle_positions[k][2] // 6
					j = aux_status[k][4]
					p_sprite = CONSTp_sprites[k - 1][j][i]
					window.blit(p_sprite, (p[0], p[1]-CONSTroom_height))
	elif my_player_x >= CONSTroom_width and my_player_y < CONSTroom_height:
		bg2 = CONSTbg_sprites[2]
		window.blit(bg2,(0,0))
		for c in coins:
			if c[0] >= CONSTroom_width and c[1] < CONSTroom_height:
				i = min(aux_coin_count // 6,5)
				c_sprite = CONSTc_sprites[i]
				window.blit(c_sprite, (c[0] % CONSTroom_width, c[1] % CONSTroom_height))
		for k in range(1,5):
			if k != player_selected:
				p = last_cycle_positions[k]
				if p[0] >= CONSTroom_width and p[1] < CONSTroom_height:
					i = last_cycle_positions[k][2] // 6
					j = aux_status[k][4]
					p_sprite = CONSTp_sprites[k - 1][j][i]
					window.blit(p_sprite, (p[0]-CONSTroom_width, p[1]))
	elif my_player_x >= CONSTroom_width and my_player_y >= CONSTroom_height:
		bg3 = CONSTbg_sprites[3]
		window.blit(bg3,(0,0))
		for c in coins:
			if c[0] >= CONSTroom_width and c[1] >= CONSTroom_height:
				i = min(aux_coin_count // 6,5)
				c_sprite = CONSTc_sprites[i]
				window.blit(c_sprite, (c[0] % CONSTroom_width, c[1] % CONSTroom_height))
		for k in range(1,5):
			if k != player_selected:
				p = last_cycle_positions[k]
				if p[0] >= CONSTroom_width and p[1] >= CONSTroom_height:
					i = last_cycle_positions[k][2] // 6
					j = aux_status[k][4]
					p_sprite = CONSTp_sprites[k - 1][j][i]
					window.blit(p_sprite, (p[0]-CONSTroom_width, p[1]-CONSTroom_height))
	i = aux_status[player_selected][5] // 6
	j = aux_status[player_selected][4]
	my_player_sprite = CONSTp_sprites[player_selected - 1][j][i]
	window.blit(my_player_sprite, (last_cycle_positions[player_selected][0]%CONSTroom_width, last_cycle_positions[player_selected][1]%CONSTroom_height))
	pygame.display.update()


	return json.dumps('cloudbook: done') 

def f4(player_selected, status):
#Automated code for global var:
 #fun_name: f4 final fun name: f4 globalName: game_status destiny du: 0 global_fun_name: f1
#============================global vars automatic code=========================
	#game_status
	if not hasattr(f4, "game_status"):
		f4.game_status = None

	if not hasattr(f4, "ver_game_status"):
		f4.ver_game_status = 0
        
	aux_game_status,aux_ver = invoker(['du_0'],'f1',"'None',"+str(f4.ver_game_status),'f4')
	if aux_game_status != "None":
		f4.game_status = aux_game_status
	game_status=f4.game_status
	f4.ver_game_status= aux_ver
	ver_game_status= f4.ver_game_status
		#	global game_status#Aqui va el chorrazo de codigo
	aux_status = game_status
	for i in range(0,len(aux_status)):
		if i != player_selected:
			status[i] = aux_status[i]


	return json.dumps('cloudbook: done') 


def nonblockingf2(player_selected,aux_player):
	threadf2 = threading.Thread(target=f2, daemon = False, args = [player_selected,aux_player])
	threadf2.start()
	return json.dumps("thread launched")

def nonblockingf7(player_selected,c):
	threadf7 = threading.Thread(target=f7, daemon = False, args = [player_selected,c])
	threadf7.start()
	return json.dumps("thread launched")

def nonblockingf3():
	threadf3 = threading.Thread(target=f3, daemon = False, args = [])
	threadf3.start()
	return json.dumps("thread launched")

def nonblockingf4(player_selected,status):
	threadf4 = threading.Thread(target=f4, daemon = False, args = [player_selected,status])
	threadf4.start()
	return json.dumps("thread launched")

