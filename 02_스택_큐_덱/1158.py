n, k = map(int, input().split())  # 5 3
queue = [i for i in range(1, n + 1)]  # 큐에 삽입

result = []
count = 0  # 큐 인덱스

for i in range(n):
    count += k - 1  # 2, 4, 2, 4, 2
    if count >= len(queue):
        count = count % len(queue)  # 0 0 0
    result.append(str(queue.pop(count)))  # 3 1 5 2 4
print("<", ", ".join(result), ">", sep="")


"""
list = ['a', 'b', 'c', 'd']
print( ','.join(list) ) # a,b,c,d

"""
