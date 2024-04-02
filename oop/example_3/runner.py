from loader import load_data
from matcher import match

buyers, sellers = load_data()
matches = match(buyers=buyers, sellers=sellers)
