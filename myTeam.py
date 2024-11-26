import random
from pacai.agents.capture.capture import CaptureAgent

def createTeam(firstIndex, secondIndex, isRed):
    return [
        OffensiveAgent(firstIndex),
        DefensiveAgent(secondIndex),
    ]

class OffensiveAgent(CaptureAgent):
    def getSuccessor(self, gameState, action):
        return gameState.generateSuccessor(self.index, action)

    def chooseAction(self, gameState):
        actions = gameState.getLegalActions(self.index)
        foodList = self.getFood(gameState).asList()
        myPos = gameState.getAgentPosition(self.index)

        if len(foodList) > 0:
            distances = [(self.getMazeDistance(myPos, food), food) for food in foodList]
            closestFood = min(distances, key=lambda x: x[0])[1]

            bestAction = None
            minDistance = float('inf')
            for action in actions:
                successor = self.getSuccessor(gameState, action)
                successorPos = successor.getAgentPosition(self.index)
                distance = self.getMazeDistance(successorPos, closestFood)
                if distance < minDistance:
                    minDistance = distance
                    bestAction = action

            return bestAction

        return random.choice(actions)


class DefensiveAgent(CaptureAgent):
    def getSuccessor(self, gameState, action):
        return gameState.generateSuccessor(self.index, action)
    
    def chooseAction(self, gameState):
        actions = gameState.getLegalActions(self.index)
        myPos = gameState.getAgentPosition(self.index)
        opponents = self.getOpponents(gameState)

        invaders = [
            gameState.getAgentState(opponent)
            for opponent in opponents
            if gameState.getAgentState(opponent).isPacman and gameState.getAgentState(opponent).getPosition() is not None
        ]

        if invaders:
            distances = [(self.getMazeDistance(myPos, invader.getPosition()), invader) for invader in invaders]
            closestInvader = min(distances, key=lambda x: x[0])[1]

            bestAction = None
            minDistance = float('inf')
            for action in actions:
                successor = self.getSuccessor(gameState, action)
                successorPos = successor.getAgentPosition(self.index)
                distance = self.getMazeDistance(successorPos, closestInvader.getPosition())
                if distance < minDistance:
                    minDistance = distance
                    bestAction = action

            return bestAction

        return random.choice(actions)
