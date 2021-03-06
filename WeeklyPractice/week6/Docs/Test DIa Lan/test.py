import random
import os

def solution(n, k, a):

      if (k >= 12):
            t = a[0]
            for i in a:
                  t = (t & i)
            if (t==0):
                  return True
            else:
                  return False
      else:
            flag = True
      for i in range(n - k + 1):
            if (flag == False):
                  break
            t = a[i]
            for j in range(k):
                  t = (t & a[i + j])
            if (t == 0):
                  flag = False
                  break
      if (flag == False):
            return True
      else:
            return False
      
def gen_array(n):
      ans = []
      for i in range(n):
            if random.random() < 0.0001:
                  ans.append(random.randrange(8191))
            else:
                  ans.append(random.choice([1,3,7,15,31,63,127,255,511,1023,2047,4095]))
      return ans

def print_test(index, n, k, array):
	dirname = 'TEST_DIALAN_' + str(index)
	os.mkdir(dirname)

	filepath = os.path.join(dirname, 'TEST_DIALAN_')
	with open(filepath + ".INP", "w") as f:
		f.write("{} {}\n".format(n, k))
		for x in array:
			f.write("{} ".format(x))

	with open(filepath + ".OUT", "w") as f:
		if solution(n, k, array):
			f.write("YES")
		else:
			f.write("NO")

i = 0
for n in range(1, 20000, 100):
	i += 1
	k = random.randint(1,max(2, min(100,n//256)))
	array = gen_array(n)
	print_test(i, n, k, array)
