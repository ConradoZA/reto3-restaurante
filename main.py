# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
b500, b200, b100, b50, b20, b10, b5 = 500, 200, 100, 50, 20, 10, 5
m2, m1, m50, m20, m10, m5 = 2, 1, .5, .2, .1, .05
total = 0

dishes = ["Ensalada China", "Rollito Primavera", "Pan Chino", "Patatas Fritas", "Arroz Tres Delicias",
          "Arroz Chao La Fan", "Cerdo Agridulce", "Ternera Bambú y Setas", "Pato Pekín", "Pato con Piña"]
prices = [4.7, 1.5, 1.5, 3.2, 5.15, 6.45, 6.5, 6.7, 15.45, 8.7]
if len(dishes) != len(prices):
    raise Exception("Check menu: different number of dishes and prices")


if __name__ == '__main__':
    print('PyCharm')
