def g(x):
    (q,d) = (1,0)
    while q <= x:
      (q,d) = (q*10,d+1)
      print ("q", q)
      print ("d", d)
    return(d)

if __name__ == '__main__':
    g(31415927)
