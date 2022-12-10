from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import imageprocessing as ImPro
import resize
import os
from numba import jit
import cv2
from threading import Thread

print("""please enter photos that are as close to black and white as possible. Also the excepted file formats
png, jpg, jpeg, and heic. finally when a new window is shown, press any key for it to close.\n\n""")

print("when the first image prompt shows please click on the image where you want the start and end point to be\n\n")

directory = input("please enter in the directory of the image\n")

         

location = []
counter = 0
def mouseEvent(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global counter
        counter += 1
        location.append((x,y))

img = cv2.imread(directory)
cv2.imshow("image", img)
cv2.setMouseCallback("image", mouseEvent)


def countCheck():
    while counter < 2:
        pass
    cv2.destroyWindow("image")
    print(location)

task = Thread(target=countCheck, daemon = True)

task.start()
        
cv2.waitKey(0)

divider = resize.downScale(directory)


image = ImPro.ImageData("new.jpg")

matrix = image.zeroOneMatrix()
        
grid = Grid(matrix=matrix)

start = grid.node(int(location[0][0]/divider), int(location[0][1]/divider))
end = grid.node(int(location[1][0]/divider), int(location[1][1]/divider))

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)



# drawing the best path line

def draw(path: list, image: ImPro.ImageData) -> None:
    for coords in path:
        image.writePixel(coords[0], coords[1], (255,0,0))
    
    image.saveAll("./output.png")

draw(path=path, image=image)

os.system("rm new.jpg")

img = cv2.imread("output.png")
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

os.system("rm output.png")