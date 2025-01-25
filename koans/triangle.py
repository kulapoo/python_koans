#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE

    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError()

    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError()



    set1 = set([a, b, c])
    set2 = set([a, c, b])

    set3 = set1 & set2

    set_len = len(set3)

    if set_len == 1:
        return "equilateral"
    elif set_len == 2:
        return "isosceles"
    else:
        return "scalene"


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
