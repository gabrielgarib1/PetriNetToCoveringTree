
""""Trabalho Discretas 2. Implementação árvore de cobertura
Grupo: Gabriel Garib Gomes, Marcus Novais Ferrari, Fabrício Sassaki """

import numpy as np

np.printoptions(nanstr="NAN", infstr="INF")

x0=np.array([1,1,0,1])
ain=np.array([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
aout=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])



def PetriToCoveringTree(m0,Ain, Aout):
    x0=m0.astype(float) #converte o vetor de marcação inicial para float, para permitir a representação de infinito
    m0=m0.astype(float)
    tree=[]
    #define um limite para o número de tokens, para evitar loops infinitos
    maxcaptoken=10*np.max(m0) 
    print("Limite de tokens definido como:", maxcaptoken)
    if x0.any()<0 or Ain.any()<0 or Aout.any()<0 or x0.any()== np.inf or Ain.any()==np.inf or Aout.any()==np.inf or x0.any()== np.nan or Ain.any()==np.nan or Aout.any()==np.nan:
        print("Vetores inválidos, não podem conter valores negativos, infinitos ou NaN")
        return None
    if Ain.shape!=Aout.shape:
        print("Matriz de entrada e saída devem ter o mesmo número de linhas")
        return None
    if len(x0)!=Ain.shape[1]:
        print("Vetor de marcação inicial deve ter o mesmo número de colunas que as matrizes de entrada e saída")
        return None
   
    while True:
        m0past=m0
        for i in range(len(Ain)):           #percorre os lugares da rede de petri
            for j in range(len(Ain[0])):        #percorre as transições da rede de petri
                if m0[j]>= Ain[i][j]: #verifica se a transição é habilitada
                    if (m0-Ain[i]+Aout[i]).any()<0: #verifica se a marcação resultante da transição é válida (não pode ter tokens negativos)
                        continue
                    edge=[m0.tolist()]#cria uma aresta (x,t,x')
                    if m0[j]>maxcaptoken: #verifica se a marcação ultrapassou o limite definido
                        m0[j]=np.inf #se ultrapassou, define a marcação como infinito
                        edge.append('t'+str(int(i)))
                        edge.append(m0.tolist()) 
                        tree.append(edge)
                        return tree   
                        print("deu infinito aq")
                    else:
                        m0=m0-Ain[i]+Aout[i]#atualiza a marcação    
                    edge.append('t'+str(int(i)))
                    edge.append(m0.tolist())
                    if edge not in tree: #verifica se a aresta já foi adicionada à árvore
                        tree.append(edge)
        # if tree.any()==np.inf: #verifica se a árvore contém alguma marcação infinita, o que indica que a rede é ilimitada
        #     print("A rede é ilimitada")
        #     return tree
        if np.array_equal(m0past, m0): #verifica se a marcação não mudou, ou seja, se não há mais transições habilitadas
            break
        

    return tree

a=PetriToCoveringTree(x0,ain,aout)
for i in a:
    print(i, '\n\n', end='')