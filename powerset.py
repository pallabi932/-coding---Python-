def powerset(list,index=0,set=[]):
    if index==len(list):
        print(set)
        return
    powerset(list,index+1,set)
    powerset(list,index+1,set+[list[index]])
list=[2,4,5]
powerset(list)
