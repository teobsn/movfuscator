.data
    v: .long 5, 3, 6, 9, 24, 13, 21, 8, 1
    n: .long 9
    sum: .space 4       # 6 + 24 + 8 = 38

.text

.global main

main:
    movl $v, %edi   # lea v, %edi
    movl $0, %ecx   # index curent
    movl $0, %ebx   # calcul suma
    movl $2, %esi   # constanta 2 pt impartire
    jmp et_while

et_while:
    cmp n, %ecx
    je et_while_exit

    movl (%edi, %ecx, 4), %eax
    movl $0, %edx
    divl %esi

    cmp $0, %edx
    je is_even

et_while_cont:
    incl %ecx
    jmp et_while
    
is_even:
    movl (%edi, %ecx, 4), %eax
    add %eax, %ebx
    jmp et_while_cont


et_while_exit:
    movl %ebx, sum

et_exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80