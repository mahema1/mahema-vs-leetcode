''' initially: i am thinking of using a hash set- O(1)- insert and look up,
but to get the random ill require a list- random.choice(mylist)
i can remove from the list if this was the last element- pop(), but if it is a
middle element??? so instead of using a hashset, i will use a hashmap- which will
store the number and the index as well.
 then i can have it replaced by the last number(top number) in my list 
and then pop that last number- this will ensure that i have correct no.of elements in my list
to get the random element and after this i will update the index in my hashmap
'''
class RandomizedSet:

    def __init__(self):
        self.numMap={} #maps val- index in numlist[]
        self.numList=[]
        

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False

        self.numMap[val]= len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx= self.numMap[val] # get the index
        last= self.numList[-1] # get the last element 
        self.numList[idx]= last # replace that number- val with this last number copyyy
        self.numMap[last]=idx # update the change in index of the last number in the map

        self.numList.pop() # pop- here we are actually deleting the last number 
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()