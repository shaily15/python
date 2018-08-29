def f(m):
    if m == 0:
      return(0)
    else:
      print ("ans", (m+f(m-1)))
      return(m+f(m-1))

if __name__ == '__main__':
    f(8)
