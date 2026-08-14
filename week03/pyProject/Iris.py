

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
# https://archive.ics.uci.edu/dataset/53/iris
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
# print(iris.metadata) 
  
# variable information 
# print(iris.variables) 

# Total number of records
print("Total records:", len(X))

# Different flower available
print("Different flowers:")
# for flower in y:
#    print(flower["class"])
flowers = y["class"]
print(len(flowers))

# Names of all flowers
print("Flower names:")
for flower in flowers:
    print(flower)

