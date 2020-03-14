#bubble sort
def bubble(L):
                for i in range(len(L)-1):
                                for j in range(len(L)-1-i):
                                                if L[j]>L[j+1]:
                                                                L[j],L[j+1]=L[j+1],L[j]

                print(L)


L=[12,34,11,10,45,100]
bubble(L)
