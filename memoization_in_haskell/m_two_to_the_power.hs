m_two_to_the_power :: Int -> Integer
m_two_to_the_power = (map two_to_the_power [0 ..] !!)
    where two_to_the_power 0 = 1
          two_to_the_power n = m_two_to_the_power(n-1) + m_two_to_the_power(n-1)

