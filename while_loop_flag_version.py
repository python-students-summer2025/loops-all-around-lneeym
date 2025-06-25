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
    current_bottles = num_bottles
    
    while current_bottles > 0:
        if current_bottles == 1:
            # Special case for the last bottle
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            # Regular case for multiple bottles
            next_count = current_bottles - 1
            if next_count == 1:
                next_bottle_text = "1 bottle"
            else:
                next_bottle_text = f"{next_count} bottles"
            
            print(f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer.")
            print(f"Take one down, pass it around, {next_bottle_text} of beer on the wall.")
        
        current_bottles -= 1