def num_check(question):

    print("POopY")
    error = "more than zero please sir or ma'am\n"
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going== "":

    width = num_check("Mayhaps could I have the width sir or ma'am: ")
    height = num_check("Mayhaps could I have the height as well sir or ma'am: ")

    area = width * height
    perimeter = 2 * (width + height)

    print()
    print(f"I do so believe that the perimeter is {perimeter} units")
    print(f"I do so believe that the area is {area} square units")

    keep_going = input("If you wish to continue press enter, if you wish to quit press anything else")
    print()

print("Thank you for using our area / perimeter claculator. "
      "We know you have better and cheaper alternatives, but we thank you. "
      "Thank you for wasting your money")