def setup():
    size(800, 800)
    background(255)
    img = loadImage("data-c-1.jpg")
    img.resize(width, height)
    img.loadPixels()
    
    maskImg = loadImage("mask.png")
    maskImg.resize(width, height)
    
    d = 50
    xs = width / d
    ys = height / d
    le = 300
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
                vertex(x + cos(nx*nx) * ns, y + sin(ny) * ns)
                nx += cos(x) * 0.01
                ny += 0.0027
            endShape()
    
    image(maskImg, 0, 0)        
    # save("out/"+str(random(10))+"glitchScapes.jpg")
 
