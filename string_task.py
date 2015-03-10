#118A
a = raw_input().lower()
a = list(a)

j = 0
while j != len(a):
	i = a[j]
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
		a.remove(i)
	else:
		j += 1

print '.{}'.format('.'.join(a))
