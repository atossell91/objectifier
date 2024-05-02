class vector_dict:
    def __init__(self):
        self.list = []
        self.next_index = 0
        self.sort_order = 0 # 0 is none, 1 is index, 2 is vector
        
    def add_vector(self, vector):
        self.list.append((vector, self.next_index))
        index = self.next_index
        self.next_index = self.next_index + 1
        self.sort_order = 0
        return index
        
    def sort_by_vector(self):
        self.list.sort(key=lambda elem: elem[0])
        self.sort_order = 2
        
    def sort_by_index(self):
        self.list.sort(key=lambda elem: elem[1])
        self.sort_order = 1

    def find_index(self, vector):
        if self.sort_order != 2:
            self.sort_by_vector()
            
        start_index = 0
        end_index = len(self.list)-1
        
        while(start_index <= end_index):
            search_index = int((start_index + end_index) / 2)
            
            if self.list[search_index][0] < vector:
                start_index = search_index + 1
            elif self.list[search_index][0] > vector:
                end_index = search_index - 1
            else:
                return self.list[search_index][1]
            
        return None
    
    def add_or_retreive(self, vector):
        index = self.find_index(vector)
        if index is None:
            return self.add_vector(vector)
        else:
            return index
