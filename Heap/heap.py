class Heap:
  def __init__(self):
    self.heap = [0]
    
  def push(self, value):
    self.heap.append(value)
    i = len(self.heap) - 1
    
    # percolate up
    while i > 1 and self.heap[i] < self.heap[i // 2]:
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i = i // 2
      
  def pop(self):
    if len(self.heap) == 1:
      return None
    if len(self.heap) == 2:
      return self.heap.pop()
    
    root = self.heap[1]
    self.heap[1] = self.heap.pop()
    i = 1
    
    # percolate down
    self._percolate_down(i)
    return root
  
  def heapify(self, arr):
    self.heap = [0] + arr
    for i in range((len(self.heap) - 1) // 2, 0, -1):
      self._percolate_down(i)

  def _percolate_down(self, i):
    while 2 * i < len(self.heap):
      if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
        self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
        i = 2 * i + 1
      elif self.heap[i] > self.heap[2 * i]:
        self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
        i = 2 * i
      else:
        break
    
heap = Heap()
heap.push(5)
heap.push(3)
heap.push(4)
heap.push(2)
heap.push(1)
print(heap.heap)