import random
from enum import Enum
from typing import Any

from pacai.agents.capture.capture import CaptureAgent
from pacai.bin.capture import CaptureGameState
from pacai.core.directions import Directions


class Action(Enum):
    NORTH = Directions.NORTH
    SOUTH = Directions.SOUTH
    EAST = Directions.EAST
    WEST = Directions.WEST
    STOP = Directions.STOP




def createTeam(firstIndex: int, secondIndex: int, isRed: bool) -> list[CaptureAgent]:
    """
    This function should return a list of two agents that will form the capture team,
    initialized using firstIndex and secondIndex as their agent indexed.
    isRed is True if the red team is being created,
    and will be False if the blue team is being created.
    """

    firstAgent = DummyAgent
    secondAgent = DummyAgent

    return [
        firstAgent(firstIndex),
        secondAgent(secondIndex),
    ]


# Copied over from pacai/agents/capture/dummy.py
class DummyAgent(CaptureAgent):
    """
    A Dummy agent to serve as an example of the necessary agent structure.
    You should look at `pacai.core.baselineTeam` for more details about how to create an agent.
    """

    def __init__(self, index: int, **kwargs: dict[str, Any]) -> None:
        super().__init__(index, **kwargs)

    def registerInitialState(self, gameState) -> None:
        """
        This method handles the initial setup of the agent and populates useful fields,
        such as the team the agent is on and the `pacai.core.distanceCalculator.Distancer`.

        IMPORTANT: If this method runs for more than 15 seconds, your agent will time out.
        """

        super().registerInitialState(gameState)

        # Your initialization code goes here, if you need any.

    def chooseAction(self, gameState: CaptureGameState) -> list[Action]:
        """
        Randomly pick an action.
        """

        actions = gameState.getLegalActions(self.index)
        return random.choice(actions)
