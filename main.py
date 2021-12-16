def characters(data):
    output = {}
    # count = 0 #if you dont want to display the count
    # changing data into upper case,lower case

    data1 = data.lower()
    for i in data1:
        keys = output.keys()
        if i not in keys:
            output[i] = 1
            # count += 1
        else:
            output[i] += 1
    # return (output,count)
    return (output)

print(characters("Umbrella"))