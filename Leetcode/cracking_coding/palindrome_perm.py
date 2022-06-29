def palin_perm(ip_str):
    res = {}
    one_count = []
    for i in ip_str:
        if i.lower() in res:
            res[i.lower()] += 1
        else:
            res[i.lower()] = 1

    for i, j in res.items():
        if j == 1:
            one_count.append(i)
    print(one_count)


ip = "baa"
ip = "Tact Coa"
palin_perm(ip)

ip = "aba"
ip = "baa"


ip = "pratik"
