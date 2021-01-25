
from collections import deque
from itertools import permutations
from collections import defaultdict
import copy

"""
 마을에 전염병이 퍼지고 있습니다. 저희는 도로를 봉쇄해서 전염병이 퍼지는 것을 막으려고 합니다.
처음 전염병이 시작된 마을을 start_village라고 합니다. 모든 마을의 수를 num_of_village라고 합니다.
각 마을은 번호를 통하여 구별합니다. num_of_village가 3이면 마을 1, 2, 3이 존재합니다.

 도로는 마을이 서로 연결되어있음을 의미하며 1일마다 도로가 연결된 마을로 퍼집니다.
도로는 [ [1, 2], [1,3], [2,4] ] 같이 표현하며 1번 마을과 2번 마을에 도로가 있다는 의미입니다.
1번에서 2번으로 2번에서 1번으로 자유롭게 갈 수 있습니다. 하루에 하나의 도로를 봉쇄할 수 있을 때
가장 마을이 적게 감염되게 하는 방법을 찾아 가장 감염이 적게 되었을 때의 감염된 마을 숫자를 반환하세요.

 start_village는 이미 감염된 상태에서 0일로 시작합니다. 즉 0일날 도로 하나를 봉쇄하고
1일이 된 후 start_village와 연결된 다른 마을들이 전부 감염됩니다. 다시 도로 하나를 봉쇄한 후
2일이 되고 감염된 마을들과 연결된 모든 마을들이 전부 감염됩니다.
입력으로 어떤 마을에서도 갈 수 없는 고립된 마을은 주어지지 않습니다.

Ex) num_of_village = 3, start_village = 1, roads = [ [1, 2], [2, 3] ]
반환값 : 1
1번 마을만 감염되고 끝났습니다.

Ex) num_of_village = 4, start_village = 1, roads = [ [1, 2], [1, 3], [2, 4] ]
반환값 : 2
1번마을과 2번마을이 감염되거나, 1번마을과 3번마을이 감염되고 끝나므로 2입니다.

Ex) num_of_village = 6, start_village = 1, roads = [ [1, 2], [1, 3], [2, 5], [2, 6], [3, 4], [4, 5] ]
반환값 : 2
1번 마을과 3번마을만 감염된 상태로 막을 수 있으므로 2입니다.
"""

relations = [[1,2],[1,3],[1,6],[2,5],[3,4],[4,5],[5,8],[6,7]]
num_of_vertex = 8
start_vertex = 1

min_infected_vertex = num_of_vertex
relation_map = defaultdict(list)

#초기 그래프 매핑
for relation in relations:
    a, b = relation[0], relation[1]
    relation_map[a].append(b)
    relation_map[b].append(a)

#순서 생성
orders = permutations(relations)

#준비 끝
def cut_edge(order, relation_map, nums, start):

    zombies = [False for i in range(nums+1)]
    zombies[start] = True
    que = deque([start])

    while que and order:
        a, b = order.popleft()
        relation_map[a].remove(b)
        relation_map[b].remove(a)

        vertex = que.popleft()
        nears = relation_map[vertex]
        for near in nears:
            if zombies[near]: continue
            que.append(near)
            zombies[near] = True

    return sum(1 for zombie in zombies if zombie == True )
    
for order in orders:
    if order[0][0] != start_vertex: continue
    order = deque(order)
    relation_map_copy = copy.deepcopy(relation_map)
    min_infected_vertex = min(min_infected_vertex, cut_edge(order, relation_map_copy, num_of_vertex, start_vertex))

print(min_infected_vertex)