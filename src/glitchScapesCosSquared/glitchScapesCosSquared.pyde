def setup():
    size(800, 800)
    background(0)
    img = loadImage("data5.jpg")
    img.resize(width, height)
    img.loadPixels()     
    
    maskImg = loadImage("mask.png")
    maskImg.resize(width, height)
    
    d = 20
    xs = width / d
    ys = height / d
    le = 100
    nx = 0
    ny = 0
    ns = 100
    for r in range(d):
        for c in range(d):
            x = r * xs
            y = c * ys
            noStroke()
            fill(img.get(x, y))
            beginShape()
            for n in range(le):
                vertex(x + cos(nx*nx) * ns, y + sin(ny) * ns + sin(ny * nx) * ns * 0.3)
                ny += cos(n) * 0.1
                nx += 0.027
            endShape()

    image(maskImg, 0, 0)        
    #save("out/"+str(random(10))+"glitchScapesCosSquared.jpg")
 
