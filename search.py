# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # create a frontier stack
    frontier = util.Stack()
    # create an explored set
    explored = set()
    # push the start state of the problem and path
    start = (problem.getStartState(), [])
    frontier.push(start)

    # loop until the frontier is empty
    while not frontier.isEmpty():
        # pop the state and path from the frontier stack
        (state, path) = frontier.pop()

        # if this state is goal return the path
        if problem.isGoalState(state):
            return path
        # check if this state is not in the explored set
        if not state in explored:

            # add it to explored set
            explored.add(state)

            # iterate through all the children and put them on the frontier stack
            for (child, child_path, child_cost) in problem.getSuccessors(state):
                new_path = path + [child_path]
                new_node = (child, new_path)
                frontier.push(new_node)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # create a frontier queue
    frontier = util.Queue()
    # create an explored set
    explored = set()
    # push the start state of the problem and path
    start = (problem.getStartState(), [])
    frontier.push(start)

    # loop until the frontier is empty
    while not frontier.isEmpty():
        # pop the state and path from the frontier queue
        (state, path) = frontier.pop()

        # if this state is goal return the path
        if problem.isGoalState(state):
            return path
        # check if this state is not in the explored set
        if not state in explored:

            # add it to explored set
            explored.add(state)

            # iterate through all the children and put them on the frontier queue
            for (child, child_path, child_cost) in problem.getSuccessors(state):
                new_path = path + [child_path]
                new_node = (child, new_path)
                frontier.push(new_node)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # create a frontier priority queue
    frontier = util.PriorityQueue()
    # create an explored set
    explored = set()

    # create a start variable that contains the start state , path , cost
    start = (problem.getStartState(), [], 0)
    # push the start variable in frontier
    frontier.push(start, 0)

    #loop until frontier became empty
    while not frontier.isEmpty():
        # pop the state that has min cost
        (state, path, cost) = frontier.pop()
        # check if this state the goal
        if problem.isGoalState(state):
            return path
        # check if this state not on explored set
        if not state in explored:
            explored.add(state)
            # loop through all children and put them in frontier after update path and cost
            for (child, child_path, child_cost) in problem.getSuccessors(state):
                new_cost = cost + child_cost
                new_path = path + [child_path]
                new_node = (child, new_path, new_cost)
                frontier.push(new_node, new_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # create a frontier priority queue
    frontier = util.PriorityQueue()
    # create an explored set
    explored = set()

    # create a start variable put the start state of the problem and the path , cost , heuristic
    start = (problem.getStartState(), [], 0, heuristic(problem.getStartState(), problem))

    # push the start state and the heuristic
    frontier.push(start, heuristic(problem.getStartState(), problem))

    while not frontier.isEmpty():
        # pop the state that has min cost
        (state, path, cost, heuristic_cost) = frontier.pop()

        # check if this state goal state
        if problem.isGoalState(state):
            return path
        # check if this state not in explored set
        if not state in explored:
            explored.add(state)

            # iterate through all children and put the state and heuristic in the frontier
            for (child, child_path, child_cost) in problem.getSuccessors(state):
                new_cost = cost + child_cost
                new_path = path + [child_path]
                new_heuristic_cost = new_cost + heuristic(child, problem)
                new_node = (child, new_path, new_cost, new_heuristic_cost)
                frontier.push(new_node, new_heuristic_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
