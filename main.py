
"""Discrete Math 2 project. Coverability tree implementation.
Group: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki."""

import numpy as np

#Example Petri net with 4 places and 4 transitions
x0=np.array([1,1,0,1])
ain=np.array([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
aout=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])



def PetriToCoveringTree(m0,Ain, Aout):
    x0=m0.astype(float) # convert initial marking vector to float to allow infinity representation
    m0=m0.astype(float)
    tree=[]
    # define a token limit to avoid infinite loops
    maxcaptoken=10*np.max(m0) 
    if x0.any()<0 or Ain.any()<0 or Aout.any()<0 or x0.any()== np.inf or Ain.any()==np.inf or Aout.any()==np.inf or x0.any()== np.nan or Ain.any()==np.nan or Aout.any()==np.nan:
        print("Invalid vectors: values cannot be negative, infinite, or NaN")
        return None
    if Ain.shape!=Aout.shape:
        print("Input and output matrices must have the same number of rows")
        return None
    if len(x0)!=Ain.shape[1]:
        print("Initial marking vector must have the same number of columns as input/output matrices")
        return None
   
    while True:
        m0past=m0
        for i in range(len(Ain)):           # iterate through Petri net places
            for j in range(len(Ain[0])):        # iterate through Petri net transitions
                if m0[j]>= Ain[i][j]: # check whether transition is enabled
                    if (m0-Ain[i]+Aout[i]).any()<0: # check if resulting marking is valid (cannot have negative tokens)
                        continue
                    edge=[m0.tolist()]# create an edge (x,t,x')
                    if m0[j]>maxcaptoken: # check if marking exceeded the defined limit
                        m0[j]=np.inf # if exceeded, set marking to infinity
                        edge.append('t'+str(int(i)))
                        edge.append(m0.tolist()) 
                        tree.append(edge)
                        return tree  
                    else:
                        m0=m0-Ain[i]+Aout[i]# update marking    
                    edge.append('t'+str(int(i)))
                    edge.append(m0.tolist())
                    if edge not in tree: # check whether edge was already added to the tree
                        tree.append(edge)
        # if tree.any()==np.inf: # checks whether tree has infinite marking, indicating an unbounded net
        #     print("The net is unbounded")
        #     return tree
        if np.array_equal(m0past, m0): # check whether marking did not change (no more enabled transitions)
            break
        

    return tree

a=PetriToCoveringTree(x0,ain,aout)
for i in a:
    print(i, '\n\n', end='')