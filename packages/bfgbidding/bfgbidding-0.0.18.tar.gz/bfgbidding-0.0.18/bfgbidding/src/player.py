""" Bid for Game
    Player class
"""
# from termcolor import cprint

from bridgeobjects import ROLES, Board, Hand
from .bidding import Bid
from .acol_bidding import AcolBid

MODULE_COLOUR = 'blue'


class Player(object):
    """Define BfG Player class."""
    NUMBER_OF_PLAYERS = 4

    def __init__(self,
                 board: Board | None = None,
                 hand: Hand | None = None,
                 index: int | None = None):
        self.board = board
        self.hand = hand
        self.index = index
        self.role = -1

    def __repr__(self) -> str:
        """Return a string representation of player."""
        return f'player: {self.hand}'

    def make_bid(self, update_bid_history: bool = True) -> Bid:
        """Make a bid and return bid object."""
        active_bid_history = self._active_bid_history(self.board.bid_history)
        # if len(active_bid_history) >= 4 and active_bid_history[-3:] == ['P', 'P', 'P']:
        #     return 'three passes'
        self.role = self._get_role(active_bid_history)
        self.board.active_bid_history = active_bid_history

        bid = AcolBid(self.hand, self.board, self.role).bid

        if update_bid_history:
            try:
                self.board.bid_history.append(bid.name)
                x = bid.use_shortage_points
            except AttributeError:
                ic(self.role)
                ic(self.hand)
                ic(self.board.active_bid_history)
        hc_points = self.hand.high_card_points
        try:
            x = bid.use_shortage_points
        except AttributeError:
            ic(self.role)
            ic(self.hand)
            ic(self.board.active_bid_history)
            ic(len(self.board.active_bid_history))

        if bid.use_shortage_points:
            distribution_points = 0
            hand_points = f'{hc_points}+{distribution_points}'
            hand_description = f'{hand_points} = {hc_points+distribution_points}'
        else:
            hand_description = str(hc_points)
        hand_description = f'{hand_description} '
        bid.hand_points = hand_description
        return bid

    def _get_role(self, bid_history: list[str]) -> int:
        """Return role based on bid history."""
        role_id = self._get_role_id(bid_history)
        if role_id == 0:
            role = ROLES['Opener']
        elif role_id == 2:
            role = ROLES['Responder']
        else:
            role = self._assign_overcaller_advancer(bid_history, role_id)
        return role

    def _get_role_id(self, bid_history: list[str]) -> int:
        """Return the role_id based on the length of the bid_history."""
        role_id = len(bid_history)-100
        for bid in bid_history:
            if bid != 'P':
                break
            else:
                role_id -= 1
        role_id %= self.NUMBER_OF_PLAYERS
        return role_id

    def _assign_overcaller_advancer(self, bid_history: list[str], role_id: int) -> int:
        """Return the role_id if Overcaller or Advancer."""
        first_overcaller = 1
        for bid in bid_history[1::2]:
            if bid != 'P':
                break
            else:
                first_overcaller += 2
        first_overcaller %= self.NUMBER_OF_PLAYERS
        if first_overcaller == role_id:
            role = ROLES['Overcaller']
        else:
            role = ROLES['Advancer']
        return role

    @staticmethod
    def _active_bid_history(bid_history: list[str]) -> list[str]:
        """Return the bid history without leading PASSES."""
        temp_history = []
        started = False
        for bid in bid_history:
            if bid != 'P' or started:
                temp_history.append(bid)
                started = True
        return temp_history
