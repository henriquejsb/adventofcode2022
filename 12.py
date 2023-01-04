SOL = 0
H = 0
W = 0
MAP = []
E_i = 0
E_j = 0
DP = []

import sys
sys.setrecursionlimit(1500)


def solution(visited,i,j,steps):
	global MAP,SOL,H,E_i,E_j,DP
	
	height = MAP[i][j]

	if steps >= DP[i][j]:
		return

	DP[i][j] = steps

	if steps >= SOL:
		return

	if height == 0:
		#print("FOUND")
		SOL = steps
		return

	visited[i][j] = True

	#right
	if j < W-1 and MAP[i][j+1] - height >= -1 and not visited[i][j+1]:
		solution(visited,i,j+1,steps+1)
	
	#up
	if i > 0 and MAP[i-1][j] - height >= -1 and not visited[i-1][j]:
		solution(visited,i-1,j,steps+1)
	#left
	if j > 0 and MAP[i][j-1] - height >= -1 and not visited[i][j-1]:
		solution(visited,i,j-1,steps+1)
	#down
	if i < H-1 and MAP[i+1][j] - height >= -1 and not visited[i+1][j]:
		solution(visited,i+1,j,steps+1)

	visited[i][j] = False


def main():
	global MAP,SOL,H,W,E_i,E_j,DP

	i = j = 0
	E_i = E_j = 0
	S_i = S_j = 0
	while True:
		try:
			line = input()
			if 'S' in line:
				S_i, S_j = i, line.index('S')
			if 'E' in line:
				E_i, E_j = i, line.index('E')
			aux = []
			for C in line:
				if C == 'S':
					aux += [0]
				elif C == 'E':
					aux += [25]
				else:
					aux += [ord(C) - 97]
			MAP.append(aux)
			i += 1
		except EOFError:
			break
	H,W = i, len(MAP[0])
	SOL = H*W

	DP = [[SOL for i in range(W)] for j in range(H)]

	visited = [[False for i in range(W)] for j in range(H)]
	#visited[S_i][E_i] = True

	solution(visited,E_i,E_j,0)

	print(SOL)
if __name__ == '__main__':
	main()