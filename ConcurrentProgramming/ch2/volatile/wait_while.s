	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 15, 0	sdk_version 15, 4
	.globl	_wait_while_0_normal            ; -- Begin function wait_while_0_normal
	.p2align	2
_wait_while_0_normal:                   ; @wait_while_0_normal
	.cfi_startproc
; %bb.0:
	ldr	w8, [x0]
	cbz	w8, LBB0_2
; %bb.1:
	ret
LBB0_2:                                 ; =>This Inner Loop Header: Depth=1
	b	LBB0_2
	.cfi_endproc
                                        ; -- End function
	.globl	_wait_while_0_volatile          ; -- Begin function wait_while_0_volatile
	.p2align	2
_wait_while_0_volatile:                 ; @wait_while_0_volatile
	.cfi_startproc
; %bb.0:
LBB1_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [x0]
	cbz	w8, LBB1_1
; %bb.2:
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
