croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for w in croatia:
    word = word.replace(w, "#")

print(len(word))


"""
ljes=njak

ddz=z=

nljj

c=c=

dz=ak

"""