def quota():
    
    input_floats = input("nums seperated by comma: ")
    float_list = [float(num) for num in input_floats.replace(" ", "").split(",")]
    for num in float_list:
        n = math.floor(num)
        geom = (n*(n+1))**0.5
        print(f"intial quota: {num}")
        print(f"geo mean: {geom:.3f}")
        print("final allocation")
        if num > geom:
            print(f'{n+1}')
        else:
            print(f'{n}')
        

quota()