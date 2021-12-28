#name = input('What is your name?\n')
#print('Hi, %s.' % name + '\n')

def recipe_reader(file_name):  
  recipe_file = open(file_name, 'a')
  recipe_file.write('cherry\n')
  
  #ingradients = []
 #number = 0

  #for line in range(8):
    #ingradients.append(recipe_file.readline())
    #print(ingradients[number])

  recipe_file.close()
  #number = 0
  #for bits in range(14):
   # print(ingradients[number])
    #number +=1

  #recipe_file.close()
    
recipe_reader('recipe.txt')
  