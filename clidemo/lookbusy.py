import numpy as np
import argparse
import matplotlib.pyplot as plt
from time import sleep

# Create fake data
fake_data = np.random.random((1024))

# Make and show plot of data
def make_plot(user_args):
    fig = plt.figure(figsize=(12, 10))
    ax = plt.subplot(1, 1, 1)
    plt.suptitle(args.title)
    ax.plot(fake_data)
    ax.plot(fake_data + 5)
    ax.set_ylabel(args.ytitle)
    ax.set_xlabel(args.xtitle)
    plt.show()

# Fake long complex calculation
def calculation():
    x_vals = np.arange(1, 100)
    for i, val in enumerate(x_vals):
        print(f'Timestep {i} - Result {2 ** val}')
        sleep(0.01)

if __name__ == '__main__':
    #Create parser

    parser = argparse.ArgumentParser(description='Make sure I look busy.',
                                     epilog='Use Example: lookbusy')

    parser.add_argument('-title', required=False, type=str,
                        help='Set the title of the plot',
                        default='Future Oil Prices')

    parser.add_argument('-xtitle', required=False, type=str,
                        help='Set the X axis title',
                        default='Time')

    parser.add_argument('-ytitle', required=False, type=str,
                        help='Set the y axis title',
                        default='number')

    args = parser.parse_args()

    make_plot(args)
    calculation()