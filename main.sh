#!/bin/bash
remove_data() {
    for file in `ls ex?` # list all  in current directory, file name stored in $file
    do 
        echo `rm $file`
    done

    for file in `ls ex?result?`
    do
        echo `rm $file`
    done
}

main() {
    remove_data # remove all extra datas in current directory
    all_ex=()
    i=0
    for file in `ls ex?.c` # list all  in current directory, file name stored in $file
    do
        output_file=${file:0:3}
        echo `gcc $file -o $output_file`
        all_ex[$i]=$output_file
        i=$i+1
    done

    for exer in ${all_ex[@]} # list all exercises
    do
        for file in `ls ${exer}in?` # list all input files for each exercise
        do
            num=${file:${#file}-1:1}
            echo `./${exer} < ${file} > ${exer}result${num}` # executes exercise
            echo `diff -qs ${exer}result${num} ${exer}out${num}` # executes diff
        done
    done
}
main