two_to_the_power :: Int -> Integer
two_to_the_power 0 = 1
two_to_the_power n = two_to_the_power(n-1) + two_to_the_power(n-1)
