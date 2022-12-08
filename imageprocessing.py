from PIL import Image

class ImageData:
    def __init__(self, path):
        self.image = Image.open(path)
        self.pixels = list(self.image.getdata())
    
    def imageSize(self) -> tuple:
        """returns the pixel dimentions of the image"""
        return self.image.size
    
    def pixel(self, x, y):
        "returns the pixel data of a given location via x and y coords"
        return self.pixels[self.image.size[0]*y+x]
    
    def writePixel(self, x, y, rgb):
        """changes the color of the pixel at the inputted location and to the inputted color"""
        self.pixels[self.image.size[0]*y+x] = rgb
    
    def saveAll(self, newName) -> None:
        """saves the new modified image as a png in the working directory"""
        img = Image.new('RGB', self.imageSize(), "black")
        pixel = img.load()
        
        
        # rowCounter will act as tge row number so it is like the y-axis value
        rowCounter = -1
        columCounter = 0
        
        for i, pix in enumerate(self.pixels):
            if i%self.imageSize()[0] == 0:
                rowCounter+=1
            
            if i%self.imageSize()[1] == 0:
                columCounter = 0
            
            pixel[columCounter, rowCounter] = pix 
            
            columCounter+=1
            
        
        img.save(newName)
    
    def zeroOneMatrix(self):
        matrix = []
        
        # the threshhold is half the sum of the rgb values
        threshHold = (255*3)/2
        
        for i in range(self.imageSize()[1]):
            matrix.append([])
            
        row = [] # this will act as a temp list that writes to matrix
        for height in range(self.imageSize()[1]):
            for width in range(self.imageSize()[0]):
                
                if type(self.pixel(width, height)) == int:
                    pixelVal = self.pixel(width, height)
                    
                    if pixelVal < 127.5:
                        pixelVal = 0
                    else:
                        pixelVal = 1
                
                else:
                
                    pixelVal = sum(self.pixel(width, height))
                    if pixelVal < threshHold:
                        pixelVal = 0
                    else:
                        pixelVal = 1
                
                row.append(pixelVal)
            matrix[height] = row
            row = []
        return matrix
        
    
def main():

    myImage = ImageData("./test-images/IMG_3625.jpg")
    print(myImage.imageSize())
    counter = 0
    print(myImage.zeroOneMatrix())
    print(len(myImage.zeroOneMatrix()))
    # for x in range(0,2048):
        # for y in range(0,1927):
            # print(myImage.pixel(x,y))
            # counter +=1
    # print(counter)

if __name__ == "__main__":
    main()