class find_subset_sum:
    '''
    Class to implement method to find
    whether or not there exists any subset 
    of array  that sum up to targetSum
    '''
    def __init__(self):
        self.subset_count = 0  #to count the total possibilities
        self.values = []   #to store the valid values for subset
    #BACKTRACKING ALGORITHM
    def subset_sum(self,list_val,sum, st_idx,target):
        if target == sum:
            print("Subset => ",self.values)
            self.subset_count +=1

            if st_idx < len(list_val):
                self.subset_sum(list_val, sum - list_val[st_idx-1], st_idx, target)
        else:
            #generate nodes
            for i in range(st_idx,len(list_val)):
                self.values.append(list_val[i]) #store to find sum
                self.subset_sum(list_val, sum + list_val[i], i + 1, target)
                self.values.pop(-1) #remove as now longer valid

#Driving code
c1 = find_subset_sum()
c1.subset_sum([1,3,5,2,7] , 0,0,10)
print("Result: ",c1.subset_count)

c2 = find_subset_sum()
c2.subset_sum([1, 3, 7, 5, 9, 11] , 0,0,12)
print("Result: ",c2.subset_count)