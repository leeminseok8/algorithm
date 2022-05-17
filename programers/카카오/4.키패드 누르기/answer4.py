def solution(numbers, hand):
    answer = ''
    n_line = {(3*(x-1) + y) : (x,y) for x in (1,2,3,4) for y in (1,2,3)}
    left = 10
    right = 12
    
    for i in numbers:
        if (i == 1 or i == 4 or i == 7):
            answer += 'L'
            left = i
        elif (i == 3 or i == 6 or i == 9):
            answer += 'R'
            right = i
            
        elif hand == 'left' and (i == 2 or i == 5 or i == 8):
            if abs(n_line[left][0]-n_line[i][0])+abs(n_line[left][1]-n_line[i][1]) <= abs(n_line[right][0]-n_line[i][0])+abs(n_line[right][1]-n_line[i][1]):
                answer += 'L'
                left = i
            else:
                answer += 'R'
                right = i
        
        elif hand == 'left' and (i == 0):
            if abs(n_line[left][0]-n_line[11][0])+abs(n_line[left][1]-n_line[11][1]) <= abs(n_line[right][0]-n_line[11][0])+abs(n_line[right][1]-n_line[11][1]):
                answer += 'L'
                left = 11
            else:
                answer += 'R'
                right = 11
        
        elif hand == 'right' and (i == 2 or i == 5 or i == 8):
            if abs(n_line[right][0]-n_line[i][0])+abs(n_line[right][1]-n_line[i][1]) <= abs(n_line[left][0]-n_line[i][0])+abs(n_line[left][1]-n_line[i][1]):
                answer += 'R'
                right = i
            else:
                answer += 'L'
                left = i

        elif hand == 'right' and (i == 0):
            if abs(n_line[right][0]-n_line[11][0])+abs(n_line[right][1]-n_line[11][1]) <= abs(n_line[left][0]-n_line[11][0])+abs(n_line[left][1]-n_line[11][1]):
                answer += 'R'
                right = 11
            else:
                answer += 'L'
                left = 11
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))