from tqdm import trange


input = """...#....#................................#..........................#..........#.............#..#.................................
.......#........................#.......#......................#............#.....................................................
..#......#....................................................................................#.......#................#..........
..................#...........#...#..#............................#.........#...................#...............................#.
..#...................................................................................................................#....#......
............#.............................#......................#.......#...........#..................##..............#.........
..............................#................................................#.............................................#....
....................#.#...........#...#....#..............#.........#.........#..................#...........#.................#..
.#........................................................................#.....#.......##.....................#..................
.#........................#..................................#............................#...#..........#.......#.............#..
................................#......#...............#...........................#.............................#..#.#...#....#..
..........................................................#..........#..#.......#........#............#.................#.........
......#.......#......................................................................................#................#...........
##......#...................................................#................#............................#.......................
.....#.................................................................#.....................#...............................#...#
...........................................................................................................#......................
........#......................#..........#..#....#....................#..##...........#..#.............................#.#......#
#...#..................#.....................#...#...#.......................................................#.....#..............
#...#..................#.#....#...............#...........#...................#.....##......................................#.....
......#............................................................................................#...#.#........................
......................................................#..............#.....#.....#..#...........#..............................#..
.........................##.#..............#............#....................................................................##...
..#....................#...........................................................................................#......#.##....
..............#........#..#.......#................#.....#.......................................................................#
.........#..........................#........#..........#...............#...................................#.............#.......
...........#.....................#.....#..............#......#.........................................#..........................
.......##.............................#.........#...............#...............#..............................................#..
.......#.....#.....#...........#............................................................................#..............#.....#
....#.............................................#....#....#....#...........................................##..............##...
.#.............#.......#.....#.........#....#......#.............#............#......#............#......................#........
..................................................................................................#....#..........................
.............................................#....................#...............................#.............#.................
.........#...............#.....................#...............#......#.................................................#.........
..........#.................................................................................#..............#..............#.....#.
.........................#........#.....#............#.....................#.......................................#..............
.....................#.....................#..............................#..................................#..........#.........
........................#.....................#..............................#.#................#.................................
.....................................................#...............#.......................................................#....
.................#.......#......##..............................##.................#..........................#....#....#........#
.............................#................................#..#...........#..........#.........................................
.#...........................#........#.#...#...#....#......#......#...........#..................##.........................#....
.......................................#......................................#................................................#..
..........##......#..............................................................#.......#....................#..#......#.........
.#...............#............#....#....................................^......#.........................................#.#......
.................#....................#..#....#.......................#.............................#.....#.....#............#....
...............................................................#...............##.................#........#.#....................
...................................#..#.........#.........#...............#.........#.......................................#.....
.........................#......................................................................................#............#....
.................................#............#............#.............................#........................................
..........#.........#...........................................#..#...#..#.......................................................
.#....#....#..........................................#.....#..........................................................#..........
...#...............#......................................................................#.............................#.........
....#......................#...........#......................................#..............#...........................#........
.......................................................#...........#.......#..............................#.......................
......#............#.#...........#............#...................#..................#................................##..........
.......#..........................................................................................#.....................##........
....................................#.........#..................##....................#.#...........#......................#.....
.........................#...............................................................#....................#...................
...............................#........................................................................#....................#....
..#.#.......................................................................#..........#.........#........#.......................
....#....#.....................#.............#..#........................#.............#.....#....................................
..#............................................................................#....................#.................#.....#.#...
..............................................#........#............##.#..............#...#...................#...................
.............................#..................#..................#.................................#............................
......#................................#....#..................................#............#.....................................
#..........#...#..................#...............................................................................................
......................................#......................................#.......#....#.......................................
......................................................................#......................................#...........##.....#.
.......#.............#................................................#.....#..#......#......................................#....
..........................................#...............#...#........#..........................................................
#..#......#..........#....#.......................................................................................................
.......#..#............................................................#........#...#.#...........................................
.#....#...#..#................................................#......................#............................................
.........................#...........#..........#............#...............................#...#...#..................#.........
....#......................#......#.......#....................#..........................#...............................#.......
.........................#...............#.........................#.........#..................................#.................
...............................#......................................................#...........................................
..................................................#.........................#...................#......#..........................
...................#.##..............................#................#........#..............................#...................
.#.................#..............................#................#............................#............#................#...
............#..............#....................................#.....#.....#..........#................#.........................
...................#.............................#...........##...........................................#.......................
.#.............##...........#............##...#.........................................................................#.......#.
........#................#....................#..........#....#.......#.#..............#..............#.................#.........
............................#..#...#..........................................................#......#............................
.........#.................#......#.............................................#...##.....#.................................##...
............#..........................................................................#..........#...................#...........
....................................#.............#............#..................#....#.#.......................#...#............
......#...................................................##....................................................................#.
...............................#.............#.#...............#.......................................#.#.......................#
..........#............................#....#.#.#.#..............................................................#................
....#...#............#.#.................................................#.....................................#.#................
...........#...............................##.........#............#.....................#........................................
...................#.............................#.........#..............................................#.....#.................
.........#................#.........#.............#.............#...#...........................................................#.
.....#...........................#............##............#................#...............................#.............#..#...
................#.#.......#.................#...................................................#.........#..........##.#.........
.........................#.................#...............#...........................#............#.............#..............#
...................#......#...........................#.....#.....................................................#...............
......#...........##......#..................#......#............##................................#..............................
....................#.........#...........................................................................................#....#..
................................................#....#.....#..#........................#....................##....................
........#...........#....#.......#..........##............................................#.......#.........#...#...............#.
#.#.....#.#..............................................#...#...............#..........#................##.........#..........#.#
#........................#...#.........#........#..............................................................#..................
..................................................................................................................................
...........................................#..#..........................................#...................#....................
...................#.............#.....#..................................................#...................................#...
................#...........................................................................#.#...#...............................
........#.......#......#...........................................#....................................#......#............#.....
...............#.......#....................#.....................................................................#...............
..............##....#.............................#......................#.....#......#........................................#..
............................#.........#.....................#.....................................................................
#....................#...................##........#...#........#......#....#..........................................#.#.......#
..#............#...#...............................#.#....................#....................................#..............#...
..................#..#.......#......#.....#.......#.................#.....#...................................#.............#.....
.......................#..............#.........#............#.......#.................................................#.....#....
................#.....................................................#.#.............................#.........#...........#.....
......................#.................................##..................................#.................................#...
.......................................#........................................................................#.................
.........#...........#..............#......................#................................#..#.......................#..........
...................#..................#...#....#......................................................#...........................
..............................#.........#................................#............................#...........................
........#....#...................................................................##........#......................................
..................................#...................#...................#.#.......#.............#..............................#
.....................................#...##...............................................................................#.......
......................#.......#.............#.......................#..#.....#......................#.................#...........
.....##...........#.......#................#.................................#...##......#......#...............#.......#.#.......
.....#...#...............#......................#........#..........#..##...#...#........#..........#.............................
#...........#.............#...............................#..............................#...#.#........#........................."""


maze = [list(row.strip()) for row in input.split('\n')]

N, M = len(maze), len(maze[0])

guard = (0, 0)
for i in range(N):
    for j in range(M):
        if maze[i][j] == '^':
            guard = (i, j)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_in_loop(maze, guard=guard):
    current_dir = 0
    visited = set()

    while True:
        visited.add((guard, current_dir))
        next_guard = (guard[0] + dirs[current_dir][0], guard[1] + dirs[current_dir][1])
        if next_guard[0] < 0 or next_guard[0] >= N or next_guard[1] < 0 or next_guard[1] >= M:
            return False
        if maze[next_guard[0]][next_guard[1]] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            guard = next_guard
        if (guard, current_dir) in visited:
            return True


count = 0
for r in trange(N):
    for c in range(M):
        if maze[r][c] != '#' and (r, c) != guard:
            maze[r][c] = '#'
            if is_in_loop(maze):
                count += 1
                maze[r][c] = 'O'
            else:
                maze[r][c] = '.'

for row in maze:
    print(''.join(row))
print(count)
