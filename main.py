
"""Discrete Math 2 project. Coverability tree implementation.
Group: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki."""

import numpy as np
import net_to_nparray

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
   

    """The infinite logical in the code is inproperly implemented,
     it should check dominance between nodes """
    """Infinite values shouldn't stop the loop, because there are more reachable markigns to be explored,
    it should check for duplicate markigns and look for blocking nodes to stop the loop."""
    while True:
        x0past=x0
        for i in range(len(Ain)):           # iterate through Petri net places
            for j in range(len(Ain[0])):        # iterate through Petri net transitions

                """some error here that i didnt understand, probably."""
                if x0[j]>= Ain[i][j]: # check whether transition is enabled
                    if (x0-Ain[i]+Aout[i]).any()<0: # check if resulting marking is valid (cannot have negative tokens)
                        continue
                    edge=[x0.tolist()]# create an edge (x,t,x')
                    if x0[j]>maxcaptoken: # check if marking exceeded the defined limit
                        x0[j]=np.inf # if exceeded, set marking to infinity
                        edge.append('t'+str(int(i)))
                        edge.append(x0.tolist()) 
                        tree.append(edge)
                        return tree  
                    else:
                        x0=x0-Ain[i]+Aout[i]# update marking    
                    edge.append('t'+str(int(i)))
                    edge.append(x0.tolist())
                    if edge not in tree: # check whether edge was already added to the tree
                        tree.append(edge)
        # if tree.any()==np.inf: # checks whether tree has infinite marking, indicating an unbounded net
        #     print("The net is unbounded")
        #     return tree
        if np.array_equal(x0past, x0): # check whether marking did not change (no more enabled transitions)
            break
        

    return tree

a=PetriToCoveringTree(x0,ain,aout)
# print(a)
if isinstance(a, str):
    print(a)  # Print the error message if a string is returned 
else:
    
    for i in a:
        print(i, '\n\n', end='')


