def solution(board, moves):
    basket = []
    bomb = 0
    
    for i in moves:
        for j in board:
            if [j[i-1]] == basket[-1:] and j[i-1] != 0:
                basket.pop()
                bomb += 2
                j[i-1] = 0
                break
            elif [j[i-1]] != basket[-1:] and j[i-1] != 0:
                basket.append(j[i-1])
                j[i-1] = 0
                break
    
    return bomb

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))