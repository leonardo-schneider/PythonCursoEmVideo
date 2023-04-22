import math
ang = float(input("digite o seu angulo: "))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print("o cosseno do angulo {} é {:.2f}" .format (ang,cos))
print("o seno do angulo {} é {:.2f}" .format(ang,sen))
print("a tangente do angulo{} é {:.2f}" .format(ang,tan))