def apart(x1,y1,x2,y2):
	return x2-x1 , y2-y1

def simulate(positions,visited,direction):
	H_x, H_y = positions[0]
	
	if direction == 'R':
		H_x += 1
	elif direction == 'L':
		H_x -= 1
	elif direction == 'U':
		H_y += 1
	elif direction == 'D':
		H_y -= 1

	positions[0] = [H_x,H_y]

	for i in range(1,10):
		
		T_x, T_y = positions[i]

		x_dist, y_dist = apart(T_x,T_y,H_x,H_y)

		if x_dist > 1:
			T_x += 1
			if H_y != T_y:
				T_y += [-1,1][H_y > T_y]

		elif x_dist < -1:
			T_x -= 1
			if H_y != T_y:
				T_y += [-1,1][H_y > T_y]

		elif y_dist > 1:
			T_y += 1
			if H_x != T_x:
				T_x += [-1,1][H_x > T_x]

		elif y_dist < -1:
			T_y -= 1
			if H_x != T_x:
				T_x += [-1,1][H_x > T_x]

		visited[i-1] += [str(T_x)+','+str(T_y)]
		positions[i] = [T_x,T_y]
		H_x,H_y = T_x,T_y


def main():
	visited_positions= [[False for i in range(500)] for i in range(500)]
	H_x = H_y = 0
	positions = [[0,0] for i in range(10)]
	visited_positions = [['0,0'] for i in range(9)]

	while True:
		try:
			direction,steps = input().split()
			for i in range(int(steps)):
				simulate(positions,visited_positions,direction)

		except EOFError:
			break

	res = len(set(visited_positions[8]))
	print(res)

if __name__ == '__main__':
	main()