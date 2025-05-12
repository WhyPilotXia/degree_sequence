import networkx as nx
import matplotlib.pyplot as plt


def is_graphical(sequence):
    while True:  # 一直重复步骤直到结束
        sequence = sorted(sequence, reverse=True)  # 从大到小排序
        if all(d == 0 for d in sequence):   # 全0：没有边的图
            return True
        if sequence[0] < 0 or sequence[0] >= len(sequence):   # 度小于0或者最大度大于剩余点数：不行
            return False
        d = sequence[0]   # 考虑当前最大度
        sequence = sequence[1:]  # 除最大度剩余d个度数-1（最大度连接这些点）
        for i in range(d):
            if sequence[i] <= 0:
                return False
            sequence[i] -= 1


def construct_graph(sequence):
    G = nx.Graph()  # 创建图示
    degrees = sorted([(i, d) for i, d in enumerate(sequence)], key=lambda x: -x[1])  # 将 sequence 转换为 (顶点索引, 度数) 的列表，并按度数降序排序
    edges = []

    while True:
        degrees.sort(key=lambda x: -x[1])  # 按度数降序排序
        if all(d[1] == 0 for d in degrees):  # 若所有度数归零，构造完成
            break
        _, d = degrees[0]   # 当前最大度
        for i in range(1, d + 1):
            degrees[i] = (degrees[i][0], degrees[i][1] - 1)   # 除最大度剩余d个度数-1
            edges.append((degrees[0][0], degrees[i][0]))   # 最大度连接这些点
        degrees[0] = (degrees[0][0], 0)  # 第一个点度数归零（下一轮排序自动靠后）

    G.add_edges_from(edges)
    return G


def main():
    input_str = input("请输入一个非负整数序列（用空格分隔）：")
    try:
        sequence = list(map(int, input_str.split(' ')))
        if any(d < 0 for d in sequence):
            print("否")
            return
        if not is_graphical(sequence.copy()):
            print("否")
        else:
            G = construct_graph(sequence.copy())
            nx.draw(G, with_labels=True, node_color='lightblue')
            plt.show()
    except ValueError:
        print("输入无效，请输入用空格分隔的非负整数。")


if __name__ == "__main__":
    main()