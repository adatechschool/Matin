import Prelude

data Color = Red | Green | Blue | Yellow | Magenta | Cyan
    deriving (Show, Eq)

evaluate :: [Color] -> [Color] -> (Int, Int)
evaluate secret guess = (0, 0)

main = do
    putStrLn $ show $ evaluate [Red] [Red]
