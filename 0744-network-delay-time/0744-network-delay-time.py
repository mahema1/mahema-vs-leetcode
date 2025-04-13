class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g= defaultdict(list)
        for u,v, time in times:
            g[u].append((v,time))
        mintime={}
        minheap=[(0,k)] # time, node

        while(minheap):
            time, i= heapq.heappop(minheap)
            if i in mintime:
                continue
            
            mintime[i]= time
            for nei, nei_time in g[i]:
                if nei not in mintime:
                    heapq.heappush(minheap, (time+nei_time, nei))
        if len(mintime)==n:
            return max(mintime.values())
        else:
            return -1

        