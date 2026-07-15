bool does_finish(int reg0, int reg1) {
        
    int reg2=0,reg3=0,reg4=0,reg5=0,reg6=0,reg7=0,reg8=0,reg9=0,reg10=0,reg11=0,reg12=0,reg13=0,reg14=0,reg15=0;

    reg2 = 40;
    reg3 = 57;
    reg4 = 23;
    reg5 = 13;
    reg6 = 9;
    reg7 = 2;
    reg15 = 16;
    label0:
    reg1 = reg1 + reg2;
    reg3++;
    reg0 = reg3 + reg0;
    reg0 = reg0 - reg4;
    reg0 = reg15 ? reg0 % reg15 : 0;
    if (!reg0) goto label5;
    label1:
    reg1 = reg1 + reg3;
    reg1 = reg12;
    reg12 = reg12 * reg12;
    reg3 = reg3 + reg12;
    reg3 = reg3 + reg4;
    if (!reg3) goto label9;
    label2:
    reg3 = reg7;
    reg7 = reg15 ? reg7 % reg15 : 0;
    if (reg7) goto label4;
    label3:
    reg3 = reg8;
    reg8 = reg8 * reg8;
    reg9 = reg8 + reg4;
    reg10 = reg15 ? reg9 % reg15 : 0;
    reg0 = reg0 - reg10;
    if (!reg0) goto label20;
    label4:
    reg7 = reg11;
    reg11 = reg11 * reg11;
    reg3 = reg11 + reg4;
    reg3 = reg3 + reg2;
    if (!reg11) goto label8;
    label5:
    reg0 = reg0 + reg15;
    reg0 = reg0 - reg2;
    if (!reg2) goto label1;
    label6:
    reg2 = reg0 ? reg2 % reg0 : 0;
    if (!reg4) goto label19;
    label7:
    reg6 = reg6 - reg0;
    reg4 = reg4 - reg2;
    if (reg6) goto label6;
    goto label9;
    label8:
    reg4++;
    reg15--;
    if (!reg15) goto label7;
    label9:
    reg0 = reg0 + reg4;
    reg0 = reg0 - reg3;
    if (reg0) goto label15;
    label10:
    reg1 = reg15;
    reg15 = reg15 * reg1;
    reg15 = reg15 + reg2;
    reg2 = reg10 - reg2;
    reg2 = reg15 + reg2;
    reg15 = reg4 ? reg15 % reg4 : 0;
    if (!reg15) goto label18;
    label11:
    reg3 = reg5;
    reg5 = reg5 * reg3;
    reg5 = reg5 + reg2;
    reg5 = reg4 ? reg5 % reg4 : 0;
    if (!reg5) goto label3;
    label12:
    reg0 = reg0 + reg15;
    reg0 = reg0 - reg5;
    goto label21;
    label13:
    reg2 = reg2 + reg4;
    reg3 = reg3 - reg15;
    if (!reg2) goto label10;
    label14:
    reg4 = reg4 + reg5;
    reg1 = reg1 - reg2;
    if (!reg4) goto label11;
    label15:
    reg2 = reg2 + reg3;
    reg15 = reg15 - reg4;
    if (!reg2) goto label12;
    label16:
    reg4 = reg4 + reg0;
    reg5 = reg5 - reg15;
    if (reg4) goto label13;
    label17:
    reg15 = reg15 + reg1;
    reg3 = reg3 - reg5;
    if (!reg15) goto label14;
    label18:
    reg5 = reg5 + reg2;
    reg0 = reg0 - reg3;
    if (!reg5) goto label16;
    label19:
    reg3 = reg3 + reg4;
    reg2 = reg2 - reg0;
    if (!reg3) goto label17;
    label20:
    reg13 = reg0 - reg5;
    reg14 = reg2 ? reg13 % reg2 : 0;
    reg0 = reg0 + reg14;
    if (reg0) goto label0;
    label21:
    reg13 = reg15 - reg3;
    reg14 = reg4 ? reg13 % reg4 : 0;
    reg2 = reg2 + reg14;
    reg0 = reg0 + reg14;
    reg13 = reg1 - reg2;
    reg14 = reg6 ? reg13 % reg6 : 0;
    if (!reg13) goto label2;

    return 0;
}
int main() {
