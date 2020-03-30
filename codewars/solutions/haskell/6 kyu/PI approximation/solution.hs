module Codewars.Kata.PiApprox where

trunc10Dble :: Double -> Double
trunc10Dble d = (fromInteger $ truncate $ d * (10^10)) / (10.0^^10)

recursePi :: Integer -> Double -> Double -> (Integer, Double)
recursePi i num epsilon
        | abs(pi - 4 * num) < epsilon = (i, trunc10Dble $ 4 * num)
        | otherwise = recursePi (i + 1) (num + piApprox i) epsilon
    where piApprox n = ((-1) ^ n) / (2 * (fromIntegral n) + 1)

iterPi :: Double -> (Integer, Double)
iterPi epsilon = recursePi 0 0.0 epsilon
