from collections import defaultdict

def solution(tickets): # 0322~0412
    
    book = defaultdict(list)
    for (start, end) in tickets:
        book[start].append(end)
    
    for b in book:
        book[b].sort(reverse=True)
        
    path = []
    st = ['ICN']
    while st:
        top = st[-1]
        
        if not book[top]:
            path.append(st.pop())
        else:
            st.append(book[top].pop())
    
    return path[::-1]