GOLD = 1

def simulate(monkeys):
	global GOLD
	for monkey in monkeys:
		while monkey['queue']:
			old = monkey['queue'].pop(0)
			new = eval(monkey['op']) #// 3
			next_monkey = monkey['choices'][new % monkey['test'] == 0]
			monkeys[next_monkey]['queue'].append(new % GOLD)
			monkey['inspections'] += 1



def main():
	global GOLD
	monkeys = []

	while True:
		try:
			monkey = {}
			if 'Monkey' not in input(): #initial line
				continue
			monkey['queue'] = eval('[' + input().split(':')[1] + ']')
			monkey['op'] = input().split(':')[1].split('=')[1]
			monkey['test'] = int(input().replace('Test: divisible by ','').replace(' ',''))
			GOLD  *= monkey['test']
			true = int(input().replace('If true: throw to monkey ','').replace(' ',''))
			false = int(input().replace('If false: throw to monkey ','').replace(' ',''))
			monkey['choices'] = [false,true]
			monkey['inspections'] = 0
			monkeys.append(monkey)
		except EOFError:
			break

	#lens = []
	for _round in range(10000):
		#print(_round)
		simulate(monkeys)
	inspections = sorted([(monkeys[i]['inspections'],i) for i in range(len(monkeys))])[::-1]
	print(inspections)
	monkey_business = inspections[0][0] * inspections[1][0]
	print(monkey_business)

if __name__ == '__main__':
	main()