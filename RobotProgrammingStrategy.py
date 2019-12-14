def win_robot_tournament(opponent_programs):
    # Paper beats rock, scissor beats paoer and rock beats scissor
    # Opponents move is the key, our robot picks the value as the
    # move in that case
    robot_choices = {'R': 'P', 'P': 'S', 'S': 'R'}

    # Result of robot choices
    robot_program = ''

    # Oopponent's next move index
    opponents_move_pointer = [0] * len(opponent_programs)

    # While there is at least one opponent, keep eliminating
    # the opponents after finding the code to beat them
    while len(opponent_programs) > 0:

        # Best case scenario: opponents with the same move
        first_move = opponent_programs[0][opponents_move_pointer[0]]
        second_move = 'no_move'

        # Get all opponents' current moves to decide the best
        # move for our robot
        for i in range(1, len(opponent_programs)):

            # Find each opponent's current move
            move = opponent_programs[i][opponents_move_pointer[i]]
            if move == first_move:
                continue
            # Second move exists
            elif second_move == 'no_move':
                second_move = move
            # Two moves are accepted
            elif move == second_move:
                continue
            # Third move found, thus impossible to beat
            else:
                return "IMPOSSIBLE"

        # Choose robot's current move based on opponents' moves
        if second_move == 'no_move':
            robot_move = robot_choices[first_move]
        else:
            robot_move = ({first_move, second_move} & {robot_choices[first_move], robot_choices[second_move]}).pop()

        opponents_in_running = []
        opponents_in_running_moves = []
        # Eliminate opponent's based on the robot's move
        for i in range(len(opponent_programs)):
            move_index = opponents_move_pointer[i]
            move = opponent_programs[i][move_index]
            # If the robot move defeats this opponent's move
            # Mark next move pointer -1 so as to eliminate
            if robot_choices[move] == robot_move:
                continue
            elif move == robot_move:
                opponents_in_running.append(opponent_programs[i])
                opponents_in_running_moves.append((move_index + 1) % len(opponent_programs[i]))

        # Append this round's robot choice to result
        robot_program += robot_move
        # Update the opponents for next rounds
        opponent_programs = opponents_in_running
        opponents_move_pointer = opponents_in_running_moves

    return robot_program


def main():
    T = int(input())

    case_num = 1
    for _ in range(T):
        A = int(input())
        robot_programs = []
        for i in range(A):
            robot_programs.append(input())

        beating_program = win_robot_tournament(robot_programs)
        print("Case #%s: %s" % (case_num, beating_program))
        case_num += 1


if __name__ == '__main__':
    main()
