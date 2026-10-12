

left_peg = list(reversed([1,2,3,4,5,6,7,8]))
middle_peg = []
right_peg = []

def move_disc(n,source,target):
    disc = source.pop()
    target.append(disc)
    print("L: ",left_peg)
    print("M: ",middle_peg)
    print("R: ",right_peg)
    print("============")

def move_tower(n, source, intermediate, target):
    if n == 0:
        pass
    else:
        move_tower(n-1, source, target, intermediate)
        move_disc(n,source,target)
        move_tower(n-1, intermediate, source, target)

move_tower(8, left_peg, middle_peg, right_peg)
