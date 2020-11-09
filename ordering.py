def ordering(list):
    for i in range (len(list)):
        for j in range (len(list)):
            if list[i] < list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
            
def createList():
    list = []
    k = input("insert the dimension of the list: ")
    for i in range (int(k)):
        list.append(input("insert an element: ")) 
    return list 


def main():
    list = createList()
    print(f"la lista non invertita e' {list}")
    ordering(list)
    print(f"la lista invertita e' {list}")


if __name__ == "__main__":
    main()