from sankeyflow import Sankey
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10), dpi=144)
nodes = [
    [('Product', 20779), ('Sevice\nand other', 30949)],
    [('Total revenue', 51728)],
    [('Gross margin', 34768), ('Cost of revenue', 16960)],
    [('Operating income', 22247), ('Other income, net', 268), ('Research and\ndevelopment', 5758), ('Sales and marketing', 5379), ('General and\nadministrative', 1384)],
    [('Income before\nincome taxes', 22515)],
    [('Net income', 18765), ('Provision for\nincome taxes', 3750)]
]
flows = [
    ('Product', 'Total revenue', 20779, {'flow_color_mode': 'source'}),
    ('Sevice\nand other', 'Total revenue', 30949, {'flow_color_mode': 'source'}),
    ('Total revenue', 'Gross margin', 34768),
    ('Total revenue', 'Cost of revenue', 16960),
    ('Gross margin', 'Operating income', 22247),
    ('Gross margin', 'Research and\ndevelopment', 5758), 
    ('Gross margin', 'Sales and marketing', 5379), 
    ('Gross margin', 'General and\nadministrative', 1384),
    ('Operating income', 'Income before\nincome taxes', 22247),
    ('Other income, net', 'Income before\nincome taxes', 268, {'flow_color_mode': 'source'}),
    ('Income before\nincome taxes', 'Net income', 18765), 
    ('Income before\nincome taxes', 'Provision for\nincome taxes', 3750),
]

s = Sankey(
    flows=flows,
    nodes=nodes,
)
s.draw()
plt.show()