from aocd import get_data

inp = get_data(day=19, year=2018)

# Label | Line |    Instruction   |    V1                             |    V2                                  |    V3                                   |    V4
# -------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------
#       |   0  |    addi 1 16 1   |    r1 += 16; GOTO A               |    GOTO A                              |    r2 = 10551403 IF is_part2 ELSE 1003  |    r2 = 10551403 IF is_part2 ELSE 1003
# B:    |   1  |    seti 1  5 3   |    r3 = 1                         |    r3 = 1                              |    r3 = 1                               |    ;
# G:    |   2  |    seti 1  7 5   |    r5 = 1                         |    DO {                                |    DO {                                 |    FOR r3 FROM 1 TO r2:
# I:    |   3  |    mulr 3  5 4   |    r4 = r3 * r5                   |      ;                                 |      ;                                  |      ;
#       |   4  |    eqrr 4  2 4   |    r4 = r4 == r2                  |      ;                                 |      DO {                               |      ;
#       |   5  |    addr 4  1 1   |    r1 += r4; IF r4 THEN GOTO C    |      IF r3 * r5 == r2 THEN r0 += r3    |        IF r3 * r5 == r2 THEN r0 += r3   |      IF r2 MOD r3 == 0 THEN r0 += r3
#       |   6  |    addi 1  1 1   |    r1++; GOTO D                   |      ;                                 |        ;                                |      ;
# C:    |   7  |    addr 3  0 0   |    r0 += r3                       |      ;                                 |        ;                                |      ;
# D:    |   8  |    addi 5  1 5   |    r5++                           |      r5++                              |        r5++                             |      ;
#       |   9  |    gtrr 5  2 4   |    r4 = r5 > r2                   |      ;                                 |        ;                                |      ;
#       |  10  |    addr 1  4 1   |    r1 += r4; IF r4 THEN GOTO E    |      IF r5 <= r2 THEN GOTO I           |      } WHILE r5 <= r2                   |      ;
#       |  11  |    seti 2  1 1   |    r1 = 2; GOTO I                 |      ;                                 |      ;                                  |      ;
# E:    |  12  |    addi 3  1 3   |    r3++                           |      r3++                              |      r3++                               |      ;
#       |  13  |    gtrr 3  2 4   |    r4 = r3 > r2                   |      ;                                 |      ;                                  |      ;
#       |  14  |    addr 4  1 1   |    r1 += r4; IF r4 THEN GOTO F    |      ;                                 |      ;                                  |      ;
#       |  15  |    seti 1  3 1   |    r1 = 1; GOTO G                 |    } WHILE r3 <= r2                    |    } WHILE r3 <= r2                     |      ;
# F:    |  16  |    mulr 1  1 1   |    r1 *= r1; HALT                 |    HALT                                |    HALT                                 |    HALT
# A:    |  17  |    addi 2  2 2   |    r2 += 2                        |    r2 = 4*19*11                        |    ;                                    |    ;
#       |  18  |    mulr 2  2 2   |    r2 *= r2                       |    ;                                   |    ;                                    |    ;
#       |  19  |    mulr 1  2 2   |    r2 *= r1                       |    ;                                   |    ;                                    |    ;
#       |  20  |    muli 2 11 2   |    r2 *= 11                       |    ;                                   |    ;                                    |    ;
#       |  21  |    addi 4  7 4   |    r4 += 7                        |    r4 = 7*22+13                        |    ;                                    |    ;
#       |  22  |    mulr 4  1 4   |    r4 *= r1                       |    ;                                   |    ;                                    |    ;
#       |  23  |    addi 4 13 4   |    r4 += 13                       |    ;                                   |    ;                                    |    ;
#       |  24  |    addr 2  4 2   |    r2 += r4                       |    r2 += r4                            |    ;                                    |    ;
#       |  25  |    addr 1  0 1   |    r1 += r0; IF r0 THEN GOTO H    |    ;                                   |    ;                                    |    ;
#       |  26  |    seti 0  9 1   |    r1 = 0; GOTO B                 |    IF is_part2 THEN {                  |    ;                                    |    ;
# H:    |  27  |    setr 1  0 4   |    r4 = r1                        |      r4 = (27*28+29)*30*14*32          |    ;                                    |    ;
#       |  28  |    mulr 4  1 4   |    r4 *= r1                       |      ;                                 |    ;                                    |    ;
#       |  29  |    addr 1  4 4   |    r4 += r1                       |      ;                                 |    ;                                    |    ;
#       |  30  |    mulr 1  4 4   |    r4 *= r1                       |      ;                                 |    ;                                    |    ;
#       |  31  |    muli 4 14 4   |    r4 *= 14                       |      ;                                 |    ;                                    |    ;
#       |  32  |    mulr 4  1 4   |    r4 *= r1                       |      ;                                 |    ;                                    |    ;
#       |  33  |    addr 2  4 2   |    r2 *= r4                       |      r2 += r4                          |    ;                                    |    ;
#       |  34  |    seti 0  2 0   |    r0 = 0                         |    }                                   |    ;                                    |    ;
#       |  35  |    seti 0  0 1   |    r1 = 0; GOTO B                 |    GOTO B                              |    ;                                    |    ;

def sum_of_factors(x):
  return sum(factor for factor in range(1, x + 1) if x % factor == 0)

answer = sum_of_factors(1003)
print(answer)

answer = sum_of_factors(10551403)
print(answer)
