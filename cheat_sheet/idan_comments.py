# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:51:46 2020

@author: nati1
"""

#
# סיכום נקודות מהרצאה עשירית :
#     training data - data that we build are model on
#     testing data - data that we test our model on to check accuracy
#
#     calcuating "distance" between data objects :
#         minkowski metric :
#             dist(x1,x2,p) = (SIGMA(abs(x1k-x2k))^p)^1/p
#
#             SIGMA goes fron 1 to len(objects)
#
#             when :
#                 p=1 : Manhattan distance
#                 p=2 : Euclidian distance


# accuracy = (True Positive + True negative) / (True positive + True negative + False positive + False negative)
#
# sensitivity: (True positive) / (True positive + False negative)  ### Percentage of correctly found
#
# specificity: (True negative) / (True negative + False positive)  ### Percentage correctly rejected
#
# positive predictive value: (True positive) / (True positive + False positive)  ### How good will the  prediction be

# Linkage methods :
#      Single linkage - shortest way between two clusters (two individual objects per cluster)
#      Complete linkage - Longest way between two objects
#      Average linkage - Average distance between all first cluster points to all second cluster points (like a nested loop) average.












