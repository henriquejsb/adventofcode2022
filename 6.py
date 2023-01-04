def main():
	text = input()
	for i in range(len(text)):
		if len(set(text[i:i+14])) == 14:
			print(i+14)
			break

if __name__ == '__main__':
	main()