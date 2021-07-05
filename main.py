# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
b500, b200, b100, b50, b20, b10, b5 = 500, 200, 100, 50, 20, 10, 5
m2, m1, m50, m20, m10, m5, m02, m01 = 2, 1, .5, .2, .1, .05, .02, .01

dishes = ["Ensalada China", "Rollito Primavera", "Pan Chino", "Patatas Fritas", "Arroz Tres Delicias",
          "Arroz Chao La Fan", "Cerdo Agridulce", "Ternera Bambú y Setas", "Pato Pekín", "Pato con Piña"]
prices = [4.7, 1.5, 1.5, 3.2, 5.15, 6.45, 6.5, 6.7, 15.45, 8.7]
if len(dishes) != len(prices):
    raise Exception("Check menu: different number of dishes and prices")

total = round(0, 2)
command = []


def take_away():
    global command, total
    while True:
        for index, name in enumerate(dishes, start=1):
            print("%d: %s" % (index, name))

        print("\nTotal hasta ahora: %f" % round(total, 2))
        new = int(input("Seleccione plato: "))
        command.append(dishes[new - 1])
        total += prices[new - 1]
        check_order = int(input("¿Quiere pedir más platos? (1:sí, 0:no) "))
        if check_order == 1:
            continue

        print("\n\nEste es su pedido:\n")
        for dish in command:
            print(dish)
        print("\nTotal a pagar: %f" % round(total, 2))
        print("Esto equivale a ", print_bill())
        break


def print_bill():
    global total
    rest = round(total, 2)
    bill = ""

    while rest > 0:
        if rest >= b500:
            num = int(rest // b500)
            rest = round(rest % b500, 2)
            bill += "%d billetes de 500 euros, " % num
        if rest >= b200:
            num = int(rest // b200)
            rest = round(rest % b200, 2)
            bill += "%d billetes de 200 euros, " % num
        if rest >= b50:
            num = int(rest // b50)
            rest = round(rest % b50, 2)
            bill += "%d billetes de 50 euros, " % num
        if rest >= b20:
            num = int(rest // b20)
            rest = round(rest % b20, 2)
            bill += "%d billetes de 20 euros, " % num
        if rest >= b10:
            num = int(rest // b10)
            rest = round(rest % b10, 2)
            bill += "%d billetes de 10 euros, " % num
        if rest >= b5:
            num = int(rest // b5)
            rest = round(rest % b5, 2)
            bill += "%d billetes de 5 euros, " % num
        if rest >= m2:
            num = int(rest // m2)
            rest = round(rest % m2, 2)
            bill += "%d monedas de 2 euros, " % num
        if rest >= m1:
            num = int(rest // m1)
            rest = round(rest % m1, 2)
            bill += "%d monedas de 1 euros, " % num
        if rest >= m50:
            num = int(rest // m50)
            rest = round(rest % m50, 2)
            bill += "%d monedas de 50 céntimos, " % num
        if rest >= m20:
            num = int(rest // m20)
            rest = round(rest % m20, 2)
            bill += "%d monedas de 20 céntimos, " % num
        if rest >= m10:
            num = int(rest // m10)
            rest = round(rest % m10, 2)
            bill += "%d monedas de 10 céntimos, " % num
        if rest >= m5:
            num = int(rest // m5)
            rest = round(rest % m5, 2)
            bill += "%d monedas de 5 céntimos, " % num
        if rest >= m02:
            num = int(rest // m02)
            rest = round(rest % m02, 2)
            bill += "%d monedas de 2 céntimos, " % num
        if rest >= m01:
            num = int(rest // m01)
            rest = round(rest % m01, 2)
            bill += "%d monedas de 1 céntimos, " % num

    return bill


if __name__ == '__main__':
    take_away()
