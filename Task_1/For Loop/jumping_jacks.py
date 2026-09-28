total = 0
for i in range(10):
    total += 10
    print("You completed", total, "jumping jacks.")

    if total == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tried? ")

    if tired.lower() == "yes" or tired.lower() == "y":
        skip = input("Do you want to skip the remaining sets? ")

        if skip.lower() == "yes" or skip.lower() == "y":
            print("You completed a total of", total, "jumping jacks.")
            break

        print(100 - total, "jumping jacks are remaining.")


 