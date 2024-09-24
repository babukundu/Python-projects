# Project 2, semester 1, 2022
# written by Ronjon Kundu, 23215183

def main(csvfile, adultIDs):

#open file in read mode and save it to a list
    if(csvfile and csvfile.strip() and len(adultIDs)==2):
        try: #try...exception to check file existence
            with open(csvfile,'r', encoding='utf-8') as f:
                results=[]
                for line in f:
                    words=line.split(",")
                    results.append(words)
            # function to calculate the facial distance
            def calfacialdist(file,ID):
                collist=[]
                lst=['Ft_L','FT_R','Ex_L','Ex_R','Ex_L','En_L','En_R','Ex_R','En_L','En_R','Al_L','Al_R','Sbal_L','Sbal_R','Ch_L','Ch_R','N','Prn','N','Sn']
                for row in results:
                    if ID==row[0]:
                        collist.append(row[1:])     
                rows, cols = (20, 2)
                arr=[]
                for i in range(0,rows,2):
                    col = []
                    for j in range(cols):
                        for col1 in collist:
                            if col1[0].upper()==lst[i+j].upper() and i+j<rows:
                                for m in range(1,4):
                                    a=float(col1[m])
                                    #check the value is in limit or not
                                    if a>-200 and a<200:
                                        col.append(a)

                    arr.append(col)
                if (0 in arr):
                    return False
                else:
                    eqdist=[]
                    for c in range(10):
                        sum=0
                        for i in range(3):
                            cal=arr[c][i+3]-arr[c][i]
                            sum=sum+cal**2
                        eqdist.append(sum**0.5)
                    return eqdist
            
            landmarklst=["FW","OCW","LEFL","REFL","ICW","NW","ABW","MW","NBL","NH"]
            almlst={}
            blmlst={}
            alist=calfacialdist(results,adultIDs[0])
#             print(alist)
            if alist!=False:
    #             print(alist)
    #             print(len(alist))
                for i in range(len(alist)):
                    almlst[landmarklst[i]]=round(alist[i],4)
            else:
                return False
            
            blist=calfacialdist(results,adultIDs[1])
            if blist!=False:
    #             print(blist)
    #             print(len(blist))
                for i in range(len(blist)):
                    blmlst[landmarklst[i]]=round(blist[i],4)
            else:
                return False
            
    #         print(almlst,blmlst)
            def similarity(dict1,dict2):
                finallst=[dict1,dict2]
                aval=list(dict1.values())
                bval=list(dict2.values())
                sumtotal=0
                sumlst1=0
                sumlst2=0
                for i in range(len(aval)):
                    sumtotal=sumtotal+aval[i]*bval[i]
                    sumlst1=sumlst1+aval[i]**2
                    sumlst2=sumlst2+bval[i]**2
                sumlst1_rs=sumlst1**0.5
                sumlst2_rs=sumlst2**0.5
                calsim=sumtotal/(sumlst1_rs*sumlst2_rs)
                return finallst,calsim
            if(True):
    #             print(aval,bval)
    #             print(aval,bval)
                op1,sim=similarity(almlst,blmlst)
            else:
                return None
                
            IDlist=[]
            for row in results:
                IDlist.append(row[0])
    #             print(IDlist)
            def unique(IDlst):
                unique_IDlst = []
                for x in IDlst:
                    if x not in unique_IDlst:
                        unique_IDlst.append(x)
                return unique_IDlst
            
            uIDlst=unique(IDlist[1:])
    #             print(uIDlst)
            def findop3(adultID1,adultID2):
                count=0
    #             print(adultID1,adultID2)
                tup=()
                tuplst=[]
                for ids in uIDlst:
                    if ids!=adultID1 and ids!=adultID2:
                        idslist=calfacialdist(results,ids)
                        idslmlst={}
                        if idslist!=False:
                            for i in range(len(idslist)):
                                idslmlst[landmarklst[i]]=round(idslist[i],4)
                        else:
                            return False
                        id1list=calfacialdist(results,adultID1)
                        id1lmlst={}
                        if id1list!=False:
                            for i in range(len(id1list)):
                                id1lmlst[landmarklst[i]]=round(id1list[i],4)
                        else:
                            return False
                        
                        op1,sim=similarity(id1lmlst,idslmlst)
    #                     if round(sim,4)>0.9900 and round(sim,4)<1.0000 and count<5:
                        tup=(ids,sim)
    #                     print(tup)
                        tuplst.append(tup)
                lst = len(tuplst)
                for i in range(0, lst): 
                    for j in range(0, lst-i-1):
                        if (tuplst[j][1] < tuplst[j + 1][1]):
                            temp = tuplst[j]
                            tuplst[j]= tuplst[j + 1]
                            tuplst[j + 1]= temp
                        elif (tuplst[j][1] == tuplst[j + 1][1]):
                            if tuplst[j][0] < tuplst[j + 1][0]:
                                (tuplst[j],tuplst[j + 1])= (tuplst[j+1],tuplst[j])
#                 print(type(tuplst))
                
                return tuplst[:5]
    #                         count +=1
            
            def lstround(lst):
                tup=()
                tuplstrnd=[]
                for x in lst:
                    a=round(x[1],4)
                    tup=(x[0],a)
                    tuplstrnd.append(tup)
                return tuplstrnd
            
            op3lst1=findop3(adultIDs[0],adultIDs[1])
            op3lst2=findop3(adultIDs[1],adultIDs[0])
            op3lst1rnd=lstround(op3lst1)
            op3lst2rnd=lstround(op3lst2)
            op3=[]
            op3.append(list(op3lst1rnd))
            op3.append(list(op3lst2rnd))
            def findop4(lst):
                op4lst=[]
                for i in range(len(lst)):
    #                 print(op3lst1[i][0])
                    alist=calfacialdist(results,lst[i][0])
                    op4lst.append(alist)
    #             print(op4lst)
    #             print(type(op4lst))
                sumlst=[]
                i = 0
                while i < 10:
                    sum=0
                    for j in range(5):
    #                     print(j,op4lst[j][i])
                        sum=sum+op4lst[j][i]
                    sumlst.append(sum/5)
                    i += 1
                return sumlst
            op4lmlst1={}
            op4lmlst2={}
            op4lst1=findop4(op3lst1)
#             print(op4lst1)
            for i in range(len(op4lst1)):
                    op4lmlst1[landmarklst[i]]=round(op4lst1[i],4)
            op4lst2=findop4(op3lst2)
            for i in range(len(op4lst2)):
                    op4lmlst2[landmarklst[i]]=round(op4lst2[i],4)
            op4=[op4lmlst1,op4lmlst2]
            
#             print(op4lst2)
            print(op1)
            print(round(sim,4))
            print(op3)
            print(op4)
        except FileNotFoundError as e:
            return e
    else:
        return None

        
        
        
           
