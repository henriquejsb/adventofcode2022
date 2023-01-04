def main():
	res = 0
	while True:
		try:
			elf1,elf2,elf3 = input(), input(), input()
			print(elf1,elf2,elf3)
			for c in elf1:
				if c in elf2 and c in elf3:
					print(c)
					if c.islower():
						res += ord(c) - 96
					else:
						res += ord(c) - 38
					break
		except EOFError:
			break
	print(res)
if __name__ == '__main__':
	main()