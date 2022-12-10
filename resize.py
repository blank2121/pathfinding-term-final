import cv2



def downScale(path):
    img = cv2.imread(path)
    # WIDTH and HEIGHT are integers


    width, height = img.shape[0], img.shape[1]

    width = int(width/1)
    height = int(height/1)
    divider = 1
    while (width/divider) > 650 and (height/divider) > 650:
        divider+=1
    
    width = int(width/divider)
    height = int(height/divider)

    new_img = cv2.resize(img, (height,width))
    cv2.imwrite("new.jpg", new_img)
    return divider