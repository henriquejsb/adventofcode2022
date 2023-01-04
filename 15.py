MAX = 20
#MAX = 4000000

def manhattan_distance(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1-y2)

def merge_intervals(intervals):
	if len(intervals) < 2:
		return
	can_merge = True
	while can_merge:
		can_merge = False
		for i in range(1,len(intervals)):
			if can_merge:
				break
			for j in range(i):

				l1,l2 = min(intervals[j],intervals[i])
				r1,r2 = max(intervals[j],intervals[i])

				if l2 < r1-1 :
					continue

				can_merge = True

				L = l1#min(l1,r1) #unnecessary
				R = max(l2,r2)
				
				#print("\t",(l1,l2),(r1,r2),(L,R))
				intervals.pop(i)
				intervals.pop(j)
				intervals.append((L,R))
				#print("\t",intervals)
				break
	return






def solve(sensors, beacons, N, occupied):
	sol = 0
	for i in range(N):
		#print(i,N)
		sx,sy = sensors[i]
		bx,by = beacons[i]
		radius = manhattan_distance(sx,sy,bx,by)
		#if abs(sx) > radius and abs(sx-MAX) > radius and abs(sy) > radius and abs(sy-MAX) > radius:
			#range is out of bounding box
		#	print("OUT")
		#	continue
		if sy+radius+1 < 0 or sy-radius > MAX:
			continue
		if sx+radius+1 < 0 or sx-radius > MAX:
			continue

		min_y = max(0,sy-radius)
		max_y = min(MAX,sy+radius)


		for y in range(min_y,max_y+1):
			
			available = radius - abs(sy-y)

			min_x = max(0, sx - available)
			max_x = min(MAX, sx + available)
			
			occupied[y].append((min_x,max_x))

	for y in range(MAX+1):
		merge_intervals(occupied[y])
		if len(occupied[y]) > 1:
			
			print("y = "+str(y),occupied[y])
			I1,I2 = occupied[y][0],occupied[y][1]
			left = min(I1,I2)
			X = left[1] + 1
			frequency = X * 4000000 + y
			print("Frequency: " , frequency)
			break
	
		
	return sol

def main():
	sensors = []
	beacons = []
	#occupied = [[0 for i in range(MAX+1)] for j in range(MAX+1)]
	occupied = [[] for i in range(MAX+1)]
	
	N = 0
	while True:
		try:
			sensor,beacon = input().replace('Sensor at ','').replace('closest beacon is at ','').replace('x=','').replace('y=','').replace(' ','').split(':')
			s_x,s_y = map(int,sensor.split(','))
			b_x,b_y = map(int,beacon.split(','))
			sensors += [(s_x,s_y)]
			beacons += [(b_x,b_y)]
			if s_x > 0 and s_x <= MAX and s_y > 0 and s_y <= MAX :
				occupied[s_y].append((s_x,s_x))
			
			if b_x > 0 and b_x <= MAX and b_y > 0 and b_y <= MAX :
				occupied[b_y].append((b_x,b_x))
			
			N += 1
		except EOFError:
			break
	sol = solve(sensors,beacons,N,occupied)
	#print(sol)

if __name__ == '__main__':
	main()