def getMinGates(landingTimes, takeOffTimes, maxWaitTime, initialPlanes):
    # Write your code here
    gates = {}
    cnt = initialPlanes
    for i, land_time in enumerate(landingTimes):
        if not gates:
            cnt+=1
            gates[cnt] = [[land_time, takeOffTimes[i]]]
        else:
            add_gate = False
            for key, val in gates.items():
                if land_time>=val[-1][1]:
                    gates[key].append([land_time, takeOffTimes[i]])
                    add_gate = True
                    break
            if not add_gate:
                cnt+=1
                gates[cnt] = [[land_time, takeOffTimes[i]]]
    return cnt

5, 630, 645, \
730, 830, 1100, 0
wait = 20
initial = 0
