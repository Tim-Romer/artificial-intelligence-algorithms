from Node import Node

def breadthfirstsearch(nodeList, start, goal):
	visited = []
	frontier = []
	frontier.append(find(nodeList, start))
	visited.append(find(nodeList, start))
	while len(frontier) != 0:
		current = frontier.pop(0)
		print(current.val)
		if current.val == goal:
			break
		for val in current.D.keys():
			if val not in visited:
				visited.append(find(nodeList, val))
				frontier.append(find(nodeList, val))
	return visited

def depthfirstsearch(nodeList, start, goal):
	node = find(nodeList, start)
	visited = []
	depthfirstsearchH(nodeList, visited, node, goal)
	for n in visited:
		print(n.val)

def depthfirstsearchH(nodeList, visited, node, goal):
	if node is None:
		return False
	visited.append(node)
	if node.val == goal:
		return True
	else:
		for nextnode in node.D.keys():
			newnode = find(nodeList, nextnode)
			#print(newnode.val)
			found = depthfirstsearchH(nodeList, visited, newnode, goal)
			if found: return True

def find(L, val):
	for node in L:
		if node.val == val:
			return node
	return None