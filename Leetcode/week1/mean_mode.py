

#print(sorted(mode)[0])
def meanAndMode(inputArr):
    total = 0
    mode_cal = {}
    if not inputArr:
        return 0.00, 0.00
    for i in inputArr:
        total+=i
        curr = 0
        if i in mode_cal:
            curr = mode_cal.get(i)+1
            mode_cal.update({i: curr})
        else:
            mode_cal[i] = 1
    mean = round(total/len(inputArr), 2)
    mode = [k for k, v in mode_cal.items() if v == max(list(mode_cal.values()))]
    mode = round(sorted(mode)[0], 2)
    return mean, mode

ip = [4, 7.463, 1,3, 7.463,7.463, 7.463]
op = meanAndMode(ip)
print(op)

print(sum(ip)/7)

def checkIPValidity(addressIP):
	# Write your code here
	if not addressIP:
		return "INVALID"
	ips = addressIP.split(".")
	for i in ips:
		if int(i) <0 or int(i)>255:
			return "INVALID"
	return "VALID"
