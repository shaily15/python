def h(n):
    f = 0
    for i in range(1,n+1):
      if n%i == 0:
        f = f + 1
    ans = (f%2 == 1)
    print ("ans", ans)
    return ans


if __name__ == '__main__':
    h(16)
