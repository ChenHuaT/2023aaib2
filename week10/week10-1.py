#week10-1 �禡�I�s�禡 Recursion ���j N���h
N = int(input('�п�JN:'))
# �H�e�O�� for�j��g, ���ѥΡu�禡�I�s�禡�v�Ӽg
def func(n):
  if n==1: return 1 # �פ����, ���u�ƾ��k�Ǫk�vN=1����
  return n * func(n-1)
ans = func(N)
print(ans)
