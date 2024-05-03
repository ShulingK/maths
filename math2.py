import numpy as np
import matplotlib.pyplot as plt

def hermite_interpolation(x_values, y_values, derivative_values, num_points=100):
   

    interpolated_x = []
    interpolated_y = []

    for i in range(len(x_values) - 1):
        start_x, end_x = x_values[i], x_values[i + 1]
        start_y, end_y = y_values[i], y_values[i + 1]
        start_derivative, end_derivative = derivative_values[i], derivative_values[i + 1]

        for t in np.linspace(0, 1, num_points):
            # Calcul des valeurs interpolées
            hermite_term1 = (2*t**3 - 3*t**2 + 1) * start_y
            hermite_term2 = (t**3 - 2*t**2 + t) * (end_x - start_x) * start_derivative
            hermite_term3 = (-2*t**3 + 3*t**2) * end_y
            hermite_term4 = (t**3 - t**2) * (end_x - start_x) * end_derivative

            interpolated_x.append(start_x + (end_x - start_x) * t)
            interpolated_y.append(hermite_term1 + hermite_term2 + hermite_term3 + hermite_term4)

    # Relier le dernier point avec le premier point
    start_x, end_x = x_values[-1], x_values[0]
    start_y, end_y = y_values[-1], y_values[0]
    start_derivative, end_derivative = derivative_values[-1], derivative_values[0]

    for t in np.linspace(0, 1, num_points):
        # Calcul des valeurs interpolées
        hermite_term1 = (2*t**3 - 3*t**2 + 1) * start_y
        hermite_term2 = (t**3 - 2*t**2 + t) * (end_x - start_x) * start_derivative
        hermite_term3 = (-2*t**3 + 3*t**2) * end_y
        hermite_term4 = (t**3 - t**2) * (end_x - start_x) * end_derivative

        interpolated_x.append(start_x + (end_x - start_x) * t)
        interpolated_y.append(hermite_term1 + hermite_term2 + hermite_term3 + hermite_term4)

    return interpolated_x, interpolated_y

x_values=[]
y_values=[]
derivative_values=[]
# Points de données relevés graphiquement
point_values_input = input("Rentrez le nombre de points voulus")

num_points = int(point_values_input)



for i in range (num_points):
   

    x_values_input = input("Rentrez le point numero {} en x :".format(i + 1))
    x_values.append(float(x_values_input))

    y_values_input = input("Rentrez le point numero {} en y :".format(i + 1))
    y_values.append(float(y_values_input))

    derivative_values_input = input("Rentre la dérivées numero {}:".format(i+1))
    derivative_values.append(float(derivative_values_input))



# Interpolation d'Hermite
interpolated_x, interpolated_y = hermite_interpolation(x_values, y_values, derivative_values)

# Tracer les données et l'interpolation
plt.plot(x_values, y_values, 'bo', label='Points de données')
plt.plot(interpolated_x, interpolated_y, 'r-', label='Interpolation d\'Hermite')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation d\'Hermite ')
plt.legend()
plt.grid(False)
plt.axis('equal')  # Pour que les axes aient la même échelle
plt.show()
