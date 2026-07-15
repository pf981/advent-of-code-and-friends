LOAD val=40 dest_reg=2
LOAD val=57 dest_reg=3
LOAD val=23 dest_reg=4
LOAD val=13 dest_reg=5
LOAD val=9 dest_reg=6
LOAD val=2 dest_reg=7
LOAD val=16 dest_reg=15
label0:
ADD src_reg1=1 src_reg2=2 dest_reg=1
INC reg=3
ADD src_reg1=3 src_reg2=0 dest_reg=0
SUB src_reg1=0 src_reg2=4 dest_reg=0
MOD src_reg1=0 src_reg2=15 dest_reg=0
JMPIFNONZERO reg=0 label=5
label1:
ADD src_reg1=1 src_reg2=3 dest_reg=1
COPY src_reg=1 dest_reg=12
MUL src_reg1=12 src_reg2=12 dest_reg=12
ADD src_reg1=3 src_reg2=12 dest_reg=3
ADD src_reg1=3 src_reg2=4 dest_reg=3
JMPIFNONZERO reg=3 label=9
label2:
COPY src_reg=3 dest_reg=7
MOD src_reg1=7 src_reg2=15 dest_reg=7
JMPIFZERO reg=7 label=4
label3:
COPY src_reg=3 dest_reg=8
MUL src_reg1=8 src_reg2=8 dest_reg=8
ADD src_reg1=8 src_reg2=4 dest_reg=9
MOD src_reg1=9 src_reg2=15 dest_reg=10
SUB src_reg1=0 src_reg2=10 dest_reg=0
JMPIFNONZERO reg=0 label=20
label4:
COPY src_reg=7 dest_reg=11
MUL src_reg1=11 src_reg2=11 dest_reg=11
ADD src_reg1=11 src_reg2=4 dest_reg=3
ADD src_reg1=3 src_reg2=2 dest_reg=3
JMPIFNONZERO reg=11 label=8
label5:
ADD src_reg1=0 src_reg2=15 dest_reg=0
SUB src_reg1=0 src_reg2=2 dest_reg=0
JMPIFNONZERO reg=2 label=1
label6:
MOD src_reg1=2 src_reg2=0 dest_reg=2
JMPIFNONZERO reg=4 label=19
label7:
SUB src_reg1=6 src_reg2=0 dest_reg=6
SUB src_reg1=4 src_reg2=2 dest_reg=4
JMPIFZERO reg=6 label=6
JMP label=9
label8:
INC reg=4
DEC reg=15
JMPIFNONZERO reg=15 label=7
label9:
ADD src_reg1=0 src_reg2=4 dest_reg=0
SUB src_reg1=0 src_reg2=3 dest_reg=0
JMPIFZERO reg=0 label=15
label10:
COPY src_reg=1 dest_reg=15
MUL src_reg1=15 src_reg2=1 dest_reg=15
ADD src_reg1=15 src_reg2=2 dest_reg=15
SUB src_reg1=10 src_reg2=2 dest_reg=2
ADD src_reg1=15 src_reg2=2 dest_reg=2
MOD src_reg1=15 src_reg2=4 dest_reg=15
JMPIFNONZERO reg=15 label=18
label11:
COPY src_reg=3 dest_reg=5
MUL src_reg1=5 src_reg2=3 dest_reg=5
ADD src_reg1=5 src_reg2=2 dest_reg=5
MOD src_reg1=5 src_reg2=4 dest_reg=5
JMPIFNONZERO reg=5 label=3
label12:
ADD src_reg1=0 src_reg2=15 dest_reg=0
SUB src_reg1=0 src_reg2=5 dest_reg=0
JMP label=21
label13:
ADD src_reg1=2 src_reg2=4 dest_reg=2
SUB src_reg1=3 src_reg2=15 dest_reg=3
JMPIFNONZERO reg=2 label=10
label14:
ADD src_reg1=4 src_reg2=5 dest_reg=4
SUB src_reg1=1 src_reg2=2 dest_reg=1
JMPIFNONZERO reg=4 label=11
label15:
ADD src_reg1=2 src_reg2=3 dest_reg=2
SUB src_reg1=15 src_reg2=4 dest_reg=15
JMPIFNONZERO reg=2 label=12
label16:
ADD src_reg1=4 src_reg2=0 dest_reg=4
SUB src_reg1=5 src_reg2=15 dest_reg=5
JMPIFZERO reg=4 label=13
label17:
ADD src_reg1=15 src_reg2=1 dest_reg=15
SUB src_reg1=3 src_reg2=5 dest_reg=3
JMPIFNONZERO reg=15 label=14
label18:
ADD src_reg1=5 src_reg2=2 dest_reg=5
SUB src_reg1=0 src_reg2=3 dest_reg=0
JMPIFNONZERO reg=5 label=16
label19:
ADD src_reg1=3 src_reg2=4 dest_reg=3
SUB src_reg1=2 src_reg2=0 dest_reg=2
JMPIFNONZERO reg=3 label=17
label20:
SUB src_reg1=0 src_reg2=5 dest_reg=13
MOD src_reg1=13 src_reg2=2 dest_reg=14
ADD src_reg1=0 src_reg2=14 dest_reg=0
JMPIFZERO reg=0 label=0
label21:
SUB src_reg1=15 src_reg2=3 dest_reg=13
MOD src_reg1=13 src_reg2=4 dest_reg=14
ADD src_reg1=2 src_reg2=14 dest_reg=2
ADD src_reg1=0 src_reg2=14 dest_reg=0
SUB src_reg1=1 src_reg2=2 dest_reg=13
MOD src_reg1=13 src_reg2=6 dest_reg=14
JMPIFNONZERO reg=13 label=2