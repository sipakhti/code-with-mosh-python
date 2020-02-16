
def bar_grapher(num_bars: int, graph_range: int, height: list, asdata=True, placeholder="X"):
    """Returns a nested list as a 2D bar graph for manipulation
       or prints it on the screen if asdata=False
       by default it returns a 2D list.
       Param placeholder is "X" by default and will use "X" as 
       the bar body, however it could be given any argument to be placed
       instead of "X"
    """
    if graph_range >= 10:
        placeholder += " "

    print("\n\n")
    graph_range += 1  # so that i can add the column height aboce the bars to help readability of large graphs
    bar_graph = [[" " for j in range(num_bars)] for i in range(graph_range)]

    for i in range(num_bars):
        error = True
        while error:
            error = False

            try:
                for j in range(height[i]):
                    bar_graph[graph_range - 1 - j][i] = placeholder
            except IndexError:
                error = True
                return f"!!!Bar height cannot exceed {graph_range}, Index[{i}] Value: {height[i]}!!!"
            bar_graph[-1].insert(i, height[i])

    if asdata:
        return bar_graph
    else:
        for row in bar_graph:
            print(*row)


num_bars = int(input("Enter the number or bars in the grapgh: "))
graph_range = int(input("Enter the range of the graph: "))

height = []
for x in range(num_bars):
    height.append(
        int(input(f"Enter height of the bar {x+1} (max {graph_range}) : ")))

bar_grapher(num_bars, graph_range, height, asdata=False)

ending = ""
while ending.lower() == "q":
    ending = (input("enter q to quit: "))
