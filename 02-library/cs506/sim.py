def euclidean_dist(x, y):
    result = 0
    for i in range(len(x)):
    	result += abs(x[i] - y[i])**2
    result = result**(1/2)
    return result

def manhattan_dist(x, y):
    result = 0
    for i in range(len(x)):
    	result += abs(x[i] - y[i])
    return result

def jaccard_dist(x, y):
    result = 0
    if (x == []):
    	result = 0
    elif (y == []):
    	result = 0
    else:
    	result = 1 - ((len(set(x).intersection(set(y))))/len(set(x).union(set(y))))
    return result
def cosine_sim(x, y):
    result = 0
    if (x == []):
    	result = 0
    elif (y == []):
    	result = 0
    elif (euclidean_dist(x,y) == 0):
    	result = 1
    else:
    	for i in range(len(x)):
    		result += x[i]*y[i]
    	result = result / euclidean_dist(x,y)
    return result

# Feel free to add more
