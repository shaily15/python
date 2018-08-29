def h(m,n):
    ans = 0
    while (m >= n):
      (ans,m) = (ans+1,m-n)
      print ("ans", ans)
      print ("m", m)
    return(ans)

if __name__ == '__main__':
    h(231,8)
