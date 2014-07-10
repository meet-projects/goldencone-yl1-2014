Michele's group project feedback
---

Good job finishing this project as a group, even if it was challenging for you. I have a few comments: 

* You have a function called `main.py`, except that is not the function I need to run to look at your project all together - I need to run the `WrapItUp.py` file. In general, it is better to call your main file `main.py` or something similar. 
* Great job getting the ice cream scoops to stack on top of each other. 
* It would be nice if on your DONE screen (where you show me the price) that you give me the option of "buy another scoop" so I can go back to buying scoops of ice cream. 
* It would also be nice if I could click the "x" at the top right corner of the pygame window and close the screen - there is sample code for how to do this on the student website in my sample project. 
* Good job using different files / functions for the different things you needed to draw on the screen. The only small problem was that you had to use many `global` variables. 
* I really like the creative way you came up with for making text appear on the screen - instead of using a `Label` class, you used a method that puts text somewhere on the screen. Both ways are excellent ways of solving the problem. 
* In your `WrapItUp.py` function, you use `main.Button.Rectangle` to get the Rectangle from the Button that was clicked - Button is a global variable that is coming from a different file. It is better coding practice to, if you want to pass information between files, to pass it not through global variables but through objects of a class. So for example, you would make a class called `screen` that takes care of drawing everything onto that screen, and it would have a variable that keeps track of the button you are looking for. This avoids having global variables, since they are in general bad for program memory. 
* In the `MakingScreen.py` file, good job breaking the screens into different functions - there are quite a lot of functions in that file that do different tasks for drawing the screen. 
* Good job not getting confused between the page number and ClickedyClick, for counting the page you are looking at and the number of ice cream scoops. 
* You could be a little bit better with your function and variable names, since some of them are not descriptive. 