# Project 1, semester 1, 2022
# written by Ronjon Kundu, 23215183

def main(file,adult,choice):

#open file in read mode and save it to a list
    with open(file,'r') as f:
        results=[]
        for line in f:
            words=line.split(",")
            results.append(words)
        print(results)

# #define calculate function to calculate asymtry and others
#         def calculate(results,adult):
#             col=[]
#             for row in results:
# # check the value at nose point
#                 if adult==row[0] and '10'==row[1]:
#                         a=float(row[2])
#                         b=float(row[3])
#                         c=float(row[4])
#     #                     print(a,b,c)
# # convert values to float
#                 if adult==row[0]:
#                         row[1] = int(row[1])
#                         for j in range(2,5):
#                             row[j]=float(row[j])
#  
#                         col.append(row)
# # create empty lists for the values
#             asym_list=[]
#             mn1=[]
#             mx1=[]
#             avg1=[]
#             std1=[]
#             for i in range(0,9):
# # calibration                
#                 if a!=0:
#                     col[i][2]=col[i][2]-a
#                 if b!=0:
#                     col[i][3]=col[i][3]-b
#                 if c!=0:
#                     col[i][4]=col[i][4]-c
#                 
#                 sum=0
#                 for j in range(2,5):
#                     sum=sum+col[i][j]*col[i][j]
#                 asym3d=sum**0.5
# 
#                 asym3dround=round(asym3d,4)
# 
#                 asym_list.append(asym3dround)
# 
# # function to find minimum of a list            
#             def find_min( list ):
#                 min = list[ 0 ]
#                 for a in list:
#                     if a < min:
#                         min = a
#                 return min
#                     
#             uppermin = find_min(asym_list[0:6])
# 
#             mn1.append(uppermin)
#             
#             lowermin = find_min(asym_list[5:10])
# 
#             mn1.append(lowermin)
# 
# # function to find maximum of a list                    
#             def find_max(list):
#                 max_value = None
# 
#                 for num in list:
#                     if (max_value is None or num > max_value):
#                         max_value = num
# 
#                 return max_value
# # function to find average of a list            
#             def find_avg(list):
#                 total=0
#                 for ele in range(0, len(list)):
#                     total = total + list[ele]
#                 return round(total/len(list),4)
#                       
#             
#             uppermax = find_max(asym_list[0:6])
# 
#             mx1.append(uppermax)
#             
#             lowermax = find_max(asym_list[5:10])
# 
#             mx1.append(lowermax)
# 
#             
#             upperavg=find_avg(asym_list[0:5])
#             avg1.append(upperavg)
#             loweravg=find_avg(asym_list[5:10])
#             avg1.append(loweravg)
#     
# # function to find standard deviation of a list            
#             def find_std(list,avg):
#                 summ=0
#                 for item in list:
#                     sub=item-avg
#                     summ=summ+sub*sub
#                 square_std=summ/len(list)
#                 std=square_std**0.5
#                 return round(std,4)
#                
#             upperstd=find_std(asym_list[0:5],upperavg)
#             std1.append(upperstd)
#             lowerstd=find_std(asym_list[5:10],loweravg)
#             std1.append(lowerstd)
#     
#             
#             return asym_list,mn1,mx1,avg1,std1
#         
#         if choice == 'stats':
#             asym_list,mn1,mx1,avg1,std1=calculate(results,adult)
#             return asym_list,mn1,mx1,avg1,std1
#         elif choice=='corr':
#             asym_list11,mn11,mx11,avg11,std11=calculate(results,adult[0])
#             asym_list12,mn12,mx12,avg12,std12=calculate(results,adult[1])
#             avg_1=(avg11[0]+avg11[1])/2
#             avg_2=(avg12[0]+avg12[1])/2
#             total_1=0
#             total_2=0
#             square_total_1=0
#             square_total_2=0
#             corr=0
#             for i in range(len(asym_list11)):
#                 multi=(asym_list11[i]-avg_1)*(asym_list12[i]-avg_2)
#                 total_1=total_1+multi
#                 square_total_1=square_total_1+(asym_list11[i]-avg_1)*(asym_list11[i]-avg_1)
#                 square_total_2=square_total_2+(asym_list12[i]-avg_2)*(asym_list12[i]-avg_2)
#             sqroot1=square_total_1**0.5
#             sqroot2=square_total_2**0.5
#             sqroot_multi=sqroot1*sqroot2
#             corr=total_1/sqroot_multi
#             
#             return round(corr,4)
#         else:
#             print('wrong command')       