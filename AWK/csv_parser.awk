#!/bin/awk

#to run : awk -f csv_parser.awk <file_name>.csv

BEGIN {
    FPAT = "([^,]+)|(\"[^\"]+\")"
}

function hack_print(x)
{
    print substr(x, 1, length(x)-1)
}

{
    n = 0
    if (NR == 1){
        headers = ""
        #add a regex patern between the slashes in the if statement below to match columns
        for (i = 1; i <= NF; i++) {
            if ($i ~ /column1_pattern|column2_pattern|etc/){ 
                headers = headers $i ","
                a[n] = i
                n++
            }
        }
        hack_print(headers)
     }
    else{
        ln = ""
        for (i in a){
            f = a[i]
            ln = ln $f ","
        }
        hack_print(ln)
    }
}
