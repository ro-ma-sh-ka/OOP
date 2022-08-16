class Zebra:
    def which_stripe(self):
        if hasattr(self, 'color') == False:
            setattr(self, 'color', ['Полоска белая', 'Полоска черная'])
        print(self.color[0])
        self.color[0], self.color[1] = self.color[1], self.color[0]


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()