def setup():
    # Init 4960 x 7016
    size(4960, 7016)
    imageMode(CENTER)
    noStroke()
    
    # Load data
    img = loadImage("data/data11.jpg")
    img.resize(width, height)
    
    # First process 
    background(0)
    blendMode(DIFFERENCE)
    for n in range(10):
        x = width*0.5 +floor(random(-width*0.5, width*0.5))
        y = height*0.5 + floor(random(-height*0.5, height*0.5))
        image(img,  x,  y, random(width*3), random(height*3))
    
    # Overlay 
    blendMode(SCREEN)
    image(img, width*0.5, height*0.5)

    # Second proccess
    img.loadPixels()
    
    for n in range(1000):
        px = floor(random(width))
        py = floor(random(height))
        c = img.get(px, py)
        if (c != 0):
            fill(c)
            beginShape()
            for m in range(100):
                px += random(-11, 11)
                py += random(-11, 11)
                vertex(px, py)
            endShape()
    # Done
    save("out/out.png")

    exit()
