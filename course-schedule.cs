class Node{
	public Node(int val){
		childNodes = new List<Node>();
		parentNodes = new List<Node>();
		value = val;
	}
	int value {get;set;}
	List<Node> childNodes {get;set;}
	List<Node> parentNodes{get;set;}

}

class Graph{
	public Graph(){
		nodes = new List<Node>();
	}
	List<Node> nodes{get;set;}
}

private Graph BuildGraph(int[,] prereqs){

	var myGraph = new Graph();
	foreach (var prereq in prereqs){
		var nodeValue = prereq[0];
		var prereqValue = prereq[1];

		var myNode = myGraph.getNode(nodeValue) ?? new Node(nodeValue);
		var myParentNode = myGraph.getNode(prereqValue) ?? new Node(nodeValue);
		myNode.parentNodes.add(myParentNode);
		myParentNode.childNodes.add(myNode);
		myGraph.add(myNode);

	}
}

private int GetTakeableClasses(Graph _graph){
	//1) get starting nodes (nodes with no parentNodes);
	//2) foreach starting node, traverse while keeping track of visited nodes
	
	Dictionary<Node, int> visitedNodes = new Dictionary<Node, int>();
	var startingNodes = _graph.nodes.where(x => x.parentNodes.Count() == 0);
	foreach(var startingNode in startingNodes){
		Traverse(startingNode, visitedNodes);
	}

	return visitedNodes.Count();

}

private void Traverse(Node _node, Dictionary<Node, int> visitedNodes){
	visitedNodes[_node.value] += 1;
	foreach(var childNode in _node.childNodes){
		List<Node> visitableNodes= new List<Node>();
		foreach(var parentNode in childNode.parentNodes){
			if(parentNode.value != _node.value && !visitedNodes.contains(parentNode.value)){
				break;
			}
			visitableNodes.add(childNode);
		}
		foreach(var visitableNode in visitableNodes){
			Traverse(visitableNode, visitedNodes);
		}
	}
}






