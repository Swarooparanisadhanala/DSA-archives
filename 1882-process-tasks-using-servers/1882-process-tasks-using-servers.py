import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Heap for available servers: stores (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        
        # Heap for busy servers: stores (free_time, weight, index)
        unavailable = []
        
        ans = []
        current_time = 0
        
        for j, task_duration in enumerate(tasks):
            # Advance time to at least j, because task j arrives at second j
            current_time = max(current_time, j)
            
            # Free up servers whose tasks have finished by current_time
            while unavailable and unavailable[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            # If no servers are available, fast forward time to the next server release
            if not available:
                current_time = unavailable[0][0]
                while unavailable and unavailable[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(unavailable)
                    heapq.heappush(available, (weight, index))
            
            # Assign the task to the best available server
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the unavailable heap
            heapq.heappush(unavailable, (current_time + task_duration, weight, index))
            
        return ans