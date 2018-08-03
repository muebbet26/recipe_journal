print('Developer: Tugba Akan')
print('\n')      
print('Recipe Journal: A journal keeping your recipes in categories by the ingredients,')
print('letting you enter a new recipe,')
print('listing the recipes of the desired category')

#The recipes are taken from the website https://www.jamieoliver.com/

#Version 1 : The categories are: Beef, Chicken, Vegetables
print('\n')
print('if you would like to add a new recipe, put the text document into the folder that the code runs')
print('and run the code. It will load all the text documents including the new one.')
print('You can run the jupyter notebook')
print('or the py file from the command line')

#Python 3
#the subjects used in the code are : 
#importing text document and text mining
#object oriented programming
#Exception handling

#create a class for categories
class Category(object):
    def __init__(self, ID, name, keywords, ignorewords):
        self.ID = ID
        self.name = name
        self.keywords = keywords
        self.ignorewords = ignorewords

#keywords are the one that help us to find what is the main ingredient
#ignore words are the ones that misdirect us from the main ingredient. e.g. chicken stock
cate1 = Category( ID = 1, name='Beef', keywords=[' lamb ', ' lamb\n', 'steak', 'beef'], ignorewords=['stock'])
cate2 = Category( ID = 2, name='Chicken', keywords= ['chicken'], ignorewords=['stock'])
cate3 = Category( ID = 3, name='Vegetables', keywords= ['parsnip', 'beetroot', 'broccoli', 'cauliflower', 'courgette', 
                                                        'cucumber', 'lettuce', 'spinach', 'runner beans'], ignorewords=['stock'])
categories = [cate1, cate2, cate3 ]

#create a class for recipes
class Recipe(object):
    def __init__(self,name, ingredients, categories):
        self.name = name
        self.ingredients = ingredients
        self.category = []
        self.setCategory(categories)
        
    #method to set the category of the recipe
    def setCategory(self, categories):
        #loop for all categories
        for cate in categories:
            #loop for all ingredients
            for ingr in self.ingredients:
                #loop for all the words to be ignored
                for kw0 in cate.ignorewords:
                    if kw0 not in ingr: 
                        #loop for all keywords
                        if any(kw in ingr for kw in cate.keywords):
                            self.category.append(cate.name)
                            break

#enter a new recipe as a txt document
#we assume max 20 recipes will be given
recipes = []
for i in range(1,20):
    try:
        with open('recipe' + str(i) + '.txt', 'r') as f:
            #read all the document
            new_recipe = f.readlines()
            ing_index = 0
            #take the below line of 'Ingredients' for ingredient list
            #find the index and assign it to ing_index
            for i, e in enumerate(new_recipe):
                if e == 'Ingredients\n':
                    ing_index = i
                    break
            rec = Recipe(name=new_recipe[0], ingredients = new_recipe[ing_index::], categories = categories)
            recipes.append(rec)
    except IOError:
        # This will only check for an IOError exception and then execute this print statement
        print( "Error: Could not find file or read data" )
    else:
        print( "Content written successfully" )

#print the categories
#for item in categories:
#    print(item.name)

#print the name and the categories of the recipes
#for item in recipes:
#    print(item.name)
#    print(item.category)

#list the recipes in the desired category
print('Type the number of the category you wish to be listed')
for item in categories:
    print( str(item.ID) + ' for ' + item.name)
inp_cate_ID = input('')
for item in categories:
    if item.ID == int(inp_cate_ID):
        print(item.name)
        for item2 in recipes:
            for item3 in item2.category:
                if item3 == item.name:
                    print(item2.name)
                    break

                    