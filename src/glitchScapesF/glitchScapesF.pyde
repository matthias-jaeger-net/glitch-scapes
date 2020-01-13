def setup():
    size(800, 800)
    background(0)
    img2 = loadImage("data.jpg")
    img = loadImage("data6.jpg")
    img.resize(width, height)
    img.loadPixels()
    img2.loadPixels()

    maskImg = loadImage("mask.png")
    maskImg.resize(width, height)

    d = floor(random(10, 140))
    xs = width / d
    ys = height / d
    le = floor(random(10, 40))
    nx = 0
    ny = 0
    ns = floor(random(10, 40))
    for r in range(d):
        for c in range(d):
            x = r * xs
            y = c * ys
            noStroke()
            if (random(0, 1) > 0.5):
                fill(img.get(x, y))
            else:
                fill(img2.get(x, y))

            beginShape()
            for n in range(le):
                vertex(x + cos(nx * nx) * ns, y + sin(ny * ny) * ns)
                ny += 1.0 / le
                nx += 1.0 / le
            endShape()

    image(maskImg, 0, 0)
    save("out/" + str(random(10)) + "glitchScapesF.jpg")
