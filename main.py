
"""Discrete Math 2 project. Coverability tree implementation.
Group: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki."""

import numpy as np
from class_datastruc import*

#Example Petri net with 4 places and 4 transitions
x0=np.array([1,0,0,0])
ain=np.array([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]])
aout=np.array([[0,1,0,0],
               [0,0,1,0],
               [0,0,0,1],
               [1,0,0,0]])

# path="/home/arabe/Documents/UFSC/PetriNets/test.ndr"
# Ain, Aout,x0 = net_to_nparray.carregar_matrizes_tina(path)


"""This algorithm has a linear arquitecture, it doesnt consider ramifications in the three.
(linked list solution)"""
def PetriToCoveringTree(x0,Ain, Aout, visualize=False):  #implement visualization later
    x0=x0.astype(float) # convert initial marking vector to float to allow infinity representation
    tree=[]
    # define a token limit to avoid infinite loops
 
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
    nodes_global=[]
   
    stack_markings=stack() # stack to keep track of the nodes to be explored
    stack_markings.push(x0) # start with the initial marking


    while not stack_markings.is_empty():
        habilited_transitions=[] # list to store enabled transitions for the current node
        x=stack_markings.pop() # get the next marking to explore
        for i in range(Ain.shape[0]):           # iterate through Petri net transitions

            if np.all(x>= Ain[i]): # check whether transition is enabled
                habilited_transitions.append(i) # if enabled, add transition to the list
                
        for i in habilited_transitions: # iterate through enabled transitions

            possible_node=n.marking-Ain[i]+Aout[i] # calculate the possible next marking after firing transition i
            if possible_node not in nodes_global: # check if the possible next marking is already in the tree 
                #check dominance
                dominated_mask=np.all(possible_node >= nodes_global, axis=1)& np.any(possible_node > nodes_global, axis=1)
                if np.any( dominated_mask ):
                    dominated_ancestors=nodes_global[dominated_mask]#substituir pelos nós ancestrais da lista encadeada
                    places_to_omega=np.any(possible_node > dominated_ancestors, axis=0) # find which places of the possible_node are greater than the dominated ancestors
                    possible_node[places_to_omega]=np.inf # set those places to infinity in the possible_node marking
                n.add_ancestor(n.marking) # add the current marking as an ancestor of the new node
                nodes_global.append(possible_node) # add the new marking to the global list of nodes
                n.add_link(i, possible_node) # add a link to the new node with the transition that leads to it


                '''move the line bellow to the end of the loop to add the path after all transitions have been 
                checked this way, we can avoid adding paths that lead to already existing nodes,
                which would create duplicates in the tree.'''
                tree.append(n.get_triple()) #  this line                
                

        

        

a=PetriToCoveringTree(x0,ain,aout)
# print(a)
if isinstance(a, str):
    print(a)  # Print the error message if a string is returned 
else:
    
    for i in a:
        print(i, '\n\n', end='')


