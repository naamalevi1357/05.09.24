# strt

volume: int = int(input("what is the volume level?"))

match volume:
    case 0:
        print("mute")
    case volume if 1 <= volume <= 2:
        print("very quiet")
    case 3:
        print(" quiet ")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud ")
    case - 8:
        print("very loud")
    case volume if 9<= volume <= 10:
        print("extremely loud")

#stop

