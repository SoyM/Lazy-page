# Harris Corner Detection
It basically finds the difference in intensity for a displacement of **(u,v)** in all directions. This is expressed as below:

![](http://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/1948f2850c912ce3394b61ba99b546f1bf7a6adc.png)

Window function is either a rectangular window or gaussian window which gives weights to pixels underneath.

We have to maximize this function E(u,v) for corner detection. That means, we have to maximize the second term. Applying Taylor Expansion to above equation and using some mathematical steps (please refer any standard text books you like for full derivation), we get the final equation as:

![](http://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/3aea48f44ebcc36dda8055c842e209d8886d7a80.png)
# Shi-Tomasi Corner Detector &amp;amp; Good Features to Track

# Scale-Invariant Feature Transform
