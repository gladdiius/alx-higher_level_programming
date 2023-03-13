#!/usr/bin/python3
__name__ = "__main__"


def multiple_returns(sentence):
        if len(sentence) == 0:
            return None
        else:
            return (len(sentence), sentence[0])

