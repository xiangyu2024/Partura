"""Partura -- the alpha-distillation layer on top of AlphaCube.

AlphaCube's GP/RL stage searches a very large symbolic space and returns
expressions that predict without explaining.  Partura takes one such
expression and tries to find out *what part of it carries the prediction*:
it reads the operators' real implementations, measures their behaviour with
probes, decomposes the tree, states competing hypotheses, and runs the
ablations that can kill them -- then tries to distil the survivor into the
smallest structure that keeps the edge.

It owns no data, no engine and no backtester: those are imported from
AlphaCube (see ``partura.bridge``).
"""

__version__ = "0.1.0"
