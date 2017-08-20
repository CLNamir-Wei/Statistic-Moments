# comments
class Statistics:
    def __init__(self,data):
        self.data=data
        self.n=len(self.data)
    
    def sumup(self,nums):
        add=0
        for x in nums:
            add+=x
        return add
    
    def count_data(self,target):
        count=0
        for x in self.data:
            if x==target:
                count+=1
        return count
    
    def find_max(self):
        tem=self.data[0]
        maxv=0
        for x in self.data:
            if x > tem:
                maxv=x
            else:
                maxv=tem
            tem=maxv
        return maxv
    
    def find_min(self):
        tem=self.data[0]
        minv=0
        for x in self.data:
            if x < tem:
                minv=x
            else:
                minv=tem
            tem=minv
        return minv
        
    def sam_distance(self,target,power):
        temp=[]
        for x in self.data:
            b=x-target
            temp.append(b**power)
        return (self.sumup(temp))
        
class basic_stat(Statistics):
    
    def print_data(self):
        print (self.data)
   
    def freqcy(self):
        vals=set(self.data)
        freq=[]
        for val in vals:
            freq.append(super().count_data(val))
        dist=dict(zip(vals,freq))
        return dist
    
    def mode(self):
        table=self.freqcy()
        max_=0
        temp=0
        for key in table:
            if table[key]>temp:
                max_=table[key]
            else:
                max_=temp
            temp=max_
        
        for key in table:
            if table[key]==max_:
                return(key)
                
    def data_range(self):
        a=self.find_max()
        b=self.find_min()
        return (a-b)
        
class moments(Statistics):
    
    def mean(self):
        m1=super().sumup(self.data)
        return (m1/self.n)
    
    def sam_var(self):
        m2=super().sam_distance(self.mean(),2)
        return m2/(self.n-1)
    
    def sam_skew(self):
        m2=super().sam_distance(self.mean(),2)
        m3=super().sam_distance(self.mean(),3)
        temp=(m3/self.n)/(m2/self.n)**1.5
        adjn=((self.n*(self.n-1))**0.5)/(self.n-2)
        result=temp*adjn
        return result
        
    def sam_kurt(self):
        m2=super().sam_distance(self.mean(),2)
        m4=super().sam_distance(self.mean(),4)
        result=(m4/self.n)/((m2/self.n)**2)
        return result
        

        



        
        
# dict.get(key, default=None)
nums1=[1,5,9,7,8]
nums2=[1,-8,5,-7,100,896,58,-78,888,1000,-999,-89523,200]
zz=basic_stat([1,1,2,2,2,3,3,5,6])
#zz.print_data()
#print(zz.sumup(nums1))
#print(zz.find_max())
#print(zz.find_min())
#print(zz.freqcy())
print(zz.mode())

cc=moments(nums1)
print(cc.mean())
print(cc.sam_var())
print(cc.sam_skew())
print(cc.sam_kurt())
#xx=Statistics([1,5,9,7,8])
