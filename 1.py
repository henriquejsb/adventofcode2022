def main():
	calories = 0
	max_calories = []
	while True:
	    try:
	        input_ = input()
	        if input_ == '':
	        	max_calories += [calories]
	        	calories = 0
	        else:
	        	calories += int(input_)
	    except EOFError:
	    	max_calories += [calories]
	    	break
	print(sorted(max_calories)[::-1])
	print(sum(sorted(max_calories)[::-1][:3]))


if __name__ == '__main__':
	main()