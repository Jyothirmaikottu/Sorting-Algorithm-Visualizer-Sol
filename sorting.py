from time import sleep
import visualizer as vs

test = False


class Array:

    full_array = None

    def plot(self):
        if not test:
            vs.plot(Array.full_array)

    def set_all(self, values):
        for i in range(len(self.values)):
            self.values[i] = values[i]
        for i in range(len(self.values)):
            Array.full_array[self.lower_index + i] = values[i]
            self.plot()

    def __init__(self, values, lower_index=0):
        self.lower_index = lower_index
        self.values = list(values)

        if Array.full_array == None:
            Array.full_array = list(values)
            self.plot()

    def swap(self, index1, index2):
        self.values[index2], self.values[index1] = self.values[index1], self.values[index2]
        Array.full_array[self.lower_index + index2], Array.full_array[self.lower_index +
                                                                      index1] = Array.full_array[self.lower_index + index1], Array.full_array[self.lower_index + index2]
        self.plot()

    def set(self, index, num):
        self.values[index] = num
        Array.full_array[self.lower_index + index] = num
        self.plot()

    def get_len(self):
        return len(self.values)
              
def cycle_sort(nums): 
  k = 0
  r = nums.get_len()
    #new
  for cycleStart in range(0,  r- 1): 
    item = nums.values[cycleStart] 
      
    
    pos = cycleStart 
    for i in range(cycleStart + 1, r): 
      if nums.values[i] < item: 
        pos += 1
      
    if pos == cycleStart: 
      continue
      

    while item == nums.values[pos]: 
      pos += 1
    nums.values[pos], item = item, nums.values[pos] 
    k += 1
      
    while pos != cycleStart: 
   
      pos = cycleStart 
      for i in range(cycleStart + 1, r): 
        if nums.values[i] < item: 
          pos += 1
     
      while item == nums.values[pos]: 
        pos += 1
      nums.values[pos], item = item, nums.values[pos] 
      k += 1
    
  return k

def shell_sort(nums): 
  #new
    n = nums.get_len()
    gap = n//2
  
    while gap > 0: 
  
        for i in range(gap,n): 
  
            temp = nums.values[i] 

            j = i 
            while  j >= gap and nums.values[j-gap] >temp: 
                nums.values[j] = nums.values[j-gap] 
                j -= gap 
  
      
            nums.values[j] = temp 
        gap //= 2

def max(arr,n): 
  
   
    max = arr.values[0] 
  
    
    for i in range(1, n): 
        if arr.values[i] > max: 
            max = arr.values[i] 
    return max

def min(arr,n): 
  
   
    min = arr.values[0] 
  
    
    for i in range(1, n): 
        if arr.values[i] < min: 
            min = arr.values[i] 
    return min

def pigeonhole_sort(nums): 
#new
   
    n = nums.get_len()

    my_min = min(nums,n) 
    my_max = max(nums,n)
    size = my_max - my_min + 1
  
    
    holes = [0] * size  
  
    for j in range(n): 
        x = nums.values[j]
        type(x) is int
        holes[x - my_min] += 1

    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            nums.values[i] = count + my_min 
            i += 1

            
def getNextGap(gap): 
  

    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return int(gap) 
 
def comb_sort(nums): 
    n = nums.get_len()
  
    
    gap = n 
   
    swapped = True
  
    while gap !=1 or swapped == 1: 
  
        gap = getNextGap(gap) 
  
        swapped = False
        
        k = int(n-gap)
        for i in range(0, k): 
            if nums.values[i] > nums.values[i + gap]: 
                nums.values[i], nums.values[i + gap]=nums.values[i + gap], nums.values[i] 
                swapped = True


