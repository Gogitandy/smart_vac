#Import choice to help build random room layout
from random import shuffle, choice, randint

class Room:
    def __init__(self, x=5):
        self.nrows = x
        self.ncols = x
        #add random layout to the room constructor
        self.layout = self.layout_randomizer()
        #print(self.layout)
        self.no_islands()
        print("---")
        for list in self.layout:
            print(list)
        self.add_furniture()
        print("---")
        for row in self.layout:
            print(row)
        return

    #method to generate a random layout within the grid size determined by user
    def layout_randomizer(self):
        #list for entire layout
        layout = []
        #add buffer of 0's across top for out of bounds
        layout.append([0] * (self.ncols + 2))
        #iterate through all rows
        for i in range(self.nrows):
            #list for cells in row (will be 1 or 0) starting with initial 0
            row = [0]
            #iterate through all columns
            for j in range(self.ncols):
                #pick at random 1 (cell=in room) 0 (cell=not in room)
                if i == 0 or i == self.nrows - 1:
                    row.append(choice([0, 1]))
                elif j == 0 or j == self.ncols - 1:
                    row.append(choice([0, 1]))
                else:
                    row.append(1)
            #add 0 for boundary
            row.append(0)
            #add completed row to layout
            layout.append(row)
        #add bottom border of 0's for buffer
        layout.append([0] * (self.ncols + 2))

        return layout

    #check all the corners to make sure that there are no isolated 1's
    #updated to fix corners inside the border of 0's
    def no_islands(self):
        #check upper left corner
        #print("check1")
        if (
            self.layout[1][1] == 1 and
            self.layout[1][2] == 0 and
            self.layout[2][1] == 0
            ):
            #fix upper left island
            #print("FIX!")
            self.layout[1][2] = 1
        #check upper right corner
        if (
            self.layout[1][self.ncols] == 1 and
            self.layout[1][self.ncols - 1] == 0 and
            self.layout[2][self.ncols] == 0
            ):
            #fix upper right island
            #print("FIX!")
            self.layout[1][self.ncols - 1] = 1
        #check lower left corner
        if (
            self.layout[self.nrows][1] == 1 and
            self.layout[self.nrows][2] == 0 and
            self.layout[self.nrows - 1][1] == 0
            ):
            #fix lower left island
            #print("FIX!")
            self.layout[self.nrows][2] = 1
        #check lower right corner
        #print("check2")
        if (
             self.layout[self.nrows][self.ncols] == 1 and
             self.layout[self.nrows][self.ncols - 1] == 0 and
             self.layout[self.nrows - 1][self.ncols] == 0
            ):
            #fix lower right island
            #print("FIX!")
            self.layout[self.nrows][self.ncols - 1] = 1

        return

    #method to add random furniture if room > 7x7
    def add_furniture(self):
        if self.ncols > 7:
            for i in range (3, self.nrows - 3):
                for j in range (3, self.ncols - 3):
                    if choice([True, False]):
                        if (
                             self.layout[i - 1][j] == 1 and
                             self.layout[i + 1][j] == 1 and
                             self.layout[i][j + 1] == 1 and
                             self.layout[i][j - 1] == 1
                            ):
                            self.layout[i][j] = 0
                            print(f"add {i},{j}")
        return
