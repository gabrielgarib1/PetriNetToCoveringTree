
import numpy as np



class cl_linked_list_node:
    def __init__(self, init_marking):
        self.marking=init_marking
        self.x_t_xnew=[]
        self.ancestors=[]
    
    def add_link(self, t,m_next):
        self.x_t_xnew.append((self.marking, 't'+str(t), m_next))
        self.marking=m_next
    
    def get_triple(self):
        return self.x_t_xnew
    
    def add_ancestor(self, ancestor):
        self.ancestors.append(ancestor)
    def get_end(self):
        return self.end


class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self, item):
        self.stack.append(item)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    
    def get_last(self):
        return self.stack[-1] if not self.is_empty() else None
