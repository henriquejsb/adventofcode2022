def main():
	score = 0
	points = {'X':0,'Y':3,'Z':6}
	plays = {'A':{'X':'C','Y':'A','Z':'B'},'B':{'X':'A','Y':'B','Z':'C'},'C':{'X':'B','Y':'C','Z':'A'}}
	constant = {'A':1,'B':2,'C':3}
	while True:
		try:
			opponent,me = input().split()
			my_move = plays[opponent][me]
			score += points[me] + constant[my_move]
		except EOFError:
			break
	print(score)
if __name__ == '__main__':
	main()