r_two_to_power :: Int -> Integer
r_two_to_power 0 = 1
r_two_to_power n = r_two_to_power(n-1) + r_two_to_power(n-1)
