class DSU:
    def __init__(self):
        parent = []


    def dsu(v):
        for (i := 0 ; i < v ; i++){
            p[i] = i 
            R[0] = 1 
        }
    
    func find(i):
        _find(i)

    func _find(i int , items []int) {
        if p[i] == i {
            return i  
        } else {
            return p[i] = find(p[i])
        }

        #return i if p[i] == i else (p[i] = find(p[i]))

    }

    func unite(x ,y int)  {
        p1 = fin(x) 
        p2 = find(y) 
        if R[p1] > R[p2] {p[p2] = p1}
        elif R[p1] < R[p2] {p[p1] = p2}
        else {}
    }


cmp (a , b):
    a[2] < b[2]

def kruskal(edge_list , nubmerOfVertex):
    #sort(el.begin() , el.end() , cmp)
    edge_list(sort(lambda x: cmp)) 
    total_weight = 0 
    for el in edge_list:
        x = edge_list[0] 
        y = edge_list[1]
        w = edge_list[2]
        if dsu.find(x) != dsu.find(y):
            unite(x , y)
            total_weight += w 
            count += 1 
            if count == v - 1 :
                break 
    return total_weight 

#вообще бля хуй его не болватр щещен амы щещен амы 
#наху вообще лекциядаа отырмырн 
#котакта не понял  
