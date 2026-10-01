import time
height = 40
width = 120

cellsize = 10

from tkinter import *
root = Tk()
canvas = Canvas(root, bg="white", width=width * cellsize, height=height * cellsize)
canvas.pack()

# We represent the grid as a matrix.
# An empty cell is represented by None
# An occupied cell is represented by the Oval object in that cell.

def empty(height,width):
    result = []
    for i in range(height):
        row = [None] * width
        result.append(row)
    return result


def count_occupation(c):
    if c == None:
        return 0
    else:
        return 1

def grid_access(m,i,j):
    return m[i % height][j % width]

def grid_update(m,i,j,x):
    if x is not None:
        canvas.coords(x, j*cellsize, i*cellsize, (j+1)*cellsize, (i+1)*cellsize)
    m[i % height][j % width] = x

def has_single_occupied_cell(m,i,j):
    # return True iff. the 2 by 2 group starting at position i,j in the grid has a single occupied cell.
    # i,j is the top-left corner.
    total = (count_occupation(grid_access(m,i,j)) +
             count_occupation(grid_access(m,i,j+1)) +
             count_occupation(grid_access(m,i+1,j)) +
             count_occupation(grid_access(m,i+1,j+1)))
    return total == 1

def rotate_group(m,i,j):
    # modify m to rotate the 2 by 2 group starting at position i,j in the grid
    save = grid_access(m,i,j)
    grid_update(m,i,j, grid_access(m,i+1,j))
    grid_update(m,i+1,j, grid_access(m,i+1,j+1))
    grid_update(m,i+1,j+1, grid_access(m,i,j+1))
    grid_update(m,i,j+1,save)

m = empty(height,width)

def new_cell():
    return canvas.create_oval(80, 30, 140, 150, fill="blue")
    
grid_update(m,10,10, new_cell())
grid_update(m,10,11, new_cell())
grid_update(m,12,10, new_cell())
grid_update(m,12,11, new_cell())

def rotate_all(offset,m):
   i = offset
   while i < height:
       # take care of the row
       j = offset
       while j < width:
           # take care of the group
           if has_single_occupied_cell(m,i,j):
               rotate_group(m,i,j)
           j = j+2
       i = i+2


canvas.update_idletasks()

def callback(event):
    print("Called!")
    print(event)
    i = event.y  // cellsize
    j = event.x  // cellsize
    grid_update(m,i,j, new_cell())
    
canvas.bind("<Button-1>",callback)

offset = 1
iteration = 0
while True:
    iteration = iteration + 1
    offset = 1 - offset
    # display(m)
    rotate_all(offset,m)
    if iteration % 4 == 0:
        canvas.update()
    time.sleep(0.01)
