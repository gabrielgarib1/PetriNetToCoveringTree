
"""Discrete Math 2 project. Coverability tree implementation.
Group: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki."""

import numpy as np
from class_datastruc import*

#Example Petri net with 4 places and 4 transitions
x0=np.array([1,0,0,0])


# ain = np.array([
#     [1, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1]
# ])

# aout = np.array([
#     [0, 0, 0, 1],
#     [1, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0]
# ])

ain= np.array([[1, 0, 0],
               [0, 1, 1],
               [0, 0, 1],
               [0, 0, 0]])

aout = np.array([[0, 1, 0],
                [1, 0, 0],
                [1, 0, 1],
                [0, 0, 1]])

def PetriToCoveringTree(x0,Ain, Aout):  #implement visualization later
    """Build a coverability tree for a Petri net.

    The algorithm explores reachable markings, records enabled transitions,
    and replaces growing components with infinity when a marking dominates
    one of its ancestors.
    """
    x0=x0.astype(float) # convert initial marking vector to float to allow infinity representation
    tree=[]
    # Input validation keeps the traversal logic focused on the Petri-net rules.
 


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
   


    tree=[]
    nodes_global=[x0.tolist()]
   
    # Explore depth-first so the tree can be built with a small explicit stack.
    stack_markings=stack() # stack to keep track of the nodes to be explored
    root_node=cl_linked_list_node(x0.tolist()) # create the root node of the tree with the initial marking
    stack_markings.push(root_node) # start with the initial marking


    while not stack_markings.is_empty():
        habilited_transitions=[] # list to store enabled transitions for the current node
        current_node = stack_markings.pop()
        x=np.array(current_node.marking) # get the next marking to explore
        for i in range(Ain.shape[1]):           # iterate through Petri net transitions

            if np.all(x>= Ain[:,i]): # check whether transition is enabled
                habilited_transitions.append(i) # if enabled, add transition to the list

        for i in habilited_transitions: # iterate through enabled transitions

            possible_node = x - Ain[:,i] + Aout[:,i] # calculate the possible next marking
            ancestors_array = np.array(current_node.ancestors)
            

            if len(ancestors_array) > 0: 
                # If the new marking grows beyond an ancestor, mark the growth as omega.
                dominated_mask = np.all(possible_node >= ancestors_array, axis=1) & np.any(possible_node > ancestors_array, axis=1)
                if np.any(dominated_mask):
                    dominated_ancestors = ancestors_array[dominated_mask]
                    places_to_omega = np.any(possible_node > dominated_ancestors, axis=0) 
                    possible_node[places_to_omega] = np.inf 
            
            possible_node_list = possible_node.tolist()


            edge = [current_node.marking, f't{i+1}', possible_node_list]
            if edge not in tree: 
                tree.append(edge)
                current_node.add_link(i, possible_node_list)


            if possible_node_list not in nodes_global: 
                nodes_global.append(possible_node_list) 
                
                child_node = cl_linked_list_node(possible_node_list) 
                child_node.ancestors = current_node.ancestors.copy() 
                child_node.add_ancestor(current_node.marking) 
                stack_markings.push(child_node)
    return tree

                           
                

        

        

a=PetriToCoveringTree(x0,ain,aout)

# if isinstance(a, str):
#     print(a) 
# else:
    
#     for i in a:
#         print(i, '\n\n', end='')


if isinstance(a, str):
    print(a) 
else:
    print("--- Arestas da Árvore de Cobertura ---")
    for edge in a:
        # Formata os floats para inteiros e o 'inf' para o símbolo ômega
        origem = [int(v) if v != np.inf else 'ω' for v in edge[0]]
        destino = [int(v) if v != np.inf else 'ω' for v in edge[2]]
        transicao = edge[1]
        
        print(f"Origem: {origem} --({transicao})--> Destino: {destino}")

