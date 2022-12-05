def confirm_prompt(question, default="n"):
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").lower()
        if reply == "n":
            print("exiting")
            exit()
        elif reply == "y":
            print("Running....")
            # PROGRAM GOES HERE

        else:
            confirm_prompt("That is not a valid option. Enter")
    return (reply == "y")

#print(reply)