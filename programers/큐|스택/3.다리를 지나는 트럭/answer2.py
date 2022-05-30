def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_time = []
    bridge_truck = []
    
    while len(truck_weights) > 0:
        if 1 in bridge_time:
            time += 1
            for i in range(len(bridge_time)):
                bridge_time[i] -= 1
            bridge_time.pop(0)
            bridge_truck.pop(0)
            
            if sum(bridge_truck)+truck_weights[0] <= weight:
                bridge_truck.append(truck_weights.pop(0))
                bridge_time.append(bridge_length)
        
        elif sum(bridge_truck)+truck_weights[0] <= weight:
            time += 1
            bridge_truck.append(truck_weights.pop(0))
            for i in range(len(bridge_time)):
                bridge_time[i] -= 1
            bridge_time.append(bridge_length)
            
        else:
            time += 1
            for i in range(len(bridge_time)):
                bridge_time[i] -= 1
            
        if len(truck_weights) == 0:
            return time + bridge_length

print(solution(2, 10, [7,4,5,6]))

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step