# Disable PyFlakes: let g:pymode_lint = 0

class Stage:
  width = 1280
  height = 720
  background_color = 20

class Grid:
  def __init__(self, row, col, cell_dimensions, margin):
    self.row = row
    self.col = col
    self.margin = margin
    self.cell_height = self.cell_width = cell_dimensions
    # Log to console
    print "Grid is %spx x %spx with a %spx margin" % (self.row, self.col,
                                                     self.margin)
    print "Cell Width:  %s" % (self.cell_width,)
    print "Cell Height: %s" % (self.cell_height,)

stage = Stage()
###################
# GRID Class
# Arguments:
#  - Number of Rows
#  - Number of Columns
#  - Cell Dimensions (x = y)
#  - Cell Margin
##################
grid = Grid(20,20,20, 0)
posx = posy = 0

def setup():
  size(stage.width,stage.height)
  background(stage.background_color)

def draw():
  stroke(222,0,0)
  for posx in range(grid.row):
    rect(posx*grid.cell_width,posy,grid.cell_width,grid.cell_height)
