import time
import pygame
from random import randint
from operator import itemgetter

#game_status = {1: [100,350], 2: [250,350], 3: [400,350], 4: [550,350], 5: 0}
game_status = [[], [100,350,0,0,0,0,1,0,0,0,0], [250,350,0,0,0,0,1,0,0,5,1], [400,350,0,0,0,0,1,0,0,10,2], [550,350,0,0,0,0,1,0,0,0,3], 0, [0,0,0,0], 0]
#game_status struct
#[0] = coins
#[1] = player1
#[2] = player2
#[3] = player3
#[4] = player4
#[5] = end_game? 
#[6] = player_scores
#[7] = photogram counter

#Player struct: 
#[0] = X
#[1] = Y
#[2] = v_x
#[3] = v_y
#[4] = playerDirection ; € {0 = RIGHT; 1 = LEFT; 2 = DOWN; 3 = UP} 
#[5] = playerWalkCount, 
#[6] = playerStanding, 
#[7] = time()
#[8] = movement_counter
#[9] = player_score
#[10] = playerSpritePackage

CONSTbg_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_1.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_2.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_3.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda3_4.jpg'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/bg_end_7.jpg')]
#CONSTbg_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda4_1.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda4_2.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda4_3.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda4_4.jpg'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/bg_end_5.jpg')]
#CONSTbg_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda1_1.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda1_2.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda1_3.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda1_4.jpg'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/bg_end_5.jpg')]
#CONSTbgg_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda2_1.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda2_2.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda2_3.jpg'),pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/zelda2_4.jpg'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/bg2.jpg')]
CONSTc_sprites = [pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin4.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin5.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Coins/coin6.png')]
CONSTp_sprites = [[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Mario/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Red/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Sonic/up4.png')]],[[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/right4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/left4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/down4.png')],[pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up1.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up2.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up3.png'), pygame.image.load('/home/pi/cloudbook/juego/distributed/Sprites/Undertale/up4.png')]]]
CONSTcoin_diameter = 24
CONSTroom_width = 700
CONSTroom_height = 500
CONSTplayer_speed = 125

#__CLOUDBOOK:LOCAL__
def update_player(index, player):
	global game_status
	game_status[index] = player

#__CLOUDBOOK:LOCAL__
def start_photogram_clock():
	global game_status
	photogram_counter = 0
	while True:
		photogram_counter = photogram_counter + 1
		game_status[7] = photogram_counter
		time.sleep(0.05)

#__CLOUDBOOK:LOCAL__
def refresh_status(player_selected, status):
	global game_status
	aux_status = game_status
	for i in range(0,len(aux_status)):
		if i != player_selected:
			status[i] = aux_status[i]

#__CLOUDBOOK:LOCAL__
def get_status():
	global game_status
	aux_status = game_status
	return aux_status

#__CLOUDBOOK:PARALLEL__
def loop(player_selected):
	if player_selected == 1:
		#__CLOUDBOOK:NONBLOCKING__
		start_photogram_clock()
	#-----Pygame initialization-------
	pygame.init()
	pygame.display.set_caption("Game Window " + str(player_selected))
	#-----Starts the sound mixer------
	pygame.mixer.init()
	music = pygame.mixer.music.load('/home/pi/cloudbook/juego/distributed/Sprites/Music/music.mp3')
	time.sleep(0.5)
	pygame.mixer.music.set_volume(0.2)
	#pygame.mixer.music.set_volume(0)
	pygame.mixer.music.play(-1)
	#-----Creates local varaibles-----
	status = get_status()
	last_cycle_positions = [0, [100,350,0], [250,350,0], [400,350,0], [550,350,0]]
	time_measures = []
	refresh_local_counter = 0
	movement_counter = 0
	coin_sprite_counter = 0
	photogram_counter = -1
	run = True
	sorted_status = False
	#sorted_status = True
	window = pygame.display.set_mode((CONSTroom_width, CONSTroom_height))
	CLOCK_FPS = 20
	clock = pygame.time.Clock()
	keys = pygame.key.get_pressed()
	#---Starts the joystick module----
	if not pygame.joystick.get_init():
		pygame.joystick.init()
	n_joysticks = pygame.joystick.get_count()
	joystick_input = (0,0)
	last_joystick_input = (0,0)
	if n_joysticks != 0:
		my_joystick = pygame.joystick.Joystick(0)
		my_joystick.init()
	#----------Ping testing-----------
	ping_measures = []
	clk = 1/CLOCK_FPS
	T1 = time.time()
	T2 = time.time() - clk
	for i in range(1,10):
		P1_start = time.time()
		status = get_status()
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
	#-------Game loop starts----------
	while run:
		#-----------events--------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.JOYAXISMOTION:
				last_joystick_input = joystick_input
				axis0 = round(my_joystick.get_axis(0))
				axis1 = round(my_joystick.get_axis(1))
				joystick_input = (axis0,axis1)
		#-------------------------------
		#Locks a maximun of frames per second, so that all players can move with the same frequency, regardless of their processor speed
		clock.tick(CLOCK_FPS)
		if not status[5]:
			#--------FPS management--------
			T1 = T2
			T2 = time.time()
			resta = T2 - T1
			if len(time_measures) <= 12:
				if resta < 2:
					time_measures.append(resta)
			else:
				if player_selected == 1:
					CLOCK_FPS = update_fps(time_measures)
				time_measures = []
			#-------------------------------
			#------cycle management---------
			status[7] = status[7] + 1
			#photogram_counter = photogram_counter + 1
			refresh_local_counter = refresh_local_counter + 1
			if refresh_local_counter >= 5:
				#__CLOUDBOOK:NONBLOCKING__
				refresh_status(player_selected,status)
				refresh_local_counter = 0
			coin_sprite_counter = coin_sprite_counter + 1
			if coin_sprite_counter >= 36:
				coin_sprite_counter = 0
			status[player_selected][5] = status[player_selected][5] + 1
			if status[player_selected][5] >= 24:
				status[player_selected][5] = 0
			if status[player_selected][6]:
				status[player_selected][5] = 0
			#-------------------------------
			#---------check keys------------
			keys_last_cycle = keys
			keys = pygame.key.get_pressed()
			speed = round(CONSTplayer_speed/CLOCK_FPS)
			status = check_move_keys(player_selected,status,keys_last_cycle,keys,joystick_input,last_joystick_input,window,speed,photogram_counter)
			#-------------------------------
			#--------draw_room--------------
			now = time.time()
			last_cycle_positions = speculate_player_positions(player_selected,status,now,CLOCK_FPS,last_cycle_positions,photogram_counter)
			draw_room(player_selected,status,coin_sprite_counter,window,CLOCK_FPS,last_cycle_positions,photogram_counter)
			pygame.display.update()
			#print(status)
			#-------------------------------
		else:
			if not sorted_status:
				sorted_status = True
				status = score_setup(status)
			draw_end_game(status,window)
			pygame.display.update()

#__CLOUDBOOK:LOCAL__
def capture_coin(player_selected, coin):
	global game_status
	aux_status = game_status
	my_player = aux_status[player_selected]
	#print("GLOBAL:",game_status)
	#print()
	#print("AUX_0:",aux_status[0])
	#print()
	#print("COIN:",coin)
	#print("Jugador%d pide capturar moneda: [%d,%d]" % (player_selected,coin[0],coin[1]))
	if coin in aux_status[0]:
		#print("DEBERIA SONAR!!")
		aux_status[0].remove(coin)
		aux_status[6][player_selected - 1] = aux_status[6][player_selected - 1] + 1
		CONSTcoinSound1 = pygame.mixer.Sound('/home/pi/cloudbook/juego/distributed/Sprites/Music/coin2.wav')
		CONSTcoinSound1.set_volume(0.2)
		CONSTcoinSound1.play()
		if len(aux_status[0]) == 0:
			#End of game
			aux_status[5] = 1
			game_status[5] = 1
			print("ENDGAME")
		game_status[0] = aux_status[0]
		game_status[6] = aux_status[6]
		#print("Jugador%d coge moneda! Ya lleva: %d " % (player_selected,aux_status[6][player_selected - 1]))

#__CLOUDBOOK:LOCAL__
def draw_transition(player, player_sprite, room_sprite1, room_sprite2, window, x_dir, y_dir):
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

#__CLOUDBOOK:LOCAL__
def check_move_keys(player_selected, status, keys_last_cycle, keys, joystick_input, last_joystick_input, window, speed, photogram_counter):
	my_player = status[player_selected]
	my_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
	my_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
	v_x = status[player_selected][2]
	v_y = status[player_selected][3]
	test_counter = 4
	player_has_moved = False
	#print("ENTRA EN EL CHECK!!: ", keys)
	if v_x == 0 and v_y == 0:
		#print("Parado")
		#El jugador esta parado; se comprueba si se pulsa una tecla para comenzar algun movimiento, y que pueda moverse en esa direccion
		#------Comineza el movimiento---------Prioridad dasw para poder asignar siempre un sprite
		if (keys[pygame.K_d] or joystick_input[0] == 1) and my_player[0] < (2*CONSTroom_width-64-speed):
			#print("Empieza D")
			status[player_selected][2] = 1
			status[player_selected][3] = 0
			status[player_selected][4] = 0
			status[player_selected][6] = 0
			#status[player_selected][7] = time.time()
			status[player_selected][7] = status[7]
			status[player_selected][8] = 1
			aux_player = status[player_selected]
			player_has_moved = True
			#------Da comienzo transicion de sala---------
			if(aux_player[0] < CONSTroom_width and aux_player[0] + speed >= CONSTroom_width):
				#print()
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
				status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
				status[player_selected][2] = 0
				status[player_selected][3] = 0
				status[player_selected][5] = 0
				status[player_selected][6] = 1
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if aux_player[1] < CONSTroom_height:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,1,0)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,1,0)
		elif (keys[pygame.K_a] or joystick_input[0] == -1) and my_player[0] > speed:
			#print("Empieza A")
			status[player_selected][2] = -1
			status[player_selected][3] = 0
			status[player_selected][4] = 1
			status[player_selected][6] = 0
			#status[player_selected][7] = time.time()
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if aux_player[1] < CONSTroom_height:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,-1,0)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,-1,0)
				status[player_selected][0] = status[player_selected][0] - speed
		elif (keys[pygame.K_s] or joystick_input[1] == 1) and my_player[1] < (2*CONSTroom_height-64-speed):
			#print("Empieza S")
			status[player_selected][2] = 0
			status[player_selected][3] = 1
			status[player_selected][4] = 2
			status[player_selected][6] = 0
			#status[player_selected][7] = time.time()
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if aux_player[0] < CONSTroom_width:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,1)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,1)
				status[player_selected][1] = status[player_selected][1] + speed
		elif (keys[pygame.K_w] or joystick_input[1] == -1) and my_player[1] > speed:
			#print("Empieza W")
			status[player_selected][2] = 0
			status[player_selected][3] = -1
			status[player_selected][4] = 3
			status[player_selected][6] = 0
			#status[player_selected][7] = time.time()
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if aux_player[0] < CONSTroom_width:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,-1)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,-1)
				status[player_selected][1] = status[player_selected][1] - speed
	#El jugador ya se esta moviendo en alguna direccion
	#Lo unico que se comprueba es si deja de moverse en esa dir, todo lo demas significa que se sigue moviendo en esa dir.
	#Las condiciones de parada son o bien que se estuviese moviendo el ciclo anterior y deje de hacerlo, o bien que se choque con el borde del mapa
	elif v_x == 1:
		#Condicion de parada: O bien se
		if ((keys_last_cycle[pygame.K_d] or last_joystick_input[0] == 1) and not (keys[pygame.K_d] or joystick_input[0] == 1)) or not (my_player_x < (2*CONSTroom_width-64-speed)):
			#print("Acaba D")
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			#status[player_selected][7] = time.time()
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			update_player(player_selected,aux_player)
		else:
			#Se sigue moviendo en la misma direccion
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if current_player_y < CONSTroom_height:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,1,0)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,1,0)
	elif v_x == -1:
		if ((keys_last_cycle[pygame.K_a] or last_joystick_input[0] == -1) and not (keys[pygame.K_a] or joystick_input[0] == -1)) or not (my_player_x > speed):
			#print("Acaba A")
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			#status[player_selected][7] = time.time()
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			update_player(player_selected,aux_player)
		else:
			#Se sigue moviendo en la misma direccion
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if current_player_y < CONSTroom_height:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[2],window,-1,0)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[1],CONSTbg_sprites[3],window,-1,0)
	elif v_y == 1:
		if ((keys_last_cycle[pygame.K_s] or last_joystick_input[1] == 1) and not (keys[pygame.K_s] or joystick_input[1] == 1)) or not (my_player_y < (2*CONSTroom_height-64-speed)):
			#print("Acaba S")
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			#status[player_selected][7] = time.time()
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			update_player(player_selected,aux_player)
		else:
			#Se sigue moviendo en la misma direccion
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if current_player_x < CONSTroom_width:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,1)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,1)
	elif v_y == -1:
		if ((keys_last_cycle[pygame.K_w] or last_joystick_input[1] == -1) and not (keys[pygame.K_w] or joystick_input[1] == -1)) or not (my_player_y > speed):
			#print("Acaba W")
			status[player_selected][0] = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
			status[player_selected][1] = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
			status[player_selected][2] = 0
			status[player_selected][3] = 0
			status[player_selected][5] = 0
			status[player_selected][6] = 1
			#status[player_selected][7] = time.time()
			status[player_selected][7] = status[7]
			status[player_selected][8] = 0
			aux_player = status[player_selected]
			#__CLOUDBOOK:NONBLOCKING__
			update_player(player_selected,aux_player)
		else:
			#Se sigue moviendo en la misma direccion
			status[player_selected][8] = status[player_selected][8] + 1
			if status[player_selected][8] == test_counter:
				aux_player = status[player_selected]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
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
				#status[player_selected][7] = time.time()
				status[player_selected][7] = status[7]
				status[player_selected][8] = 0
				aux_player = status[player_selected]
				player_sprite = CONSTp_sprites[player_selected - 1][aux_player[4]][aux_player[5] // 6]
				#__CLOUDBOOK:NONBLOCKING__
				update_player(player_selected,aux_player)
				if current_player_x < CONSTroom_width:
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[0],CONSTbg_sprites[1],window,0,-1)
				else: 
					draw_transition(aux_player,player_sprite,CONSTbg_sprites[2],CONSTbg_sprites[3],window,0,-1)
	#Checks if any coin has been touched by the player after its last movement
	if player_has_moved:
		my_player_x = status[player_selected][0] + status[player_selected][2]*speed*status[player_selected][8]
		my_player_y = status[player_selected][1] + status[player_selected][3]*speed*status[player_selected][8]
		hitbox = pygame.Rect(my_player_x, my_player_y, 64, 64)
		coins = status[0]
		for c in coins:
			if hitbox.collidepoint(c[0] + CONSTcoin_diameter/2, c[1] + CONSTcoin_diameter/2):
				status[0].remove(c)
				#__CLOUDBOOK:NONBLOCKING__
				capture_coin(player_selected,c)
	return status

#__CLOUDBOOK:LOCAL__
def draw_room(player_selected, aux_status, aux_coin_count, window, CLOCK_FPS, last_cycle_positions, photogram_counter):
	coins = aux_status[0]
	speed = round(CONSTplayer_speed/CLOCK_FPS)
	my_player = aux_status[player_selected]
	my_player_x = my_player[0] + my_player[2]*speed*my_player[8]
	my_player_y = my_player[1] + my_player[3]*speed*my_player[8]
	now = time.time()
	#Draws background, coins and other players depending on player_selected position
	#Top left room
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
					#window.blit(p_sprite, (p[0]%CONSTroom_width, p[1]%CONSTroom_height))
					window.blit(p_sprite, (p[0], p[1]))
	#Bottom left room
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
					#window.blit(p_sprite, (p[0]%CONSTroom_width, p[1]%CONSTroom_height))
					window.blit(p_sprite, (p[0], p[1]-CONSTroom_height))
	#Top right room
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
					#window.blit(p_sprite, (p[0]%CONSTroom_width, p[1]%CONSTroom_height))
					window.blit(p_sprite, (p[0]-CONSTroom_width, p[1]))
	#Bottom right room
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
					#window.blit(p_sprite, (p[0]%CONSTroom_width, p[1]%CONSTroom_height))
					window.blit(p_sprite, (p[0]-CONSTroom_width, p[1]-CONSTroom_height))
	#Draws player_selected
	i = aux_status[player_selected][5] // 6
	j = aux_status[player_selected][4]
	my_player_sprite = CONSTp_sprites[player_selected - 1][j][i]
	window.blit(my_player_sprite, (last_cycle_positions[player_selected][0]%CONSTroom_width, last_cycle_positions[player_selected][1]%CONSTroom_height))
	pygame.display.update()

#Modifies the last_cycle_positions to get the next positions
#__CLOUDBOOK:LOCAL__
def speculate_player_positions(player_selected, status, now, CLOCK_FPS, last_cycle_positions, photogram_counter):
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
			#x = player[0] + round(player[2]*speed*time_passed*CLOCK_FPS)
			#y = player[1] + round(player[3]*speed*time_passed*CLOCK_FPS)
			unkown_cycles = status[7] - player[7]
			x = player[0] + round(player[2]*speed*unkown_cycles)
			y = player[1] + round(player[3]*speed*unkown_cycles)
			if player[2] == 0 and player[3] == 0:
				playerWalkCount = 0
			else:
				playerWalkCount = int(time_passed/(1/CLOCK_FPS)%24)
			#-----------Error correcting script--------------------
			x_dif = abs(x - last_cycle_positions[n_player][0])
			y_dif = abs(y - last_cycle_positions[n_player][1])
			if x_dif > 10:
				x = int((x + last_cycle_positions[n_player][0])/2)
			if y_dif > 10:
				y = int((y + last_cycle_positions[n_player][1])/2)
			last_cycle_positions[n_player][2] = playerWalkCount
			#------------------------------------------------------
		last_cycle_positions[n_player][0] = x
		last_cycle_positions[n_player][1] = y
	return last_cycle_positions	

#Sorts the player list depending on their score, so in the score screen they are represented in the right order.
def score_setup(status):
	global game_status
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
	return sorted_status

#__CLOUDBOOK:LOCAL__
def update_fps(time_measures):
	mean = sum(time_measures) / (len(time_measures))
	fps_mean = round(1/mean)
	new_fps = (fps_mean + 20) / 2
	#print(time_measures)
	#print("NEW FPS: ", new_fps)
	return new_fps

#Draws the end screen with player score
#__CLOUDBOOK:LOCAL__
def draw_end_game(status, window):
	window.blit(CONSTbg_sprites[4], (0,0))
	for i in range(1,5):
		#window.blit(CONSTp_sprites[i - 1][2][0], (status[i][0]%500,status[i][1]%500))
		window.blit(CONSTp_sprites[status[i][10]][2][0], (60+(i-1)*40,55+(i-1)*95))

def main():
	global game_status
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
	game_status = game_aux
	loop(1)
	loop(2)
	loop(3)
	loop(4)
	#SYNC
	print("Game ended")

main()