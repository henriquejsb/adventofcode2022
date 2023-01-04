def main():
	res = 0
	while True:
		try:
			A,B,C,D = map(int,input().replace('-',',').split(','))
			max_n = max(A,B,C,D)+1
			N1 = ['0' for i in range(max_n)]
			for i in range(A,B+1):
				N1[i] = '1'
			N1 = int(''.join(N1),2)
			N2 = ['0' for i in range(max_n)]
			for i in range(C,D+1):
				N2[i] = '1'
			N2 = int(''.join(N2),2)
			aux = N1 & N2
			if aux != 0:
				res += 1
		except EOFError:
			break
	print(res)
if __name__ == '__main__':
	main()