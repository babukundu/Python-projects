def main(file,adult):

    with open(file,'r') as f:
        results=[]
        for line in f:
            words=line.split(",")
            results.append(words)
#         print(results)
        col=[]
        for row in results:
            if adult==row[0] and '10'==row[1]:
                    a=float(row[2])
                    b=float(row[3])
                    c=float(row[4])
#                     print(a,b,c)
            if adult==row[0]:
                    row[1] = int(row[1])
                    for j in range(2,5):
                        row[j]=float(row[j])

                    col.append(row)
#         print(col)
#         print(type(col))
        asym_list=[]
        mn1=[]
        mx1=[]
        avg1=[]
        std1=[]
        for i in range(0,9):
            
            if a!=0:
                col[i][2]=col[i][2]-a
            if b!=0:
                col[i][3]=col[i][3]-b
            if c!=0:
                col[i][4]=col[i][4]-c
            sum=0
            for j in range(2,5):
#                 print(col[i][j])
                sum=sum+col[i][j]*col[i][j]
            asym3d=sum**0.5
#             print(sum)
#             print(asym3d)
#             print(type(asym3d))
            asym3dround=round(asym3d,4)
#             print(asym3dround)
            asym_list.append(asym3dround)
        print(asym_list)
        
        def find_min( list ):
            min = list[ 0 ]
            for a in list:
                if a < min:
                    min = a
            return min
                
        uppermin = find_min(asym_list[0:6])
#         print(uppermin)
        mn1.append(uppermin)
        lowermin = find_min(asym_list[5:10])
#         print(lowermin)
        mn1.append(lowermin)
        print(mn1)
                
        def find_max(list):
            max_value = None

            for num in list:
                if (max_value is None or num > max_value):
                    max_value = num

            return max_value
        def find_avg(list):
            total=0
#             print(len(list))
            for ele in range(0, len(list)):
                total = total + list[ele]
            return round(total/len(list),4)
                  
        
        uppermax = find_max(asym_list[0:6])
#         print(uppermax)
        mx1.append(uppermax)
        lowermax = find_max(asym_list[5:10])
#         print(lowermax)
        mx1.append(lowermax)
        print(mx1)
        
        upperavg=find_avg(asym_list[0:5])
        avg1.append(upperavg)
        loweravg=find_avg(asym_list[5:10])
        avg1.append(loweravg)
        print(avg1)
        
        def find_std(list,avg):
            summ=0
            for item in list:
                sub=item-avg
                summ=summ+sub*sub
            square_std=summ/len(list)
            std=square_std**0.5
            return round(std,4)
           
        upperstd=find_std(asym_list[0:5],upperavg)
        std1.append(upperstd)
        lowerstd=find_std(asym_list[5:10],loweravg)
        std1.append(lowerstd)
        print(std1)
