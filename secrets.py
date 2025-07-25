import  argparse
parser = argparse.ArgumentParser()
parser.add_argument('usuario')
parser.add_argument('password')
args = parser.parse_args()

if args.usuario == "Nancy" and args.password == "morado":
    print("Hola acceso correcto")
else:
    print("Hola acceso incorrecto")