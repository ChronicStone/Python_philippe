# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
def forward_price(spot, interest_rate, time):
    return round(spot * 2.7182 ** (interest_rate * time), 2)



# TODO: 2nd exercise: Define the `short_pnl` function

def short_pnl(positions, mtm): 
    value = 0
    for (index, key) in enumerate(positions):
        value += (positions[index] - mtm[index])
    return value