func = input().split("-")

for i in range(len(func)):
    sum = 0
    for j in func[i].split("+"):
        sum += int(j)
    func[i] = sum
func[0] = int(func[0])

answer = func[0]
for a in range(1, len(func)):
    answer -= func[a]

print(answer)