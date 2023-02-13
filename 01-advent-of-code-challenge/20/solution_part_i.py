from collections import deque

with open('sample.in', 'r') as file:
    data = file.read().splitlines()

data_content = deque([*map(lambda n: int(n), data)])
index_data_content = deque(range(0, length := len(data_content)))

for idx in range(length):
    position = index_data_content.index(idx)
    for deq in [data_content, index_data_content]:
        deq.rotate(position * -1)
        local_value = deq.popleft()
        if deq == data_content: current_value = local_value
        deq.rotate(current_value * -1)
        deq.appendleft(local_value)

zero = data_content.index(0)
hint1, hint2, hint3 = (
    data_content[(zero + 1000) % (len(data_content))],
    data_content[(zero + 2000) % (len(data_content))],
    data_content[(zero + 3000) % (len(data_content))]
)

print(str(sum([hint1, hint2, hint3])))

data_content = deque([*map(lambda n: int(n) * 811589153, data)])
index_data_content = deque(range(0, length := len(data_content)))

for _ in range(10):
    for idx in range(length):
        position = index_data_content.index(idx)
        for deq in [data_content, index_data_content]:
            deq.rotate(position * -1)
            local_value = deq.popleft()
            if deq == data_content: current_value = local_value
            deq.rotate(current_value * -1)
            deq.appendleft(local_value)

zero = data_content.index(0)
hint1, hint2, hint3 = (
    data_content[(zero + 1000) % (len(data_content))],
    data_content[(zero + 2000) % (len(data_content))],
    data_content[(zero + 3000) % (len(data_content))]
)