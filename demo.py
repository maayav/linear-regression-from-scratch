from numpy import*
def compute_error_for_line_points(b,m,points):
    #initialize the error at 0
    totalError=0
    #for every point 
    for i in range(0,len(points)):
        #get the x value
        x=points[i,0]
        #get the y value
        y=points[i,1]
        #get the difference , square it and add it to the total
        totalError+=(y-(m*x+b))**2 #formula used to calculate the error(m,b) with the initial line
    #Get the Average 
    return totalError/float(len(points))


    
def run():
    #Collect our data
    points = genfromtxt('data.csv',delimiter=',') #x=hours studied , y = marks scored by students

    #defining hyperparameters (parameters that define how the model is analyzing the data)
    learning_rate=0.0001 #how fast our models converge
    #y=mx+b(slope)
    initial_b=0
    initial_m=0
    num_iterations=1000

    #training model
    print 'starting gradient descent at b={0},m={1},error={2}'.format(initial_b,initial_m,compute_error_for_line_given_points(initial_b,initial_m,points))
    [b,m]= gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    
    print 'starting gradient descent at b={1},m={2},error={3}'.format(num_iterations,b,m,compute_error_for_line_given_points(b,m,points))

    
if __name__ == '__main__':
    run()