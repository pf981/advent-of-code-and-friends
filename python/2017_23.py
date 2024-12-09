from aocd import get_data

inp = get_data(day=23, year=2017)

# Label |  Line  |  Instruction   |    V1                  |    V2                   |  V3
# -----------------------------------------------------------------------------------|----------------------------
#       |  0     |  set b 84      | b = 84                 | b = 84                  | b = 84                     
#       |  1     |  set c b       | c = b                  | c = 84                  | c = 84                     
#       |  2     |  jnz a 2       | IF a != 0 THEN GOTO A  | IF part2:               | IF part2:                  
#       |  3     |  jnz 1 5       | GOTO B                 |   ;                     |   ;                        
# A:    |  4     |  mul b 100     | b *= 100               |   b = 108400            |   b = 108400               
#       |  5     |  sub b -100000 | b += 100000            |   ;                     |   ;                        
#       |  6     |  set c b       | c = b                  |   ;                     |   ;                        
#       |  7     |  sub c -17000  | c += 17000             |   c = 125400            |   c = 125400               
# B:    |  8     |  set f 1       | f = 1                  | REPEAT:                 | DO:                        
#       |  9     |  set d 2       | d = 2                  |   f = 1; d = 2          |   no_factors = TRUE        
# E:    |  10    |  set e 2       | e = 2                  |   DO:                   |   FOR d FROM 2 TO b:       
#                                                                e = 2               |     ;                      
# D:    |  11    |  set g d       | g = d                  |     DO:                 |     FOR e FROM 2 TO b:     
#       |  12    |  mul g e       | g *= e                 |       ;                 |       ;                    
#       |  13    |  sub g b       | g -= b                 |       ;                 |       ;                    
#       |  14    |  jnz g 2       | IF g != 0 THEN GOTO C  |       IF d*e == b:      |       IF d*e == b:         
#       |  15    |  set f 0       | f = 0                  |         f = 0           |         no_factors = FALSE 
# C:    |  16    |  sub e -1      | e++                    |       e++               |       ;                    
#       |  17    |  set g e       | g = e                  |       ;                 |       ;                    
#       |  18    |  sub g b       | g -= b                 |       ;                 |       ;                    
#       |  19    |  jnz g -8      | IF g != 0 GOTO D       |     WHILE e != b        |     ;                      
#       |  20    |  sub d -1      | d++                    |     d++                 |     ;                      
#       |  21    |  set g d       | g = d                  |     ;                   |     ;                      
#       |  22    |  sub g b       | g -= b                 |     ;                   |     ;                      
#       |  23    |  jnz g -13     | IF g != 0 GOTO E       |   WHILE d != b          |   ;                        
#       |  24    |  jnz f 2       | IF f != 0 GOTO F       |   IF f == 0             |   IF NOT no_factors:       
#       |  25    |  sub h -1      | h++                    |     h++                 |     n_factors++            
# F:    |  26    |  set g b       | g = b                  |   ;                     |   ;                        
#       |  27    |  sub g c       | g -= c                 |   ;                     |   ;                        
#       |  28    |  jnz g 2       | IF g != 0 GOTO G       |   IF b == c:            |   ;                        
#       |  29    |  jnz 1 3       | HALT                   |     HALT                |   ;                        
# G:    |  30    |  sub b -17     | b += 17                |   b += 17               |   b += 17                  
#       |  31    |  jnz 1 -23     | GOTO B                 |                         | WHILE b != c               

# When a = 0, the main loop runs only once
# The outer range loop runs b-2 times (82 times)
# The inner range loop runs b-2 times (82 times) for each outer loop
# mul is executed once per inner range loop run
answer = 82 * 82
print(answer)

import math

def is_prime(x):
  return all(x % y != 0 for y in range(2, int(math.sqrt(x))))

answer = sum(not is_prime(b) for b in range(108400, 125400 + 1, 17))
print(answer)
