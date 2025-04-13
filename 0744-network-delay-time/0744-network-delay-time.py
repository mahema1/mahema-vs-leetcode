class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g= defaultdict(list)
        for u,v, time in times:
            g[u].append((v,time))
        mintime={}
        min_heap=[(0,k)] # distance from source to node, node

        while (min_heap):
            time_k_to_i, i= heapq.heappop(min_heap)
            if i in mintime:
                continue
            
            mintime[i]= time_k_to_i
            for nei, nei_time in g[i]:
                heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
        if len(mintime)==n:
            return max(mintime.values())
        else:
            return -1
        