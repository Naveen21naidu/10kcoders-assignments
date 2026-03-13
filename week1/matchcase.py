#write a code on match using realworld best cases 
signal = input("Enter signal color: ")

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
