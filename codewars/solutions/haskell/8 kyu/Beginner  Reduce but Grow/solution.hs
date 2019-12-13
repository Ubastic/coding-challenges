module Grow where

grow :: [Int] -> Int
grow = foldr (*) 1