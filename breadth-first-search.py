from search import breadthfirstsearch, depthfirstsearch
from Node import Node

def main():
	re = open('nodelist.txt')
	count = int(re.readline().strip("\n"))
	nodeList = []
	for n in range(count):
		ele = re.readline().strip("\n")
		frontier = re.readline().strip("\n").split(' ')
		weights = re.readline().strip("\n").split(' ')
		node = Node(ele, dict(zip(frontier, weights)))
		nodeList.append(node)
	breadthfirstsearch(nodeList, 'S', 'G')
	print()
	depthfirstsearch(nodeList, 'S', 'G')
	
if __name__ == '__main__':
	main()

