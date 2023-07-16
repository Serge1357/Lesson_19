import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Чтение файла CSV с указанием разделителя
df = pd.read_csv('C:\\Users\\Пользователь\\Downloads\\cities.csv', sep='\t', encoding='cp1251')

# Создание списка для хранения значений
cities = []

# Цикл по строкам DataFrame
for index, row in df.iterrows():
    # Разделение значения в каждом столбце по символу ';'
    subset = []
    for column in row:
        # Разделение значения по символу ';'
        column_values = column.split(';')
        # Добавление отдельных значений в набор
        subset.extend(column_values)
    # Проверка, что в наборе три значения и третее значение можно преобразовать в int
    if len(subset) == 3 and subset[2].isdigit():
        # Преобразование третьего значения в int
        subset[2] = int(subset[2])
        # Добавление набора в список
        cities.append(subset)


print(cities)





g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight = edge[2])


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Ukraine distance map")
plt.show()

def minpath(graph, start, goal):
    path = nx.shortest_path(graph, start, goal, weight='weight')
    path_length = nx.shortest_path_length(graph, start, goal, weight='weight')
    return path, path_length

print(minpath(g, "Odesa", "Kyiv"))