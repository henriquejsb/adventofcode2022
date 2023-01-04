
def main():
	register = [1 for i in range(2400)]
	cycle = 1
	while True:
		try:
			instruction = input().split()
			if instruction[0] == 'noop':
				register[cycle+1] = register[cycle]
				cycle += 1
			else:
				register[cycle+1] = register[cycle]
				register[cycle+2] = register[cycle] + int(instruction[1])
				cycle += 2

		except EOFError:
			break
	print(register[:15])
	for i in range(6):
		for j in range(0,40):
			if abs(j-register[i*40 + j+1]) < 2:
				print('#',end='')
			else:
				print('.',end='')
		print('')
	
if __name__ == '__main__':
	main()