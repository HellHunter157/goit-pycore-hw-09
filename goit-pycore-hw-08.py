import heapq

def cabls(cablesCOL):
 
    if len(cablesCOL) <= 1:
        return 0
    heapq.heapify(cablesCOL)
    total_cost = 0
    while len(cablesCOL) > 1:
        first = heapq.heappop(cablesCOL)
        second = heapq.heappop(cablesCOL)
        cost = first + second
        total_cost += cost
        heapq.heappush(cablesCOL, cost)
    return total_cost
cablesCOL = [4, 3, 2, 6]
result = cabls(cablesCOL)
print(result)  # 29
