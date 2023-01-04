from copy import deepcopy

MAX_FLOW = 0
sol = 0
MAX_TIME = 26
MAX_VALVES = 0
BEST_PATH = []
def recursive(tunnel,pressure,time,graph,isopen,openvalves,openthis, DP, path):
	global sol
	global BEST_PATH

	flow = graph[tunnel]['flow']
	#print(tunnel,flow)


	if time > MAX_TIME - 1:
		return
	


	if openthis:
		pressure += flow * (MAX_TIME - time)

	if pressure < DP[tunnel][time]:
		return

	DP[tunnel][time] = pressure


	if pressure > sol:
		#print(sol,pressure)
		sol = pressure	
		BEST_PATH = deepcopy(path)
	#sol = max(sol,pressure)

	if openvalves == MAX_VALVES:
		return

	'''
	aux = MAX_VALVES - openvalves
	res = 0
	auxtime = time
	
	for i in range(aux):
		res += MAX_FLOW  * (MAX_TIME - auxtime)
		auxtime -= 2
	if pressure + res < sol:
		#print("exit here	","time:",(MAX_TIME - time - aux * 2))
		return
	'''
	neighbours = graph[tunnel]['adj']
	for N in neighbours:
		path.append(N)

		#walk and open valve
		if not isopen[N] and graph[N]['flow'] > 0:
			isopen[N] = True
			path.append("open")
			recursive(N,pressure,time+2,graph,isopen,openvalves+1,True, DP,path)
			path.pop()
			isopen[N] = False
		#walk only
		recursive(N,pressure,time+1,graph,isopen,openvalves,False, DP,path)
		path.pop()

def main():
	global MAX_FLOW, sol, MAX_VALVES, BEST_PATH
	graph = {}
	isopen = {}
	DP = {}
	while True:
		try:
			aux = input().replace("Valve","").replace("has flow rate","").replace("tunnels lead to valves","").replace("tunnel leads to valve","").replace(" ","")
			aux1,aux2 = aux.split(";")
			tunnel,flow = aux1.split("=")
			adjacent = aux2.split(",")
			graph[tunnel] = {}
			isopen[tunnel] = False
			graph[tunnel]["flow"] = int(flow)
			if int(flow) > 0:
				MAX_VALVES += 1
			MAX_FLOW = max(MAX_FLOW,int(flow))
			graph[tunnel]["adj"] = adjacent
			DP[tunnel] = [0 for i in range(MAX_TIME+1)]
		except EOFError:
			break
	#print(graph)
	#SOL = 0

	recursive('AA',0,0,graph,isopen,0,False, DP, [])
	#SOL += sol
	print(BEST_PATH)
	print(sol)
	elephant_time = 0
	my_time = 0
	my_turn = True
	last_T = ''
	sol = 0
	my_path = []
	el_path = []
	for T in BEST_PATH:
		curr_time = 0
		if my_turn:
			my_time += 1
			curr_time = my_time
			my_path += [T]
		else:
			elephant_time += 1
			curr_time = elephant_time
			el_path += [T]
		if T == 'open':
			flow = graph[last_T]['flow']
			sol += (MAX_TIME - curr_time) * flow
		else:
			last_T = T
		if T == 'AA':
			if my_turn and elephant_time < my_time:
				my_turn = not my_turn
			if not my_turn and my_time < elephant_time:
				my_turn = not my_turn
	print(sol)
	print(my_path)
	print(el_path)



	return
	#sol = 0
	print(len(BEST_PATH),MAX_VALVES)
	


	for N in BEST_PATH:
		isopen[N] = True
	for N in DP.keys():
		DP[N] = [0 for i in range(MAX_TIME+1)]
	#print(SOL)
	recursive('AA',sol,0,graph,isopen,len(BEST_PATH),False, DP, [])
	#SOL += sol
	print(sol)
if __name__ == '__main__':
	main()