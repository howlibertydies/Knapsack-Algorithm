import random

def solve(products, maxWeight):
    currentWeight = 0
    currentValue = 0
    statementCount = 0
    productCount = []
    
    # Algorithm starts here

     
    # Algorithm ends here
    
    print("Final value $" + str(currentValue) + ", Final weight " + str(currentWeight) +\
          ", Statement count: " + str(statementCount))
    
    print("Product Counts: ",end="")
    for i in range(len(productCount)):
        print("Product #" + str(i) + ": " + str(productCount[i]) + ", ",end="" )
    print()



def byValue(element):
    return element[1]  

def byValueToWeight(element):
    return element[1] / element[2]  


# heuristic #1
def solveKnapsack1(products,maxWeight):
    print("===Heuristic 1===")

    products.sort(reverse=True, key=byValue)  
    
    displayProducts("Sorted for heuristic 1",products)
    
    solve(products,maxWeight)
    

# heuristic #2
def solveKnapsack2(products,maxWeight):
    print("===Heuristic 2===")

    products.sort(reverse=True, key=byValueToWeight)

    displayProducts("Sorted for heuristic 2",products)

    solve(products,maxWeight)

def displayProducts(prefix, products):
    print(prefix + ": ",end="")
    for product in products:
        num = product[0]
        value = product[1]
        weight = product[2]
        print("#" + str(num) + ", Value $" + str(value) + \
               ", Weight " + str(weight) + " | ", end="")
    print()
        

commands = str.split(input("Enter number of products and simulation number: "))
numProducts = int(commands[0])
simNumber = int(commands[1])

random.seed(simNumber) 

products = []

for i in range(numProducts):
    product = []
    product.append(i)
    product.append(random.randrange(1,5))
    product.append(random.randrange(1,5))
    product.append(0)
    products.append(product)

# display our initial set of products
displayProducts("Unsorted products    ",products)

# run both heuristic algorithms to see which is better
solveKnapsack1(products,10)
solveKnapsack2(products,10)
