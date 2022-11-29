#Name: Angst S Gregory
#Email: angst.gregory17@myhunter.cuny.edu
#Date: ------
#This program prints: ----

    ADDI $s1 , $zero , 100 #Initialize register $s4 with 500 for checking the condition when $s0 is equal to 500

    ADDI $s0 , $zero , 0 #Initialize register $s0 with0

LOOP: 

    ADDI $s0, $s0, 10 #Add 100 to register $s0

    BEQ $s0, $s1 , DONE  #Branch to label abc if not equal to 500
    
    J LOOP

DONE:

