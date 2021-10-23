from collections import defaultdict, deque


def have_trace(st, end, graph):
    order = deque()
    used = set()
    order.append(st)
    while len(order) > 0:
        curr_v = order.popleft()
        if curr_v not in used:
            for v in graph[curr_v]:
                order.append(v)
            used.add(curr_v)
    return end in used


def main():
    s = input()
    graph = defaultdict(set)
    while len(s.split()) == 2:
        v1, v2 = s.split()
        graph[v1].add(v2)
        graph[v2].add(v1)
        s = input()
    st = s
    end = input()
    ans = have_trace(st, end, graph)

    print("YES" if ans else "NO")


if __name__ == "__main__":
    main()
