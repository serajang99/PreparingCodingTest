from collections import defaultdict

def dfs(start_node, graph, visited):
    st = [start_node]
    cnt = 0
    while st:
        node = st.pop()
        cnt = cnt + 1
        for nodes in graph[node]:
            # print("dfs nodes:", nodes)
            if visited[nodes] == False:
                visited[nodes] = True
                st.append(nodes)
        
    return cnt-1

def solution(n, results):
    answer = 0
    wins = [[] for _ in range(n+1)]
    loses = [[] for _ in range(n+1)]
    for win, lose in results:
        wins[win].append(lose)
        loses[lose].append(win)
        
    
    win_rank = defaultdict(int)
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        cnt = dfs(i, wins, visited)
        win_rank[i] = cnt
        
    # print(win_rank)
    
    lose_rank = defaultdict(int)
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        cnt = dfs(i, loses, visited)
        lose_rank[i] = cnt
    
    # print(lose_rank)
    for i in range(1, n+1):
        if win_rank[i] + lose_rank[i] == n-1:
            answer += 1

    return answer