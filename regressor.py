###

from statistics import mean, median, mode, stdev, variance
import matplotlib.pyplot as plt

class bivar:
    '''
    Bivariate Data Class
    ----------------------------------------------------------------
    A class to store bivariate data
    ----------------------------------------------------------------
    Methods:
    - __init__(data): takes in an array of tuples, each tuple being a point in the form (x, y)
    - __str__(): returns the string representation of the data
    ----------------------------------------------------------------
    Attributes:
    - data: a list of tuples, each tuple being a point in the form (x, y)
    - x: an array of all the x values
    - y: an array of all the y values
    ----------------------------------------------------------------
    '''
    
    def __init__(self, data):
        self.data = data
        self.x = [data[i][0] for i in range(len(data))]  # breaking into x and y arrays
        self.y = [data[i][1] for i in range(len(data))]  # numpy not used as not necessary, though can be added if needed
    
    def __str__(self):
        return str(self.data)  # mainly to check if the data is being stored correctly

# testing
'''
a = bivar([(1, 2), (3, 4), (5, 6)])
print(a.__str__())
'''


class regress(bivar):
    '''
    Regress Class
    ----------------------------------------------------------------
    A class to perform linear regression on the bivariate data. Inherits from class 'bivar'
    ----------------------------------------------------------------
    Methods:
    - __init__(data): takes in an array of tuples, each tuple being a point in the form (x, y)
    - __str__(): returns the string representation of the data
    - x_bar(): returns the mean of the x values
    - y_bar(): returns the mean of the y values
    - s_x(): returns the standard deviation of the x values
    - s_y(): returns the standard deviation of the y values
    - r(): returns the (pearson) product momentum correlation coefficient
    - m(): returns the gradient of the line of best fit (line of least squares)
    - c(): returns the y-intercept of the line of best fit
    - line(): returns the equation of the line of best fit
    - plot(): plots the line of best fit & all data points
    ----------------------------------------------------------------
    Attributes:
    - data: a list of tuples, each tuple being a point in the form (x, y)
    - x: an array of all the x values
    - y: an array of all the y values
    ----------------------------------------------------------------
    '''

    def x_bar(self):
        return mean(self.x)
    
    def y_bar(self):
        return mean(self.y)
    
    def s_x(self):
        return stdev(self.x)
    
    def s_y(self):
        return stdev(self.y)
    
    def r(self):
        top = sum([(self.x[i]-self.x_bar())*(self.y[i]-self.y_bar()) for i in range(len(self.x))])
        bottom = (sum([(self.x[i]-self.x_bar())**2 for i in range(len(self.x))]) * sum([(self.y[i]-self.y_bar())**2 for i in range(len(self.y))]))**0.5

        return top/bottom   # see pearson correlation coefficient formula

    def m(self):
        return self.r() * (self.s_y() / self.s_x())
    
    def c(self):
        return self.y_bar() - self.m() * self.x_bar()
    
    def line(self):
        return f"y = {self.m()}x + {self.c()}"
    
    def plot(self):
        plt.scatter(self.x, self.y) # plot scattered points
        # plt.plot([min(self.x), max(self.x)], [self.m() * min(self.x) + self.c(), self.m() * max(self.x) + self.c()], color = 'red')
        x_values = [min(self.x), max(self.x)]
        y_values = [self.m() * x + self.c() for x in x_values]
        plt.plot(x_values, y_values, color='red')
        plt.scatter(self.x_bar(), self.y_bar(), color='red')  # plot line of least squares
        plt.annotate(f'({self.x_bar()}, {self.y_bar()})', (self.x_bar(), self.y_bar()), textcoords="offset points", xytext=(0,10), ha='center')  # label the coordinates of (x_bar, y_bar)
        plt.show()  # display the plt in another window

# testing
'''
b = regress([(49,90), (51,88), (54,85), (58,91), (63,82), (64,85), (68,76), (70,77), (75,70), (78,71)])
c = regress([(15,4.4067), (30,4.1744), (60,3.7612), (90,3.6109), (120,3.0910), (150,2.9444), (180,2.4849), (240,1.7918), (300,0.69315)])
print(c.x_bar())
print(c.y_bar())
print(c.s_x())
print(c.s_y())
print(c.line())
c.plot()
'''


def main():
    '''
    Main Function
    ----------------------------------------------------------------
    The driver function to regress points, to make the entering of pts easier. Calls regress
    ----------------------------------------------------------------
    Methods:
    [None]
    ----------------------------------------------------------------
    Attributes:
    - pts: an array of user-entered points in the form (x, y)
    - r: an instance of the regress class created using pts
    ----------------------------------------------------------------
    '''

    print('Welcome to the linear regressor.')
    print('NOTE: Enter 0 to stop entering points.')

    pts = []  # see docstring

    enter = True  # boolean flag to let user continuously enter all data
    while enter != False:
        pt = input('Enter a point in the form (x,y): ')

        if pt == '0':  # exit code
            enter = False
            break  # not very beautiful but it works

        comma = pt.index(',')

        x = float(pt[1:comma:])
        y = float(pt[comma+1:-1:])  # slicing the x and y values from the input

        pts.append((x, y))
    
    print(f'Your points are: {pts}')

    r = regress(pts)  # regress class instance
    print(f'Line of best fit: {r.line()}')
    r.plot()



# driver
main()


# for documentation or help see: help(regress) or help(bivar)
# Hongpeng, 2024