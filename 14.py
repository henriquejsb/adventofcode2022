def simulate(scene,border):
	x,y = 500,0
	void = False
	sand = 0
	while True:
		#try down
		if not scene[x][y+1]:
			y += 1
			#falling into void
			#if y >= border+1:
			#	break
			continue
		#try left down
		if not scene[x-1][y+1]:
			x -= 1
			y += 1
			continue
		#try right down
		if not scene[x+1][y+1]:
			x += 1
			y += 1
			continue
		scene[x][y] = 2
		sand += 1
		if x == 500 and y == 0:
			return sand
		x,y = 500,0
	return sand

def draw_scene(scene):
	for y in range(14):
		for x in range(493,505):
			if scene[x][y] == 1:
				print('#',end='')
			elif scene[x][y] == 2:
				print('o',end='')
			else:
				print('.',end='')
		print("") 


def draw_rocks(scene,coords, last_horizontal):
	print(coords)
	for i in range(1,len(coords)):
		p1,p2 = coords[i-1], coords[i]
		x1,y1 = map(int,p1.split(","))
		x2,y2 = map(int,p2.split(","))
		if x1 == x2:
			#vertical line
			if y1 > y2:
				R = range(y2,y1+1)
			else:
				R = range(y1,y2+1)
			for y in R:
				scene[x1][y] = 1

		else:
			last_horizontal = max(last_horizontal,y1)
			if x1 > x2:
				R = range(x2,x1+1)
			else:
				R = range(x1,x2+1)
			for x in R:
				scene[x][y1] = 1
			#horizontal line
	return last_horizontal

def main():
	last_horizontal = 0
	scene = [[0 for i in range(1000)] for i in range(1000)]
	while True:
		try:
			coords = input().replace(' ','').split('->')
			last_horizontal = draw_rocks(scene,coords,last_horizontal)
		except EOFError:
			break
	ground = ['0,' + str(last_horizontal+2)  , '999,' + str(last_horizontal+2) ]
	
	draw_rocks(scene,ground,last_horizontal)
	
	sand = simulate(scene,last_horizontal)
	print(sand)
if __name__ == '__main__':
	main()