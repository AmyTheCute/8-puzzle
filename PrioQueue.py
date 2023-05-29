class PQueue:
    def __init__(self) -> None:
        self.array = [0]
    
    def sink(self, node):
        k = node
        c = k*2
        
        while(c < len(self.array)):
            if(c+1 < len(self.array) and self.array[c+1] > self.array[c]):
                c+=1
            if(self.array[c] > self.array[k]):
                self.array[c], self.array[k] = self.array[k],  self.array[c]
                k = c
                c = k*2
            else:
                break
    
    def swim(self, node):
        child = int(node/2)
        current = node
        
        while(child >= 1):
            if(self.array[current] > self.array[child]):
                self.array[child], self.array[current] = self.array[current],  self.array[child]
                current = child
                child = int(current/2)
            else:
                break
            
    def __repr__(self):
        return(str(self.array))
    
    def pop(self):
        temp = self.array[1]
        self.array[1] = self.array[len(self.array) - 1]
        del self.array[len(self.array) - 1]
        self.sink(1)
        return temp
    
    def push(self, value):
        self.array.append(value)
        self.swim(len(self.array) - 1)