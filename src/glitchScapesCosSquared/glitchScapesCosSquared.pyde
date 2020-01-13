
"""
glitchScapesCosSquared

"""
add_library('pdf')
url = "data9.jpg"
img = None
density = 90 # How many grid cells
time = 300 # How long will be iterated 
ns = 50 # Scaler to multiply the effects
nx = ny = 0 # Will be increased
incX = 0.01 
incY = 0.027

def renderShape(x, y):
    global nx, ny

    # Render the shape
    beginShape()
    for n in range(time):
        # Polar cos squared effect
        addx = cos(nx * nx) * ns
        addy = sin(ny) * ns  # TRY + sin(ny * nx) * ns * 0.3
        vertex(x + addx, y + addy)
        ny += incX
        nx += incY
    endShape()
    
def setup():
    global img
    # Format settings
    size(500, 700)
    # Load image data (skew image to fit)
    img = loadImage(url)
    img.resize(width, height)
    
def draw():
    global img
    noLoop()    
    beginRecord(PDF, "out/"+url+"glitchScapesCosSquared.pdf")
    
    background(0)
    noStroke()
    
    img.loadPixels()  
    
    # HACK – Hide ripples on the right
    scale(1.3) 
    
    # Grid
    for rows in range(density):
        for cols in range(density):
            # Calculate grid coordinates
            x = rows * (width / density)
            y = cols * (height / density)
    
            # Pick the fill color from the image
            fill(img.get(x, y))
            renderShape(x, y)
    
    endRecord()
    exit()
