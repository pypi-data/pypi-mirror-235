import numpy as np

##EIGENTHINGS
def spectral_radius(A):
  #incorrect logic, its the largest absolute value, so would have to check all of them. any way to get smallest one? negate and power method?

    x0=np.ones(A.shape[0]).astype(float)
    lam, u = get_dominant_eigenpair(A, x0, 1e-10, 1000)
    return lam

def get_dominant_eigenpair(A, x0, tol, maxiter):
    return power_method(A, x0, tol, maxiter)

def get_second_argest_eigenpair(A, x0, tol, maxiter):
    lam1, v1 = get_dominant_eigenpair(A, x0, tol, maxiter)
    B = A - (lam1 / np.dot(v1, v1.T)) * np.outer(v1, v1)
    return power_method(B, x0, tol, maxiter)

def get_all_eigenpairs(A, x0, tol, maxiter):
    pairs = []
    B = np.copy(A)
    #number of columns of A is the nu,ber of maximum eigen vectors, what happens if not all of them exist?
    for i in range(A.shape[1]):
      [lam, v] = get_dominant_eigenpair(B, x0, tol, maxiter)
      pairs.append((lam, v))
      B = B - (lam / np.dot(v, v.T)) * np.outer(v, v)
    return pairs

def power_method(A, x0, tol, maxiter):
    n = len(x0)
    x = np.copy(x0)

    for k in range(maxiter):
      u = x/np.linalg.norm(x)
      x = np.dot(A, u)
      lambda1 = np.dot(u, x)
      if np.linalg.norm(np.subtract(x, lambda1*u)) < tol:
        break
    return lambda1, u
