import copy
import math
import random
import networkx as nx


def turn_node(s):
        i, j = s.split("_")
        return [int(i), int(j)]

class Coloring:
    def __init__(self, n, population=20, count=100, depth=10**5):
        self.tabu = []
        self.n = n
        self.G = nx.Graph()
        self.nodes = [f'{i}_{j}' for i in range(self.n) for j in range(self.n)]
        edges = []
        self.G.add_nodes_from(self.nodes)
        for i in range(self.n):
            for j in range(self.n):
                for t in range(min(i, j) + 1, self.n):
                    if t > j:
                        edges.append((f'{i}_{j}', f'{i}_{t}'))
                    if t > i:
                        edges.append((f'{i}_{j}', f'{t}_{j}'))
        self.G.add_edges_from(edges)
        self.colors = [[set(range(n)) for _ in range(n)] for __ in range(n)]
        self.P = []
        self.population = population
        self.count = count
        self.depth = depth

    def solve(self, ls):
        """

        :param ls: latin square with each cell is a set of possible solution of the cell
        :return: Filled latin square
        """
        colors = copy.deepcopy(ls)
        self.reduce_LSC_choices(colors)
        coloring = self.MMCOL(self.count)
        return self.coloring_to_sol(coloring)

    def reduce_LSC_choices(self, choice):
        self.colors = choice
        for i in range(self.n):
            for j in range(self.n):
                if len(self.colors[i][j]) == 1:
                    self.G.remove_node(f'{i}_{j}')

    def init_color(self):
        p = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                p[random.choice(list(self.colors[i][j]))].append(f"{i}_{j}")
        return p

    def conflict(self, p):
        conf = 0
        for i in range(self.n):
            for e in range(len(p[i])):
                for f in range(e + 1, len(p[i])):
                    x, y = turn_node(p[i][e])
                    u, v = turn_node(p[i][f])
                    if x == u or v == y:
                        conf += 1
        return conf

    def coloring_to_sol(self, c):
        sol = [[0 for _ in range(self.n)] for __ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                y, x = turn_node(c[i][j])
                sol[y][x] = i
        return sol

    def MMCOL(self, counter):
        new_color = self.init_color()
        self.population_initialization()
        best_color = copy.deepcopy(new_color)
        best_conf = self.conflict(best_color)
        while best_conf > 0 and counter > 0:
            counter -= 1
            p_1, p_2 = self.selection()
            o_MMCOL = self.MAGX(p_1, p_2)
            o_MMCOL = self.ITS(o_MMCOL, counter)
            new_conf = self.conflict(o_MMCOL)
            if new_conf < best_conf:
                best_color = o_MMCOL
                best_conf = new_conf
                if best_conf == 0:
                    return best_color
            self.population_updating(o_MMCOL)
        return best_color

    def MAGX(self, p1, p2):
        g = 0
        t1 = copy.deepcopy(p1)
        t2 = copy.deepcopy(p2)
        o_MAGX = [[] for _ in range(self.n)]
        nodes = copy.deepcopy(self.nodes)
        while g < self.n:
            max_t = [0, 0, 0]
            for i in range(self.n):
                if len(o_MAGX[i]) == 0:
                    if ((self.n - len(o_MAGX[i])) >= len(t1[i]) >= len(t2[i])) and len(t1[i]) > max_t[0]:
                        max_t = [len(t1[i]), i, 1]
                    elif ((self.n - len(o_MAGX[i])) >= len(t2[i]) >= len(t1[i])) and len(t2[i]) > max_t[0]:
                        max_t = [len(t2[i]), i, 2]
            if max_t[0] != 0:
                max_p = t1 if max_t[2] == 1 else t2
                min_p = t1 if max_t[2] != 1 else t2
                o_MAGX[max_t[1]] = max_p[max_t[1]]
                for i in max_p[max_t[1]]:
                    nodes.remove(i)
                    for j in range(self.n):
                        if i in min_p[j]:
                            min_p[j].remove(i)
                            break
                max_p[max_t[1]] = []
            g += 1
        for i in range(self.n):
            if len(o_MAGX[i]) == 0:
                o_MAGX[i] = list(set(t1[i]) & set(t2[i]))
                for j in o_MAGX[i]:
                    nodes.remove(j)
        for i in nodes:
            x, y = turn_node(i)
            n = random.choice(list(self.colors[x][y]))
            # print("GGGGGGG",o[n])
            o_MAGX[n].append(str(i))
            # print(o[n])
        # print("!!!!!!!!",o)
        return o_MAGX

    def ITS(self, o, count):
        best_o = copy.deepcopy(o)
        best_conf = self.conflict(o)
        i = 0
        o_ITS = o
        while i < count:
            i += 1
            o_ITS = self.TS(o_ITS)
            conf = self.conflict(o_ITS)

            if best_conf > conf:
                print("Best :", best_conf, " Conflict after TS: ", conf)
                best_o = copy.deepcopy(o_ITS)
                best_conf = conf
            if conf > 0:
                o_ITS, conf = self.perturbation_procedure(o_ITS)
                if best_conf > conf:
                    print("Best :", best_conf, " Conflict after Per: ", conf)
                    best_o = copy.deepcopy(o_ITS)
                    best_conf = conf
            else:
                return best_o
        return best_o

    def TS(self, c):#https://www.researchgate.net/publication/2674877_Tabu_Search_for_Graph_Coloring_T-Colorings_and_Set_T-Colorings
        self.tabu = []
        time = 0
        best_choice = c
        for _ in range(self.depth):
            conf_number = self.conflict(c)
            if conf_number ==0:
                break
            color = copy.deepcopy(c)
            best_neighbor, best_conf, old_option = self.best_neighbor(c)
            c = self.change_coloring(color,best_neighbor,old_option)
            tabu_time = int(0.6 * conf_number) + random.randint(0, 10) + time
            self.tabu.append([tabu_time, old_option[0], old_option[1]])
            time += 1
            self.tabu = list(filter(lambda x: x[0] != time, self.tabu))
        return c

    def best_neighbor(self, c):
        conflicts = self.find_conflicts(c)
        best_conf = self.n**2
        best_neighbor = ["", 0] #best node and it's best color
        old_option = ["", 0]
        for conf in conflicts:
            remove_one_conflict = copy.deepcopy(c)
            old_node_color = 0
            for i in range(len(c)):
                if conf in remove_one_conflict[i]:
                    remove_one_conflict[i].remove(conf)
                    old_node_color = i
                    break
            remove_one_conflict_number = self.conflict(remove_one_conflict)
            i, j = turn_node(conf)
            colors_options = self.colors[i][j]
            for c_o in colors_options:
                conf_count = remove_one_conflict_number
                if c_o != old_node_color:
                    for f in range(len(remove_one_conflict[c_o])):
                        u, v = turn_node(remove_one_conflict[c_o][f])
                        if i == u or j == v:
                            conf_count += 1
                    if best_conf > conf_count and not(self.is_tabu(conf, c_o)):
                        best_conf = conf_count
                        best_neighbor = [conf, c_o]
                        old_option = [conf, old_node_color]
        return best_neighbor, best_conf, old_option

    def is_tabu(self, node, color):
        for tab in self.tabu:
            if node == tab[1] and color == tab[2]:
                return True
        return False

    def find_conflicts(self, c):
        conflicts = []
        for i in range(self.n):
            for e in range(len(c[i])):
                for f in range(e + 1, len(c[i])):
                    x, y = turn_node(c[i][e])
                    u, v = turn_node(c[i][f])
                    if x == u or v == y:
                        if c[i][e] not in conflicts:
                            conflicts.append(c[i][e])
                        if c[i][f] not in conflicts:
                            conflicts.append(c[i][f])
        return conflicts

    def perturbation_procedure(self, c):
        conflicts = self.find_conflicts(c)
        k = len(conflicts)//2
        half_conflicts = random.sample(conflicts, k)
        half_colored = []
        removed_half_conf = copy.deepcopy(c)
        for conf in half_conflicts:
            for i in range(len(removed_half_conf)):
                if conf in removed_half_conf[i]:
                    removed_half_conf[i].remove(conf)
                    half_colored.append([conf, i])
        half_c = self.TS(removed_half_conf)
        for h_c in half_colored:
            half_c[h_c[1]].append(h_c[0])
        return half_c, self.conflict(half_c)

    def score(self, c):
        conf = self.conflict(c)
        dist_pp = self.dist_population(c)
        dist = min(dist_pp)
        return conf + math.pow(math.e, 0.08 * self.n**2 / dist)

    def population_updating(self, o):
        add = True
        for p2 in self.P:
            if self.dist_coloring(p2, o) == 0:
                add = False
                break
        if add:
            self.P.append(o)
        else:
            return
        worst = [0,[]]
        sec_worst = [0,[]]
        for p in self.P:
            s = self.score(p)
            if s > worst[0]:
                worst = [s, p]
            elif s > sec_worst[0]:
                sec_worst = [s, p]
        if o == worst[1]:
            y = random.random()
            if y < 0.8:
                r = worst
            else:
                r = sec_worst
            self.P.remove(r[1])
        else:
            self.P.remove(worst[1])

    def selection(self):
        sample = list(range(len(self.P)))
        i, j = random.sample(sample, 2)
        return self.P[i], self.P[j]

    def population_initialization(self):
        c = 0
        while c < self.population:
            p = self.init_color()
            add = True
            for p2 in self.P:
                if self.dist_coloring(p2, p) == 0:
                    add = False
                    break
            if add:
                self.P.append(p)
                c += 1

    def change_coloring(self, c, best_neighbor,old_coloring):
        c[old_coloring[1]].remove(old_coloring[0])
        c[best_neighbor[1]].append(old_coloring[0])
        return c

    def dist_population(self, c):
        distance = []
        for p in self.P:
            if p != c:
                distance.append(self.dist_coloring(p,c))
        return distance

    def dist_coloring(self,c1,c2):
        dist = 0
        for i in range(len(c1)):
            for n in c1[i]:
                if n not in c2[i]:
                    dist += 1
        return dist


