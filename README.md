## pi-monte-carlo: Estimate &#960; using the Monte Carlo Method

<p align="center">
  <img src="img/example_estimation.svg">
  <br></br>
  <b>Estimation of pi with a sample size of n=10000</b>
</p>

## Getting Started
### Dependencies ###

- [Cython](https://cython.org/) is used for calculations to increase performance
- Random points are generated using [Numpy](https://numpy.org/) 
- Graphs are plotted using [Matplotlib](https://matplotlib.org/)

### Preperations ###
1. Clone the repository
```bash
git clone https://github.com/emrecil/pi-monte-carlo
cd pi-monte-carlo
```


2. Install requirements
```bash
pip install -r requirements.txt
```


3. Build Cython file
```bash
python setup.py build_ext --inplace
```

## Usage

To start the program run the following command
```bash
python monte_carlo_pi.py
```

By default 1000 random points will be generated. You can specify a custom sample size as an argument:
```bash
python monte_carlo_pi.py [sample size]
```

## How it works
First we draw a unit square which has an Area of ![area of square](https://latex.codecogs.com/gif.latex?A_%7Bsquare%7D%20%3D%201). Then we draw a circle inside this square with a radius of 0.5. The area of this circle is 
![area of circle](https://latex.codecogs.com/gif.latex?A_%7Bcircle%7D%20%3D%20%5Cfrac%7B%5Cpi%7D%7B4%7D).

Now we create n random points inside the square. With the ratio of the number of points inside the circle to the total number of points an approximation of &#960; can be computed since:

![ratio area circle to area square](https://latex.codecogs.com/gif.latex?%5Cfrac%7BA_%7Bcircle%7D%7D%7BA_%7Bsquare%7D%7D%20%3D%20%5Cfrac%7B%5Cpi%5Cfrac%7B1%7D%7B4%7D%7D%7B1%7D%20%3D%20%5Cfrac%7B%5Cpi%7D%7B4%7D)

and thus

![formula to estimate pi](https://latex.codecogs.com/gif.latex?%5Cpi%5C%20%5Capprox%5C%204%5C%20*%5C%20%5Cfrac%7B%20number%5C%20of%5C%20points%5C%20inside%5C%20the%5C%20circle%7D%7Btotal%5C%20number%5C%20of%5C%20points%7D).
