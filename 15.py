def bestbatsman2(fmatches):
    def bestbatsman1(fname):
        f1=open(fname,"r")
        for i in range(0,71,1):
            f1.readline()
        list1=f1.readlines()
        len1=len(list1)
        batsmans=[]
        runs=[]
        for i in range(0,len1,1):
            a1=list1[i].split(",")
            batsmans.append(a1[4])
            runs.append(a1[7])
        set1=set(batsmans)
        players=list(set1)
        len2=len(batsmans)
        total=[]

        len3=len(players)
        for j in range(0,len3,1):
            total1=0
            for i in range(0,len2,1):
                if(players[j]==batsmans[i]):
                    total1=total1+int(runs[i])
            total.append(total1)

        max1=max(total)
        pos1=total.index(max1)
        bestbatsman=players[pos1]
        return (bestbatsman,max1)

    f2=open(fmatches,"r")
    for i in range(0,8,1):
        match1=f2.readline().replace("\n","")
        result1=bestbatsman1(match1)
        print(result1[0],result1[1])

bestbatsman2("cric1.txt")
        


