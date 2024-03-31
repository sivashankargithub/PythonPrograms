def createDir(dictM):
    import os
    dict1=dictM
    s1=dict1.values()
    s2=dict1.keys()
    list1=list(s2)
    list2=list(s1)

    root1="Movies"
    os.mkdir(root1)
    os.chdir(root1)
    for i in range(0,3,1):
        os.mkdir(list1[i])
    for j in range(0,3,1): 
        list3=list2[j]
        len1=len(list3)
        os.chdir(list1[j])
        for i in range(0,len1,1):
            os.mkdir(list3[i])
        os.chdir("..")

dict1={
       "Sholay":["SanjeevKumar","AmitabhBuchchan","Dharmendra","Hemamalini","Jayabhaduri"],
       "Lagaan":["AmirKhan","GracySingh"],
       "Swadesh":["Sharukhan","Gayatri"]
    }
createDir(dict1)
