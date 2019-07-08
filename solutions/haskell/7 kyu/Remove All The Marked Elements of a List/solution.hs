module Remove where

remove :: [Int] -> [Int] -> [Int]
remove src dst = filter (\x -> not (elem x dst)) src