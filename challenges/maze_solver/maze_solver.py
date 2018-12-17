import png
import sys


# maze_matrix_example = [['False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False'], ['False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False'], ['False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False'], ['False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'False'], ['False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'True', 'True', 'False'], ['False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'False'], ['False', 'True', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False'], ['False', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'False'], ['False', 'False', 'False', 'True', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'True', 'False', 'True', 'False'], ['False', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'False', 'True', 'False', 'True', 'False', 'True', 'False'], ['False', 'True', 'False', 'False', 'False', 'True', 'False', 'True', 'False', 'True', 'False', 'True', 'False', 'True', 'False'], ['False', 'True', 'False', 'True', 'True', 'True', 'False', 'True', 'False', 'True', 'False', 'False', 'False', 'False', 'False'], ['False', 'True', 'False', 'True', 'False', 'False', 'False', 'True', 'False', 'True', 'False', 'True', 'True', 'True', 'False'], ['False', 'True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'False', 'True', 'False'], ['False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False']]



class Node():
    def __init__(self, neighbors, coord):
        self.prev = None
        self.weight = math.inf
        self.neighbors = neighbors
        self.coord = coord





def maze_solve(input_maze):

    try:
        maze_obj = png.Reader(filename=input_maze).asDirect()
    except:
        raise FileNotFoundError

    graph_coords = []
    maze_matrix = []
    start_end_coords = []

    end_maze_matrix = []

    for row in maze_obj[2]:
        row = list(row)[::3]
        for index, pixel in enumerate(row):
            if pixel < 100:
                row[index] = False
            else:
                row[index] = True
        maze_matrix.append(row)

    for row_ind, row in enumerate(maze_matrix):
        for col_ind, pixel in enumerate(row):
            if pixel is True:
                try:
                    if maze_matrix[row_ind - 1][col_ind] is True:
                        if maze_matrix[row_ind + 1][col_ind] is False:
                            graph_coords.append((row_ind, col_ind))
                        else:
                            if maze_matrix[row_ind][col_ind - 1] is True:
                                if maze_matrix[row_ind][col_ind + 1] is True:
                                    graph_coords.append((row_ind, col_ind))
                                else:
                                    graph_coords.append((row_ind, col_ind))
                            elif maze_matrix[row_ind][col_ind + 1] is True:
                                graph_coords.append((row_ind, col_ind))
                    elif maze_matrix[row_ind + 1][col_ind] is True:
                        if maze_matrix[row_ind - 1][col_ind] is False:
                            graph_coords.append((row_ind, col_ind))
                    elif maze_matrix[row_ind][col_ind - 1] is True:
                        if maze_matrix[row_ind][col_ind + 1] is False:
                            graph_coords.append((row_ind, col_ind))
                    elif maze_matrix[row_ind][col_ind + 1] is True:
                        if maze_matrix[row_ind][col_ind - 1] is False:
                            graph_coords.append((row_ind, col_ind))

                except:
                    # This is the start or end, as these pixels are on the border and raise an index error
                    start_end_coords.append((row_ind, col_ind))


    for coord in graph_coords:
        maze_matrix[coord[0]][coord[1]] = 'Node'

    for row in maze_matrix:
        new_row = []
        for pixel in row:
            if pixel == 'Node':
                new_row += [60, 255, 112]
            elif pixel is True:
                new_row += [255,255,255]
            elif pixel is False:
                new_row += [0,0,0]
        end_maze_matrix.append(new_row)

    maze_with_nodes =  png.from_array(end_maze_matrix, 'RGB').save('new_maze.png')






def main():
    if len(sys.argv) != 2:
        print("Usage: python3 maze_solver.py maze_file.png")
        sys.exit(1)

    input_maze = sys.argv[1]

    maze_solve(input_maze)

if __name__ == '__main__':
    main()

