
class Board:
    def __init__(self, MAX_X = 10, MAX_Y = 6):
        self.size = (MAX_X, MAX_Y)
        self.layers = []
        self.layers.append(self._new_layer())


    def _new_layer(self):
        x_len, y_len = self.size
        return [[None for i in range(x_len)] for j in range(y_len)]

    # TODO move to private
    def add_layer(self):
        self.layers.append(self._new_layer())

    def _find_top(self, select_x, select_y):
        top_layer = None
        top_layer_i = -1
        for i, layer in enumerate(self.layers):
            if layer[select_y][select_x] is not None:
                top_layer = layer
                top_layer_i = i
        return (top_layer, top_layer_i)

    def DRAW_RECTANGLE(self, fill, left_x, top_y, right_x, bottom_y):
        self.add_layer()
        layer = self.layers[-1]
        x_len, y_len = self.size
        for y in range (top_y, bottom_y + 1):
            for x in range(left_x, right_x + 1):
                layer[y][x] = fill

    def PRINT_CANVAS(self):
        print(self)

    def ERASE_AREA(self, left_x, top_y, right_x, bottom_y):
        for layer in self.layers:
            for y in range (top_y, bottom_y + 1):
                for x in range(left_x, right_x + 1):
                    layer[y][x] = None

    def DRAG_AND_DROP(self, select_x, select_y, release_x, release_y):
        # Find top layer at index x,y
        top_layer, top_layer_i = self._find_top(select_x, select_y)

        # Move top layer over
        offset_x = release_x - select_x
        offset_y = release_y - select_y
        x_len, y_len = self.size
        new_layer = self._new_layer()
        for y in range(y_len):
            for x in range(x_len):
                old = top_layer[y][x]
                new_x = x + offset_x
                new_y = y + offset_y
                if new_x < x_len and new_y < y_len:
                    new_layer[new_y][new_x] = old

        # Put new layer instead of old layer
        self.layers[top_layer_i] = new_layer

    def BRING_TO_FRONT(self, select_x, select_y):
        top_layer, top_layer_i = self._find_top(select_x, select_y)
        if top_layer_i >= 0:
            del self.layers[top_layer_i]
            self.layers.append(top_layer)

    def __str__(self):
        x_len, y_len = self.size
        output = self._new_layer()
        # Find winning char for every layer
        for layer in self.layers:
            for y in range(y_len):
                for x in range(x_len):
                    if layer[y][x] is not None:
                        output[y][x] = layer[y][x]
        # Prepare output string
        output_str = "\nBoard is:\n\n"

        # Add x index
        output_str += "  "
        for x in range(x_len):
            output_str += str(x)
        output_str += "\n\n"

        for y in range(y_len):
            output_str += str(y) + " " # Add Y index
            for x in range(x_len):
                if output[y][x] is None:
                    output_str += " "
                else:
                    output_str += str(output[y][x])
            output_str += "\n"
        return output_str

