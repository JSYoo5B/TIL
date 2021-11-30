# [Paths on a Grid](https://www.acmicpc.net/problem/6556)

| 시간 제한 | 메모리 제한 |
| :-------: | :---------: |
| 1 초      | 128 MB      |

## 문제

Imagine you are attending your math lesson at school. Once again, you are bored because your teacher tells things that you already mastered years ago (this time he's explaining that (a+b)^2=a^2+2ab+b^2). So you decide to waste your time with drawing modern art instead.

Fortunately you have a piece of squared paper and you choose a rectangle of size n×m on the paper. Let's call this rectangle together with the lines it contains a grid. Starting at the lower left corner of the grid, you move your pencil to the upper right corner, taking care that it stays on the lines and moves only to the right or up. The result is shown on the left:

![](6556.gif)

Really a masterpiece, isn't it? Repeating the procedure one more time, you arrive with the picture shown on the right. Now you wonder: how many different works of art can you produce?


## 입력

The input contains several testcases. Each is specified by two unsigned 32-bit integers n and m, denoting the size of the rectangle. As you can observe, the number of lines of the corresponding grid is one more in each dimension. Input is terminated by n=m=0.


## 출력

For each test case output on a line the number of different art works that can be generated using the procedure described above. That is, how many paths are there on a grid where each step of the path consists of moving one unit to the right or one unit up? You may safely assume that this number fits into a 32-bit unsigned integer.

