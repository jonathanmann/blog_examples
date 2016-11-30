-- Exercise 1
toDigits :: Integer -> [Integer]
toDigits x
    | x <=0 = []
    | otherwise = toDigits (x `div` 10) ++ [x `mod` 10]

toDigitsRev :: Integer -> [Integer]
toDigitsRev x 
    | x <=0 = []
    | otherwise = x `mod` 10 : toDigitsRev (x `div` 10)


-- Exercise 2
doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther (x:y:z) = (2*x:y:doubleEveryOther z)
doubleEveryOther x = x

-- Main
main :: IO ()
main = do

    -- Expect [1,2,3,4]
    print (toDigits 1234)

    -- Expect [4,3,2,1]
    print (toDigitsRev 1234)

    -- Expect [16,7,12,5]
    print (doubleEveryOther [8,7,6,5])

    -- Expect [1,4,3]
    print (doubleEveryOther [1,2,3])

    print (doubleEveryOther (toDigitsRev 1234))
