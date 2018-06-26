from graphviz import Digraph

dot = Digraph(comment='IoT-Crawler',format='png')
#dot.engine='circo'


'''
node for metadata
'''
dot.node('Sensor','Sensor',style='filled',fillcolor='lightyellow')
dot.node('QuantityKind','QuantityKind',style='filled',fillcolor='lightyellow',shape='rectangle')
dot.node('unit','unit',style='filled',fillcolor='lightyellow',shape='rectangle')
#Geo
with dot.subgraph(name='cluster_0') as s:
	s.attr(style='filled')
	s.attr(color='lightyellow')
	s.node('point','point')
	s.attr(label='Geo(location)')
#dot.node('point','point',style='filled',fillcolor='lightyellow')

#Coverage
with dot.subgraph(name='cluster_1') as s:
	s.attr(style='filled')
	s.attr(color='lightyellow')
	s.node('coverage','coverage')
	s.attr(label='use geoSPARQL')
#dot.node('coverage','coverage(use geoSPARQL)',style='filled',fillcolor='lightyellow')


'''
Service node, link meta data to QoI
'''
dot.node('QoI','Quality of Information',style='filled',fillcolor='green')
dot.node('Security','Security',shape='rectangle',style='filled',fillcolor='green')
dot.node('Communication','Communication',shape='rectangle',style='filled',fillcolor='green')
dot.node('Timeliness','Timeliness',shape='rectangle',style='filled',fillcolor='green')
dot.node('Accuracy','Accuracy',shape='rectangle',style='filled',fillcolor='green')
dot.node('Cost','Cost',shape='rectangle',style='filled',fillcolor='green')
'''
Node for data, link meta data to data
'''
dot.node('Service','Service',style='filled',fillcolor='lightblue')
dot.node('Streamdata','Streamdata',style='filled',fillcolor='lightblue')
dot.node('StreamAnalysis','StreamAnalysis',style='filled',fillcolor='lightblue')
dot.node('time','time',style='filled',fillcolor='lightblue')

#link the nodes
dot.edge('Sensor','QuantityKind',label='hasQuantityKind')
dot.edge('Sensor','unit',label='hasUnit')
dot.edge('Sensor','point',label='hasPoint')
dot.edge('Sensor','coverage',label='hasCoverage')
dot.edge('Sensor','QoI',label='hasQoI')
dot.edge('QoI','Accuracy',label='hasAcuuracy')
dot.edge('QoI','Security',label='hasSecurity')
dot.edge('QoI','Communication',label='hasCommunication')
dot.edge('QoI','Timeliness',label='hasTimeliness')
dot.edge('QoI','Cost',label='hasCost')
dot.edge('Sensor','Service',label='hasService')
dot.edge('Service','Streamdata',label='hasStreamData')
dot.edge('Streamdata','StreamAnalysis',label='wasDerivedFrom')
dot.edge('StreamAnalysis','Streamdata',label='wasDerivedFrom')
dot.edge('Streamdata','time',label='hasTime')


dot.render(view=True)