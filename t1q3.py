def main():
    popPaisA = int(input())
    popPaisB = int(input())
    anos = 0
    
    if popPaisB > popPaisA:
        aux = popPaisB
        popPaisB = popPaisA
        popPaisA = aux

    while True:
        popPaisA *= 1.02
        popPaisB *= 1.03
        anos += 1

        if popPaisB > popPaisA: break
    
    print(anos)

if __name__ == '__main__':
    main()