
'''

Print nodes at k distance from root
Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.
            1
          /   \
        2      3
      /   \   /
    4     5  8 


    '''


def printNodeFunc(root,n,store = []):

	if not root:
		return

	if n==0:
		print(root.data)

	else:
		printNodeFunc(root.left,n-1)
		printNodeFunc(root.right,n-1)



#Ans : 4,5,8