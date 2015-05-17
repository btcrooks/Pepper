# Disable PyFlakes: let g:pymode_lint = 0
import math

class Pepper:
  # Maths
  def roundUp(self,x):
    return int(math.ceil(x / 10.0)) * 10
    #return x
  # Coordinates
  def printMouseCoordinates(self):
    print "Mouse Coordniates:"
    print "X: %s" % (mouseX/grid.cell_width)
    print "Y: %s" % (mouseY/grid.cell_height)
  def mouseCellPosition(self,coord):
    if coord == "x":
      return int(mouseX/grid.cell_width)
    elif coord == "y":
      return int(mouseY/grid.cell_height)
    else:
      print "Please specify if you want to return 'x' or 'y' coordinate for\
            object: pepper.mouseCellPosition"
  # Editor State
  ## Colors
  red   = color(255,0,0)
  green = color(0,255,0)
  blue  = color(0,0,255)
  ## Color State
  color_state = red
  # Log to console
  def log(self):
    print "Editor:"
    print "Color State: %s" % (self.color_state)
    print ""

class Stage:
  width = 1280
  height = 720
  background_color = 20

class Grid:
  def __init__(self, row, col, cell_dimensions, margin):
    self.cell = []
    self.row = row
    self.col = col
    self.cell_dimensions = cell_dimensions
    self.margin = margin
    self.cell_height = self.cell_width = cell_dimensions
    # Log to console
  def draw(self):
    posx = 0
    posy = 0
    for col in grid.cell:
      for row in col:
        if row == 1:
          fill(pepper.color_state)
        else:
          fill(255,255,255)
        rect(posx,posy,grid.cell_width,grid.cell_height)
        posy = posy + grid.cell_height
      posx = posx + grid.cell_width
      posy = 0
  def log(self):
    print "Grid info:"
    print "Grid is %s x %s with a %s margin" % (self.row, self.col,
                                                     self.margin)
    print "Cell Width:  %s" % (self.cell_width)
    print "Cell Height: %s" % (self.cell_height)
    print ""

###################
# Class: Pepper
# Arguments:
#  - None
###################
pepper = Pepper()

###################
# Class: Stage
# Arguments:
#  - None
###################
stage = Stage()

###################
# Class: Grid
# Arguments:
#  - Number of Rows
#  - Number of Columns
#  - Cell Dimensions (x = y)
#  - Cell Margin
##################
grid = Grid(50,50,10,0)
for row in range(grid.row):
  grid.cell.append([])
  for col in range(grid.col):
    grid.cell[row].append(0)

def setup():
  size(stage.width,stage.height)
  background(stage.background_color)
  grid.cell[1][1] = 1
  # Log all the things
  print "Setup Log:"
  pepper.log()
  grid.log()
  print ""

def draw():
  stroke(222,0,0)
  grid.draw()
  if keyPressed:
    if key == 'b':
      pepper.color_state = pepper.blue

def mousePressed():
  x = pepper.mouseCellPosition("x")
  y = pepper.mouseCellPosition("y")
  if grid.cell[x][y] == 1:
    grid.cell[x][y] = 0
  elif grid.cell[x][y] == 0:
    grid.cell[x][y] = 1
  else:
    pass
