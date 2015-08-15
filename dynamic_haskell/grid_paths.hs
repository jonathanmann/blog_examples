m :: (Int -> Int -> a) -> [[a]]
m f = map (\x -> map (f x) [0..]) [0..]

grid_paths :: Int -> Int -> Int
grid_paths 0 _ = 1
grid_paths _ 0 = 1
grid_paths x y = (f_grid_paths (x - 1) y) + (f_grid_paths x (y - 1))

m_grid_paths :: [[Int]]
m_grid_paths = m grid_paths

f_grid_paths :: Int -> Int -> Int
f_grid_paths x y = m_grid_paths !! x !! y
