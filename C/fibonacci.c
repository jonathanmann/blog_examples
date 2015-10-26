#include <stdio.h>

int fib(int pos){
    /*
     * Fibonacci sequence position value calculator 
     * 
     * Args:
     *      pos (int): The Fibonacci sequence position to compute the value for
     *
     * Returns:
     *      int: The value of the Fibonacci sequence at the input position
     */

    if (pos < 1)
    {
        // return -1 for invalid requests
        return -1;
    }     
    else if (pos == 1)
    {
        return 0;
    }
    else if (pos <= 3)
    {
        return 1;
    }

    int result = 1, prev = 1, tmp_result = 0;

    int i = 4;
    while (i <= pos)
    { 
        tmp_result = result;       
        result += prev;
        prev = tmp_result;
        i++;
    }

    return result; 
}

main(){
    int i = 1;
    while (i <= 6)
    {
        printf("%i\n",fib(i));
        i++;
    }
    return 0;
}
