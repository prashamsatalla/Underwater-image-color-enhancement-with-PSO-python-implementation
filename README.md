# Underwater-image-color-enhancement-with-PSO-python-implementation

Implemented the research paper, [Natural-based underwater image color enhancement through fusion of swarm-intelligence algorithm](http://umpir.ump.edu.my/id/eprint/26347/) in python language. <br />
### The Four steps strategy followed in NUCE method:
- Superior based underwater color cast neutralization
- Dual-intensity images fusion based on average of mean and median values
- Swarm-intelligence based mean equalization
- Unsharp masking

**Image credits**: [paper](http://umpir.ump.edu.my/id/eprint/26347/) <br />
![](https://github.com/prashamsatalla/Underwater-image-color-enhancement-with-PSO-python-implementation/blob/main/NUCE_flowchart.png)

## User Guide
- Clone this repository
```commandline
$ git clone https://github.com/prashamsatalla/Underwater-image-color-enhancement-with-PSO-python-implementation.git
$ cd Underwater-image-color-enhancement-with-PSO-python-implementation
```
- Collect input images in **images** folder, then the enhanced output image will be saved in **results** folder with respective input image name.
- Install required packages 
```commandline
$ pip install -r requirements.txt
```
- Run main.py .
```commandline
$ python main.py
```

### Code Result:
![](https://github.com/prashamsatalla/Underwater-image-color-enhancement-with-PSO-python-implementation/blob/main/results/output.jpg)

## Dependencies
- OpenCV 3.4.8
- NumPy
- Matplotlib
