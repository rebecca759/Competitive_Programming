class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = {}
        res = []
        vals = set()
        eqs = [(equations[i][0],equations[i][1],values[i]) for i in range(len(equations))]
        i = 0
        while i < len(eqs):
            eq = eqs[i]
            a,b,div = eq[0],eq[1],eq[2]
            vals.add(a)
            vals.add(b)
            j = i+1

            while j < len(eqs):
                # print(eqs)
                if (j != i):
                    a2,b2,prod = eqs[j][0],eqs[j][1],eqs[j][2]

                    if a == a2 and (b,b2) not in dic:
                        dic[(b,b2)] = (1/div)*prod
                        eqs.append((b,b2,(1/div)*prod))

                    elif b == b2 and (a,a2) not in dic:
                        dic[(a,a2)] = div*(1/prod)
                        eqs.append((a,a2,div*(1/prod)))

                    elif a == b2 and (a2,b) not in dic:
                        dic[(a2,b)] = div*prod
                        eqs.append((a2,b,div*prod))

                    elif b == a2 and (a,b2) not in dic:
                        dic[(a,b2)] = div*prod
                        eqs.append((a,b2,div*prod))

                j += 1
            
            i += 1

            dic[(a,b)] = div

        for c,d in queries:
            if (c,d) in dic:
                res.append(dic[(c,d)])

            elif (d,c) in dic:
                res.append(1/dic[(d,c)])

            elif c == d and c in vals:
                res.append(float(1))

            else:
                res.append(float(-1))


        return res


        