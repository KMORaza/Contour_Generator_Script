import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def generate_3d_contours():
    variable_x = input("Write variable for x-axis: ")
    variable_y = input("Write variable for y-axis: ")
    expression = input("Write mathematical expression (use {} for variables): ")
    x_min = float(input("Write minimum value for x-axis: "))
    x_max = float(input("Write maximum value for x-axis: "))
    y_min = float(input("Write minimum value for y-axis: "))
    y_max = float(input("Write maximum value for y-axis: "))
    num_contours = int(input("Write number of contour levels: "))
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    x, y = np.meshgrid(x, y)
    z = eval(expression.format(variable_x, variable_y))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    contour_plot = ax.contour3D(x, y, z, num_contours, cmap='viridis')
    fig.colorbar(contour_plot, ax=ax, label='Function Value')
    ax.set_xlabel(variable_x)
    ax.set_ylabel(variable_y)
    ax.set_zlabel('Function Value')
    ax.set_title('3D Contour')
    plt.show()
if __name__ == "__main__":
    generate_3d_contours()
