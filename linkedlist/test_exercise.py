if __name__ == "__main__" :
    str_test = ["test1","test2","test3"]

    str_arr = str_test
    print(str_arr)

    left =0
    right = len(str_arr) -1

    print(type(str_arr))

    print(left,right)

    while left < right:
        temp = str_arr[left]
        str_arr[left] =str_arr[right]
        str_arr[right] = temp
        left +=1
        right -=1
    

    print(str_arr)
