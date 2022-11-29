#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

ADDI $sp, $sp, -11
ADDI $to, $zero, 73 #I 
SB $t0, 0($sp)
ADDI $to, $zero, 32 #Space  
SB $t0, 1($sp)
ADDI $to, $zero, 117 #u
SB $t0, 2($sp)
ADDI $to, $zero, 115 #s
SB $t0, 3($sp)
ADDI $to, $zero, 101 #e
SB $t0, 4($sp)
ADDI $to, $zero, 32 #Space  
SB $t0, 5($sp)
ADDI $to, $zero, 77 #M  
SB $t0, 6($sp)
ADDI $to, $zero, 73 #I  
SB $t0, 7($sp)
ADDI $to, $zero, 80 #P  
SB $t0, 8($sp)
ADDI $to, $zero, 83 #S 
SB $t0, 9($sp)
ADDI $to, $zero, 33 #! 

SB $t0, 10($sp)
ADDI $v0, $zero, 4 
ADDI $a0, $sp, 0 
syscall