#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""For the chess fans"""


import time


class ChessPiece(object):
    """write this docstring up later - my apartment complex is turning
    the power off and i will write these up after it comes back on; hopefully
    on time before the time is up!!
    """
    prefix = ''

    def __init__(self, position):
        """write this docstring up later
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, title):
        """write this docstring up later
        """
        x_val = 'abcdefgh'
        y_val = [1, 2, 3, 4, 5, 6, 7, 8]
        if len(title) > 2:
            return None
        else:
            if tile[0] in x_val and int(title[1]) in y_val:
                return(x_val.find(title[0]), int(title[1])-1)

            else:
                return None

def is_legal_move(self, position):
        """write this docstring up later
        """
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """write this docstring up later
        """
        if self.is_legal_move(position):
            first = self.prefix + self.position
            second = self.prefix + position
            move = (first, second, time.time())
            self.moves.append(move)
            self.position = position
            return move
        else:
            return False


class Rook(ChessPiece):
    """write this docstring up later"""
    prefix = 'R'

    def __init__(self, position):
        """write this docstring up later
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """write this docstring up later
        """
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position) is not int(position[1]):
                    return True
            else:
                if int(self.position[1]) is int(position[1]):
                    return True
        else:
            return False


class Bishop(ChessPiece):
    """write this docstring up later
    """
    prefix = 'B'

    def __init__(self, position):
        """write this docstring up later
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """write this docstring up later
        """
        before = self.algebraic_to_numeric(position)
        after = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if (before[0] + after[0]) % (before[1] + after[1]) is 0:
                return True
        else:
            return False


class King(ChessPiece):
    """write this docstring up later
    """
    prefix = 'K'

    def is_legal_move(self, position):
        """write this docstring up later
        """
        before = self.algebraic_to_numeric(position)
        after = self.algebraic_to_numeric(self.position)
        if abs(after[1] - before[1]) <= 1:
            if after[1]+after[0] % before[1]+before[0]:
                return True
        else:
            return False


class ChessMatch(object):
    """write this docstring up later
    """

    def __init__(self, pieces=None):
        """write this docstring up later
        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """write this docstring up later
        """
        self.log = []
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}
        return self.pieces

    def move(self, piece, position):
        """write this docstring up later
        """
        ChessPiece.move.__init__(self)
        if piece in self.pieces:
            mypiece = self.pieces[piece]
            wenthere = mypiece.move(position)
            self.log.append(wenthere)
            self.pieces.pop(piece)
            self.pieces[wenthere[1]] = mypiece
