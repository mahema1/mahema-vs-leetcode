from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        g= defaultdict(list)
        #Sort visits by timestamp so we know the real order of visits
        for (t, user, web) in sorted(zip(timestamp, username, website)):
            g[user].append(web) #Group each user's websites in visit order

        scores= defaultdict(int)

        #For each user, find all unique 3-sequences they visited
        for user, web in g.items():
            # use set to avoid counting duplicate patterns from the same user
            for pattern in set(combinations(web, 3)):
                scores[pattern]+=1 # Count how many users had this pattern


        max_pattern, max_cnt= "", 0
        #Find the pattern with the highest count (or lex smallest if tie)
        for pattern, cnt in scores.items():
            if cnt> max_cnt or (cnt== max_cnt and pattern< max_pattern): ########
                max_pattern = pattern
                max_cnt= cnt

                # but we also need to see if we have two patterns of same score- we need to return lexicographically --------- go to the ####
        return max_pattern