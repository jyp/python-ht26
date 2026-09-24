# We represent the grid as a matrix.
# An empty cell is represented by a space character. (' ')
# Any other character represents an occupied cell.

def empty(height,width):
    result = []
    for i in range(height):
        row = [' '] * width
        result.append(row)
    return result

def display(m):
  for row in m:
      print("".join(row) + "|")

def count_occupation(c):
    if c == ' ':
        return 0
    else:
        return 1

def has_single_occupied_cell(m,i,j):
    # return True iff. the 2 by 2 group starting at position i,j in the grid has a single occupied cell.
    # i,j is the top-left corner.
    total = (count_occupation(m[i][j]) +
             count_occupation(m[i][j+1]) +
             count_occupation(m[i+1][j]) +
             count_occupation(m[i+1][j+1]))
    return total == 1

def rotate_group(m,i,j):
    # modify m to rotate the 2 by 2 group starting at position i,j in the grid
    save = m[i][j]
    m[i][j] = m[i+1][j]
    m[i+1][j] = m[i+1][j+1]
    m[i+1][j+1] = m[i][j+1]
    m[i][j+1] = save

height = 40
width = 120
m = empty(height,width)
m[10][10] = 'x'
m[10][11] = 'x'
m[12][10] = 'x'
m[12][11] = 'x'

def rotate_all(offset,m):
   i = offset
   while i < height-1:
       # take care of the row
       j = offset
       while j < width-1:
           # take care of the group
           if has_single_occupied_cell(m,i,j):
               rotate_group(m,i,j)
           j = j+2
       i = i+2

offset = 1
while True:
    offset = 1 - offset
    display(m)
    input()
    rotate_all(offset,m)
