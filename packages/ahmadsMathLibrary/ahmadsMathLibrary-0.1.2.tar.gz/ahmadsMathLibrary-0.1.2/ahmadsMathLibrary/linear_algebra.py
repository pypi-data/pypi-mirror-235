def mat_vec(matrix, vector):

    """Multiply a matrix with a vector."""


    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix column size should match vector size.")
    
    result = []
    for row in matrix:
        res = 0
        for j, value in enumerate(row):
            res += value * vector[j]
        result.append(res)
    
    return result


def dot(u, v):
  return sum(ui * vi for ui, vi in zip(u, v))

def norm(x, y=0, type='2'):
    #vector norms

    if type not in ['1', '2', 'inf']:
        return ValueError("invalid norm type, options are '1', '2', 'inf'. defaults to '2'")
    if y==0:
        y= [0] * len(x)
    if len(x) != len(y):
        return ValueError("Vector dimensions do not match")
    diff = [xi-yi for xi,yi in zip(x,y)]
    if type=='1':
        return sum([abs(si) for si in diff])
    if type=='2':
        #print("invlaid norm type, giving the default 2 norm")
        return sum([si**2 for si in diff])
    if type =='inf':
        return max([abs(si) for si in diff])
    

    

