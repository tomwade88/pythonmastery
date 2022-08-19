class Layers:
    def __init__(self, layers, label=None):
        self.layers = layers
        self.label = label or "MyLog"

    def __len__(self):
        return len(self.layers)

    def __str__(self):
        return "Layers({} layers)".format(len(self.layers))

    def __repr__(self):
        return "Layers(layers={}, label={})".format(self.layers.__repr__(), self.label)

layers = [1, 2, 3, 4, 5, 6]

l = Layers(layers, "monkey-1")


