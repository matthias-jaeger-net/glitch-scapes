def setup():
    size(800, 800)
    imageMode(CENTER)
    img = loadImage("data-c-2.jpg")
    img.resize(width, height)
    maskImg = loadImage("mask.png")
    maskImg.resize(width, height)
    # First process 
    background(0)
    blendMode(DIFFERENCE)
    for n in range(10):
        x = floor(random(-400, 400))
        y = floor(random(-400, 400))
        image(img, 400 + x, 400 + y, random(width*3), random(height*3))
    
    blendMode(SCREEN)
    image(img, 400, 400)
    
    img.loadPixels()
    
    for n in range(1000):
        px = floor(random(width))
        py = floor(random(height))
        c = img.get(px, py)
        stroke(c, 100)
        #line(0, py, width, py)
        
        for m in range(2000):
            px += random(-1, 1)
            py += random(-1, 1)
            point(px, py)
    
    blendMode(BLEND)
             
    image(maskImg, 400, 400)
    
    save("out/"+str(random(10))+"glitchScapes.jpg")
