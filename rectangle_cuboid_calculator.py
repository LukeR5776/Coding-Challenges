def calculate_rectangle_area(length, width):
    return length * width

def calculate_cuboid_volume(length, width, height):
    return length * width * height

def main():
    print("Rectangle Area & Cuboid Volume Calculator")
    print("1. Calculate rectangle area (length × width)")
    print("2. Calculate cuboid volume (length × width × height)")
    
    choice = input("Choose option (1 or 2): ").strip()
    
    if choice == "1":
        try:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            
            if length <= 0 or width <= 0:
                print("Error: Dimensions must be positive numbers")
                return
                
            area = calculate_rectangle_area(length, width)
            print(f"Rectangle area: {area}")
            
        except ValueError:
            print("Error: Please enter valid numbers")
            
    elif choice == "2":
        try:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            
            if length <= 0 or width <= 0 or height <= 0:
                print("Error: Dimensions must be positive numbers")
                return
                
            volume = calculate_cuboid_volume(length, width, height)
            print(f"Cuboid volume: {volume}")
            
        except ValueError:
            print("Error: Please enter valid numbers")
            
    else:
        print("Error: Please choose 1 or 2")

if __name__ == "__main__":
    main()