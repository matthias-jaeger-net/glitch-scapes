# glitch-scapes
Glitch landscape image generator w/ Processing



# Examaple images
![glitchScapes](imgages/cover.png)

## Data Downloads
- Final front side
- - https://github.com/matthias-jaeger-net/shirts-processed/raw/master/print/shapeFlow/matthias-jaeger-net--shapeFlow.pdf
- Final back side
- - https://github.com/matthias-jaeger-net/shirts-processed/raw/master/print/shapeFlow/matthias-jaeger-net--shapeFlow-code.pdf

## Printed code
```java
import processing.pdf.*;

String title = "matthias-jaeger-net--shapeFlow.pdf";
PGraphics pdf = createGraphics(3600, 3600, PDF, title);
PVector[] shape = new PVector[100];

for (int i = 0; i < shape.length; i++) {
  float x = i * (pdf.width / shape. length);
  shape[i] = new PVector(x, 0);
}

pdf.beginDraw();
pdf.fill(255, 255, 255);
pdf.stroke(0, 0, 0);
pdf.strokeWeight(8);

for (int i = 0; i < pdf.height; i++) {
  pdf.beginShape();
  for (PVector vector : shape) {
    pdf.vertex(vector.x, vector.y);
    float shift_x = random(-10, 10);
    float drops_y = random(0, 30);
    vector.add(new PVector(shift_x, drops_y));
  }
  pdf.endShape();
}

pdf.endDraw();
pdf.dispose();
exit();
```
