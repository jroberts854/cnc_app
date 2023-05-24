from orders.calcs import DESK
from orders.calcs import TT
from orders.calcs import SPED




lookup = {
    'DESK': DESK.calc,
    'RTN': DESK.calc,
    'TT': TT.calc,
    'PED': SPED.calc,
}

def calc(model, qty, options):
    key = model.split("-")[0]
    try:
        f=lookup[key]
        # print("f",f)

        return lookup[model.split('-')[0]](model, qty, options)
    except:
        print("Model not found",key)
        return "Model not found"
