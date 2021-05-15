'''
Greedy approach 


sort the jobs based on the finish time, 


since doing the job with least finish time would maximise the total number of activities performed


'''
n=int(input("enter total jobs: "))
job=[] 
print("enter start and end times :")
for i in range(n):
    start,end=map(int,input().split(' '))
    job.append((start,end))
job.sort(key=lambda x:x[1])
print(job)
cnt=0
i=0
prev_finish=0
while(i<len(job)):
    if(prev_finish<=job[i][0]):
        cnt=cnt+1
        prev_finish=job[i][1]
    i+=1
        
print('total activities possible {0}'.format(cnt))
    
    
    
'''
test_case1

   start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};
     
   op/ 2 

test_case2
   start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
     op/ 4
'''
