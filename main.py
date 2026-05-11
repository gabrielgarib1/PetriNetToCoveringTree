
"""Discrete Math 2 project. Coverability tree implementation.
Group: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki."""

import numpy as np
import cl_node

#Example Petri net with 4 places and 4 transitions
x0=np.array([1,0,0,0])
ain=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
aout=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])

# path="/home/arabe/Documents/UFSC/PetriNets/test.ndr"
# Ain, Aout,x0 = net_to_nparray.carregar_matrizes_tina(path)


"""This algorithm has a linear arquitecture, it doesnt consider ramifications in the three.
(linked list solution)"""
def PetriToCoveringTree(x0,Ain, Aout, visualize=False):  #implement visualization later
    x0=x0.astype(float) # convert initial marking vector to float to allow infinity representation
    tree=[]
    # define a token limit to avoid infinite loops
    maxcaptoken=10*np.max(x0) 
    """Raise execptions in case of invalid matrices, such as negative values, infinite values, NaN values, 
    or incompatible dimensions."""

    try:
        if np.any(x0 != np.floor(x0)) or np.any(Ain != np.floor(Ain)) or np.any(Aout != np.floor(Aout)):
            raise ValueError("Invalid Matrices: values must be integers.")
        
        if (x0<0).any() or (Ain<0).any() or (Aout<0).any():
            raise ValueError("Invalid Matrices: values cannot be negative.")
        
        if (x0== np.inf).any() or (Ain==np.inf).any() or (Aout==np.inf).any():
            raise ValueError("Invalid Matrices: values cannot be infinite.")

        if Ain.shape!=Aout.shape:
            raise ValueError("Input and Output Matrices must have the same size")
            
        if len(x0)!=Ain.shape[0]:
            raise ValueError("Initial marking Matrix must have the same number of lines as input/output matrices")
    except ValueError as e:
        return str(e)
   

    """Infinite values shouldn't stop the loop, because there are more reachable markigns to be explored,
    it should check for duplicate markigns and look for blocking nodes to stop the loop."""
    tree=[]
    nodes=[]
    n=cl_node.cl_linked_list_node(x0)
    
    while True:
        habilited_transitions=[] # list to store enabled transitions for the current node
        for i in range(Ain.shape[0]):           # iterate through Petri net transitions

            if np.all(x0>= Ain[i]): # check whether transition is enabled
                habilited_transitions.append(i) # if enabled, add transition to the list
        if len(habilited_transitions)==0:
            return tree # if no transitions are enabled, return the tree
            
        possible_node=n.marking-Ain[i]+Aout[i] # calculate the possible next marking after firing transition i
        if possible_node not in nodes: # check if the possible next marking is already in the tree 
            #check dominance
            
            if np.any( np.all(possible_node >= nodes, axis=1)& np.any(possible_node > nodes, axis=1) ):
                np.where(possible_node > nodes) # find the index of the dominated node
                
                pass #implement np.inf where dominance is detected


            n.add_link(i, possible_node) # if it is, add a link to the existing node
            nodes.append(possible_node) # add the new marking to the list of nodes
            '''move the line bellow to the end of the loop to add the path after all transitions have been 
            checked this way, we can avoid adding paths that lead to already existing nodes,
            which would create duplicates in the tree.'''
            tree.append(n.get_path()) #  this line                
                
                # x0=x0-Ain[i]+Aout[i]# update marking    


        # if tree.any()==np.inf: # checks whether tree has infinite marking, indicating an unbounded net
        #     print("The net is unbounded")
        #     return tree

        

        

a=PetriToCoveringTree(x0,ain,aout)
# print(a)
if isinstance(a, str):
    print(a)  # Print the error message if a string is returned 
else:
    
    for i in a:
        print(i, '\n\n', end='')


