# linreg
Linear regressor. 

Give an array of (x,y) and it will return a plot and the line of least squares.

Interact with the code either using the ```main()``` function or by directly creating the ```regress``` class instance.

E.g.: 
```
# using the app using the main function
main()
```

or

```
# directly entering the array of (x,y) tuples as shown in the file
c = regress([(15,4.4067), (30,4.1744), (60,3.7612), (90,3.6109), (120,3.0910), (150,2.9444), (180,2.4849), (240,1.7918), (300,0.69315)])
print(c.line())
c.plot()
```

The line of best fit should open in a separate matplotlib window.

The Windows executable can be downloaded at: [https://drive.google.com/file/d/1yihwD3MzIbgoT_WVLPIG69XFGh48OYAp/view?usp=sharing]([url](https://drive.google.com/file/d/1yihwD3MzIbgoT_WVLPIG69XFGh48OYAp/view?usp=sharing))
