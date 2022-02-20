from sankeyflow import Sankey
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5), dpi=144)

flows = [
    ['All', 'Preselection', 44908], 
    ['Preselection', 'Not VBF', 44181], 
    ['Not VBF', 'Merged', 22209], 
    ['Merged', 'SR', 17446]
]
nodes = [
    [['All', 48907]], 
    [['Preselection', 44908]], 
    [['Not VBF', 44181]],
    [['Merged', 22209]], 
    [['SR', 17446]]
]

s = Sankey(
    flows=flows,
    nodes=nodes,
)
s.draw()
plt.show()