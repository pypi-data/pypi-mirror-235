class IterativeSolver:
  def __init__(self, A, b, x0, tol, maxiter):
    self.A = A.astype(float)
    self.b = b.astype(float)
    self.x0 = x0.astype(float)
    self.tol = tol
    self.maxiter = maxiter
    if self.b.shape != self.x0.shape or self.A.shape[1] != self.b.shape[0]:
       return  ValueError("Dimension Mismatch")
       



  def conjugateGradient(self):
    A , b, x0 = self.A, self.b, self.x0
    tol, maxiter = self.tol, self.maxiter
    x = np.copy(x0)
    m = len(x0)
    w = np.dot(A,x0)
    r = np.subtract(b,w)
    for k in range(m):
        if k == 0:
          v = np.copy(r)
        else:
          v = r + np.dot(s, v)

        u = np.dot(A,v);
        t = np.dot(v,r)/np.dot(v,u)
        x = x+ t*v
        w = w + t*u
        r = b - np.dot(A,x)
        if np.linalg.norm(r)/np.linalg.norm(b) < tol:
          print("Converged Early in", k+1, "iterations!")
          break
        s = - np.dot(r,u)/np.dot(v,u)

    return x

#ITERATIVE SOLVERS FOR Ax=b, take in as inputs A, b, x0, maxiter/tol and solves the system of equations.

#TODO - 1) clean up the functions, make code more readable, add comments.
#       2) Vectorize/Matrix forms of the solvers, refer to notes.

#conjugate gradient method
  def jacobi(self):
    A , b, x0 = self.A, self.b, self.x0
    tol, maxiter = self.tol, self.maxiter

    n = len(x0)
    itr = 0
    x = np.copy(x0)
    while True:
        x = np.copy(x0)
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += A[i][j] * x0[j]
            x[i] = (b[i]-sigma) / A[i][i]

        itr += 1
        norman = np.linalg.norm(np.subtract(x ,x0), np.inf)

        if norman < tol or itr>=maxiter:
          if norman<tol:
            print("Solution converged")
          if itr>=maxiter:
            print("Maximum iterations reached")

          break
        x0=np.copy(x)
    return x




#jacobi's method


  #gauss-seidel method
  def gs(self):
      A , b, x0 = self.A, self.b, self.x0
      tol, maxiter = self.tol, self.maxiter
      n = len(x0)
      itr = 0
      x = np.copy(x0)
      while itr < maxiter:
          x_prev = np.copy(x)
          for i in range(n):
              sigma = b[i]
              for j in range(i):
                  sigma -= A[i,j] * x[j]
              for j in range(i+1, n):
                  sigma -= A[i,j] * x_prev[j]
              x[i] = sigma / A[i,i]
          itr += 1
      return x



# Testing the functions
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]]).astype(float)

b = np.array([15, 10, 10, 10]).astype(float)

# Initial guess
x0 = np.array([0, 0, 0, 0]).astype(float)

test = IterativeSolver(A, b, x0, 1e-10, 100)
test.jacobi()
test.conjugateGradient()
test.gs()
#x_cg = conjugateGradient(A, b, x0, 1e-4)
#x_jacobi = jacobi(A, b, x0, 1e-10, 25)
#x_gs = gs(A, b, x0, 25)

#print("Solution from CG:", x_cg)
#print("Solution from Jacobi:", x_jacobi)
#print("Solution from Gauss-Seidel:", x_gs)
