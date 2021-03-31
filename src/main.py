
from functions import *


def main():
    create_20_random_puzzles()

    goal_state = read_state(get_goal_state())

    puzzles = [read_state(x) for x in get_all_puzzles()]

    test_Astar_on_puzzles(goal_state, puzzles)
    test_dfs_on_puzzles(goal_state, puzzles)
    test_iter_deepening_on_puzzles(goal_state, puzzles, 100)

    # testing()


def test_Astar_on_puzzles(goal: tuple, puzzles: list) -> None:
    """ Runs the A* algorithm on all puzzles using each heuristic.

    The heuristics we use are: sum permutation, Hamming distance, and a
    modified version of the Manhattan distance.
    :param goal: The goal state
    :param puzzles: All the puzzles being solved
    :return: None
    """
    print("------------")
    print("A* ALGORITHM")
    print("------------")

    for idx, puzzle in enumerate(puzzles, 1):
        print("\nPuzzle " + str(idx) + ":\n")
        # Test A* using all heuristics
        start = puzzle

        start_state = PuzzleState(start, 0)
        goal_state = PuzzleState(goal, 0)
        heuristics = [PuzzleState.sum_permutation, PuzzleState.hamming_distance, PuzzleState.manhattan_distance]
        print("start:", start_state)
        print("goal:", goal_state)

        for heuristic in heuristics:
            print(heuristic.__name__, "path")
            closed_list, search_list, elapsed = PuzzleState.a_star(start_state, goal_state, heuristic)

            output_to_files("A_Star", idx, search_list, closed_list, elapsed, heuristic=heuristic.__name__)

            if elapsed > 60.0:
                print("no solution")
            else:
                for index, state in enumerate(search_list):
                    print(state, state.level)
                print("Time taken: " + str(elapsed))


def test_dfs_on_puzzles(goal: tuple, puzzles: list) -> None:
    """ Runs the DFS algorithm on all puzzles

    :param goal: The goal state
    :param puzzles: All the puzzles being solved
    :return: None
    """
    print("----------------------------")
    print("DEPTH-FIRST SEARCH ALGORITHM")
    print("----------------------------")

    for idx, puzzle in enumerate(puzzles, 1):
        print("\nPuzzle " + str(idx) + ":\n")
        # Depth-First Search
        start = puzzle

        start_state = PuzzleState(start, 0)
        goal_state = PuzzleState(goal, 0)
        print("start:", start_state)
        print("goal:", goal_state)

        dfs_solution_path, dfs_search_path, elapsed = PuzzleState.depth_first_search(start_state, goal_state)
        
        output_to_files("DFS", idx, dfs_search_path, dfs_solution_path, elapsed)

        if elapsed > 60:
            print("no solution")
        else:
            print("search path:")
            for index, state in enumerate(dfs_search_path):
                print(state, state.level)
            print("solution path:")
            print_solution_path(dfs_solution_path)
            print("Time taken: " + str(elapsed))


def test_iter_deepening_on_puzzles(goal: tuple, puzzles: list, max_depth: int) -> None:
    """ Runs the DFS algorithm with iterative deepening on all puzzles

    :param goal: The goal state
    :param puzzles: All the puzzles being solved
    :param max_depth: The maximum depth to search to before concluding that there is no solution
    :return: None
    """
    print("-----------------------------")
    print("ITERATIVE DEEPENING ALGORITHM")
    print("-----------------------------")

    for idx, puzzle in enumerate(puzzles, 1):
        print("\nPuzzle " + str(idx) + ":\n")
        # Iterative Deepening
        start = puzzle

        start_state = PuzzleState(start, 0)
        goal_state = PuzzleState(goal, 0)
        print("start:", start_state)
        print("goal:", goal_state)

        iter_solution_path, iter_search_path, elapsed = PuzzleState.iterative_deepening(start_state, goal_state, max_depth)

        output_to_files("Iter_Deepening", idx, iter_search_path, iter_solution_path, elapsed)

        if elapsed > 60:
            print("no solution")
        else:
            print("search path:")
            for index, state in enumerate(iter_search_path):
                print(state, state.level)
            print("solution path:")
            print_solution_path(iter_solution_path)
            print("Time taken: " + str(elapsed))


if __name__ == '__main__':
    main()
