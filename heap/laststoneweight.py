import heapq

def lastStoneWeight(stones):
    heap = []
    
    # Create max heap using negative values
    for i in stones:
        heapq.heappush(heap, -i)
    
    # Process until one or no stone left
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        
        if a != b:
            heapq.heappush(heap, -(a - b))
    
    # Return result
    if len(heap) > 0:
        return -heap[0]
    else:
        return 0


# 🔹 Taking input from user
stones = list(map(int, input("Enter stones separated by space: ").split()))

# 🔹 Function call
result = lastStoneWeight(stones)

# 🔹 Output
print("Last Stone Weight:", result)