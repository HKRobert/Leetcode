#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/5
"""Prob 48. Rotate Image

https://leetcode.com/problems/rotate-image/description/

Description:
    You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise).
    
    Note: 
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    
    Example 1: 
    Given input matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ], 
    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    Example 2:
    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]
"""


# clockwise rotate: first reverse up to down, then swap the symmetry
# anticlockwise rotate: first reverse left to right, then swap the symmetry
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix[::] = zip(*matrix[::-1])


def rotate2(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in xrange(n):
        for j in xrange(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(mat)
    print(mat)