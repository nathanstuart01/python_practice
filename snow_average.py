import numpy as np

snow70s = [481,466,496,595,605,439,314,524,488,514]
snow80s = [391,696,637,743,457,599,381,410,581,448]
snow90s = [580,395,650,490,745,562,599,574,458,446]
snow20s = [469,567,399,570,553,633,356,654,578,430]
snow21s = [553,329,382,357,267,393]

# Make average of yearly snowfall for all areas in PNW/Utah/Jackson
# Take stan dev of yearly snowfall and determine the swing in each year 

def snow_averager(array1,array2,array3,array4,array5):
    snow70 = np.average(array1)
    snow80 = np.average(array2)
    snow90 = np.average(array3)
    snow20 = np.average(array4)
    snow21 = np.average(array5)

    print("The average snowfall at Alta in the 70's was " + str(snow70) + " inches.")
    print("The average snowfall at Alta in the 80's was " + str(snow80) + " inches.")
    print("The average snowfall at Alta in the 90's was " + str(snow90) + " inches.")
    print("The average snowfall at Alta in the 20's was " + str(snow20) + " inches.")
    print("The average snowfall at Alta in the 21's was " + str(snow21) + " inches.")


snow_averager(snow70s, snow80s, snow90s, snow20s, snow21s)
	