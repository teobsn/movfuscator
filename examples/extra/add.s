.data
    x: .long 15
    y: .long 17
    sum: .space 4

.text

.global main

main:
    movl x, %eax     # eax = 15
    add y, %eax     # eax <- eax (15) + y (17) = 32
    movl %eax, sum

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80