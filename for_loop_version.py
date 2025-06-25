def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter a number 1 or greater.")
        except ValueError:
            print("Please enter a valid integer.")

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            next_count = i - 1
            if next_count == 1:
                next_bottle_text = "1 bottle"
            else:
                next_bottle_text = f"{next_count} bottles"
            
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {next_bottle_text} of beer on the wall.")