def taller(curr,tree):
	return tree >= curr

def checkUp(MAP,i,j):
	score = 0
	curr = MAP[i][j]
	for I in range(i-1,-1,-1):
		score += 1
		if taller(curr,MAP[I][j]):
			break
	return score

def checkDown(MAP,i,j):
	curr = MAP[i][j]
	score = 0
	for I in range(i+1,len(MAP)):
		score += 1
		if taller(curr,MAP[I][j]):
			break
	return score

def checkLeft(MAP,i,j):
	score = 0
	curr = MAP[i][j]
	for J in range(j-1,-1,-1):
		score += 1
		if taller(curr,MAP[i][J]):
			break
	return score

def checkRight(MAP,i,j):
	score = 0
	curr = MAP[i][j]
	for J in range(j+1,len(MAP)):
		score += 1
		if taller(curr,MAP[i][J]):
			break
	return score


def main():
	MAP = []
	while True:
		try:
			MAP += [input()]
		except EOFError:
			break
	res = 0

	for i in range(1,len(MAP)-1):
		for j in range(1,len(MAP)-1):
			
			up = checkUp(MAP,i,j)
			down = checkDown(MAP,i,j)
			right = checkRight(MAP,i,j)
			left = checkLeft(MAP,i,j)

			scenic_score = up * down * right * left
			#print('[',i,j,']',MAP[i][j],'\t\t',up,left,down,right,'\t',scenic_score)

			res = max(res,scenic_score)
	
	print(res)
	#print(len(MAP),len(MAP[0]))
if __name__ == '__main__':
	main()