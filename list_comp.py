# List comprehension to get the anti-diagonal elements of a 2D list
b=[[3,4,5],[6,7,8],[9,10,11]]
print([b[i][len(b)-1-i] for i in range (len(b))])


# Output: [5, 7, 9]






    
   
