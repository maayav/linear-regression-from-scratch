from numpy import*
def run():
    #Collect our data
    points = genfromtxt('data.csv',delimiter=',') #x=hours studied , y = marks scored by students

    #defining hyperparameters (parameters that define how the model is analyzing the data)
    learning_rate=0.0001
    #y=mx+b(slope)
    initial_b=0
    initial_m=0

if __name__ == '__main__':
    run()