#bubble sort o[n2]

# compare i,i+1 over loop and swap, untill everything is sortef


def bubble_sort(sequence):
    
    sorted_seq = False
    
    while not sorted_seq :
        
        sorted_seq = True
        
        for i in range(0, len(sequence)-1):
            
            if sequence[i+1] < sequence[i]:
                
                sorted_seq = False
                
                sequence[i],sequence[i+1] = sequence[i+1],sequence[i]
                
    print(sequence)


bubble_sort([7,-3,4,8,2,-5,9])