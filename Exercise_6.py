class Product:
    """
    creates a product object with a name and a price
    """
    def __init__(self, product, price: int | float):
        if not isinstance(price, (int, float)):
            raise TypeError('price must be a number')
        if price < 1:
            raise 'NegativePrice(product)'
        self.product = product
        self.price = price

    def __str__(self):
        return f'{self.product}: {self.price} UAH/KG'


class Buyer:
    """
    stores information about the buyer, name, surname, order
    delivery address, telephone number for communication.
    """
    def __init__(self, name, surname, phone: int, address):
        if not isinstance(phone, int):
            raise TypeError('phone number must contain numbers')
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.name} {self.surname}, +{self.phone}, {self.address}'


class Order:
    """
    creates an order object with the date and time of creation,
    as well as information about the buyer, implements methods
    for adding products to the list and their default quantity
    in the amount of 1 product, calculating the sum of the cost
    of all products in the order.
    """

    def __init__(self, data, time, buyer: Buyer):
        if not isinstance(buyer, Buyer):
            raise TypeError
        self.data = data
        self.time = time
        self.buyer = buyer
        self.products = {}

    def __iter__(self):
        return My_seq_iterator(self.products)

    def __getitem__(self, item):
        if isinstance(item, int):
            if -len(self.products) <= item < len(self.products):
                return [list(self.products)[item], self.products.get(list(self.products)[item])]
            raise IndexError('Index error')
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or len(self.products)
            step = item.step or 1

            if stop > len(self.products) or \
                    (step > 0 and start > stop) or \
                    (step < 0 and start < stop):
                raise IndexError('Index Error')
            res = []
            for i in range(start, stop, step):
                res.append(self[i])
            return res
        raise IndexError('IndexError')

    def add_cart(self, value: Product, count=1):
        if not isinstance(value, Product):
            raise TypeError('value is not Product')
        if not isinstance(count, int):
            raise TypeError('entered something wrong ')
        if self.products.get(value):
            self.products[value] += count
        else:
            self.products[value] = count

    def summa_order(self):
        summa = 0
        for item, count in self.products.items():
            summa += item.price * count
        return summa

    def __str__(self):
        res = f'{self.data} {self.time}\n{self.buyer}\n'
        for product, count in self.products.items():
            res += f'{product}\n x {count} = {product.price * count}\n'
        return res


class My_seq_iterator:
    """
    class iterator overload Order
    Takes a dictionary, returns the next iterator of the dictionary.
    """

    def __init__(self, seq):
        self.seq = seq
        self.list = list(seq)
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self.seq.get(self.index)

    def __next__(self):
        if self.index < len(self.seq):
            self.index += 1
            return [self.list[self.index - 1], self.seq.get(self.list[self.index - 1])]
        raise StopIteration


try:
    bread = Product('bread', 22)
    milk = Product('milk', 34)
    cola = Product('cola', 12)
    meat = Product('meat', 145)

    buyer_1 = Buyer('Максим', 'Сергеевич', 380777223312, 'ул.Новая 56')
    buyer_2 = Buyer('Андрей', 'Николаевич', 380563843803, 'ул.Франка 70')

    order_1 = Order('22/09/2022', '18:30', buyer_1)
    order_1.add_cart(milk, 2)
    order_1.add_cart(bread)
    order_1.add_cart(milk)
    order_1.add_cart(cola)
    order_1.add_cart(meat)

    print(order_1)
    print(f'  Total {order_1.summa_order()} UAH\n')

    for pr in order_1[:3]:
        print(pr[0], 'x', pr[1])

    print(order_1[0][0])


except Exception as error:
    print(error)
