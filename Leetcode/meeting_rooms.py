ip = [[0, 30],[5, 10],[15, 20]]
ip = [[7,10],[2,4]]
ip.sort()
print(ip)

ip = [[9,10],[4,9],[4,17]]
ip = [[2,11],[6,16],[11,16]]
ip = [[1,5],[8,9],[8,9]]
ip = [[2,15],[36,45],[9,29],[16,23],[4,9]]
print(sorted(ip, key=lambda x: x[1]))

def _meetings(ip):
    meetings = {}
    cnt = 0
    ip = sorted(ip, key=lambda x: x[1])
    ip.sort()
    print(ip)
    for i in ip:
        if not meetings:
            cnt += 1
            meetings[cnt] = [i]
        else:
            append = False
            #curr_meet_start, curr_meet_end = meetings[cnt][-1][0], meetings[cnt][-1][1]
            for key, val in meetings.items():
                if i[0] >= val[-1][1]:
                    meetings[key].append(i)
                    append = True
                    break
            if not append:
                cnt += 1
                meetings[cnt] = [i]
    print(meetings)
    return cnt


min = _meetings(ip)
print(min)
