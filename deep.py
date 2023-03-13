Answer= input("What is the Answer to the great question of life, the Universe and everything? ")

match Answer:
    case "42" | "forty-two" | "Forty-two":
        print("YES")
    case _:
        print("NO")
    

        