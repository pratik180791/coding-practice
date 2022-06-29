class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        my_res = []

        for i in cpdomains:
            cnt, domain = i.split()
            cnt = int(cnt)
            if domain in res:
                res[domain] = res[domain]+cnt
            else:
                res[domain] = cnt
            for j in range(len(domain)):
                if '.' in domain[j]:
                    if domain[j+1::] in res:
                        res[domain[j+1::]] = res[domain[j + 1::]]+cnt
                    else:
                        res[domain[j+1::]] = cnt
        for i, j in res.items():
            my_res.append(i+" "+str(j))
            my_res.append(str(j)+" "+i)
        return my_res



ip = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
ip_ = ["9001 discuss.leetcode.com"]
Solution().subdomainVisits(ip)
