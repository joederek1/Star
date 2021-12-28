def recipe_reader(file_name):
    recipe_file = open(file_name)
    ingradients = []

    for line in range(5):
        ingradients.append(recipe_file.readline())
    print(ingradients)
    recipe_file.close()
    #print(ingradients)

recipe_reader('recipe.txt')