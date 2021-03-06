# Disable PyFlakes: let g:pymode_lint = 0
#import math
import os
import sys
sys.path.append(os.getcwd())
import pepperUI

class Pepper:
  # Maths
  #def roundUp(self,x):
    #return int(math.ceil(x / 10.0)) * 10
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
      print "Please specify if you want to return an 'x' or 'y' coordinate for\
            object: pepper.mouseCellPosition"
  # Editor State
  ## Colors
  red   = color(255,0,0)
  green = color(0,255,0)
  blue  = color(0,0,255)
  black = color(0)
  translucent = color(0,0,0,0)
  ## Color State
  color_state = 1
  # Log to console
  def log(self):
    print "Editor:"
    print "Color State: %s" % (self.color_state)

class Stage:
  width = 1280
  height = 720
  background_color = 20
  background_image = loadImage("resources/UI_Background.png")
  stroke_color = color(0,0,0,0)
  #stroke_color = color(15,15,15,50)


class Grid:
  def __init__(self, row, col, cell_dimensions, margin):
    self.cell = []
    self.row = row
    self.col = col
    self.cell_dimensions = cell_dimensions
    self.margin = margin
    self.cell_height = self.cell_width = cell_dimensions
  def draw(self):
    posx = 0
    posy = 0
    for col in grid.cell:
      for row in col:
        if row == 1:
          fill(pepper.red)
        elif row == 2:
          fill(pepper.green)
        elif row == 3:
          fill(pepper.blue)
        else:
          fill(0,0,0,0)
        rect(posx,posy,grid.cell_width,grid.cell_height)
        posy = posy + grid.cell_height
      posx = posx + grid.cell_width
      posy = 0
  # Log to console
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
#################r
grid = Grid(150,160,5,0)
for row in range(grid.row):
  grid.cell.append([])
  for col in range(grid.col):
    grid.cell[row].append(0)

def setup():
  size(stage.width,stage.height)
  smooth()
  cursor(HAND)
  # Log all the things
  print "Setup Log:"
  pepper.log()
  grid.log()
  # Graphics Buffer
  #pg = createGraphics(500,500)

def draw():
  background(stage.background_image)
  noStroke()
  #stroke(stage.stroke_color)
  grid.draw()
  # Handle Mouse Events
  # Kludge hard in the paint...
  try:
    if mousePressed and (mouseButton == LEFT):
      x = pepper.mouseCellPosition("x")
      y = pepper.mouseCellPosition("y")
      if (pepper.mouseCellPosition("x") <= len(grid.cell)) and\
      (pepper.mouseCellPosition("y") <= len(grid.cell)*10):
        if grid.cell[x][y] != pepper.color_state:
          grid.cell[x][y] = pepper.color_state
  except:
    # TODO: Try pass statement
    print ""

def keyPressed():
  k = str(key)
  print "Key logged: %s" % (k)
  if k == "1":
    pepper.color_state = 1
  elif k == "2":
    pepper.color_state = 2
  elif k == "3":
    pepper.color_state = 3
  elif k == "e":
    pepper.color_state = 0
  elif k == "~":
    print "Console: "
  elif k == "c":
    grid.cell = []
    for row in range(grid.row):
      grid.cell.append([])
      for col in range(grid.col):
        grid.cell[row].append(0)
    print "Screen cleard!"

  elif k == "s":
    img  = get(0, 0, 750, stage.height)
    print "Saving image..."
    img.save("drawing.tif")
