from sankeyflow import Sankey
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10), dpi=144)

flows = [
    ('Product', 'Total revenue', 20779),
    ('Sevice\nand other', 'Total revenue', 30949),
    ('Total revenue', 'Gross margin', 34768),
    ('Total revenue', 'Cost of revenue', 16960),
    ('Gross margin', 'Operating income', 22247),
    ('Operating income', 'Income before\nincome taxes', 22247, {'flow_color_mode': 'dest'}),
    ('Other income, net', 'Income before\nincome taxes', 268),
    ('Gross margin', 'Research and\ndevelopment', 5758), 
    ('Gross margin', 'Sales and marketing', 5379), 
    ('Gross margin', 'General and\nadministrative', 1384),
    ('Income before\nincome taxes', 'Net income', 18765), 
    ('Income before\nincome taxes', 'Provision for\nincome taxes', 3750),
]

s = Sankey(flows=flows, flow_color_mode='lesser')
s.draw()
plt.show()