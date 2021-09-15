filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
def newfilenames(filenames):
   
    postfix =''
    x = 0
   
    for item in filenames:
        if x <= (len(filenames)):
          
            postfix = postfix +item[x].replace(item[x], item.replace('.hpp','.h')) +' '
      
            x = x+1
    return postfix
 

print(newfilenames(filenames)) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]