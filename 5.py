def main():
	res = 0
	stacks = [[] for i in range(9)]
	for i in range(8):

		line = input()
		index = 1
		for i in range(9):
			crate = line[index]
			if crate != ' ':
				stacks[i].append(crate)
			index += 4
	for i in range(9):
		stacks[i] = stacks[i][::-1]

	print(stacks)
	input()
	input()
	while True:
		try:
			move = input().split()
			N,origin,dest = map(int,[move[1],move[3],move[5]])
			aux = []
			for i in range(N):
				crate = stacks[origin-1].pop()
				aux.append(crate)
			aux = aux[::-1]
			for c in aux:
				stacks[dest-1].append(c)
		except EOFError:
			break
	res = ''
	for stack in stacks:
		res += stack[-1]
	print(res)
if __name__ == '__main__':
	main()