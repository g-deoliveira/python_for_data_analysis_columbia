import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('x')
parser.add_argument('y')

args = parser.parse_args()
data = vars(args)

x = data.get('x')
y = data.get('y')

def hello(x,y):
    z = None
    try:
        z = x / y
    except ValueError as err:
        print(f'Error: ValueError {err}')
    except ZeroDivisionError as err:
        print(f'Error: ZeroDivisionError: {err}')
    except Exception as err:
        print(f'Exception {err.__class__.__name__}: {err}')
    finally:
        print('here')
        print(f'x={x} y={y} z={z}')


hello(x,y)



