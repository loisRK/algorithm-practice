sen = str(input())
croatia_transfer = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

cnt = 0
for c in croatia_transfer:
  sen = sen.replace(c,"_")

print(len(sen))