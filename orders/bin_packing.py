# rectpacking
# last update may 16, 2023

import matplotlib.pyplot as plt
import matplotlib.patches as patches


# store RECTANGLE INFORMATION
class Rectangle:
    def __init__(self, width, height, id=0):
        self.width = float(width)
        self.height = float(height)
        self.x = 0.0
        self.y = 0.0
        self.area = width * height
        self.id = id

    def rotate(self):
        self.width, self.height = self.height, self.width

    def overlaps(self, other):
        return not (self.x >= other.x + other.width or
                    self.x + self.width <= other.x or
                    self.y >= other.y + other.height or
                    self.y + self.height <= other.y)

    def __str__(self):
        return f"Rectangle(x={self.x:.1f}, y={self.y:.1f}, width={self.width:.1f}, height={self.height:.1f})"


# store sheet information
class Sheet:
    def __init__(self, width, height, sheet_number):
        self.width = float(width)
        self.height = float(height)
        self.sheet_number = sheet_number
        self.placements = []
        self.grid = []  # Grid to keep track of placed rectangles

    # check for overlap
    def overlaps_with_any(self, rectangle):
        for placed_rectangle in self.placements:
            if placed_rectangle.overlaps(rectangle):
                return True
        return False

    # okace rectangles in a shee
    def place_rectangle(self, rectangle, attempt_rotation=2):
        # If the grid is empty, add the rectangle to a new row
        if not self.grid:
            if rectangle.width <= self.width and rectangle.height <= self.height:
                rectangle.x = 0.0
                rectangle.y = 0.0
                new_row = [rectangle]
                self.grid.append(new_row)
                self.placements.append(rectangle)
                return True

        # find place for rectangle
        for i, row in enumerate(self.grid):
            row_width = sum([r.width for r in row])
            if row_width + rectangle.width <= self.width:
                rectangle.x = row_width
                rectangle.y = row[0].y
                if not self.overlaps_with_any(rectangle):
                    row.append(rectangle)
                    self.placements.append(rectangle)
                    return True

        # If rectangle doesn't fit in current row, check if it can be placed in a new row
        max_height_in_last_row = max([rectangle.y + rectangle.height for rectangle in self.grid[-1]])
        if max_height_in_last_row + rectangle.height <= self.height:
            rectangle.x = 0.0
            rectangle.y = max_height_in_last_row
            if not self.overlaps_with_any(rectangle):
                new_row = [rectangle]
                self.grid.append(new_row)
                self.placements.append(rectangle)
                return True

        # If the rectangle couldn't be placed and rotation hasn't been attempted yet, and rotation would help, rotate and try again
        # if attempt_rotation and ((self.width >= rectangle.height and self.height >= rectangle.width) != (self.width >= rectangle.width and self.height >= rectangle.height)):
        if attempt_rotation > 0:
            rectangle.rotate()
            return self.place_rectangle(rectangle, attempt_rotation - 1)

        return False

    # plot rectangles in sheet
    def plot(self):
        fig, ax = plt.subplots()
        for rect in self.placements:
            ax.add_patch(patches.Rectangle((rect.x, rect.y), rect.width, rect.height, fill=False))
            annotation = f"x:{rect.x:.1f}, y:{rect.y:.1f}, w:{rect.width:.1f}, h:{rect.height:.1f}"
            ax.text(rect.x, rect.y, annotation, fontsize=6)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        plt.show()


# pack rectangles into sheets
class Driver:
    def __init__(self, sheet_width, sheet_height):
        self.sheet_width = float(sheet_width)
        self.sheet_height = float(sheet_height)
        self.sheets = []

    # sort rectangle by orientation then area
    def sort_rectangles(self, rectangles):
        # Align the orientation of rectangles with the sheet
        for rectangle in rectangles:
            if ((self.sheet_width > self.sheet_height and rectangle.width < rectangle.height) or
                    (self.sheet_height > self.sheet_width and rectangle.height < rectangle.width)):
                rectangle.rotate()

        # sort by area
        sorted_rectangles = sorted(rectangles, key=lambda r: r.area, reverse=True)
        return sorted_rectangles

    # pack all rectangles in sheet
    def pack_rectangles(self, rectangles):

        # Sort the rectangles by width/height orientation then area
        sorted_rectangles = self.sort_rectangles(rectangles)

        sheet_number = 1
        sheet = Sheet(self.sheet_width, self.sheet_height, sheet_number)  # Create a new sheet

        # for all rectangles place in sheets
        for rectangle in sorted_rectangles:
            if not sheet.place_rectangle(rectangle):
                self.sheets.append(sheet)
                sheet_number += 1
                sheet = Sheet(self.sheet_width, self.sheet_height, sheet_number)  # Create a new sheet
                sheet.place_rectangle(rectangle)

        # Add the final sheet if it's not empty
        if sheet.placements:
            self.sheets.append(sheet)

        return self.sheets

    # plot all sheets
    def plot_sheets(self):
        for sheet in self.sheets:
            print(f"Sheet #{sheet.sheet_number}")
            for placement in sheet.placements:
                print(placement)
            sheet.plot()


# test vertical sheet
driver = Driver(sheet_width=2768, sheet_height=1549)




rectangles = [
    Rectangle(698.5, 762), Rectangle(698.5, 762), Rectangle(698.5, 762), Rectangle(698.5, 762),
    Rectangle(698.5, 762), Rectangle(698.5, 762), Rectangle(292.1, 1219.2),

]
driver.pack_rectangles(rectangles)
driver.plot_sheets()

# # test horizontal sheet
# driver = Driver(sheet_width=90, sheet_height=65.5)
# rectangles = [
#     Rectangle(30.5, 40.5), Rectangle(30.5, 40.5), Rectangle(30.5, 40.5), Rectangle(30.5, 40.5),
#     Rectangle(40, 30), Rectangle(40, 30), Rectangle(40, 30), Rectangle(40, 30),
#     Rectangle(40, 30), Rectangle(30, 40), Rectangle(40, 30), Rectangle(30, 40), Rectangle(40, 10)
# ]

# pack rectangles
# driver.pack_rectangles(rectangles)
# driver.plot_sheets()
