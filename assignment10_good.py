from graphics import *

def main():
    win = GraphWin("BMI Calculator", 500, 600)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1,3)," Enter height in feet:").draw(win)
    Text(Point(1,3.25)," Enter the remaining inches:").draw(win)
    Text(Point(1,2.75)," Enter Weight in pounds:").draw(win)
    Text(Point(1,1), "Your BMI is: ").draw(win)
    
    input1 = Entry(Point(2.5,3),5)
    input1.setText("0.0")
    input1.draw(win)
    output1 = Text(Point(2.1, 1),"")
    output1.draw(win)

    input2 = Entry(Point(2.5,3.25),5)
    input2.setText("0.0")
    input2.draw(win)
    output1 = Text(Point(2.1, 1),"")
    output1.draw(win)

    input3 = Entry(Point(2.5, 2.75),5)
    input3.setText("0.0")
    input3.draw(win)
    output1 = Text(Point(2.1, 1),"")
    output1.draw(win)

    output2 = Text(Point(1.5, 0.66),"")
    output2.draw(win)
    
  #creating the calculate and output button
    
    button1 = Text(Point(1.5, 2.0),"Calculate BMI")
    button1.draw(win)
    rectangle1 = Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)
    win.getMouse()
    rectangle2 = Rectangle(Point(1.0,0.5),Point(2,0.75)).draw(win)
    
  #BMI calculations
    
    height_feet = float(input1.getText())
    height_inches = float(input2.getText())
    height = (height_feet * 12) + height_inches
    weight = float(input3.getText())
    bmi = (703 * weight) / (height**2)

    if bmi < 18.5:
        rectangle2.setOutline('DarkOliveGreen1')
        output2.setOutline('DarkOliveGreen1')
        x = "you are underweight"
    elif bmi >= 18.5 and bmi < 25:
        rectangle2.setOutline('green2')
        output2.setOutline('green2')
        x = "you are a normal weight"
    elif bmi >= 25 and bmi < 30:
        rectangle2.setOutline('tomato2')
        output2.setOutline('tomato2')
        x = "you are overweight"
    elif bmi >=30:
        rectangle2.setOutline('red2')
        output2.setOutline('red2')
        x = "you are obese"
        
    output1.setText(str(bmi))
    output2.setText(str(x))
    button1.setText("Quit")
    win.getMouse()
    win.close()
    #click = win.getMouse()
    #if click.getX() == rectangle1 or click.getY() == rectangle1:
    #    win.close()
    
    
        

main()
