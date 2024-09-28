//hollow buterfly pattern:


n = int(input())

# top half
for i in range(1 , n + 1):
     middle_space = (4 * n) - (4 * i - 1)
     if i == 1:
         row = "*" + " " *( middle_space)+ "*"
         print(row)
    
     else:
         hollow_space = (2 * i) - 3 
         left_rat = "*" + " " * hollow_space + "*"
         right_rat = "*" + " " * hollow_space + "*"
         row = left_rat + " " * (middle_space )+ right_rat
         print(row)
         
         
#bottom half
for i in range(1 , n +1 ):
    middle_space = 4 * i - 3 
    hollow_space = 2 * (n - i ) - 1
    if i == n :
        row = "*" + " " * (middle_space ) + "*"
        print(row)
    else :
        left_rat = "*" + " " * hollow_space + "*"
        right_rat = "*" +" " * hollow_space + "*"
        row = left_rat + " " * (middle_space ) + right_rat
        print(row)
        











         
