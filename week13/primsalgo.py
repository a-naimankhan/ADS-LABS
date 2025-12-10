#pseudocode 
#func minInx(inMST []bool , D []int) {
    #min_val = INT_max 
    #min_ixd = -1  
    #for (i := 0 ; i < len(inMST) ; i++) {
    #if d[i] < min_val && !inMST[i] {
        #min_idx = -1 
        #

#} 
#}

#func Prim([][]int G , v int) {
    #inMST := []bool{}
    #D := []int{}

    #D[0] = 0 or anoluge of d = [0] * (n+1) as I guess 
    #for (int i  = 0 ; i < v-1 ; i++ {
        #next = minINd(inMST , D) 
        #inMST[next] = True 
        #total_weight += D[next] 
        #for( j = 0 ; j < V ; j++) {
            #if G[next][j] > 0 and G[next][j] < D[j] and !inMST[j]  {
            #D[j] = G[next][j]
            # 
        
#}
        #}
 
#}

#}#