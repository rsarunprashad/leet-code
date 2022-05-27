#Quick sort, pivot (random number in seq), compare rest elements against pivot and create left , pivot and right sequence 
#do this till sequene length is gt 1


def quick_sort(sequece, order_type=None):
    
    if sequece is None or type(sequece) is not list or len(sequece) <= 1:
        return sequece
    
    pivot = sequece.pop()
    

    
    if order_type is None or order_type == 'ASC':
        
        less_than_pivot = []
        greater_than_pivot = []
    
        for item in sequece:
            if item > pivot:
                greater_than_pivot.append(item)
            else:
                less_than_pivot.append(item)

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

        

seq1=[9,8,7,1,2,8,3,-3,-5,0]
print (quick_sort(seq1,order_type='ASC'))