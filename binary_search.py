class BinarySearch:
    
    def search_index(self,seq, key):
        
        begin_index = 0
        end_index = len(seq) - 1
        
        while(begin_index <= end_index):
            
            print('begin at {}, end at {}'.format(begin_index,end_index))
            
            mid_point_index = begin_index + (end_index - begin_index) // 2
            
            mid_point_value = seq[mid_point_index]
            
            print('mid index {}, mid val {}'.format(mid_point_index,mid_point_value))
            
            if mid_point_value == key:
                return mid_point_index
            elif key < mid_point_value:
                end_index = mid_point_index -1
            else:
                begin_index = mid_point_index+1
                
        return None
    
seq_1 = [-5,-3,2,4,6,8,12]
key=-3

sn=BinarySearch()

print(str(sn.search_index(seq_1,key)))