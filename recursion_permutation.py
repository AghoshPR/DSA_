def perm(w, step=0):
    if len(w) == step:
        print("".join(w))
        return
    for i in range(step, len(w)):
        l = list(w)
        l[i], l[step] = l[step],l[i]
        perm(l,step = step + 1)
        
perm("abc")