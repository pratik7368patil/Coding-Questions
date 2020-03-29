strings = ['ab', 'xay','zyx','abc', 'ab']
que = ['xyz', 'ab', 'abc']
res = []
count = 0

for i in que:
   count = strings.count(i)
   res.append(count)
print(res)
