#quando o passo é 2
def josefo(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 2*josefo(n/2)-1
    else:
        return 2*josefo(n//2)+1

n = int(input("Quanto é n?:\n>>"))
print(josefo(n))