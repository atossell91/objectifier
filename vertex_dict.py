class vertex_dict:
    def __init__(self):
        self.list = []
        self.next_index = 0
        self.sort_order = 0 # 0 is none, 1 is index, 2 is vertex
        
    def add_vertex(self, vertex):
        self.list.append((vertex, self.next_index))
        self.next_index = self.next_index + 1
        self.sort_order = 0
        
    def sort_by_vertex(self):
        self.list.sort(key=lambda elem: elem[0])
        self.sort_order = 2
        
    def sort_by_index(self):
        self.list.sort(key=lambda elem: elem[1])
        self.sort_order = 1

    def find_vertex(self, vertex):
        if self.sort_order != 2:
            self.sort_by_vertex()
            
        start_index = 0
        end_index = len(self.list)-1
        
        while(start_index <= end_index):
            search_index = int((start_index + end_index) / 2)
            
            if self.list[search_index][0] < vertex:
                start_index = search_index + 1
            elif self.list[search_index][0] > vertex:
                end_index = search_index - 1
            else:
                return self.list[search_index]
            
        return None
