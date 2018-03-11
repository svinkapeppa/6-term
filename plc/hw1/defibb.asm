funcb -1688265053
mov *ex **sp
pop
mov *ax **sp
pop
mov *bx **sp
pop
mov *fx **sp
pop
goto *fx 4
push *bx
push *ax
mov *ip *ex
sub *fx 1
push *ex
push *fx
push *bx
push *ax
call -1688265053
mov *ax **sp
pop
mov *bx **sp
pop
mov *cx *bx
add *bx *ax
mov *ax *cx
mov *ex **sp
pop
push *bx
push *ax
mov *ip *ex
funce
putstr This program calculates the n-th number in fibonacci sequence [1, 1, 2, 3, 5, 8, ...].
putstr Enter a number:
read *ax
push *ax
push 1
push 0
call -1688265053
mov *ax **sp
pop
mov *bx **sp
pop
putstr The n-th number in fibonacci sequence is:
print *bx
exit
