def countingValleys(steps, path):
    # define valleyCount (track the number of valleys)
    valleyCount = 0
    # define levelCount (track the current level)
    levelCount = 0
    # define levelTrack (to track all the levels)
    levelTrack = [0]

    # track if start of valley found
    valleyFound = False

    # determine the current level
    for i in range(steps):
        if path[i] == "U":
            levelCount += 1
        elif path[i] == "D":
            levelCount -= 1

        # keep record of the levels
        levelTrack.append(levelCount)

        # check if this is the START of a valley (START of valley level will have 0 level BEFORE it)
        if (levelCount == -1) and (levelTrack[i] == 0):
            valleyFound = True

        # check if this is the END of a valley (END of valley level will have -2 level BEFORE it)
        if valleyFound and ((levelTrack[i] == -2) or (levelTrack[i] == 0)):
            # valley found so add 1 value
            valleyCount += 1
            # back to sealevel so valley just found is back to false
            valleyFound = False

    return valleyCount


print(countingValleys(10, "DUDDDUUDUU"))
