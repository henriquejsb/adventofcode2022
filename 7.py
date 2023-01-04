USED = 44965705
TOTAL =70000000
sol = TOTAL
FREE=25034295
UNUSED=30000000
def recursive(folder):
	global sol
	size = 0
	while True:
		try:
			command = input()
			if command == '$ cd ..':
				#print(folder,size)  PART 1
				#if size <= 100000:
				#	sol += size
				if FREE + size >= UNUSED:
					sol = min(sol,size)
				return size
			parse = command.split()
			if parse[0] == '$':
				if parse[1] == 'cd':
					size += recursive(parse[2])
			elif parse[0] != 'dir':
				size += int(parse[0])
		except EOFError:
			break
	return size

def main():
	global sol
	print(recursive(''))
	print(sol)
if __name__ == '__main__':
	main()