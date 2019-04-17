from Board import Board

def test_blank_board_print():
    board = Board()
    board.PRINT_CANVAS()

def test_board_full_layer_print():
    board = Board()
    x_len, y_len = board.size
    for y in range(y_len):
        for x in range(x_len):
            board.layers[0][y][x] = x
    board.PRINT_CANVAS()

def test_board_two_layer_print():
    board = Board()
    board.add_layer()
    x_len, y_len = board.size
    for y in range(y_len):
        for x in range(x_len):
            board.layers[0][y][x] = x
    for y in range(y_len):
        for x in range(x_len):
            if x % 2 == 0:
                board.layers[1][y][x] = "X"
    board.PRINT_CANVAS()

def test_draw_rect():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.PRINT_CANVAS()

def test_draw_two_rect():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.DRAW_RECTANGLE("R",2,1,4,4)
    board.PRINT_CANVAS()

def test_erase_area():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.DRAW_RECTANGLE("R",2,1,4,4)
    board.PRINT_CANVAS()
    board.ERASE_AREA(3,2,3,3)
    board.PRINT_CANVAS()

def test_drag_rect():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.DRAW_RECTANGLE("R",2,1,4,4)
    board.PRINT_CANVAS()
    board.ERASE_AREA(3,2,3,3)
    board.DRAW_RECTANGLE('#',1,3,8,4)
    board.DRAG_AND_DROP(2,2,6,2)
    board.PRINT_CANVAS()

def test_bring_to_front():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.DRAW_RECTANGLE("R",2,1,4,4)
    board.PRINT_CANVAS()
    board.ERASE_AREA(3,2,3,3)
    board.DRAW_RECTANGLE('#',1,3,8,4)
    board.DRAG_AND_DROP(2,2,6,2)
    board.BRING_TO_FRONT(1,2)
    board.BRING_TO_FRONT(6,2)
    board.PRINT_CANVAS()

def test_select_through_erase():
    board = Board()
    board.DRAW_RECTANGLE("L",1,1,4,4)
    board.DRAW_RECTANGLE("R",2,1,4,4)
    board.PRINT_CANVAS()
    board.ERASE_AREA(3,2,3,3)
    board.DRAW_RECTANGLE('#',1,3,8,4)
    board.DRAG_AND_DROP(2,2,6,2)
    board.BRING_TO_FRONT(1,2)
    board.BRING_TO_FRONT(6,2)
    board.DRAG_AND_DROP(3,3,3,2)
    board.PRINT_CANVAS()
