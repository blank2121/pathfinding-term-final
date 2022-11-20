# winston's a-star alg
---

- each node with have a value denoting its distance from the starting node
- when searching for the end node, the direction of search will be towards the end node
- when the end node is found, the node that touches/overlaps the end node will check its neighbors for the smallest distance and then add that to the path, repeat the process until the distance is 0
