
import numpy as np



class cl_linked_list_node:
    def __init__(self, init_marking):
        self.marking=init_marking
        self.end = False
        self.path = []
    
    def add_link(self, t,m_next):
        self.path.append((self.marking, 't'+str(t), m_next))
        self.marking=m_next
    
    def get_path(self):
        return self.path
    
    def get_end(self):
        return self.end

    def set_end(self):
        self.end=True
