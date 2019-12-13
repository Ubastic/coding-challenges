module Codewars.Arrays where

positiveSum :: [Int] -> Int
positiveSum arr = foldr (+) 0 (filter (>0) arr)
