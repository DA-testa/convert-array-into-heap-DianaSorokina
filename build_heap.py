# python3


def build_heap(data):
    n = len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    for i in range(n//2,-1,-1):
        swaps += sift_down(data,i,n)


    return swaps

def sift_down(data,i,n):
    swaps = []
    min = i
    
    l_child = 2*i+1
    if l_child < n and data[l_child] < data [min]:
        min = l_child
    
    r_child = 2*i+2
    if r_child < n and data[r_child]<data[min]:
        min = r_child
        
    if i != min:
        swaps.append((i,min))
        data[i], data[min] = data[min], data[i]
        swaps += sift_down(data, min,n)
      
    return swaps 


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file 
    
    
    n = input().strip()
    if n == 'I':
         n = int(input())
         data = list(map(int, input().split()))
         assert len(data) == n
         swaps = build_heap(data)
         print(len(swaps))
         for i, j in swaps:
             print(i, j)
     
    elif n =='F':
        file = input()
        with open("test/" + file, 'r') as f:
             n = int(f.readline().strip())
             data = list(map(int, f.readline().strip().split()))
             assert len(data) == n
             swaps = build_heap(data)
             print(len(swaps))
             for i, j in swaps:
                 print(i, j)
     


   
    # checks if lenght of data is the same as the said lenght
    # assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    # swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    # print(len(swaps))
    # for i, j in swaps:
        # print(i, j)


if __name__ == "__main__":
    main()
