## 目 录

第一章 分析引论 ..... 1
§1. 实数 ..... 1
§2. 叙列的理论 ..... 25
§3. 函数的概念 ..... 95
§4. 函数的图形表示法 ..... 128
§5. 函数的极限 ..... 226
§6. 函数无穷小和无穷大的阶 ..... 357
§7. 函数的连续性 ..... 375
§8. 反函数 用参数表示的函数 ..... 425
§9. 函数的 - 致连续性 ..... 444
§10. 函数方程 ..... 463


## 第一章 分析引论

## §1. 实 数

1. $1+2+\cdots+n=\frac{n(n+1)}{2}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-008.jpg?height=64&width=686&top_left_y=2498&top_left_x=268)

证 当 $n=1$ 时，等式成立。
设对于 $n=k$ （自然数）时，等式成立，即

$$
1+2+\cdots+k=\frac{k(k+1)}{2}
$$

则对于 $n=k+1$ 时,有

$$
\begin{gathered}
1+2+\cdots+k+(k+1)=\frac{k(k+1)}{2}+k+1 \\
=\frac{(k+1)[(k+1)+1]}{2}
\end{gathered}
$$

即对于 $n=k+1$ 时等式也成立。
于是，由数学归纳法知，对于任何自然数 $n$ ，有

$$
1+2+\cdots+n=\frac{n(n+1)}{2}
$$

2. $1^{2}+2^{2}+\cdots+n^{2}=\frac{n(n+1)(2 n+1)}{6}$.

证 当 $n=1$ 时，等式成立。
设 $n=k$ 时，等式成立，即

$$
1^{2}+2^{2}+\cdots+k^{2}=\frac{k(k+1)(2 k+1)}{6}
$$

则对于 $n=k+1$ 时, 有

$$
\begin{aligned}
1^{2} & +2^{2}+\cdots+k^{2}+(k+1)^{2} \\
& =\frac{k(k+1)(2 k+1)}{6}+(k+1)^{2} \\
& =\frac{1}{6}(k+1)[k(2 k+1)+6(k+1)] \\
& =\frac{(k+1)[(k+1)+1)(2(k+1)+1)}{6},
\end{aligned}
$$

即对于 $n=k+1$ ，时等式也成立。
于是，对于任何自然数 $n$ ，有

$$
1^{2}+2^{2}+\cdots+n^{2}=\frac{n(n+1)(2 n+1)}{6}
$$

3. $\quad 1^{3}+2^{3}+\cdots+n^{3}=(1+2+\cdots+n)^{2}$.

证 当 $n=1$ 时，等式成立.
设 $n=k$ 时，等式成立，即

$$
1^{3}+2^{3}+\cdots+k^{3}=(1+2+\cdots+k)^{2},
$$

则对于 $n=k+1$ 时，有

$$
\begin{aligned}
& 1^{3}+2^{3}+\cdots-k^{3}+(k+1)^{3} \\
& =(1+2-\cdots+k)^{2}+(k+1)^{3} \\
& =\frac{k^{2}(k+1)^{2}}{4}+(k+1)^{3} \\
& =\frac{(k+1)^{2}(k+2)^{2}}{4} \\
& =\left\{\frac{(k+1)[(k+1)+1]}{2}\right\}^{2} \\
& =[1+2+\cdots+(k+1)]^{2}
\end{aligned}
$$

即对于 $n=k+1$ 时，等式也成立。
于是，对于任何自然数 $n$ ，有

$$
1^{3}+2^{3}+\cdots+n^{3}=(1+2+\cdots+n)^{2}
$$

4. $\quad 1+2+2^{2}+\cdots+2^{* 1}=2^{n}-1$.

证 当 $n=1$ 时，等式成立。
设 $n=k$ 时，等式成立，即

$$
1+2+2^{2}+\cdots+2^{k-1}=2^{k}-1
$$

则对于 $n=k+1$ 时, 有

$$
\begin{aligned}
& 1+2+2^{2}+\cdots+2^{k-1}+2^{k} \\
& \quad=\left(2^{k}-1\right)+2^{k}=2^{k+1}-1
\end{aligned}
$$

即对于 $n=k+1$ 时，等式也成立。
于是，对于任何自然数 $n$ ，有

$$
1+2+2^{2}+\cdots+2^{n-1}=2^{n}-1
$$

5. 设 $a^{[n:}=a(a-h) \cdots[a-(n-1) h]$ 及 $a^{[0]}=1$, 求证

$$
(a+b)^{[n]}=\sum_{m=0}^{n} C_{n} a^{(n \cdots m)} b^{[m]},
$$

其中 $C_{n}^{m}$ 是由 $n$ 个元素中选取 $m$ 个的组合数，由此推出牛顿的二项式公式。
证 当 $n=1$ 时，由于

$$
\begin{gathered}
{[a+b]^{(1)}=a+b} \\
\sum_{m=0}^{1} C_{1}^{m} a^{[1-m]} b^{(m)}=a+b,
\end{gathered}
$$

所以等式成立。
设 $n=k$ 时，等式成立，即

$$
(a+b)^{[\mathrm{l}]}=\sum_{m=0}^{k} C_{k}^{m} a^{[k-m]} b^{[m]}
$$

则对于 $n=k+1$ 时, 有

$$
(a+b)^{[k+1]}=(a+b)^{[k]} \cdot(a+b-k h) .
$$

将（1）式代入（2）式得

$$
\begin{aligned}
& (a+b)^{[a+1]}=(a+b-k h) \cdot \sum_{m=0}^{b} C^{m} a^{[h-m]} b^{[m]} \\
& =(a+b-k h)\left\{C_{k}^{(a} a^{(k)} b^{[0]}+C_{k}^{1} a^{[k-1]} b^{[1]}\right. \\
& \left.+\cdots+C_{k}^{k} a^{[0]} b^{[k]}\right\} \\
& =((a-k h)+b\} C_{i}^{0} a^{[0)} b^{(0)} \\
& +\{[a-(k-1) h]+(b-h)\} C_{k} a^{[k-1]} b^{[1]} \\
& +\cdots+\{a+(b-k h)\} C_{k} a^{[0]} b^{(b)} \\
& =C_{k}^{0} a^{[k+1]} b^{[0]}+C_{k}^{0} a^{[k]} b^{[1]}+C_{k} a^{(k)} b^{[1]} \\
& +C_{k}^{1} a^{[k-1]} b^{[2]}+\cdots+C_{k}^{k} a^{(1)} b^{[k]} \\
& +C_{k}^{k} a^{[00} b^{(a+1)}
\end{aligned}
$$

$$
\begin{aligned}
= & C_{k+1}^{0} a^{[k+1)} b^{[0]}+\left(C_{k}^{0}+C_{n}\right) a^{[k]} b^{[1]} \\
& +\cdots+\left(C_{k}^{k-1}+C_{k}^{k}\right) a^{[1]} b^{[k]}+C_{k-1}^{k+1} a^{[0]} b^{[k+1]} \\
= & C_{k+1}^{0} a^{[k+1]} b^{[0]}+\left(C_{k+1}^{0} a^{[k)} b^{[1]}\right. \\
& +\cdots-\left(C_{k+1}^{k} a^{[1]} b^{[k]}+C_{k+1}^{k+1} a^{[0]} b^{[k+1)}\right. \\
= & \sum_{m=0}^{k+1} C_{k+1}^{m} a^{[k+1-m]} b^{[m]},
\end{aligned}
$$

故由 $(a+b)^{[k)}=\sum_{m=0}^{k} C_{k}^{n} a^{[k-m]} b^{(m]}$ 可推得下式成立：

$$
(a+b)^{[k+1]}=\sum_{m=0}^{+1]} C_{k+1}^{n} a^{[k+1-m]} b^{[m]}
$$

即对于 $n=k+1$ 时，等式也成立。
于是，对于任何自然数 $n$ ，有

$$
(a+b)^{[n]}=\sum_{m=0}^{\infty} C_{n}^{m} a^{[n-m]} b^{[m]}
$$

在式子

$$
a^{[m]}=a(a-h) \cdots[a-(n-1) h]
$$

中，令 $h=0$ ，即得

$$
a^{[n]}=a^{n}
$$

将（4）式代人（3）式，得牛顿二项式公式

$$
(a+b)^{n}=\sum_{\mathrm{m}=0}^{\infty} C_{n}^{n} a^{n-m} b^{n}
$$

6. 证明贝努里不等式
$\left(1+x_{1}\right)\left(1+x_{2}\right) \cdots\left(1+x_{n}\right) \geqslant 1+x_{1}+x_{2}+$
$\cdots+x_{n}$
式中 $x_{1}, x_{2}, \cdots, x_{n}$ 是符号相同且大于 -1 的数.
证 当 $n=1$ 时，此式取等号。
设 $n=k$ 时，不等式成立，即

$$
\left(1+x_{1}\right)\left(1+x_{2}\right) \cdots\left(1+x_{k}\right) \geqslant 1+x_{1}+x_{2}+\cdots
$$

$+x_{k}$,

则对于 $n=k+1$ 时，由于 $x_{i}(i=1,2, \cdots, n)$ 大于 -1 ，所以 $1+x_{i}>0$. 因而有

$$
\begin{aligned}
&\left(1+x_{1}\right)\left(1+x_{2}\right) \cdots\left(1+x_{k}\right)\left(1+x_{k+1}\right) \\
& \geqslant\left(1+x_{1}+x_{2}+\cdots+x_{k}\right)\left(1+x_{k+1}\right) \\
&=\left(1+x_{1}+x_{2}+\cdots+x_{k}+x_{k+1}\right) \\
&+\left(x_{1} x_{k+1}+x_{2} x_{k+1}+\cdots+x_{k} x_{k+1}\right) .
\end{aligned}
$$

由于 $x_{i} x_{j} \geqslant 0$, 所以

$$
\begin{aligned}
& \left(1+x_{1}\right)\left(1+x_{2}\right) \cdots\left(1+x_{k+1}\right) \\
& \quad \geqslant 1+x_{1}+x_{2}+\cdots+x_{k+1}
\end{aligned}
$$

即对于 $n=k+1$ 时，不等式也成立，
于是，对于任何自然数 $n$ ，有

$$
\begin{aligned}
& \left(1+x_{1}\right)\left(1+x_{2}\right) \cdots\left(1+x_{n}\right) \\
& \quad \geqslant 1+x_{1}+x_{2}+\cdots+x_{n}
\end{aligned}
$$

7. 证明若 $x>-1$ ，则不等式 $$ (1+x)^{n} \geqslant 1+n x \quad(n>1) $$ 为真，且仅当 $x=0$ 时，等号成立。
证 只要在 6 题的贝努里不等式中，设

$$
x_{i}=x \quad(i=1,2 \cdots, n),
$$

即得证

$$
(1+x)^{n} \geqslant 1+n x
$$

从 6 题的证明过程中看出，仅当 $x=0$ 时，上式才取等号。
8. 证明不等式

$$
n:<\left(\frac{n+1}{2}\right)^{n} \text { 当 } n>1 \text {. }
$$

证 当 $n=2$ ，因为 $\left(\frac{2+1}{2}\right)^{2}=\frac{9}{4}>2=2!$ ，故不等式成立。

设 $n=k$ 时，不等式成立，则

$$
k!<\left(\frac{k+1}{2}\right)^{k}
$$

则对于 $n=k+1$ 时，有

$$
(k+1)!<\left(\frac{k+1}{2}\right)^{k}(k+1)=2\left(\frac{k+1}{2}\right)^{k+1}
$$

由于

$$
\left(\frac{k+2}{k+1}\right)^{k+1}=\left(1+\frac{1}{k+1}\right)^{k+1}>2(k=1,2, \cdots),
$$

从而有

$$
(k+1) 1<\left[\frac{(k+1)+1}{2}\right]^{k+1},
$$

即对于 $n=k+1$ 时，不等式也成立。
于是，对于任何自然数 $n$ ，有

$$
n_{1}<\left(\frac{n+1}{2}\right)^{n}
$$

9. 证明不等式

$$
2!\cdot 4!\cdots(2 n)!>[(n+1)!]^{n} \quad \text { 当 } n>1 \text {. }
$$

证 当 $n=2$ 时,因为 $2!\cdot 4!=48$. 及 $[(2+1)!]^{2}=$ 36, 所以 , 2! • $4!>[(2+1)!]^{2}$ ，故不等式成立。

设 $n=k$ 时，不等式成立，即

$$
2!\cdot 4!\cdots(2 k) \mid>[(k+1)!]^{k}
$$

则对于 $n=k+1$ 时,有

$$
2!\cdot 4!\cdots(2 k+2)!>[(k+1)!] k(2 k+2)!
$$

$$
\begin{aligned}
= & {[(k+1)!]^{k+1}(k+2)(k+3) \cdots(2 k+2) } \\
& >[(k+1)!]^{k+1}(k+2)^{k+1}=[(k+2)!]^{k+1},
\end{aligned}
$$

即对于 $n=k+1$ 时，不等式也成立。于是，据归纳法原理，本题证毕。
10. 证明不等式

$$
\frac{1}{2} \cdot \frac{3}{4} \ldots \frac{2 n-1}{2 n}<\frac{1}{\sqrt{2 n+1}}
$$

证 当 $n=1$ 时，因为 $\frac{1}{2}<\frac{1}{\sqrt{3}}$ ，不等式显然成立。
设 $n=k$ 时，不等式成立，即

$$
\frac{1}{2} \cdot \frac{3}{4} \ldots \frac{2 k-1}{2 k}<\frac{1}{\sqrt{2 k+1}}
$$

对于 $n=k+1$ 而言，由于

$$
\begin{aligned}
\frac{1}{2} & \cdot \frac{3}{4} \cdots \frac{2 k+1}{2 k+2}<\frac{1}{\sqrt{2 k+1}} \cdot \frac{2 k+1}{2 k+2} \\
& =\frac{\sqrt{2 k+1}}{2 k+2}
\end{aligned}
$$

故只要证

$$
\frac{\sqrt{2 k+1}}{2 k+2}<\frac{1}{\sqrt{2 k+3}}
$$

即证 $(2 k+1)(2 k+3)<(2 k+2)^{2}$ ，
而上述不等式由于

$$
4 k^{2}+8 k+3<4 k^{2}+8 k+4
$$

因而是成立的. 于是，最后得

$$
\frac{1}{2} \cdot \frac{3}{4} \cdots \frac{2 k+1}{2 k+2}<\frac{1}{\sqrt{2 k+3}}
$$

即对于 $n=k+1$ 时,不等式也戊立。由旧纳法证毕。
11. 设 $c$ 为正整数, 而不为整数的平方, 且 $A / B$ 为确定实数 $\sqrt{c}$ 的分割，其中 $B$ 类包含所有合于 $b^{2}>c$ 的正有理数 $b$ ，而 $A$ 类包含所有其余的有理数。求证在 $A$ 类中无最大数，而在 $B$ 类中也无最小数。
证 设 $a \in A$. 若 $a \leqslant 0$, 则显然存在 $a^{\prime}>a\left(a^{\prime}>0\right)$ 且 $a^{\prime} \in A$. 故可设 $a>0$, 于是 $a^{2} \leqslant c$ 。但不可能有 $a^{2}=c$. 因若 $a^{2}=c$ ，设 $a=\frac{p}{q}, p$ 与 $q$ 为互质的正整数，则 $\frac{p^{2}}{q^{2}}=c$ 。由于 $c$ 是正整数，而 $p^{2}$ 与 $q^{2}$ 也是互质的，故必 $q=1$ ，从而 $c=p^{2}$ ，此与假定矛盾，故必 $a^{2}<c$ 。下面我们证明，存在正整数 $n$,使

$$
\left(a+\frac{1}{n}\right)^{2}<c,
$$

于是 $a$ ， $+\frac{1}{n}$ 也属于 $A$ 。
上述不等式相当于：

$$
a^{2}+\frac{2 a}{n}+\frac{1}{n^{2}}<c, \quad \frac{2 a}{n}+\frac{1}{n^{2}}<c-a^{2},
$$

若 $n$ 满足不等式

$$
\frac{2 a+1}{n}<c-a^{2}
$$

则上面的第二个不等式也自然能满足了。
为此，只要取

$$
n>\frac{2 a+1}{c-a^{2}}
$$

而这是佂为可能的。因此，不论 $a$ 为 $A$ 类内的怎样的数，在 $A$ 类内总能找到大于它的数，故 $A$ 类中无最大数。

同法可证 $B$ 类中也无最小数。
实质上，此处分割 $A / B$ 确定了一个无理数 $\sqrt{c}$ 。
12. 确定数 $\sqrt[3]{2}$ 的分割 $A / B$ 用下面的方法来作成： $A$ 类包含所有的有理数 $a$, 而 $a^{3}<2 ; B$ 类包含所有其余的有理数.证明在 $A$ 类中无最大数，而在 $B$ 类中也无最小数。
证 设 $a \in A$ 。即 $a^{3}<2$ 。下证必可取正整数 $n$ ，使

$$
\left(a+\frac{1}{n}\right)^{3}<2
$$

事实上，上式相当于 $\frac{3 a^{2}}{n}+\frac{3 a}{n^{2}}+\frac{1}{n^{3}}<2-a^{3}$ 。若 $a \leqslant 0$ ，取 $n=1$ 即可. 若 $a>0$, 注意到 $n \geqslant 1$, 即知若取 $n$ 充分大,使 $n>\frac{3 a^{2}+3 a+1}{2-a^{3}}$, 则上列各式均成立. 从而 $a+\frac{1}{n} \in$ $A$. 故 $A$ 中无最大数.

下设 $b \in B$, 则 $b^{3} \geqslant 2$.下证不可能有 $b^{3}=2$. 事实 上,若 $b^{b}=2$ ，设 $b=\frac{p}{q}, p$ 与 $q$ 为互质的正整数，则 $\frac{p^{3}}{q^{3}}=2, p^{3}$ $=2 q^{3}$ ，从而 $p^{3}$ 为偶数，因此 $p$ 必为偶数： $p=2 r, r$ 为正整数。由于 $q$ 与 $p$ 是互质的，故 $q$ 必为奇数，从而 $q^{2}$ 也为奇数。但 $\dot{q}^{3}=4 r^{3}$ ，故 $q^{3}$ 又必是偶数，因此矛盾。由此可知必有 $b^{3}>2$. 仿前面之证，可取正整数 $n$ ，使 $\left(b-\frac{1}{n}\right)^{3}>2$ ，从而 $b-\frac{1}{n} \in B$ 。由此可知 $B$ 类中无最小数。实质上，此处分割 $A / B$ 确定了一个无理数 $\sqrt[5]{2}$.
13. 作出适当的分割, 然后证明等式:
(a) $\sqrt{2}+\sqrt{8}=\sqrt{18}$;
(6) $\sqrt{2} \sqrt{3}=\sqrt{6}$.

证 (a) 作确定 $\sqrt{2}$ 的分割 $A / B$ : 一切有理数 $a \leqslant 0$ 以及满足 $a^{2}<2$ 的正有理数 $a$ 都归于 $A$ 类，一切满足 $b^{2}>2$ 的

正有理数 $b$ 归入 $B$ 类。又作确定 $\sqrt{8}$ 的分割 $A^{\prime} / B^{\prime}$ ；一切有理数 $a^{\prime} \leqslant 0$ 以及满足 $a^{\prime 2}<8$ 的正有理数 $a^{\prime}$ 归入 $A^{\prime}$类，一切满足 $b^{\prime 2}>8$ 的正有理数 $b^{\prime}$ 归入 $B^{\prime}$ 类。我们知道，根据实数加法的定义，满足不等式。
$a+a^{\prime}<c<b+b^{\prime}$ （对任何 $a \in A, b \in B, a^{\prime} \in A^{\prime}$ ， $b^{\prime} \in B^{\prime}$ )
的唯一实数 $c$ 就量 $\sqrt{2}+\sqrt{8}$. 因此,如果我们能证明恒有 $\left(a+a^{\prime}\right)^{2}<18$ （当 $a+a^{\prime}>0$ 时）， $\left(b+b^{\prime}\right)^{2}>18$ ，则有 $a+a^{\prime}<\sqrt{18}<b+b^{\prime}$. 于是得知 $\sqrt{18}=c=\sqrt{2}+$ $\sqrt{8}$ 。

若 $a+a^{\prime}>0$, 则 $a$ 与 $a^{\prime}$ 中至少有一个为正，从而由 $a^{2} a^{\prime 2}<16$ 知 $a a^{\prime}<4$, 从而 $\left(a+a^{\prime}\right)^{2}=a^{2}+a^{\prime 2}+2 a a^{\prime}$ $<2+8+8=18$; 同样, 因 $b^{2}>2, b^{\prime 2}>8, b>0, b^{\prime}>$ 0 , 故 $b^{2} b^{\prime 2}<16, b b^{\prime}>4,\left(b+b^{\prime}\right)^{2}=b^{2}+b^{\prime 2}+2 b b^{\prime}>$ $2+8+8=18$. 于是证毕.
(6) 作确定 $\sqrt{2}$ 的分割 $A / B$ 如（a）中所示，再作确定 $\sqrt{3}$的分割 $A_{1} / B_{1}$ : 一切有理数 $a_{1} \leqslant 0$ 以及满足 $a_{1}{ }^{2}<3$ 的正有理数 $a_{1}$ 归入 $A_{1}$ 类，一切满足 $b_{1}{ }^{2}>3$ 的正有理数 $b_{1}$ 师入 $B_{1}$ 类. 根据实数乘法的定义，满足 $a a_{1}<c_{1}<b b_{1}$ （对任何 $a \in A, a>0, a_{1} \in A_{1}$, $a_{1}>0, b \in B, b_{1} \in B_{1}$ )
的（正）实数 $c_{1}$ 存在唯一，它就是 $\sqrt{2} \cdot \sqrt{3}$ 。但由于当 $a$ $\in A, a>0, a_{1} \in A_{1}, a_{1}>0$ 时 $\left(a a_{1}\right)^{2}<6$ ，而当 $b \in B, b_{1}$ $\in B_{1}$ 时, $\left(b b_{1}\right)^{2}>6$. 故恒有 $a a_{1}<\sqrt{6}<b b_{1}$. 由此可知 $\sqrt{6}=c_{1}=\sqrt{2} \cdot \sqrt{3}$ 。证完。
14. 建立确定数 $2 \sqrt{3}$ 的分割。

解 先作分割 $A_{1} / B_{1}$ ，使之确定数 $\sqrt{2}$ 。
其次，作分割 $A / B$ ，其中 $A$ 类包含全体负有理数、零以及满足下述条件的正有理数 $a$ ：

如果有 $\frac{P}{q}$ （ $p 、 q$ 互质）局于 $A_{1}$ ，则有

$$
a^{q}<2^{p} ;
$$

而其余的正有理数归入 $B$ 类.
这样的分割 $A / B$ 就确定数 $2 \sqrt{2}$ 。
15. 求证任何非空且下方有界的数集有下确界,而任何非空且上方有界的数集有上确界。
证 不失一般性，只证本题的后半部分，分两种情形：
（1） $A$ 中有最大数 $\bar{a}$ 。设 $a \in A$, 此时则有 $a \leqslant \bar{a}$ ，说明 $\bar{a}$ 为 $A$ 的上界。 又由于 $\bar{a} \in A$, 故对 $A$ 的任何上界 $M$, 均有 $\bar{a} \leqslant M$, 故 $\bar{a}$ 为 $A$ 的有上确界。
（2） $A$ 中无最大数. 此时，作分割 $A_{1} / B_{1}$ ：取集 $A$ 的一切上界归入 $B_{1}$ 类，而其余的数归入 $A_{1}$ 类。这样， $A$ 中一切数全部落在 $A_{1}$ 内, $A_{1}$ 及 $A_{2}$ 均非空, 且 $A_{1}$ 中的数小于 $B_{1}$ 中的数，这确实是一个实数分部，易知由此分割所产生的实数 $\beta$ 是 $B_{1}$ 类中的最小数，即 $\beta$ 是 $A$ 的最小上界，从而 $\beta$ 是 $A$ 的上确界。
16. 证明一切有理真分式 $\frac{m}{n}$ （式中 $m$ 及 $n$ 为自然数，且 $0<m$ $<n$ ）的集合无最小及最大的元素。并求集合的上确界及下确界。
证 令 $E$ 表一切有理真分式 $\frac{m}{n}$ （式中正整数 $m, n$ 满足 0
$<m<n$ ) 所成的集合. 对任何 $\frac{m}{n} \in E$, 显然 $\frac{m+1}{n+1} \in E$且 $\frac{m}{n+1}>\frac{m}{n}$ ，又 $\frac{m^{2}}{n^{2}} \in E$ ，且 $\frac{m^{2}}{n^{2}}<\frac{m}{n}$ ；故 $E$ 中既无最大数，也无最小数. 显然

$$
\sup E=1, \quad \inf E=0
$$

17. 有理数 $r$ 满足不等式

$$
r^{2}<2
$$

求这些有理数 $r$ 所成集合的下确界和上确界。
解 用 $E$ 表所有满足 $r^{2}<2$ 的有理数 $r$ 所成的集合。我们知道，分割 $A / B$ 确定无理数 $\sqrt{2}$ ，这里 $A$ 表由一切非正有理数以及满足 $r^{2}<2$ 的正有理数 $r$ 所成的类， $B$ 表其余有理数构成的类，并且已证 $A$ 中无最大数，于是

$$
\sup E=\sup A=\sqrt{2} .
$$

同样，分割 $A^{\prime} / B^{\prime}$ 确定无理数 $-\sqrt{2}$ ，这里 $B^{\prime}$ 表由所有非负有理数以及满足 $r^{2}<2$ 的负有理数 $r$ 构成的类， $A^{\prime}$表其余有理数构成的类，并且 $B^{r}$ 中无最小数。于是，显然有

$$
\inf E=\inf B^{\prime} \doteq-\sqrt{2} .
$$

18. 理 $\{-x\}$ 为数的集合；这些数是与 $x \in\{x\}$ 符号相反的数. 证明等式：
(a) $\inf \{-x\}=-\sup \{x\} ;(6) \sup \{-x\}=-\inf \{x\}$.

证 (a) 设 inf $\{-x\}=m^{\prime}$, 则有:
(1) 当 $-x \in\{-x\}$ 时, $-x \geqslant m^{\prime}$;
（2）对于任何的正数 $\varepsilon$ ，存在有 $-x^{\prime} \in\{-x\}$ ，使

$$
-x^{\prime}<m^{\prime}+\varepsilon
$$

由（1）及（2）推得：
(3) 当 $x \in\{x\}$ 时, $x \leqslant-m^{\prime}$;
（4）对于任何的正数 $\varepsilon$ ，存在有 $x^{\prime} \in\{x\}$ ，使

$$
x^{\prime}>-m^{\prime}-\varepsilon
$$

由 (3) 及 (4) 知数 $-m^{\prime}=\sup \{x\}$, 即 $m^{\prime}=-\sup \{x\}$, 所以 $\inf \{-x\}=-\sup \{x\}$ 。
（6）设 $\sup \{-x\}=M^{\prime}$ ，则有:
(5) 当 $-x \in\{-x\}$ 时, $-x \leqslant M^{\prime}$;
（6）对于任何的正数 $\varepsilon$ ，存在有 $-x^{\prime} \in\{-x\}$ ，使

$$
-x^{\prime}>M^{\prime}-\varepsilon_{.}
$$

由(5)及(6) 推得:
（7）当 $x \in\{x\}$ 时， $x \geqslant-M^{\prime}$ ；
(8) 对于任何的正数 $\boldsymbol{E}$, 存在有 $x^{\prime} \in\{x\}$, 使

$$
\boldsymbol{x}^{\prime}<-\boldsymbol{M}^{\prime}+\boldsymbol{\varepsilon}
$$

由 (7) 及 (8) 知数 $-M^{\prime}=\inf \{x\}$, 即 $M^{\prime}=-\inf \{x\}$, 所以, $\sup \{-x\}=-\inf \{x\}$ 。
19. 设 $\{x+y\}$ 为所有 $x+y$ 这些和的集合，其中 $x \in\{x\}$ 及 $y \in\{y\}$ ，证明等式：
(a) $\inf \{x+y\}=\inf \{x\}+\inf \{y\}$;
(б) $\sup \{x+y\}=\sup \{x\}+\sup \{y\}$.

证 (a) 设 $\inf \{x\}=m_{1}, \inf \{y\}=m_{2}$, 则有:
（1）当 $x \in\{x\}, y \in\{y\}$ 时, $x \geqslant m_{1}, y \geqslant m_{2}$;
（2）对于任何的正数 $\epsilon$ ，存在有数 $x^{\prime} \in\{x\}, y^{\prime} \in\{y\}$ ，使

$$
x^{\prime}<m_{1}+\frac{\varepsilon}{2}, \quad y^{\prime}<m_{2}+\frac{\varepsilon}{2} .
$$

由 (1) 及（2）推得：
(3) 当 $x+y \in\{x+y\}$ 时（其中 $x \in\{x\}, y \in\{y\}$ ），

$$
x+y \geqslant m_{1}+m_{2}
$$

（4）对于任何的正数 $\varepsilon$ ，存在有 $x^{\prime}+y^{\prime} \in\{x+y\}$ （其中 $\left.x^{\prime} \in\{x\}, y^{\prime} \in\{y\}\right)$, 使

$$
x^{\prime}+y^{\prime}<\left(m_{1}+m_{2}\right)+\varepsilon .
$$

由（3）及（4）知数 $m_{1}+m_{2}=\inf \{x+y\}$ ，即

$$
\inf \{x+y\}=\inf \{x\}+\inf \{y\}
$$

（6）同法可证

$$
\sup (x+y\}=\sup \{x\}+\sup \{y\}
$$

20. 设 $\{x y\}$ 为所有 $x y$ 乘积的集合,其中 $x \in\{x\}$ 及 $y \in\{y\}$ ，且 $x \geqslant 0$ 及 $y \geqslant 0$ ，证明等式：
(a)inf $\{x y\}=\inf \{x\} \inf \{y\}$;
(6) $\sup \{x\} \sup \{y\}=\sup \{x y\}$.

证 （a）设 $\inf \{x\}=m_{1}, \inf \{y\}=m_{2}$ ，由于恒有 $x \geqslant 0, y$
$\geqslant 0$ 。故必 $m_{1} \geqslant 0, m_{2} \geqslant 0$ 。于是
（1）当 $x \in\{x\}, y \in\{y\}$ 时， $x \geqslant m_{1} \geqslant 0, y \geqslant m_{2} \geqslant 0$ ；
（2）对任何的正数 E ，存在有数 $x^{\prime} \in\{x\}, y^{\prime} \in\{y\}$ ，使

$$
0 \leqslant x^{\prime}<m_{1}+\varepsilon, 0 \leqslant y^{\prime}<m_{2}+\varepsilon .
$$

由（1）及（2）推得：
（3）当 $x y \in\{x y\}$ ，其中 $x \in\{x\}, y \in\{y\}, x y \geqslant m_{1} m_{2}$ ；
（4）对于任何的正数 $\varepsilon$ ，存在有 $x^{\prime} y^{\prime} \in\{x y\}$ (其中 $x^{\prime} \in$ $\{x\}, y^{\prime} \in\{y\}$ ，使

$$
0 \leqslant x^{\prime} y^{\prime}<\left(m_{1}+\varepsilon\right)\left(m_{2}+\varepsilon\right)=m_{1} m_{4}+\varepsilon^{\prime},
$$

其中 $\varepsilon^{\prime}=\left(m_{1}+m_{2}\right) \varepsilon+\varepsilon^{2}$ 。
由（3）及（4）知数 $m_{1} m_{2}=\inf \{x y\}$ ，即

$$
\inf \{x y\}=\inf \{x\} \inf \{y\}
$$

（6）同法可证

$$
\sup \{x y\}=\sup \{x\} \sup \{y\} .
$$

21. 求证不等式；
(a) $|x-y| \geqslant||x|-|y||$;
(б) $\left|x+x_{1}+\cdots+x_{n}\right| \geqslant|x|-\left(\left|x_{1}\right|+\cdots+\left|x_{n}\right|\right)$.

证 (a) 由 $|x-y|=|x+(-y)| \geqslant|x|-|-y|$

$$
=|x|-|y|,
$$

及

$$
\begin{aligned}
|x-y| & =|y-x| \geqslant|y|-|x| \\
& =-(|x|-|y|),
\end{aligned}
$$

即得

$$
|x-y| \geqslant||x|-|y||
$$

也可如下证明：由 $|x y| \geqslant x y$ 知

$$
x^{2}-2 x y+y^{2} \geqslant x^{2}-2|x y|+y^{2},
$$

则 $\quad(x-y)^{2} \geqslant(|x|-|y|)^{2}$,
开方即得

$$
|x-y| \geqslant||x|-|y||
$$

(Б) $\left|x+x_{1}+\cdots+x_{n}\right| \geqslant|x|-\left|x_{1}+\cdots+x_{n}\right|$,

而

$$
\begin{aligned}
& \left|x_{1}+\cdots+x_{n}\right| \leqslant\left|x_{1}\right|+\left|x_{2}+\cdots+x_{n}\right| \leqslant \cdots \\
& \leqslant\left|x_{1}\right|+\left|x_{2}\right|+\cdots+\left|x_{n}\right|
\end{aligned}
$$

所以，

$$
\left|x+x_{1}+\cdots+x_{n}\right| \geqslant|x|-\left(\left|x_{1}\right|+\cdots+\left|x_{n}\right|\right) .
$$

解不等式：
22. $|x+1|<0.01$.

解 由 $|x+1|<0.01$ 推得

$$
-0.01<x+1<0.01,
$$

所以，

$$
-1.01<x<-0.99 .
$$

23. $|x-2| \geqslant 10$.

解 由 $|x-2| \geqslant 10$ 推得

$$
x-2 \geqslant 10 \text { 或 } \quad x-2 \leqslant-10 \text {. }
$$

所以,
$" x \geqslant 12$ 或 $\quad x \leqslant-8$.
24. $|x|>|x+1|$.

解 两边平方，即得

$$
x^{2}>(x+1)^{2} \text { 或 } 2 x+1<0,
$$

于是, 有

$$
x<-\frac{1}{2} .
$$

25. $|2 x-1|<|x-1|$.

解 两 边平方，即得

$$
(2 x-1)^{2}<(x-1)^{2} \text { 或 } 3 x^{2}-2 x<0 \text {, }
$$

解之，䄍

$$
0<x<\frac{2}{3} .
$$

26. $|x+2|+|x-2| \leqslant 12$.

解 令 $x-2=t$, 则得

$$
|t+4|+|t| \leqslant 12 \text { 或 }|t+4| \leqslant 12-|t| .
$$

两边平方, 即有

$$
t^{2}+8 t+16 \leqslant 144-24|t|+t^{2},
$$

或

$$
3|t| \leqslant 16-t .
$$

将上式两端再平方，化简整理得

$$
t^{2}+4 t-32 \leqslant 0,
$$

于是, 有

$$
-8 \leqslant t \leqslant 4 .
$$

从而得

$$
-8 \leqslant x-2 \leqslant 4
$$

即

$$
-6 \leqslant x \leqslant 6 \quad \text { 或 } \quad|x| \leqslant 6 .
$$

27. $|x+2|-|x|>1$.

解 $1+|x|<|x+2|$, 将此式两端平方，化简得

$$
2|x|<4 x+3 .
$$

再平方之，化简得

$$
4 x^{2}+8 x+3>0
$$

于是, 有

$$
x>-\frac{1}{2} \quad \text { 或 } \quad x<-\frac{3}{2} .
$$

后者不适合，所以，

$$
x>-\frac{1}{2} .
$$

28. $||x+1|-|x-1||<1$.

解 两端平方，化简得

$$
x^{2}+\frac{1}{2}<\left|x^{2}-1\right|,
$$

即

$$
x^{2}-1>x^{2}+\frac{1}{2} \quad \text { 或 } \quad x^{2}-1<-\left(x^{2}+\frac{1}{2}\right) .
$$

前者不可能，所以，

$$
x^{2}-1<-\left(x^{2}+\frac{1}{2}\right) .
$$

即 $x^{2}<\frac{1}{4}$ ，解之得

$$
|x|<\frac{1}{2} .
$$

29. $|x(1-x)|<0.05$.

粰 由 $\left|x-x^{2}\right|<\frac{1}{20}$ 得

$$
x^{2}-x+\frac{1}{20}>0 \text { 或 } x^{2}-x-\frac{1}{20}<0 \text {, }
$$

解之得

$$
\left\{\begin{array}{l}
\frac{5-\sqrt{30}}{10}<x<\frac{5+\sqrt{30}}{10} \\
\frac{5+\sqrt{20}}{10}<x \text { 或 } \quad x<\frac{5-\sqrt{20}}{10},
\end{array}\right.
$$

即

$$
\begin{aligned}
& \frac{5-\sqrt{30}}{10}<x<\frac{5-\sqrt{20}}{10} \text { 或 } \\
& \frac{5+\sqrt{20}}{10}<x<\frac{5+\sqrt{30}}{10} .
\end{aligned}
$$

30. 证明恒等式

$$
\left(\frac{x+|x|}{2}\right)^{2}+\left(\frac{x-|x|}{2}\right)^{2}=x^{2}
$$

证 $\quad\left(\frac{x+|x|}{2}\right)^{2}+\left(\frac{x-|x|}{2}\right)^{2}$

$$
=\frac{1}{2} x^{2}+\frac{1}{2} x|x|+\frac{1}{2} x^{2}-\frac{1}{2} x|x|=x^{2} .
$$

31. 当测量长度 10 厘米时，绝对误差为 0.5 毫米；当测量㭱离 500 千米时，绝对误差等于 200 米，哪种测量较为精确？
解 用相对误差

$$
\delta=\frac{\Delta}{|a|}
$$

进行比较，其中 $a$ 为被测量的精确值，而 $\Delta$ 是绝对误差.
对于前者， $\delta=\frac{0.5 \times 0.1}{10}=0.5 \%$ ，
对于后者， $\delta=\frac{200}{500 \times 1000}=0.04 \%$ ，
所以，后者测量较为精确。
32. 设数

$$
x=2.3752
$$

的相对误差为 $1 \%$ ，试求此数包含若干位准确数字？
解 因为 $\frac{\Delta}{2.3752}=0.01$, 所以 $\triangle=0.023752$ 。
因而，此数包含两位准确数字。
33. 数

$$
x=12.125
$$

创含三位准确数字。试求此数的相对误差？
要 因为 $x$ 包含三位准确数字，所以 $\Delta<0.05$ 。早是得相对误差

$$
\delta=\frac{\Delta}{|x|}<\frac{0.05}{12.125}<0.42 \%
$$

即

$$
\delta<0.42 \%
$$

34. 矩形的边等于：

$$
\begin{aligned}
& x=2.50 \text { 理米 } \pm 0.01 \text { 俚米, } \\
& y=4.00 \text { 堚米 } \pm 0.02 \text { 厘米. }
\end{aligned}
$$

这个矩形的面积 $S$ 界于甚么范围内？设其边长取平均值时，矩形面积的绝对误差 $\Delta$ 和相对误差 $\delta$ 为何

$$
\text { 解 } \begin{aligned}
S_{\text {min }} & =(2.50-0.01)(4.00-0.02) \\
& =9.9102(\text { 平方厘米 })^{*},
\end{aligned}
$$

$$
\begin{aligned}
& S_{\text {max }}=(2.50+0.01)(4.00+0.02) \\
&=10.0902 \text { (平方厘米), } \\
& S_{\text {min }} \leqslant S \leqslant S_{\max }, \\
& S_{\text {平绝 }}=2.50 \times 4.00=10 \text { (平方厘米), } \\
& \Delta_{1}=10.0902-10=0.0902 \text { (平方厘米), } \\
& \Delta_{2}=10-9.9102=0.0898 \text { (平方厘米); } \\
& \Delta \leqslant \max \left(\Delta_{1}, \Delta_{2}\right)=0.0902 \text { (平方厘米), } \\
& \delta=\frac{\Delta}{10} \leqslant \frac{0.0902}{10}<0.91 \% .
\end{aligned}
$$

*）以后各题简写为厘米 ${ }^{2}$ ，厘米 ${ }^{3}$ 等.
35. 物体的重量 $P=12.59$ 克士 0.01 克, 其体积 $V=3.2$ 厘米 $^{3} \pm 0.2$ 厘米 ${ }^{3}$ 。若对物体的重量和体积都取其平均值，试求物体的比重，并估计比重的绝对误差和相对误差。
解 比重 $\dot{C}=\frac{12.59}{3.2}$ 克 $/$ 厘米 $^{3}=3.93$ 克 $/$ 厘米 $^{3}$ 。

$$
C_{\mathrm{max}}=\frac{12.60}{3.0} \text { 克 } / \text { 厘米 }^{3}=4.20 \text { 克 } / \text { 厘米 }^{3} \text {, }
$$

$$
\begin{aligned}
& C_{\min }= \frac{12.58}{3.4} \text { 克 } / \text { 厘米 }{ }^{3}=3.70 \text { 克 } / \text { 厘米 }^{3}, \\
& C_{\min } \leqslant C \leqslant C_{\max },
\end{aligned}
$$

$\Delta_{1}=C_{\max }-C=0.27$ 克 $/$ 厘米 $^{3}$ ，
$\Delta_{2}=C-C_{\text {min }}=0.23$ 克 / 厘 米 ${ }^{3} ;$
$\Delta \leqslant \max \left(\Delta_{1}, \Delta_{2}\right)=0.27$ 克/ 厘米;
一般地, 比重为（3.93土0.27）克/厘米；

$$
\delta \leqslant \frac{0.27}{3.70}<7.3 \%
$$

## $36^{+}$. • 圆半汞

$$
r=7.2 \text { 米士 } 0.1 \text { 米. }
$$

若取 $\pi=3.14$, 则求出的圆面积的最小相对误差为何?解 圆面积 $A=\pi \times 7.2^{2} \approx 51.84 \pi\left(*^{2}\right)$

$$
\begin{aligned}
\Delta_{1} & =\pi(7.2+0.1)^{2}-\pi \cdot 7.2^{2}=1.45 \pi \\
\Delta_{2} & =\left|\pi(7.2-0.1)^{2}-\pi \cdot 7.2^{2}\right|=1.43 \pi \\
& \Delta \leqslant \max \left(\Delta_{1}, \Delta_{2}\right)=1.45 \pi\left(\text { 米 }^{2}\right)
\end{aligned}
$$

即一般的圆面积 $A$ 为 $(51.84 \pm 1.45) \pi\left({ }^{2}{ }^{2}\right)$ ，故

$$
\delta \leqslant \frac{1.45 \pi}{51.84 \pi}<2.80 \%
$$

37. 对直角平行六面体测得

$$
\begin{aligned}
& x=24.7 \text { 米 } \pm 0.2 \text { 米; } \\
& y=6.5 \text { 米 } \pm 0.1 \text { 米; } \\
& z=1.2 \text { 米 } \pm 0.1 \text { 米. }
\end{aligned}
$$

这个平行六面体的体积 $V$ 界于甚么范围内 3 若测量的各结果都取其平均值，则求出的平行六面体的体积可能有的绝对哒差和相对误差为何？
样 $24.5 \times 6.4 \times 1.1 \leqslant V \leqslant 24.9 \times 6.6 \times 1.3$
即 172.480 米 $^{3} \leqslant V \leqslant 213.642$ 米 $^{3}$ 。
当 $x, y, z$ 均取平均值时,

$$
\begin{aligned}
& V=24.7 \times 6.5 \times 1.2=192.660 \text { 米 }^{3} \\
& \Delta_{1}=213.642-192.660=20.982\left(\text { 米 }^{3}\right) \\
& \Delta_{2}=.192 .660-172.480=20.180\left(\text { 米 }^{3}\right) .
\end{aligned}
$$

[^1]于是,

$$
\begin{aligned}
& \Delta \leqslant 20.982 \text { 米 }^{3} \\
& \delta \leqslant \frac{20.982}{172.480} \approx 12.2 \%
\end{aligned}
$$

38. 测量正方形的边 $x$ ，此处 2 米 $<x<3$ 米，应有多小的绝对误差，才能使此正方形面积有可能精确到 0.001 米 $^{2} ?$续 按题设我们有 $0<x^{2}-4<0.001$ 或 $0<9-x^{2}<$ 0.001 ，解之得

$$
\text { 2. } 99983<x<3 \text { 或 } 2<x<2.00024 \text {. }
$$

因此， $\triangle$ 取二者中误差较小者，即

$$
\Delta \leqslant 0.00017 \text { (米) }=0.17 \text { 毫米, }
$$

故当边长 $x$ 的绝对误 差不趋过 0.17 襄米时，就能使此正方形的面积精确到 0.001 米 ${ }^{2}$ 。
39. 假定矩形每边的长皆不超过 10 米，为了使根据测量所计算出来的面积与原面积之差不超过 0.01 平方米，问测量矩形的边 $x$ 与 $y$ 时，许可的绝对误差 $\Delta$ 的值多大"）?
解 按题设我们有

$$
(x+\Delta)(y+\Delta)-x y \leqslant 0.01,
$$

即

$$
\Delta^{2}+(x+y) \Delta \leqslant 0.01,
$$

由于 $x \leqslant 10$ 及 $y \leqslant 10$ ，所以只要

$$
\Delta^{2}+20 \Delta \leqslant 0.01 \text { 或 } \Delta^{2}+20 \Delta-0.01 \leqslant 0
$$

即可. 解之, 得

$$
\begin{aligned}
\Delta & \leqslant \frac{-20+\sqrt{20^{2}+0.04}}{2}=-10+\frac{20.00099}{2} \\
& =0.000499<0.0005(*) .
\end{aligned}
$$

*）此题假设 $x ; y$ 有相等的绝对误差. 又原著上为 " 0.01平方米"，而误译为" 0.01 平方厘米"。
40. 设 $\delta(x)$ 及 $\delta(y)$ 为数 $x$ 和 $y$ 的相对误差， $\delta(x y)$ 为数 $x y$ 的相对误差. 求证：

$$
\delta(x y) \leqslant \delta(x)+\delta(y)+\delta(x) \delta(y) .
$$

证 设 $x=a+\Delta_{x}, \quad y=b+\Delta_{y}$,
其中 $a$ 及 $b$ 分別是 $x$ 及 $y$ 的精确值， $\Delta_{x}$ 及 $\Delta_{y}$ 是绝对误差, 则有

$$
x y-a b=b \Delta_{y}+a \Delta_{y}+\Delta_{x} \cdot \Delta_{y}
$$

于是，

$$
\begin{aligned}
& \Delta=|x y-a b| \\
& \quad \leqslant|b| \cdot \Delta_{x}+|a| \cdot \Delta_{y}+\Delta_{x} \cdot \Delta_{y}
\end{aligned}
$$

最后即得

$$
\delta(x y)=\frac{\Delta}{|a b|} \leqslant \frac{\Delta_{x}}{|a|}+\frac{\Delta_{y}}{|b|}+\frac{\Delta_{x}}{|a|} \cdot \frac{\Delta_{y}}{|b|} .
$$

此即

$$
\delta(x y) \leqslant \delta(x)+\delta(y)+\delta(x) \delta(y) .
$$

## §2. 叙列的理论

$1^{\circ}$ 級列的极榢的概念 假设对于任何的 $\varepsilon>0$ ，有数 $N=N(\varepsilon)+$ 使当 $n>N$ 时 $\left|x_{n}-a\right|<\varepsilon$ ，
则称叙列 $x_{1}, x_{2} \cdots, x_{*}, \cdots$ 有极限 $a$ （或者说，收敛于 $a$ ）亦即

$$
\lim _{n \rightarrow \infty} x_{n}=a
$$

其中, 若

$$
\lim _{n \rightarrow \infty} x_{n}=0,
$$

则称 $x_{n}$ 为无穷小。
没有极限的叙列，称为发散的。
$2^{\circ}$ 极限存在的准则
(1)设

$$
y_{n} \leqslant x_{n} \leqslant z_{n}
$$

及

$$
\lim _{n \rightarrow \infty} y_{n}=\lim _{n \rightarrow \infty} x_{n}=c,
$$

则

$$
\lim _{\pi \rightarrow \infty} x_{n}=c
$$

（2）单调而且有界的叙列有极限。
（3）哥西判别法 叙列 $\left\{x_{n}\right\}$ 的极限存在的必婁而且充分的条件是：对于任何的 $\varepsilon>0$ ，有数 $N=N(\varepsilon)$ ，使当 $n>N$ 和 $p>0$ 时， $\mid x_{n}-$ $x_{n+p} \mid<\varepsilon$ 。
$3^{a}$ 关于叙列的极限的基本定理 设 $\lim _{n \rightarrow \infty} x_{n}$ 和 $\lim _{n \rightarrow \infty} y_{n}$
存在，则有：
(1)若 $x_{n} \leqslant y_{n}$ ，则 $\lim _{n \rightarrow \infty} x_{n} \leqslant \lim _{n \rightarrow \infty} y_{n}$ ；
(2) $\lim _{n \rightarrow \infty}\left(x_{4} \pm y_{n}\right)=\lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}$ ，
(3) $\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\lim _{n \rightarrow \infty} x_{n} \lim _{n \rightarrow \infty} y_{n}$;
(4) 若 $\lim _{n \rightarrow+\infty} y_{n} \neq 0$, 则 $\lim _{n \rightarrow \infty} \frac{x_{\mathrm{a}}}{y_{n}}=\frac{\lim _{n} x_{n}}{\lim _{n+\infty}^{\infty} y_{n}}$.
$4^{a}$ 数 $e$ ，叙列

$$
\left(1+\frac{1}{n}\right)^{n} \quad(n=1,2, \cdots)
$$

有确定的极限

$$
\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e=2.7182818284 \cdots
$$

$5^{\circ}$ 无穷极限 符号

$$
\lim _{n \rightarrow \infty} x_{n}=\infty
$$

表示对于任何的 $E>0$ ，有数 $N=N(E)$ ，使
当 $n>N$ 时， $\left|x_{n}\right|>E$ 。
$5^{\circ}$ 聚点 设已知叙列 $x_{n}(n=1,2, \cdots)$ 有子叙列

$$
x p_{1}, x p_{2}, \cdots, x p_{n} \cdots
$$

适合

$$
\lim _{n \rightarrow \infty} x_{\rho_{n}}=\xi
$$

则称数 $E\left(\right.$ 或符号 $\infty$ ) 为已知数列 $a_{n}(n=1,2, \cdots)$ 的聚点。
一切有界的叙列至少有一个有穷的聚点（婆尔植诺 外尔斯特拉斯原理）、若这个聚点是唯一的，则它即为已知叙列的有穷枝限。

銠列 $x_{n}$ 的最小聚点（有穷的或无穿的）

$$
\varliminf_{n \rightarrow \infty} x_{n}
$$

称为下极限，而它的最大筫点

$$
\lim _{n \rightarrow \infty} x_{n}
$$

称为此叙列的上极限
等式

$$
\lim _{n+\infty} x_{n}=\varlimsup_{n+\infty} x_{n}
$$

为叙列 $x_{n}$ 的（有穷或无穷）极限存在的必要而且充分的条件。
41. 设

$$
x_{n}=\frac{n}{n+1} \quad(n=1,2, \cdots)
$$

证明

$$
\lim _{n \rightarrow \infty} x_{n}=1,
$$

即：对于任一个给定的 $\varepsilon>0$ ，求数 $N=N(\varepsilon)$
使得
在 $n>N$ 时, $\left|x_{n}-1\right|<\varepsilon$ 。
埧下表：

| $\epsilon$ | 0.1 | 0.01 | 0.001 | 0.0001 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $N$ |  | $\cdots$ |  |  |  |

证 $\left|x_{n}-1\right|=\frac{1}{n+1}$. 仕给 $\varepsilon>0$, 要 $\left|x_{n}-1\right|<\varepsilon$ 。只

要

$$
\frac{1}{n+1}<\varepsilon .
$$

即只要 $n>\frac{1}{\epsilon}-1$. 可取

$$
N=N(\varepsilon)=\left[\frac{1}{\varepsilon}\right],
$$

则当 $n>N$ 时， $\left|x_{n}-1\right|<\varepsilon$ 。所以，

| $\lim _{n \rightarrow \infty} \boldsymbol{x}_{n}=1$ |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\varepsilon$ | 0.1 | 0.01 | 0.001 | 0.0001 | $\cdots$ |
| $N$ | 10 | 100 | 1000 | 10000 | $\ldots$ |

42. 假若：

$$
\begin{aligned}
& \text { (a) } x_{n}=\frac{(-1)^{n+1}}{n} ; \text { (c) } \frac{2 n}{n^{3}+1} ; \\
& \text { (в) } x_{n}=\frac{1}{n!} ; \text { (г) } x_{n}=(-1)^{n} \cdot 0.999^{*}
\end{aligned}
$$

对于任何的 $\varepsilon>0$ ，求出数 $N=N(\varepsilon)$ ，使

$$
\text { ， 当 } n>N \text { 时， } x_{n} \mid<\varepsilon \text { ； }
$$

即证明 $x_{n}(n=1,2, \cdots)$ 为无穿小（就是说，有极限值为 $0)$

对应着上面四种情形，塿下表：

| $\epsilon$ | 0.1 | 0.01 | 0.001 | $\cdots$ |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $N$ |  |  |  |  |  |

证 (a) $\left|x_{n}\right|=\frac{1}{n}$. 任给 $\varepsilon>0$, 要 $\left|x_{n}\right|<\varepsilon$, 只要

$$
\frac{1}{n}<\varepsilon,
$$

即只要 $n>\frac{1}{\varepsilon}$. 取 $N=\left[\frac{1}{\varepsilon}\right]^{*}$, 则当 $n>N$ 时， $\left|x_{n}\right|<\varepsilon$ ，所以，

$$
\begin{aligned}
& \quad \lim _{n \rightarrow \infty} x_{n}=0 . \\
& (6)\left|x_{n}\right|=\frac{2 n}{n^{3}+1}<\frac{2}{n^{2}} \text {. 任给 } \varepsilon>0 \text {, 要 }\left|x_{n}\right|<\varepsilon \text {, 只 }
\end{aligned}
$$

要

$$
\frac{2}{n^{2}}<\varepsilon
$$

即只要 $n>\sqrt{\frac{2}{\varepsilon}}$. 取 $N=\left[\sqrt{\frac{2}{\varepsilon}}\right]$, 则当 $n>N$ 时, $\left|x_{n}\right|<$ $\varepsilon$, 所以,

$$
\lim _{n \rightarrow \infty} x_{n}=0
$$

$$
\text { (в) }\left|x_{n}\right|=\frac{1}{n!} \leqslant \frac{1}{2^{n-1}} \text {. 任给 } \epsilon>0 \text {, 要 }\left|x_{n}\right|<\epsilon \text {, 只要 }
$$

即只要 $n>1+\log _{2} \frac{1}{\varepsilon}$, 取

$$
N=\left[\log _{2} \frac{1}{\varepsilon}\right)+1
$$

则当 $n>N$ 时, $\left|x_{n}\right|<\varepsilon$, 所以,

$$
\lim _{n \rightarrow \infty} x_{n}=0
$$

（г） $\left|x_{n}\right|=0.999^{n}$ 。任给 $\varepsilon>0$ ，要 $\left|x_{n}\right|<\varepsilon$ ，只要 nlg0. $999<1 g \varepsilon$.
由于 $\lg 0.999<0$ ，故只要 $\left.n>\frac{\lg \varepsilon}{\lg 0.999} \approx 2500 \lg \frac{1}{E} . *\right)$

取

$$
N=\left[2500 \lg \frac{1}{\varepsilon}\right]
$$

则当 $n>N$ 时， $\left|x_{n}\right|<\varepsilon$ ，所以

$$
\lim _{n \rightarrow \infty} x_{n}=0
$$

填下表：

| $\varepsilon$ |  | 0.1 | 0.01 | 0.001 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| (a) | $N$ | 10 | 100 | 1000 | $\cdots$ |
| (6) | $N$ | 4 | 14 | 44 | $\cdots$ |
| (в) | $N$ | 4 | 7 | 10 | $\ldots$ |
| (г) | $N$ | 2500 | 5000 | 7500 | $\ldots$ |

*）或取 $N \geqslant \frac{1}{\varepsilon}$ 。 以下各题类似，不再一一说明。

*     * ）査四位数学用表所得的数据。

43. 证明叙列
（a） $x_{n}=(-1)^{n} n$ ，(6) $x_{n}=2^{\sqrt{n}},(н) x_{t}=\lg (\lg n)(n \geqslant 2)$
当 $n \rightarrow \infty$ 时，有无穷极限（即成为无穷大），即；
对任意的 $E>0$ ，求数 $N=N(E)$ ，使
当 $n>N$ 时， $\left|x_{n}\right|>E$ 。

对应着上面的毎一种情形，填下゙表：

| $E$ | 10 | 100 | 1000 | 10000 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $N$ |  |  |  |  |  |

证 （a） $\left|x_{n}\right|=n$ 。任给 $E>0$ ，要 $\left|x_{n}\right|>E$ ，只要

$$
n>E .
$$

取 $N=[E]$ ，则当 $n>N$ 时， $\left|x_{n}\right|>E$ ，所以，

$$
\lim _{n \rightarrow \infty} x_{n}=\infty
$$

(6) $\left|x_{n}\right|=2^{\sqrt{n}}$, 任给 $E>0$ ，要 $\left|x_{n}\right|>E$ ，只要 $2^{\sqrt{n}}$ $>$ E.
即只要 $n>\left(\frac{\lg E}{\lg 2}\right)^{2}$. 取

$$
N=\left[\left(\frac{\lg E}{\lg 2}\right)^{2}\right],
$$

则当 $n>N$ 时, $\left|x_{n}\right|>E$, 所以

$$
\lim _{n \rightarrow \infty} x_{3}=\infty .
$$

(в) 当 $n>10$ 时, $\lg n>1$ 及 $\lg (\lg n)>0$.

任给 $E>0$ ，要 $\left|x_{n}\right|>E$ ，只要

$$
\lg (\lg n)>E,
$$

即只要 $n>10^{\left(10^{E}\right)}$ ，取

$$
N=\left[10^{\left(10^{E}\right)}\right],
$$

则当 $n>N$ 时， $\left|x_{n}\right|>E$ ，所以，

$$
\lim _{n \rightarrow \infty} x_{n}=\infty .
$$

填下表：

| $E$ |  | 10 | 100 | 1000 | 10000 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $(\mathrm{a})$ | $N$ | 10 | 100 | 1000 | 10000 | $\ldots$ |
| $(6)$ | $N$ | 11 | 44 | 99 | 176 | $\cdots$ |
| $\left(B_{B}\right)$ | $N$ | $19^{\left(10^{10}\right)}$ | $10^{\left(19^{100}\right)}$ | $10^{\left(10^{1009}\right)}$ | $10^{\left(10^{10000}\right)}$ | $\cdots$ |

## 44. 求证

$$
x_{n}=n^{(\cdots 1)^{n}} \quad(n=1,2, \cdots)
$$

无界，但当 $n \rightarrow \infty$ 时，它并不成为无穷大。
证 因为 $x_{n}=n^{(\cdot 1)^{n}}=\left\{\begin{array}{l}2 k, \text { 当 } n=2 k, k \text { 为自然数， } \\ \frac{1}{2 k+1}, \text { 当 } n=2 k+1,\end{array}\right.$
所以，

$$
x_{2 k} \rightarrow \infty, \quad x_{2 k+1} \rightarrow 0 \quad(k \rightarrow \infty) .
$$

由于 $x_{2 k} \rightarrow \infty$ ，故 $x_{n}$ 无界；但因 $x_{2 k+1} \rightarrow 0$ ，故 $x_{n}$ 并不趋于无穷大。
45. 用不等式表示下列各式:
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-038.jpg?height=101&width=1243&top_left_y=1269&top_left_x=281)
解（a）对于任给的正数 $E$ ，存在有自然数 $N=N(E)$ ，使当 $n>N$ 时， $\left|x_{n}\right|>E$ ，
此即 $\lim _{x \rightarrow \infty} x_{n}=\infty$ 。
（6）对于任给的正数 $E$ ，存在有自然数 $N=N(E)$ ，使当 $n>N$ 时， $x_{n}<-E$ ，
此即 $\lim _{n \rightarrow \infty} x_{n}=-\infty$ 。
（в）对于任给的正数 $E$ ，存在有自然数 $N=N(E)$ ，使当 $n>N$ 时， $x_{n}>E$ ，
此即 $\lim _{n \rightarrow \infty} x_{n}=+\infty$ 。
设 $n$ 跑过自然数列，求下列各式之值：
46. $\lim _{n \rightarrow \infty} \frac{10000 n}{n^{2}+1}$.

解 $\lim _{n \rightarrow \infty} \frac{10000 n}{n^{2}+1}=\lim _{n \rightarrow \infty} \frac{10000}{n+\frac{1}{n}}=0$ 。
47. $\lim _{n \rightarrow m}(\sqrt{n+1}-\sqrt{n})$.

解 $\lim _{n \rightarrow \infty}(\sqrt{n+1}-\sqrt{n})$

$$
\begin{aligned}
& =\lim _{n \rightarrow \infty} \frac{(\sqrt{n+1}-\sqrt{n})(\sqrt{n+1}+\sqrt{n})}{\sqrt{n+1}+\sqrt{n}} \\
& =\lim _{n \rightarrow \infty} \frac{1}{\sqrt{n+1}+\sqrt{n}}=0 .
\end{aligned}
$$

48. $\lim _{n \rightarrow \infty} \frac{\sqrt[3]{n^{2}} \sin n!}{n+1}$.

解 因为 $\sin n$ ：有界： $|\sin n!| \leqslant 1$ 及 $\frac{\sqrt[3]{n^{2}}}{n+1} \rightarrow 0(n \rightarrow \infty)$,所以，

$$
\lim _{n \rightarrow \infty} \frac{\sqrt[3]{n^{2}} \sin n!}{n+1}=0
$$

49. $\lim _{x \rightarrow \infty} \frac{(-2)^{n}+3^{n}}{(-2)^{n+1}+3^{n+1}}$.

解 $\lim _{n \rightarrow \infty} \frac{(-2)^{n}+3^{n}}{(-2)^{n+1}+3^{n+1}}=\lim _{n \rightarrow \infty} \frac{\left(-\frac{2}{3}\right)^{n} \cdot \frac{1}{3}+\frac{1}{3}}{\left(-\frac{2}{3}\right)^{n+1}+1}=\frac{1}{3}$.
50. $\lim _{n \rightarrow \infty} \frac{1+a+a^{2}+\cdots+a^{n}}{1+b+b^{2}+\cdots+b^{n}}(|a|<1,|b|<1)$.

解 $\lim _{n \rightarrow \infty} \frac{1+a+a^{2}+\cdots+a^{n}}{1+b+b^{2}+\cdots+b^{n}}=\lim _{n \rightarrow \infty} \frac{\frac{1-a^{n+1}}{1-a}}{\frac{1-b^{n+1}}{1-b}}=\frac{1-b}{1-a^{2}}$.
51. $\lim _{n \rightarrow \infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n-1}{n^{2}}\right)$.

解 $\lim _{n \rightarrow \infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n-1}{n^{2}}\right)=\lim _{n \rightarrow \infty} \frac{(n-1) n}{2 n^{2}}=\frac{1}{2}$.
52. $\lim _{n \rightarrow \infty}\left[\frac{1}{n}-\frac{2}{n}+\frac{3}{n}-\cdots+\frac{(-1)^{n-1} n}{n}\right]$.

解 当 $n=2 k$ 时 ( $k$ 为自然数),
$\frac{1}{n}-\frac{2}{n}+\frac{3}{n}-\cdots+\frac{(-1)^{n-1} n}{n}$
$=\frac{1}{2 k}-\frac{2}{2 k}+\frac{3}{2 k}-\cdots-\frac{2 k}{2 k}=\frac{-k}{2 k}=-\frac{1}{2} ;$
当 $n=2 k+1$,
$\frac{1}{n}-\frac{2}{n}+\frac{3}{n}-\cdots+\frac{(-1)^{n-1} n}{n}$
$=\frac{1}{2 k+1}-\frac{2}{2 k+1}+\frac{3}{2 k+1}-\cdots+\frac{2 k+1}{2 k+1}$
$=\frac{k+1}{2 k+1} \rightarrow \frac{1}{2}$ ；
由于取不同方式时，所得的极限值不同，所以，极限

$$
\lim _{n \rightarrow \infty}\left[\frac{1}{n}-\frac{2}{n}+\frac{3}{n} \cdots+\frac{(-1)^{n-1} n}{n}\right]
$$

不存在.
53. $\lim _{n \rightarrow \infty}\left[\frac{1^{2}}{n^{3}}+\frac{2^{2}}{n^{3}}+\cdots+\frac{(n-1)^{i}}{n^{3}}\right]$.

解 $\lim _{n \rightarrow \infty}\left[\frac{1^{2}}{n^{3}}+\frac{2^{2}}{n^{3}}+\cdots+\frac{(n-1)^{2}}{n^{3}}\right]$
$=\lim _{n \rightarrow \infty}\left[\frac{1}{n^{3}} \cdot \frac{(n-1) n(2 n-1)}{6}\right]=\frac{1}{3}$.
54. $\lim _{n \rightarrow \infty}\left[\frac{1^{2}}{n^{3}}+\frac{3^{2}}{n^{3}}+\cdots+\frac{(2 n-1)^{2}}{n^{3}}\right]$.

解 设 $f(n)=\frac{1^{2}}{n^{3}}+\frac{2^{2}}{n^{3}}+\cdots+\frac{(n-1)^{2}}{n^{3}}$ ，由 53 题
即得 $\lim _{n \rightarrow \infty}\left[\frac{1^{2}}{n^{3}}+\frac{3^{2}}{n^{3}}+\cdots+\frac{(2 n-1)^{2}}{n^{3}}\right]$

$$
=\lim _{n \rightarrow \infty}[8 f(2 n)-4 f(n)]=\frac{4}{3} .
$$

55. $\lim _{n \rightarrow \infty}\left(\frac{1}{2}+\frac{3}{2^{2}}+\frac{5}{2^{3}}+\cdots+\frac{2 n-1}{2^{n}}\right)$.

解 设 $f(n)=\frac{1}{2}+\frac{3}{2^{2}}+\frac{5}{2^{3}}+\cdots+\frac{2 n-1}{2^{n}}$,

$$
g(n)=1+\frac{1}{2}+\cdots+\frac{1}{2^{*-1}},
$$

则有 $2 f(n+1)-g(n)=f(n)+1$,
又由 $2 f(n+1)-f(n)=f(n)+\frac{2 n+1}{2^{n}}=g(n)+1$,
故

$$
f(n)=g(n)+1-\frac{2 n+1}{2^{n}} .
$$

而 $\lim _{n \rightarrow \infty}[g(n)+1]=3$ 及 $\lim _{n \rightarrow \infty} \frac{2 n+1}{2^{n}}=0^{*}$ ，故得

$$
\lim _{n \rightarrow \infty}\left(\frac{1}{2}+\frac{3}{2^{2}}-\frac{5}{2^{3}}+\cdots+\frac{2 n-1}{2^{*}}\right)=3
$$

* ）参看 58 题

56. $\lim _{n \rightarrow \infty}\left[-\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}\right]$.

解 $\frac{1}{1-2}=1-\frac{1}{2}$,

$$
\frac{1}{2 \cdot 3}=\frac{1}{2}-\frac{1}{3}, \cdots \cdots,
$$

$$
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1},
$$

相加之，得 $\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}$

$$
=1-\frac{1}{n+1}
$$

故 $\lim _{n \rightarrow m}\left[\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}\right]$

$$
=\lim _{n \rightarrow \infty}\left(1-\frac{1}{n+1}\right)=1
$$

57. $\lim _{n \rightarrow \infty}(\sqrt{2} \cdot \sqrt[4]{2} \cdot \sqrt[8]{2} \cdots \sqrt[2 n]{2})$.

解 由于 $\sqrt{2} \cdot \sqrt[4]{2} \cdot \sqrt[8]{2} \cdots \sqrt[2 n]{2}$

$$
\begin{aligned}
& =2\left(\frac{1}{2}+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\cdots+\frac{1}{2^{4}}\right) \\
& =2\left[\frac{1}{2} \cdot \frac{1-\left(\frac{1}{2}\right)^{1}}{1-\frac{1}{2}}\right]
\end{aligned}
$$

故 $\lim _{n \rightarrow \infty}(\sqrt{2} \cdot \sqrt[4]{2} \cdot \sqrt[8]{2} \cdots \sqrt[2 n]{2})$

$$
=\lim _{x \rightarrow \infty} 2\left[\frac{1}{2} \cdot \frac{1 \cdot\left(\frac{1}{2} j\right.}{1-\frac{1}{2}}\right]=2
$$

证明下列等式：
58. $\lim _{n \rightarrow \infty} \frac{n}{2^{n}}=0$.

证 因为 $2^{n}=(1+1)^{n}=1+n+\frac{n(n-1)}{2}+\cdots+1$

$$
>\frac{n(n-1)}{2}(n>2),
$$

故 $\quad 0<\frac{n}{2^{*}}<\frac{2}{n-1}$ ；
又因为 $\lim _{n \rightarrow \infty} \frac{2}{n-1}=0$, 所以，

$$
\lim _{n \rightarrow \infty} \frac{n}{2^{n}}=0
$$

59. $\lim _{x \rightarrow \infty} \frac{2^{n}}{n!}=0$.

证 因为 $0<\frac{2^{n}}{n!}=\frac{2}{1} \cdot \frac{2}{2} \cdots \frac{2}{n} \leqslant \frac{4}{n}$ 及 $\lim _{n \rightarrow \infty} \frac{4}{n}=0$, 所以,

$$
\lim _{n \rightarrow \infty} \frac{2^{n}}{n!}=0
$$

60. $\lim _{n \rightarrow \infty} \frac{n^{k}}{a^{n}}=0 \quad(a>1)$.

$$
\text { 证 令 } a=1+\lambda \quad(\lambda>0) \text {, }
$$

则 $a^{n}=(1+\lambda)^{n}=1+n \lambda+\frac{n(n-1)}{2} \lambda^{2}+\cdots$

$$
+\lambda^{n}>\frac{n(n-1)}{2} \cdot \lambda^{2} \quad(n>2) .
$$

当 $n>2$ 时, $n-1>\frac{n}{2}$, 此时,

$$
a^{n}>\frac{n^{2}}{4} \lambda^{2}=\frac{n^{2}(a-1)^{2}}{4} .
$$

分三种情形：
（1）当 $k \leqslant 0$ 时，这时显然有

$$
\lim _{n \rightarrow \infty} \frac{n^{k}}{a^{n}}=\lim _{n \rightarrow \infty} \frac{1}{a^{n}+n}=0
$$

（2）当 $k=1$ 时，

$$
0<\frac{n^{k}}{a^{*}}=\frac{n}{a^{n}}<\frac{4 n}{n^{2}(a-1)^{2}},
$$

而 $\frac{4 n}{n^{2}(a-1)^{2}} \rightarrow 0$, 所以，

$$
\lim _{n \rightarrow \infty} \frac{n}{a^{n}}=0 ;
$$

（3）当 $k>0$ 时，

$$
\frac{n^{k}}{a^{n}}=\left[\frac{\pi}{\left(a^{\frac{1}{2}}\right)^{n}}\right]^{*},
$$

而 $a^{\frac{1}{x}}>1$, 于是由 $(1)$ 知, $\frac{n}{\left(a^{\frac{1}{t}}\right)^{\pi}} \rightarrow 0$, 所以,

$$
\lim _{n \rightarrow \infty} \frac{n^{n}}{a^{n}}=0 .
$$

61. $\lim _{n \rightarrow \infty} \frac{a^{n}}{n!}=0$.

证 令 $k$ 代表任何一个大于 $2|a|$ 的自然数，
则当 $n>k$ 时，有
$0<\left|\frac{a^{n}}{n!}\right|=\left(\frac{|a|}{1} \cdot \frac{|a|}{2} \cdots \frac{|a|}{k}\right)\left(\frac{|a|}{k+1} \cdot \frac{|a|}{k+2} \cdots \frac{|a|}{n}\right)$

$$
<|a|^{k} \cdot\left(\frac{1}{2}\right)^{n-k}=\frac{(2|a|)^{k}}{2^{n}}
$$

由于 $\lim _{n \rightarrow \infty} \frac{(2|a|)^{k}}{2^{*}}=-0$, 所以，

$$
\lim _{n \rightarrow \infty} \frac{a^{n}}{n!}=0
$$

62. $\lim _{n \rightarrow \infty} n q^{n}=0$, 若 $|q|<1$.

证
(1) 当 $0<q<1$ 时，可令 $q=\frac{1}{a}$ ，其中 $a>1$ ，所以，

当 $n \rightarrow \infty$ 时, $n q^{n}=\frac{n}{a^{n}} \rightarrow 0^{*}$ ；
（2）当 $-1<q<0$ 时, 可令 $q=-q^{\prime}$, 其中 $0<q^{\prime}<1$,所以，

当 $n \rightarrow \infty$ 时, $n q^{*}=(-1)^{n} n q^{\prime n} \rightarrow 0$;
（3）当 $q=0$ 时， $n q^{n}=0$ 。
总之，当 $|q|<1$ 时， $\lim _{n \rightarrow \infty} n q^{n}=0$ 。
*) 利用 60 题的结果。
63. $\lim _{n \rightarrow \infty} \sqrt[7]{a}=1 \quad(a>0)$.

证（1）当 $a=1$ 时，等式显然成立；
（2）当 $a>1$ 时，因为 $(1+\varepsilon)^{n}>1+n \varepsilon(n>1, \varepsilon>0)$ ，则
当 $n$ 充分大后，可使 $1+n \varepsilon>a$ ，即 $(1+\varepsilon)^{n}>a$ 。事实上，只
要联 $N=\left[\frac{a-1}{\varepsilon}\right]$ ，当 $n>N$ 时，就可保证这点，所以，

$$
1<\sqrt[7]{a}<1+\varepsilon,
$$

于是，当 $n>N$ 时， $|\sqrt[n]{a}-1|<\varepsilon$ ，
此即 $\lim _{n \rightarrow \infty} \sqrt{a}=1$ ；
（3）当 $0<a<1$ 时，则令 $a=\frac{1}{a^{\prime}}$ ，其中 $a^{\prime}>1$ 。

于是，当 $n \rightarrow \infty$ 时， $\sqrt[n]{a}=\frac{1}{\sqrt[7]{a^{T}}} \rightarrow 1$ 。
总之，当 $a>0$ 时， $\lim _{n \rightarrow \infty} \sqrt[n]{a}=1$ 。
64. $\lim _{n \rightarrow \infty} \frac{\log _{a} n}{n}=0 \quad(a>1)$.

证 先证 $\lim _{n \rightarrow \infty} \sqrt[n]{n}=1$. 事实上, 令 $a_{n}=\sqrt[n]{n}$. 则
$a_{n}>1$. 由 60 题前半部分的推导知

$$
a_{n}^{n}>\frac{n^{2}}{4}\left(a_{n}-1\right)^{2},
$$

即

$$
n>\frac{n^{2}}{4}(\sqrt[7]{n}-1)^{2},
$$

由此可知

$$
0<\sqrt[n]{n}-1<\frac{2}{\sqrt{n}},
$$

故 $\lim _{n \rightarrow \infty} \sqrt[7]{n}=1$ 成立.
现任给 $\varepsilon>0$. 因 $a^{\prime}>1(a>1)$, 故存在 $N=N(\varepsilon)$, 使当 $n>N$ 时，恒有 $\sqrt[n]{n}<a^{\mathbf{x}}$ ，由此可知 $(n>N)$ ，

$$
0<\frac{\log _{a} n}{n}<\epsilon
$$

故 $\lim _{n \rightarrow \infty} \frac{\log _{a} n}{n}=0$.
65. $\lim _{n \rightarrow \infty} \sqrt[n]{n}=1$.

证 在 64 题的证明过程中已证。
66. $\lim _{n \rightarrow \infty} \frac{1}{\sqrt[2]{n!}}=0$ 。

证 由数学归纳法易证 $n!\geqslant \frac{1}{2} n^{\frac{n}{2}}$, 从而 $\frac{1}{\sqrt[3]{n}} \leqslant 2^{\frac{1}{7}}$ 。 $\frac{1}{\sqrt{n}}$, 又因 $\lim _{n \rightarrow \infty} 2^{\frac{1}{n}} \cdot \frac{1}{\sqrt{n}}=0$, 所以,

$$
\lim _{n \rightarrow \infty} \frac{1}{\sqrt[n]{n!}}=0
$$

67. 当 $n$ 充分大时，下面的式子哪个大些？
（a） $100 n+200$ 或 $0.01 n^{2}$ ?；（ 6$) 2^{n}$ 或 $n^{1000}$ ?；
( B ) $1000^{\prime \prime}$ 或 $n!?$
证 （a）因为 $\lim _{n \rightarrow \infty} \frac{100 n+200}{0.01 n^{2}}=0$ ，所以，
当 $n$ 充分大时，0.01 $n^{2}$ 较 $100 n+200$ 大些。
（6）因为 $\lim _{n \rightarrow \infty} \frac{n^{1000}}{2^{n}}=0^{*}$ ，所以，
当 $n$ 充分大时， $2^{2}$ 较 $n^{1000}$ 大些。
（（因为 $\lim _{x \rightarrow \infty} \frac{1000^{*}}{n!}=0^{* *)}$ ，所以，
当 $n$ 充分大时, $n$ ! 较 $1000^{n}$ 大些.
*）利用 60 题的结果。

*     * ）利用 61 题的结果。

68. 证明

$$
\lim _{n \rightarrow \infty}\left(\frac{1}{2} \cdot \frac{3}{4} \ldots \frac{2 n-1}{2 n}\right)=0
$$

证 因为 $0<\frac{1}{2} \cdot \frac{3}{4} \ldots \frac{2 n-1}{2 n}<\frac{1}{\sqrt{2 n+1}}$,
又因为 $\lim _{n \rightarrow \infty} \frac{1}{\sqrt{2 n+1}}=0$, 所以

$$
\lim _{n \rightarrow \infty}\left(\frac{1}{2} \cdot \frac{3}{4} \ldots \frac{2 n-1}{2 n}\right)=0
$$

*）利用 10 题的结果。
69. 证明叙列

$$
x_{n}=\left(1+\frac{1}{n}\right)^{n}(n=1,2 \cdots)
$$

是单调增加的，且上方有界。而叙列

$$
y_{n}=\left(1+\frac{1}{n}\right)^{n+1}(n=1,2, \cdots)
$$

是单调减少的，且下方有界。由此推出这些叙列有公共的极限：

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n+3}=e . \\
& x_{n}=\left(1+\frac{1}{n}\right)^{n}=1+1+C_{n}^{2} \frac{1}{n^{2}}+C_{n}^{\frac{1}{n}} \frac{1}{n^{3}} \\
& +\cdots+C_{n}^{k} \frac{1}{n^{2}}+\cdots+\frac{1}{n^{n}} \\
& =2+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\cdots \\
& +\frac{1}{k!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots\left(1-\frac{k-1}{n}\right)+\cdots \\
& \left.+\frac{1}{n!}\left(1-\frac{1}{n}\right)^{( } 1-\frac{2}{n}\right) \cdots\left(1-\frac{n-1}{n}\right) .
\end{aligned}
$$

证

其中每一项都为正，当 $n$ 增加时，不但对应的项数增多，而且每一个括㾍内的数值也增大，所以，叙列 $x_{n}(n=1,2$ ， …)单调增加。

又当 $k>2$ 时, $\left(1-\frac{k-1}{n}\right)<1, \frac{1}{k!}<\frac{1}{2^{k-1}}$, 所以,

$$
\begin{aligned}
& \left(1+\frac{1}{n}\right)^{n}<2+\frac{1}{2}+\frac{1}{2^{2}}+\cdots+\frac{1}{2^{*-1}} \\
& =2+\left(1-\frac{1}{2^{*-1}}\right)<3
\end{aligned}
$$

此即叙列 $x_{\boldsymbol{n}}(n=1,2, \cdots)$ 上方有界。
由此，我们知 $\lim _{x \rightarrow \infty}\left(1+\frac{1}{n}\right)$ "存在，以 $e$ 表之。
其次，由于

$$
\left(\frac{n^{2}}{n^{2}-1}\right)^{n}=\left(1+\frac{1}{n^{2}-1}\right)^{n}>1+\frac{n}{n^{2}-1}>1+\frac{1}{n},
$$

即 $\left(\frac{n}{n+1}\right)^{n}\left(\frac{n}{n-1}\right)^{n}>\frac{n+1}{n}$ ，
也即 $\left(\frac{n}{n-1}\right)^{n}>\left(\frac{n+1}{n}\right)^{n+1}$ ，所以，

$$
\left(1+\frac{1}{n-1}\right)^{n}>\left(1+\frac{1}{n}\right)^{n+1}
$$

此即 $y_{n-1}>y_{n}$ ，因而，叙列 $y_{n}(n=1,2, \cdots)$ 单调减少。又因

$$
y_{n}=\left(1+\frac{1}{n}\right)^{n} \cdot\left(1+\frac{1}{n}\right)>1+n \cdot \frac{1}{n}=2
$$

所以，叙列 $y_{n}(n=1,2, \cdots)$ 下方有界。
由此，我们知 $\lim _{\alpha \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n+1}$ 存在，且

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n+1}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n} \cdot\left(1+\frac{1}{n}\right) \\
& =\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{*} \cdot \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)=e .
\end{aligned}
$$

于展；

$$
\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n+1}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e .
$$

70. 证明

$$
0<e-\left(1+\frac{1}{n}\right)^{n}<\frac{3}{n} \quad(n=1,2, \cdots) .
$$

当指数 $n$ 是甚么样的数值时，表示式 $\left(1+\frac{1}{n}\right)^{\prime \prime}$ 与数 $e$ 之差小于 0.001 ?
证 利用 69 题的结果知

$$
0<\left(1+\frac{1}{n}\right)^{n}<e<\left(1+\frac{1}{n}\right)^{n+1}
$$

即 $0<e-\left(1+\frac{1}{n}\right)^{n}<\left(1+\frac{1}{n}\right)^{n+1}-\left(1+\frac{1}{n}\right)^{\prime \prime}$,
而 $\left(1+\frac{1}{n}\right)^{n+1}-\left(1+\frac{1}{n}\right)^{n}=\left(1+\frac{1}{n}\right)^{n}\left[\left(1+\frac{1}{n}\right)-1\right]$
$=\frac{1}{n}\left(1+\frac{1}{n}\right)^{n}<\frac{3}{n}$,
园而

$$
0<e-\left(1+\frac{1}{n}\right)^{n}<\frac{3}{n}
$$

其次，要 $e-\left(1+\frac{1}{n}\right)^{k}<0.001$ ，只要 $\frac{3}{n} \leqslant 0.001$ ，即只要 $n \geqslant 3000$ ，所以，当指数 $n$ 是代表任一不小于 3000 的自然数，表示式 $\left(1+\frac{1}{n}\right)^{n}$ 与数 $e$ 之差就小于 0.001 .
71. 设 $p_{n}(n=1,2, \cdots)$ 为趋于 $+\infty$ 的任意数列，面 $q_{\pi}(n=1,2$ ， …）为趋于 $-\infty$ 的任意数列。求证

$$
\lim _{n \rightarrow \infty}\left(1+\frac{1}{p_{n}}\right)^{p_{n}}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{q_{n}}\right)^{q_{n}}=e .
$$

证 令 $k_{n}=\left[p_{n}\right]$ ，即 $k_{n}$ 表 $p_{n}$ 的整数部分，则

$$
k_{n} \leqslant p_{n}<k_{n}+1
$$

由于 $p_{n} \rightarrow+\infty$ ，故 $k_{n} \rightarrow+\infty$ 。从而显然 $\left(1+\frac{1}{k_{n}}\right)^{k_{n}} \rightarrow e$ （参看 89 题题解）。由于

$$
\begin{aligned}
& \frac{1}{k_{n}} \geqslant \frac{1}{p_{n}}>\frac{1}{k_{n}+1} \\
& \left(1+\frac{1}{k_{n}}\right)^{k_{n}+1}>\left(1+\frac{1}{p_{n}}\right)^{p_{n}}>\left(1+\frac{1}{k_{n}+1}\right)^{2}
\end{aligned}
$$

而 $\lim _{n \rightarrow \infty}\left(1+\frac{1}{k_{n}}\right)^{k_{n}+1}=e$ ，

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(1+\frac{1}{k_{n}+1}\right)^{k_{n}}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{k_{n}+1}\right)^{2_{n}^{+1}} \\
& \cdot\left(1+\frac{1}{k_{n}+1}\right)^{-1}=e
\end{aligned}
$$

故 $\lim _{n \rightarrow \infty}\left(1+\frac{1}{p_{n}}\right)^{p_{n}}=e$ 。
其次，若 $q_{n} \rightarrow-\infty$ ，令 $q_{*}=-p_{n}$ ，其中 $p_{n} \rightarrow+\infty$ 。

于是，

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(1+\frac{1}{q_{n}}\right)^{\theta_{n}}=\lim _{n \rightarrow \infty}\left(1-\frac{1}{p_{n}}\right)^{-p_{n}}=\lim _{n \rightarrow \infty}\left(\frac{p_{n}}{p_{n}-1}\right)^{p_{n}} \\
& =\lim _{x \rightarrow \infty}\left(1+\left.\frac{1}{p_{n}-1}\right|^{p_{n}-1} \cdot\left(1+\frac{1}{p_{n}}\right)=e,\right.
\end{aligned}
$$

故 $\lim _{n \rightarrow \infty}\left(1+\frac{1}{p_{n}}\right)^{p_{n}}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{q_{n}}\right)^{\varphi_{n}}=e$.
72. 已知

$$
\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e
$$

求证 $\lim _{n \rightarrow \infty}\left(1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}\right)=e$ 。由此推出公式

$$
e=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}+\frac{\theta_{n}}{n!n},
$$

其中 $0<\theta_{0}<1$, 并计算数 $e$ 准确到 $10^{-5}$ 。
证 因为 $x_{n}=\left(1+\frac{1}{n}\right)^{n}=2+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)$

$$
\begin{aligned}
& \left(1-\frac{2}{n}\right)+\frac{1}{k!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots\left(1-\frac{k-1}{n}\right)+ \\
& \cdots+\frac{1}{n!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots\left(1-\frac{n-1}{n}\right)
\end{aligned}
$$

若固定 $k$, 且 $n>k$, 则有

$$
\begin{aligned}
& x_{n}>2+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\cdots \\
& +\frac{1}{k!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots\left(1-\frac{k-1}{n}\right)
\end{aligned}
$$

今使 $n$ 趋于无穷，在上式两边取极限，得

$$
e \geqslant 2+\frac{1}{2!}+\frac{1}{3!}+\cdots \frac{1}{k!} .
$$

由于此不等式对任何自然数 $k$ 皆成立，因此，

$$
2+\frac{1}{2!}+\frac{1}{3!}+\cdots \frac{1}{n!} \leqslant e
$$

另一方面，有

$$
x_{\mathrm{n}}<2+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!} \text {, 及 } x_{n} \rightarrow e \text {, }
$$

故 $\lim _{n \rightarrow \infty}\left(1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}\right)=e$.
其次，设 $\omega_{n}=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}$ ，则

$$
0<\omega_{n+m}-\omega_{n}=\frac{1}{(n+1)!}+\frac{1}{(n+2)!}+\cdots+\frac{1}{(n+m)!}
$$

$=\frac{1}{(n+1)}\left\{1+\frac{1}{n+2}+\cdots\right.$
$\left.+\frac{1}{(n+2)(n+3) \cdots(n+m)}\right\}<\frac{1}{(n+1)!}$

- $\left\{1+\frac{1}{n+2}+\frac{1}{(n+2)^{2}}+\cdots+\frac{1}{(n+2)^{m-1}}\right\}$
$<\frac{1}{(n+1)!}\left\{1+\frac{1}{n+2}+\frac{1}{(n+2)^{2}}+\cdots\right\}$
$=\frac{1}{(n+1)!} \cdot \frac{n+2}{n+1}$ ，
今立 $n$ 固定不变，并让 $m$ 道于无穷，取极限，得

$$
0 \leqslant e-\omega_{n} \leqslant \frac{1}{(n+1)!} \cdot \frac{n+2}{n+1}=\frac{1}{n!} \cdot \frac{n+2}{(n+1)^{2}}
$$

由于 $\frac{n+2}{(n+1)^{2}}<\frac{1}{n}$, 所以，

$$
0<e-\omega_{n}<\frac{1}{n!} \cdot \frac{1}{n},
$$

即 $0<e-\omega_{n}=\frac{\theta_{2}}{n!n}$, 其中 $0<\theta_{n}<1$,
因而

$$
e=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}+\frac{\theta_{n}}{n!n} .
$$

下面将用公式（1）计算 $e$ ，使之准磷到 $10^{-5}$ 。首先须确定怎

样选取 $n$ ，才能实现这一准确度。取 $n=8$ ，在公式（1）中的.余项已是小于

$$
\frac{1}{8!8}<0.0000032,
$$

所以弃去它时，由公式所造成的误差远远地小于所规定的限度，因此，取 $n=8$ 计算之。其次，还须考虑计算每一项时的舍入误差，为保证 $e$ 准确到 $10^{-5}$ ，我们在计算每一项时，计算到第六位小数上四舍五入凑成整数，则舍入误差总的不超过 $\frac{1}{2 \cdot 10^{6}} \times 6=\frac{3}{10^{6}}$ 。于是总误差不超过
$6.2 \times 10^{-6}<10^{-5}$.
列表:

$$
\begin{array}{r}
2.000000 \\
\frac{1}{2!}=0.500000 \\
\frac{1}{3!}=0.166667 \quad(-) \\
\frac{1}{4!}=0.041667 \quad(-) \\
\frac{1}{5!}=0.008333 \quad(+) \\
\frac{1}{6!}=0.001389 \quad(-) \\
\frac{1}{7!}=0.000198 \quad(+) \\
\frac{1}{8!}=0.000025 \\
2.718279
\end{array}
$$

考虑到修正数的符号，则总误差介手 $-\frac{2}{10^{6}}$ 和 $\frac{4}{10^{6}}$ 之间，因而，数 $e$ 介于

## 2. 718277 及 2.718283

之间，所以，

$$
\varepsilon=2.71828 \pm 0.00001
$$

73. 证明数 $e$ 为无理数。

证 假设 $e$ 为有理数 $\frac{m}{n}$ ，则对于这个 $n$ 有公式

$$
\frac{m}{n}=2+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}+\frac{\theta_{n}}{n!n} \quad\left(0<\theta_{n}<1\right) .
$$

在等式两端同乘以 $n!$ ，我们即得出左端是整数，而右端是整数加一真分数 $\frac{\theta_{n}}{n}$ ，但这是矛盾的。所以数 $e$ 为无理数。
74. 证明不等式

$$
\left(\frac{n}{e}\right)^{n}<n!<e\left(\frac{n}{2}\right)^{n}
$$

证 由 $\sqrt{i(n-i)} \leqslant \frac{n}{2}$, 则 $\frac{1}{2}[\ln i+\ln (n-i)] \leqslant \ln \frac{n}{2}$.
从而 $\sum_{i=1}^{n-1} \ln i \leqslant(n-1) \ln \frac{n}{2},(n-1)!\leqslant\left(\frac{n}{2}\right)^{n-1}$.
两边同乘以 $\frac{n}{2}$ ，得 $\frac{1}{2} n!\leqslant\left(\frac{n}{2}\right)^{n}$ 。于是

$$
n!\leqslant 2\left(\frac{n}{2}\right)^{n}<e\left(\frac{n}{2}\right)^{n}
$$

即 $n!<e\left(\frac{n}{2}\right)^{*}$.

$$
\text { 再证 }\left(\frac{n}{e}\right)^{n}<n 1 .
$$

设 $x_{n}=\left(\frac{n}{e}\right)^{n}$ ，则有

$$
\frac{x_{n}}{x_{n-1}}=\frac{n^{n}}{(n-1)^{n-1} e}=\frac{\left(1+\frac{1}{n-1}\right)^{n-1} n}{e}<n
$$

所以（注意到 $x_{1}=\frac{1}{e}<1$ ）

$$
x_{n}=x_{1} \cdot \frac{x_{2}}{x_{1}} \cdots \frac{x_{n}}{x_{n}}<n!
$$

从而证得 $\left(\frac{n}{e}\right)^{n}<n!$.
75. 证明不等式：
(a) $\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}$ ，式中 $n$ 为任意的自然数。
(6) $1+a<e^{a}$ ，式中 $a$ 为异于零的实数。

证 (a) 因为 $1<\left(1+\frac{1}{n}\right)^{n}<e$ ，两边取对数，得

$$
0<n \ln \left(1+\frac{1}{n}\right)<1
$$

故 $\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}$ ；
又因为 $e<\left(1+\frac{1}{n}\right)^{n+1}$ ，两边取对数，得

$$
1<(n+1) \ln \left(1+\frac{1}{n}\right),
$$

故

$$
\ln \left(1+\frac{1}{n}\right)>\frac{1}{n+1}
$$

因而 $\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}$.
(6) $(1+x)^{n} \geqslant 1+n x(x>0, n$ 为正整数)。

设 $a$ 为正有理数： $a=\frac{p}{q}, p, q$ 是正整数。则由于 $e>$
$\left(1+\frac{1}{q}\right)^{q}$ ，故 $e^{e}>\left(1+\frac{1}{q}\right)^{q a}=\left(1+\frac{1}{q}\right)^{\nu} \geqslant 1+\frac{p}{q}=1+a$.
至于 $a$ 为任意实数 $(\neq 0$ ) 时的证明见 1289 题 (a).
76. 求证

$$
\lim _{n \rightarrow \infty} n\left(a^{\frac{1}{n}}-1\right)=\ln a \quad(a>0),
$$

式中 $\ln a$ 是取 $e=2.718 \cdots$ 作底时数 $a$ 的对数。
证 先设 $a>1$. 令 $b_{n}=a^{\frac{1}{4}}-1$, 则 $b_{n}>0$,
且 $\frac{\ln a}{n}=\ln \left(1+b_{n}\right)$, 故

$$
n\left(a^{\frac{1}{n}}-1\right)=\ln a \frac{b_{n}}{\ln \left(1+b_{n}\right)}
$$

由于 $b_{n} \rightarrow 0$ ，故存在正整数 $N$ ，使当 $n>N$ 时， $0<b_{n}<1$ 。于是，对每个 $n>N$ ，存在唯一正整数 $k_{n}$ ，使 $\frac{1}{k_{n}+1} \leqslant b_{n}<\frac{1}{k_{n}}$ 。由于 $b_{n} \rightarrow 0$, 故 $k_{n} \rightarrow+\infty$ 。由 75 题 (a) 知

$$
\frac{1}{n+1}<\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}(n=1,2, \cdots),
$$

故

$$
\begin{aligned}
\frac{1}{k_{n}+2} & <\ln \left(1+\frac{1}{k_{n}+1}\right) \leqslant \ln \left(1+b_{n}\right) \\
& <\ln \left(1+\frac{1}{k_{n}}\right)<\frac{1}{k_{*}}
\end{aligned}
$$

从而

$$
\begin{aligned}
1-\frac{1}{k_{n}+1} & =\frac{k_{n}}{k_{n}+1}<\frac{b_{n}}{\ln \left(1+b_{n}\right)}<\frac{k_{n}+2}{k_{n}} \\
& =1+\frac{2}{k_{n}}
\end{aligned}
$$

由于 $k_{n} \rightarrow+\infty(n \rightarrow \infty)$ ，故 $\frac{b_{*}}{\ln \left(1+b_{n}\right)} \rightarrow 1(n \rightarrow \infty)$ ，由此得

$$
\lim _{x \rightarrow+\infty} n\left(a^{\frac{1}{x}}-1\right)=\ln a
$$

现设 $0<a<1$. 则 $\frac{1}{a}>1$.于是，由上结果可知

$$
\lim _{n \rightarrow \infty} n\left(a^{\frac{1}{n}}-1\right)=\lim _{n \rightarrow \infty}\left(-a^{\frac{1}{n}}\right) \cdot n\left(\left(\frac{1}{a}\right)^{\frac{1}{n}}-1\right)
$$

$$
=-\ln \frac{1}{a}=\ln a .
$$

当 $a=1$ 时, $\lim _{n \rightarrow \infty} n\left(a^{\frac{1}{n}}-1\right)=\ln a$ 显然成立, 故此式对任何 $a$ $>0$ 成立，证毕。
利用关于单调而且有界的叙列的极限存在的定理，证明以下各叙列的收敛性：
77. $x_{n}=p_{0}+\frac{p_{1}}{10}+\cdots+\frac{p_{n}}{10^{n}} \quad(n=1,2, \cdots)$

式中 $p_{i}(i=0,1,2, \cdots)$ 是非负的整数，从 $p_{1}$ 起不大于 9 .
证 $x_{n+1}=x_{n}+\frac{p_{n+1}}{10^{*+1}}$, 由于 $p_{*+1}>0$ ，所以，

$$
x_{n+1}>x_{n},
$$

因而， $x_{n}(n=1,2, \cdots)$ 是单调增加的. 其次由于 $p_{\mathrm{c}}+\frac{1}{10}<x_{n}$ $\leqslant 9\left(\frac{1}{10}+\cdots+\frac{1}{10^{n}}\right)+p_{0}<1+p_{0}$, 所以，叙列 $x_{n}(n=1,2$, …) 是有界的。
因而，根据单谓而且有界的叙列的极限存在的定理，可知叙列 $\left\{x_{k}\right\}$ 悬收敛的。
78. $x_{\mathrm{n}}=\frac{10}{1} \cdot \frac{11}{3} \cdots \frac{n+9}{2 n-1}$.

解 当 $n \leqslant 10$ 时, 虽然 $\left\{x_{n}\right\}$ 单调增加; 但当 $n>10$ 时，由 $\frac{n+9}{2 n-1}<1$ 知叙列 $\left\{x_{n}\right\}$ 单调减少。注意有下界 $x_{\boldsymbol{n}}>0\{n=1$, $2, \cdots)$. 因而，叙列 $\left\{x_{n}\right\}$ 收敛。
79. $x_{n}=\left(1-\frac{1}{2}\right)\left(1-\frac{1}{4}\right) \cdots\left(1-\frac{1}{2^{n}}\right)$.

证 因 $x_{n+1}=x_{n} \cdot\left(1-\frac{1}{2^{x+1}}\right)<x_{n}$, 所以，叙列 $\left\{x_{n}\right\}$ 是单调

減少的。
又因 $0<x_{n}<1$, 所以，叙列 $\left\{x_{n}\right\}$ 是有界的. 因而 $\left\{x_{n}\right\}$ 收敛。
80. $x_{n}=\left(1+\frac{1}{2}\right)\left(1+\frac{1}{4}\right) \cdots\left(1+\frac{1}{2^{n}}\right)$.

证 因 $x_{n+1}=x_{n} \cdot\left(1+\frac{1}{2^{n+1}}\right)>x_{n}$, 所以，叙列 $\left\{x_{n}\right\}$ 是单调增加的。
又因 $1+a<e^{a}$ ，所以，

$$
0<x_{n}<e^{\frac{1}{2}} \cdot e^{\frac{1}{4} \cdots e_{z^{*}}^{\frac{1}{2}}=e^{\frac{1}{2}+\frac{1}{2^{2}}++\frac{1}{z^{*}}}<e},
$$

即叙列是有界的. 因而 $\left\{x_{n}\right\}$ 收敛.
81. $x_{1}=\sqrt{2}, x_{2}=\sqrt{2+\sqrt{2}}, \cdots$,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-057.jpg?height=196&width=801&top_left_y=1281&top_left_x=276)
证 叙列 $\left\{x_{n}\right\}$ 显然是单调增加的.
其次，利用数学归纳法可以证明： $x_{\mathrm{H}}<\sqrt{2}+1$ 。事实上，对于 $n=1$ 是成立的. 倨设 $x_{n}<\sqrt{2}+1$, 则

$$
\begin{aligned}
x_{k+1} & =\sqrt{2+x_{k}}<\sqrt{2+\sqrt{2}+1} \\
& <\sqrt{(\sqrt{2}+1)^{2}}=\sqrt{2}+1
\end{aligned}
$$

因而，不等式对一切自然数均成立。
由此知叙列 $\left\{x_{n}\right\}$ 是有界的。因而 $\left\{x_{n}\right\}$ 收敛。
利用哥西判别法，证明以下各叙列的收敛性：
82. $x_{\mathrm{n}}=a_{0}+a_{1} q+\cdots+a_{n} q^{\pi}$ ，

其中 $\left|a_{k}\right|<M(k=0,1,2, \cdots)$ 且 $|q|<1$ 。
证 $\left|x_{m}-x_{n}\right|=\left|a_{n+1} q^{n+1}+\cdots+a_{m} q^{m}\right|$

$$
\begin{aligned}
& \leq\left|a_{n+1}\right| \cdot|q|^{n+1}+\cdots+\left|a_{m}\right| \cdot|q|^{m} \\
& <M \cdot|q|^{n+1}\left(1+|q|+\cdots+|q|^{m-n-1}\right) \\
& <M \cdot|q|^{n+1} \cdot \frac{1}{1-|q|} \quad(m>n) .
\end{aligned}
$$

任给 $\epsilon>0$, 由于 $|q|^{n+1} \rightarrow 0(n \rightarrow \infty)$ ，故存在正整数 $N$ ，使当 $n>N$ 时，有

$$
|q|^{n+1}<\frac{(1-|q|) E}{M}
$$

下是，当 $m>n>N$ 时，佰有

$$
\left|x_{m}-x_{n}\right|<\varepsilon .
$$

由此可知，叙列 $\left\{x_{x}\right\}$ 收敛。
83. $x_{n}=\frac{\sin 1}{2}+\frac{\sin 2}{2^{2}}+\cdots+\frac{\sin n}{2^{n}}$.

证 $\quad\left|x_{m}-x_{n}\right|=\left|\frac{\sin (n+1)}{2^{n+1}}+\cdots+\frac{\sin m}{2^{m}}\right|$
$\leqslant \frac{1}{2^{n+1}}\left(1+\frac{1}{2}+\cdots+\frac{1}{2^{m-n-1}}\right)$
$<\frac{1}{2^{+1}} \cdot \frac{1}{1-\frac{1}{2}}=\frac{1}{2^{n}} \quad(m>n)$.
任㘿 $\varepsilon>0$, 取 $N=\left[\begin{array}{c}\ln \frac{1}{\varepsilon} \\ \ln 2\end{array}\right]$,
则当 $m>n>N$ 时，必有 $\frac{1}{2^{n}}<\varepsilon$ ，从而 $\left|x_{m}-x_{x}\right|<\varepsilon$ ，所以，叙列 $\left\{x_{n}\right\}$ 收敛。

B4. $x_{n}=\frac{\cos 1!}{1 \cdot 2}-\frac{\cos 2!}{2 \cdot 3}+\cdots+\frac{\cos n!}{n(n+1)}$.
证 $\left|x_{m}-x_{n}\right|=\left|\frac{\cos (n+1)!}{(n+1)(n+2)}+\cdots+\frac{\cos m!}{m(m+1)}\right|$

$$
\begin{aligned}
& <\frac{1}{(n+1)^{2}}+\frac{1}{(n+2)^{2}}+\cdots+\frac{1}{m^{2}} \\
& <\left(\frac{1}{n}-\frac{1}{n+1}\right)+\left(\frac{1}{n+1}-\frac{1}{n+2}\right)+\cdots \\
& +\left(\frac{1}{m-1}-\frac{1}{m}\right)=\frac{1}{n}-\frac{1}{m}<\frac{1}{n} \quad(m>n)
\end{aligned}
$$

任给 $\epsilon>0$, 取 $N=\left[\frac{1}{\varepsilon}\right]$, 则当 $m>n>N$ 时, 必有 $\mid x_{m}$ $-x_{n} \mid<\varepsilon$ ，所以，叙列 $\left\{x_{n}\right\}$ 收敛.
85. $x_{n}=1+\frac{1}{2^{2}}+\cdots+\frac{1}{n^{2}}$.

证 $\quad\left|x_{m}-x_{n}\right|=\frac{1}{(n+1)^{2}}+\cdots+\frac{1}{m^{2}}, \quad(m>n)$.
以下与 84 题证法步骤相同，故知叙列 $\left\{x_{n}\right\}$ 收敛。
86. 若存在数 $c$, 使得

$$
\begin{gathered}
\left|x_{2}-x_{1}\right|+\left|x_{3}-x_{2}\right|+\cdots+\left|x_{n}-x_{n-1}\right|<c \\
(n=2,3, \cdots),
\end{gathered}
$$

则称叙列 $x_{n}(n=1,2, \cdots$ )有有界变差。
证明凡有有界变差的叙列是收敛的。
举出一个收敛叙列而无有界变差的例子。
证 设 $y_{n}=\left|x_{2}-x_{1}\right|+\left|x_{3}-x_{2}!+\cdots+\left|x_{n}-x_{n-1}\right|\right.$
$(n=2,3, \cdots)$ ，
则叙列 $\left\{y_{n}\right\}$ 单调增加且有界，所以它是收敛的。
根据哥西收敛准则，对于任给的 $\varepsilon>0$ ，存在数 $N$ ，使
当 $m>n>N$ 时, $\left|y_{m}-y_{n}\right|<\varepsilon$,
即 $\left|x_{m}-x_{m-1}\right|+\left|x_{m-1}-x_{m-2}\right|+\cdots+\left|x_{n+1}-x_{n}\right|<\varepsilon$ 。而对于叙列 $\left\{x_{n}\right\}$ 有

$$
\left|x_{m}-x_{n}\right|=\mid x_{m}-x_{m-1}+x_{m-1}-x_{m-2}+\cdots
$$

$$
\begin{aligned}
& +x_{n+1}-x_{n}\left|\leqslant\left|x_{m}-x_{m-1}\right|+\left|x_{m-1}-x_{m-2}\right|+\cdots\right. \\
& +\left|x_{n+1}-x_{n}\right|<\varepsilon
\end{aligned}
$$

所以，叙列 $\left\{x_{n}\right\}$ 是收敛的。
叙列: $1,-1, \frac{1}{2},-\frac{1}{2}, \frac{1}{3},-\frac{1}{3}, \cdots, \frac{1}{n},(-1) \frac{1}{n}, \cdots$,它是以零为极限的收敛叙列。但它不是有有界变差的。事实上，

$$
\begin{aligned}
& \left|x_{2}-x_{1}\right|+\left|x_{3}-x_{2}\right|+\left|x_{4}-x_{3}\right|+\cdots \\
& \quad+\left|x_{2 n}-x_{2 n-1}\right|>\left|x_{2}-x_{1}\right|+\left|x_{4}-x_{3}\right|+\cdots \\
& \quad+\left|x_{2 n}-x_{2 n-1}\right| \\
& = \\
& 2\left(1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots+\frac{1}{n}\right),
\end{aligned}
$$

而叙列 $\omega_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}$ 是发散的 ${ }^{* 2}$ ，又是递增的，故 $\omega_{n} \rightarrow+\infty$ 。 于是,

$$
\left|x_{2}-x_{1}\right|+\left|x_{3}-x_{2}\right|+\cdots+\left|x_{2 n}-x_{2 n-1}\right|
$$

不是有界的，因而，收敛叙列 $\left\{x_{x}\right\}: 1,-1, \frac{1}{2},-\frac{1}{2}, \cdots$ 无有界变差。

* ) 详见 88 题的证明。

87. 试叙述"某叙列不满足哥西准则"的意义。

解 即存在某一个 $\varepsilon_{0}>0$ ，不论对于怎样的数 $N$ ，总有 $n_{0}>N, m_{0}>N$ ，使得

$$
\left|x_{n_{0}}-x_{m_{0}}\right| \geqslant \varepsilon_{0}
$$

88. 利用的西判别法, 证明叙列

$$
x_{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}
$$

## 的发散性。

54

证 取 $m=2 n$, 则

$$
\begin{aligned}
\left|x_{m}-x_{n}\right| & =\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n} \\
& >\frac{1}{2 n}+\frac{1}{2 n}+\cdots+\frac{1}{2 n}=\frac{1}{2},
\end{aligned}
$$

所以，叙列 $\left\{x_{n}\right\}$ 发散。
89. 证明若叙列 $x_{n}(n=1,2, \cdots)$ 收敛，则它的任何子叙列 $x_{\rho_{n}}$世收敛，且有同一极限：

$$
\lim _{n \rightarrow \infty} x p_{n}=\lim _{n \rightarrow \infty} x_{n}
$$

证 $\quad$ 设 $\lim _{n \rightarrow \infty} x_{n}=a$ ，则对于任给的 $E>0$ ，存在有正整数 $N$ ，使

$$
\text { 当 } n>N \text { 时, }\left|x_{n}-a\right|<\varepsilon \text {. }
$$

今因自然数叙列 $\left\{p_{k}\right\}$ 以 $+\infty$ 为其极限，所以，对于 $N$ ，存在有正整数 $k_{0}$ ，使

$$
\text { 当 } k>k_{0} \text { 时 }, p_{k}>N \text {, }
$$

此时 $\left|x_{\rho_{k}}-a\right|<\varepsilon\left(k>k_{0}\right)$ ，所以，子叙列 $\left\{x_{\rho_{k}}\right\}$ 收敛，且

$$
\lim _{n \rightarrow \infty} x p_{n}=\lim _{n \rightarrow \infty} x_{n}=\dot{a} .
$$

90. 证明：若单调叙列的某一子叙列收敛，则此单调叙列本身是收敛的。
证 不失一般性，假设叙列 $\left\{x_{n}\right\}$ 单调增加，其一予叙列 $\left\{x_{p_{n}}\right\}$ 收敛于 $a$ 。则对于任给的 $\varepsilon>0$ ，存在正整数 $N$ ，使

当 $k>N$ 时， $\left|x_{p_{k}}-a\right|<\varepsilon$ ，
令 $N^{\prime}=P_{N+1}$ ，设 $n>N^{\prime}$ ，由于 $p_{1}<p_{2}<p_{2}<\cdots \rightarrow+$ $\infty$ ，故必有 $p_{k}(k>N)$ 使 $p_{k} \leqslant n<p_{k+1}$. 由上知

$$
\left|x_{p_{k}}-a\right|<\varepsilon,\left|x_{p_{t+1}}-a\right|<\varepsilon .
$$

而 $x_{p_{k}} \leqslant x_{\pi} \leqslant x_{p_{k-1}}$ （因 $x_{n}$ 递增），故必

$$
\left|x_{n}-a\right|<\varepsilon .
$$

由此可知 $\lim _{n \rightarrow \infty} x_{n}=a$, 即 $\left\{x_{n}\right\}$ 是收敛的。

91. 证明：若

$$
\lim _{n+\infty} x_{n}=a,
$$

则

$$
\lim _{n \rightarrow \infty}\left|x_{n}\right|=|a| .
$$

证 因为 $\lim _{n \rightarrow \infty} x_{n}=a$ ，则对于任给的 $\epsilon>0$ ，存在有数 $N$ ，使当 $n>N$ 时, $\left|x_{n}-a\right|<\varepsilon$. 又因 $\left|\left|x_{n}\right|-|a|\right| \leqslant \mid x_{n}-$ $a \mid$, 故当 $n>N$ 时, $\left|\left|x_{n}\right|-a\right| \mid<\varepsilon$ 。于是,

$$
\lim _{n \rightarrow \infty}\left|x_{n}\right|=a \mid
$$

92. 设 $x_{n} \rightarrow a$, 则极限

$$
\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}
$$

## 是什么？

橝 按题意，应设 $x_{n} \neq 0(n=1,2, \cdots)$ 。
若 $a \neq 0$ ，则显然

$$
\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}=\frac{\lim _{\substack{ \\ \\x_{n+1}}}^{\lim _{n \rightarrow \infty} x_{n}}=\frac{a}{a}=1 . . ~}{}
$$

若 $a=0$, 则 $\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}$ 可能不存在, 例媢, 若 $\left\{x_{n}\right\}$ 为：

$$
1,1, \frac{1}{2}, \frac{1}{2}, \frac{1}{2^{2}}, \frac{1}{2^{2}}, \frac{1}{2^{3}}, \frac{1}{2^{3}}, \cdots
$$

则 $x_{n} \rightarrow 0$ ，但显然 $\frac{x_{2 m}}{x_{2 m-1}} \rightarrow 1, \frac{x_{2 m+1}}{x_{2 m}} \rightarrow \frac{1}{2}$ ，故 $\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}$ 不存在. 下面我们证明，若 $\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}$ 存在，设为 $b$ ，则必有 $-1 \leqslant$
$b \leqslant 1$.
用反证法. 若 $|b|>1$. 取 $r$ ，使 $|b|>r>1$ 。利用 91题结果，知

$$
\lim _{n \rightarrow \infty} \frac{\left|x_{n+1}\right|}{\left|x_{n}\right|}=|6|
$$

于是，存在正整数 $N$ ，使当 $n \geqslant N$ 时，揸有 $\frac{\left|x_{n+1}\right|}{\left|x_{x}\right|}>r$ 。从而，当 $n>N$ 时，
$\left|x_{n}\right|=\left|x_{N}\right| \cdot\left|\frac{x_{N+1}}{x_{N}}\right| \cdot\left|\frac{x_{N+2}}{x_{N+1}}\right| \cdots\left|\frac{x_{n}}{x_{n-1}}\right|>\left|x_{N}\right| \cdot r^{n-N}$,由此可知 $\lim _{n \rightarrow \infty} x_{n}=\infty$, 此与 $\lim _{n \rightarrow \infty} x_{n}=0$ 矛盾, 故必有 $-1 \leqslant$ $b \leqslant 1$ 。

总结起来，若 $a \neq 0$ ，则 $\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}=1$ ；若 $a=0$ ，则 $\lim _{n \rightarrow \infty}$ $\frac{x_{n+1}}{x_{n}}$ 可能存在也可能不存在，当存在时，它必属于 $[-1$ ， 17 .
93. 证明收敛的数列是有界的.

证 设 $\lim _{n \rightarrow \infty} x_{n}=a$. 要证 $\left\{x_{n}\right\}$ 有界。对于正数 $\varepsilon=1$, 存在正整数 $N$ ，使当 $n>N$ 时，必有 $\left|x_{n}-a\right|<1$ ，从而 $\left|x_{n}\right|$ $<|a|+1(n>N)$. 于是, 令

$$
M=\max \left\{\left|\boldsymbol{x}_{1}\right|,\left|\boldsymbol{x}_{2}\right|, \cdots,\left|x_{N}\right|,|a|+1\right\} .
$$

则 $\left|x_{n}\right| \leqslant M(n=1,2, \cdots)$. 由此可知 $\left\{x_{n}\right\}$ 有界.
94. 证明收敛的数列或达到其上确界，或达到其下研界，或两者都达到。举出这三类叙列的例子。
证（1）对于各项恒为常数的数列，显然上、下确界均达到.
(2) 对于不恒为常数的收敛数列,

设 $\lim _{n \rightarrow \infty} x_{n}=A$ ，则或存在某 $x_{i}>A$ ，或存在某 $x_{j}<A$ ，或这种 $x_{i}, x_{j}$ 都存在。作 $A$ 的充分小的邻域使它不包含 $x_{i}$ 或 $x_{j}$ ，或 $x_{i}, x_{j}$ 都不包含在此邻域内。由于 $x_{\pi} \rightarrow A$ ，故在这三种情况的任一种下，这个邻域外部都只有 $\left\{x_{n}\right\}$ 中的有限个元素。因此分别为必达到上确界、必达到下确界或上、下确界均必达到。在第一种情形下确界可能达到，也可能达不到；在第二种情形，上确界可能达到也可能达不到。
95. 证明趋近于 $+\infty$ 的数列 $x_{n}(n=1,2, \cdots)$ 必定达到其下确界。
证 由题设可知存在正整数 $N$ ，使当 $n>N$ 时恒有 $x_{N}>$ $x_{1}$ ，于是，显然， $x_{1}, x_{2} \cdots, x_{N}$ 中的最小者即为 $\left\{x_{n}\right\}$ 的下确界。
求叙列 $x_{N}(n=1,2, \cdots)$ 的最大项，设：
96. $x_{n}=\frac{n^{2}}{2^{2}}$.

解 当 $n=3$ 时， $n^{2}>2^{n}$ ；当 $n \neq 3$ 时， $n^{2} \leqslant 2^{n}$ ；
所以，最大项为 $x_{3}=\frac{9}{8}$ 。
97. $x_{n}=\frac{\sqrt{n}}{100+n}$.

㑇 $x_{n}=\frac{1}{\left(\sqrt[4]{n}-\frac{10}{\sqrt[4]{n}}\right)^{2}+20} \leqslant \frac{1}{20}$, 其中 $x_{100}=\frac{1}{20}$,
所以，最大项为 $x_{100}=\frac{1}{20}$ 。
98. $x_{n}=\frac{1000^{n}}{n!}$.

解 $\frac{x_{n+1}}{x_{n}}=\frac{1000}{n+1}$.

$$
\text { 当 } n+1<1000 \text { 时, } x_{n+1}>x_{n} \text {; }
$$

当 $n+1>1000$ 时, $x_{n+1}<x_{n}$.
所以，最大项为 $x_{999}=x_{1000}=\frac{1000}{10001}$ 。
求叙列 $x_{n}(n=1,2, \cdots)$ 的最小项，若：
99. $x_{n}=n^{2}-9 n-100$.

解 若 $n^{2}-9 n \geqslant 0$ ，则 $n \geqslant 9$ ；
若 $n^{2}-9 n<0$ ，则 $0<n<9$ 。
所以，最小项从 $x_{1}$ 到 $x_{8}$ 中去寻找，比较之，得 $x_{n}$ 的最小项为

$$
x_{4}=x_{5}=-20-100=-120 .
$$

100. $x_{n}=n+\frac{100}{n}$.

解 $x_{n}=\left(\sqrt{n}-\frac{10}{\sqrt{n}}\right)^{2}+20 \geqslant 20$ ，其中 $x_{10}=20$ ，
所以，最小项为 $x_{10}=20$ 。
求叙列 $x_{n}(n=1,2, \cdots)$ 的 $\inf \left\{x_{n}\right\}, \sup \left\{x_{n}\right\}, \lim _{n \rightarrow \infty} x_{n}$ 及 $\prod_{n \rightarrow \infty} x_{n}$ ，设：
101. $x_{n}=1-\frac{1}{n}$.

解 $\inf \left\{x_{n}\right\}=0 ; \sup \left\{x_{n}\right\}=1 ;$

$$
\underline{\lim }_{n \rightarrow \infty} x_{n}=1 ; \quad \lim _{n \rightarrow \infty} x_{n}=1
$$

102. $x_{n}=\frac{(-1)^{n}}{n}+\frac{1+(-1)^{n}}{2}$.

解 $\inf \left\{x_{n}\right\}=-1 ; \quad \sup \left\{x_{n}\right\}=\frac{3}{2} ;$

$$
\varliminf_{n \rightarrow \infty} x_{n}=0 ; \quad \lim _{N \rightarrow \infty} x_{n}=1
$$

103. $x_{n}=1+\frac{n .}{n+1} \cos \frac{n \pi}{2}$.

$$
\text { 解 } \begin{aligned}
& x_{1}=1, x_{2}=1-\frac{2}{3}, x_{3}=1, x_{4}=1+\frac{4}{5}, \cdots . \\
& \\
& \inf \left\{x_{n}\right\}=0 ; \quad \sup \left\{x_{n}\right\}=2 ; \\
& \\
& \underline{x i m}_{x \rightarrow \infty} x_{n}=0 ; \quad \operatorname{\prod im}_{n \rightarrow \infty} x_{n}=2 .
\end{aligned}
$$

104. $x_{n}=1+2(-1)^{n+1}+3(-1)^{\frac{n(n-1)}{2}}$.

悄 $x_{4 k}=1-2+3, x_{4 k+1}=1+2+3$,

$$
x_{4+2}=1-2-3, x_{4+3}=1+2-3(k=0,1,2,
$$

․).

$$
\begin{aligned}
& \inf \left\{x_{n}\right\}=-4 ; \quad \sup \left\{x_{n}\right\}=6 ; \\
& \lim _{n \rightarrow \infty} x_{n}=-4 ; \quad \lim _{n \rightarrow \infty} x_{n}=6 .
\end{aligned}
$$

105. $x_{n}=\frac{n-1}{n+1} \cos \frac{2 n \pi}{3}$.

解 $x_{1}=0, x_{2}=\frac{1}{3}\left(-\frac{1}{2}\right), x_{3}=\frac{1}{2}$ ，
$x_{4}=\frac{3}{5}\left(-\frac{1}{2}\right), x_{5}=\frac{2}{3}\left(-\frac{1}{2}\right), x_{6}=\frac{5}{7}$,
$x_{7}=\frac{3}{4}\left(-\frac{1}{2}\right), x_{\mathrm{g}}=\frac{7}{9}\left(-\frac{1}{2}\right), x_{9}=\frac{4}{5}, \cdots$.
$\inf \left\{x_{n}\right\}=-\frac{1}{2} ; \quad \sup \left\{x_{n}\right\}=1 ;$
$\varliminf_{n \rightarrow \infty} x_{n}=-\frac{1}{2} ; \quad \lim _{n \rightarrow \infty} x_{n}=1$.
106. $x_{n}=(-1)^{n} n$.

婻 $\inf \left\{x_{n}\right\}=-\infty ; \quad \sup \left\{x_{n}\right\}=+\infty ;$

$$
\underline{\lim _{n \rightarrow \infty}} x_{n}=-\infty ; \quad \lim _{n \rightarrow \infty} x_{n}=+\infty
$$

107. $x_{n}=-n\left[2+(-1)^{n}\right]$.

解 $\inf \left\{x_{n}\right\}=-\infty ; \quad \sup \left\{x_{n}\right\}=-1 ;$

$$
\lim _{n=x} x_{n}=-\infty ; \quad \lim _{n \rightarrow \infty} x_{n}=-\infty .
$$

108. $x_{\mathrm{r}}=n(-1)^{n}$.

解 $\inf \left\{x_{n}\right\}=0 ; \sup \left\{x_{n}\right\}=+\infty ;$

$$
\varliminf_{n \rightarrow \infty} x_{n}=0 ; \quad \lim _{n \rightarrow \infty} x_{n}=+\infty
$$

109. $x_{n}=1+n \sin \frac{n \pi}{2}$.

解 $x_{1}=1+1, x_{2}=1+0, x_{3}=1-3, x_{4}=1+0$,

$$
x_{5}=1+5, \cdots .
$$

$$
\begin{array}{ll}
\inf \left\{x_{n}\right\}=-\infty ; & \sup \left\{x_{n}\right\}=+\infty ; \\
\lim _{n \rightarrow \infty} x_{n}=-\infty ; & \lim _{n \rightarrow \infty} x_{n}=+\infty .
\end{array}
$$

110. $x_{n}=\frac{1}{n-10.2}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-067.jpg?height=83&width=1106&top_left_y=1529&top_left_x=366)
当 $n$ 由 11 到 $+\infty$ 时， $x_{n}$ 由正数往下降，所以，

$$
\begin{aligned}
& \inf \left\{x_{n}\right\}=x_{10}=-5 ; \sup \left\{x_{n}\right\}=x_{13}=1.25 ; \\
& \lim _{n \rightarrow \infty} x_{n}=0 ; \quad \lim _{n \rightarrow \infty} x_{n}=0
\end{aligned}
$$

求 $\lim _{n \rightarrow \infty} x_{n}$ 及 $\lim _{n \rightarrow \infty} x_{n}$. 设:
111. $x_{n}=\frac{n^{2}}{1+n^{2}} \cos \frac{2 n \pi}{3}$.

解 $\underline{\lim }_{n \rightarrow \infty} x_{n}=-\frac{1}{2} ; \lim _{n \rightarrow \infty} x_{n}=1$.
112. $x_{n}=\left(1+\frac{1}{n}\right)^{n} \cdot(-1)^{n}+\sin \frac{n \pi}{4}$

解： $\quad \lim _{\pi \rightarrow \infty} x_{n}=-\left(e+\frac{1}{\sqrt{2}}\right), \lim _{t \rightarrow \infty} x_{n}=e+1$.
113. $x_{n}=\frac{n}{n+1} \sin ^{2} \frac{n \pi}{4}$.

解 $\varliminf_{n \rightarrow \infty} x_{n}=0 ; \quad \lim _{x \rightarrow \infty} x_{n}=1$.
114. $x_{4}=\sqrt[3]{1+2^{n} \cdot(-1)^{n}}$.

解 $\lim _{n \rightarrow \infty} x_{n}=1 ; \quad \prod_{n \rightarrow \infty} x_{n}=2$ （因 $\left(2^{2 k}+1\right)^{\frac{1}{2}}$

$$
\left.=2\left(1+\frac{1}{2^{2 k}}\right)^{\frac{1}{2 k}} \rightarrow 2\right) .
$$

115. $x_{n}=\cos ^{n} \frac{2 n \pi}{3}$.

解 $\varliminf_{n \rightarrow \infty} x_{n}=0 ; \quad \lim _{n \rightarrow \infty} x_{n}=1$.
求下列各叙列的聚点：
116. $\frac{1}{2}, \frac{1}{2}, \frac{1}{4}, \frac{3}{4}, \frac{1}{8}, \frac{7}{8} \cdots, \frac{1}{2^{n}}, \frac{2^{*}-1}{2^{n}}, \cdots$.

解 聚点为 0 及 1 。
117. $1, \frac{1}{2}, 1+\frac{1}{2}, \frac{1}{3}, 1+\frac{1}{3}, \frac{1}{2}+\frac{1}{3}, \frac{1}{4}, 1+\frac{1}{4}$,
$\frac{1}{2}+\frac{1}{4}, \frac{1}{3}+\frac{1}{4}, \frac{1}{5}, \cdots, \frac{1}{n}, 1+\frac{1}{n}, \frac{1}{2}+\frac{1}{n}, \cdots$.
$\frac{1}{n-1}+\frac{1}{n}, \frac{1}{n+1}, \cdots$
角 聚点为

$$
0,1, \frac{1}{2}, \frac{1}{3}, \cdots
$$

它们分别为子叙列：
$\left\{\frac{1}{n}\right\} \cdot\left\{1+\frac{1}{n}\right\},\left\{\frac{1}{2}+\frac{1}{n}\right\},\left\{\frac{1}{3}+\frac{1}{n}\right\}, \cdots$ 的极限.
118. $\frac{1}{2}, \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{2}{4}, \frac{3}{4}, \frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}, \cdots$.

解 所述数列正好包含 $(0,1)$ 中全部有理数，故对于闭

区间 $[0,1]$ 上的每一点 $x$, 在其任意的 $\varepsilon$ 邻域内均有此数列中无穷个数，因此 $x$ 必可作为某子数列的极限，所以， $x$ 是所述数列的聚点，由此可知 $[0,1]$ 中的任何点都是所述数列的聚点, 显然, $[0,1]$ 外的点都不是所述数列的聚点。
119. $\left.x_{n}=3!1-\frac{1}{n}\right)+2(-1)^{n}$ 。

解 因为 $2 \cdot(-1)^{*}$ 为 2 或 -2 . 所以,聚点为 5 及 1 .
120. $x_{n}=\frac{1}{2}\left[(a+b)+(-1)^{n}(a-b)\right]$ 。

解 聚点为 $a$ 及 $b$ 。
121. 试举出以已知数

$$
a_{1}, a_{2}, \cdots, a_{p}
$$

作为秝点的数列的例子。
解 数列
$a_{1}-\frac{1}{2}, a_{2}-\frac{1}{2}, \cdots, a_{p}-\frac{1}{2}, a_{1}-\frac{1}{3}$,
$a_{2}-\frac{1}{3}, \cdots, a_{p}-\frac{1}{3}, \cdots, a_{1}-\frac{1}{n}, a_{2}-\frac{1}{n}, \cdots$,
$a_{p}-\frac{1}{n}, \cdots$
显然以 $a_{1}, a_{2}, \cdots, a_{p}$ 为聚点.
122. 试挙出数列的例子, 对此数列而言, 已知数列

$$
a_{1}, a_{2}, \cdots, a_{n}^{-}, \cdots
$$

所有各项皆为其聚点，已知叙列还必有怎样的聚点？
解 例如，数列
$a_{1}+\frac{1}{2}, a_{2}+\frac{1}{2}, a_{1}+\frac{1}{3}, a_{2}+\frac{1}{3}, a_{3}+\frac{1}{3}$,
$a_{1}+\frac{1}{4}, a_{2}+\frac{1}{4}, a_{3}+\frac{1}{4}, a_{4}+\frac{1}{4}, \cdots$,

$$
a_{1}+\frac{1}{n}, a_{2}+\frac{1}{n}, a_{3}+\frac{1}{n}, \cdots, a_{n}+\frac{1}{n}, \cdots
$$

就以 $a_{1}, a_{2}, a_{3}, \cdots, a_{n}, \cdots$ 为其聚点.
另外, 很明显, 若 $\left\{x_{n}\right\}$ 为一数列, 使已知数列 $\left\{a_{n}\right\}$ 的各项 $a_{1}, a_{2}, a_{3}, \cdots$ 皆为 $\left\{x_{n}\right\}$ 的聚点，则已知数列 $\left\{a_{n}\right\}$ 本身的聚点也必为数列 $\left\{x_{n}\right\}$ 的聚点。
123. 举出叙列的例子：
（a）没有有限的聚点；
（6）有唯一有限的聚点，但非收敛者；
(B) 有无限多的聚点;
(r) 以每一实数作为聚点.

解 (a) 叙列 $x_{n}=n(n=1,2, \cdots)$ 没有有限的聚点.
（6）叙列: $1,-1, \frac{1}{2},-2, \frac{1}{3},-3, \cdots, \frac{1}{n},-n, \cdots$有唯一有限的聚点 0 , 但此叙列却不收敛。
(в) 118 题的叙列即有无限多的聚点.
（ r ）我们按下述"对角线法则" 来构造一个叙列，使每一元菜后面珢一个对应的负数，排列顺次如图1１．
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-070.jpg?height=647&width=784&top_left_y=1821&top_left_x=816)

图 1.1

$$
\begin{aligned}
& x_{1}=1, x_{2}=-1, x_{3}=\frac{1}{2}, x_{4}=-\frac{1}{2}, x_{5}=2, \\
& x_{6}=-2, x_{7}=3, x_{8}=-3, x_{3}=\frac{2}{2}, \\
& x_{11}=-\frac{2}{2}, x_{11}=\frac{1}{3}, x_{12}=-\frac{1}{3}, \cdots .
\end{aligned}
$$

此叙列以每一实数作为其聚点，即聚点的集合为 $(-\infty \times$ ， $+\infty$ )。
124. 证明叙列 $x_{n}$ 和 $y_{n}=x_{n} \cdot \sqrt[n]{n}(n=1,2, \cdots)$ 有相同的聚点.
证 因为 $\sqrt[n]{n} \rightarrow 1$ ，所以，叙列 $\left\{x_{n}\right\}$ 的子叙列 $\left\{x_{n_{k}}\right\}$ 与 $\left\{y_{n}\right\}$ 的对应子叙列 $\left\{x_{n_{k}} \cdot \sqrt[n]{n_{k}}\right\}$ 同时收敛, 且具有相同的极限，此即叙列 $\left\{x_{n}\right\}$ 和 $\left\{y_{n}\right\}$ 有相同的聚点。
125. 证明从有界的叙列 $x_{n}(n=1,2, \cdots)$ 中, 永远可选出收敛的子钷列 $x_{\boldsymbol{p}_{\mathrm{F}}}(n=1,2, \cdots)$ 。
证 因为叙列 $\left\{x_{n}\right\}$ 有界，故可设一切项满足不等式

$$
a \leqslant x_{4} \leqslant b,
$$

其中 $a, b$ 为有限的实数，将区间 $[a, b]$ 二等分之，得区间 $\left(a, \frac{a+b}{2}\right],\left[\frac{a+b}{2}, b\right]$ ，其中必至少有一个包含所给叙列的无限多项，将它记成 $\left[a_{1}, b_{1}\right]$ （若两者均含无穷多项，则任取其一作为 $\left.\left(a_{1}, b_{1}\right]\right)$ 。再将区间 $\left[a_{1}, b_{1}\right]$ 等分之, 又可得区间 $\left[a_{2}, b_{2}\right] \subset\left[a_{1}, b_{1}\right]$ ，它包含所给叙列的无限多项。依次类推，于是得一串区间：

$$
\left[a_{1}, b_{i}\right] \supset\left[a_{2}, b_{2}\right] \supset \cdots \supset\left[a_{n}, b_{n}\right] \supset \cdots,
$$

其中每一 $\left[a_{n}, b_{n}\right]$ 都包含所给叙列 $\left\{x_{n}\right\}$ 中的无限多项，

且有

$$
b_{n}-a_{n}=\frac{b-a}{2^{n}} \rightarrow 0(n \rightarrow \infty)
$$

因此, 根据区间套定理诸 $\left[a_{n}, b_{n}\right\}$ 具有唯一的公共点 $c$,且

$$
\lim _{n \rightarrow \infty} a_{n}=\lim _{n \rightarrow \infty} b_{n}=c .
$$

现按下法选出 $\left\{x_{n}\right\}$ 的一个子序列 $\left\{x_{\rho_{k}}\right\}$ ：在包含于 $\left[a_{1}\right.$ ， $\left.b_{1}\right]$ 内的诸 $x_{n}$ 中任取一个作为 $x_{\rho_{1}}$ 。然后，在包含于 $\left[a_{2}\right.$ ， $\left.b_{2}\right]$ 内且在 $x_{p_{1}}$ 后面的诸 $x_{n}$ 中任取一个作为 $x_{P_{2}}$ ，然后，又在包含于 $\left[a_{3}, b_{3}\right]$ 内且在 $x_{f_{2}}$ 后面的诸 $x_{\pi}$ 中任取一个作为 $x_{p_{1}}$ 。余类推（这是可能的，因为每个 $\left[a_{k}, b_{k}\right]$ 中都包含有 $x_{n}$ 无穷多项). 于是我们得出 $\left\{x_{n}\right\}$ 的一子数列 $\left\{x_{p_{k}}\right\}$,满足

$$
a_{k} \leqslant x_{p_{1}} \leqslant b_{k} \quad(k=1,2, \cdots) .
$$

由此，知 $\left|x_{p_{k}}-c\right| \leqslant b_{k}-a_{k}(k=1,2, \cdots)$ ，
故 $\lim _{n \rightarrow \infty} x_{p_{k}}=c$. 从而 $\left(x_{p_{d}}\right\}$ 是 $\left\{x_{n}\right\}$ 的一个收敛子数列.证毕。
126. 证明：若叙列 $x_{n}(n=1,2, \cdots)$ 无界，则存在子叙列 $x_{f_{-}}(n$ $=1,2, \cdots$ ，使得

$$
\lim _{n \rightarrow \infty} x_{p_{n}}=\infty .
$$

证 因 $x_{n}(n=1,2, \cdots)$ 无界，故存在某项 $x_{p_{1}}$ 满足 $\left|x_{\rho_{1}}\right|$ $>1$ 。由于数列 $x_{n}\left(n=p_{1}+1, p_{1}+2, \cdots\right)$ 也无界，故又存在某项 $x_{p_{2}}\left(p_{2}>p_{1}\right)$, 使 $\left|x_{p_{2}}\right|>2$ ；又由于数列 $x_{n}(n$ $\left.=p_{2}+1, p_{2}+2, \cdots\right)$ 无界，故又存在某项 $x_{p_{3}}\left(p_{3}>p_{2}\right)$,使 $\left|x_{p_{9}}\right|>3$. 余类推. 于是，我们得 $\left\{x_{n}\right\}$ 的一个子数列 $\left\{x_{e_{k}}\right\}$ ，满足

$$
\left|x_{p_{i}}\right|>k(p=1,2, \cdots) .
$$

由此可知

$$
\lim _{k \rightarrow \infty} x_{p_{k}}=\infty
$$

证毕。
127. 设叙列 $x_{n}(n=1,2, \cdots)$ 收敛，而叙列 $y_{n}(n=1,2, \cdots)$ 发散，则能否断定关于叙列
（a） $x_{n}+y_{n}$ ；（б） $x_{n} y_{n}$
的收敛性?
举出适当的例子。
解 （a） $\left\{x_{z}+y_{n}\right\}$ 一定发散。如果 $\left\{x_{n}+y_{n}\right\}$ 收敛，则由 $\left(x_{n}+y_{n}\right)-x_{n}=y_{n}$ ，知 $\left\{y_{n}\right\}$ 收敛，与题设矛盾。
（б）叙列 $\left\{x_{x} y_{n}\right\}$ 可能收敛，也可能发散。例如：
（1）叙列 $x_{n}=\frac{1}{n}(n=1,2, \cdots)$ 收敛，
叙列 $y_{n}=n(n=1,2, \cdots)$ 发散，
而叙列 $x_{n} y_{n}=1(n=1,2, \cdots)$ 是收敛的.
（2）叙列 $x_{n}=\frac{1}{n}(n=1,2, \cdots)$ 收敛，
叙列 $y_{n}=n^{2}(n=1,2, \cdots)$ 发散，
而叙列 $x_{n} y_{n}=n(n=1,2, \cdots)$ 却是发散的。
128. 设叙列 $x_{n}$ 和 $y_{n}$ 发散 $(n=1,2, \cdots)$ 。可否断定叙列 （а） $x_{n}+y_{n} ; \quad$ （б） $x_{n} y_{n}$.
也发散呢?
举出适当的例子。
解 不能。例如，叙列

$$
x_{n}=\frac{1+(-1)^{n}}{2} \text { 及 } y_{n}=\frac{1-(-1)^{n}}{2}(n=1,2, \cdots)
$$

都发散，但叙列

$$
x_{n}+y_{n}=1 \quad(n=1,2, \cdots)
$$

及

$$
x_{n} y_{n}=0 \quad(n=1,2, \cdots)
$$

却都是收敛的，
129. 设：

$$
\lim _{n \rightarrow \infty} x_{n}=0
$$

及 $y_{n}(n=1,2, \cdots)$ 为任意叙列，能否断定

$$
\lim _{n \rightarrow \infty} x_{n} y_{n}=0 ?
$$

举出迠当的例子。
解 不能。例如，叙列

$$
x_{n}=\frac{1}{n} \rightarrow 0(n \rightarrow \infty)
$$

及

$$
y_{n}=n(n=1,2, \cdots)
$$

的乘积

$$
x_{n} y_{n}=1(n=1,2, \cdots),
$$

当 $n \rightarrow \infty$ 时㙁于 1 , 不趋于 0 .
130. 设：

$$
\lim _{n \rightarrow \infty} x_{n} y_{n}=0
$$

是否由此可得出或 $\lim _{x \rightarrow \infty} x_{n}=0$ ，或 $\lim _{n \rightarrow \infty} y_{n}=0$ ？
䄈 不能。例如，叙列

$$
x_{n}=\frac{1+(-1)^{n}}{2} \text { 及 } y_{n}=\frac{1-(-1)^{n}}{2}(n=1,2, \cdots) \text {, }
$$

則有

$$
\lim _{n \rightarrow \infty} x_{n} y_{n}=0
$$

但 $\lim _{n \rightarrow \infty} x_{n}$ 及 $\lim _{n \rightarrow \infty} y_{n}$ 均不存在。
当然，还可举例 $x_{n}=\frac{1}{n^{2}}, y_{n}=n,(n=1,2, \cdots)$ ，则 $x_{n} y_{n}$ $\rightarrow 0, x_{n} \rightarrow 0$ ，而 $\left\{y_{n}\right\}$ 极限不存在（当 $n \rightarrow \infty$ ）。注意，假若已知 $x_{n} y_{n} \rightarrow 0$ ，而又已知 $\left\{x_{n}\right\},\left\{y_{n}\right\}$ 中至少有一个叙列有极限的话，则： $\lim _{n \rightarrow \infty} x_{n}=0$ 或 $\lim _{n \rightarrow \infty} y_{n}=0$ 至少有一个是成立的.
131. 证明
(a) $\underline{l i m}_{n \rightarrow \infty} x_{n}-\lim _{n \rightarrow \infty} y_{n} \leqslant \underline{\lim _{n \rightarrow \infty}}\left(x_{n}+y_{n}\right) \leqslant \lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}$,

及
(б) $\lim _{n \rightarrow \infty} x_{n}+\lim _{x \rightarrow+\infty} y_{n} \leqslant \lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right) \leqslant \lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}$.

举出在上面关系式中仅不等号成立的例子。
证 (a) 先证右蝡不等式. 根据定义，存在 $\left\{x_{\mathrm{v}}\right\}$ 的子序列 $\left\{x_{n_{k}}\right\}$ 使 $x_{n_{k}} \rightarrow \alpha=\lim _{n \rightarrow \infty} x_{n}$ 。对于序列 $\left\{y_{n_{k}}\right\}$ ，必有子序列 $y_{n_{i}} \rightarrow \beta=\lim _{k \rightarrow \infty} y_{n_{k}}$. 显然 $\lim _{k \rightarrow \infty} y_{n_{k}} \leqslant \lim _{n \rightarrow \infty} y_{n}$ 。由于 $x_{n_{k}}+y_{t_{i}} \rightarrow$ $\alpha+\beta$, 故 $\alpha+\beta$ 是 $\left\{x_{n}+y_{n}\right\}$ 的一个聚点。
由此可知

$$
\alpha+\beta \geqslant \lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right) .
$$

故得

$$
\lim _{n+\infty}\left(x_{n}+y_{n}\right) \leqslant \alpha+\beta \leqslant \lim _{n \rightarrow \infty} x_{n}+\operatorname{Tim}_{n \rightarrow \infty} y_{n} .
$$

再证左端的不等式，根据定义，存在 $\left\{x_{n}+y_{n}\right\}$ 的子序列 $\left\{x_{n_{k}}+y_{n_{k}}\right\}$ 使 $x_{n_{t}}+y_{n_{k}} \rightarrow a^{\prime}=\varliminf_{n \rightarrow \infty}\left(x_{n}+y_{n}\right)$ 。对于序列 $\left\{x_{n_{i}}\right\}$, 存在子序列 $\left\{x_{n_{i}}\right\}$ 使 $x_{n_{i}} \rightarrow \beta^{\prime}=\lim _{k \rightarrow \infty} x_{n_{k}}$,显然 $\lim _{k \rightarrow \infty} x_{n_{t}} \geqslant \lim _{n \rightarrow \infty} x_{n}$ 。由于

$$
y_{n_{k_{i}}}=\left(x_{n_{i_{i}}}+y_{n_{n_{i}}}\right)-x_{n_{k_{i}}} \rightarrow \alpha^{\prime}-\beta^{\prime}
$$

故 $\alpha^{\prime}-\beta^{\prime}$ 是 $\left\{y_{*}\right\}$ 的一个聚点, 从而

$$
\alpha^{\prime}-\beta^{\prime} \geqslant \underline{\lim y_{n}},
$$

由此可知

$$
\varliminf_{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=\alpha^{\prime} \geqslant \beta^{\prime}+\underline{l i m}_{n \rightarrow \infty} y_{n} \geqslant \lim _{n \rightarrow \infty} x_{n}+\underline{l i m}_{n \rightarrow \infty} y_{n} .
$$

（6）先证右端不等式. 根据定义, 存在 $\left\{x_{n}+y_{n}\right\}$ 的一个子序列 $\left\{x_{n_{k}}+y_{n_{k}}\right\}$, 使 $x_{n_{k}}+y_{n_{t}} \rightarrow r=\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)$ 。对于序列 $\left\{x_{n_{k}}\right\}$, 存在子序列 $x_{x_{i}} \rightarrow \tau=\overline{\lim _{k \rightarrow-\infty}} x_{n_{k}}$ 。显然 $\lim _{n \rightarrow \infty} x_{n_{n}} \leqslant \lim _{n \rightarrow \infty} x_{n}$ 。由于

$$
y_{v_{s_{i}}}=\left(x_{n_{k_{i}}}+y_{v_{v_{i}}}\right)-x_{n_{i_{i}}} \rightarrow \tau-\tau,
$$

故 $r-\tau$ 是 $\left\{y_{n}\right\}$ 的一个聚点, 从而

$$
r-r \leqslant \lim _{n \rightarrow \infty} y_{n} .
$$

由此可知

$$
\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=r \leqslant \tau+\prod_{n \rightarrow \infty} y_{n} \leqslant \lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n} .
$$

再证左端的不等式。根据定义, 存在 $\left\{y_{*}\right\}$ 的一个子序列 $\left\{y_{n_{k}}\right\}$, 使 $y_{n_{i}} \rightarrow r^{\prime}=\lim _{n \rightarrow \infty} y_{n}$ ，对于序列 $\left\{x_{n_{k}}\right\}$ ，存在子序列 $\left\{x_{a_{i}}\right\}$ 使 $x_{n_{i}} \rightarrow \tau^{\prime}=\lim _{k \rightarrow \infty} x_{n_{i}}$. 显然 $\lim _{\vec{n}-\infty} x_{n_{k}} \geqslant \lim _{n \rightarrow \infty} x_{n}$. 由于

$$
x_{i_{i}}+y_{n_{k_{i}}} \rightarrow r^{\prime}+\tau^{\prime},
$$

故 $r^{\prime}+\tau^{\prime}$ 是 $\left\{x_{n}+y_{n}\right\}$ 的一个聚点，从而

$$
\lim _{n \rightarrow \infty}\left(x_{n}+y_{*}\right) \geqslant r^{\prime}+\tau^{\prime}
$$

由此可知

$$
\overline{\lim }_{n \rightarrow \infty}\left(x_{n}+y_{n}\right) \geqslant r^{\prime}+r^{\prime} \geqslant \underline{\lim }_{n \rightarrow \infty} x_{n}+\operatorname{\prod im}_{n \rightarrow \infty} y_{n} .
$$

证毕。
以下举不等号成立的例子。例如，令

$$
\begin{aligned}
& \left\{x_{n}\right\} \text { 为: } 1,0,1,0,1,0, \cdots \\
& \left\{y_{n}\right\} \text { 为: } 0,2,0,2,0,2, \cdots .
\end{aligned}
$$

则有不等式

$$
\begin{aligned}
& \underline{\lim }_{n \rightarrow \infty} x_{n}+\underline{\lim }_{n \rightarrow \infty} y_{n}=0<\underline{\lim }_{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=1 \\
& <\underline{\lim _{n \rightarrow \infty}} x_{n}+\lim _{n \rightarrow \infty} y_{n}=2 .
\end{aligned}
$$

而对于数列

$$
\begin{aligned}
& \left\{x_{n}\right\} \text { 为: } 0,2,0,2,0,2, \cdots \\
& \left\{y_{n}\right\} \text { 为: } 1,0,1,0,1,0, \cdots,
\end{aligned}
$$

则有

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}=1<\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=2 \\
& <\lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}=3
\end{aligned}
$$

132. 设 $x_{n} \geqslant 0$ 和 $y_{n} \geqslant 0(n=1,2, \cdots)$.

证明：
(a) $\lim _{n \rightarrow \infty} x_{n} \cdot \lim _{n \rightarrow \infty} y_{n} \leqslant \lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \leqslant \lim _{n \rightarrow \infty} x_{n} \cdot \lim _{n \rightarrow \infty} y_{n}$,

及
（б） $\lim _{n \rightarrow \infty} x_{n} \cdot \operatorname{Iim}_{n \rightarrow \infty} y_{n} \leqslant \operatorname{Iim}_{n \rightarrow \infty}\left(x_{n} y_{n}\right) \leqslant \lim _{n \rightarrow \infty} x_{n} \cdot \lim _{\rightarrow \infty \infty} y_{n}$
举出在这些关系式中仅不等号成立的例子。
证 （a）先证右端的不等式。根据定义，存在 $\left\{x_{n}\right\}$ 的一个子序列 $\left\{x_{n_{4}}\right\}$ ，使 $x_{n_{4}} \rightarrow a=\underline{\lim } x_{n} \geqslant 0$ ；对于序列 $\left\{y_{n_{k}}\right\}$ ，存在学芧列 $\left\{y_{n_{k}}\right\}$, 使 $y_{n_{k_{i}}} \rightarrow \beta=\lim _{k \rightarrow \infty} y_{n_{k}} \geqslant 0$. 显然 $\lim _{k \rightarrow \infty} y_{n_{k}} \leqslant$
$\lim _{n \rightarrow \infty} y_{n}$ 。由于 $x_{n_{k_{i}}} y_{n_{k}} \rightarrow \alpha \beta$, 故 $\alpha \beta$ 是序列 $\left\{x_{n} y_{n}\right.$ ：的一个聚点, 因此

$$
\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \leqslant \alpha \beta
$$

由此，再注意到 $\alpha \geqslant 0, \beta \geqslant 0$ ，即得知

$$
\underline{\lim }_{x \rightarrow 1}\left(x_{n} y_{n}\right) \leqslant \alpha \beta \leqslant\left(\prod_{n \rightarrow n} y_{n}\right)==\left(\lim _{n \neq x} x_{n}\right) \cdot
$$

( $\overline{\lim y_{n}}$ ).

再证左端的不等式。若 $\frac{\lim }{n-\mathrm{m}} x_{n}=0$ ，则此不等式显然成立，故设 $\frac{\lim _{n+\infty} x_{n}}{n+\beta^{*}}>0$ 。于是，存在正整数 $N_{0}$ ，使当 $n$ $>N_{0}$ 时， $x_{s}>0$ 。根据定义，存在 $\left\{x_{n} y_{n}\right\}$ 的子序列 $\left\{x_{n_{k}} y_{n_{k}}\right\}$ 使

$$
x_{n_{1}} y_{n_{k}} \rightarrow \alpha^{\prime}=\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \geqslant 0 .
$$

对于序列 $\left\{x_{x_{2}}\right\}$, 存在子序列 $\left\{x_{n_{t}}\right\}$, 使

$$
x_{n_{n_{1}}} \rightarrow \beta^{\prime}=\lim _{k \rightarrow \infty} x_{n_{i}} .
$$

注意到 $\beta^{\prime}=\lim _{k \rightarrow \infty} x_{n_{1}} \geqslant \lim _{n \rightarrow \infty} x_{n}=\beta^{*}>0$ 以及 $x_{n}>0(n>$ $N_{0}$ ),
知

$$
y_{n_{k_{i}}}=\left(x_{x_{k_{1}}} y_{x_{x_{1}}}\right) \cdot \frac{1}{x_{x_{k_{1}}}} \rightarrow \frac{\alpha^{\prime}}{\beta^{\prime}} .
$$

故 $\frac{\alpha^{\prime}}{\beta^{\prime}}$ 是 $\left\{y_{n}\right\}$ 之一聚点，从而

$$
\frac{\alpha^{\prime}}{\beta^{\prime}} \geqslant \underline{\lim } y_{n},
$$

由此可知

$$
\varliminf_{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\alpha^{\prime} \geqslant \beta^{\prime}\left(\varliminf_{n \rightarrow \infty} y_{n}\right) \geqslant\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right)
$$

（6）先证右端不等式，可设 $\left\{y_{n}\right\}$ 有界（若 $\left\{y_{n}\right\}$ 无界，则 $\lim _{n \rightarrow \infty} y_{n}=+\infty$ ，从而此不等式显然成立）。根据定义，存在 $\left\{x_{n} y_{n}\right\}$ 的子序列 $\left\{x_{n_{k}} y_{n_{k}}\right\}$ 使

$$
x_{n_{k}} y_{n_{n}} \rightarrow \bar{\alpha}=\prod_{n \rightarrow \infty}\left(x_{n} y_{n}\right) \geqslant 0
$$

对于 $\left\{x_{a_{k}}\right\}$ ，存在子芧列 $\left\{x_{n_{i_{i}}}\right\}$ 使

$$
x_{n_{k_{k}}} \rightarrow \bar{\beta}=\varlimsup_{k \rightarrow \infty} x_{n_{k}} \geqslant 0
$$

若 $\bar{\beta}=0$ ，则由于 $\left\{y_{n}\right\}$ 有界，知 $x_{u_{t_{i}}} y_{t_{t_{i}}} \rightarrow 0$ ，从而 $\bar{\alpha}=0$ ，此时所要证的不等式泉然成立，故下设 $\bar{\beta}>0$ 。于是，当 $i$ 充分大时 $\left(i>i_{0}\right), x_{i_{k_{i}}}>0$ ，故得

$$
y_{n_{n_{i}}}=\left(x_{n_{k_{i}}} y_{n_{i_{i}}}\right) \cdot \frac{1}{x_{n_{i_{i}}}} \rightarrow \frac{\bar{\alpha}}{\bar{\beta}} .
$$

因此，依 $\frac{\bar{\beta}}{}$ 是 $\left\{y_{n}\right\}$ 之一聚点，从而 $\frac{\bar{\alpha}}{\beta} \leqslant \lim _{N \rightarrow \infty} y_{n}$ ；由此可知

$$
\left.\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\bar{\alpha} \leqslant \bar{\beta}\left(\lim _{; \rightarrow \infty} y_{n}\right) \leqslant \lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right)
$$

再证左端的不等式。根据定义，存在 $\left\{y_{n}\right\}$ 的一子序列 $\left\{y_{n_{k}}\right\}$, 使 $y_{n_{k}} \rightarrow r=\varlimsup_{n \rightarrow \infty} y_{n} \geqslant 0$ ，对于 $\left\{x_{v_{k}}\right\}$ ，存在子序列 $\left\{x_{n_{k_{j}}}\right\}$ 使

$$
x_{x_{x_{1}} \rightarrow} \rightarrow \tau=\lim _{t \rightarrow \infty} x_{v_{k}} \geqslant 0 .
$$

显然， $\lim _{i \rightarrow \infty} x_{n_{k}} \geqslant \underset{\lim _{\rightarrow \infty}}{ } x_{n} \geqslant 0$ 。由于

$$
x_{n_{i_{i}}} y_{n_{m_{i}}} \rightarrow \sigma,
$$

故 $\pi$ 是 $\left\{x_{n} y_{n}\right\}$ 之一儛点，从而

$$
\tau r \leqslant \lim _{n \rightarrow \infty}\left(x_{k} y_{n}\right)
$$

由此可知

$$
\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right) \leqslant r \leqslant \lim _{n+\infty}\left(x_{n} y_{n}\right) .
$$

证毕。
下面举不等号成立的例子，例妇，令

$$
\begin{aligned}
& \left\{x_{n}\right\} \text { 为: } \frac{1}{2}, 2, \frac{1}{2}, 2, \frac{1}{2}, 2, \cdots \\
& \left\{y_{n}\right\} \text { 为: } 2, \frac{1}{4}, 2, \frac{1}{4}, 2, \frac{1}{4}, \cdots
\end{aligned}
$$

则有不等式

$$
\begin{aligned}
& \left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right)=\frac{1}{8}<\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \\
& =\frac{1}{2}<\left(\underset{n \rightarrow \infty}{\left(\lim _{n} x_{n}\right) \cdot\left(\operatorname{Iim}_{n \rightarrow \infty} y_{n}\right)=1 .}\right.
\end{aligned}
$$

再令
$\left\{x_{n}\right\}$ 为: $2, \frac{1}{4}, 2, \frac{1}{4}, 2, \frac{1}{4}, \cdots$
$\left\{y_{n}\right\}$ 为: $\frac{1}{2}, 2, \frac{1}{2}, 2, \frac{1}{2}, 2, \cdots$
则有不等式

$$
\begin{aligned}
& \left(\lim _{n \rightarrow-\infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right)=\frac{1}{2}<\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \\
& =1<\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{x \rightarrow \infty} y_{n}\right)=4 .
\end{aligned}
$$

133. 证明：若 $\lim x_{n}$ 存在，则对任何的叙列 $y_{n}(n=1,2, \cdots)$ ，有
(a) $\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=\lim _{n \rightarrow \infty} x_{n}+\operatorname{\prod im}_{n \rightarrow \infty} y_{n}$

及
(6) $\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n}\left(x_{n} \geqslant 0\right)$.

证 (a) 由于 $\lim _{n \rightarrow \infty} x_{n}$ 存在，故

$$
\lim _{n \rightarrow \infty} x_{n}=\lim _{n \rightarrow \infty} x_{n}=\lim _{n \rightarrow \infty} x_{n},
$$

从而，利用 131 题的结果可知

$$
\begin{aligned}
& \operatorname{\prod im}_{n \rightarrow \infty}\left(x_{n}+y_{n}\right) \leqslant \operatorname{\prod im}_{n \rightarrow \infty} x_{n}+\varlimsup_{n \rightarrow \infty} y_{n} \\
& =\lim _{n \rightarrow \infty} x_{n}+\varlimsup_{n \rightarrow \infty} y_{n} \\
& =\lim _{n \rightarrow \infty} x_{n}+\overline{\lim _{n \rightarrow \infty}} y_{n} \leqslant \operatorname{\prod im}_{n \rightarrow \infty}\left(x_{n}+y_{n}\right),
\end{aligned}
$$

故得

$$
\varlimsup_{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=\lim _{n \rightarrow \infty} x_{n}+\lim _{n \rightarrow \infty} y_{n} .
$$

（6）分三种情形：(i) 设 $y_{n} \geqslant 0(n=1,2, \cdots)$ 。则利用 132 题的结果可知

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right) \leqslant\left(\lim _{x \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right) \\
& =\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right) \\
& =\left(\lim _{x \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right) \leqslant \lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right),
\end{aligned}
$$

故得

$$
\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} y_{n}\right)
$$

(ii) 设 $y_{n} \leqslant 0(n=1,2, \cdots)$. 则 $-y_{n} \geqslant 0(n=1,2$,
…），于是，仍利用 132 题的结果可知

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(-x_{n} y_{n}\right) \leqslant \varliminf_{n \rightarrow \infty} \lim _{n}\left(-y_{n}\right) \cdot \lim _{n \rightarrow \infty} x_{n} \\
& =\lim _{n \rightarrow \infty}\left(-y_{n}\right) \cdot \lim _{n \rightarrow \infty} x_{n} \\
& =\underline{\lim }_{n \rightarrow \infty}\left(-y_{n}\right) \cdot \underline{\lim _{n \rightarrow \infty} x_{n} \leqslant \varliminf_{n \rightarrow \infty}\left(-x_{n} y_{n}\right), ~}
\end{aligned}
$$

故得

$$
\varliminf_{n \rightarrow \infty}\left(-x_{n} y_{n}\right)=\lim _{n \rightarrow \infty} x_{n} \cdot \underline{\lim }_{n \rightarrow \infty}\left(-y_{n}\right) ;
$$

但是根据上、下极限的定义，显然有等式

$$
\lim _{n \rightarrow \infty}\left(-x_{n} y_{n}\right)=-\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right),
$$

$$
\lim _{n \rightarrow \infty}\left(-y_{n}\right)=-\lim _{n \rightarrow \infty} y_{n},
$$

由此可知

$$
\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\lim _{n \rightarrow \infty} x_{n} \cdot \lim _{n \rightarrow \infty} y_{n} .
$$

（iii）设｛ $\left.y_{n}\right\}$ 中有无穷多项是非负的，设这些项构成的子序列为 $\left\{y_{n_{k}}\right\}\left(y_{n_{k}} \geqslant 0, k=1,2, \cdots\right.$ ）（如果 $\left\{y_{n}\right\}$ 中只有有限项是非负的，则从某一项开始有 $y_{n}<0$ ，这时应用（ii）的结果即知所要证的等式成立）。于是，注意到 $x_{\mathrm{m}}$ $\geqslant 0$,显然有 (利用 (i) 已证的结果)

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\lim _{k \rightarrow \infty}\left(x_{n_{k}} y_{n_{k}}\right) \\
& =\lim _{k \rightarrow \infty} x_{n_{k}} \cdot \lim _{k \rightarrow \infty} y_{n_{k}} \\
& =\lim _{n \rightarrow \infty} x_{n} \cdot \lim _{n \rightarrow \infty} y_{n} .
\end{aligned}
$$

证半。
134. 证明：若对于某非负 " 叙列 $x_{n}\left(x_{n} \geqslant 0, n=1,2, \cdots\right)$ ，任何叙列 $y_{n}(n=1,2, \cdots)$ 都使下二等式中至少有一成立：
(a) $\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=\lim _{n \rightarrow \infty} x_{n}+\operatorname{\prod im}_{n \rightarrow \infty} y_{n}$

或
（5） $\operatorname{\Gamma im}_{n \rightarrow \infty}\left(x_{n} y_{n}\right)=\operatorname{im}_{n \rightarrow \infty} x_{n} \cdot \operatorname{im}_{n \rightarrow \infty} y_{n}$,
则叙列 $x_{n}$ 是收敛的。
证 • 取 $\left\{x_{n}\right\}$ 的子叙列 $\left\{x_{m_{k}}\right\}$ ，使

$$
x_{n_{k}} \rightarrow \underline{l i m}_{n=\infty} x_{n}
$$

取

其中 $A$ 为任取的正常数, 对此 $\left\{y_{n}\right\}$ 若（a）成立，则由（注意到 $x_{n} \geqslant 0$ )

$$
\lim _{n \rightarrow \infty}\left(x_{n}+y_{n}\right)=\left(\underline{\lim }_{n \rightarrow \infty} x_{n}\right)+A, \overline{\lim }_{n \rightarrow \infty} y_{n}=A,
$$

知

$$
\left(\lim _{n \rightarrow \infty} x_{n}\right)+A=\left(\overline{\lim }_{n \rightarrow \infty} x_{n}\right)+A,
$$

由此可知

$$
\lim _{n \rightarrow \bar{x}} x_{n}=\lim _{n \rightarrow \infty} x_{n},
$$

故 $\left\{x_{n}\right\}$ 收敛.
若（ $\sigma$ ）成立，则由（同样，注意到 $x_{n} \geqslant 0$ ）

$$
\lim _{n \rightarrow \infty}\left(x_{n} y_{n}\right)=A=\underline{\lim _{n \rightarrow \infty} x_{n}}
$$

知

$$
A \cdot \underline{\lim }_{n \rightarrow \infty} x_{n}=A \cdot \varliminf_{n \rightarrow \infty} x_{n}
$$

由此可知

$$
\lim _{n \rightarrow \infty} x_{n}=\lim _{n \rightarrow \infty} x_{n},
$$

故 $\left\{x_{n}\right\}$ 也是收敛的. 证毕。
*）编者注：原著中将 $x_{n} \geqslant 0$ 的假定加在条件（6）后，似不妥，因为叙列 $x_{m}$ 应该是预先给定的。
135. 证明：若 $x_{*}>0(n=1,2, \cdots)$ 及

$$
\lim _{n \rightarrow \infty} x_{n} \cdot \operatorname{\varlimsup im}_{n \rightarrow \infty} \frac{1}{x_{n}}=1,
$$

则叙列 $x_{n}$ 是收敛的。
证 由假定知

$$
0<\lim _{n \rightarrow \infty} x_{n}<+\infty, 0<\lim _{n \rightarrow \infty} \frac{1}{x_{n}}<+\infty,{ }^{(*)}
$$

由于（利用 132 颗的结果）

$$
1=\underline{\lim }_{n \rightarrow \infty}\left(x_{n} \cdot \frac{1}{x_{n}}\right) \leqslant\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} \frac{1}{x_{n}}\right)
$$

$$
\leqslant \lim _{n \rightarrow \infty}\left(x_{n} \cdot \frac{1}{x_{n}}\right)=1
$$

故

$$
\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\lim _{n \rightarrow \infty} \frac{1}{x_{n}}\right)=1
$$

从而

$$
\left(\lim _{n \rightarrow \infty} x_{n}\right) \cdot\left(\overline{\lim _{n \rightarrow \infty}} \frac{1}{x_{n}}\right)=\left(\overline{\lim _{n \rightarrow \infty} x_{n}}\right) \cdot\left(\lim _{n \rightarrow \infty} \frac{1}{x_{n}}\right) .
$$

由此，再注意到（＊）式，即知

$$
\underset{n \rightarrow \infty}{\lim _{n \rightarrow \infty} x_{n}=\prod_{n \rightarrow \infty} x_{n}=a \quad(0<a<+\infty) . ~}
$$

故 $\lim _{n \rightarrow \infty} x_{n}$ 存在有限，因此 $\left\{x_{n}\right\}$ 收敛，证毕。
136. 证明：若叙列 $x_{n}(n=1,2, \cdots)$ 有界，且

$$
\lim _{n \rightarrow \infty}\left(x_{n+1}-x_{n}\right)=0
$$

则此叙列的聚点密布于下极限和上极限

$$
l=\varliminf_{x \rightarrow \infty} x_{n} \text { 和 } L=\prod_{n \rightarrow \infty} x_{n}
$$

之间，即是说间陪〔 $l, L]$ 中的任意一个数都是已知叙列的聚点。
证 根据定斑， $l$ 与 $L$ 都是 $\left\{x_{n}\right\}$ 的苼点，故我们只要证明 $l$ 与 $L$ 之间的任何数 $a(l<a<L)$ 都是 $\left\{x_{n}\right\}$ 的霖点。先证：对于任意给定的 $\varepsilon>0$ 及任意给定的正整数 $N$ ，必有正整数 $n^{+}>N$ 存在，使 $\left|x_{n}^{*}-a\right|<\epsilon$ 。

由假定，必有正整数 $N^{\prime}$ ，存在，使当 $n>N^{\prime}$ 时，恒有 $\left|x_{n+1}-x_{n}\right|<\varepsilon$ 。令 $N_{0}=\max \left\{N, N^{\prime}\right\}$ ，则于序列 $x_{n}\left(n=N_{0}+1, N_{0}+2, \cdots\right)$ 中必至少有两项 $x_{n^{\prime}}$ 和 $x_{n^{\prime}}$ 。存在，使 $x_{w^{\prime}}<a, x_{n^{\prime}}>a$ （因为否则的话，例如，无小于 $a$ 的项，则必 $\lim _{n \rightarrow \infty} x_{n} \geqslant a$ ，此与 $l<a$ 矛盾），不妨设 $n^{\prime}<n^{\prime \prime}$ ，令

满足 $n^{\prime} \leqslant n \leqslant n^{\prime \prime}$ 且使 $x_{*}<a$ 的正整数 $n$ 中之最大者为 $n^{*}$ 。显然 $n^{*} \leqslant n^{\prime \prime}-1$ ，且 $x_{n} \cdot<a, x_{n}{ }^{*}+1>a$ 。故 $n^{*}>N$ ， $n^{*}>N^{\prime}$ 并且

$$
\left|x_{n}^{*}-a\right|<x_{n+1}^{*}-x_{n}{ }^{*}<\varepsilon .
$$

现取 $\varepsilon_{:}=1, N_{1}=1$, 则存在 $x_{n_{1}}\left(n_{1}>1\right.$, 使 $\left|x_{n_{1}}-a\right|$ $<1$; 再取 $\varepsilon_{2}=\frac{1}{2}, N_{2}=n_{1}$, 则存在 $x_{m_{2}}\left(n_{2}>n_{1}\right)$ 使 $\mid x_{n_{2}}$ $-a \left\lvert\,<\frac{1}{2}\right.$; 又取 $\epsilon_{3}=\frac{1}{3}, N_{3}=n_{2}$, 存在则 $x_{n_{3}}\left(n_{3}>n_{2}\right)$使 $\left|x_{*_{3}}-a\right|<\frac{1}{3}$ ；这样一直继续下去，则得 $\left\{x_{7}\right\}$ 的一个子数列 $\left\{x_{m_{k}}\right\}$ ，满足

$$
\left|x_{n_{k}}-a\right|<\frac{1}{k} \quad(k=1,2, \cdots)
$$

故 $x_{n_{A}} \rightarrow a$ ，即 $a$ 是 $\left\{x_{n}\right\}$ 的一个衆点，证毕。
137. 设数列 $x_{1}, x_{2}, \cdots, x_{n}, \cdots$ 满足条件

$$
0 \leqslant x_{m+n} \leqslant x_{m}+x_{n}(m, n=1,2, \cdots)
$$

证明 $\lim _{n \rightarrow \infty} \frac{x_{n}}{n}$ 存在。
证 证法一：
由于

$$
x_{n} \leqslant x_{n-1}+x_{1} \leqslant x_{n-2}+x_{1}+x_{1} \leqslant \cdots \leqslant n x_{1},
$$

故 $0 \leqslant \frac{x_{n}}{n} \leqslant x_{1}$, 从而数列 $\left\{\frac{x_{n}}{n}\right\}$ 有界，令 $\lim _{n \rightarrow \infty} \frac{x_{n}}{n}=a$ ，则 0 $\leqslant a \leqslant x_{1}$, 任给 $\varepsilon>0$ ，存在正整数 $N>1$ 使 $\frac{x_{N}}{N}<a+\varepsilon$.任何正整数 $n>N$ 都可表为 $n=q N+r$ 的形式，其中 $q$为正整数， $r$ 为小于 $N$ 的非负整数 $(0 \leqslant r<N)$ 。我门有

$$
\begin{aligned}
x_{n} & =x_{q N+r} \leqslant x_{(q-1) N}+x_{N}+x_{r} \leqslant x_{(q-q) N}+x_{N}+ \\
& +x_{N}+x_{r} \leqslant \cdots \leqslant q x_{N}+x_{r} \leqslant q x_{N}+r x_{1} \\
& \leqslant q x_{N}+N x_{1},
\end{aligned}
$$

从面

$$
\frac{x_{n}}{n} \leqslant \frac{q x_{N}}{n}+\frac{N x_{1}}{n} \leqslant \frac{x_{N}}{N}+\frac{N x_{1}}{n}<a+\varepsilon+\frac{N x_{1}}{n} .
$$

由此可知

$$
\varlimsup_{n+\infty} \frac{x_{n}}{n} \leqslant a+\varepsilon,
$$

再根据 $\varepsilon>0$ 的任意性，即得

$$
\varlimsup_{n \rightarrow \infty} \frac{x_{n}}{n} \leqslant a,
$$

故

$$
\varliminf_{n \rightarrow \infty} \frac{x_{n}}{n}=\varlimsup_{n \rightarrow \infty} \frac{x_{n}}{n},
$$

因此， $\lim _{n \rightarrow \infty} \frac{x_{n}}{n}$ 存在有限。

## 证法二：

用反证法。假定 $\lim _{n \rightarrow \infty} \frac{x_{n}}{n}$ 不存在，则序列 $\left\{\frac{x_{n}}{n}\right\}$ 至少有两个聚点 $a$ 与 $b$, 不妨设 $a<b$, 由于（证法一中已证）

$$
0 \leqslant \frac{x_{n}}{n} \leqslant x_{1} \quad(n=1,2, \cdots),
$$

故 $0 \leqslant a<b \leqslant x_{1}$ 。根据聚点定义, 存在 $\left\{x_{n}\right\}$ 的两个子序列 $\left\{x_{n_{i}}\right\}$ 与 $\left\{x_{m_{j}}\right\}$ ，使

$$
\lim _{i \rightarrow \infty} \frac{x_{m_{i}}}{n_{i}} \doteq a, \quad \lim _{j \rightarrow \infty} \frac{x_{m_{i}}}{m_{j}}=b .
$$

任给 $\varepsilon<0$ ，必存在正整数 $i_{0}>1$ ，使

$$
\frac{x_{n_{10}}}{n_{i_{2}}}<a+\varepsilon .
$$

显然，当 $j$ 充分大时 $\left(j>j_{0}\right)$ ，必 $m_{j}>n_{i_{0}}$ ，此时仿证法一，有不等式（〔 $x 〕$ 表 $x$ 的整数部分）

$$
x_{m_{j}} \leqslant\left[\frac{m_{j}}{n_{i_{0}}}\right] x_{i_{i_{0}}}+n_{i_{0}} x_{1} \leqslant \frac{m_{j}}{n_{i_{0}}} x_{n_{i_{0}}}+n_{i_{0}} x_{1}
$$

故（ $j>j_{0}$ 时）

$$
\frac{x_{m_{j}}}{m_{j}} \leqslant \frac{x_{\pi_{i_{0}}}}{n_{i_{9}}}+\frac{n_{i_{0}} x_{1}}{m_{j}}<a+\varepsilon+\frac{n_{i_{0}} x_{1}}{m_{j}}
$$

由此可知

$$
b=\lim _{i \rightarrow \infty} \frac{x_{m_{j}}}{m_{j}} \leqslant a+\varepsilon
$$

由 $\varepsilon>0$ 的任意性，即得 $b \leqslant a$ ，此与 $a<b$ 矛盾，证毕。
138. 证明：若叙列 $x_{n}(n=1,2, \cdots)$ 收敛，则算术平均值的叙列

$$
\xi_{n}=\frac{1}{n}\left(x_{1}+x_{2}+\cdots+x_{n}\right) \quad(n=1,2, \cdots)
$$

也收敛，且

$$
\lim _{n \rightarrow \infty} \frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=\lim _{n \rightarrow \infty} x_{n}
$$

反之，则结论不真，举例说明之。
证 令 $s_{n}=x_{1}+x_{2}+\cdots+x_{n}$ ，则

$$
\begin{aligned}
& \frac{s_{n}}{n}=\frac{s_{N}}{n}+\frac{s_{n}-s_{N}}{n}=\frac{s_{N}}{n}+\frac{x_{N+1}+x_{N+2}+\cdots+x_{n}}{n-N} \\
& \cdot\left(1-\frac{N}{n}\right)
\end{aligned}
$$

因为 $\lim _{n \rightarrow \infty} x_{n}$ 存在，设收敛于 $a$ ，则对于任给的 $\varepsilon>0$ 存在序

号 $N$, 使当 $n>N$ 时, $\left|x_{*}-a\right|<\varepsilon$, 即 $x_{N+1}, x_{N+2}, \cdots$ 均 $\in(a-\varepsilon, a+\varepsilon)$. 由此推得 $\frac{x_{N+1}+x_{N+2}+\cdots+x_{n}}{n-N} 也$含在 $(a-\varepsilon, a+\varepsilon)$ 之内, 即

$$
\frac{x_{N+1}+x_{N+2}+\cdots+x_{n}}{n-N}=a+a,
$$

式中 $|a|<\varepsilon$.
这样, $\frac{s_{n}}{n}=\frac{s_{N}}{n}+(a+a)\left(1-\frac{N}{n}\right)$. 由此得

$$
\left|\frac{s_{*}}{n}-a\right| \leqslant \frac{\left|s_{N}\right|}{n}+|\alpha|+(|a|+|\alpha|) \frac{N}{n}
$$

今取 $N^{\prime}>N$, 使当 $n>N^{\prime}$ 时, 恒有

$$
\frac{\left|s_{N}\right|}{n}<\varepsilon, \quad \frac{N}{n}<\frac{\varepsilon}{|a|+\varepsilon} .
$$

于是，当 $n>N^{\prime}$ 时，恒有 $\left|\frac{s_{n}}{n}-a\right|<3 \varepsilon$ 。由此可知

$$
\lim _{n \rightarrow \infty} \frac{s_{n}}{n}=a,
$$

即

$$
\lim _{n \rightarrow \infty} \frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=\lim _{n \rightarrow \infty} x_{n}=a .
$$

但反之不然，例如叙列 $x_{n}=(-1)^{n+1}(n=1,2, \cdots)$ 是发散的，但是叙列

$$
\zeta_{\mathrm{a}}=\left\{\begin{array}{l}
0, \text { 若 } n \text { 为偶数, } \\
-\frac{1}{n}, \text { 若 } n \text { 为奇数, }
\end{array}\right.
$$

却是收敛的。
139. 证明：若

$$
\lim _{n \rightarrow \infty} x_{n}=+\infty
$$

82

则 $\lim _{n \rightarrow \infty} \frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=+\infty$.
证 因为 $\lim _{n \rightarrow \infty} x_{n}=+\infty$ ，故对于任给的 $M>0$ ，存在有序号 $N$, 使当 $n>N$ 时， $x_{n}>3 M$ 。此时，仿 138 题之证，有

$$
\frac{s_{n}}{n}=\frac{s_{N}}{n}+\frac{s_{n}-s_{N}}{n-N}\left(1-\frac{N}{n}\right)>\frac{s_{N}}{n}+3 M\left(1-\frac{N}{n}\right) .
$$

又因 $\frac{s_{N}}{n} \rightarrow 0,1-\frac{N}{n} \rightarrow 1(n \rightarrow \infty)$, 故可取正整数 $N^{\prime}>$ $N$ ，使当 $n>N^{\prime}$ 时，恒有

$$
\frac{\left|s_{N}\right|}{n}<\frac{M}{2}, \quad 1-\frac{N}{n}>\frac{1}{2}
$$

于是，当 $n>N^{\prime}$ 时恒有 $\frac{s_{n}}{n}>M$ ，由此可知

$$
\lim _{n \rightarrow \infty} \frac{s_{n}}{n}=\lim _{n \rightarrow \infty} \frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=+\infty .
$$

140. 证明：若叙列 $x_{n}(n=1,2, \cdots)$ 收敛，且 $x_{n}>0$,

则

$$
\lim _{n \rightarrow \infty} \sqrt[n]{x_{1} x_{2} \cdots x_{n}}=\lim _{n \rightarrow \infty} x_{n}
$$

证 设 $\lim _{n \rightarrow \infty} x_{n}=a$. 因 $x_{n}>0(n=1,2, \cdots)$ ，故 $a \geqslant 0$ 。先设 $a>0$, 则 $\lim _{n \rightarrow \infty} \ln x_{n}=\ln a$, 于是, 利用 138 题的结果可知

$$
\lim _{n \rightarrow \infty} \frac{1}{n}\left(\ln x_{1}+\ln x_{2}+\cdots+\ln x_{n}\right)=\ln a
$$

由此可知

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \sqrt[n]{x_{1} x_{2} \cdots x_{n}}=\lim _{n \rightarrow \infty} e^{\frac{1}{\left(\ln x_{1}+\ln x_{2}+\cdots+\ln x_{2}\right)}} \\
& =e^{\mathrm{low}}=a=\lim _{n \rightarrow \infty} x_{n}
\end{aligned}
$$

若 $a=0$, 则 $\lim _{n \rightarrow \infty}\left(-\ln x_{n}\right)=+\infty$. 利用 139 题的结果可知

$$
\lim _{x \rightarrow \infty} \frac{1}{n}\left(-\ln x_{1}-\ln x_{2}-\cdots-\ln x_{n}\right)=+\infty,
$$

由此可知

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \sqrt[n]{x_{1} x_{2} \cdots x_{n}} & =\lim _{n \rightarrow \infty} e^{\left.-\frac{1}{n} t-\ln x_{i}-\ln x_{z}-\cdots \cdot \ln x_{n}\right)} \\
& =0=\lim _{n \rightarrow \infty} x_{n}
\end{aligned}
$$

证毕，
141. 证明: 若 $x_{n}>0(n=1,2, \cdots)$ 且 $\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}$ 存在, 则

$$
\lim _{n \rightarrow \infty} \sqrt[n]{x_{n}}=\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}
$$

证 令 $y_{n}=\frac{x_{n+1}}{x_{n}}(n=1,2, \cdots)$, 则 $y_{n}>0$. 由假定 $\lim _{n \rightarrow \infty} y_{*}$
存在，设为 $a$ 。利用 140 题的结果可知

$$
\lim _{n \rightarrow \infty}\left(y_{1} y_{2} \cdots y_{n-1}\right)^{\frac{1}{n-1}}=a
$$

于是

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \sqrt[n]{x_{n}}=\lim _{n \rightarrow \infty} \sqrt[n]{x_{1}} \sqrt[n]{\frac{x_{2}}{x_{1}} \frac{x_{3}}{x_{2}} \cdots \frac{x_{n}}{x_{n-1}}} \\
& =\lim _{n \rightarrow \infty} \sqrt[n]{x_{1}}\left[\left(y_{1} y_{2} \cdots y_{n-1}\right)^{\frac{1}{n-1}}\right]^{\frac{n-1}{n}} \\
& =1 \cdot a=a=\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}
\end{aligned}
$$

142. 证明

$$
\lim _{n \rightarrow \infty} \frac{n}{\sqrt[n]{n!}}=e
$$

证 设数列 $x_{n}=\frac{n^{n}}{n!}(n=1,2, \cdots)$ 则有

$$
\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{n}}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e,
$$

所以，利用 141 题的结果，即得

$$
\lim _{n \rightarrow \infty} \frac{n}{\sqrt{n}}=\lim _{n \rightarrow \infty} \sqrt[n]{x_{n}}=\lim _{n \rightarrow \infty} \frac{x_{n+1}}{x_{2}}=e
$$

143. 证明：若
(a) $y_{n+1}>y_{n}(n=1,2, \cdots)$ ，
(6) $\lim _{n \rightarrow \infty} y_{n}=+\infty$,
(B) $\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{4}}{y_{n+1}-y_{n}}$ 存在,

则 $\quad \lim _{x \rightarrow \infty} \frac{x_{n}}{y_{n}}=\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{x+1}-y_{n}}$.
证 假定 $\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=a$ 。由此。并注意到 $y_{n} \rightarrow+\infty$ ，知对于任给的 $\varepsilon>0$ ，存在有序号 $N$ ，使当 $n>N$ 时，佰有

$$
\left|\frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}-a\right|<\frac{\varepsilon}{2}\left(\text { 且 } y_{n}>0\right) \text {. }
$$

于是分数（当 $n>N$ 时）

$$
\begin{aligned}
& \frac{x_{N+2}-x_{N+1}}{y_{N+2}-y_{N+1}}, \frac{x_{N+3}-x_{N+2}}{y_{N+3}-y_{N+2}}, \cdots \\
& \frac{x_{n}-x_{n-1}}{y_{n}-y_{n-1}}, \frac{x_{n+1}-x_{n+1}-y_{n}}{y_{n+1}}
\end{aligned}
$$

都包含在（ $a-\frac{\varepsilon}{2}, a+\frac{\varepsilon}{2}$ ）之内，因为 $y_{m+1}>y_{n}$ ，所以，这些分数的分母都是正数，于是得

$$
\begin{aligned}
& \left(a-\frac{\varepsilon}{2}\right)\left(y_{N+2}-y_{N+1}\right)<x_{N+2}-x_{N+1} \\
& <\left(a+\frac{\varepsilon}{2}\right)\left(y_{N+2}-y_{N+1}\right) \\
& \left(a-\frac{\varepsilon}{2}\right)\left(y_{N+3}-y_{N+2}\right)<x_{N+3}-x_{N+2} \\
& <\left(a+\frac{\varepsilon}{2}\right)\left(y_{N+3}-y_{N+2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \left(a-\frac{\varepsilon}{2}\right)\left(y_{n+1}-y_{n}\right)<x_{n+1}-x_{n} \\
& <\left(a+\frac{\varepsilon}{2}\right)\left(y_{n+1}-y_{n}\right)
\end{aligned}
$$

相加之，得

$$
\begin{aligned}
& \left(a-\frac{\varepsilon}{2}\right)\left(y_{n+1}-y_{n+1}\right)<x_{n+1}-x_{N+1} \\
& <\left(a+\frac{\varepsilon}{2}\right)\left(y_{n+1}-y_{N+1}\right)
\end{aligned}
$$

即 $a-\frac{\varepsilon}{2}<\frac{x_{n+1}-x_{N+1}}{y_{n+1}-y_{N+1}}<a+\frac{\varepsilon}{2}$,
所以，当 $n>N$ 时，恒有

$$
\left|\frac{x_{n+1}-x_{N+1}}{y_{n+1}}-a\right|<\frac{\varepsilon}{y_{N+1}} .
$$

另外，我们有（当 $n>N$ 时）

$$
\begin{gathered}
\frac{x_{n}}{y_{n}}-a=\frac{x_{N+1}-a y_{N+1}}{y_{n}}+\left(1-\frac{y_{N+1}}{y_{n}}\right) \\
\cdot\left(\frac{x_{n}-x_{N+1}}{y_{n}-y_{N+1}}-a\right)
\end{gathered}
$$

故

$$
\left|\frac{x_{n}}{y_{n}}-a\right| \leqslant\left|\frac{x_{N+1}-a y_{N+1}}{y_{n}}\right|+\frac{\varepsilon}{2} .
$$

现取正整数 $N^{\prime}>N$ ，使当 $n>N^{\prime}$ 时，恒有

$$
\frac{\left|x_{N+1}-a y_{N-1}\right|}{y_{n}}<\frac{\epsilon}{2}
$$

于是，当 $n>N^{\prime}$ 时，恒有

$$
\left|\frac{x_{n}}{y_{n}}-a\right|<\varepsilon .
$$

由此可知， $\lim _{n \rightarrow \infty} \frac{x_{n}}{y_{n}}=a=\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}$.

$$
\begin{aligned}
& \text { 注. 本题中, 若将条件(B) 换为 } \\
& \left.\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{n+1}-\frac{y_{n}}{y_{n}}}=+\infty \text { (或 }-\infty\right)
\end{aligned}
$$

则结论仍成立：

$$
\lim _{n \rightarrow \infty} \frac{x_{n}}{y_{n}}=\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}} .
$$

详见 Г. M. 菲赫金哥尔茨著《勧积分学教程》第一章 § 2.
144. 求 (a) $\lim _{n \rightarrow \infty} \frac{n^{2}}{a^{n}}(a>1)$;
(6) $\lim _{n \rightarrow \infty} \frac{\lg n}{n}$.

解 (a) 设 $x_{n}=n^{2}, y_{n}=a^{n}(a>1)$
则 $y_{n+1}>y_{n}, y_{n} \rightarrow+\infty$, 且有

$$
\frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=\frac{(n+1)^{2}-n^{2}}{a^{n+1}-a^{*}}=\frac{2 n+1}{a^{n}(a-1)} .
$$

再设 $x^{\prime}{ }_{n}=2 n+1, y^{\prime}{ }_{n}=a^{*}$ ，
则 $y^{\prime}{ }_{n+1}>y^{\prime}, y^{\prime}, \rightarrow+\infty$, 且有

$$
\frac{x_{n+1}^{\prime}-x^{\prime}}{y_{n+1}^{\prime}-y_{n}^{\prime}}=\frac{2}{a^{\prime \prime}(a-1)} \rightarrow 0,
$$

因而利用 143 题的结果得

$$
\lim _{\rightarrow \infty} \frac{2 n+1}{a^{n}}=0,
$$

即

$$
\lim _{n \rightarrow \infty} \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=0
$$

继续利用 143 题的结果，得

$$
\lim _{n \rightarrow \infty} \frac{x_{n}}{y_{n}}=0,
$$

即 $\lim _{n \rightarrow \infty} \frac{n^{2}}{a^{n}}=0$.
（6）设 $x_{n}=\lg n, y_{n}=n$,
则

$$
\begin{aligned}
& y_{n+1}>y_{n}, y_{n} \rightarrow+\infty, \text { 且有 } \\
& \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=\lg \left(1+\frac{1}{n}\right) \rightarrow 0,
\end{aligned}
$$

故

$$
\lim _{n \rightarrow \infty} \frac{x_{*}}{y_{n}}=\lim _{n \rightarrow \infty} \frac{\lg n}{n}=0 .
$$

注 143 题的结果属于O. Stolz, 当 $y_{n}=n$ 时, 早已被A. L. Cauchy 所证明，此结果常用于确定 $\frac{{ }^{\infty}{ }^{\infty} \text { " }}{\infty}$ 型的待定式 $\frac{x_{n}}{y_{\pi}}$ 的极限，144题即是一例。应用此结果，也可证明 138题及 139 题的结果（此结果属于哥西 Cauchy）. 事实上，令

$$
x_{n}^{\prime}=x_{1}+x_{2}+\cdots+x_{n}, y_{n}^{\prime}=n,
$$

则 $\lim _{n \rightarrow \infty} \zeta_{n}=\lim _{n \rightarrow \infty} \frac{x_{1}+x_{2}+\cdots+x_{n}}{n}=\lim _{n \rightarrow \infty} \frac{x^{\prime} y^{\prime}}{n}$

$$
=\lim _{n \rightarrow \infty} \frac{x_{n+1}^{\prime}-x^{\prime}}{y_{n+1}^{\prime}-y^{\prime}}=\lim _{n \rightarrow \infty} x_{n+1}=\lim _{n \rightarrow \infty} x_{n} .
$$

145. 证明：若 $p$ 为自然数，则

$$
\text { (a) } \lim _{n \rightarrow \infty} \frac{1^{p}+2^{p}+\cdots+n^{p}}{n^{p+1}}=\frac{1}{p+1} \text {; }
$$

(6) $\lim _{n \rightarrow \infty}\left(\frac{1^{p}+2^{p}+\cdots+n^{p}}{n^{p}}-\frac{n}{p+1}\right)=\frac{1}{2}$;
(в) $\lim _{n \rightarrow \infty} \frac{1^{p}+3^{p}+\cdots+(2 n-1)^{p}}{n^{p+1}}=\frac{2^{p}}{p+1}$.

证（a）令 $x_{n}=1^{p}+2^{p}+\cdots+n^{p}, y_{n}=n^{p+1}$ ，
则 $y_{n+1}>y_{n}, y_{n} \rightarrow+\infty$ ，且有

$$
\frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=\frac{(n+1)^{p}}{(n+1)^{p+1}-n^{p+1}}=\frac{(n+1)^{p}}{(p+1) n^{p}}+\cdots
$$

$$
=\frac{\left(1+\frac{1}{n}\right)^{p}}{p+1+o\left(\frac{1}{n}\right)} \rightarrow \frac{1}{p+1},
$$

式中 $\lim _{n \rightarrow \infty}\left(\frac{1}{n}\right)=0$ 为无穿小，以下不再说明，
故 $\lim _{n \rightarrow \infty} \frac{x_{n}}{y_{n}}=\lim _{n \rightarrow \infty} \frac{1^{p}+2^{p}+\cdots+n^{p}}{n^{p+1}}=\frac{1}{p+1}$.

$$
\begin{aligned}
\text { (6) 令 } x_{n}= & (p+1)\left(1^{p}+2^{p}+\cdots+n^{p}\right)-n^{p+1}, \\
y_{n} & =(p+1) n^{p},
\end{aligned}
$$

则 $y_{n+1}>y_{n}, y_{n} \rightarrow+\infty$ ，月有

$$
\begin{aligned}
& \frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}}=\frac{(p+1)(n+1)^{p}\left[n^{p-1}-(n+1)^{p+1}\right]}{\left.(p+1)_{-}(n+1)^{p}-n^{p}\right]} \\
&=\frac{p(p+1)}{2} n^{p-1}+\cdots \\
& p(p+1) n^{p-1}+\cdots .
\end{aligned}
$$

当 $n \rightarrow \infty$ 时， $\frac{x_{n+1}-x_{n}}{y_{n+1}-y_{\pi}} \rightarrow \frac{1}{2}$ ，所以，

$$
\begin{aligned}
& \lim _{x \rightarrow \infty} \frac{x_{n}}{y_{n}}=\lim _{n \rightarrow \infty}\left(\frac{1^{p}+2^{p}+\cdots+n^{p}}{n^{p}}-\frac{n}{p+1}\right)=\frac{1}{2} . \\
& \text { (B) 令 } x_{n}=1^{p}+3^{p}+\cdots+(2 n-1)^{p}, y_{n}=n^{p+1},
\end{aligned}
$$

则 $y_{n+1}>y_{n}, y_{\pi} \rightarrow+\infty$, 且有

$$
\begin{aligned}
\frac{x_{n+1}-x_{n}}{y_{n+1}-y_{n}} & =\frac{(2 n+1)^{p}}{(n+1)^{p+1}-n^{p+1}}=\frac{(2 n+1)^{p}}{(p+1) n^{p}+\cdots} \\
& =\frac{\left(2+\frac{1}{n}\right)^{p}}{p+1+o\left(\frac{1}{n}\right)} \rightarrow \frac{2^{p}}{p+1}
\end{aligned}
$$

所以，

$$
\lim _{n \rightarrow \infty} \frac{x_{n}}{y_{n}}=\lim _{n \rightarrow \infty} \frac{1^{p}+3^{p}+\cdots+(2 n-1)^{p}}{n^{p+j}}
$$

$$
=\frac{2^{r}}{p+1} .
$$

146. 证明：叙列

$$
x_{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{l}{n}-\ln n(n=1,2, \cdots
$$

收敛。
因此有公式

$$
1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}=C+\ln n+\varepsilon_{n},
$$

式克 $C=0.577216 \cdots$ 称为尤拉常数，且当 $n \rightarrow \infty$ 时， $e_{n} \rightarrow$ 0 .
证 因为 $\ln \left(1+\frac{1}{n}\right)<\frac{1}{n}^{+}$.
故 $\quad \ln (n+1)-\ln n<\frac{1}{n}$,
令 $n=1,2,3, \cdots n$ 得出

$$
\begin{aligned}
& 1 n 2-\ln 1<1 \\
& \ln 3-\ln 2<\frac{1}{2} \\
& \ln 4-\ln 3<\frac{1}{3}
\end{aligned}
$$

$$
\ln (n+1)-\ln n<\frac{1}{n},
$$

相加之得

$$
\ln (n+1)<1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n} .
$$

于是，

$$
\begin{aligned}
x_{n+1} & =1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}+\frac{1}{n+1}-\ln (n+1) \\
& >\frac{1}{n+1}>0
\end{aligned}
$$

斯 $\left\{x_{1}\right\}$ 是一个有下界的叙列，其次，

$$
\begin{gathered}
x_{n}-x_{n+1}=-\frac{1}{n+1}+\ln (n+1)-\ln n \\
=\ln \left(1+\frac{1}{n} \left\lvert\,-\frac{1}{n+1}\right.\right.
\end{gathered}
$$

因为 $-\frac{1}{n \div-1}<\ln \left(1+\frac{1}{n}\right)^{* *}$ ，所以 $x_{n} \cdots x_{n+1}>0$ ，这就是
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-097.jpg?height=104&width=1460&top_left_y=845&top_left_x=344)㳖示之，即

$$
C=\lim _{n \rightarrow \infty}\left(1+\frac{1}{2}+\frac{1}{3}+\cdots+\cdots \frac{1}{n}-\ln n\right),
$$

它的近倾㑲为 0.577216 ，或表成

$$
1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}=C+\ln n+\varepsilon_{n},
$$

其中 $\lim _{n \rightarrow \infty}=0$ 。
*）及＊＊）利用 75 题（a）的结果。
147. 求

$$
\lim _{x+\infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}\right) .
$$

## 解 因为

$$
\begin{aligned}
& 1+\frac{1}{2}+\cdots+\frac{1}{n}=C+\ln n+\varepsilon_{n} \\
& 1+\frac{1}{2}+\cdots+\frac{1}{2 n}=C+\ln 2 n+\epsilon_{2 n}
\end{aligned}
$$

其中 $C$ 为尤拉常数， $\epsilon_{n} \rightarrow 0, \varepsilon_{2 n} \rightarrow 0(n \rightarrow \infty)$ 。
（2）式减（1）式得

$$
\begin{gathered}
\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}=\ln 2 n-\ln n+\left(\varepsilon_{2 n}-\varepsilon_{n}\right) \\
\quad=\ln 2+\left(\varepsilon_{2 n}-\varepsilon_{n}\right) \rightarrow \ln 2(n \rightarrow \infty),
\end{gathered}
$$

所以，

$$
\lim _{n \rightarrow \infty}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2 n}\right)=\ln 2
$$

148. 数列 $x_{n}(n=1,2, \cdots)$ 是由下列各式

$$
x_{1}=a, x_{2}=b, x_{n}=\frac{x_{n-1}+x_{n-2}}{2}(n=3,4, \cdots)
$$

所确定. 求

$$
\lim _{n \rightarrow \infty} x_{n}
$$

## 解 由于

$$
\begin{aligned}
x_{n+1}-x_{n} & =\frac{x_{n}+x_{n-1}}{2}-x_{n}=\frac{x_{n-1}-x_{n}}{2} \\
& =\cdots=\frac{x_{2}-x_{1}}{(-2)^{n-1}}=\frac{b-a}{(-2)^{n-1}}
\end{aligned}
$$

及

$$
\begin{aligned}
x_{n+1} & =\sum_{m=1}^{n}\left(x_{m+1}-x_{m}\right)+x_{1} \\
& =(b-c) \sum_{n=1}^{n} \frac{1}{(-2)^{m-i}}+a,
\end{aligned}
$$

所以

$$
\lim _{n \rightarrow-\infty} x_{n}=\frac{b-a}{1-\left(-\frac{1}{2}\right)}+a=\frac{a+2 b}{3}
$$

149. 设 $a>0$ 和 $x_{n}(n=1,2, \cdots)$ 为由以下各式

$$
x_{0}>0, x_{n+1}=\frac{1}{2}\left(x_{n}+\frac{a}{x_{n}}\right)(n=0,1,2, \cdots)
$$

所确定的数列. 求证

$$
\lim _{n \rightarrow \infty} x_{n}=\sqrt{a} .
$$

证 由 $x_{n+1}=\frac{1}{2}\left(\sqrt{x_{n}}-\frac{\sqrt{a}}{\sqrt{x_{n}}}\right)^{2}+\sqrt{a} \geqslant \sqrt{a}$

$$
(n=0,1,2, \cdots),
$$

则 $x_{n+1}-x_{n}=\frac{1}{2}\left(\frac{a}{x_{n}}-x_{n}\right) \leqslant 0$ 。
知 $\left\{x_{n}\right\}$ 为单调下降的有界数列，必有极限存在。设其极限为 $l$, 则 $l \geqslant \sqrt{a}>0$ ，对于等式

$$
x_{n-1}=\frac{1}{2}\left(x_{n}+\frac{a}{x_{n}}\right)
$$

两端取极限，即得

$$
l=\frac{1}{2}\left(l+\frac{a}{l}\right),
$$

解之得

$$
l=\sqrt{a} \text { (负值不合适), }
$$

故证得

$$
\lim _{n \rightarrow \infty} x_{n}=\sqrt{a} .
$$

150. 证明由下列各式

$$
x_{1}=a, y_{1}=b, x_{n+1}=\sqrt{x_{n} y_{n}}, y_{n+1}=\frac{x_{n}+y_{n}}{2} \text {, }
$$

确定的叙列 $x_{n}$ 和 $y_{n}(n=1,2, \cdots)$ 有公共的极限

$$
\mu(a, b)=\lim _{n \rightarrow \infty} x_{n}=\lim _{n-\infty} y_{n}
$$

（数 $a$ 和 $b$ 的算术一几何平均数）。
证 分两种情形：
1） $a$ 与 $b$ 中至少有一个为零，例如，设 $a=0$ 。则显然有 $x_{n}$ $=0(n=1,2, \cdots), y_{n+1}=\frac{y_{n}}{2}$ ，从而，递推得

$$
y_{x}=\frac{b}{2^{*-1}}(n=1,2, \cdots)
$$

由此可知

$$
\lim _{n \rightarrow \infty} x_{n}=0=\lim _{n \rightarrow \infty} y_{n}
$$

2) 设 $a \neq 0, b \neq 0$. 这吋，必须 $a>0, b>0$ 。否则，若 $a b<0$ ，则 $x_{2}=a b$ 没有意义; 若 $a<0, b<0$, 则 $x_{2}=\sqrt{a b}>0, y_{2}=$ $\frac{a+b}{2}<0$ ，从而 $x_{3}=\sqrt{x_{2} y_{2}}$ 没有意义。因此，必须 $a>0, b$ $>0$ 。不妨假定 $a \leqslant b$ 。由于两正数的等比中项不超过它们的等差中项，并且都界于原来两数之间，故有

$$
a \leqslant x_{2} \leqslant y_{2} \leqslant b,
$$

由此又有

$$
a \leqslant x_{2} \leqslant x_{3} \leqslant y_{3} \leqslant y_{2} \leqslant b .
$$

应用数学腈纳法可知一般有

$$
a \leqslant x_{n} \leqslant x_{n+1} \leqslant y_{n+1} \leqslant y_{n} \leqslant b . \quad(n=2,3, \cdots) .
$$

故 $\left\{x_{n}\right\}$ 为单调增大的有界数列， $\left\{y_{n}\right\}$ 为单调减小的有界数列，因此它们的极限都存在，令

$$
\lim _{n \rightarrow \infty} x_{n}=\alpha, \lim _{n \rightarrow \infty} y_{n}=\beta .
$$

在等式

$$
y_{n-1}=\frac{x_{n}+y_{n}}{2}
$$

两端取报限，得

$$
\beta=\frac{\alpha+\beta}{2},
$$

故 $\alpha=\beta$ ，即

$$
\lim _{n \rightarrow \infty} x_{n}=\lim _{n \rightarrow \infty} y_{n} .
$$

证毕.

## §3. 函数的概念

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-101.jpg?height=72&width=1463&top_left_y=638&top_left_x=336)实数 $y \in Y=\{y\}$ 与之对应，则变量 $y$ 称为变量 $x$ 在已知变域 $X$ 的单值唒数 $f$ 。并记为 $y=f(x)$ 。

集合 $X$ 名为函数 $f(x)$ 的定义㳦或存在域； $Y$ 称为这个函数的值域、在最简单的情形下，集合 $X$ 或为开区间 $(a, b): a<x<b$ ，或为半正区间 $(a, b]: a<x \leqslant b$ 或 $[a, b$ ): $a \leqslant x<b$ ，或为闭区㽤（线段 $[a, b]: a$ $\leqslant x \leqslant b$ ，其中 $a$ 稩 $b$ 为某实数或符号 $\cdots \infty$ 和 $+\infty$ 。

若对于 $X$ 中的每一个值 $x$ 有若 个个值 $y=f(x)$ 与乙对应，则 $y$ 称为 $x$ 的多值函数。
$2^{2}$ 发函数 若把 $x$ 了解为满足方程式

$$
f(x)=y
$$

（式中 $y$ 为骬于函数 $f(x)$ 的值域 $Y$ 中之一固定数值）的仼何数植，则这个对应关系确定出在集合 $Y$ 上的某函数

$$
x=f^{-t}(y),
$$

这个荬数称为函数 $f(x)$ 的区函数，这个函数一般地说来是多值的。若函数 $y=f(x)$ 是严格单调的，即当 $x_{2}>x_{1}$ 时， $f\left(x_{2}\right)>f\left(x_{1}\right)$ [或相应地 $\left.f\left(x_{2}\right)<f\left(x_{1}\right)\right]$ ，则反函数 $x=f^{-1}(y)$ 为单值而且严格的单调函数。

求下列函数的存在域：
151. $y=\frac{x^{2}}{1+x}$.

解 当 $1+x \neq 0$ ，即 $x \neq-1$ 时，函数 $y$ 才有意义，所以，
它的存在域为 $(-\infty,-1),(-1,+\infty)$ 。
152. $y=\sqrt{3 x-x^{3}}$.

解 存在域为满足不等式

$$
3 x-3 x^{3} \geqslant 0
$$

的实数 $x$ 的集合，解之，得存在域为 $(-\infty,-\sqrt{3}],[0$, $\sqrt{3}]$.
153. ${ }^{+} y=(x-2) \sqrt{\frac{1-x}{1-x}}$.

解 当 $\frac{1+x}{1-x} \geqslant 0$ 时， $y$ 值确定。
解之，得存在域为满足

$$
-1 \leqslant x<1
$$

的数 $x$ 的集合。
154. (a) $y=\log \left(x^{2}-4\right)$ ，(6) $y=\log (x+2)+\log (x-2)$.

解 (a) 当 $x^{2}-4>0$ 时, $y$ 值确定. 解之, 得存在域为 ( $\infty,-2),(2,+\infty)$ 。
(б)函数 $y$ 由两个函数组成，其中第一个函数的存在域为 $(-2,+\infty)$ ，而第二个函数的存在域为 $(2,+\infty)$ ，于是，函数 $y$ 的存在域为它们的公共部分，即 $(2,+\infty)$ 。
155. $y=\sqrt{\sin (\sqrt{x})}$.

解 当 $\sin \sqrt{x} \geqslant 0$ 时, $y$ 值才为确定的实数. 解之, 得
$2 k \pi \leqslant \sqrt{x} \leqslant(2 k+1) \pi \quad(k=0,1,2, \cdots)$.
存在域为满足不等式

$$
4 k^{2} \pi^{2} \leqslant x \leqslant(2 k+1)^{2} \pi^{2}(k=0,1,2, \cdots)
$$

的数 $x$ 的集合。
156. $y=\sqrt{\cos x^{2}}$.

解 当 $\cos x^{2} \geqslant 0$ 时， $y$ 值才为确定的实数，即只要 $x$ 满足

$$
\begin{aligned}
& 0 \leqslant x^{2} \leqslant \frac{\pi}{2} 及(4 k-1) \frac{\pi}{2} \leqslant x^{2} \leqslant(4 k+1) \frac{\pi}{2} \\
&(k=1,2, \cdots) .
\end{aligned}
$$

解之，得存在域为满足不等式

$$
\begin{gathered}
|x| \leqslant \sqrt{\frac{\pi}{2}} \text { 及 } \sqrt{(4 k-1) \frac{\pi}{2}} \leqslant|x| \leqslant \sqrt{(4 k+1) \frac{\pi}{2}}(k=1,2, \cdots)
\end{gathered}
$$

的数 $x$ 的集合。
$157 . y=\log \left(\sin \frac{\pi}{x}\right)$.
解 当 $\sin \frac{\pi}{x}>0$ 时， $y$ 值确定，即只要

$$
2 k \pi<\frac{\pi}{x}<(2 k+1) \pi \quad(k=0,1,2, \cdots)
$$

及

$$
-(2 k+2) \pi<\frac{\pi}{x}<-(2 k+1) \pi
$$

所以，存在域为满足不等式

$$
\frac{1}{2 k+1}<x<\frac{1}{2 k}, \quad(k=0,1,2, \cdots)
$$

及

$$
-\frac{1}{2 k+1}<x<-\frac{1}{2 k+2}
$$

的数 $x$ 的集合。
158. $y=\frac{\sqrt{x}}{\sin \pi x}$.

解 当 $x \geqslant 0$ 及 $\sin \pi x \neq 0$ 时， $y$ 值确定，解之，得仔在域为满足关系式

$$
x>0, x \neq n(n=1,2, \cdots)
$$

的数 $x$ 的集合。
159. $y=\arcsin \frac{2 x}{1+x}$.

解 当 $\left|\frac{2 x}{1+x}\right| \leqslant 1$ 时， $y$ 值确定。解之，得

$$
-1 \leqslant \frac{2 x}{1+x} \leqslant 1,
$$

$$
\begin{aligned}
& -1 \leqslant 2-\frac{2}{1+x} \leqslant 1, \\
& -3 \leqslant-\frac{2}{1+x} \leqslant-1, \\
& -\frac{2}{3} \leqslant 1+x \leqslant 2 .
\end{aligned}
$$

最后得存在域为满足不等式

$$
-\frac{1}{3} \leqslant x \leqslant 1
$$

的数 $x$ 的集合
160. $y=\operatorname{arc} \cos (2 \sin x)$ 。

解 当 $2 \sin x \mid \leqslant 1$ 时， $y$ 值确定，解之，得
存在域为满足不等式

$$
|x-k x| \leqslant \frac{\pi}{6} \quad(k=0, \pm 1, \pm 2, \cdots)
$$

的数 $x$ 的集合。
161. $y=\lg [\cos (\lg x)]$.

解 当 $\cos (\lg x)>0$ 时， $y$ 值确定，解之，得

$$
\left(2 k-\frac{1}{2}\right) \pi<\lg x<\left(2 k+\frac{1}{2}\right) \pi
$$

从而存在域为满足不等式

$$
\begin{gathered}
\left.10^{\left(2 k-\frac{1}{2}\right)}\right)<x<10^{\left(2 k+\frac{1}{2}\right) \pi} \\
(k=0, \pm 1, \pm 2, \cdots) .
\end{gathered}
$$

所数 $x$ 的集合。
762. $y=\left(x-|x| \sqrt{-\sin ^{2} \pi x}\right.$.

解 由于 $\sin ^{2} \pi x \geqslant 0$,故仅当 $\sin \pi x=0$ 时 $\sqrt{-\sin ^{2} \pi x}$ 才有 98

意义，从而函数 $y$ 才有意义. 解之，得存在域为

$$
x=k \quad(k=0, \pm 1, \pm 2, \cdots) .
$$

163. $y=\operatorname{ctg} \pi x+\operatorname{arc} \cos \left(2^{x}\right)$.

解 当 $\sin \pi x \neq 0$ 时, 第一项有意义,即 $x \neq k(k=0 . \pm 1$, $\pm 2, \cdots)$ 。

当 $0 \leqslant 2^{2} \leqslant 1$ 时，第二项有意义，即 $x \leqslant 0$ 。由此得存在域为满足关系式

$$
x<0, x \neq-n \quad(n=1,2, \cdots)
$$

的数 $x$ 的集合。
164. $y=\arcsin (1-x)+\lg (\lg x)$.

解 当 $-1 \leqslant 1-x \leqslant 1$, 即 $0 \leqslant x \leqslant 2$ 时, 第一个函数有意义;

当 $\lg x>0$ ，即 $x>1$ 时，第二个函数有意义。
由此得存在域为满足不等式

$$
1<x \leqslant 2
$$

的数 $x$ 的集合。
$165^{+}+y=(2 x) \mathrm{I}$ 。
解 当 $2 x=n(n=0,1, \cdots)$ 时， $y$ 值确定，所以，存在域为集合：

$$
0, \frac{1}{2}, 1, \frac{3}{2}, 2, \frac{5}{2}, \cdots, \frac{n}{2}, \cdots
$$

求下列函数的存在域和函数值域：
166. $y=\sqrt{2+x-x^{2}}$.

解 当 $2+x-x^{2} \geqslant 0$ 时， $y$ 值确定。解之，得存在域为满足不等式

$$
-1 \leqslant x \leqslant 2
$$

的数 $x$ 的集合. 又因

$$
y=\sqrt{\frac{9}{4}-\left(x-\frac{1}{2}\right)^{2}} \leqslant \frac{3}{2},
$$

所以，函数值域为满足不等式

$$
0 \leqslant y \leqslant \frac{3}{2}
$$

的数 $y$ 的集合。
167. $y=\lg (1-2 \cos x)$.

解 当 $1-2 \cos x>0$ 时， $y$ 值确定，解之，得存在域为满足不等式

$$
2 k \pi+\frac{\pi}{3}<x<2 k \pi+\frac{5 \pi}{3} \quad(k=0, \pm 1, \pm 2 \cdots)
$$

的数 $x$ 的集合 $A$. 因为

$$
\begin{aligned}
& \max _{x \in A}(1-2 \cos x)=1-(-2)=3, \\
& \inf _{x \in A}(1-2 \cos x)=0,
\end{aligned}
$$

所以，函数值域为满足不等式

$$
-\infty<y \leqslant \lg 3
$$

的数 $y$ 的集合。
168. $y=\arccos \frac{2 x}{1+x^{2}}$.

解 当 $\left|\frac{2 x}{1+x^{2}}\right| \leqslant 1$ 时， $y$ 值确 定，而对于 $-\infty<x<+$ $\infty$ 来说，始终有 $\left|\frac{2 x}{1+x^{2}}\right| \leqslant 1$ ，所以，存在域为全体实数所组成的集合，而函数值域为闭区间 $[o, \pi]$ 。
169. $y=\arcsin \left(\lg \frac{x}{10}\right)$ 。

䉽 当 $-1 \leqslant \lg \frac{x}{10} \leqslant 1$ 时, 即当 $\frac{1}{10} \leqslant \frac{x}{10} \leqslant 10$, 或 $1 \leqslant x \leqslant$ 100 时, $y$ 值确定, 且在 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 上变化, 所以, 存在域为闲区间 $[1,100]$ ，函数值域为 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 。 170. $y=(-1)^{2}$.

䉽 存在域为数 $x: x=\frac{p}{2 q+1}$ （ $p, q$ 为整数）的集合，而函数值域为: $y=(-1)^{p}$, 即由 $-1,1$ 两数组成的集合。
171. 在底为 $A C=b$ 和高为 $B D=h$ 的三角形 $A B C$ 中（图12）内接一个高为 $N M=x$ 的矩形 $K L M N$ ，把矩形 $K L M N$ 的周长 $P$ 及其面积 $S$ 表为 $x$ 之函数。

作函数 $P=P(x)$ 及 $S=S$ （ $x$ ）的图形。
解 因为 $\frac{L M}{b}=\frac{h-x}{h}$ ，
所以，

$$
L M=b\left(1-\frac{x}{h}\right)
$$

周长 $P=2 L M+2 x$ ，即
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-107.jpg?height=586&width=681&top_left_y=1306&top_left_x=1070)

图1.2

$$
P=P(x)=2\left(1-\frac{b}{h}\right) x+2 b,
$$

式中 $0<x<h$ 。
当 $b<h$ 时,如图1-3中直线段 $A B$ 所示（不包含 $A, B$ 两点)。

当 $b>h$ 时，如图 $1 \cdot 3$ 中直线段 $A C$ 所示（不包含 $A, C$ 两点)。其中 $O A=2 b, B$ 和 $C$ 的坐标为 $h$ 和 $2 h$.矩形面积

$$
\begin{aligned}
& S=L M \cdot x=b x \\
& \cdot\left(1-\frac{x}{h}\right)(0<x<h) .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-108.jpg?height=72&width=1451&top_left_y=592&top_left_x=348)杵 $\overline{O A B}$ 。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-108.jpg?height=638&width=663&top_left_y=863&top_left_x=251)

图 1.3
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-108.jpg?height=498&width=846&top_left_y=910&top_left_x=933)

图 1.4
172. 在三角形 $A B C$ 中, 边 $A B=6$ 厘米, 边 $A C=8$ 里米, 角 $B A C=x$ ，把边 $B C=a$ 和面积 $A B C=S$ 表为变量 $x$ 的棌数。作函数 $a=a(x)$ 及 $S=S(x)$ 的图形。
解 利用余弦定理得三角形的边

$$
\begin{array}{r}
a=\sqrt{6^{2}+8^{2}-2+6 \cdot 8 \cos x}=\sqrt{100-96 \cos x} \\
(0<x<\pi),
\end{array}
$$

如图 $1 \cdot 5$ 所示 (系一不包含 $A$ 点及 $B$ 点的曲线沠 $\overparen{A B}$ ).而三角形的面积

$$
S=\frac{1}{2} \cdot 6 \cdot 8 \sin x=24 \sin x(0<x<\pi) .
$$

如图 1-6 所示 (两轴单位取得不同, 系一不包含 $O$ 点改 $A$ 点的弧 $\overparen{O B A}$ 。.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-109.jpg?height=661&width=523&top_left_y=366&top_left_x=384)

图1.5
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-109.jpg?height=550&width=781&top_left_y=476&top_left_x=946)

䀱1.6
173. 在等婹梯形 $A B C D$ 执（图 1 - 7)，底为 $A D=a, B C=b(a$ $>b)$ ，商为 $H B=h$ ，引直线 $M N \| B H, M N$ 与顶点 $A$ 相距 $A M=x$ ，把图形 $A B N M A$ 的面积 $S$ 表为变量 $x$ 的函数. 作瞆数 $S=S(x)$ 的图形。
解 $A M=\frac{1}{2}(a-b)$ ，分三种情况讨论：
(1) 当 $0 \leqslant x \leqslant \frac{a-b}{2}$ 时, 即 $M N$ 线在 $\triangle A B H$ 内, 此时

$$
\frac{M N}{h}=\frac{x}{\frac{a}{2}} \cdot M N=\frac{2 h x}{a-b} .
$$

于踑，

$$
S=\frac{1}{2} M N \cdot x=\frac{h a^{2}}{a-b},
$$

如图1-8中㽴

$$
\begin{gathered}
\text { (2) 当 } \frac{a-b}{2}<x<\frac{a-b}{2}+b=\frac{a+b}{2} \text { 时, 面积 } \\
S=\frac{a-b}{2} \cdot \frac{h}{2}+h\left(x-\frac{a-b}{2}\right)=h\left(x-\frac{a-b}{4}\right),
\end{gathered}
$$

如图 1.8 中不含 $A$ 点及 $B$ 点的直线段 $A B$.
（3）当 $\frac{a+b}{2} \leqslant x \leqslant a$ 时，向积
$S=\frac{h(a+b)}{2}-\frac{h}{a-b} \cdot\left(a-a^{a}\right)=h\left[\frac{a+b}{2}-\frac{(a-x)^{2}}{a-b}\right]$,
如圂1 - 8 中抛物线段 $\widehat{B C}$ 。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-110.jpg?height=746&width=1480&top_left_y=875&top_left_x=342)

图 1.7

图1-8中各点的位置如下：

$$
\begin{aligned}
& A\left(\frac{a-b}{2}, \frac{h(a-b)}{4}\right), B\left(\frac{a+b}{2}, \frac{h(a+3 b)}{4}\right), \\
& C\left(a, \frac{h(a+b)}{2}\right)
\end{aligned}
$$

又 $\operatorname{tg} \alpha=h$ 。
174. 在 $O x$ 轴上的闭区间 $0 \leqslant x \leqslant 1$ 内有等于 2 克的质量均匀地分布省，而在此轴上的两点 $x=2$ 和 $x=3$ 有集中的质黒各 1 克。

设 $m(x)$ 是介于区间 $(-\infty, x)$ 的质量的值，求函数 $m=m(x)(-\infty<x<+\infty)$ 的解析表示式。并作这个函

数的图形。
解 当 $-x<x \leqslant 0$ 时， $m(x)=0$ ；
当 $0<x \leqslant 1$ 时，因为
$1: x=2: m(x)$,
于是,

$$
\begin{aligned}
& m(x)=2 x ; \\
& \text { 当 } 1<x \leqslant 2 \text { 时, } m(x)=2 ; \\
& \text { 当 } 2<x \leqslant 3 \text { 时, } m(x)=3 ; \\
& \text { 当 } 3<x<+\infty \text { 时, } m(x)=4 .
\end{aligned}
$$

如图 1 - 9 所示。
175. 函数 $y=\operatorname{sgn} x$ ，用下列方法来定义：

$$
\operatorname{sgn} x=\left\{\begin{array}{l}
\text {, 若 } x>0 ; \\
0, \text { 若 } x=0 ; \\
-1, \text { 若 } x<0 .
\end{array}\right.
$$

作这个函数的图形. 证明

$$
|x|=x \operatorname{sgn} x
$$

解 函数 $\operatorname{sgn} x$ 的图形如图 $1 \cdot 10$ 所示.因为

当 $x<0$ 时,
$|x|=-x=x \operatorname{sgn} x ;$
当 $x=0$ 时,

$$
|x|=0=x \operatorname{sgn} x ;
$$

当 $x>0$ 时,

$$
|x|=x=x \operatorname{sgn} x .
$$

所以，
$|x|=x \operatorname{sgn} x$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-112.jpg?height=586&width=755&top_left_y=438&top_left_x=316)

图1.9
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-112.jpg?height=421&width=627&top_left_y=589&top_left_x=1080)

图 1.10
176. 函数 $y=[x]$ (数 $x$ 的整数部分)用下法定义：若 $x=n+$ $r$, 式中 $n$ 为整数且 $0 \leqslant r<1$, 则
$[x]=n$.
作这个函数的图形。
解 当 $x \in[n, n+1]$ 时 ( $n$ 为整数) $y=n$ ，如图 1 - 11 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-112.jpg?height=698&width=764&top_left_y=1667&top_left_x=686)

图1.11
177. 设：

$$
y=\pi(x) \quad(x \geqslant 0),
$$

表示不就过数 $x$ 的素数的数目，对于自变数 $0 \leqslant x \leqslant 20$的造，作这个函数的图形。
解 按题没可知：
当 $0 \leqslant x<2$ 时， $\pi(x)=0$ ；
当 $2 \leqslant x<3$ 时， $\pi(x)=1$ ；
当 $3 \leqslant x<5$ 时， $\pi(x)=2$ ；
当 $5 \leqslant x<7$ 时， $\pi(x)=3$ ；
当 $7 \leqslant x<11$ 时， $\pi(x)=4$ ；
当 $11 \leqslant x<13$ 时， $\pi(x)=5$ ；
当 $13 \leqslant x<17$ 时， $\pi(x)=6$ ；
当 $17 \leqslant x<19$ 时， $\pi(x)=7$ ；
当 $19 \leqslant x \leqslant 20$ 时， $\pi(x)=8$ （如图 1 - 12 所示）。
函数 $y=f(x)$ 在复样的集合 $E_{y}$ 上咉出集合 $E_{x}$, 若:
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-113.jpg?height=506&width=878&top_left_y=1620&top_left_x=572)

图 1.12
178. $y=x^{2}, E_{x}=\{1 \leqslant x \leqslant 2\}$.

解 $E_{y}\{1 \leqslant y \leqslant 4\}$.
179. $y=\lg x . E_{x}=\{10<x<1000\}$.

解 $E_{J}=\{1<y<3\}$.
180. $y=\frac{1}{\pi} \operatorname{arcctg} x, E_{x}=\{-\infty<x<+\infty\}$.

解 $E_{y}=\{0<y<1\}$.
181. $y=\operatorname{ctg} \frac{\pi x}{4}, E_{x}=\{0<|x| \leqslant 1\}$.

解 $E_{y}\{1<|y|<+\infty\}$ 。
182. $y=|x|, E_{x}=\{1 \leqslant|x| \leqslant 2\}$.

解 $E_{y}=\{1 \leqslant y \leqslant 2\}$ 。
变量 $x$ 跑过区间 $0<x<1$ ，则变量 $y$ 跑过怎样的集合，若 183. $y=a+(b-a) x$.

解 变量 $x$ 从 0 变至 1 时, $y$ 从 $a$ 变至 $b$ 。于是, 变量 $y$ 的变化区间为 $a<y<b($ 当 $a<b$ )或 $b<y<a($ 当 $b<a)$ 。
184. $y=\frac{1}{1-x}$.

解 当 $x$ 从 0 变至 1 时, $y$ 从 1 变至正无穷大。于是, $y$ 的变化区间为 $1<y<+\infty$ 。
185. $y=\frac{x}{2 x-1}$.

解 $y=\frac{1}{2}+\frac{1}{2} \cdot \frac{1}{2 x-1}$.
当 $x$ 从 0 变至 $\frac{1}{2}, y$ 从 0 变至负无穷大；当 $x$ 从 $\frac{1}{2}$ 变至 1 时, $y$ 从正无穷大变至 1 . 于是, $y$ 的变化区间为 $-\infty$ $<y<0,1<y<+\infty$ 。
186. $y=\sqrt{x-x^{2}}$.

解 $y=\sqrt{\frac{1}{4}-\left(x-\frac{1}{2}\right)^{2}}$.
当 $x=\frac{1}{2}$ 时， $y=\frac{1}{2}$ （最大值）；由于 $x$ 趋于 0 时， $y$ 赩于 0 , 而 $y>0$ ，从而 $y=0$ 是变量 $y$ 的下确界。于是， $y$ 的 108

变化区间为 $0<y \leqslant \frac{1}{2}$.
187. $y=\operatorname{ctg} \pi x$.

䈎 当 $x$ 从 0 变至 1 时，变量 $y$ 从 $+\infty$ 变至 $-\infty$ 。于是，变量 $y$ 的变化区间为 $-\infty<y<+\infty$ 。
188. $y=x+[2 x]$.

解 当 $x$ 从 0 变至 $\frac{1}{2}$ 时, $y$ 从 0 变至 $\frac{1}{2}$ ；当 $x$ 从 $\frac{1}{2}$ 变至 1时， $y$ 从 $\frac{3}{2}$ 变至 2 。于是， $y$ 的变化区间为 $0<y<\frac{1}{2}, \frac{3}{2} \leqslant$ $y<2$.
189. 设：

$$
f(x)=x^{4}-6 x^{3}+11 x^{2}-6 x,
$$

求 $f(0), f(1), f(2), f(3), f(4)$ 。
解 因为 $f(x)=x(x-1)(x-2)(x-3)$,
所以，

$$
\begin{aligned}
& f(0)=f(1)=f(2)=f(3)=0, \\
& f(4)=24 .
\end{aligned}
$$

190. 设：

$$
f(x)=\lg x^{2},
$$

求 $f(-1), f(-0.001), f(100)$.
解 $f(-1)=\lg 1=0$ ；

$$
\begin{aligned}
& f(-0.001)=\lg 0.000001=-6 ; \\
& f(100)=\lg 10000=4 .
\end{aligned}
$$

191. 设:

$$
f(x)=1+[x]
$$

求 $f(0.9), f(0.99), f(0.999), f(1)$.

解 $f(0.9)=f(0.99)=f(0.999)=1$ ，

$$
f(1)=2
$$

192. 设：

$$
f(x)=\left\{\begin{array}{l}
1+x, \text { 当 }-\infty<x \leqslant 0 ; \\
2^{x}, \text { 当 } 0<x<+\infty \text { 。 }
\end{array}\right.
$$

求 $f(-2), f(-1), f(0), f(1), f(2)$ 。
解 $f(-2)=1-2=-1, f(-1)=1-1=0$ ，

$$
\begin{aligned}
& f(0)=1+0=1, f(1)=2^{1}=2, \\
& f(2)=2^{2}=4
\end{aligned}
$$

193. 设 :

$$
f(x)=\frac{1-x}{1+x}
$$

求 $f(0), f(-x), f(x+1), f(x)+1, f\left(\frac{1}{x}\right), \frac{1}{f(x)}$.
解 $f(0)=1$,

$$
\begin{aligned}
& f(-x)=\frac{1+x}{1-x}, \\
& f(x+1)=\frac{1-(x+1)}{1+(x+1)}=-\frac{x}{x+2},
\end{aligned}
$$

$$
\begin{aligned}
& f(x)+1=\frac{1-x}{1+x}-1=\frac{2}{1+x} . \\
& f\left(\frac{1}{x}\right)=\frac{1-\frac{1}{x}}{1+\frac{1}{x}}=\frac{x-1}{x+1} . \\
& \frac{1}{f(x)}=\frac{1}{\frac{1-x}{1+x}}=\frac{1+x}{1-x} .
\end{aligned}
$$

194. 设：

$$
\text { (a) } f(x)=x-x^{3} ;(6) f(x)=\sin \frac{\pi}{x} ;
$$

$$
\text { (B) } f(x)=(x+|x|)(1-x)
$$

求使以下各式满足的 $x$ 值：
(1) $f(x)=0$ ；（2） $f(x)>0$ ；（3） $f(x)<0$.

解 (a)（1） $x-x^{3}=0$ ，所以， $x=0,1$ 及 -1 。
(2) $x-x^{3}>0$, 即 $x(1-x)(1-x)>0$,

所以， $-\infty<x<-1$ 和 $0<x<1$.
(3) $x(1-x)(1+x)<0$, 所以, $-1<x<0$ 和 $1<x<$ $+\infty$ 。
(6) (1) $\sin \frac{\pi}{x}=0$, 则 $\frac{\pi}{x}=k \pi(k=0, \pm 1, \pm 2, \cdots)$, 所 $\mathrm{W}, x=\frac{1}{k} \quad(k= \pm 1, \pm 2, \cdots)$.
(2) $\sin \frac{\pi}{x}>0$, 则 $2 k \pi<\frac{\pi}{x}<(2 k+1) \pi$ 和
$-(2 k+2) \pi<\frac{\pi}{x}<-(2 k+1) \pi$, 所以

$$
\begin{gathered}
\frac{1}{2 k+1}<x<\frac{1}{2 k} \text { 和 }-\frac{1}{2 k+1}<x<-\frac{1}{2 k+2} \\
\quad(k=0,1,2, \cdots)
\end{gathered}
$$

(3) $\sin \frac{\pi}{x}<0$, 则 $(2 k+1) \pi<\frac{\pi}{x}<(2 k+2) \pi$ 和 $-(2 k$ $+1) \pi<\frac{\pi}{x}<-2 k \pi(k=0,1,2, \cdots)$,
所以,$\frac{1}{2 k+2}<x<\frac{1}{2 k+1}$ 和 $-\frac{1}{2 k}<x<-\frac{1}{2 k+1}(k=0,1$, 2, ․) ,
（в）（1）(x+|x|)(1-x)=0，则 $x \leqslant 0$ 和 $x=1$ 。
（2）因为 $x+|x| \geqslant 0$ ，所以 $1-x>0$ ，即 $x<1$ 。而由 $f(x)>0$, 得 $x+|x|>0$, 即 $x>0$ 。

总之，当 $0<x<1$ 时， $(x+x \mid)(1-x)>0$ 。
(3) $(x+|x|)(1-x)<0$ 。

首先， $x>0$ ，否则 $x+|x|=0$ 。
其次，应有 $1-x<0$ ，所以 $x>1$ ，此即所求之解。
195. 设：
(a) $f(x)=a x+b ;$ (5) $f(x)=x^{2} ;$ （ $) f(x)=a^{x}$.

求 $\varphi(x)=\frac{f(x+h)-f(x)}{h}$.
解 $(\mathrm{a}) \varphi(x)=\frac{a(x+h)+b-(a x+b)}{h}=a ;$

$$
\text { (6) } \varphi(x)=\frac{(x+h)^{2}-x^{2}}{h}=2 x+h
$$

$$
\text { (в) } \varphi(x)=\frac{a^{s+h}-a^{s}}{h}=a^{x} \cdot \frac{a^{h}-1}{h} \text {. }
$$

196. 设：

$$
f(x)=a x^{2}+b x+c,
$$

证明 $\quad f(x+3)-3 f(x+2)+3 f(x+1)-f(x)=0$.
证 $\quad f(x+3)-3 f(x+2)+3 f(x+1)-f(x)$.

$$
=a(x+3)^{2}+b(x+3)+c-3\left[a(x+2)^{2}\right.
$$

$+b(x+2)+c]+3\left[a(x+1)^{2}+b(x+1)+c\right]$
$-\left[a x^{2}+b x+c\right]=a x^{2}+6 a x+9 a+b x+3 b+c$
$-3 a x^{2}-12 a x-12 a-3 b x-6 b-3 c+3 a x^{2}$
$+6 a x+3 a+3 b x+3 b+3 c-a x^{2}-6 x-c$
$=0$ ，

## 于是，

$$
f(x+3)-3 f(x+2)+3 f(x+1)-f(x)=0
$$

197. 若 $f(0)=-2, f(3)=5$, 求线性整函数：

$$
f(x)=a x+b
$$

$f(1)$ 及 $f(2)$ 等于什么（线性补插法）？
解 因为 $f(0)=b=-2$ 及 $f(3)=3 a+b=5$,
所以，

$$
a=\frac{7}{3}, b=-2 .
$$

于是，所求的线性整函数为

$$
f(x)=\frac{7}{3} x-2,
$$

且 $f(1)=\frac{1}{3}, f(2)=\frac{8}{3}$ 。
198. 若 $f(-2)=0, f(0)=1, f(1)=5$. 求二次有理整函数:

$$
f(x)=a x^{2}+b x+c,
$$

$f(-1)$ 及 $f(0.5)$ 等于什么(二次补插法)?
解 因为 $f(-2)=4 a-2 b+c=0$,

$$
f(0)=c=1, f(1)=a+b+c=5,
$$

所以, $a=\frac{7}{6}, b=\frac{17}{6}, c=1$.
于是，所求的二次有理整函数为

$$
f(x)=\frac{7}{6} x^{2}+\frac{17}{6} x+1,
$$

且 $\quad f(-1)=-\frac{2}{3}, f(0.5)=\frac{65}{24}=2 \frac{17}{24}$.
199. 设 $f(-1)=0, f(0)=2, f(1)=-3, f(2)=5$. 求三次有理整函数；

$$
f(x)=a x^{3}+b x^{2}+c x+d .
$$

解 因为 $f(-1)=-a+b-c+d=0$,

$$
\begin{aligned}
& f(0)=d=2 . \\
& f(1)=a+b+c+d=-3 . \\
& f(2)=8 a+4 b+2 c+d=5
\end{aligned}
$$

$$
\text { 所以, } a=\frac{10}{3}, b=-\frac{7}{2}, c=-\frac{29}{6}, d=2 \text {. }
$$

子是，所求的三次有理整函数为

$$
f(x)=\frac{10}{3} x^{3}-\frac{7}{2} x^{2}-\frac{29}{6} x+2
$$

200. 设 $f(0)=15, f(2)=30, f(4)=90$, 求形状为

$$
f(x)=a+b c^{x}
$$

的数。
解 因为 $f(0)=a+b=15$ 。

$$
\begin{aligned}
& f(2)=a+b c^{2}=30 \\
& f(4)=a+b c^{4}=90
\end{aligned}
$$

所以， $a=10, b=5, c=2$ （ -2 不适合）。
于是，所求的函数为

$$
f(x)=10+5 \cdot 2^{x} .
$$

201. 证明：对于线性函数

$$
f(x)=a x+b,
$$

若自变量的诸值 $x=x_{n}(n=1,2, \cdots)$ 组成一等差级数，则对应的函数值 $y_{*}=f\left(x_{n}\right)(n=1,2, \cdots)$ 也组成一等差级数。
证 设叙列 $x_{n}(n=1,2, \cdots)$ 为
$x_{1}, x_{1}+d, x_{1}+2 d, x_{1}+3 d, \cdots$,
$x_{1}+(n-1) d, \cdots$
其中 $d$ 为公差。
于是，

$$
\begin{aligned}
y_{n}-y_{n-1}= & \left(a x_{n}+b\right)-\left(a x_{n-1}+b\right) \\
= & \left\{a\left[x_{1}+(n-1) d\right]+b ; \cdots\right. \\
& \left\{a\left[x_{1}+(n-2) a\right]+b\right\}=a d,
\end{aligned}
$$

由于 $a d$ 为一常数，所以，叙列 $y_{n}=f\left(x_{n}\right)$ 也组成等差级数。
202. 证明：对于指数函数

$$
f(x)=a^{x}(a>0),
$$

若自变数 $x^{2}=x_{n}(n=1,2, \cdots)$ 的值组成一等差级数，则对应的函数值 $y_{n}=f\left(x_{n}\right)(n=1,2, \cdots)$ 组成一等比级数。
证 因为 $x_{n}-x_{n-1}=d$ ，所以

$$
y_{n}: y_{n-1}=a^{x_{n}}: a^{x_{n-1}}=a^{x_{n}-x_{n-1}}=a^{d},
$$

即函数值 $y_{n}=f\left(x_{n}\right)$ 组成一等比级数。
203. 设当 $0<u<1$ 函数 $f(u)$ 有定义，求下列函数的定廹域：
(a) $f(\sin x)^{+} ;(6) f(\ln x) ;(B)^{+} f\left(\frac{[x]}{x}\right)$.

解 (a) 因为 $0<\sin x<1$, 所以,

$$
\begin{aligned}
& 2 k \pi<x<\pi+2 k \pi \quad(k=0, \pm 1, \pm 2, \cdots) \text { 且 } \\
& x \neq \frac{4 k+1}{2} \pi \quad(k=0, \pm 1, \pm 2, \cdots) ;
\end{aligned}
$$

(6) 因为 $0<\ln x<1$, 所以, $1<x<e$ ；
(в) 因为 $0<\frac{[x]}{x}<1$,

所以， $x>1$ 且 $x \neq k(k=2,3,4, \cdots)$.
204. 设：

$$
f(x)=\frac{1}{2}\left(a^{x}+a^{-x}\right)(a>0) .
$$

证明： $f(x+y)+f(x-y)=2 f(x) \cdot f(y)$.
证 $f(x+y)+f(x-y)$
$=\frac{1}{2}\left(a^{x+y}+a^{-x-y}\right)+\frac{1}{2}\left(a^{x-y}+a^{-x+y}\right)$
$=\frac{1}{2}\left(a^{x} \cdot a^{y}+a^{-x} \cdot a^{-y}\right)+\frac{1}{2}\left(a^{x} \cdot a^{-y}+a^{-x} \cdot a^{y}\right)$

$$
\begin{aligned}
& =\frac{1}{2} a^{x}\left(a^{y}+a^{-y}\right)+\frac{1}{2} a^{-x}\left(a^{-y}+a^{y}\right) \\
& =\frac{1}{2}\left(a^{x}+a^{-x}\right)\left(a^{y}+a^{-y}\right) \\
& =2 f(x) f(y),
\end{aligned}
$$

于是,

$$
f(x+y)+f(x-y)=2 f(x) f(y) .
$$

205. 设；

$$
f(x)+f(y)=f(z) .
$$

求出 $z$, 若:
(a) $f(x)=a x ;$
(6) $f(x)=\frac{1}{x}$;
(в) $f(x)=\operatorname{arctg} x(|x|<1) ;(r) f(x)=\lg \frac{1+x}{1-x}$.

解 (a) $f(x)+f(y)=a x+a y=a(x+y)$ ，

$$
f(x)=a z,
$$

由 $f(x)+f(y)=f(z)$ 得 $z=x+y$.
（5）由 $\frac{1}{x}+\frac{1}{y}=\frac{1}{z}$ 得 $z=\frac{x y}{x+y}$ 。
(в) 由 $\operatorname{arctg} x+\operatorname{arctg} y=\operatorname{arctg} x$ 得

$$
\operatorname{arctg} \frac{x+y}{1-x y}=\operatorname{arctg} z
$$

所以， $z=\frac{x+y}{1-x y}$;
(г) 由 $\lg \frac{1+x}{1-x}+\lg \frac{1+y}{1-y}=\lg \frac{1+z}{1-x}$ 得

$$
\frac{(1+x)(1+y)}{(1-x)(1-y)}=\frac{1+z}{1-z},
$$

所以， $z=\frac{x+y}{1+x y}$.
求 $\varphi[\varphi(x)], \psi[\phi(x)], \varphi[\phi(x)]$ 及 $\psi[\varphi(x)]$, 设：
206. $\varphi(x)=x^{2}$ 及 $\psi(x)=2^{x}$.

解 $\varphi[\varphi(x)]=\left(x^{2}\right)^{2}=x^{4} ; \varphi[\phi(x)]=\left(2^{*}\right)^{2}=2^{2 x} ;$ $\psi[\psi(x)]=2^{\left(z^{2}\right)} ; \psi[\varphi(x)]=2^{\left(x^{2}\right)}$.
207. $\varphi(x)=\operatorname{sgn} x$ 及 $\psi(x)=\frac{1}{x}$ 。

解 $\varphi[\varphi(x)]=\operatorname{sgn}(\operatorname{sgn} x)=\operatorname{sgn} x$;

$$
\begin{aligned}
& \phi[\psi(x)]=\frac{1}{\frac{1}{x}}=x(x \neq 0) ; \\
& \phi[\psi(x)]=\operatorname{sgn}\left(\frac{1}{x}\right)=\operatorname{sgn} x \quad(x \neq 0) ; \\
& \phi[\phi(x)]=\frac{1}{\operatorname{sgn} x}=\operatorname{sgn} x \quad(x \neq 0) .
\end{aligned}
$$

208. $\varphi(x)=\left\{\begin{array}{l}0, \text { 当 } x \leqslant 0, \\ x, \text { 当 } x>0 .\end{array}\right.$ 及 $\psi(x)=\left\{\begin{array}{l}0, \text { 当 } x \leqslant 0, \\ -x^{2}, \text { 当 } x>0 .\end{array}\right.$

解 $\varphi[\phi(x)]=\varphi(x) ; \psi[\phi(x)]=0$ （因为 $-x^{2} \leqslant 0$ ；

$$
\varphi[\phi(x)]=0 ; \psi[\varphi(x)]=\psi(x) .
$$

209. 设：

$$
f(x)=\frac{1}{1-x},
$$

求 $f[f(x)], f\{f[f(x)]\}$.
解 $f[f(x)]=\frac{1}{1-\frac{1}{1-x}}=1-\frac{1}{x}$ ；

$$
f\{f[f(x)]\}=\frac{1}{1-\left(1-\frac{1}{x}\right)}=x .
$$

210. 设：

$$
f_{n}(x)=\underbrace{f\{f[\cdots f(x)]\}}_{n \hbar} .
$$

若

$$
f(x)=\frac{x}{\sqrt{1+x^{2}}} \text {, 求 } f_{n}(x) \text {. }
$$

解 当 $n=2$ 时, $f_{2}(x)=\frac{x}{\sqrt{1+2 x^{2}}}$.
设对于 $n=k$ 时, 有

$$
f_{k}(x)=\frac{x}{\sqrt{1+k x^{2}}},
$$

则对于 $n=k+1$ 时, 有

$$
f_{k+1}(x)=\frac{\frac{x}{\sqrt{1+k x^{2}}}}{\sqrt{1+\frac{x^{2}}{1+k x^{2}}}}=\frac{x}{\sqrt{1+(k+1) x^{2}}} .
$$

从而由数学旧纳法知, 对于任何自然数 $n$, 有

$$
f_{n}(x)=\frac{x}{\sqrt{1+n x^{2}}} .
$$

211. 设：

$$
f(x+1)=x^{2}-3 x+2,
$$

求 $f(x)$.
解 因为 $f(x+1)=(x+1)^{2}-5(x+1)+6$, 于是，

$$
f(x)=x^{2}-5 x+6 .
$$

212. 设：

$$
f\left(x+\frac{1}{x}\right)=x^{2}+\frac{1}{x^{2}},
$$

求 $f(x)$.
解 因为 $f\left(x+\frac{1}{x}\right)=\left(x+\frac{1}{x}\right)^{2}-2$, 于是,

$$
f(x)=x^{2}-2
$$

213. 设：

$$
f\left(\frac{1}{x}\right)=x+\sqrt{1+x^{2}} \quad(x>0),
$$

求 $f(x)$.
解 因为 $f\left(\frac{1}{x}\right)=\frac{1+\sqrt{1+\left(\frac{1}{x}\right)^{2}}}{\frac{1}{x}}$, 于是,

$$
f(x)=\frac{1+\sqrt{1+x^{2}}}{x}
$$

证明下列各函数在所示间隔内是单调增函数：
214. $f(x)=x_{2} \quad(0 \leqslant x<+\infty)$.

证 当 $x_{2}>x_{1} \geqslant 0$ 时,

$$
\begin{aligned}
& f\left(x_{2}\right)-f\left(x_{1}\right)=x_{2}^{2}-x_{1}^{2} \\
& =\left(x_{2}-x_{1}\right)\left(x_{2}+x_{2}\right)>0,
\end{aligned}
$$

于是 $f(x)=x^{2}$ 在 $0 \leqslant x<+\infty$ 内是单调增函数。
215. $f(x)=\sin x\left(-\frac{\pi}{2} \leqslant x \leqslant \frac{\pi}{2}\right)$.

证 当 $-\frac{\pi}{2}<x_{1}<x_{2}<\frac{\pi}{2}$ 时,
因为 $-\frac{\pi}{2}<\frac{x_{1}+x_{2}}{2}<\frac{\pi}{2}$ 及 $0<\frac{x_{2}-x_{1}}{2}<\frac{\pi}{2}$,
所以， $\cos \frac{x_{1}+x_{2}}{2}>0$ 及 $\sin \frac{x_{2}-x_{1}}{2}>0$ 。
又因 $f\left(x_{2}\right)-f\left(x_{1}\right)=\sin x_{2}-\sin x_{1}$

$$
=2 \cos \frac{x_{2}+x_{1}}{2} \sin \frac{x_{2}-x_{1}}{2}>0,
$$

所以， $f(x)=\sin x$ 在 $-\frac{\pi}{2} \leqslant x \leqslant \frac{\pi}{2}$ 内是单调增函数.
216. $f(x)=\operatorname{tg} x\left(-\frac{\pi}{2}<x<\frac{\pi}{2}\right)$.

证 $\quad f\left(x_{2}\right)-f\left(x_{1}\right)=\operatorname{tg} x_{2}-\operatorname{tg} x_{1}=\frac{\sin x_{2}}{\cos x_{2}}-\frac{\sin x_{1}}{\cos x_{1}}$

$$
\begin{aligned}
& =\frac{\sin x_{2} \cos x}{\cos x_{1} \cos x_{2}} \cos x_{2} \sin x_{1} \\
& =\frac{\sin \left(x_{2}-x_{1}\right)}{\cos x_{1} \cdot \cos x_{2}} \\
& \text { 当 }-\frac{\pi}{2}<x_{1}<x_{2}<\frac{\pi}{2} \text { 时, } \cos x_{1}>0, \cos x_{2}>0 \text { 及 }
\end{aligned}
$$

$\sin \left(x_{2}-x_{1}\right)>0$ ，从而可知

$$
f\left(x_{2}\right)-f\left(x_{1}\right)>0,
$$

所以, $f(x)=\operatorname{tg} x$ 在 $-\frac{\pi}{2}<x<\frac{\pi}{2}$ 内是单调增函数. 217. $f(x)=2 x+\sin x(-\infty<x<+\infty)$.

证 $\quad f\left(x_{2}\right)-f\left(x_{1}\right)=2\left(x_{2}-x_{1}\right)+\sin x_{2}-\sin x_{1}$,
因为 $\left|\sin x_{2}-\sin x_{1}\right|$

$$
\begin{aligned}
& =2\left|\cos \frac{x_{1}+x_{2}}{2}\right|\left|\sin \frac{x_{2}-x_{1}}{2}\right| \\
& \leqslant 2 \cdot\left|\sin \frac{x_{2}-x_{1}}{1}\right| \leqslant 2 \cdot\left|\frac{x_{2}-x_{1}}{2}\right|=\left|x_{2}-x_{1}\right|
\end{aligned}
$$

所以当 $x_{2}<x_{1}$ 时，有

$$
-\left(x_{2}-x_{1}\right) \leqslant \sin x_{2}-\sin x_{1} \leqslant x_{2}-x_{1}
$$

从而

$$
\begin{aligned}
& 2\left(x_{2}-x_{1}\right)+\sin x_{2}-\sin x_{1}>2\left(x_{2}-x_{1}\right) \\
& -\left(x_{2}-x_{1}\right)=x_{2}-x_{1}>0
\end{aligned}
$$

即 $f\left(x_{2}\right)-f\left(x_{1}\right)>0$, 于是, $f(x)=2 x+\sin x$ 在 $-\infty$ $<x<+\infty$ 内是单调增函数。
证明下列各函数在所示间隔内是单调煘函数：
218. $f(x)=x^{2} \quad(-\infty<x \leqslant 0)$.

证 $\quad f\left(x_{2}\right)-f\left(x_{1}\right)=\left(x_{2}-x_{1}\right)\left(x_{2}+x_{1}\right)<0$

$$
\left(x_{1}<x_{2}<0\right),
$$

于是, $f(x)=x^{2}$ 在 $-\infty<x \leqslant 0$ 内是单调减函数.
219. $f(x)=\cos x(0 \leqslant x \leqslant \pi)$.

证 $\quad f\left(x_{2}\right)-f\left(x_{1}\right)=\cos x_{2}-\cos x_{1}$

$$
=-2 \sin \frac{x_{2}+x_{1}}{2} \sin \frac{x_{2}-x_{1}}{2},
$$

当 $0<x_{1}<x_{2}<\pi$ 时,

$$
0<\frac{x_{1}+x_{2}}{2}<\pi \text { 及 } 0<\frac{x_{2}-x_{1}}{2}<\frac{\pi}{2} \text {, }
$$

于是, $\sin \frac{x_{1}+x_{2}}{2}>0, \sin \frac{x_{2}-x_{1}}{2}>0$, 从而

$$
f\left(x_{2}\right)-f\left(x_{1}\right)<0 .
$$

即 $f(x)=\cos x$ 在 $0 \leqslant x \leqslant \pi$ 内是单调减函数。
220. $f(x)=\operatorname{ctg} x \quad(0<x<\pi)$.

证 $f\left(x_{2}\right)-f\left(x_{1}\right)=\frac{\cos x_{2}}{\sin x_{2}}-\frac{\cos x_{1}}{\sin x_{1}}$

$$
\begin{gathered}
=\frac{\cos x_{2} \sin x_{1}-\cos x_{1} \sin x_{2}}{\sin x_{1} \sin x_{2}}=\frac{\sin \left(x_{1}-x_{2}\right)}{\sin x_{1} \cdot \sin x_{2}}<0 \\
\text { (当 } 0<x_{1}<x_{2}<\pi \text { 时), }
\end{gathered}
$$

于是， $f(x)=\operatorname{ctg} x$ 在 $0<x<\pi$ 内是单调减函数。

## 221. 研究下列函数的单调性：

(a) $f(x)=a x+b ;$
(6) $f(x)=a x^{2}+b x+c ;$
( B ) $f(x)=x^{3} ;$
(r) $f(x)=\frac{a x+b}{c x+d}$;
(д) $f(x)=a^{x}(a>0)$.

解 (a) 对于 $x_{1}<x_{2}$ ，有 $f\left(x_{2}\right)-f\left(x_{1}\right)=a\left(x_{2}-x_{1}\right)$ 。当 $a>0$ 时，它大于零；当 $a<0$ 时，它小于零。所以，当 $a$ $>0$ 时, $f(x)$ 是增函数; 当 $a<0$ 时, $f(x)$ 是㺂函数。
(6) $f(x)=a\left(x+\frac{b}{2 a}\right)^{2}+\frac{4 a c-b^{2}}{4 a}$.
（1）当 $a>0$ 时，图形呈凹形，顶点在 $\left(-\frac{b}{2 a}, \frac{b^{2}-4 a c}{4 a}\right)$ ，于是, 在 $-\infty<x<-\frac{b}{2 a}$ 内, 函数单调下降, 在 $-\frac{b}{2 a}<$ $x<+\infty$ ，函数单调上升。
(2) 当 $a<0$ 时, 图形呈凸状.于是, 在 $-\infty<x<-\frac{b}{2 a}$内增加，而在 $-\frac{b}{2 a}<x<+\infty$ 内减小。
(घ) $f\left(x_{2}\right)-f\left(x_{1}\right)=x_{2}^{3}-x_{1}^{3}$
$+\left(x_{2}-x_{1}\right)\left(x_{2}^{2}+x_{1} x_{2}+x_{1}^{2}\right)>0\left(x_{2}>x_{1}\right)$, 于是 $f(x)=x^{3}$ 在 $-\infty<x<+\infty$ 内单调增加.
(r) $f(x)=\frac{a x+b}{c x+d}=\frac{a}{c}+\frac{b-a \frac{d}{c}}{c x+d}$ ，其中 $c \neq 0$ ，若 $c=0$ ，则同（a）一样讨论。下面不妨就 $c>0$ 讨论其增减性。
（1）当 $b>a \frac{d}{c}$ 时，若 $x$ 值单调增加，则 $f(x)$ 值瑊小.所以， $f(x)$ 在 $\left(-\infty,-\frac{d}{c}\right)$ 及 $\left(-\frac{d}{c},+\infty\right)$ 内减小.
（2）当 $b<\frac{a d}{c}$ 时,若 $x$ 值单调增加，则 $f(x)$ 值也增加。所以， $f(x)$ 在 $\left(-\infty,-\frac{d}{c}\right)$ 及 $\left(-\frac{d}{c},+\infty\right)$ 内增加.
（） $f\left(x_{2}\right)-f\left(x_{1}\right)=a_{2}^{x}-a_{1}^{x}$. 若 $x_{2}>x_{1}$ ，则
当 $0<a<1$ 时, $f\left(x_{2}\right)-f\left(x_{1}\right)<0$, 此时 $f(x)$ 在 $-\infty<x<+\infty$ 内减小.

当 $a>1$ 时, $f\left(x_{2}\right)-f\left(x_{1}\right)>0$, 此时, $f(x)$ 在 $-\infty$
$<x<+\infty$ 内增加。

## 222. 不等式能否逐项取对数？

解 不一定可以，当底大于 1 时才可以。因为对于对数函数当底大于 1 时为单调增函数。若底介于 0 与 1 之间，则为单调㺂函数，所以，此时就不能逐项取对数。
223. 设

$$
\begin{aligned}
& \varphi(x), \phi(x) \text { 及 } f(x) \text { 为单调增函数. 证明: 若 } \\
& \varphi(x) \leqslant f(x) \leqslant \psi(x),
\end{aligned}
$$

则

$$
\varphi[\varphi(x)] \leqslant f[f(x)] \leqslant \phi[\psi(x)] .
$$

证 设 $x_{0}$ 为三个函数公共域内的任一点，则

$$
\varphi\left(x_{0}\right) \leqslant f\left(x_{0}\right) \leqslant \varphi\left(x_{0}\right) .
$$

由（1）以及函数 $f(x)$ 的单调增性知

$$
\begin{aligned}
& f\left[\varphi\left(x_{0}\right)\right] \leqslant f\left[f\left(x_{0}\right)\right], \\
& \varphi\left[\varphi\left(x_{0}\right)\right] \leqslant f\left[\varphi\left(x_{0}\right)\right] ;
\end{aligned}
$$

从而

$$
\varphi\left[\varphi\left(x_{0}\right)\right] \leqslant f\left[f\left(x_{0}\right)\right] .
$$

同理，可证

$$
f\left[f\left(x_{0}\right)\right] \leqslant \phi\left[\phi\left(x_{0}\right)\right],
$$

由 $x_{0}$ 的任意性，于是（2）式得证。
求反函数 $x=\varphi(y)$ 和它的存在域, 若：
224. $y=2 x+3(-\infty<x<+\infty)$.

解 $x=\frac{y-3}{2},-\infty<y<+\infty$.
225. $y=x^{2}$. (a) $(-\infty<x \leqslant 0)$ （6） $(0 \leqslant x<+\infty)$.

湳 (a) $x=-\sqrt{y}, 0 \leqslant y<+\infty$ ；
(6) $x=\sqrt{y}, \quad 0 \leqslant y<+\infty$.
226. $y=\frac{1-x}{1+x}(x \neq-1)$.

解 由于 $y+x y=1-x$ ，解出 $x$ 得反函数

$$
x=\frac{1-y}{1+y}, \quad y \neq-1 .
$$

227. $y=\sqrt{1-x^{2}}$. (a) $(-1 \leqslant x \leqslant 0) ;(6)(0 \leqslant x \leqslant 1)$.

算 (a) $x=-\sqrt{1-y^{2}}, 0 \leqslant y \leqslant 1$;

$$
\text { ( } 6) x=\sqrt{1-y^{2}}, 0 \leqslant y \leqslant 1 .
$$

228. $y=\operatorname{sh} x$, 式中 $\operatorname{sh} x=\frac{1}{2}\left(e^{x}-e^{-x}\right)(-\infty<x<+\infty)$.

解 由于 $2 y=e^{x}-e^{-x}$, 即

$$
\left(e^{x}\right)^{2}-2 y e^{x}-1=0,
$$

解出 $e^{x}$ 两端再取对数，即得

$$
x=\operatorname{arsh} y=\ln \left(y+\sqrt{1+y^{2}}\right),-\infty<y<+\infty .
$$

229. $y=\mathrm{th} x$, 式中 th $x=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}(-\infty<x<+\infty)$.

解 由于 $y=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}=\frac{\left(e^{x}\right)^{2}-1}{\left(e^{x}\right)^{2}+1}$, 即

$$
e^{2 x}=\frac{1+y}{1-y},
$$

两端取对数，并注意到 $\frac{1+y}{1-y}>0$ 即 $-1<y<1$ ，于是

$$
x=\operatorname{arth} y=\frac{1}{2} \ln \frac{1+y}{1-y},-1<y<1 .
$$

230. $y=\left\{\begin{array}{l}x, \text { 若 }-\infty<x<1 ; \\ x^{2} \text {, 若 } 1 \leqslant x \leqslant 4 ; \\ 2^{x}, \text { 若 } 4<x<+\infty .\end{array}\right.$

解

$$
x=\left\{\begin{array}{l}
y, \text { 若 }-\infty<y<1 ; \\
\sqrt{y}, \text { 若 } 1 \leqslant y \leqslant 16 ; \\
\log _{2} y, \text { 若 } 16<y<+\infty .
\end{array}\right.
$$

231. 函数 $f(x)$ 定义于对称区间 $(-l, l)$ 中, 且若

$$
f(-x)=f(x),
$$

则称 $f(x)$ 为偶函数, 若

$$
f(-x)=-f(x),
$$

则称 $f(x)$ 为奇函数。
确定下列各已知函数中哪些是偶函数，呀些是奇函数:
(a) $f(x)=3 x-x^{2}$;
(б) $f(x)=\sqrt[3]{(1-x)^{2}}+\sqrt[3]{(1+x)^{2}}$;
(в) $f(x)=a^{x}+a^{\cdots x}(a>0) ;(\mathrm{r}) f(x)=\ln \frac{1-x}{1+x} ;$
(л) $f(x)=\ln \left(x+\sqrt{1+x^{2}}\right)$.

解 (a) $f(-x)=-3 x+x^{3}=-f(x)$, 故为奇函数.
(6) $f(-x)=\sqrt[3]{(1+x)^{2}}+\sqrt[3]{(1-x)^{2}}=f(x)$,

故为偶函数.

$$
\begin{aligned}
& \text { (в) } f(-x)=a^{-x}+a^{x}=f(x) \text { ，故为偶函数。 } \\
& (\mathrm{r}) f(-x)=\ln \frac{1+x}{1-x}=-\ln \frac{1-x}{1+x}=-f(x),
\end{aligned}
$$

故为奇函数。

$$
\text { (Д) } \begin{aligned}
f(-x) & =\ln \left(-x+\sqrt{1+\dot{x}^{2}}\right) \\
& =\ln \frac{1}{x+\sqrt{1+x^{2}}} \\
& =-\ln \left(x+\sqrt{1+x_{2}}\right)=-f(x),
\end{aligned}
$$

故为奇函数。
232. 证明定义于对称区间 $(-l, l)$ 内的任何函数 $f(x)$ 可以表示为偶函数与奇函数之和的形式。
证 因为

$$
f(x)=\frac{f(x)+f(-x)}{2}+\frac{f(x)-f(-x)}{2},
$$

而 $\frac{f(x)+f(-x)}{2}$ 为偶函数， $\frac{f(x)-f(-x)}{2}$ 为奇函数，于是本题得证。
233. 若存在有数 $T>0$ (函数的周期——在广义的意义上)使对于一切被考虑的自变量 $x$ 满足等式

$$
f(x+n T)=f(x)(n=0, \pm 1, \pm 2, \cdots)
$$

则函数 $f(x)$ 称为周期函数.
说明下列各已知函数中哪些是周期函数，并求它们的最小周期. 设：

$$
\begin{aligned}
& \text { (а) } f(x)=A \cos \lambda x+B \sin \lambda x \\
& \text { (б) } f(x)=\sin x+\frac{1}{2} \sin 2 x+\frac{1}{3} \sin 3 x \\
& \text { (в) } f(x)=2 \operatorname{tg} \frac{x}{2}-3 \operatorname{tg} \frac{x}{3} ; \text { (г) } f(x)=\sin ^{2} x \\
& \text { (а) } f(x)=\sin x^{2} ; \text { (е) } f(x)=\sqrt{\operatorname{tg} x} \\
& \text { (к) } f(x)=\operatorname{tg} \sqrt{x} ; \text { (а) } f(x)=\sin x+\sin (x
\end{aligned}
$$

解 对于（a），由千

$$
\begin{aligned}
f\left(x+\frac{2 \pi}{\lambda}\right) & =A \cos \lambda\left(x+\frac{2 \pi}{\lambda}\right)+B \sin \lambda\left(x+\frac{2 \pi}{\lambda}\right) \\
& =A \cos \lambda x+B \sin \lambda x=f(x)
\end{aligned}
$$

故为周期函数，最小周期为 $T=\frac{2 \pi}{\lambda}(\lambda>0)$ 。同理可证： (a)、(B)、(r) 和（e）也是周期面数，最小周期分别为 $2 \pi$ 、 $6 \pi 、 \pi$ 和 $\pi$ 。对于 $(A)$ ，若周期为 $a$ ，即 $\sin (x+a)^{2}=\sin x^{2}$ 。令 $x=0$ 即得 $a= \pm \sqrt{m \pi}$ ( $m$ 为某正整数), 代入, 又令 $x$
$=\sqrt{2 m \pi}$ ，易得 $\sin \left(2 \sqrt{2} m \pi=0\right.$ 。但 $2 \sqrt{2} m^{\prime}$ 显然不是整数，得到矛盾。于是， $\sin x^{2}$ 不是周期函数。同理，（庶和 （3）也不是周期函数。
234. 证明：对于迪里黑里函数

$$
\chi(x)=\left\{\begin{array}{l}
1, \text { 若 } x \text { 为有理数, } \\
0, \text { 若 } x \text { 为无理数. }
\end{array}\right.
$$

任何有理数皆为其周期。
证 设 $l$ 为任一有理数，则当 $x$ 为有理数时， $x+l$ 也为有理数. 若 $x$ 为无理数, 则 $x+l$ 也为无理数, 所以

$$
x(x+l)=\left\{\begin{array}{l}
1, \text { 若 } x \text { 为有理数, } \\
0, \text { 若 } x \text { 为无理数. }
\end{array}\right.
$$

即 $\chi(x+l)=\chi(x), l$ 为周期.
235. 证明定义于公共的集合上且周期是可公度的二个周期函数之和及其乘积也是周期函数。
证 投 $f_{1}(x)$ 及 $f_{2}(x)$ 为定义在集合 $A$ 上的周期函数， $T_{1}$ 及 $T_{2}$ 分别为它们的周期。又设 $T$ 为 $T_{1}$ 及 $T_{2}$ 的公约数, 即

$$
T_{1}=T k_{1}, T_{2}=T k_{2},
$$

其中 $k_{1}, k_{2}$ 为正整数. 于是

$$
f_{1}\left(x+k_{2} T_{1}\right)=f_{1}(x), f_{2}\left(x+k_{1} T_{2}\right)=f_{2}(x)
$$

设

$$
F_{1}(x)=f_{1}(x)+f_{2}(x), F_{2}(x)=f_{1}(x) f_{2}(x),
$$

可以证明： $k_{1} k_{3} T$ 分别题 $F_{1}(x)$ 和 $F_{2}(x)$ 的周期。事实上，我们有

$$
\begin{aligned}
& F_{1}\left(x+k_{1} k_{2} T\right)=f_{1}\left(x+k_{1} k_{2} T\right) \\
& +f_{2}\left(x+k_{1} k_{2} T\right)
\end{aligned}
$$

$$
\begin{aligned}
& =f_{1}(x)+f_{2}(x)=F_{1}(x) \\
& \quad F_{2}\left(x+k_{1} k_{2} T\right)=f_{1}\left(x+k_{1} k_{2} T\right) f_{2}\left(x+k_{1} k_{2} T\right) \\
& =f_{1}(x) f_{2}(x)=F_{2}(x)
\end{aligned}
$$

从而本题得证。
236. 证明：若对于函数 $f(x)(-\infty<x<+\infty)$ 有等式

$$
f(x+T)=k f(x)
$$

（式中 $k$ 和 $T$ 为正的常数）成立，则

$$
f(x)=a^{x} \varphi(x)
$$

（式中 $a$ 为大于零的常数，而 $\varphi(x)$ 为以 $T$ 为周期的函数）。
证 由假定 $k>0, T^{\prime}>0$ ，令 $a=k^{\frac{1}{r}}>0$ ，则 $a^{T}=k$ 。于是有

$$
f(x+T)=a^{T} f(x)
$$

今定义函数 $\varphi(x)$ 如下：

$$
\varphi(x)=a^{-x} f(x) .
$$

易知 $\varphi(x)$ 是周期为 $T$ 的函数。事实上，

$$
\begin{aligned}
\varphi(x+T) & =a^{-(x+T)} f(x+T)=a^{-x} a^{-T} a^{T} f(x) \\
=a^{-x} f(x) & =\varphi(x) .
\end{aligned}
$$

于是

$$
f(x)=a^{x} \varphi(x),
$$

其中 $\varphi(x)$ 是周期为 $T$ 的函数。证毕。

## §4. 函数的圈形表示法

$1^{\circ}$ 要作函数 $y=f(x)$ 的图形可用下法来进行：(1) 确定函数的存在域 $X=\{x\}$ ；（2）从 $X$ 中选出充分密集的自变数值 $x_{1}, x_{2}$ ，
$\cdots, x_{n}$ 并作出函数

$$
y_{i}=f\left(x_{i}\right) \quad(i=1,2, \cdots, n)
$$

的对应数值贞；（3）在坐标平面 $O x y$ 上荟出一系列的点 $M_{i}\left(x_{i}\right.$ 。 $\left.y_{i}\right)(i=1,2, \cdots, n$ 并用线把它们连接起来，此连线的性质就是可认为是许多中间点的位是。
$2^{\circ}$ 为了得到函数的正确图形，应当研究这个函数的一般性质。

首先必彺：（1）解方程式 $f(x)=0$ ，求出函数固形与 $O x$ 轴的交点（函数值为零的点）；（2）确定使函数为正或为负时自变数的变域；（3）尽可能地说明画数单调（增或醎）的区间（4）研究当自变数无限趋近于函数存在城的境界点时函数的情况。

这一节里要假定读者已经知道最简单的初等函数的性质，如矮函数、指数函数、三角函数等。

利用这些性质，不用作大量的计基工作，立期可以画出许多函数的略固，其他的图形有时就是这些最筒单困形的组合（和或来积等等）。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-135.jpg?height=666&width=732&top_left_y=1637&top_left_x=199)

图1.13
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-135.jpg?height=569&width=760&top_left_y=1737&top_left_x=1002)

国1.14
237. 作出线性齐次函数

$$
y=a x
$$

当 $a=0, \frac{1}{2}, 1,2,-1$ 时的图形.
解 如图 1.13 所示.
238. 作出线性函数

$$
y=x+b
$$

当 $b=0,1,2,-1$ 时的
图形。
星 如图1 - 14 所示。
239. 作出线性函数的图形：
(a) $y=2 x+3$;
(б) $y=2-0.1 x ;$ (в) $y$
$=-\frac{x}{2}-1$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-136.jpg?height=621&width=741&top_left_y=592&top_left_x=1023)

困 1.15

解 如图 1.15 所示。
240. 铁的线性脂胀系数 $a=$
$1.2 \times 10^{-6}$ 。在适当的
尺度下作出函数

$$
\begin{aligned}
& l=f(T) \\
& \left(-40^{\circ} \leqslant T\right. \\
& \left.\leqslant 100^{\circ}\right)
\end{aligned}
$$

的图形，其中 $T$ 表温度
（以度计） $l$ 表当温度为
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-136.jpg?height=526&width=752&top_left_y=1416&top_left_x=1046)

国1.16
$T$ 时铁棒的长。设当 $T=0^{\circ}$ 时， $l=100$ 厘米。
解 铁棒的长与温度的关系为

$$
t=l_{0}(1+\alpha T)
$$

当 $T=0$ 时， $l=100$ ，代入上式得 $l_{0}=100$.
于是, $l=100\left(1+1.2 \times 10^{-6} T\right)$,

如图1.16所示（两轴单位不同）。
241. "质点在数轴上运动, 第一质点在时间 $t=0$ 的时刻在原点左方 20 米处, 其速度为 $v_{1}=10$ 米/秒; 第二质点当 $t=$ 0 时在原点 $O$ 之右方 30 米处，其速度为 $v_{2}=-20$ 米/秒；作出此二点运动方程的图形并求它们相週的时刻和位置。
解 二质点运动的位移 $s$ 与时间 $t$ 的关系分别为

$$
\begin{aligned}
& s=10 t-20 \\
& s=-20 t+30
\end{aligned}
$$

如图 1.17 所示. 解上述方程, 得

$$
t=1 \frac{2}{3} \text { (秒), } s=-3 \frac{1}{3}(\text { 米), }
$$

即在运动开始后 $1 \frac{2}{3}$ 秒，在 $O t$ 轴之下方 $3 \frac{1}{3}$ 米处相用，如图中 $P$ 点所示。
242. 作出二次有理整函数的图形（拋物线）：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-137.jpg?height=721&width=432&top_left_y=1627&top_left_x=172)
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-137.jpg?height=581&width=709&top_left_y=1694&top_left_x=956)

图 1.18

$$
\begin{aligned}
& \text { （a） } y=a x^{2}, \text { 当 } a=1, \frac{1}{2}, 2,-1 ; \\
& \text { （6） } y=\left(x-x_{0}\right)^{2} \text { ，当 } x_{0}=0,1,2,-1 ;
\end{aligned}
$$

$$
\text { (B) }=x^{2}+c \text {, 当 } c=0,1,2,-1 \text {. }
$$

醉 (a) 如图1.18所示。
( $\sigma$ ）如图1.19所示。
(B) 如图 1.20 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-138.jpg?height=612&width=937&top_left_y=711&top_left_x=685)

图 1.19
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-138.jpg?height=755&width=766&top_left_y=1393&top_left_x=722)

图 1.20
243. 把 一次三项式

$$
y=a x^{2}+b x+c
$$

化为下面的形状

$$
y=y_{0}+a\left(x-x_{0}\right)^{2},
$$

作出它的图形，研究例子：
（a） $y=8 x-2 x^{2} ;$ （6） $y=x^{2}+3 x+2$ ；
(в) $y=-x^{2}+2 x-1 ; \quad$ (г) $y=\frac{1}{2} x^{2}+x+1$.

界 利用配方法得

$$
y=a\left|x+\frac{b}{2 a}\right|^{2}+\frac{4 a c-b^{2}}{4 a}=y_{0}+a\left(x-x_{0}\right)^{2},
$$

其中

$$
x_{1}=-\frac{b}{2 a}, \quad y_{0}=\frac{4 a c-b^{2}}{4 a},
$$

如图 1.21 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-139.jpg?height=578&width=778&top_left_y=1190&top_left_x=288)
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-139.jpg?height=615&width=643&top_left_y=1189&top_left_x=1112)

图 1.21
图 1.22
(a) $y=8 x-2 x^{2}=8-2(x-2)^{2}$,

$$
x_{0}=2, \quad y_{0}=8, \quad a=-2
$$

如图 1.22 所示, 顶点 $A(2,8)$.

$$
\begin{aligned}
\text { (б) } y & =x^{2}-3 x+2 \\
& =\left(x-\frac{3}{2}\right)^{2}-\frac{1}{4}, \\
x_{0}= & \frac{3}{2}, y_{0}=-\frac{1}{4}, a=1,
\end{aligned}
$$

如图 1.23 所示. 顶点 $B\left(\frac{3}{2}-\frac{1}{4}\right)$.

$$
\begin{gathered}
(a) y=-x^{2}+2 x-1=-(x-1)^{2}, \\
x_{0}=1, \quad y_{0}=0, \quad a=-1,
\end{gathered}
$$

如图 1. 24 所示. 頂点 $C(1,0)$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-140.jpg?height=706&width=694&top_left_y=795&top_left_x=284)
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-140.jpg?height=589&width=504&top_left_y=908&top_left_x=1230)

图1.23
囯1.24

$$
\begin{gathered}
(\mathrm{r}) y=\frac{1}{2} x^{2}+x+1=\frac{1}{2}(x+1)^{2}+\frac{1}{2}, \\
x_{0}=-1, \quad y_{0}=\frac{1}{2}, \quad a=\frac{1}{2},
\end{gathered}
$$

如图 1.25 所示. 顶点 $D\left(-1, \frac{1}{2}\right)$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-140.jpg?height=460&width=770&top_left_y=2003&top_left_x=603)

图 1.25
244. 质点以初速度 $v_{0}=600$ 米 $/$ 每秒沿与水平面成角 $\alpha=45^{\circ}$的方向射出。作出运动轨道的图形，并求最大的开高及飞行的射程（假定 $\mathrm{g} \approx 10$ 米/秒 ${ }^{2}$ ，空气的阻力不计）。
解 运动轨道方程为

$$
\begin{gathered}
y=x \operatorname{tg} \alpha-\frac{g x^{2}}{2 v_{0}^{2} \cos ^{2} \alpha}, \\
\text { 以 } v_{9}=600, g=10, \alpha=45^{\circ} \text { 代入得 } \\
y=x-\frac{x^{2}}{36000},
\end{gathered}
$$

即

$$
y=-\frac{1}{36000}(x-18000)^{2}+9000 .
$$

当 $x=18000$ 时， $y$ 值最大，最大升高为 9000 米；
当 $x=36000$ 时, $y=0$, 即飞行射侱为 36000 米. 如图1.26 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-141.jpg?height=461&width=829&top_left_y=1663&top_left_x=656)

图 1.26
作出高于二次的有理整函数的图形：
245. $y=x^{3}+1$.

解 如图 1.27 所示.
246. $y=\left(1-x^{2}\right)(2+x)$.

解 当 $x= \pm 1,-2$ 时， $y=0$ ；
当 $x<-2,-1<x<1$ 时, $y>0$ ；
当 $-2<x<-1$ 及 $x>1$ 时， $y<0$ 。
当 $x<-2$ 及 $x>1$ 时.曲线下降；当 $-1<x<1$时，曲线由上升到下降；当 $-2<x<-1$ 时，曲线由下降到上升. 如图1.28所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-142.jpg?height=598&width=663&top_left_y=866&top_left_x=248)

图1.27
247. $y=x^{2}-x^{4}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-142.jpg?height=678&width=907&top_left_y=843&top_left_x=900)

图1.28

神 $y=x^{2}(1-x)(1+x)=\frac{1}{4}-\left(x^{2}-\frac{1}{2}\right)^{2}$.
图形关于 $O y$ 轴对称，与两坐标轴的交点为

$$
(-1,0), \quad(1,0), \quad(0,0),
$$

且在 $(0,0)$ 点与 $O x$ 轴相切.
当 $x= \pm \frac{1}{\sqrt{2}}$ 时, $y=\frac{1}{4}$, 此时 $A\left(\frac{1}{\sqrt{2}}, \frac{1}{4}\right)$ 及 $B\left(-\frac{1}{\sqrt{2}}, \frac{1}{4}\right)$ 均为图形上的最高点.

当 $0<x<\frac{1}{\sqrt{2}}$ 时,曲线上开;
当 $\frac{1}{\sqrt{2}}<x<+\infty$ 时，曲线下降。如图1.29所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-143.jpg?height=452&width=821&top_left_y=454&top_left_x=623)

图1.29
248. $y=x(a-x)^{2}(a+x)^{3}$
$(a>0)$.
解 当 $x=0, a,-a$ 时, $y=0 .(-a, 0)$ 及 $(a, 0)$ 为切点.

当 $x>0$ 及 $x<-a$ 时, $y>0$;
当 $-a<x<0$ 时, $y<0$. 如图 1.30 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-143.jpg?height=486&width=926&top_left_y=1639&top_left_x=585)

图1.30
作出线性分式函数的图形（双曲线）：
249. $y=\frac{1}{x}$.

徱 如图1.31所示。
250. $y=\frac{1-x}{1+x}$.

解 $y=-1+\frac{2}{1+x}$,
图形的对称中心为 $(-1,-1)$ ，如图 1.32 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-144.jpg?height=661&width=795&top_left_y=746&top_left_x=208)

图1.31
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-144.jpg?height=644&width=626&top_left_y=746&top_left_x=1069)

困 1.32
251. 把线性分式函数

$$
\begin{aligned}
& y=\frac{a x+b}{c x+d} \\
& (a d-b c \neq 0, c \neq 0)
\end{aligned}
$$

化为下面的形式

$$
y=y_{0}+\frac{m}{x-x_{0}} .
$$

再作它的图形。

## 研究例子

$$
y=\frac{3 x+2}{2 x-3}
$$

解 $y=\frac{a x+b}{c x+d}=\frac{a}{c}+\frac{\frac{b-a d}{c^{2}}}{x-\left(-\frac{d}{c}\right)}=y_{0}+\frac{m}{x-x_{0}}$ ，
其中

$$
x_{0}=-\frac{d}{c}, \quad y_{0}=\frac{a}{c}, \quad m=\frac{b c-a d}{c^{2}},
$$

如图1.33所示。

$$
\begin{aligned}
& \text { 对于 } y=\frac{3 x+2}{2 x-3}, \text { 有 } \\
& x_{0}=y_{0}=\frac{3}{2}, \text { 如图 } 1.34 \text { 所示. }
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-145.jpg?height=644&width=661&top_left_y=860&top_left_x=275)

图1.33
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-145.jpg?height=612&width=690&top_left_y=910&top_left_x=980)

固1.34
252. 气体当压力 $p_{0}=1$ 大气压时占有体积 $v_{0}=12$ 立方米. 设气体的温度保持不变作出气体体积 $v$ 随压力变化面变化的图形（波义耳一马瑞阿特定律）。
部 当温度 $T=k$ （常数）时，气体体积 $v$ 与压力 $p$ 成反比，眀

$$
p v=c
$$

其中 $C$ 为常数.
当 $p_{0}=1$ 时, $v_{0}=12$, 故 $C=12$, 从而 $p v=12$, 如图 1.35 所示.

作下列有理分式函数的图形：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-146.jpg?height=732&width=763&top_left_y=479&top_left_x=264)

国1.35
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-146.jpg?height=735&width=703&top_left_y=472&top_left_x=1025)

梸 1.36
253. $y=x+\frac{1}{x}$ (双曲线).

解 将 $y=x$ 及 $y=\frac{1}{x}$ 的图形蒀加即得，如图1.36中黑粗线所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-146.jpg?height=684&width=764&top_left_y=1754&top_left_x=252)

图 1.37
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-146.jpg?height=608&width=787&top_left_y=1766&top_left_x=1020)

图 1.38
254. $y=x^{2}+\frac{1}{x}$ (牛顿三次曲线).

解 将 $y=x^{2}$ 及 $y=\frac{1}{x}$ 的图形管加即得，如图 1.37 中黑粗线所示.
255. $y=x+\frac{1}{x^{2}}$.

解 如图 1.38 中黑粗线所示.
256. $y=\frac{1}{1+x^{2}}$ (筫舌线)。

解 图形对称于 $O y$ 轴，位于 $O x$ 轴上方，最高点为 $(0$ ， 1). 当 $x$ 的绝对值无限增大时, $y$ 值无限变小。如图1.39所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-147.jpg?height=455&width=777&top_left_y=1274&top_left_x=705)

图 1.39
257. $y=\frac{2 x}{1+x^{2}}$ (牛顿蛇形线).

解 以 $-x$ 换 $x, y$ 值的绝对值不变但改变符号，故图形对称于原点。

又因 $\left|\frac{2 x}{1+x^{2}}\right| \leqslant 1$, 故 $-1 \leqslant y \leqslant 1$.
当 $0<x<1$ 时， $y>0$ ，曲线上升；当 $1<x<+\infty$时， $y>0$ ，曲线下降。

图形以 $O x$ 轴为渐近线，如图 1.40 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-148.jpg?height=589&width=897&top_left_y=488&top_left_x=454)

娄1.40
258. $y=\frac{1}{1-x^{2}}$.

解 图形关于 $O y$ 轴对称，且经过点 $(0,1)$ 。
当 $0<x<1$ 及 $x>1$ 时, 曲线上升。但当 $x= \pm 1$
时， $y$ 无意义， $x= \pm 1$ 为曲线的渐近线。如图1.41 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-148.jpg?height=801&width=895&top_left_y=1510&top_left_x=472)

图1.41
259. $y=\frac{x}{1-x^{2}}$.

解 图形关于原点对称, 且经过原点. $x= \pm 1$ 为渐近 142

线. 在 $(0,1)$ 及（ $1,+\infty$ ）内曲线上升。如图1.42所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-149.jpg?height=758&width=795&top_left_y=449&top_left_x=231)

图1.42
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-149.jpg?height=732&width=849&top_left_y=451&top_left_x=1020)

图1.43
260. $y=\frac{1}{1+x}-\frac{2}{x}+\frac{1}{1-x}$.

解 将 $y=\frac{1}{1+x}, y=-\frac{2}{x}$ 及 $y=\frac{1}{1-x}$ 的图形备加即得，渐近线： $x=-1, x=0, x=1$ 及 $y=0$ ，如图 1.43所示。
261. $y=\frac{1}{1+x}-\frac{2}{x^{2}}+\frac{1}{1-x}$.

解 图形关于 $O y$ 納对称，详近线： $x=-1, x=1, x=$ 0 及 $y=0$ 。如图 1.44 所示。
262. $y=\frac{(x+1)(x-2)}{(x-1)(x+2)}$.

解 $y=\frac{x^{2}-x-2}{x^{2}+x-2}=1-\frac{2 x}{x^{2}+x-2}$.
将 $y=1$ 及 $y=-\frac{2 x}{(x+2)(x-1)}$ 的图形霍加即得。如图1.45所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-150.jpg?height=639&width=600&top_left_y=363&top_left_x=284)

图1.44
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-150.jpg?height=594&width=621&top_left_y=410&top_left_x=983)

图1.45
263. 把函数

$$
y=\frac{a x^{2}+b x+c}{a_{1} x+b_{1}}\left(a_{1} \neq 0\right)
$$

化为下面的形状

$$
y=k x+m+\frac{n}{x-x_{0}},
$$

然后作出它的略图。研究例子

$$
y=\frac{x^{2}-4 x+3}{x+1}
$$

解 $y=\frac{a}{a_{1}} x+\frac{a_{1} b-a b_{1}}{a_{1}^{2}}+\frac{\frac{c}{a_{1}}-\frac{b_{1}}{a_{1}^{3}}\left(a_{1} b-a b_{1}\right)}{x-\left(-\frac{b_{1}}{a_{1}}\right)}$

$$
\begin{aligned}
&=k x+m+\frac{n}{x-x_{0}} \\
& \text { 其中 } k=\frac{a}{a_{1}}, m=\frac{a_{1} b-a b_{1}}{a_{1}^{2}} ; \\
& x_{0}=-\frac{b_{1}}{a_{1}}, \\
& n=\frac{c}{a_{1}}-\frac{b_{1}}{a_{1}^{3}}\left(a_{1} b-a b_{1}\right) .
\end{aligned}
$$

如图1.46中黑粗线所示.
对于 $y=\frac{x^{2}-4 x+3}{x+1}$

$$
=x-5+\frac{8}{x+1}
$$

如图1.47中黑柤线所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-151.jpg?height=760&width=758&top_left_y=885&top_left_x=455)

图 1.46
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-151.jpg?height=1003&width=664&top_left_y=661&top_left_x=1227)
1.47
264. 一质点与引力中心相距 $x$. 设当 $x=1$ 米时引力 $F=10$千克，作出质点的引力 $F$ 的绝对值的图形（牛顿定律）。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-151.jpg?height=470&width=754&top_left_y=1975&top_left_x=731)

图1.48

解 由万有引力定律知

$$
F=\frac{k}{x^{2}},
$$

其中 $k$ 为常数。

$$
\begin{aligned}
& \text { 当 } x=1 \text { 时, } F=10, \text { 从而 } k=10 \text {, 于是, } \\
& F=\frac{10}{x^{2}},
\end{aligned}
$$

如图1.48 所示。
265. 根据梵德耳瓦斯定律（Завон Ван-дер-Вадъса），当温度不变时，真实气体的体积 $v$ 和它的压力 $p$ 以关系式

$$
\left(p+\frac{a}{v^{2}}\right)(v-b)=c
$$

相连系.
设 $a=2, b=0.1$ 及 $c=10$, 作出函数 $p=p(v)$ 的
图形。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-152.jpg?height=709&width=715&top_left_y=1504&top_left_x=271)

国1.49
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-152.jpg?height=638&width=718&top_left_y=1577&top_left_x=1043)

图1.50

解 由于

$$
p=\frac{10}{v-0.1}-\frac{2}{v^{2}},
$$

将 $p=\frac{10}{v-0.1}$ 及 $p=\frac{2}{v^{2}}$ 的图形叠加即得。如图1.49所示。

## 作下列无理函数的图形：

266. $y= \pm \sqrt{-x-2}$ (拋物线).

解 $y^{2}=-(x+2)$, 如图 1.50 所示.
267. $y= \pm x \sqrt{x}$ (半立方抛物线).

解 $y^{2}=x^{3}$ ，如图 1.51 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-153.jpg?height=680&width=569&top_left_y=1025&top_left_x=412)

图1.51
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-153.jpg?height=595&width=820&top_left_y=1073&top_left_x=1115)

图1.52
268. $y= \pm \frac{1}{2} \sqrt{100-x^{2}}$ (椭圆).

解 $\frac{x^{2}}{100}+\frac{y^{2}}{25}=1$ ，如图 1.52 所示。
269. $y= \pm \sqrt{x^{2}-1}$ (双曲线).

解 $x^{2}-y^{2}=1$, 如图 1.53 所示.
270. $y= \pm \sqrt{\frac{1-x}{1+x}}$.

解 $y^{2}=\frac{1-x}{1+x}, x=-1+\frac{2}{1+y^{2}}$,

将 $x=-1$ 及 $x=\frac{2}{1+y^{2}}$ 的图形㕿加即得, 如图 1.54 所示( $-1<x \leqslant+1$ )。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-154.jpg?height=595&width=727&top_left_y=613&top_left_x=139)

图1.53
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-154.jpg?height=703&width=735&top_left_y=568&top_left_x=903)

图 1.54
271. $y= \pm x \sqrt{100-x^{2} .}$

解 当 $x=0$ ， $\pm 10$ 时， $y=0$ 。
将 $y=x$ 和 $y=\sqrt{100-x^{i}}$ 的图形上点的纵坐标相乘，即可描出图形。如图1.55 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-154.jpg?height=752&width=635&top_left_y=1714&top_left_x=276)

图1.55
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-154.jpg?height=746&width=655&top_left_y=1717&top_left_x=963)

图1.56
272. $y= \pm x \sqrt{\frac{x}{10-x}}$ (嚷叶线).

解 $y^{2}(10-x)=x^{3}$ ，如图1.56所示。
273. $y= \pm \sqrt{\left(x^{2}-1\right)\left(9-x^{2}\right)}$.

野 $y= \pm \sqrt{16-\left(x^{2}-5\right)^{2}}$ 。如图1.57所示.

## 274. 作需函数

$$
y=x^{*}
$$

当：(a) $n=1,3,5$ ；(6) $n=2,4,6$ 时的图形。
普 如图 1.58 所示.

## 275. 作幕函数

$$
y=x^{n}
$$

当：（a） $n=-1,-3 ;(6) n=-2,-4$ 时的图形.
解 如图 1.59 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-155.jpg?height=869&width=1582&top_left_y=1413&top_left_x=237)

国 1.57
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-156.jpg?height=664&width=726&top_left_y=299&top_left_x=671)

图1.59
276. 作根式

$$
\begin{aligned}
& y=\sqrt[n]{x} \\
& \text { 当： }(\mathrm{a}) m=2,4 \text {; }
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-156.jpg?height=892&width=972&top_left_y=1310&top_left_x=573)

因1.60
(5) $m=3,5$ 时的图形.

解 如图 1.60 所示.
277. 设：

150
(a) $m=2, k \doteq 1 ;$
(6) $m=2, k=3$;
(в) $m=3, k=1 ;$
(r) $m=3, k=2$;
(д) $m=3, k=4$;
( e ) $m=4, k=2$;
(*) $m=4, k=3$ 。

作根式的图形

$$
y=\sqrt[m]{x^{x}}
$$

解 将所绘数据代入 $y=\sqrt[7]{x^{2}}$ ，可知：
(a) 即 $y=\sqrt{x}$ 的图形，见图1.60.
(6) $y=x \sqrt{x}$, 如图 1.61 所示: 1 ；
(B) 即 $y=\sqrt[3]{x}$ 的图形，见图1.60；
(г) $y=\sqrt[3]{x^{2}}$, 如图 1.61 所示: 2 ;
(д) $y=x \sqrt[3]{x}$, 如图 1.61 所示: 33
(e) 即 $y=\sqrt{|x|}$ 的图形;
（ж） $y=\sqrt[4]{x^{3}}$ ，如图1.61所示：4，
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-157.jpg?height=612&width=738&top_left_y=1661&top_left_x=248)

图1.61
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-157.jpg?height=638&width=772&top_left_y=1663&top_left_x=985)

图1.62
278. 作指数函数

$$
y=a^{x}
$$

当 $a=\frac{1}{2}, 1,2, e, 10$ 时的图形。
解 如图1.62所示。
279. 作复合指数函数

$$
y=e^{y_{1}}
$$

的图形，设：
（a） $y_{1}=x^{2}$ ；( 6 ) $y_{1}=-x^{2}$ ；( $) y_{1}=\frac{1}{x}$;
（г） $y_{1}=\frac{1}{x^{2}} ;$ （ $y_{1}=-\frac{1}{x^{2}}$, (e) $y_{1}=\frac{2 x}{1-x^{2}}$.

覃 （a）如图1.63所示；（6）如图1.64所示；
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-158.jpg?height=515&width=529&top_left_y=1210&top_left_x=501)

图1.63
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-158.jpg?height=501&width=521&top_left_y=1868&top_left_x=499)

图1.65
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-158.jpg?height=523&width=606&top_left_y=1212&top_left_x=1076)

嵲1.64
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-158.jpg?height=530&width=598&top_left_y=1871&top_left_x=1123)

图1.66
（B）如图1.65所示；（г）如图1.66所示；
（Д）如图1.67所示；（e）如图1.68所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-159.jpg?height=521&width=529&top_left_y=459&top_left_x=432)

園 1.67
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-159.jpg?height=538&width=609&top_left_y=462&top_left_x=1123)

图1.68
280. 作对数函数 $y=\log _{a} x$ 当 $a=\frac{1}{2}, 2, e, 10$ 时的图形。

解 如图1.69所示。
281. 作下列函数的图形：
(a) $y=\ln (-x) ;(6) y=-\ln x$.

解 如图1.70所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-159.jpg?height=560&width=495&top_left_y=1579&top_left_x=478)

团 1.69
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-159.jpg?height=704&width=689&top_left_y=1487&top_left_x=1046)

图 1.70
282. 设：

$$
\begin{aligned}
& \text { (a) } y_{1}=1+x^{2} ; \text { (б) } y_{1}=(x-1)(x-2)^{2}(x-3)^{3} ; \\
& \text { (в) } y_{1}=\frac{1-x}{1+x} ; \text { (г) } y_{1}=\frac{1}{x^{2}} ; \text { (д) } y_{1}=1+e^{x} .
\end{aligned}
$$

作出对数复合函数 $y=\ln y_{1}$ 的图形。
解 (a) 如图 1.71 所示;
（ $\sigma$ ）存在域： $x>3$ 或 $x<1$ 。
$y=\ln |x-1|+2 \ln |x-2|+3 \ln |x-3|$, 将此三个函
数的图形英加即得，如图 1.72 所示；
(в) $y=\ln (1-x)-\ln (1+x)$ ，将 $y=\ln (1-x)$ 及 $y$
$=-\ln (1+x)$ 的图形坥加即得, 如图 1.73 所示 $(-e<$ $x<1$ );
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-160.jpg?height=615&width=729&top_left_y=1009&top_left_x=321)

图1.71
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-160.jpg?height=661&width=572&top_left_y=1708&top_left_x=454)

图 1.73
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-160.jpg?height=657&width=635&top_left_y=965&top_left_x=1207)

图1.72
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-160.jpg?height=663&width=714&top_left_y=1696&top_left_x=1085)

图1.74
（г） $y=\ln \frac{1}{x^{2}}$ ，如图 1.74 所示，图形关于 $O_{y}$ 轴对称；
(込 如图 1.75 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-161.jpg?height=664&width=866&top_left_y=499&top_left_x=452)

图 : 75

## 283. 作函数

$$
y=\log _{x} 2
$$

的图形
解 如图 1.76 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-161.jpg?height=1075&width=1571&top_left_y=1573&top_left_x=231)

## 284. 作函数

$$
y=A \sin x
$$

当 $A=1,10,-2$ 时的图形.
解 如图1.77所示。

## 285. 作函数

$$
y=\sin \left(x-x_{0}\right)
$$

当 $x_{4}=0, \frac{\pi}{4}, \frac{\pi}{2}, \frac{3 \pi}{4}$, $\pi$ 时的图形.
解 只要将 $y=\sin x$ 的图形向右平移距离 $\frac{\pi}{4}, \frac{\pi}{2}, \frac{3 \pi}{4}, \pi$即得，如图1.78所示。

$$
\begin{aligned}
& \text { 1. } y=\sin x ; 2 . y=\sin \left(x-\frac{\pi}{4}\right) ; \\
& \text { 3. } y=\sin \left(x-\frac{\pi}{2}\right) ; 4 . y=\sin \left(x-\frac{3 \pi}{4}\right) ; \\
& \text { 5. } y=\sin (x-\pi) .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-162.jpg?height=581&width=1260&top_left_y=1594&top_left_x=449)

图 1.78
286. 作函数

$$
y=\sin n x
$$

的图形. 设 $n=1,2,3, \frac{1}{2}, \frac{1}{3}$.
解 如图 1.79 所示.

1. $y=\sin x ; 2 . y=\sin 2 x ;$
2. $y=\sin 3 x ; 4 . y=\sin \frac{1}{2} x$;
3. $y=\sin \frac{1}{3} x$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-163.jpg?height=483&width=1146&top_left_y=975&top_left_x=546)

图1.79
287. 把函数

$$
y=a \cos x+b \sin x
$$

化为下面的形状

$$
y=A \sin \left(x-x_{0}\right),
$$

再作它的图形。

## 研究例子

$$
y=6 \cos x+8 \sin x
$$

解 $y=\sqrt{a^{2}+b^{2}}\left(\frac{a}{\sqrt{a^{2}+b^{2}}} \cos x+\frac{b}{\sqrt{a^{2}+b^{2}}} \sin x\right)$ ，
由于

$$
\left|\frac{a}{\sqrt{a^{2}+b^{2}}}\right| \leqslant 1,\left|\frac{b}{\sqrt{a^{2}+b^{2}}}\right| \leqslant 1 \text { 及 }
$$

$\left(\frac{a}{\sqrt{a^{2}+b^{2}}}\right)^{2}+\left(\frac{b}{\sqrt{a^{2}+b^{2}}}\right)^{2}=1$,
故可令

$$
\sin x_{0}=\frac{-a}{\sqrt{a^{2}+b^{2}}}, \quad \cos x_{0}=\frac{b}{\sqrt{a^{2}+b^{2}}} .
$$

于是

$$
y=A \sin \left(x-x_{0}\right)
$$

其中

$$
A=\sqrt{a^{2}+b^{2}} \quad\left(a^{2}+b^{2} \neq 0\right), x_{2} \text { 适合 (1) 式. }
$$

（2）式图形是这样作的：先把正弦曲线 $y=\sin x$ 沿 $O x$ 轴平移距高 $\left|x_{0}\right|$ （或 $x_{0}>0$ 时，则向右移：若 $x_{0}<0$时向左移），然后再从纵轴"伸长" $A$ 倍（当 $A<1$ 时为压缩 $\frac{1}{A}$ 倍)。

## 对于例子

$$
\begin{aligned}
& y=6 \cos x+8 \sin x \\
& A=\sqrt{6^{2}+8^{2}}=10, \\
& \sin x_{0}=-\frac{6}{10}=-\frac{3}{5}, \\
& \cos x_{0}=-\frac{4}{5} \\
& x_{0}=-\operatorname{arctg} \frac{3}{4},
\end{aligned}
$$

如图1.80所示。
作下列三角函数的图形：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-164.jpg?height=917&width=681&top_left_y=1306&top_left_x=1093)

图 - 1 - 80 288. $y=\cos x$.

解 如图 1.81 所示.
289. $y=\operatorname{tg} x$.

解 如图 1.82 所示.
290. $y=\operatorname{ctg} x$.

解 如图 J. 83 所示。
297. $y=\sec x$.

解 如图1.84所示. 292. $y=\csc x$.

解 如图1.85所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-165.jpg?height=509&width=826&top_left_y=448&top_left_x=986)

图1-81
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-165.jpg?height=1354&width=1580&top_left_y=1119&top_left_x=238)

图 I - 83
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-166.jpg?height=637&width=735&top_left_y=404&top_left_x=195)

团 $1 \cdot 84$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-166.jpg?height=600&width=589&top_left_y=451&top_left_x=1093)

田1 - 85
293. $y=\sin ^{2} x$.

解 如图1.86所示.
294. $y=\sin ^{3} x$.

解 如图1.87所示.
295. $y=\operatorname{ctg}^{2} x$

解 如图1.88所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-166.jpg?height=441&width=892&top_left_y=1113&top_left_x=936)
-

手 1 - 86
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-166.jpg?height=512&width=1593&top_left_y=1643&top_left_x=240)

图1 1 - 87

图 1 • 88
296. $y=\sin x \cdot \sin 3 x$.

解 图形关于 $O y$ 轴对称. 周期为 $\pi$. 将 $y=\frac{1}{2} \cos 2 x$ 及 $y=-\frac{1}{2} \cos 4 x$ 的图形叠加即得. 如图 1.89 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-167.jpg?height=638&width=1186&top_left_y=732&top_left_x=532)

图 1-89
297. $y= \pm \sqrt{\cos x}$.

解 图形关于 $O x$ 轴及 $O y$ 轴均对称，是以 $2 \pi$ 为周期的周期函数，如图 1.90 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-167.jpg?height=484&width=1051&top_left_y=1728&top_left_x=591)

图 1 - 90
作下列函数的图形：
298. $y=\sin x^{2}$.

解 图形关于 $O y$ 轴对称。因为

$$
f(\sqrt{\pi})=f(\sqrt{2 \pi})=\cdots=f(\sqrt{n \pi})=0
$$

并且 $\lim _{n \rightarrow \infty}(\sqrt{n+1) \pi}-\sqrt{n \pi})=0$, 所以曲线和横轴的相邻交点的相互距离所成的叙列的极限为零。

由不等式 $\sin x^{2}<x^{2}$ ，我们知道这条曲线位于拋物线 $y=x^{z}$ 的下方，如图1.91所示。
299. $y=\sin \frac{1}{x}$.

解 $-1 \leqslant y \leqslant 1 . \lim _{x \rightarrow \infty} y=0, y=0$ 为渐近线。
当 $x$ 由 $+\infty$ 减小到 $\frac{2}{\pi}$ 时，则 $\frac{1}{x}$ 由 0 增大到 $\frac{\pi}{2}$ ，而 $y$由 0 增到 1 ；但当 $x$ 由 $\frac{2}{\pi}$ 减小到 $\frac{2}{3 \pi}$ ，则 $\frac{1}{x}$ 由 $\frac{\pi}{2}$ 增大到 $\frac{3 \pi}{2}$ ，而 $y$ 由 1 减小到 -1 、当 $x=\frac{1}{\pi}$ 时， $y=0$ 等。因为 $y$ 是奇函数，故图形关于原点对称。当 $x$ 无限接近 0 时，芼数在 -1 与 1 之间摆动，并且㾳聚于 0 点，而在点 $x=0$ 处，函数 $y$ 没有 定义。如图1.92所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-168.jpg?height=655&width=1117&top_left_y=1757&top_left_x=458)

图 1 - 91
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-169.jpg?height=469&width=1763&top_left_y=445&top_left_x=135)

图 1 1 . 92
300. $y=x \cos \frac{\pi}{x}$.

解 $-x \leqslant y \leqslant x . \quad \lim _{x \rightarrow \infty} y=\infty$.
当 $x=\frac{2}{2 k+1}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ 。
当 $x>2$ 时， $y$ 单调增加，因为 $y$ 基奇函数，故固形关于原点对称。而在点 $x=0$ ，函数 $y$ 没有定义。

当 $x$ 无限接近 0 时，函数作无限次衰减控动，并凝聚于 $O$ 点。如图1.93所亦。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-169.jpg?height=732&width=846&top_left_y=1730&top_left_x=611)

图 $1 \cdot 93$

## 301. $y=\operatorname{tg} \frac{\pi}{x}$.

解 当 $x=\frac{1}{k}(k= \pm 1, \pm 2, \cdots)$ 时， $y=0$ 。
当 $x \rightarrow \frac{2}{2 k+1}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y \rightarrow \infty$ 。
当 $x>2$ 时, $y>0$, 且当 $x \rightarrow+\infty$ 时, $y \rightarrow 0$ 。
因为 $y$ 为奇函数，故图形关于原点对称。
当 $x \rightarrow 0$ 时，图形疑聚于 $O$ 点，而在点 $x=\frac{2}{2 k+1}$ 及
0 ，函数 $y$ 是没有定义的。
如图 1.94 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-170.jpg?height=1063&width=1332&top_left_y=1276&top_left_x=336)

图 1.94
302. $y=x\left(2+\sin \frac{1}{x}\right)$.

解 先作 $y=x \sin \frac{1}{x}$ 的图形。因为 $y$ 为偶函数，故图形关于 $O y$ 轴对称。

当 $x=\frac{2}{(2 k+1) \pi}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=$ $\pm x$ 。

$$
\begin{aligned}
& \text { 当 } x=\frac{1}{k \pi}(k= \pm 1, \pm 2, \cdots) \text { 时, } y=0 . \\
& \text { 当 } x>\frac{2}{\pi} \text { 时, } y \text { 单调增加, 且有 } \\
& \left.\qquad \lim _{x \rightarrow \infty} x \sin \frac{1}{x}=\lim _{x \rightarrow \infty} \frac{\sin \frac{1}{x}}{\frac{1}{x}}=1 *\right)
\end{aligned}
$$

如图1.95所示（在点 $x=0$ 无定义）。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-171.jpg?height=872&width=1251&top_left_y=1409&top_left_x=491)

图 1.95
其次，再将函数 $y=2 x$ 及 $y=x \sin \frac{1}{x}$ 的图形"叠加"，即得

$$
y=x\left(2+\sin \frac{1}{x}\right)
$$

的图形。如图1.96所示，

* ）此结果参看本章§5.


## 303. $y= \pm \sqrt{1-x^{2}} \sin \frac{\pi}{x}$.

解 图形关芐原点及
$O y$ 轴， $O x$ 轴均对称。由于

$$
\begin{aligned}
& -\sqrt{1-x^{2}} \leqslant y \\
& \leqslant \sqrt{1-x^{2}} \\
& (|x| \leqslant 1)
\end{aligned}
$$

故图形位于圆 $x^{2}+y^{2}$
$=1$ 内。
将函数 $y= \pm \sqrt{1-x^{2}}$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-172.jpg?height=1126&width=712&top_left_y=336&top_left_x=1072)

图 1.96

与 $y=\sin \frac{\pi}{x}$ 的级坐标
对应相乘，即可描出所求的图形。

如图1 - 97 所示.
304. $y=\frac{\sin x}{x}$.

算 $\lim _{\alpha \rightarrow 0} y=1$.
$\lim _{x \rightarrow \infty} y=0$. 由于 $|y| \leqslant \frac{1}{|x|}$,
故图形在 $y=-\frac{1}{x}$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-172.jpg?height=660&width=680&top_left_y=1629&top_left_x=1145)

图 1.97

及 $y=\frac{1}{x}$ 之问。又图形关于 $O y$ 轴对称. 当 $x=k \pi$ 时， $y=$

$$
\begin{array}{r}
0(k= \pm 1, \pm 2, \cdots) . \\
\text { 如图 } 1 \cdot 98 \text { 所示. }
\end{array}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-173.jpg?height=566&width=1777&top_left_y=562&top_left_x=111)

图 $1 \cdot 98$
305. $y=e^{x} \cos x$.

解 由于 $-e^{x} \leqslant y \leqslant e^{x}$ ，故图形在 $y=e^{x}$ 及 $y=e^{-x}$ 之间。

$$
\text { 当 } x=(2 k+1) \frac{\pi}{2}(k=0, \pm 1, \pm 2, \cdots) \text { 时, } y=
$$

0 . 且 $\lim _{x \rightarrow-\infty} y=0$, 但 $\lim _{x \rightarrow+\infty} e^{x} \cos x$ 却不存在。
如图 1.99 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-173.jpg?height=684&width=1221&top_left_y=1794&top_left_x=446)

图 1.99
306. $y= \pm 2^{-x} \sqrt{\sin \pi x}$.

解 当 $2 k \leqslant x \leqslant(2 k+1)(k=0, \pm 1, \pm 2 \cdots)$ 时， $y$值才确定。当 $k=2 k+\frac{1}{2}$ 时， $y= \pm 2^{-x}$ 。

图形关于 $O x$ 轴对称。 $\lim _{x \rightarrow+\infty} y=0$ ，而 $\lim _{x \rightarrow-\infty} y$ 不存在。如图 $1 \cdot 100$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-174.jpg?height=934&width=1023&top_left_y=875&top_left_x=539)

图 $1 \cdot 100$
307. $y=\frac{\cos x}{1+x^{2}}$.

解 $-\frac{1}{1+x^{2}} \leqslant y \leqslant \frac{1}{1+x^{2}}$,
图形在 $y=-\frac{1}{1+x^{2}}$ 及 $=\frac{1}{1+x^{2}}$ 之间, 且关于 $O y$ 轴对称.
$\lim _{x \rightarrow \infty} y=0, \quad \lim _{x \rightarrow 0} y=1$.
㚼图 1-101 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-175.jpg?height=458&width=1574&top_left_y=316&top_left_x=224)

图 1 • 101
308. $y=\ln (\cos x)$.

解 存在域是使 $\cos x>0$ 的开区间

$$
\left((4 k-1) \frac{\pi}{2},(4 k+1) \frac{\pi}{2}\right)(k=0, \pm 1, \pm 2, \cdots)
$$

的全体. 函数 $y$ 是以 $2 \pi$ 为周期的周期函数. 在区间 $\left(-\frac{\pi}{2}, 0\right)$ 内， $y$ 单调增加，且 $y<0$ 。在 $\left(0, \frac{\pi}{2}\right)$ 内， $y$ 单调城小， $y<0$ 。最大值是 $y=\operatorname{lncos} 0=0$ 。又 $\lim _{x \rightarrow \frac{\pi}{2}+0} y=\lim _{x \rightarrow \frac{\pi}{2}-6} y=-\infty$ ，如団 $1 \cdot 102$ 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-175.jpg?height=820&width=989&top_left_y=1669&top_left_x=616)

图 $\mathbf{1 - 1 0 2}$
309. $y=\cos (\ln x)$.

解 存在域为数 $x>0$ 的全体。
当 $x=e^{(2 k+1) \frac{\pi}{2}}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ 。
当 $x=e^{2 \pi}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=1$ ；
而当 $x=e^{(2 k+1) *}$ 时, $y=-1$ 。
图形始终在直线 $y=-1$ 和 $y=1$ 之间摆动，而且越靠近原点时，摆动越密。

如图1.103所示. (两轴所取的单位不一致)。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-176.jpg?height=635&width=1240&top_left_y=1113&top_left_x=431)

图 1 • 103.
310. $y=e^{\frac{1}{\sin }}$.

解 $y>0$ 。
函数 $y$ 是以 $2 \pi$ 为周期的周期函数.
当 $0<x<\frac{\pi}{2}$ 时， $y$ 单调减少；
当 $\frac{\pi}{2}<x<\pi$ 时， $y$ 单调增加. 又有
$\lim _{x \rightarrow 0} y=\lim _{x \rightarrow-0} y=+\infty$.
$\left.y\right|_{ \pm=\frac{\pi}{2}}=e$ 为区间 $(0, \pi)$ 内, 函数 $y$ 的最小值.

同理， $x$ 由 $\pi$ 到 $\frac{3 \pi}{2}$ 时， $y$ 由 0 增到 $\frac{1}{e}$; 而 $x$ 由 $\frac{3 \pi}{2}$ 到 $2 \pi$ 时, $y$西 $\frac{1}{e}$ 减到 $0 . \lim _{x \rightarrow x+0} y=\lim _{x \rightarrow 2 x-0} y=0$ 。

如图 1 - 104 所示.
作下列反三角函数的图形：
$311 . y=\arcsin x$.
解 如图 1.105 所示的 $A B$ 段曲线。
312. $y=\arccos x$.

解 如图1.106所示的 $A B$ 段曲线。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-177.jpg?height=575&width=903&top_left_y=706&top_left_x=939)

图 1 - 104
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-177.jpg?height=977&width=341&top_left_y=1462&top_left_x=1326)

图1 1 106
313. $y=\operatorname{arctg} x$.

解 如图 1.107 所示的 $A B$ 段曲线。
314. $y=\operatorname{arcctg} x$.

释 如图1.108 所示的 $A B$ 段曲线.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-178.jpg?height=806&width=792&top_left_y=722&top_left_x=232)

图1.107
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-178.jpg?height=806&width=635&top_left_y=725&top_left_x=1096)

图1 • 108
315. $y=\arcsin \frac{1}{x}$.

解 图形关于原点对称。
存在域量区间 $(-\infty,-1)$ 和 $(1,+\infty)$ 。
当 $1 \leqslant x<+\infty$ 时，由于 $\frac{1}{x}$ 单调减少，所以， $y$ 也是减函
数, 且有

$$
\begin{aligned}
& \lim _{x \rightarrow 1+\infty} y=\frac{\pi}{2} \\
= & \left.y\right|_{x=1}, \lim _{s \rightarrow+\infty} y \\
= & 0 .
\end{aligned}
$$

如图 1-109 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-178.jpg?height=446&width=714&top_left_y=2050&top_left_x=1071)

固 1 • 109
316. $y=\arccos \frac{1}{x}$.

解 存在域是区间 $(-\infty,-1$ 〕和 $[1,+\infty$ ).
当 $1 \leqslant x<+\infty$ 时，由于 $\frac{1}{x}$ 单调减少，所以， $y$ 是增函数，且有

$$
\lim _{x \rightarrow+\infty} y=0, \quad \lim _{x \rightarrow+\infty} y=\frac{\pi}{2} .
$$

同理，当 $-\infty<x \leqslant-1$ 时， $y$ 单调增加；且有

$$
\lim _{x \rightarrow-1-0} y=\pi, \quad \lim _{x \rightarrow-\infty} y=\frac{\pi}{2} .
$$

如图1 - 110 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-179.jpg?height=710&width=1180&top_left_y=1207&top_left_x=529)

图 1 • 110
317. $y=\operatorname{arctg} \frac{1}{x}$.

解 图形关于原点对称。
当 $x>0$ 时，由于 $\frac{1}{x}$ 单调减少，所以， $y$ 是减函数，且有

$$
\lim _{x \rightarrow+0} y=\frac{\pi}{2}, \quad \lim _{x \rightarrow+\infty} y=0 .
$$

如图 1-111所示。
318. $y=\arcsin (\sin x)$.

解 $\sin y=\sin x,-\frac{\pi}{2} \leqslant y \leqslant \frac{\pi}{2}$.
因此，当 $-\frac{\pi}{2} \leqslant x \leqslant \frac{\pi}{2}$ 时. $y=x$ ；

$$
\begin{aligned}
& \text { 当 } \frac{\pi}{2} \leqslant x \leqslant \frac{3 \pi}{2} \text { 时, } y=\pi-x ; \\
& \text { 当 } \frac{3 \pi}{2} \leqslant x \leqslant \frac{5 \pi}{2} \text { 时, } y=x-2 \pi .
\end{aligned}
$$

## 一般地，

$$
\text { 当 }-\frac{\pi}{2}+2 k \pi \leqslant x \leqslant \frac{\pi}{2}+2 k \pi \text { 时, } y=x-2 k \pi \text {; }
$$

$(k=0, \pm 1, \pm 2, \cdots$ )
而当 $\frac{\pi}{2}+2 k \pi \leqslant x \leqslant \frac{3 \pi}{2}+2 k \pi$ 时， $y=(\pi-x)+2 k \pi$.
如图 $1 \cdot 112$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-180.jpg?height=610&width=921&top_left_y=1511&top_left_x=222)

图 $1 \cdot 111$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-180.jpg?height=452&width=969&top_left_y=2033&top_left_x=795)

图 $1 \cdot 112$
319. $y=\arcsin (\cos x)$.

解 $\sin y=\cos x,-\frac{\pi}{2} \leqslant y \leqslant \frac{\pi}{2}$.
因此，当 $-\pi \leqslant x \leqslant 0$ 时， $y=\frac{\pi}{2}+x$ ；
当 $0 \leqslant x \leqslant \pi$ 时， $y=\frac{\pi}{2}-x$ 。
一般地，
当 $(2 k-1) \pi \leqslant x \leqslant 2 k \pi$ 时， $y=\left|\frac{\pi}{2}+x\right|-2 k \pi$ $(k=0, \pm 1, \pm 2, \cdots)$ ；

而当 $2 k \pi \leqslant x \leqslant(2 k+1) \pi$ 时,$y=\left|\frac{\pi}{2}-x\right|+$ $2 k \pi$.

如图1 - 113 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-181.jpg?height=592&width=1198&top_left_y=1440&top_left_x=489)

图 $1 \cdot 113$
320. $y=\arccos (\cos x)$.

箥 $\cos y=\cos \boldsymbol{x}, 0 \leqslant y \leqslant \pi$.
因此，当 $0 \leqslant x \leqslant \pi$ 时， $y=x$ ；
当 $\pi \leqslant x \leqslant 2 \pi$ 时， $y=2 \pi \ldots x$ ；
当 $-\pi \leqslant x \leqslant 0$ 时, $y=-x$ 。

一般地，
当 $(2 k-1) \pi \leqslant x \leqslant 2 k \pi$ 时， $y=-x+2 k \pi(k=0$,
$\pm 1, \pm 2, \cdots)$;
而当 $2 k \pi \leqslant x \leqslant(2 k+1) \pi$ 时， $y=x-2 k \pi$.
如图 $1 \cdot 114$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-182.jpg?height=566&width=1497&top_left_y=862&top_left_x=294)

图 1 : 114
321. $y=\operatorname{arctg}(\operatorname{tg} x)$.

解 $\operatorname{tg} y=\operatorname{tg} x,-\frac{\pi}{2}<y<\frac{\pi}{2}$.
因此, 当 $-\frac{\pi}{2}<x<\frac{\pi}{2}$ 时, $y=x$ ；

$$
\begin{aligned}
& \text { 当 } \frac{\pi}{2}<x<\frac{3 \pi}{2} \text { 时, } y=x-\pi ; \\
& \text { 当 }-\frac{3 \pi}{2}<x<-\frac{\pi}{2} \text { 时, } y=\pi+x .
\end{aligned}
$$

## 一般地，

$$
\text { 当 }-\frac{\pi}{2}+k \pi<x<\frac{\pi}{2}+k \pi \text { 时, } y=x-k \pi(k=
$$

$0, \pm 1, \pm 2, \cdots)$ 。
如图 1-115所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-183.jpg?height=472&width=949&top_left_y=409&top_left_x=556)

图 $1 \cdot 115$
322. $y=\arcsin (2 \sin x)$.

解 $\sin y=2 \sin x,-\frac{2}{\pi} \leqslant y \leqslant \frac{\pi}{2}$.
存在域为区间：

$$
\left[-\frac{\pi}{6}, \frac{\pi}{6}\right),\left(\frac{5 \pi}{6}, \frac{7 \pi}{6}\right], \cdots
$$

的全体. 即 $\left[-\frac{\pi}{6}+k \pi, \frac{\pi}{6}+k \pi\right](k=0, \pm 1, \pm 2, \cdots)$的全体。

利用复合函数作图法得其图形，如图 1.116 所示，它关于原点对称。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-183.jpg?height=680&width=1226&top_left_y=1756&top_left_x=512)

固 1.116
323. 设
(a) $y_{1}=1-\frac{x}{2} ;$
（б） $y_{1}=\frac{2 x}{1+x^{2}}$ ；
（в） $y_{1}=\frac{1-x}{1+x} ; \quad$ (г) $y_{1}=e^{x}$.

作函数

$$
y=\arcsin y_{1}
$$

的图形。
解
（a）存在域为满足不等式

$$
0 \leqslant x \leqslant 4
$$

的数 $x$ 的集台。
当 $0 \leqslant x \leqslant 2$ 时， $y$ 由 $\frac{\pi}{2}$ 减少到 0 ；
而当 $2 \leqslant x \leqslant 4$ 牱,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-184.jpg?height=577&width=829&top_left_y=868&top_left_x=948)
$y$ 由 0 减少到 $-\frac{\pi}{2}$.
图 $1 \cdot 117$

如图1 - 117 所示.
（Б）图形关
于原点对称。存在域为全体实数。
当 $x$ 由 0 增到 1
时，"由 $\frac{2 x}{1+x^{2}}$
为增函数，故 $y$ 由
0 增到的 $\frac{\pi}{2}$. 而当
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-184.jpg?height=664&width=892&top_left_y=1644&top_left_x=885)

图 $1 \cdot 118$
$x>1$ 时, $\frac{2 x}{1+x^{2}}$ 为减函数,故 $y$ 由 $\frac{\pi}{2}$ 减少到 0 , 且 $\lim _{x \rightarrow+\infty} y$
$=0$. 如图1 - 118 所示.
( ( ) 要 $\left|\frac{1--x}{1+x}\right| \leqslant 1$, 只要 $x \geqslant 0$, 故存在域为 $x \geqslant 0$的数 $x$ 的集合。当 $x$ 由 0 增到 1 时， $\frac{1}{1+x}$ 由 1 减少到 0 ，而 $y$ 则甶 $\frac{\pi}{2}$ 减少到 0 ；而当 $x$ 由 1 增到 $+\infty$ 时， $\frac{1-x}{1+x}$ 由 0 减少到 -1 , 而 $y$ 由 0 减少到 $-\frac{\pi}{2}$, 且 $\lim _{x \rightarrow+\infty} y=\frac{\pi}{2}$, 如图 1. 119 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-185.jpg?height=549&width=937&top_left_y=1113&top_left_x=571)

图 1.119
（「）存在域为 $-\infty<x \leqslant 0$的数 $x$ 的集合。当 $x$ 由 一 $\infty$ 增到 0 时， $e^{x}$ 由 0 增到 1 ，而 $y$ 则由 0 增到 $\frac{\pi}{2}$ ，如图
1 - 120 所示.
$\qquad$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-185.jpg?height=63&width=61&top_left_y=2133&top_left_x=1076)

图 $1 \cdot 120$
324. 设
(a) $y_{1}=x^{2}$ ；(6) $y_{1}=\frac{1}{x^{2}}$ ；
(в) $y_{1}=\ln x ;$ （г） $y_{1}=\frac{1}{\sin x}$.

作函数

$$
y=\operatorname{arctg} y_{1}
$$

的图形。
管，（a）如图1 - 121 所示的 $A B$ 曲线.
(6) 如图 1 - 122 所示.
(B) 如图 1 - 123 所示的 $O A$ 曲线.
（г）以 $2 \pi$ 为周期. 当 $x$ 由 0 增到 $\frac{\pi}{2}$ 时， $\frac{1}{\sin x}$ 由 $+\infty$
减到 1 ，而 $y$ 则由 $\frac{\pi}{2}$ 减到 $\frac{\pi}{4}$. 余类推，如图 $1 \cdot 124$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-186.jpg?height=703&width=746&top_left_y=1253&top_left_x=244)

图 1 - 121
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-186.jpg?height=492&width=960&top_left_y=1890&top_left_x=802)

因 $1 \cdot 122$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-187.jpg?height=812&width=801&top_left_y=394&top_left_x=185)

图 $1 \cdot 123$
325. 已知函数 $y=f(x)$ 的图形，作下列各函数的图形
(a) $y=-f(x)$;
(6) $y=f(-x)$;
(B) $y=-f(-x)$.

解 (a) 函数 $y=-f(x)$
的图形和函数 $y=f(x)$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-187.jpg?height=506&width=844&top_left_y=701&top_left_x=983)

图 $1 \cdot 124$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-187.jpg?height=464&width=563&top_left_y=1304&top_left_x=1232)

图 1-125的图形关于 $O x$ 轴对称. 如图 1 - 125所示.
（6）函数 $y=$
$f(-x)$ 的图形和
函数 $y=f(x)$ 的
图形关于 $O y$ 轴
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-187.jpg?height=478&width=881&top_left_y=1920&top_left_x=916)

图 1.126

对称. 如图 1.126 所示.
(B) 函数 $y=-f(-x)$ 的图形和函数 $y=f(x)$的图形关于原点
对称. 如图1 - 127
所示。
326. 已知函数 $y=$
$f(x)$ 的图形, 作下列各函数的图形：
(a) $y=f\left(x-x_{0}\right)$;
(6) $y=y_{0}+f\left(x-x_{0}\right)$;
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-188.jpg?height=207&width=838&top_left_y=522&top_left_x=969)
(B) $y=f(2 x) ;$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-188.jpg?height=655&width=1046&top_left_y=1117&top_left_x=805)
(5) $y=f(k x+b)$
( $k \neq 0$ )
解 （a）函数 $y=$
$f\left(x-x_{0}\right)$ 的图形可
由 $y=f(x)$ 的图形平移距离 $\left|x_{0}\right|$得出.

当 $x_{0}>0$ 时，问右平移；
当 $x_{0}<0$ 时，向左平移。
如图1-128所示。
（ 6 ）函数 $y=y_{0}+f\left(x-x_{0}\right)$ 的图形可由 $y=f(x)$的图形先平移距离 $\left|x_{0}\right|$ ，再上下平移距离 $\left|y_{0}\right|$ 得出，其中

当 $y_{0}>0$ 时，向上平移；
当 $x_{0}<0$ 时，向下平移。
事实上，只要先将坐标原点平移到点 $\left(x_{0}, y_{0}\right)$. 坐标轴的

方向均不变，再在新坐标系中作 $y^{\prime}=f\left(x^{\prime}\right)$ 的图形，其中 $y^{\prime}=y-y_{0}, x^{\prime}=x-x_{0}$.

图形如图 $1 \cdot 129$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-189.jpg?height=786&width=1240&top_left_y=595&top_left_x=545)
(B) $y=f(2 x)$ 的图形可由 $y=f(x)$ 的图形沿 $O x$ 轴方向缩小二倍得出。

图形如图1 - 130 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-189.jpg?height=667&width=883&top_left_y=1671&top_left_x=715)

图 1 • 130
(г) $y=f(k x+b)$

的图形可由 $y=f(x)$的图形先沿 $O x$ 轴方向 "医缩" $k$ 倍（ $0<k<1$时，理㙰为"放大"）。
然后再将所得图形平移距离 $|b|$ 。

图形如图1.131所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-190.jpg?height=593&width=775&top_left_y=366&top_left_x=1023)

图 1 • 131
327. 作函数的图形
(a) $y=2+\sqrt{1-x}$ ；(6) $y=1-e^{-x} ;$
(в) $y=\ln (1+x)$. ( $) y=-\frac{\pi}{2} \arcsin (1+x)$;
(д) $y=3+2 \cos 3 x$.

解 (a) 如图 1-132 所示.
(6) 如图 1.133 所示.
(B) 如图 $1 \cdot 134$ 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-190.jpg?height=561&width=903&top_left_y=1781&top_left_x=314)
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-190.jpg?height=549&width=606&top_left_y=1342&top_left_x=1205)

图 $1 \cdot 132$

图 $1 \cdot 139$
(r) 如图 1 - 135 所示的 $A B$ 曲线.
（л）如图 1 - 136 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-191.jpg?height=681&width=613&top_left_y=502&top_left_x=316)

图 1 • 134
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-191.jpg?height=803&width=387&top_left_y=501&top_left_x=977)

图 1 - 135
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-191.jpg?height=800&width=995&top_left_y=1462&top_left_x=485)

图 1 - 136
328. 已知函数 $y=f(x)$ 的图形，作下列函数的图形：

$$
\text { (a) } y=|f(x)| ; \text { (б) } y=\frac{1}{2}[|f(x)|+f(x)] \text {; }
$$

(B) $y=\frac{1}{2} \subset|f(x)|$

- $f(x)$.

解 (a) 当 $f(x) \geqslant$ 0 时， $y=f(x)$ ；

当 $f(x)<0$ 时,
$y=-f(x) ;$
如图 $1 \cdot 137$ 黑
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-192.jpg?height=561&width=834&top_left_y=379&top_left_x=948)

图 $1 \cdot 137$
粗线所示.
(6) 当 $f(x) \geqslant$

0 时, $y=f(x)$ ；
当 $f(x)<0$ 时,
$y=0$.
如图 1 • 138黑
粗线所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-192.jpg?height=549&width=758&top_left_y=1022&top_left_x=1052)

图 $1 \cdot 138$
（日）档 $f(x) \geqslant 。$ 0 时， $y=0$ ；

当 $f(x)<0$ 时, $y=-f(x)$.

如图 $1 \cdot 139$ 黑粗线所示.
329. 已知函数 $y=f(x)$

的图形，作下列函
数的图形：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-192.jpg?height=626&width=981&top_left_y=1660&top_left_x=877)

图 1 • 139
（a） $y=f^{2}(x) ;(5) y=\sqrt{f(x)}$ ；
(в) $y=\ln f(x) ;(\Gamma) y=f[f(x)] ;$
（山） $y=\operatorname{sng} f(x) ;(e) y=[f(x)]$.
解 (a) 以 $y=1$ 为图形的分界线.
如图 1 - 140 所示. 1: $y=f(x) ; 2: y=f^{2}(x)$.
（5）当 $f(x)>1$ 时， $\sqrt{f(x)}<f(x)$ ；而当 $0 \leqslant f(x)$
$<1$ 时， $\sqrt{f(x)} \geqslant f(x)$ 。
如图 1-141 所示. 1: $y=f(x) ; 2 ; y=\sqrt{f(x)}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-193.jpg?height=597&width=829&top_left_y=935&top_left_x=248)

囯 1 - 140
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-193.jpg?height=606&width=664&top_left_y=928&top_left_x=1113)

图 1 - 141
（B）当 $f(x) \geqslant 1$ 时， $\ln f(x)<f(x)$ ；而当 $0<f(x)$ $<1$ 时, $\ln f(x)<f(x)$, 故 $y=\ln f(x)$ 的图形始终在 $y$ $=f(x)$ 之下.

如图1.142所示.
(г) 若 $f(x)$ 的存在域为 $[a, b]$ ，则仅当 $f(x)$ 之值在 $a$与 $b$ 之间，才能使 $f[f(x)]$ 有意义。其详细作图法见 330题（B）。

如图 1 - 143 所示. 1: $y=f(x)$; 2: $y=f[f(x)]$ 。
（д）当 $f(x)>0$ 时, $y=1$ ；当 $f(x)=0$ 时, $y=0$ ；当 $f(x)<0$ 时, $y=-1$ 。

如图1-144所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-194.jpg?height=866&width=1533&top_left_y=341&top_left_x=310)
(e) 当 $n \leqslant f(x)<n+1$ 时, $y=n$ （ $n$ 为自然数）。如图1 - 145 所示.
其中图1 144及 1.145 均为黑粗线所示的图形。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-194.jpg?height=612&width=867&top_left_y=1507&top_left_x=229)

图 $1 \cdot 144$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-194.jpg?height=527&width=667&top_left_y=1504&top_left_x=1140)

图 1 －145
330. 已知函数 $y=f(x)$ 和 $y=g(x)$ 的图形，作下列函数的图形:
(a) $y=f(x)+g(x) ;(6) y=f(x) g(x) ;$
(в) $y=f[g(x)]$.

解 (a)利用图形相加法即得。
如图1.146所示。
（6）利用图形相乘法即得。

如图1.147所示。
（в）如图1.148所示。设 $P$ 点是 $O x$ 轴上横坐标为 $x$ 的点。通过 $P$ 点引铅直线。它和 $y=g(x)$ 的图形相交得 $Q$ 点（当然假定值 $P Q$ 在 $f(x)$ 的存在域内） $P Q=g(x)$ 。过 $Q$ 点引水平线，它与 $y=x$ 交于 $R$ 点，过 $R$ 作铅直线与 $O x$ 轴及 $y=f(x)$ 分别交于 $T$ 点及 $S$ 点，则 $O T=$ $T R=P Q=g(x)$ ，因而 $T S=f[g(x)]$ 。最后，把 $S$点向通过 $P$ 点的铅直线投影得 $M$ 点，此即函数 $y$ $=f[g(x)]$ 图形上的一点。至于该图形上的其它点，同法求得。但要注意，函数 $y=f[g(x)]$ 的存在域是满足不等式
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-195.jpg?height=650&width=843&top_left_y=446&top_left_x=1012)

图1.146
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-195.jpg?height=526&width=818&top_left_y=1202&top_left_x=1010)

图1.147
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-195.jpg?height=632&width=800&top_left_y=1820&top_left_x=1022)

图 1.148

$$
a \leqslant g(x) \leqslant b
$$

-的数 $x$ 的集合，式中 $[a, b]$ 是 $f(x)$ 的存在域。
利用图形的相加法，作下列函数的图形：
$331 . y=1+x+e^{x}$ 。
解 如图1.149 所示.
332. $y=(x+1)^{-2}+(x-1)^{-2}$

解 图形关于 $O y$ 轴对称。
如图1.150所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-196.jpg?height=772&width=732&top_left_y=1073&top_left_x=248)

图 1.149
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-196.jpg?height=606&width=892&top_left_y=1213&top_left_x=933)

图 1.150
333. $y=x+\sin x$.

解 如图1.151所示。

$$
P_{1} Q_{1}=P_{2} Q_{2}=\cdots=1
$$

334. $y=x+\operatorname{arctg} x$.

解 如图1.152所示，图中仅画了主值的一支，一般地，在平行线 $y=x+(2 k+1) \frac{\pi}{2}$ 及 $y=x+(2 k-1) \frac{\pi}{2}$ 之间 $(k$ $=0, \pm 1, \pm 2 \cdots$ ，有类似的一支。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-197.jpg?height=792&width=701&top_left_y=384&top_left_x=258)

图1.151
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-197.jpg?height=775&width=632&top_left_y=389&top_left_x=1072)

图1.152
335. $y=\cos x+\frac{1}{2} \cos 2 x+\frac{1}{3} \cos 3 x$.

解 图形关于 $O y$ 轴对称，且关于直线 $x=k \pi$ 对称。
周期为 $2 \pi$ 。如图 1.153 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-197.jpg?height=409&width=741&top_left_y=1646&top_left_x=612)

图1.153
336. $y=\sin x-\frac{1}{3} \sin 3 x+\frac{1}{5} \sin 5 x$.

解 图形关于原点对称, 周期为 $2 \pi$, 且有 $f(x+\pi)=-f$ $(x)$ ，故在 $[0,2 \pi]$ 内图形关于直线 $x=\pi$ 反对称"。因此，我们只需做出 $[0, \pi]$ 内的图形即可。

如图 1.154 所示.
*）即关于点 $\pi$ 对称，也称之为以 $\pi$ 为周期的反周期函数。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-198.jpg?height=553&width=909&top_left_y=563&top_left_x=619)

图1.154
337. $y=\sin ^{4} x+\cos ^{4} x$.

解 图形关于 $O y$ 轴对称。周期为 $\frac{\pi}{2}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-198.jpg?height=589&width=860&top_left_y=1407&top_left_x=238)

图1.155
338. $y=|1-x|+|1+x|$.

解 当 $-1 \leqslant x \leqslant 1$ 时， $y=2$ ；
当 $x<-1$ 时, $y=-2 x$;
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-198.jpg?height=752&width=689&top_left_y=1457&top_left_x=1152)

当 $x>1$ 时, $y=2 x$.
如图 1.156 所示.
339. $y=|1-x|-|1+x|$.

解 当 $-1 \leqslant x \leqslant 1$ 时， $y=-2 x$ ；
当 $x<-1$ 时， $y=2$ ；
当 $x>1$ 时， $y--2$ 。
如图1. 157 所示.
340. 作双曲线函数的图形：
(a) $y=\operatorname{ch} x$, 式中 $\operatorname{ch} x=\frac{1}{2}\left(e^{-4}+e^{-x}\right)$;
（6） $y=\operatorname{sh} x$ ；式中 $\operatorname{sh} x=\frac{1}{2}\left(e^{x}-e^{x}\right)$ ；
(B) $y=\operatorname{th} x$; 式中 $\operatorname{th} x=\frac{\operatorname{sh} x}{\operatorname{ch} x}$.

解 如图 1.158 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-199.jpg?height=701&width=692&top_left_y=1220&top_left_x=288)

图1.157
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-199.jpg?height=641&width=686&top_left_y=1247&top_left_x=1073)

困 1.158

利用图形的相乘法，作下列函数的图形：
341. $y=x \sin x$.

解 当 $x=k \pi(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ 。
图形关于 Oy 轴对称。
当 $x=\frac{\pi}{2}+2 k \pi$ 时， $y=x$ ；
又当 $x=\frac{3 \pi}{2}+2 k \pi$ 时， $y=-x$.

如图1.159 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-200.jpg?height=721&width=909&top_left_y=493&top_left_x=602)

图1.159
342. $y=x \cos x$.

解 图形关于原点对称。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-200.jpg?height=604&width=812&top_left_y=1494&top_left_x=702)

图1.160
当 $x=(2 k+1) \frac{\pi}{2}(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ ；
当 $x=2 k \pi$ 时, $y=x$ ；当 $x=(2 k+1) \pi$ 时， $y=-x$ 。
如图1.160所示.
343. $y=x^{2} \sin ^{2} x$.

194

解 只要将图形 $y=x \sin x$ 作出后，再按 329 题（a）的作法画出. 如图 1.161 所示.

其实，我们也可由下列几点画出该函数的图形：
$0 \leqslant y \leqslant x^{2} ;$
当 $x=k \pi(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ ；
当 $x=(2 k+1) \frac{\pi}{2}$ 时， $y=x^{2}$ 。
图形关于 $O y$ 轴对称。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-201.jpg?height=520&width=672&top_left_y=985&top_left_x=472)

图1.161
344. $y=\frac{\sin x}{1+x^{2}}$.

解 图形关于原点对称。
当 $x=k \pi(k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0 ;$
当 $x=\frac{3 \pi}{2}+2 k \pi$ 时， $y=-\frac{1}{1+x^{2}}$ ；
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-201.jpg?height=418&width=1046&top_left_y=2004&top_left_x=459)

图1.162

当 $x=\frac{\pi}{2}+2 k \pi$ 时, $y=\frac{1}{1+x^{2}}$.
当 $x \rightarrow \infty$ 时， $y \rightarrow 0$ 。
如图1.162所亦.
345. $y=e^{-x^{z}} \cos 2 x$.

解 因 $-e^{-x^{2}} \leqslant y \leqslant e^{-x^{2}}$ ，故图形在图形 $y-e^{-x^{2}}$ 及 $y=-e^{x^{2}}$ 之间。

如图 1.163 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-202.jpg?height=524&width=1003&top_left_y=983&top_left_x=521)

图1.163
346. $y=x \operatorname{sgn}(\sin x)$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-202.jpg?height=774&width=915&top_left_y=1666&top_left_x=553)

图1.164

## 解 图形关于 Oy 轴对称。

当 $x=k \pi(k=0, \pm 1, \pm 2 \kappa \cdots)$ 时， $y=0$ ；
当 $2 k \pi<x<(2 k+1) \pi$ 时， $y=x$ ；
当 $(2 k+1) \pi<x<(2 k+2) \pi$ 时,$y=-x$.
如图1.164所示.
347. $y=[x] \cdot|\sin \pi x|$.

解 当 $x=k(k=0, \pm 1, \pm 2, \cdots)$ 时 $+y=0 . \quad *$当 $n<x<n+1$ ( $n$ 为自然数)时， $y=n|\sin \pi x|$ 。如图1.165 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-203.jpg?height=824&width=1038&top_left_y=1073&top_left_x=543)

图1.165
348. $y=\cos x \cdot \operatorname{sgn}(\sin x)$.

解 图形关于原点对称. 周期为 $\pi$.
当 $x=k \pi(~ k=0, \pm 1, \pm 2, \cdots)$ 时， $y=0$ ；
当 $2 k \pi<x<(2 k+1) \pi$ 时, $y=\cos x$ ；
当（ $2 k+1$ ） $\pi<x<(2 k+2) \pi$ 时， $y=-\cos x$ 。
如图1.166所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-204.jpg?height=442&width=1133&top_left_y=430&top_left_x=490)

图1.166
349. 设

$$
f(x)=\left\{\begin{array}{l}
1-|x|, \text { 若 }|x| \leqslant 1 ; \\
0, \text { 若 } \mid x,>1 .
\end{array}\right.
$$

作函数
$y=f(x) f(a-x)$
当（a） $a=0,(6) a=1$,
(B) $a=2$ 时的图形.

解
(a) $y=f(x) f(-$
$\boldsymbol{x}$ ).
因为 $f(x)$ 为偶函数，
所以， $y=f^{2}(x)$ 。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-204.jpg?height=495&width=712&top_left_y=1232&top_left_x=1072)

图1.167

由函数 $f(x)$ 的定义易得
$y=\left\{\begin{array}{l}(1+x)^{2}, \text { 若 }-1 \leqslant x<0, \\ (1-x)^{2}, \text { 若 } 0 \leqslant x \leqslant 1, \\ 0, \text { 若 }|x|>1 .\end{array}\right.$
如图1.167所示.
（6） $y=f(x) \cdot f(1-x)$.
由函数 $f(x)$ 的定义易得
$y=\left\{\begin{array}{l}0, \text { 若 } x \leqslant 0, \\ x-x^{2}, \text { 若 } 0<x<1, \\ 0, \text { 若 } x \geqslant 1 .\end{array}\right.$
如图1.168所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-205.jpg?height=469&width=1131&top_left_y=699&top_left_x=451)

图1.168
(B) $y=f(x) f(2-x)$.

由 函数 $f(x)$ 的定义易得

$$
y=0 .
$$

如图1.169 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-205.jpg?height=344&width=504&top_left_y=1253&top_left_x=1253)

团1.169
350. 作函数 $y=x+$ $\sqrt{x} \operatorname{sgn}(\sin \pi x)$
的图形。
解 当 $2 k<x<$
$2 k+1(k=0,1$ ，
$2, \cdots$ )时， $\sin \pi x>0$,
$\operatorname{sgn}(\sin \pi x)=1$,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-205.jpg?height=553&width=726&top_left_y=1728&top_left_x=936)

图1.170

因而， $y=x+\sqrt{x}$ 。
而当 $2 k+1<x<2 k+2$ 时，

$$
y=x-\sqrt{x} .
$$

图1.170中系函数
$y=\sqrt{x} \operatorname{sgn}(\sin \pi x)$
的图形（黑粗线所示）。
其中在 $y=x$ 上的 一支系 $y=\sqrt{x}+x$ 的一段。

## 至于函数

$y=x+\sqrt{x} \cdot \operatorname{sgn}(\sin \pi x)$ 的图形如图 1.171 所示.
作函数

$$
y=\frac{1}{f(x)}
$$

的图形，设：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-206.jpg?height=715&width=901&top_left_y=1273&top_left_x=646)

图1.171
351. $f(x)=x^{2}\left(1-x^{2}\right)$.

解 $y=\frac{1}{x^{2}}+\frac{1}{1-x^{2}}$.
利用图形的相加法，将函数 $y=\frac{1}{x^{2}}$ 及 $y=\frac{1}{1-x^{2}}$ 的图形相加即得. 如图1.172所示.
352. $f(x)=x(1-x)^{2}$.

200

解 $y=\frac{1}{x(1-x)^{2}}=\frac{1}{x}+\frac{1}{1-x}+\frac{1}{(1-x)^{2}}$.
当 $x>0$ 时, $y>0$;
当 $x<0$ 时， $y<0$ 。
利用图形的相加法即得，如图 1.173 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-207.jpg?height=944&width=783&top_left_y=750&top_left_x=248)

图1.172
353. $f(x)=\sin ^{2} x$.

解 $y=\frac{1}{\sin ^{2} x}$ 是一
周期为 $\pi$ 的周期函数。

图形关于 $O y$ 轴
对称. 如图1.174所
示.
354. $f(x)=\ln x$.数.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-207.jpg?height=874&width=633&top_left_y=768&top_left_x=1037)

图1.173
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-207.jpg?height=618&width=900&top_left_y=1781&top_left_x=949)

图1.174

解 $y=\frac{1}{\ln x}$.
当 $0<x<1$ 时， $y$ 由 0 下降到一 $\infty$ ；
当 $1<x<+\infty$ 时， $y$ 由十 $+\infty$ 下降到 0 . 如图 1.175 所
示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-208.jpg?height=817&width=637&top_left_y=688&top_left_x=835)

图1.175
355. $f(x)=e^{x} \sin x$.

解 $y=e^{-x} \csc x$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-208.jpg?height=672&width=932&top_left_y=1754&top_left_x=582)

图1.176
因为 $|\csc x| \geqslant 1$, 所以

$$
|y| \geqslant e^{-x} .
$$

利用图形的相乘法即得. 如图 1.176 所示.
356. 设：

$$
f(u)=\left\{\begin{array}{l}
-1, \text { 若 }-\infty<u<-1 ; \\
u, \text { 若 }-1 \leqslant u \leqslant 1 ; \\
1, \text { 若 } 1<u<+\infty .
\end{array}\right.
$$

作复合函数

$$
y=f(u)
$$

的图形，其中 $u=2 \sin x$ 。
解 如图 1.177 所示。
当 $|x-k \pi| \leqslant \frac{\pi}{6}$ 时，
$y=2 \sin x ;$ 当 $\frac{\pi}{6}<|x-k \pi|$
$<\frac{5 \pi}{6}, y=(-1)^{k}(k=0, \pm$
$1, \pm 2, \cdots)$.
357. 设

$$
\begin{aligned}
& \varphi(x)=\frac{1}{2}(x+|x|) \text { 和 } \\
& \psi(x)=\left\{\begin{array}{l}
x, \text { 若 } x<0 ; \\
x^{2}, \text { 若 } x \geqslant 0 .
\end{array}\right.
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-209.jpg?height=409&width=709&top_left_y=1369&top_left_x=1062)

图1.177

作下列函数的图形：
(a) $y=\varphi[\varphi(x)] ; \quad$ (б) $y=\varphi[\psi(x)] ;$
(в) $y=\psi[\phi(x)] ; \quad$ (г) $y=\psi[\psi(x)]$.

解 (a) $\varphi(x)=\left\{\begin{array}{l}x, \text { 若 } x \geqslant 0 ; \\ 0, \text { 若 } x<0 .\end{array}\right.$
$\varphi[\varphi(x)]=\varphi(x)$ ，如图1.178所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-210.jpg?height=412&width=572&top_left_y=411&top_left_x=411)

图 1.178
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-210.jpg?height=435&width=572&top_left_y=388&top_left_x=1142)

图 1.179
（6） $\varphi[\psi(x)]=\left\{\begin{array}{l}x^{2}, \text { 若 } x \geqslant 0 ; \\ 0, \text { 若 } x<0 .\end{array}\right.$
如图1.179所示.
（в） $\varphi\lfloor\varphi(x)]=\left\{\begin{array}{l}x^{2}, \text { 若 } x \geqslant 0 ; \\ 0, \text { 若 } x<0 .\end{array}\right.$
如图1.179所示.
（Г） $\psi[\psi(x)]=\left\{\begin{array}{l}x^{4}, \text { 若 } x \geqslant 0 ; \\ x, \text { 若 } x<0 .\end{array}\right.$
如图1.180所示.
358. 设

$$
\varphi(x)=\left\{\begin{array}{l}
1, \text { 若 }|x| \leqslant 1 ; \\
0, \text { 若 }|x|>1 .
\end{array}\right.
$$

及

$$
\phi(x)=\left\{\begin{array}{l}
2-x^{2}, \text { 若 }|x| \leqslant 2 ; \\
2, \text { 若 }|x|>2 .
\end{array}\right.
$$

作函数：
(a) $y=\varphi[\varphi(x)]$;
(6) $y=\varphi[\psi(x)] ;$
(в) $=\psi[(\varphi(x)] ;$
(r) $y=\psi[\phi(x)]$ 的图形.

解 (a) $\varphi[\varphi(x)]=1$.
如图1.181所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-211.jpg?height=598&width=618&top_left_y=409&top_left_x=362)
（6） $\varphi[\psi(x)]=\varphi$ $[\psi(-x)]$ ，故图形关于 Oy 轴对称。

当 $0 \leqslant x<1$ 时， $\psi(x)=2-x^{2}$,
由于

$$
1<2-x^{2} \leqslant 2,
$$

所以， $[\phi(x)]=0$ 。

$$
\text { 当 } 1 \leqslant x \leqslant \sqrt{3}
$$

时， $\psi(x)=2-x^{2}$ ，由于

$$
-1 \leqslant 2-x^{2} \leqslant 1,
$$

所以， $\varphi[\phi(x)]=1$.

$$
\text { 当 } \sqrt{3}<x \leqslant 2
$$

时， $\psi(x)=2-x^{2}$ ，由于

$$
-2 \leqslant 2-x^{2}<-1
$$

所以， $\varphi[\phi(x)]=0$.
当 $x>2$ 时， $\psi(x)=2$ ，所以， $\varphi[\psi(x)]=0$ 。如图1.182所示.
(B) $\varphi[\phi(x)]=\left\{\begin{array}{l}1, \text { 若 }|x| \leqslant 1 ; \\ 2, \text { 若 }|x|>1 .\end{array}\right.$

如图1.183所示.
( 1 ) $\psi[\psi(x)]=\left\{\begin{array}{l}2-\left(2-x^{2}\right)^{2}, \text { 若 }|x| \leqslant 2 ; \\ -2, \text { 若 }|x|>2 .\end{array}\right.$
如图1.184所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-212.jpg?height=486&width=741&top_left_y=839&top_left_x=652)

图1.184
359. 由函数 $f(x)$ 定义于正数域 $x>0$ 内, 把 $f(x)$ 延拓到负数域 $x<0$ 内，使所得的函数为：（1）偶函数；（2）奇函数。设
（a） $f(x)=1-x ; \quad$ （6） $f(x)=2 x-x^{2}$ ；
(в) $f(x)=\sqrt{x} ; \quad$ (г) $f(x)=\sin x$;
（д） $f(x)=e^{x} ; \quad$ (е) $f(x)=\ln x$.
作出对应的函数的图形。
解（a）（1）当 $x<0$ 时，定义 $f(x)=1+x$ ，则 $f(x)$ 在整个数轴上为偶函数。
(2) 当 $x<0$ 时，定义 $f(x)=-(1+x)$ ，则 $f(x)$ 在整个数轴上为奇函数。

如图1.185所示.
（6）（1）当 $x<0$ 时，定 义 $f(x)=-2 x-x^{2}$ 即行；
(2) 当 $x<0$ 时，定义 $f(x)=2 x+x^{2}$ 既行.

如图1.186所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-213.jpg?height=567&width=1032&top_left_y=362&top_left_x=512)

图1.185
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-213.jpg?height=486&width=840&top_left_y=1079&top_left_x=548)

图1.186
（в）（1）当 $x<0$ 时，定义 $f(x)=\sqrt{-x}$ 即行；
（2）当 $x<0$ 时，定义 $f(x)=-\sqrt{-x}$ 即行。
如图1.187所示.
（ $\Gamma$ ）（1）当 $x<0$ 时，定义 $f(x)=-\sin x=|\sin x|$ 即行；
（2）当 $x<0$ 时，定义 $f(x)=\sin x$ 即行。
如图1.188所示.
（д）（1）当 $x<0$ 时，定义 $f(x)=e^{-x}$ 即行；
（2）当 $x<0$ 时，定义 $f(x)=-e^{-x}$ 即行。
（8）（1）当 $x<0$ 时，定义 $f(x)=\ln (-x)$ 即行；
(2) 当 $x<0$ 时, 定义 $f(x)=-\ln (-x)$ 即行.

如图 1.190 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-214.jpg?height=524&width=737&top_left_y=435&top_left_x=177)

图1.187
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-214.jpg?height=409&width=872&top_left_y=521&top_left_x=929)

图1.188

如图1.189 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-214.jpg?height=532&width=618&top_left_y=1250&top_left_x=225)

图 1.189
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-214.jpg?height=595&width=880&top_left_y=1230&top_left_x=925)

图 1.190
360. 确定下列函数的图形对于什么垂直轴对称：
（a） $y=a x^{2}+b x+c ;(6) y=\frac{1}{x^{2}}+\frac{1}{(1-x)^{2}}$ ；
(в) $y=\sqrt{a+x}+\sqrt{b-x} \quad(0<a<b) ;$
$(r) y=a+b \cos x$.
融（a） $y=a\left(x+\frac{b}{2 a}\right)^{2}+\frac{4 a c-b^{2}}{4 a}$, 它关于直线 $x=-\frac{b}{2 a}$
对称. （6）显然图形对于直线 $x=\frac{1}{2}$ 对称.
（B）显然图形对于直线 $x=\frac{b-a}{2}$ 对称.
（「）对于直线 $x=k \pi(~ k=0, \pm 1, \pm 2, \cdots)$ 对称。
361. 确定下列函数的图形的对称中心：
(a) $y=a x+b$;
（6） $y=\frac{a x+b}{c x+d}$;
(в) $y=a x^{3}+b x^{2}+c x+d ;$
( ) $y=\frac{1}{x-1}+\frac{1}{x-2}+\frac{1}{x-3}$;
（刀） $y=1+\sqrt[3]{x-2}$.

解 (a) 显然对称中心为 $\left(x_{0}, a x_{0}+b\right), x_{0}$ 任意。
（ 6 ）设对称中心为 $\left(x_{0}, y_{0}\right)$ ，则对充分大的 $x$ ，有 $y$ 便 $y+y_{0}=\frac{c\left(x+x_{0}\right)+b}{c\left(x+x_{0}\right)+d},-y+y_{0}=\frac{a\left(-x+x_{0}\right)+b}{c\left(-x+x_{0}\right)+d}$, 由 此易得 $x_{0}=-\frac{d}{c}, y_{0}=\frac{a}{c}$ 。
(в) 用类似于（6）的方法，可得对称中心为 $\left(x_{0}, y\right)$ ，其中 $x_{0}=-\frac{b}{3 a}, y_{0}=a x_{0}^{3}+b x_{0}^{2}+c x_{0}+d$.
（г）类似于（6），可得对称中心为（2,0）。
（д）类似于（6），可得对称中心为（2,1）。
362. 作周期函数的图形：
（a） $y=|\sin x| ; \quad$ （5） $y=\operatorname{sgncos} x ;$
（в） $y=f(x)$ ，其中 $f(x)=A \frac{x}{l}\left(2-\frac{x}{l}\right)$ ，假设 $0 \leqslant x \leqslant 2 l$
和 $f(x+2 l) \equiv f(x) ;$
(г) $y=[x]-2\left[\frac{x}{2}\right]$;
（） $y=(x)$ ，此处 $(x)$ 为从数 $x$ 至与它最近的整数间的距离.

解 (a) 如图 1.191 所示, 周期 $\pi$.
（6）如图1.192所示，周期 $2 \pi$ 。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-216.jpg?height=301&width=729&top_left_y=523&top_left_x=344)

图1. 191
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-216.jpg?height=358&width=903&top_left_y=786&top_left_x=899)

图1.192
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-216.jpg?height=412&width=812&top_left_y=1202&top_left_x=325)

图 1.193
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-216.jpg?height=387&width=872&top_left_y=1554&top_left_x=932)

图1.194
（B）当 $0 \leqslant x \leqslant 2 l$ 时，
由 $f(x)$ 的定义易䅞

$$
f(x+2 k l)=f(x)(k=0, \pm 1, \pm 2, \cdots)
$$

故知所给函数为以 $2 l$ 为周期的周期函数，它在 $[0,2 l]$ 内的图形为一拋物线，顶点为 $(l, A)$ 。如图 1.193 所示.
（r）周期为 $2^{*}$ ，如图1.194所示。
*) 原本该题为 $y=|x|-2\left[\frac{x}{2}\right]$, 当 $x \geqslant 0$ 时，它是以 2 为周期函数。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-217.jpg?height=563&width=1239&top_left_y=581&top_left_x=451)

国1.195
（д）周期为 1 ，如图 1.195 所示。
363. 证明：若函数 $y=f(x)(-\infty<x<+\infty)$ 的图形对于二垂直轴 $x=a$ 和 $x=b(b>a)$ 对称，则函数 $f(x)$ 为周期函数。
证 设 $x$ 为任一实数，则按倩设有

$$
f(a+x)=f(a-x) \text { 及 } f(b+x)=f(b-x) .
$$

在 $f(a+x)=f(a-x)$ 中将 $x$ 换成 $x+(b-a)$, 则得

$$
f(x+b)=f(a-x-b+a)=f(2 a-b-x) ;
$$

面 $f(x+b)=f(b-x)$, 所以

$$
f(b-x)=f(2 a-b-x) .
$$

将 $b-x$ 换成 $x$, 则得 $f(x)=f(2 a-2 b+x)$.
再将 $x$ 换成 $2(b-a)+x$, 即得

$$
f(x+2(b-a))=f(x),
$$

即 $f(x)$ 为一以 $2(b-a)$ 为周期的周期函数. 如图 1.196所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-218.jpg?height=602&width=968&top_left_y=307&top_left_x=541)

图 1.195
364. 证明: 若函数 $y=f(x)(-\infty<x<+\infty)$ 的图形对于两点 $A\left(a, y_{0}\right)$ 和 $B\left(b, y_{1}\right)(b>a)$ 对称，则函数 $f(x)$ 是线性函数与周期函数的和。特别是，若 $y_{0}=y_{1}$ ，则函数 $f(x)$ 是周期函数。
证 设 $x$ 是任一实数，按假设有：

$$
\begin{aligned}
& f(a+x)-y_{0}=y_{0}-f(a-x), \\
& f(b+x)-y_{1}=y_{1}-f(b-x) .
\end{aligned}
$$

在（1）中，将 $x$ 换成 $x+(b-a)$ 则得

$$
f(b+x)-y_{0}=y_{0}-f(2 a-b-x)
$$

将（3）代入（2）得

$$
2 y_{1}-f(b-x)=2 y_{0}-f(2 a-b-x),
$$

即

$$
f(b-x)=2\left(y_{1}-y_{0}\right)+f(2 a-b-x)
$$

在（4）中，将 $b-x$ 换成 $x$ ，则得

$$
f(x)=2\left(y_{1}-y_{0}\right)+f(2 a-2 b+x)
$$

再在（5）中将 $x$ 换成 $2(b-a)+x$ ，则得

$$
f(x)=2\left(y_{0}-y_{1}\right)+f[2(b-a)+x] .
$$

令

$$
f(x)=-\frac{y_{0}-y_{1}}{b-a} x+\varphi(x)
$$

下面证明 $\varphi(x)$ 一定是周期函数. 事实上，我们有

$$
\begin{aligned}
& f[x+2(b-a)]=-\frac{y_{0}-y_{1}}{b-a}[x+2(b-a)] \\
& \quad+\varphi(x+2(b-a)] \\
& f(x)-f[x+2(b-a)]=2\left(y_{0}-y_{1}\right)+\varphi(x) \\
& \quad-\varphi[x+2(b-a)] .
\end{aligned}
$$

因此由（5）式可得

$$
\varphi(x)=\varphi[x+2(b-a)] .
$$

由（6）式和（7）式可知， $f(x)$ 是一个线性函数与一个周期函数的和。

若 $y_{0}=y_{1}$ ，则由（6）式和（7）式可知， $f(x)$ 是一个周期函数。
365. 证明：若函数 $y=f(x)(-\infty<x<+\infty)$ 的图形关于点 $A$ $\left(a, y_{0}\right)$ 及直线 $x=b(b \neq a)$ 对称，则函数 $f(x)$ 是周期函数.
证 设 $x$ 为任一实数，按假设则有

$$
\begin{aligned}
& f(a+x)-y_{0}=y_{0}-f(a-x), \\
& f(b+x)=f(b-x) .
\end{aligned}
$$

在（1）中，将 $x$ 换戌 $x+(b-a)$ ，则得

$$
f(b+x)=2 y_{0}-f(2 a-b-x),
$$

即

$$
f(b-x)=2 y_{0}-f(2 a-b-x) .
$$

在（2）中，将 $b-x$ 换成 $\boldsymbol{x}$ ，则得

$$
f(x)=2 y_{0}-f(2 a-2 b+x) .
$$

在（3）中，将 $x$ 换成 $2 b-2 a+x$ ，则得

$$
f(2 b-2 a+x)=2 y_{0}-f(x)
$$

由 (3) (4) 得 $f(2 a-2 b+x)=f(2 b-2 a+x)$ ，再将 $x$ 换成 $2 b-2 a+x$ ，即得

$$
f(x)=f(4(b-a)+x) .
$$

此即证明 $f(x)$ 为一以 $4(b-a)$ 为周期的周期函数。
366. 设 $f(x+1)=2 f(x)$ 及当 $0 \leqslant x \leqslant 1$ 时, $f(x)=x(1-x)$,作函数

$$
y=f(x) \quad(-\infty<x<+\infty)
$$

的图形。
解 当 $0 \leqslant x \leqslant 1$ 时，图形为一抛物线，顶点为 $\left(\frac{1}{2}, \frac{1}{4}\right)$.当 $1 \leqslant x \leqslant 2$ 时，只要将级标放大 2 倍，余类推。如图1.197所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-220.jpg?height=301&width=1049&top_left_y=1340&top_left_x=555)

图1.197
当 $x=\frac{2 n+1}{2}$ 时， $y=\frac{2^{n}}{4}=2^{n-2}$ ，因而当 $n \rightarrow+\infty$ 时， $y$ $\rightarrow+\infty$ ；当 $n \rightarrow-\infty$ 时， $y \rightarrow 0$ 。
367. 设 $f(x+\pi)=f(x)+\sin x$; 且当 $0 \leqslant x \leqslant \pi$ 时, $f(x)=0$.作函数

$$
y=f(x)(-\infty<x<+\infty)
$$

的图形。

## 㓓 由题设知

当 $0 \leqslant x \leqslant \pi$ 时， $f(x)=0$ ；
当 $\pi<x \leqslant 2 \pi$ 时, 设 $0<x_{1} \leqslant \pi$, 则有

$$
f(x)=f\left(x_{1}+\pi\right)=f\left(x_{1}\right)+\sin x_{1}=\sin x_{1} ;
$$

当 $2 \pi<x \leqslant 3 \pi$ 时, 设 $\pi<x_{2} \leqslant 2 \pi$, 则有

$$
f(x)=f\left(x_{2}+\pi\right)=f\left(x_{2}\right)+\sin x_{2}=0 ;
$$

余类推. 周期为 $2 \pi$. 如图 1.198 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-221.jpg?height=275&width=983&top_left_y=793&top_left_x=205)

图1.198
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-221.jpg?height=452&width=546&top_left_y=665&top_left_x=1212)

目 1.199
368. 作函数 $y=y(x)$ 的图形，设：
$\begin{array}{ll}\text { (a) } x=y-y^{3} ; & \text { (6) } x=\frac{1-y}{1+y^{2}} ; \\ \text { (в) } x=y-\ln y ; & \text { (г) } x^{2}=\sin y .\end{array}$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-221.jpg?height=618&width=369&top_left_y=1710&top_left_x=361)

图 1.200
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-221.jpg?height=450&width=750&top_left_y=1865&top_left_x=713)

图1.201
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-221.jpg?height=938&width=360&top_left_y=1367&top_left_x=1462)

图 1.202

解 (a) 如图 1.199 所示.
（5）如图 1.200 所示.
(в) 如图1.201 所示.
（「）如图1.202所示。
369. 作出下列用参数表小的各函数的图形，设：
（a） $x=1-t, y=1-t^{2}$ ；
（6） $x=t+\frac{1}{t}, y=t+\frac{1}{t^{2}}$;
(в) $x=10 \cos t, y=\sin t$
（落圆）；
（г） $x=\operatorname{ch} t, y=\operatorname{sh} t$
（双曲线）；
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-222.jpg?height=375&width=655&top_left_y=715&top_left_x=1112)

图1.203
（д） $x=5 \cos ^{2} t, y=3 \sin ^{2} t$;
(e) $x=2(t-\sin t), y=2(1-\cos t)$ (摆线);
(ж) $x=\sqrt[x+1]{t}, y=\sqrt[t]{t+1}(t>0)$.

船 (a) $y-1=-(x-1)^{2}$ 。如图1.203所示.
（6）如图1.204 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-222.jpg?height=884&width=912&top_left_y=1571&top_left_x=526)
(B) $\frac{x^{2}}{10^{2}}+\frac{y^{2}}{1^{3}}=1$. 如图 1.205 所示.
（г） $x^{2}-y^{2}=1$. 如图 1.206 所示.
(д) $\frac{x}{5}+\frac{y}{3}=1$, 如图 1.207 所示.
(e) 如图 1.208 所示.
（※）如图1:209所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-223.jpg?height=329&width=1055&top_left_y=749&top_left_x=455)

图 1.205
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-223.jpg?height=547&width=846&top_left_y=1137&top_left_x=185)

图1.206
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-223.jpg?height=547&width=795&top_left_y=1137&top_left_x=1022)

固1.207
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-223.jpg?height=352&width=643&top_left_y=2143&top_left_x=335)

图 1.208
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-223.jpg?height=612&width=566&top_left_y=1896&top_left_x=1096)

图 1.209

## 370. 作下列隐函数的图形：

(a) $x^{2}-x y+y^{z}=1$ (植圆)；
（6） $x^{3}+y^{3} x y=0$ (笛卡尔叶形线)；
（в） $\sqrt{x}+\sqrt{y}=1$ (抛物线);
（г） $x^{\frac{2}{3}}+y^{\frac{3}{3}}=4$ (内摆线)；
(д) $\sin x=\sin y ;$
(e) $\cos \left(\pi x^{3}\right)=\cos (\pi y) ;$
(ж) $\dot{x}^{y}=y^{x}(x>0, y>0)$;
(a) $x-|x|=y-|y|$.

解（a）将坐标轴按正向绪原点旋转 $45^{\circ}$ ，得新坐标系 $O x^{\prime} y^{\prime}$ ，则由旋转公式得

$$
\begin{aligned}
& x=\frac{x^{\prime}-y^{\prime}}{\sqrt{2}}, \\
& y=\frac{x^{\prime}+y^{\prime}}{2} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-224.jpg?height=701&width=689&top_left_y=980&top_left_x=1069)

囯 1.210
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-224.jpg?height=565&width=595&top_left_y=1756&top_left_x=1133)

图 1.211

如图1.210所示.
（6）渐近线为 $x$ 十
$y+1=0$.
如图 1.211 所示。
(a) 如图 1.212 所示.
（「）如图1.213所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-225.jpg?height=515&width=566&top_left_y=516&top_left_x=431)

图 1.212
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-225.jpg?height=569&width=620&top_left_y=475&top_left_x=1072)

图 1.213
（） $y=x+2 k \pi$ 或 $y=(2 k+1) \pi-x$
（ $k=0, \pm 1, \pm 2, \cdots$ ）。如图1. 214 所示.
(e) $y=x^{2}+2 k$ 或 $y=2 k-x^{2}(k=0, \pm 1, \pm 2$,

如图1.215所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-225.jpg?height=650&width=712&top_left_y=1571&top_left_x=312)

图1.214
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-225.jpg?height=729&width=501&top_left_y=1503&top_left_x=1097)

固 1.215
（※）如图1.216所示. 参看 1544 题的作图法.
（e）如图1.217所示。图形包括第一象限阴影部分 （连同边界） $x \geqslant 0, y \geqslant 0$ 以及第三象限的黑粗线部分： $y$

$$
=x, x<0, y<0 .
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-226.jpg?height=521&width=709&top_left_y=542&top_left_x=294)

图1.216
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-226.jpg?height=598&width=640&top_left_y=452&top_left_x=1025)

图 1.217
371. 在极坐标 $(r), \varphi$ 系中作出函数 $r=r(\varphi)$ 的图形.设：
(a) $\mathrm{r}=\varphi$ (阿基米得紫线); $(6) \mathrm{r}=\frac{\pi}{\varphi}$ （双曲缐线）；
(в) $\mathrm{r}=\frac{\varphi}{\varphi+1}(0 \leqslant \varphi<+\infty) ;$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-226.jpg?height=73&width=595&top_left_y=1574&top_left_x=391)
(ㄱ) $\mathbf{r}=2(1+\cos \varphi$ ) (心脏形线);
(e)r $=10 \sin 3 \varphi($ 三無玫现线)；
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-226.jpg?height=455&width=655&top_left_y=1846&top_left_x=792)

图1.218
（※） $r^{2}=36 \cos 2 \varphi$ (贝努里双纽线）；
(3) $\varphi=\frac{r}{r-1}(r>1) ;(n) \varphi=2 \pi \sin r$.

解 (a) 如图 1.218 所示. $M_{1} M_{2}=M_{2} M_{3}=\cdots=2 \pi$.
（6）如图1.219所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-227.jpg?height=497&width=1166&top_left_y=671&top_left_x=456)

用 1.219
(B) 如图 1.220 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-227.jpg?height=646&width=941&top_left_y=1339&top_left_x=609)

图1.220
(r) 如图 1.221 所示.
(д) 如图 1.222 所示.
(e) 如图1.223所示.
（ж）如图1.224所示.
(3) 如图1.225 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-228.jpg?height=574&width=1427&top_left_y=363&top_left_x=248)

图 1.223

图1.221
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-228.jpg?height=643&width=872&top_left_y=1135&top_left_x=204)

图1.222
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-228.jpg?height=316&width=632&top_left_y=1007&top_left_x=1080)

图1.224
(u) 如图 1.226 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-228.jpg?height=440&width=1118&top_left_y=1973&top_left_x=503)

图 1.226
372. 作函数 $y=x^{3}-3 x+1$ 的图

222

形，以求方程式

$$
x^{3}-3 x+1=0
$$

的近似解。
解 如图 1.227 所示.
因 $\left.y\right|_{z=0}=1>0$ ，

$$
\left.y\right|_{x=0.4}=-0.136,
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-229.jpg?height=478&width=595&top_left_y=315&top_left_x=1207)

图 1.227

所以，在 0 与 0.4 之间有一实根，
约为 0.35 。
同法可求得其它二根为 1.53 及

- 1.88 。

用图旅法解下列方程式：
373. $x^{3}-4 x-1=0$.

解 作㓰数 $y=x^{3}$ 及 $y=4 x+1$
的图形，它们的交点的樓坐标即所求之根（图 1.228）。

在图示的根 $x_{0}$ 猞近研究雨
数 $f(x)=x^{2}-4 x-1$, 若 $f\left(x_{0}\right.$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-229.jpg?height=838&width=401&top_left_y=880&top_left_x=1376)
$-\delta) \cdot f\left(x_{0}+\delta\right)<0$ ，则根 $x_{0}$ 界
于 $x_{0}-\delta$ 及 $x_{0}+\delta$ 之问，其中 $\delta$ 为很小的某个正数。下列各题同。

经判别，根的近似解为

- 1. 86; - 0.25; 2.11.


## 374. $x^{4}-4 x+1=0$.

解：作函数 $y=x^{4}$ 及 $y=4 x-1$的图形。㚼图1.229所示.
交点的横坐标即所求之根，其近

图 1.228
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-229.jpg?height=712&width=498&top_left_y=1780&top_left_x=1344)

国

似 值为 $0.25 ; 1.49$ 。
375. $x=2^{-x}$ 。

解 作函数 $y=2^{-x}$ 及 $y=x$
的图形，如图1.230 所示。
交点的横坐标为 0.64 , 此
即所求之根的近似值。
376. $\lg x=0.1 x$.

解 作函数 $y=\lg x$ 及 $y=$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-230.jpg?height=529&width=641&top_left_y=432&top_left_x=1187)

国1.230
$0.1 x$ 的图形，如图 1.231 所示：
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-230.jpg?height=354&width=1044&top_left_y=1325&top_left_x=549)

图 1.231
交点的横坐标为 1.37 及 10 ，此即所求之根，前者为近似值，后者为栯确值。
377. $10^{x}=x^{2}$ 。

解 作函数 $y=10^{\circ}$ 及 $y=x^{2}$ 的
图形，如图1.232所示. 交点
的横坐标为 -0.54 , 此即所求之根的近似值。
378. $\operatorname{tg} x=x(0 \leqslant x \leqslant 2 \pi)$

粠 作函数
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-230.jpg?height=498&width=526&top_left_y=1958&top_left_x=1302)

图1.232

$$
y=\operatorname{tg} x \text { 及 } y=x
$$

的图形，如图1.233所示。
交点的横坐标为 0 及 4.49 ，此即所求之根，前者为精确值，后者为近似值。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-231.jpg?height=703&width=735&top_left_y=825&top_left_x=338)

图1.233
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-231.jpg?height=846&width=530&top_left_y=705&top_left_x=1254)

图1.234

用图解法以解下列方程组:
379. $x+y^{2}=1,16 x^{2}+y=4$.

解 作函数

$$
y^{2}=1-x \text { 及 }-y+4=16 x^{2}
$$

的图表，如图 1.234 所示。
交点为点 $A, B, C$ 及 $D$, 它们的一对坐标即所求之解 （近假值）：

$$
\begin{aligned}
& x_{1}=-0.42, y_{1}=1.19 \text { ( } A \text { 点) } \\
& x_{2}=0.45, y_{2}=0.74(B \text { 点) } \\
& x_{3}=0.54, y_{3}=-0.68(C \text { 点 })_{4} \\
& x_{4}=-0.57, y_{4}=1.25 \text { (D 点). }
\end{aligned}
$$

380. $x^{2}+y^{2}=100, y=10\left(x^{2}-x-2\right)$.

解 作画数

$$
x^{2}+y^{2}=100
$$

及 $y=10\left(x^{2}-x-2\right)$
的图形，如图1.235所示。
交点为点 $A, B, C$ 及 $D$,
它们的一对坐标即所求之
解 (近似值):

$$
\begin{aligned}
& x_{1}=-1.30 ; \\
& y_{1}=9.92(A \text { 点); } \\
& x_{2}=2.30, \\
& y_{2}=9.73(B \text { 点 }) ; \\
& x_{3}=1.62, \\
& y_{3}=-9.87(C \text { 点 }) ; \\
& x_{4}=-0.62, y_{4}=-9.98(D \text { 点 }) .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-232.jpg?height=800&width=649&top_left_y=565&top_left_x=1160)

国1.235

## §5. 函数的极限

$1^{*}$ 画数的有界性 投存在有某两数 $m$ 和 $M$ ，使得
当 $x \in(a, b)$ 时， $m<f(x)<M$ ，
则积固数 $f(x)$ 在这区间 $(a, b)$ 上为有界的。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-232.jpg?height=92&width=1471&top_left_y=2144&top_left_x=318)而数 $M_{0}=\operatorname{suc}_{x \in(a, b)}\{f(x)\}$ 称为西数 $f(x)$ 在这区间 $(a, b)$ 上的上嗩界.

差 $M_{0}-m_{0}$ 称为函数在区间 $(a, b)$ 上的振幅。
$2^{2}$ 画数在基一点的极限 符号

$$
\lim _{x} f(x)=A
$$

表示对千任一个数 $\varepsilon>0$ ，都存在有数 $\delta=\delta(t)>0$ ，使得对于满足条件式 $0<|x-a|<\delta$ ，并使 $f(x)$ 有意义的一切 $x$ ，有下列不等式成立：

$$
\{f(x)-A\}<E .
$$

涵数的极限（1）存在的必要而且充分的条件量：对于每一个叙列 $x_{\text {。 }}$ $\rightarrow a(n=1,2, \cdots)$ ，下佂的等式都成立

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=A .
$$

有两本著名的极限：
(1) $\lim _{x \rightarrow 0} \frac{\sin x}{x}=1$
(2) $\lim _{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$

哥西判别佉. 通数 $f(x)$ 在 $a$ 点的极限存在，当而且仅当，对于毎一个 $\varepsilon>0$ ，都能找得着 $\delta=\delta(\varepsilon)>0$ ，使得，只要是
$0<\left|x^{\prime}-a\right|<\delta$ 和 $0<\left|x^{\prime \prime}-a\right|<\delta$,
就有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon .
$$

式中 $x^{\prime}$ 和 $x^{\prime \prime}$ 是居于函数 $f(x)$ 的定义域内的。
$3^{\circ}$ 单你的揫限 若
当 $0<a-x<\delta(E)$ 时，有 $\left|A^{\prime}-f(x)\right|<E$ ，则称数 $A^{\prime}$ 为函数 $f(x)$ 在 $a$ 点的左极限：

$$
A^{\prime}=\lim _{x \rightarrow-6} f(x)=f(a-0)
$$

同样, 若 当 $0<x-a<b(\varepsilon)$ 时, 有 $\left|A^{\prime \prime}-f(x)\right|<\epsilon$, 则称数 $A^{\prime \prime}$为函数 $f(x)$ 在 $a$ 点的右敬限：

$$
A^{x}=\lim _{x \rightarrow+\infty} f(x)=f(a+0)
$$

函数 $f(x)$ 在 $a$ 点的极硍存在的必要而且充分的条件为：

$$
f(a-0)=f(a+0)
$$

$4^{\circ}$ 无穷极限 符号

$$
\lim _{x \rightarrow e} f(x)=\infty
$$

表示对于任何的 $E>0$ ，只要是
$0<|x-a|<\delta(E)$, 则有 $|f(x)|>E$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-234.jpg?height=78&width=992&top_left_y=378&top_left_x=326)

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=B
$$

则称数（或符号 $\infty$ ） $B$ 为函数 $f(x)$ 在 $a$ 点的子烈模限（有穷的或无穷的).

这些子列极限中最小的和最大的用

$$
\varliminf_{x \rightarrow a} f(x) \text { 和 } \lim _{x \rightarrow a} f(x)
$$

来表示，分别称为函数 $f(x)$ 在 $a$ 点的下极限和上极限。

$$
\lim _{x=1} f(x)=\lim _{x \rightarrow 0} f(x)
$$

为函数 $f(x)$ 在 $a$ 点有极限（有穷的或无穷的）的必要而且充分的条件. 381. 函数 $f(x)$ 由下面的条件所定义：

若

$$
x=\frac{m}{n} \text {, 则 } f(x)=n \text {, }
$$

式中 $m$ 和 $n$ 为互质的整数，且 $n>0$ ；
若 $x$ 为无理数，则

$$
f(x)=0
$$

证明此函数在每一点 $x$ 为有穷的，但并非有界的（即在这点的任何猞域中是无界的）。
证 - 任给 $x_{0}>0$ ，当 $x_{0}$ 固定时， $f\left(x_{0}\right)$ 值确定。由于有理数在数轴上处处椆密，故在 $x_{0}$ 的任何邻域 $\left(x_{0}-\delta, x_{0}+\right.$ $\delta$ ）内总有无限多个有理数。下面证明对于任给的 $\delta>0$ ，函数 $f(x)$ 在区间（ $x_{0}-\delta, x_{0}+\delta$ ）内是无界的。若不然，存在 $M>0$, 使当 $x \in\left(x_{0}-\delta, x_{0}+\delta\right)$ 时,

$$
|f(x)| \leqslant M .
$$

于是，在 $\left(x_{0}-\delta, x_{0}+\delta\right)$ 中的有理数只能表示成

$$
\frac{k}{1}, \frac{k}{2}, \cdots, \frac{k}{[M]} .
$$

其中 $k$ 是与分母互质的整数， $[M]$ 为 $M$ 的整数部分。由

于这些有理数都在 $\left(x_{6}-\delta, x_{0}+\delta\right)$ 中，故有

$$
\left(x_{0}-\delta\right)[M]<k<\left(x_{0}+\delta\right)[M],
$$

上式表明在 $\left(x_{0}-\delta, x_{0}+\delta\right)$ 中的有理数仅为有限个, 这与有理数在数轴上的处处椆密性相矛盾。

于是，本题所定义的函数 $f(x)$ 在每一点 $x$ (有穷) 的任何邻域中是无界的。
382. 若函数 $f(x)$ 在：（a）开区间，(6) 闲区间内的每一点确定而有界，则此函数在这给定的区间内或对应的闭区间内是否为有界的？

举出适当的例子。
解 （a）一般地说，不一定。例如，函数 $f(x)=\frac{1}{x}$ 在 $(0$, 1) 内每一点确定而有界，但它在 $(0,1)$ 内无界。
(6) 是有界的. 事实上, 若 $f(x)$ 在 $[a, b]$ 无界, 则存在 $x_{n} \in[a, b]$ 使 $\lim _{n \rightarrow \infty} f\left(x_{n}\right)=\infty$ 。取子列 $x_{x_{k}} \rightarrow x_{0} \in[a$, $b]$. 显然， $f(x)$ 在 $x_{0}$ 无界（即在 $x_{b}$ 的任何猞域中无界），矛盾.
383. 证明函数 $f(x)=\frac{1+x^{2}}{1+x^{4}}$

在间隔 $-\infty<x<+\infty$ 中是有界的。
证 当 $|x| \leqslant 1$ 时， $|f(x)|<\frac{1+1}{1}=2$ 。
当 $|x|>1$ 时, $|f(x)|<\frac{1+x^{2}}{1+x^{4}}<1$.
因而，当 $-\infty<x<+\infty$ 时， $|f(x)|<2$ 。即函数 $f(x)$是有界的。
384. 证明函数

$$
f(x)=\frac{1}{x} \cos \frac{1}{x}
$$

在点 $x=0$ 的任何邻域内是无界的，但当 $x \rightarrow 0$ 时不成为无穷大。
证 当 $x=\frac{2}{(2 k+1) \pi}$ 时, $f(x)=0$ ；而当 $x=\frac{1}{k \pi}$ 时， $f(x)=(-1)^{*} k \pi$ 。于是当 $k \rightarrow \infty$ 时, 点 $\frac{2}{(2 k+1) \pi}$ B $\frac{1}{k \pi}$均在点 $x=0$ 的任何邻域内。由于 $\left|(-1)^{k} \cdot k \pi\right| \rightarrow+$ $\infty(k \rightarrow+\infty)$ ，故菡数 $f(x)$ 在点 $x=0$ 的任何邻域内是无界的。然而当 $k \rightarrow \infty$ 时， $f(x)$ 不断地与 $O x$ 轴相交，即 $f(x)=0$ (这样的数 $x$ 的集合是无限的)。因而，当 $x \rightarrow 0$时， $f(x)$ 又不成为无穷大。
385. 研究函数 $f(x)=\ln x \cdot \sin ^{2} \frac{\pi}{x}$ 在区间 $0<x<\varepsilon$ 内的有界性。
解 上方有界，它小于 |lne|. 下方无界。

## 386. 证明函数

$$
f(x)=\frac{x}{1+x}
$$

在域 $0 \leqslant x<+\infty$ 内有下确界 $m_{0}=0$ 和上确界 $M_{0}=1$.
亚 $1>f(x) \geqslant 0$, 且 $f(x)$ 单调上升趋近于 1 , 所以,

$$
m_{0}=0, M_{0}=1 .
$$

387. 函数 $f(x)$ 在闭区间 $[a, b]$ 上有定义且单调上升, 则在此闲区间内函数的下碚界和上确界等于什么？
解 $m_{0}=f(a), M_{0}=f(b)$ ，其中 $m_{0}$ 及 $M_{0}$ 代表下确界及上确界，以下各题均采用此符号。
求函数的下确界和上确界：
388. $f(x)=x^{2}$ 在 $(-2,5)$ 内.

解 $m_{0}=0, M_{0}=25$.
389. $f(x)=\frac{1}{1+x^{2}}$ 在 $(\cdots \infty,+\infty$ ) 內.

解 $m_{0}=0, M_{0}=1$ 。
390. $f(x)=\frac{2 x}{1+x^{2}}$ 在 $(0,+\infty)$ 内。

解 由于 $f(x)$ 在 $(0,1)$ 内为增函数，而在（ $1,+\infty$ ）内为减函数，且 $f(1)$ 存在，所以，

$$
m_{0}=0, M_{0}=f(1)=1
$$

391. $f(x)=x+\frac{1}{x}$ 在 $(0,+\infty)$ 内.

解 由 $x+\frac{1}{x} \geqslant 2$ 知 $m_{0}=f(1)=2, M_{0}=+\infty$. 392. $f(x)=\sin x$ 在 $(0,+\infty$ ) 内.

解 $m_{0}=-1, M_{0}=1$.
393. $f(x)=\sin x+\cos x$ 在 $[0,2 \pi]$ 内.

解 由 $f(x)=\sqrt{2} \sin \left(x+\frac{\pi}{4}\right)$ 知 $m_{0}=-\sqrt{2}, M_{0}=$ $\sqrt{2}$.
394. $f(x)=2^{x}$ 在 $(-1,2)$ 内.

稦 $m_{0}=f(-1)=\frac{1}{2} ; M_{0}=f(2)=4$.
395. $f(x)=[x]:(a)$ 在 $(0,2)$ 内, (6) 在 $[0,2]$ 内.

解（a） $m_{0}=0, M_{0}=1$ ；
(б) $m_{0}=0, M_{0}=2$.
396. $f(x)=x-[x]$ 在 $[0,1]$ 内.

$$
\text { 解 } m_{0}=1, M_{0}=1 .
$$

397. 求狰数 $f(x)=x^{2}$ 在下列区 间内的振幅：
(a) $(1,3)$;
(б) $(1.9,2.1)$;
(B) $(1.99,2,01$ )
(г) (1. 999,2.001).
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-238.jpg?height=78&width=1080&top_left_y=475&top_left_x=331)
因为 $m_{0}=1, M_{0}=9$ ，所以

$$
\omega=8
$$

(6) $\begin{aligned} m_{0} & =(1.9)^{2}, M_{0}=(2.1)^{2}, \\ \omega & =(2.1)^{2}-(1.9)^{2}=0.8 .\end{aligned}$
(в) $\omega=(2.01)^{2}-(1.99)^{2}=0.08$.
$(\Gamma) \omega=(2.001)^{2}-(1.999)^{2}=0.008$.
398. 求函数

$$
f(x)=\operatorname{arctg} \frac{1}{x}
$$

在下列区间内的振幅：
(а) $(-1,+1)$ ；（6）（ $-0.1,0.1) ;$
(в) $(-0.01,0.01) ;(г)(-0.001,0.001)$.

解（（日） $\omega=\frac{\pi}{2}-\left(-\frac{\pi}{2}\right)=\pi$ ；
(6) $\boldsymbol{\omega}=\boldsymbol{\pi}$;
(в) $\omega=\pi$ ；
(r) $\omega=\pi$.
399. 设 $m[f]$ 和 $M[f]$ 分别为函数 $f(x)$ 在区间 $(a, b)$ 内的下确界和上确界。
证明若 $f_{1}(x)$ 和 $f_{2}(x)$ 为定义于 $(a, b)$ 内的函数，
则

$$
m\left[f_{1}+f_{2}\right] \geqslant m\left[f_{1}\right]+m\left[f_{2}\right]
$$

及

$$
M\left[f_{1}+f_{2}\right] \leqslant M\left[f_{1}\right]+M\left[f_{2}\right] .
$$

举出函数 $f_{1}(x)$ 和 $f_{2}(x)$ 的例子，使它们在最后的二关

系中是：（a）等式的情形，（6）不等式的情形。
证 因为

$$
m\left[f_{1}\right] \leqslant f_{1} \leqslant M\left[f_{1}\right]
$$

及

$$
m\left[f_{2}\right] \leqslant f_{z} \leqslant M\left[f_{2}\right],
$$

所以,

$$
m\left[f_{1}\right]+m\left[f_{2}\right] \leqslant f_{1}+f_{2},
$$

从而有

$$
m\left[f_{1}\right]+m\left[f_{z}\right] \leqslant m\left[f_{1}+f_{z}\right] .
$$

又因

$$
f_{1}+f_{z} \leqslant M\left[f_{1}\right]+M\left[f_{2}\right],
$$

所以，

$$
M\left[f_{1}+f_{2}\right] \leqslant M\left[f_{1}\right]+M\left[f_{2}\right] .
$$

(a) 当 $f_{1}(x)$ 及 $f_{2}(x)$ 在 $(a, b)$ 内具有相同的单调性, 且 $m$ 及 $M$ 均为有限时，取等式。
(6) $f_{1}(x)=x^{2}, f_{2}(x)=-x^{2}$ 在区间 $(-1,1)$ 内

$$
\begin{gathered}
m\left[f_{1}\right]=0, M\left[f_{1}\right]=1 \\
m\left[f_{z}\right]=-1, M\left[f_{2}\right]=0 .
\end{gathered}
$$

又因为 $f_{1}+f_{2}=0$, 所以

$$
m\left[f_{1}+f_{2}\right]=M\left[f_{1}+f_{2}\right]=0
$$

此时

$$
\begin{aligned}
& m\left[f_{1}+f_{2}\right]>m\left[f_{1}\right]+m\left[f_{2}\right] \\
& M\left[f_{1}+f_{2}\right]<M\left[f_{1}\right]+M\left[f_{2}\right] .
\end{aligned}
$$

取不等式的符号。
400. 设函数 $f(x)$ 定义于域 $[a,+\infty)$ 内, 并且在每一个闭区

间 $[a, b]$ 上是有界的. 假定

$$
\begin{aligned}
& m(x)=\inf _{\text {es }} f(\xi)
\end{aligned}
$$

作函数 $y=m(x)$ 和 $y=M(x)$ 的图形，设

$$
\text { (a) } f(x)=\sin x, \quad \text { (6) } f(x)=\cos x
$$

緦 (a) 如图1.236 所示. (6) 加图1.236所示
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-240.jpg?height=698&width=1055&top_left_y=962&top_left_x=495)

图1.236

## 401. 利用 $(\varepsilon-\delta$ 》 论证法, 证明

$$
\lim _{x \rightarrow 2} x^{2}=4
$$

填下表：

| $\varepsilon$ | 0.1 | 0.01 | 0.001 | 0.0001 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ |  |  |  |  |  |

证 $\quad\left|x^{2}-4\right|=|x-2||x+2|$.
先限制 $|x-2|<1$ ，期 $1<x<3$ ，则
$\left|x^{2}-4\right|=|x-2||x+2|<5|x-2|$.

取 $\delta=\min \left\{1, \frac{E}{5}\right\}$ 。于是，当 $0<|x-2|<\delta$ 的，

$$
\left|x^{2}-4\right|<\varepsilon
$$

即

$$
\lim _{x \rightarrow 2} x^{2}=4
$$

| $\varepsilon$ | 0.1 | 0.01 | 0.001 | 0.0001 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ | 0.02 | 0.002 | 0.0002 | 0.00002 | $\cdots$ |

## 402. 以 $4 E-\delta$ 》的说法, 证明

$$
\lim _{x \rightarrow 1} \frac{1}{(1-x)^{2}}=+\infty .
$$

填下表：

| $E$ | 10 | 100 | 1000 | 10000 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ |  |  |  |  | $\cdots$ |

证 任合 $E>0$ ，
要使 $\frac{1}{|1-x|^{2}}>E$ ，
只要 $0<|x-1|<\frac{1}{\sqrt{E}}$,
又只要 $0<|x-1|<\frac{1}{E}(E>1)$,
取 $\delta=\min \left\{1, \frac{1}{E}\right\}$ ，
则当 $0<|x-1|<\delta$ 时，

$$
\left|\frac{1}{(1-x)^{2}}\right|>E,
$$

所以

$$
\lim _{x \rightarrow 1} \frac{1}{(1-x)^{2}}=+\infty
$$

| $E$ | 10 | 100 | 1000 | 10000 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ | 0.1 | 0.01 | 0.001 | 0.0001 | $\cdots$ |

403. 利用不等式表示下列各式：
(a) $\lim _{x \rightarrow a} f(x)=b$;
(6) $\lim _{x \rightarrow a-0} f(x)=b$;
(B) $\lim _{x \rightarrow a+0} f(x)=b$.

举出适当的例子。
解 (a) 对于任给的 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<1 x-$ $a \mid<\delta$ 时，

$$
|f(x)-b|<\varepsilon,
$$

此即

$$
\lim _{x \rightarrow a} f(x)=b .
$$

例如, $f(x)=x+1, \lim _{x \rightarrow 1} f(x)=2$.
（6）对于任给的 $\varepsilon>0$ ，存在数 $\delta>0$ ，使当 $0<a-x<$ $\delta$ 时,

$$
|f(x)-b|<\varepsilon,
$$

此即

$$
\lim _{x \rightarrow-0} f(x)=b .
$$

例如，

则

$$
\text { 若 } f(x)=\left\{\begin{array}{l}
x+1, \text { 当 } x \leqslant 1 ; \\
2, \text { 当 } x>1,
\end{array}\right.
$$

(B) 对于任给的 $\epsilon>0$, 存在数 $\delta>0$ ，使当 $0<x-a<$ $\delta$ 时

$$
|f(x)-b|<\varepsilon,
$$

此即

$$
\lim _{x \rightarrow a+a} f(x)=b
$$

例如本题（6）之例，即有

$$
\lim _{x \rightarrow 1+0} f(x)=2
$$

利用不等式表示下列各式，并举出适当的例子：
404. (a) $\lim _{x \rightarrow \infty} f(x)=b$ ；
(6) $\lim _{x \rightarrow-\infty} f(x)=b ;$
(в) $\lim _{x \rightarrow+\infty} f(x)=b$.

解（a）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
|f(x)-6|<\varepsilon
$$

此即

$$
\lim _{x \rightarrow \infty} f(x)=b .
$$

（6）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $x<-N$ 时，

$$
|f(x)-b|<\varepsilon
$$

此即

$$
\lim _{x \rightarrow-\infty} f(x)=b
$$

(B) 任给 $\mathrm{E}>0$ ，存在数 $N>0$ ，使当 $x>N$ 时，

$$
|f(x)-b|<\varepsilon
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=b
$$

例如，对于函数 $f(x)=\frac{1}{x^{2}}$ ，即有

$$
\lim _{x \rightarrow-\infty} f(x)=\lim _{x \rightarrow+\infty} f(x)=\lim _{x \rightarrow \infty} f(x)=0
$$

405. (a) $\lim _{x \rightarrow+} f(x)=\infty ;$
(5) $\lim _{x \rightarrow 4} f(x)=\infty$;
(B) $\lim _{x \rightarrow a} f(x)=+\infty$;
(г) $\lim _{x \rightarrow-0} f(x)=\infty$;
(д) $\lim _{x \rightarrow-\infty} f(x)=-\infty$ ；
(e) $\lim _{x \rightarrow-0} f(x)=+\infty$;
(ж) $\lim _{x \rightarrow a+0} f(x)=\infty$;
(и) $\lim _{x \rightarrow+0} f(x)=+\infty$.

䉽 (a) 任给 $E>0$, 存在数 $\delta>0$ ，使当 $0<|x-a|<\delta$时，

$$
|f(x)|>E,
$$

此即

$$
\lim _{x \rightarrow a} f(x)=b
$$

例如, $f(x)=\frac{1}{x-1}$, 即有

$$
\lim _{x \rightarrow 1} f(x)=\infty
$$

（6）任给 $E>0$ ，存在数 $\delta>0$ ，使当 $0<|x-\alpha|<\delta$ 时，

$$
f(x)<-E,
$$

此即

$$
\lim _{x \rightarrow 0} f(x)=-\infty
$$

例如， $f(x)=\frac{-1}{(x-1)^{2}}$ ，即有

$$
\lim _{x \rightarrow 1} f(x)=-\infty
$$

(B) 任给 $E>0$, 存在数 $\delta>0$, 使当 $0<|x-a|<\delta$ 时,

$$
f(x)>E .
$$

此期

$$
\lim _{x \rightarrow a} f(x)=+\infty .
$$

例如， $f(x)=\frac{1}{(x-1)^{2}}$ ，即有

$$
\lim _{x \rightarrow 1} f(x)=+\infty
$$

( $r$ ) 任给 $E>0$ ，存在数 $\delta>0$ ，使当 $0<a-x<\delta$ 时，

$$
|f(x)|>E .
$$

此即

$$
\lim _{x \rightarrow-0} f(x)=\infty .
$$

例如, $f(x)=\frac{(-1)}{\left.1-\frac{1}{[ } \frac{1}{1} x\right]}$, 即有

$$
\lim _{x \rightarrow 1+0} f(x)=\infty
$$

（д）任给 $E>0$ ，存在数 $\delta>0$ ，使当 $0<a-x<\delta$ 时， $f(x)<-E$,
此即 $\lim _{x \rightarrow-0} f(x)=-\infty$.

例如， $f(x)=\frac{1}{x-1}$ ，即有

$$
\lim _{x \rightarrow 1-0} f(x)=-\infty .
$$

(e) 任给 $E>0$, 存在数 $\delta>0$, 使当 $0<a-x<\delta$ 时, $f(x)>E$,
此耶

$$
\lim _{x \rightarrow-\infty} f(x)=+\infty .
$$

例如, $f(x)=\frac{1}{1-x}$, 即有

$$
\lim _{x \rightarrow-1-0} f(x)=+\infty .
$$

（ж）任给 $E>0$ ，存在数 $\delta>0$ ，使当 $0<x-a<\delta$ 时，

$$
|f(x)|>E .
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=\infty,
$$

例如， $f(x)=\frac{(-1)^{\left[\frac{1}{x-1}\right]}}{x-1}$ ，即有

$$
\lim _{x \rightarrow 1+\infty} f(x)=\infty .
$$

(a) 任给 $E>0$, 存在数 $\delta>0$, 使当 $0<x-a<\delta$ 时，

$$
f(x)<-E,
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=-\infty .
$$

例如， $f(x)=\frac{1}{1-x}$ ，即有

$$
\lim _{x \rightarrow 1+0} f(x)=-\infty .
$$

(H) 任给 $E>0$, 存在数 $\delta>0$, 使当 $0<x-a<\delta$ 时, $f(x)>E$,
此即

$$
\lim _{x \rightarrow+\infty} f(x)=+\infty .
$$

例如， $f(x)=\frac{1}{x-1}$ ，即有

$$
\lim _{x \rightarrow 1+0} f(x)=+\infty
$$

406. (a) $\lim _{x \rightarrow \infty} f(x)=\infty$
(B) $\lim _{x \rightarrow \infty} f(x)=+\infty$;
(r) $\lim _{x \rightarrow-\infty} f(x)=\infty$;
(д) $\lim _{x \rightarrow-\infty} f(x)=-\infty$;
(e) $\lim _{x \rightarrow \infty} f(x)=+\infty$;
(ж) $\lim _{x \rightarrow+\infty} f(x)=\infty$;
(и) $\lim _{x \rightarrow+\infty} f(x)=+\infty$.

解 （a）任给 $E>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
|f(x)|>E,
$$

此即

$$
\lim _{x \rightarrow \infty} f(x)=\infty
$$

例如， $f(x)=x^{2}$ ，则有 $\lim _{x \rightarrow \infty} f(x)=\infty$ 。
（6）任给 $E>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
f(x)<-E,
$$

此即

$$
\lim _{x \rightarrow \infty} f(x)=-\infty
$$

例如, $f(x)=-x^{2}$, 即有

$$
\lim _{x \rightarrow \infty} f(x)=-\infty
$$

（B）任给 $E>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
f(x)>E,
$$

此即

$$
\lim _{x \rightarrow \infty} f(x)=+\infty
$$

例如， $f(x)=x^{2}$ ，即有

$$
\lim _{x \rightarrow \infty} f(x)=+\infty .
$$

（「）任给 $E>0$ ，存在数 $N>0$ ，使当 $x<-N$ 时，

$$
|f(x)|>E,
$$

此即

$$
\lim _{x \rightarrow \infty} f(x)=\infty .
$$

例如, $f(x)=(-1)^{\left[x^{2}\right]} x$, 即有

$$
\lim _{x \rightarrow \infty} f(x)=\infty .
$$

（）任给 $E>0$ ，传在数 $N>0$ ，使当 $x<-N$ 时，

$$
f(x)<-E,
$$

此即

$$
\lim _{x \rightarrow-\infty} f(x)=-\infty .
$$

例如, $f(x)=x$, 即有

$$
\lim _{x \rightarrow-\infty} f(x)=-\infty
$$

（e）任给 $E>0$ ，存在数 $N>0$ ，使当 $x<-N$ 时，

$$
f(x)>E,
$$

此即

$$
\lim _{x \rightarrow-\infty} f(x)=+\infty .
$$

例如, $f(x)=-x$, 即有

$$
\lim _{x \rightarrow \infty} f(x)=+\infty
$$

（ж）任给 $E>0$ ，存在数 $N>0$ ，使当 $x>N$ 时，

$$
|f(x)|>E,
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=\infty .
$$

例如, $f(x)=(-1)^{[x]} x^{2}$, 即有

$$
\lim _{x \rightarrow+\infty} f(x)=\infty
$$

(9) 任给 $E>0$, 存在数 $N>0$, 使当 $x>N$ 时,

$$
f(x)<-E,
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=-\infty .
$$

例如, $f(x)=-x$, 即有

$$
\lim _{x \rightarrow+\infty} f(x)=-\infty
$$

（ $\boldsymbol{1}$ ）任给 $E>0$ ，存在数 $N>0$ ，使当 $x>N$ 时，

$$
f(x)>E,
$$

此即

$$
\lim _{x \rightarrow+\infty} f(x)=+\infty
$$

例如， $f(x)=x$ ，即有

$$
\lim _{x \rightarrow+\infty} f(x)=+\infty
$$

407. 命 $y=f(x)$. 利用不等式表示下列各情况：
（a）当 $x \rightarrow a$ 时， $y \rightarrow b-0$;
（5）当 $x \rightarrow a-0$ 时， $y \rightarrow b-0$ ；
（в）当 $x \rightarrow a+0$ 时， $y \rightarrow b-0$ ；
（ r ）当 $x \rightarrow a$ 时， $y \rightarrow b+0$ ；
（д）当 $x \rightarrow a-0$ 时， $y \rightarrow b+0$ ；
(e) 当 $x \rightarrow a+0$ 时， $y \rightarrow b+0$ ；
（*）当 $x \rightarrow \infty$ 时， $y \rightarrow b-0$ ；
（a）当 $x \rightarrow-\infty$ 时， $y \rightarrow b-0$ ；
(u) 当 $x \rightarrow+\infty$ 时， $y \rightarrow b-0_{\text {， }}$
（к）当 $x \rightarrow+\infty$ 时 $y \rightarrow b+0$ ；
（л）当 $x \rightarrow-\infty$ 时， $y \rightarrow b+0_{4}$
（м）当 $x \rightarrow+\infty$ 时， $y \rightarrow+0$ 。

## 举出适当的例子。

解 (a) 任给 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<|x-a|<$ $\delta$ 时,

$$
0<b-y<\varepsilon,
$$

㽖即

$$
\lim _{x \rightarrow a} f(x)=b-0
$$

或
当 $x \rightarrow a$ 时， $y \rightarrow b-0$ 。
例如， $y=-|x|$ ，即有
当 $x \rightarrow 0$ 时， $y \rightarrow 0-0$ 。
（6）任给 $\varepsilon>0$ ，存在数 $\delta>0$ ，使当 $0<a-x<\delta$ 时，

$$
0<b-y<\varepsilon,
$$

此即

$$
\lim _{x \rightarrow a-0} f(x)=b-0 .
$$

例如， $y=x$ ，即有

$$
\text { 当 } x \rightarrow 0-0 \text { 时, } \quad y \rightarrow 0-0 \text {. }
$$

(B) 任给 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<x-a<\delta$ 时,

$$
0<b-y<\varepsilon,
$$

此即, 当 $x \rightarrow a+0$ 时, $y \rightarrow b-0$.
例如， $y=-x$ ，即有

$$
\text { 当 } x \rightarrow 0+0 \text { 时, } y \rightarrow 0-0 \text {. }
$$

(r) 任给 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<|a-x|<\delta$ 时,

$$
0<y-b<\varepsilon,
$$

此即，当 $x \rightarrow a$ 时， $y \rightarrow b+0$ 。
例如， $y=|x|$ ，即有

$$
\text { 当 } x \rightarrow 0 \text { 时, } y \rightarrow 0+0 \text {. }
$$

(д) 任给 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<a-x<\delta$ 时,

$$
0<y-b<\varepsilon_{\text {, }}
$$

此即，当 $x \rightarrow a-0$ 时， $y \rightarrow b+0$ 。
例如, $y=-x$, 即有

$$
\text { 当 } x \rightarrow 0-0 \text { 时, } y \rightarrow 0+0 \text {. }
$$

(e) 任给 $\varepsilon>0$, 存在数 $\delta>0$, 使当 $0<x-a<\delta$ 时,

$$
0<y-b<\varepsilon,
$$

此即，当 $x \rightarrow a+0$ 时， $y \rightarrow b+0$ 。
例如, $y=x$, 即有

$$
\text { 当 } x \rightarrow 0+0 \text { 时, } y \rightarrow 0+0 \text {. }
$$

（※）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
0<b-y<\varepsilon
$$

此即，当 $x \rightarrow \infty$ 时， $y \rightarrow b-0$ 。
例如， $y=-\frac{1}{|x|}$ ，即有

$$
\text { 当 } x \rightarrow \infty \text { 时, } y \rightarrow 0-0 \text {. }
$$

（a）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $x<-N$ 时，

$$
0<b-y<\varepsilon,
$$

此即，当 $x \rightarrow-\infty$ 时， $y \rightarrow b-0$ 。
例如， $y=\frac{1}{x}$ ，即有

$$
\text { 当 } x \rightarrow-\infty \text { 时, } y \rightarrow 0-0 \text {. }
$$

（и）任给 $\epsilon>0$ ，存在数 $N>0$ ，使当 $x>N$ 时，

$$
0<b-y<\varepsilon,
$$

此即，当 $x \rightarrow+\infty$ 时， $y \rightarrow b-0$ 。
例如， $y=-\frac{1}{x}$ ，即有

$$
\text { 当 } x \rightarrow+\infty, y \rightarrow 0-0 \text {. }
$$

（н）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $|x|>N$ 时，

$$
0<y-b<\varepsilon,
$$

此即，当 $x \rightarrow \infty$ 时， $y \rightarrow b+0$ 。
例如， $y=\frac{1}{|x|}$ ，即有

$$
\text { 当 } x \rightarrow \infty \text { 时, } y \rightarrow 0+0 \text {. }
$$

（л）任给 $\varepsilon>0$ ，存在数 $N>0$ ，使当 $x<-N$ 时，

$$
0<y-b<\varepsilon,
$$

此即，当 $x \rightarrow-\infty$ 时， $y \rightarrow b+0$ 。
例如， $y=-\frac{1}{x}$ ，即有
当 $x \rightarrow-\infty$ 时， $y \rightarrow 0+0$ 。
（м）任给 $\varepsilon>0$, 存在数 $N>0$, 使当 $x>N$ 时,

$$
0<y-b<\varepsilon,
$$

此即, 当 $x \rightarrow+\infty$ 时, $y \rightarrow b+0$.
例如， $y=\frac{1}{x}$ ，即有

$$
\text { 当 } x \rightarrow+\infty \text { 时, } y \rightarrow 0+0 \text {. }
$$

408. 设

$$
p(x)=a_{0} x^{n}+a_{1} x^{a-1}+\cdots+a_{r},
$$

式中 $a_{i}(i=0,1, \cdots, n)$ 为实数.
证明 $\lim _{x \rightarrow \infty}|p(x)|=+\infty$ 。
证 不妨设 $a_{0} \neq 0$, 则

$$
\begin{aligned}
& |p(x)| \geqslant\left|a_{0}\right| \cdot\left|x^{2}\right| \cdot \left\lvert\, 1-\left(\frac{\left|a_{1}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|}\right.\right. \\
& \left.+\frac{\left|a_{2}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|^{2}}+\cdots+\frac{\left|a_{n}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|^{2}}\right) \mid,
\end{aligned}
$$

由于 $\lim _{x \rightarrow \infty} \frac{1}{|x|^{i}}=0(i=1,2, \cdots, n)$, 故存在 $E_{1}>0$, 使当 $|x|>E_{1}$ 时, 恒有

$$
\begin{array}{|l}
\mid 1 \\
\left|-\left(\frac{\left|a_{1}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|}+\frac{\left|a_{2}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|^{2}}+\cdots+\frac{\left|a_{n}\right|}{\left|a_{0}\right|} \cdot \frac{1}{|x|^{n}}\right)\right| \\
\\
>-\frac{1}{2}
\end{array}
$$

从而有

$$
|p(x)|>\frac{1}{2}\left|a_{0}\right| \cdot|x|^{*} .
$$

任合 $M>0$ ，设

$$
E_{2}=\sqrt[n]{\frac{2 M}{\left|a_{0}\right|}}
$$

取

$$
E=\max \left(E_{1}, E_{1}\right),
$$

则当 $|x|>E$ 时，恒有

$$
|p(x)|>M
$$

故

$$
\lim _{x \rightarrow \infty}|p(x)|=+\infty
$$

409. 设：

$$
R(x)=\frac{a_{0} x^{n}+a_{1} a^{n-1}+\cdots+a_{n}}{b_{0} x^{m}+b_{1} x^{m-1}+\cdots b_{m}}
$$

式中 $a_{0} \neq 0, b_{0} \neq 0$ 。
证明：

$$
\lim _{x \rightarrow \infty} R(x)=\left\{\begin{array}{l}
\infty, \text { 若 } n>m ; \\
\frac{a_{0}}{b_{0}}, \text { 若 } n=m ; \\
0, \\
\text { 若 } n<m .
\end{array}\right.
$$

证 分子分母同除以 $x^{*}$ ，得

$$
R(x)=\frac{a_{0} x^{-n}+a_{1} x^{-n-1}+\cdots+a_{n} x^{-m}}{b_{0}+b_{1} x^{-1}+\cdots+b_{m} x^{-m}}
$$

当 $n>m$ 时，分子趋干无穷，分母趋于 $b_{0}$ ，所以，

$$
\lim _{x \rightarrow \infty} R(x)=\infty
$$

当 $n=m$ 时,分子趋干 $a_{0}$, 分母㤘于 $b_{0}$, 所以,

$$
\lim _{x \rightarrow \infty} R(x)=\frac{a_{0}}{b_{0}}
$$

当 $n<m$ 时，分子㑇于 0 ，分母趋于 $b_{0}$ ，所以，

$$
\lim _{x \rightarrow \infty} R(x)=0
$$

410. 设：

$$
R(x)=\frac{P(x)}{Q(x)}
$$

式中 $P(x)$ 和 $Q(x)$ 为 $x$ 的多项式，且

$$
P(a)=Q(a)=0 .
$$

下式有什么可能的值

$$
\lim _{x \rightarrow a} \frac{P(x)}{Q(x)} ?
$$

解 若 $a$ 仅为 $P(x)=0$ 及 $Q(x)=0$ 的一重根，则极限

$$
\lim _{x \rightarrow 4} \frac{P(x)}{Q(x)}
$$

为一确定值（不等于零）。
若 $a$ 为 $P(x)=0$ 的 $n$ 重根，而为 $Q(x)=0$ 的 $m$ 重根，则当 $n>m(n, m$ 均大于 1$)$ 时，此极限为 0 ；当 $n<m$时，此极限为 $\infty$ ；当 $n=m$ 时，此极限为一不等手零的值.

总之，极限

$$
\lim _{x \rightarrow 4} \frac{P(x)}{Q(x)}
$$

为零，或为 $\infty$ ，或为不等于零的值。
求下列各式之值：
411.
（a） $\lim _{x \rightarrow 9} \frac{x^{2}-1}{2 x^{2}-x-1}$ ；(6) $\lim _{x \rightarrow 1} \frac{x^{2}-1}{2 x^{2}-x-1}$
(B) $\lim _{x \rightarrow \infty} \frac{x^{2}-1}{2 x^{2}-x-1}$

解 (a) $\lim _{x \rightarrow 0} \frac{x^{2}-1}{2 x^{2}-x-1}=\frac{-1}{-1}=1$.
(6) $\lim _{x \rightarrow 1} \frac{x^{2}-1}{2 x^{2}-x-1}=\lim _{x \rightarrow 1} \frac{(x-1)(x+1)}{(2 x+1)(x-1)}$

$$
=\lim _{x \rightarrow 1} \frac{x+1}{2 x+1}=\frac{2}{3} .
$$

(B) $\lim _{x \rightarrow \infty} \frac{x^{2}-1}{2 x^{2}-x-1}=\lim _{x \rightarrow \infty} \frac{1-\frac{1}{x^{2}}}{2-\frac{1}{x}-\frac{1}{x^{2}}}=\frac{1}{2}$.
412. $\lim _{x \rightarrow 0} \frac{(1+x)(1+2 x)(1+3 x)-1}{x}$.

解 $(1+x)(1+2 x)(1+3 x)=1+6 x+11 x^{2}+6 x^{3}$ ，
于是，

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{(1+x)(1+2 x)(1+3 x)-1}{x} \\
& \quad=\lim _{x \rightarrow 0}\left(6+11 x+6 x^{2}\right)=6 .
\end{aligned}
$$

413. $\lim _{x \rightarrow 0} \frac{(1+x)^{5}-(1+5 x)}{x^{2}+x^{5}}$.

蛼 $\lim _{x \rightarrow 0} \frac{(1+x)^{5}-(1+5 x)}{x^{2}+x^{5}}$
$=\lim _{x \rightarrow 0} \frac{x^{5}+5 x^{4}+10 x^{3}+10 x^{2}}{x^{2}+x^{5}}$
$=\lim _{x \rightarrow 0} \frac{x^{3}+5 x^{2}+10 x+10}{x^{3}+1}$
$=10$.
414. $\lim _{x \rightarrow 0} \frac{(1+m x)^{2}-(1+n x)^{-}}{x^{2}}(m$ 与 $n$ 为自然数 .

解 $\frac{(1+m x)^{\prime \prime}-(1+n x)^{m}}{x^{2}}$
$=\frac{\left[1+n m x+\frac{1}{2!} n(n-1) m^{2} x^{2}+\cdots+m^{n} x^{\prime \prime}\right]}{x^{2}}$
$+\frac{-\left[1+m n x+\frac{1}{2!} m(m-1) n^{2} x^{2}+\cdots+n^{m} x^{m}\right]}{x^{2}}$
$=\frac{n}{2}(n-1) m^{2}-\frac{m}{2}(m-1) n^{2}+o(x) \cdot "$
$=\frac{1}{2} m n(n-m)+o(x)$.
于是，

$$
\lim _{x \rightarrow 0} \frac{(1+m x)^{n}-(1+n x)^{m}}{x^{2}}=\frac{1}{2} m n(n-m)
$$

* $30(x)$ 表示当 $x \rightarrow 0$ 时的无穷小量。

415. $\lim _{x \rightarrow \infty} \frac{(x-1)(x-2)(x-3)(x-4)(x-5)}{(5 x-1)^{5}}$.

解 分子的最高次方为 5 次，分母的最高次方也为 5次，园而当 $x \rightarrow \infty$ 时，此分式的极限为分子与分母的最高次方系数之比，于基
$\lim _{x \rightarrow \infty} \frac{(x-1)(x-2)(x-3)(x-4)(x-5)}{(5 x-1)^{5}}=\frac{1}{5^{5}}$.
416. $\lim _{x \rightarrow \infty} \frac{(2 x-3)^{20}(3 x+2)^{30}}{(2 x+1)^{50}}$.

解 分子与分母的最高次方相同，故

$$
\lim _{x \rightarrow \infty} \frac{(2 x-3)^{20}(3 x+2)^{30}}{(2 x+1)^{50}}=\frac{2^{20} \cdot 3^{30}}{2^{50}}=\left(\frac{3}{2}\right)^{30}
$$

417. $\lim _{x \rightarrow \infty} \frac{(x+1)\left(x^{2}+1\right) \cdots\left(x^{n}+1\right)}{\left[(n x)^{n}+1\right]^{\frac{x+1}{2}}}$.

## 解 分子的最高次方为

$$
1+2+\cdots+n=\frac{n(n+1)}{2}
$$

它与分母的最高次方相同，所以

$$
\lim _{x \rightarrow \infty} \frac{(x+1)\left(x^{2}+1\right) \cdots\left(x^{n}+1\right)}{\left[(n x)^{n}+1\right]^{\frac{n+1}{2}}}=n^{-\frac{n(x+1)}{2}}
$$

418. $\lim _{x \rightarrow 3} \frac{x^{2}-5 x+6}{x^{2}-8 x+15}$.

解 $\lim _{x \rightarrow 3} \frac{x^{2}-5 x+6}{x^{2}-8 x+15}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 3} \frac{(x-3)(x-2)}{(x-3)(x-5)} \\
& =\lim _{x \rightarrow 3} \frac{x-2}{x-5}=-\frac{1}{2} .
\end{aligned}
$$

419. $\lim _{x \rightarrow 1} \frac{x^{3}-3 x+2}{x^{4}-4 x+3}$.

解 $\lim _{x \rightarrow 1} \frac{x^{3}-3 x+2}{x^{4}-4 x+3}$

$$
=\lim _{x \rightarrow-1} \frac{(x-1)^{2}(x+2)}{(x-1)^{2}\left(x^{2}+2 x+3\right)}
$$

$$
=\lim _{x \rightarrow 1} \frac{x+2}{x^{2}+2 x+3}=\frac{1}{2} .
$$

420. $\lim _{x \rightarrow 1} \frac{x^{3}-3 x+2}{x^{4}-x^{3}-x+1}$.

解 $\lim _{x \rightarrow 1} \frac{x^{3}-3 x+2}{x^{4}-x^{3}-x+1}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 1} \frac{(x-1)^{2}(x+2)}{(x-1)^{2}\left(x^{2}+x+1\right)} \\
& =\lim _{x \rightarrow 1} \frac{x+2}{x^{2}+x+1}=1 .
\end{aligned}
$$

*) 原书 419 题与 420 题相同.
421. $\lim _{x \rightarrow 2} \frac{x^{3}-2 x^{2}-4 x+8}{x^{4}-8 x^{2}+16}$.

解 $\lim _{s \rightarrow 2} \frac{x^{3}-2 x^{2}-4 x+8}{x^{4}-8 x^{2}+16}$
$=\lim _{x \rightarrow 2} \frac{(x-2)^{2}(x+2)}{(x-2)^{2}(x+2)^{2}}$
$=\lim _{x \rightarrow 2} \frac{1}{x+2}=\frac{1}{4}$.
422. $\lim _{x \rightarrow-1} \frac{x^{3}-2 x-1}{x^{5}-2 x-1}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow-1} \frac{x^{3}-2 x-1}{x^{5}-2 x-1} \\
= & \lim _{x \rightarrow-1} \frac{(x+1)\left(x^{2}-x-1\right)}{(x+1)\left(x^{4}-x^{3}+x^{2}-x-1\right)} \\
= & \lim _{x \rightarrow-1} \frac{x^{2}-x-1}{x^{4}-x^{3}+x^{2}-x-1}=\frac{1}{3} .
\end{aligned}
$$

423. $\lim _{x \rightarrow 2} \frac{\left(x^{2}-x-2\right)^{20}}{\left(x^{3}-12 x+16\right)^{10}}$.

解 $\lim _{x \rightarrow 2} \frac{\left(x^{2}-x-2\right)^{20}}{\left(x^{3}-12 x+16\right)^{10}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 2} \frac{(x-2)^{20}(x+1)^{20}}{(x-2)^{20}(x+4)^{10}} \\
& =\lim _{x \rightarrow 2} \frac{(x+1)^{20}}{(x+4)^{10}} \\
& =\frac{3^{20}}{6^{10}}=\left(\frac{3}{2}\right)^{10} .
\end{aligned}
$$

424. $\lim _{x \rightarrow 1} \frac{x+x^{2}+\cdots+x^{4}-n}{x-1}$.

解 $x+x^{2}+\cdots+x^{2}-n$

$$
\begin{aligned}
= & (x-1)+\left(x^{2}-1\right)+\cdots+\left(x^{n}-1\right) \\
= & (x-1)[1+(x+1)+\cdots \\
& \left.+\left(x^{*-1}+x^{n-2}+\cdots+1\right)\right] \\
= & (x-1)\left[n+(n-1) x+(n-2) x^{2}\right. \\
& \left.+\cdots+x^{n-1}\right] .
\end{aligned}
$$

于是，

$$
\begin{aligned}
\lim _{x \rightarrow 1} & \frac{x+x^{2}+\cdots+x^{n}-n}{x-1} \\
& =\lim _{x \rightarrow 1}\left[n+(n-1) x+(n-2) x^{2}+\cdots+x^{n-1}\right] \\
& =n+(n-1)+(n-2)+\cdots+1 \\
& =\frac{n(n+1)}{2} .
\end{aligned}
$$

425. $\lim _{x \rightarrow 1} \frac{x^{m}-1}{x^{*}-1}$ （ $m$ 和 $n$ 为自然数）。

晖 $\lim _{x \rightarrow 1} \frac{x^{m}-1}{x^{x}-1}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 1} \frac{x^{m-1}+x^{m-2}+\cdots+x+1}{x^{n-1}+x^{n-2}+\cdots+x+1} \\
& =\frac{m}{n}
\end{aligned}
$$

426. $\lim _{x \rightarrow a} \frac{\left(x^{*}-a^{*}\right)-n a^{*-1}(x-a)}{(x-a)^{2}} \quad(n$ 表自然数).

艶 设 $x=a+y$, 则当 $x \rightarrow a$ 时, $y \rightarrow 0$.
代入，得

$$
\begin{aligned}
& \lim _{x \rightarrow a} \frac{\left(x^{n}-a^{n}\right)-n a^{n-1}(x-a)}{(x-a)^{2}} \\
& =\lim _{y \rightarrow 0} \frac{(a+y)^{n}-a^{n}-n a^{n-1} y}{y^{2}} \\
& =\lim _{y \rightarrow 0}\left[\frac{n}{2}(n-1) a^{n-2}+\frac{1}{3!} n(n-1)(n-2) a^{n-3} y\right. \\
& \left.\quad+\cdots+y^{n-2}\right] \\
& = \\
& =\frac{n(n-1)}{2} a^{n-2} .
\end{aligned}
$$

427. $\lim _{x \rightarrow 1} \frac{x^{n+1}-(n+1) x+n}{(x-1)^{2}}$ ( $n$ 表自然数).

解 设 $x=1+y$, 则当 $x \rightarrow 1$ 时， $y \rightarrow 0$ 。代入，得

$$
\begin{aligned}
& \lim _{x \rightarrow 1} \frac{x^{n+1}-(n+1) x+n}{(x-1)^{2}} \\
& =\lim _{y \rightarrow 0} \frac{(1+y)^{n+1}-(n+1)(1+y)+n}{y^{2}} \\
& =\lim _{y \rightarrow 0}\left[\frac{n(n+1)}{2}+\frac{1}{3!}(n+1) n(n-1) y+\cdots+y^{-1}\right) \\
& =\frac{n(n+1)}{2} .
\end{aligned}
$$

428. $\lim _{x \rightarrow 1}\left(\frac{m}{1-x^{m}}-\frac{n}{1-x^{*}}\right)$ （ $m$ 租 $n$ 为自然数）。

解 当 $m=n$ 时, 此极限显然为零。
当 $m \neq n$ 时，不失一般性，假设 $m<n$ ，且

$$
m+l=n .
$$

此时

$$
\begin{aligned}
& \frac{m}{1-x^{m}}-\frac{n}{1-x^{n}} \\
& =\frac{m\left(1+x+\cdots+x^{n-1}\right)-n\left(1+x+\cdots+x^{m-1}\right)}{(1-x)\left(1+x+x^{2}+\cdots+x^{m-1}\right)\left(1+x+\cdots+x^{n-1}\right)} \\
& =\frac{-l-l x-\cdots-l x^{m-1}+m x^{m}+m x^{m+1}+\cdots+m x^{m+l-1}}{(1-x)\left(1+x+\cdots+x^{n-1}\right)\left(1+x+\cdots+x^{m+l+1}\right)} \\
& =-\frac{m x^{m+1-2}+2 m x^{m+i-3}+\cdots+m l x^{m-1}}{\left(1+x+\cdots+x^{-1}\right)\left(1-x+\cdots+x^{m+l-1}\right)} \\
& \quad-\frac{+l(m-1) x^{m-2}+l(m-2) x^{m-3}+\cdots+l}{\left(1+x+\cdots+x^{m-1}\right)\left(1+x+\cdots+x^{m+l-1}\right)} .
\end{aligned}
$$

于是,

$$
\begin{aligned}
& \lim _{x \rightarrow 1}\left(\frac{m}{1-x^{m}}-\frac{n}{1-x^{n}}\right) \\
& =-\frac{m[1+2+\cdots+(l-1)]+l[m+(m-1)+\cdots+1]}{m n} \\
& =-\frac{\frac{m l(l-1)}{2}+\frac{m l(m+l)}{2}}{m n}=-\frac{m l(m+l)}{2 m n} \\
& =\frac{m-n}{2} .
\end{aligned}
$$

当 $m=n$ 时, 上述结果就等于零. 即上述结果对 $m=n$ 的情况仍然适用。

总之，不论 $m$ 及 $n$ 为任何的自然数，均有

$$
\lim _{x \rightarrow 1}\left(\frac{m}{1-x^{m}}-\frac{n}{1-x^{n}}\right)=\frac{m-n}{2} .
$$

429. $\lim _{n \rightarrow \infty} \frac{1}{n}\left[\left(x+\frac{a}{n}\right)+\left(x+\frac{2 a}{n}\right)+\cdots+\left(x+\frac{(n-1) a}{n}\right)\right]$.

解 $\lim _{n \rightarrow \infty} \frac{1}{n}\left(\left(x+\frac{a}{n}\right)+\left(x+\frac{2 a}{n}\right)+\cdots+\left(x+\frac{(n-1) a}{n}\right)\right)$
$=\lim _{n \rightarrow \infty} \frac{1}{n}\left\{(n-1) x+\frac{a}{n}(1+2+\cdots+(n-1)]\right\}$
$=\lim _{n \rightarrow \infty} \frac{n-1}{n}\left(x+\frac{a}{2}\right)$
$=x+\frac{a}{2}$.
430. $\lim _{n \rightarrow \infty} \frac{1}{n}\left[\left(x+\frac{a}{n}\right)^{2}+\left(x+\frac{2 a}{n}\right)^{2}+\cdots+\left(x+\frac{(n-1) a}{n}\right)^{2}\right)$.

解 $\lim _{n \rightarrow \infty} \frac{1}{n}\left(\left(x+\frac{a}{n}\right)^{2}+\left(x+\frac{2 a}{n}\right)^{2}+\cdots\right.$

$$
\left.+\left(x+\frac{(n-1) a}{n}\right)^{2}\right)
$$

$=\lim _{n \rightarrow \infty} \frac{1}{n}\left\{(n-1) x^{2}+\frac{2 a x}{n}(1+2+\cdots+(n-1))\right.$

$$
\left.+\frac{a^{2}}{n^{2}}\left[1^{2}+2^{2}+\cdots+(n-1)^{2}\right]\right\}
$$

$=\lim _{n \rightarrow \infty} \frac{1}{n}\left\{(n-1) x^{2}+\frac{n-1}{1} a x+\frac{(n-1)(2 n-1)}{6 n} a^{2}\right\}$
$=x^{2}+a x+\frac{a^{2}}{3}$.
431. $\lim _{n \rightarrow \infty} \frac{1^{2}+3^{2}+\cdots+(2 n-1)^{2}}{2^{2}+4^{2}+\cdots+(2 n)^{2}}$.

解 $1^{2}+3^{2}+\cdots+(2 n-1)^{2}=\frac{n}{3}\left(4 n^{2}-1\right)$,

$$
2^{2}+4^{2}+\cdots+(2 n)^{2}=\frac{2 n(n+1)(2 n+1)}{3}
$$

于是,

$$
\lim _{n \rightarrow \infty} \frac{1^{2}+3^{2}+\cdots+(2 n-1)^{2}}{2^{2}+4^{2}+\cdots+(2 n)^{2}}=\lim _{n \rightarrow \infty} \frac{2 n-1}{2(n+1)}=1
$$

254
432. $\lim _{n \rightarrow \infty}\left(\frac{1^{3}+2^{3}+\cdots+n^{3}}{n^{3}}-\frac{n}{4}\right)$.

$$
\text { 解 } \begin{aligned}
& \lim _{n \rightarrow \infty}\left(\frac{1^{3}+2^{3}+\cdots+n^{3}}{n^{3}}-\frac{n}{4}\right) \\
= & \lim _{n \rightarrow \infty}\left(\frac{n^{2}(n+1)^{2}}{4 n^{3}}-\frac{n}{4}\right)^{*} \\
= & \lim _{n \rightarrow \infty} \frac{2 n+1}{4 n}=\frac{1}{2} .
\end{aligned}
$$

*）利用 3 题及 1 题的结果。
433. $\lim _{n \rightarrow \infty} \frac{1^{3}+4^{3}+7^{3}+\cdots+(3 n-2)^{3}}{[1+4+7+\cdots+(3 n-2)]^{2}}$.

解 令

$$
\begin{aligned}
& 1^{3}+4^{3}+7^{3}+\cdots+(3 n-2)^{3}=x_{n} \\
& {[1+4+7+\cdots+(3 n-2))^{2}=y_{n}}
\end{aligned}
$$

则 $y_{n+1}>y_{n}$, 且 $y_{n} \rightarrow+\infty$, 由于

$$
\begin{aligned}
& \frac{x_{n+1}-x_{n}}{y_{n+1}-y} \\
&= \frac{(3 n+1)^{3}}{(1+4+7+\cdots+(3 n+1)]^{2}-(1+4+7+\cdots+(3 n-2)]^{2}} \\
&= \frac{(3 n+1)^{3}}{\left[\frac{(1+n)(3 n+2)}{2}+\frac{n(3 n-1)}{2}\right](3 n+1)} \rightarrow 3 \\
&(n \rightarrow \infty) .
\end{aligned}
$$

利用 143 题的结果即得
$\lim _{n \rightarrow \infty} \frac{1^{3}+4^{3}+7^{3}+\cdots+(3 n-2)^{3}}{[1+4+7+\cdots+(3 n-2)]^{2}}=3$.
434. 把由抛物线 $y=b\left(\frac{x}{a}\right)^{2}, O x$ 轴及直线 $x=a$ 所围成的曲边三角形 $O A M$ （图 1. 237）的面积，当作以 $\frac{a}{n}$为底的各内接矩形面积之和当 $n \rightarrow \infty$ 的极限值，求此面积。
解 底的 $n$ 个分点为
$0, \frac{a}{n}, \frac{2 a}{n}, \cdots, \frac{n-1}{n} a$ ；
它们所对应的高为
$0, b\left(\frac{1}{n}\right)^{2}, b\left(\frac{2}{n}\right)^{2}, \cdots$,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-262.jpg?height=635&width=621&top_left_y=505&top_left_x=1177)
$b\left|\frac{n-1}{n}\right|^{2}$.
于是, 得内接的 $n$ 个矩形面积之和为

$$
a b \sum_{k=0}^{n-1} \frac{1}{n} \cdot\left(\frac{k}{n}\right)^{2}=\frac{a b(n-1)(2 n-1)}{6 n^{2}},
$$

当 $n \rightarrow \infty$ 时,它趋向于 $\frac{a b}{3}$, 即

$$
\text { 面积 } O A M=\frac{a b}{3} \text {. }
$$

求极限：
435. $\lim _{x \rightarrow+\infty} \frac{\sqrt{x+\sqrt{x+\sqrt{x}}}}{\sqrt{x+1}}$.

解 分子分母同除以 $\sqrt{x}$, 得

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{\sqrt{x+\sqrt{x+\sqrt{x}}}}{\sqrt{x+1}} \\
& =\lim _{x+\infty} \frac{\sqrt{1+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x^{3}}}}}}{\sqrt{1+\frac{1}{x}}} \\
& =1 .
\end{aligned}
$$

436. $\lim _{x \rightarrow+\infty} \frac{\sqrt{x}+\sqrt[3]{x}+\sqrt[4]{x}}{\sqrt{2 x+1}}$.

解 分子分母同除以 $\sqrt{x}$, 得

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{\sqrt{x}+\sqrt[3]{x}+\sqrt[4]{x}}{\sqrt{2 x+1}} \\
& =\lim _{x \rightarrow+\infty} \frac{1+x^{-\frac{1}{6}}+x^{-\frac{1}{4}}}{\sqrt{2+\frac{1}{x}}}=\frac{1}{\sqrt{2}}
\end{aligned}
$$

437. $\lim _{x \rightarrow 4} \frac{\sqrt{1+2 x}-3}{\sqrt{x}-2}$.

解 分子分母同乘以它们的共轱因式，得

$$
\begin{aligned}
& \lim _{x \rightarrow 4} \frac{\sqrt{1+2 x}-3}{\sqrt{x}-2} \\
= & \lim _{x \rightarrow 4} \frac{(\sqrt{1+2 x}-3)(\sqrt{1+2 x}+3)(\sqrt{x}+2)}{(\sqrt{x}-2)(\sqrt{x}+2)(\sqrt{1+2 x}+3)} \\
= & \lim _{x \rightarrow 4} \frac{2(x-4)(\sqrt{x}+2)}{(x-4)(\sqrt{1+2 x}+3)} \\
= & \lim _{x \rightarrow 4} \frac{2(\sqrt{x}+2)}{\sqrt{1+2 x}+3}
\end{aligned}
$$

$$
=\frac{4}{3} .
$$

438. $\lim _{x \rightarrow-8} \frac{\sqrt{1-x}-3}{2+\sqrt[3]{x}}$.

解 $\lim _{x \rightarrow-8} \frac{\sqrt{1-x}-3}{2+\sqrt[3]{x}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow-8} \frac{(\sqrt{1-x}-3)(\sqrt{1-x}+3)\left(4+\sqrt[3]{x^{2}}-2 \sqrt[3]{x}\right)}{(2+\sqrt[3]{x})\left(4+\sqrt[3]{x^{2}}-2 \sqrt[3]{x}\right)(\sqrt{1-x}+3)} \\
& =\lim _{x \rightarrow-8} \frac{-(8+x)\left(4+\sqrt[3]{x^{2}}-2 \sqrt[3]{x}\right)}{(8+x)(\sqrt{1-x}+3)} \\
& =-\lim _{x \rightarrow-8} \frac{4+\sqrt[3]{x^{2}}-2 \sqrt[3]{x}}{\sqrt{1-x}+3} \\
& =-2 .
\end{aligned}
$$

439. $\lim _{x \rightarrow a} \frac{\sqrt{x}-\sqrt{a}+\sqrt{x-a}}{\sqrt{x^{2}-a^{2}}}$

解 $\lim _{x \rightarrow a} \frac{\sqrt{x}-\sqrt{a} \pm \sqrt{x-a}}{\sqrt{x^{2}-a^{2}} .}$
$=\lim _{x \rightarrow a} \frac{(\sqrt{x}-\sqrt{a}+\sqrt{x-a})(\sqrt{x}+\sqrt{a})}{\sqrt{x^{2}-a^{2}}(\sqrt{x}+\sqrt{a})}$
$=\lim _{x \rightarrow a} \frac{\sqrt{x-a}(\sqrt{x-a}+\sqrt{x}+\sqrt{a})}{\sqrt{x-a} \cdot \sqrt{x+a}(\sqrt{x}+\sqrt{a})}$
$=\lim _{x \rightarrow a} \frac{\sqrt{x-a}+\sqrt{x}+\sqrt{a}}{\sqrt{x+a}(\sqrt{x}+\sqrt{a})}$
$=\frac{1}{\sqrt{2 a}}(a>0)$.
440. $\lim _{x \rightarrow-3} \frac{\sqrt{x+13}-2 \sqrt{x+1}}{x^{2}-9}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 3} \frac{\sqrt{x+13}-2 \sqrt{x+1}}{x^{2}-9} \\
= & \lim _{x \rightarrow 3} \frac{(\sqrt{x+13}-2 \sqrt{x+1})(\sqrt{x+13}+2 \sqrt{x+1})}{(x+3)(x-3)(\sqrt{x+13}+2 \sqrt{x+1})} \\
= & \lim _{x \rightarrow 3} \frac{-3(x-3)}{(x-3)(x+3)(\sqrt{x+13}+2 \sqrt{x+1})} \\
= & \lim _{x \rightarrow 3} \frac{-3}{(x+3)(\sqrt{x+13}+2 \sqrt{x+1})} \\
= & -\frac{1}{16} .
\end{aligned}
$$

441. $\lim _{x \rightarrow-2} \frac{\sqrt[3]{x-6}+2}{x^{3}+8}$.

解 $\lim _{x \rightarrow-2} \frac{\sqrt[3]{x-6}+2}{x^{3}+8}$

$$
\begin{aligned}
& =\lim _{x \rightarrow-2} \frac{(\sqrt[3]{x-6}+2)\left(\sqrt[3]{(x-6)^{2}}-2 \sqrt[3]{x-6}+4\right)}{\left(x^{3}+8\right)\left(\sqrt[3]{(x-6)^{2}}-2 \sqrt[3]{x-6}+4\right)} \\
& =\lim _{x \rightarrow-2} \frac{1}{\left(x^{2}-2 x+4\right)\left(\sqrt[3]{(x-6)^{2}}-2 \sqrt[3]{x-6}+4\right)} \\
& =\frac{1}{144}
\end{aligned}
$$

442. $\lim _{x \rightarrow 6} \frac{\sqrt[4]{x}-2}{\sqrt{x}-4}$.

解 $\lim _{x \rightarrow 16} \frac{\sqrt[4]{x}-2}{\sqrt{x}-4}=\lim _{x \rightarrow 16} \frac{1}{\sqrt[4]{x}+2}=\frac{1}{4}$.
443. $\lim _{x \rightarrow 5} \frac{\sqrt{9+2 x}-5}{\sqrt[3]{x}-2}$.

解 $\lim _{x \rightarrow 8} \frac{\sqrt{9+2 x}-5}{\sqrt[3]{x}-2}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 4} \frac{(\sqrt{9+2 x}-5)(\sqrt{9+2 x}+5)\left(\sqrt[5]{x^{4}}+2 \sqrt[3]{x}+4\right)}{(\sqrt[3]{x}-2)\left(\sqrt[3]{x^{2}}+2 \sqrt[3]{x}+4\right)(\sqrt{9+2 x}+5)} \\
& =2 \lim _{x \rightarrow-1} \frac{\sqrt[3]{x^{2}}+2 \sqrt[3]{x}+4}{\sqrt{9}-2 x}+5
\end{aligned}
$$

444. $\lim _{x \rightarrow 0} \frac{\sqrt{1+x}-1}{x}$ （ $n$ 为整数）。

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow 0} \frac{\sqrt[n]{1+x}-1}{x} \\
& =\lim _{x \rightarrow 0} \frac{(\sqrt[n]{1+x}-1)\left(\sqrt[n]{(1+x)^{n-1}}+\sqrt[n]{(1+x)^{n-2}}+\cdots+1\right)}{x\left(\sqrt[n]{(1+x)^{n-1}}+\sqrt[n]{(1+x)^{n-2}}+\cdots+1\right)} \\
& =\lim _{x \rightarrow 0} \frac{1}{\sqrt[n]{(1+x)^{n-1}}+\sqrt[n]{(1+x)^{n-2}}+\cdots+\sqrt[n]{1+x}+1} \\
& =\frac{1}{n} .
\end{aligned}
$$

445. $\lim _{x \rightarrow 0} \frac{\sqrt{1-2 x-x^{2}}-(1+x)}{x}$.

解 $\lim _{x \rightarrow 0} \frac{\sqrt{1-2 x-x^{2}}-(1+x)}{x}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\left(\sqrt{1-2 x-x^{2}}-1-x\right)\left(\sqrt{1-2 x-x^{2}}+1+x\right)}{x\left(\sqrt{1-2 x-x^{2}}+1+x\right)} \\
& =\lim _{x \rightarrow 0} \frac{-2(2+x)}{\sqrt{1-2 x-x^{2}}+1+x} \\
& =-2 .
\end{aligned}
$$

446. $\lim _{x \rightarrow 0} \frac{\sqrt[3]{8+3 x-x^{2}}-2}{x+x^{2}}$.

$$
\begin{aligned}
& \text { \{ } \quad \lim _{x \rightarrow 0} \frac{\sqrt[3]{8+3 x-x^{2}}-2}{x+x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{\left(\sqrt[3]{8+3 x-x^{2}}-2\right)}{\left(x+x^{2}\right)}
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{3-x}{(1+x)\left(\sqrt[3]{\left(8+3 x-x^{2}\right.}\right)^{2}+2 \sqrt[3]{8+3 x-x^{2}}+4} \\
& =\frac{1}{4} \text {. }
\end{aligned}
$$

447. $\lim _{x \rightarrow 0} \frac{\sqrt[3]{27+x}-\sqrt[3]{27-x}}{x+2 \sqrt[3]{x^{4}}}$

$$
\begin{aligned}
\text { 解 } & \lim _{x \rightarrow 0} \frac{\sqrt[3]{27+x}-\sqrt[3]{27-x}}{x+2 \sqrt[3]{x^{4}}} \\
= & \lim _{x \rightarrow 0} \frac{(\sqrt[3]{27+x}-\sqrt[3]{27-x)}}{\left(x+2 \sqrt[3]{x^{4}}\right)} \\
& \cdot \frac{\left(\sqrt[3]{(27+x)^{2}}+\sqrt[3]{27^{2}-x}+\sqrt[3]{(27-x)^{2}}\right)}{\left(\sqrt[3]{(27+x)^{2}}+\sqrt[3]{27^{2}-x^{2}}+\sqrt[3]{(27-x)^{2}}\right)} \\
= & \lim _{x \rightarrow 0} \frac{2}{(1+2 \sqrt[3]{x})\left(\sqrt[3]{(27+x)^{2}}+\sqrt[3]{27^{2}-x^{2}}+\sqrt[3]{(27-x)^{2}}\right)} \\
= & \frac{2}{27} .
\end{aligned}
$$

448. $\lim _{x \rightarrow 0} \frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt[3]{1+x}-\sqrt[3]{1-x}}$.

解 $\lim _{x \rightarrow 0} \frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt[3]{1+x}-\sqrt[3]{1-x}}$

$$
\begin{gathered}
=\lim _{x \rightarrow 0} \frac{(\sqrt{1+x}-\sqrt{1-x})(\sqrt{1+x}+\sqrt{1-x})}{(\sqrt[3]{1+x}-\sqrt[3]{1-x})(\sqrt{1+x}+\sqrt{1-x})} \\
\cdot \frac{\left(\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1-x^{2}}+\sqrt[3]{(1-x)^{2}}\right)}{\left(\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1-x^{2}}+\sqrt[3]{(1-x)^{2}}\right)} \\
=\lim _{x \rightarrow 0} \frac{\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1-x^{2}}+\sqrt[3]{(1-x)^{2}}}{\sqrt{1+x}+\sqrt{1-x}}
\end{gathered}
$$

$$
=\frac{3}{2} .
$$

449. $\lim _{x \rightarrow 7} \frac{\sqrt{x+2}-\sqrt[3]{x+20}}{\sqrt{x+9}-2}$.

$$
\text { 解 } \lim _{x \rightarrow 7} \frac{\sqrt{x+2}-\sqrt[3]{x+20}}{\sqrt[4]{x+9}-2}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 7} \frac{\left(\sqrt[6]{(x+2)^{3}}-\sqrt[6]{(x+20)^{2}}\right)(\sqrt[4]{x+9}+2)(\sqrt{x+9}+4)}{(\sqrt{x+9}-2)(\sqrt[4]{x+9}+2)(\sqrt{x+9}+4)} \\
& \frac{\left(\sqrt[6]{(x+2)^{15}}+\sqrt[6]{(x+2)^{12}(x+20)^{2}}+\cdots+\sqrt[8]{(x+20)^{10}}\right)}{\left(\sqrt[8]{(x+2)^{15}}+\cdots+\sqrt[6]{\left.(x+20)^{16}\right)}\right.} \\
& =\lim _{x \rightarrow 7} \frac{\left((x+2)^{3}-(x+20)^{2}\right](\sqrt[4]{x+9}+2)(\sqrt{x+9}+4)}{(x-7)\left(\sqrt[5]{(x+2)^{15}}+\cdots+\sqrt[6]{(x+2)^{10}}\right)} \\
& =\lim _{x \rightarrow 7} \frac{(x-7)\left(x^{2}+12 x+56\right)(\sqrt[4]{x+9}+2)(\sqrt{x+9}+4)}{(x-7)\left(\sqrt[6]{(x+2)^{15}}+\cdots+\sqrt[8]{(x+20)^{10}}\right)} \\
& =\lim _{x \rightarrow 7} \frac{\left(x^{2}+12 x+56\right)(\sqrt[4]{x+9}+2)(\sqrt{x+9}+9)}{\left(\sqrt[6]{(x+2)^{15}}+\sqrt[6]{(x+2)^{12}(x+20)^{2}}+\cdots+\sqrt[5]{(x+20)^{16}}\right)} \\
& =\frac{189 \cdot 4 \cdot 8}{3^{5}+3^{4} \cdot 3+3^{3} \cdot 3^{2}+3^{2} \cdot 3^{3}+3 \cdot 3^{4}+3^{5}} \\
& =\frac{6048}{1458}=4 \frac{4}{27}
\end{aligned}
$$

450. $\lim _{x \rightarrow 0} \frac{\sqrt[3]{1+\frac{x}{3}}-\sqrt[4]{1+\frac{x}{4}}}{1-\sqrt{1-\frac{x}{2}}}$.

解 $\lim _{x \rightarrow 0} \frac{\sqrt[3]{1+\frac{x}{3}}+\sqrt[4]{1+\frac{x}{4}}}{1-\sqrt{1-\frac{x}{2}}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\left(\sqrt[12]{\left(1+\frac{x}{3}\right)^{4}}-\sqrt[12]{\left(1+\frac{x}{4}\right)^{3}}\right)\left(1+\sqrt{1-\frac{x}{2}}\right)}{\left(1-\sqrt{1-\frac{x}{2}}\right)\left(1+\sqrt{1-\frac{x}{2}}\right)} \\
& \cdot \frac{\left(\sqrt[12]{\left(1+\frac{x}{3}\right)^{44}}+\cdots+\sqrt[12]{\left(1+\frac{x}{4}\right)^{33}}\right)}{\left(\sqrt[12]{\left(1+\frac{x}{3}\right)^{14}}+\cdots+\sqrt[12]{\left(1+\frac{x}{4}\right)^{33}}\right)} \\
& =\lim _{x \rightarrow 0} \frac{x\left(\frac{7}{12}+\frac{23 x}{48}+\frac{7 x^{2}}{54}+\frac{x^{3}}{81}\right)\left(1+\sqrt{1-\frac{x}{2}}\right)}{\frac{x}{2} \cdot\left(\sqrt[12]{\left(1+\frac{x}{3}\right)^{4}}+\cdots+\sqrt[12]{\left(1+\frac{x}{4}\right)^{3}}\right)} \\
& =\frac{7}{36} .
\end{aligned}
$$

451. $\lim _{x \rightarrow 0} \frac{x^{2}}{\sqrt[5]{1+5 x}-(1+x)}$.

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow 0} \frac{x^{2}}{\sqrt[5]{1+5 x}-(1+x)} \\
& =\lim _{x \rightarrow 0} \frac{x^{2}\left(\sqrt[5]{(1+5 x)^{4}}+\sqrt[5]{(1+5 x)^{3}}(1+x)+\cdots+(1+x)^{4}\right)}{(1+5 x)^{-(1+x)^{5}}} \\
& =\lim _{x \rightarrow 0} \frac{\sqrt[5]{(1+5 x)^{4}}+\sqrt[5]{(1+5 x)^{3}(1+x)+\cdots+(1+x)^{4}}}{-10-10 x-5 x^{2}-x^{3}} \\
& =-\frac{1}{2} .
\end{aligned}
$$

452. $\lim _{x \rightarrow 0} \frac{\sqrt[m]{1+\alpha x}-\sqrt[7]{1+\beta x}}{x}$ ( $m$ 及 $n$ 为整数).

解 如果 $m$ 及 $n$ 为正整数，则

$$
\lim _{x \rightarrow 0} \frac{\sqrt{1+\alpha x}-\sqrt[r]{1+\beta x}}{x}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 1} \frac{(1+\alpha x)^{n}-(1+\beta x)^{m}}{\left.x \sqrt[m]{(1+\alpha x)^{n(m n-1)}}+\cdots+\sqrt[m]{(1+\beta x)^{m(m-1)}}\right)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{n a-m p^{2}}{m n}=\frac{a}{m}-\frac{\beta}{n} \text {. }
\end{aligned}
$$

如果 $m$ 及 $n$ 为负整数. 设 $m=-m^{\prime}, n=-n^{\prime}$, 其中 $m^{\prime}$ 及 $n^{\prime}$ 为正整数，则

上式的分母趋于 1 ,于是利用本题前半段的结果，得

$$
\lim _{x \rightarrow 0} \frac{\sqrt[z^{\prime}]{1+\beta x}-\sqrt[m^{\prime}]{1+\alpha x}}{x}=\frac{\beta}{n^{\prime}}-\frac{\alpha}{m^{\prime}}=\frac{\alpha}{m}-\frac{\beta}{n} .
$$

如果 $m$ 及 $n$ 中有一个为负整数，另一个为正整数，则同法可证上述结论仍然成立。因此，

$$
\lim _{x \rightarrow 0} \frac{\sqrt[n]{1+\alpha x}-\sqrt[n]{1+\beta x}}{x}=\frac{\alpha}{m}-\frac{\beta}{n} \quad(m n \neq 0)
$$

453. $\lim _{x \rightarrow 0} \frac{\sqrt[n]{1+\alpha_{x}} \cdot \sqrt[2]{1+\beta x}-1}{x}(m$ 及 $n$ 为整数)。

解 与 452 题相同，先设 $m$ 及 $n$ 为正整数。

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sqrt[\pi]{1+\alpha x} \cdot \sqrt[n]{1+\beta x}-1}{x} \\
& =\lim _{x \rightarrow 0} \frac{(1+\alpha x)^{n}(1+\beta x)^{m}-1}{x\left(\sqrt[m]{(1+\alpha x)^{\left.\alpha^{(m+1}-1\right)} \cdot(1+\beta)^{m(m n-1)}}+\cdots+1\right)} \\
& =\lim _{x \rightarrow 0} \frac{n \alpha+m \beta+o(x)}{\sqrt[m]{(1+\alpha x)^{n(\operatorname{man}-1)}(1+\beta x)^{m(\operatorname{mn}-1)}}+\cdots+1} \\
& =\frac{n \alpha+m \beta}{m n} \\
& =\frac{a}{m}+\frac{\beta}{n} .
\end{aligned}
$$

若 $m$ 及 $n$ 为负整数，则此结果仍然成立。事实上，只须设 $m=-m^{\prime}, n=-n^{\prime}$ ，其中 $m^{\prime}$ 及 $n^{\prime}$ 为正整数。于是，
$\sqrt[m]{1+a x} \cdot \sqrt[n]{1+\overline{\beta x}}-1=\frac{1-\sqrt[n]{1+a x} \cdot \sqrt[n]{1+\beta x}}{\sqrt[m]{1+a x} \cdot \sqrt[n^{\prime}]{1+\beta x}}$.
再利用前半段结果，即得
$\lim _{x \rightarrow 0} \frac{1-\sqrt[m^{\prime}]{1+\alpha x} \cdot \sqrt[n^{\prime}]{1+\beta x}}{x(\sqrt[n]{1+\alpha x} \cdot \sqrt[x^{\prime}]{1+\beta x})}=-\frac{\alpha}{m^{\prime}}-\frac{\beta}{n^{2}}=\frac{\alpha}{m}+\frac{\beta}{n}$.
若 $m$ 及 $n$ 中只有一个为负整数，则同法可证上述结论仍然成立。因而，当 $m$ 及 $n$ 为整数时，有 $\lim _{x \rightarrow 0} \frac{\sqrt[m]{1+a x}-\sqrt[7]{1+\beta x}-1}{x}=\frac{a}{m}+\frac{\beta}{n} \quad(m n \neq 0)$.
454. 投 $P(x)=a_{1} x+a_{3} x^{2}+\cdots+a_{4} x^{\pi}$ 又 $m$ 表整数，求证：

$$
\lim _{x \rightarrow 0} \frac{\sqrt[n]{1+P(x)}-1}{x}=\frac{a_{1}}{m}
$$

证 $\lim _{x \rightarrow 0} \frac{\sqrt[n]{1+P(x)}-1}{x}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{P(x)}{x\left(\sqrt[n]{1+P(x)^{m-1}}+\cdots+1\right)} \\
& =\lim _{x \rightarrow 0} \frac{a_{1}+a_{2} x+\cdots+a_{n} x^{n-1}}{(1+P(x))^{\frac{m-1}{m}}+\cdots+1} \\
& =\frac{a_{1}}{m}
\end{aligned}
$$

求下列的极限：
455. $\lim _{x \rightarrow 1} \frac{\sqrt[m]{x}-1}{\sqrt[n]{x}-1}(m$ 及 $n$ 表整数 .

解 当 $m$ 及 $n$ 为正整数时，我们有

$$
\frac{\sqrt[m]{x}-1}{\sqrt{x-1}}=\frac{x^{\frac{x-1}{n}}+x^{\frac{\pi-2}{n}}+\cdots+1}{x^{\frac{m-1}{m}}+x^{\frac{m-2}{n}}+\cdots+1} \rightarrow \frac{n}{m}(x \rightarrow 1) .
$$

若 $m$ 及 $n$ 为负整数时，设 $m=-n^{\prime}, n=-n^{\prime}$ ，
其中 $m^{\prime}$ 及 $\pi^{\prime}$ 为正整数，于是

$$
\frac{\sqrt[m]{x}-1}{\sqrt[n]{x}-1}=\frac{1-\sqrt[m^{\prime}]{x}}{1-\sqrt[n^{\prime}]{x}} \cdot \frac{\sqrt[n]{x}}{\sqrt[m^{\prime}]{x}} \rightarrow \frac{n^{\prime}}{m^{\prime}}=\frac{n}{m} \quad(x \rightarrow
$$

$1)$.
当 $m$ 及 $n$ 中只有一个为负整数仍然成立。因此

$$
\lim _{x \rightarrow 1} \frac{\sqrt[7]{x}-1}{\sqrt[n]{x-1}}=\frac{n}{m} \quad(m \neq 0) .
$$

456. $\lim _{x \rightarrow 1} \frac{(1-\sqrt{x})(1-\sqrt[3]{x}) \cdots(1-\sqrt{x})}{(1-x)^{r^{-1}}}$

解 设 $x=t^{* 1}$ ，则

$$
\begin{aligned}
& \frac{(1-\sqrt{x})(1-\sqrt[3]{x}) \cdots(1-\sqrt[4]{x})}{(1-x)^{x-1}} \\
& =\frac{\left(1-t^{3 \cdot 4-n}\right)\left(1-t^{2 \cdot 4 \cdot 5 \cdots n}\right) \cdots\left(1-t^{2 \cdot 3 \cdot 4 \cdot \cdots(n-1)}\right)}{\left(1-t^{-1}\right)^{n^{-1}}} \\
& =\frac{\left(1+t+t^{2}+\cdots+t^{\frac{n 1}{2}-3}\right)\left(1+t+\cdots+t^{\frac{\pi}{3}-1}\right) \cdots\left(1+t+\cdots+t^{\frac{n!}{n}-1}\right)}{\left(1+t+\cdots+t^{n-1}\right)^{n-1}} \\
& \text { 当 } x \rightarrow 1 \text { 时， } t \rightarrow 1 \text { ，于是上式㛀向于， } \\
& \frac{\frac{n!}{2} \cdot \frac{n!}{3} \ldots \frac{n!}{n}}{(n!)^{n-1}}=\frac{1}{n!},
\end{aligned}
$$

即

$$
\lim _{x \rightarrow 1} \frac{(1-\sqrt{x})(1-\sqrt[3]{x}) \cdots(1-\sqrt{x})}{(1-x)^{n-1}} \rightleftharpoons \frac{1}{n!}
$$

457. $\lim _{x \rightarrow+\infty}[\sqrt{(x+a)(x+b)}-x]$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow+\infty}[\sqrt{(x+a)(x+b)}-x] \\
= & \lim _{x+\infty+\infty} \frac{(x+a)(x+b)-x^{2}}{\sqrt{(x+a)(x+b)}+x} \\
= & \lim _{x \rightarrow+\infty} \frac{a+b+\frac{a b}{x}}{1+\sqrt{\left(1+\frac{a}{x}\right)\left(1+\frac{b}{x}\right)}}=\frac{a+b}{2} .
\end{aligned}
$$

458. $\lim _{x \rightarrow+\infty}(\sqrt{x+\sqrt{x+\sqrt{x}}}-\sqrt{x})$.

$$
\text { 解 } \left.\begin{array}{rl} 
& \lim _{x \rightarrow+\infty}(\sqrt{x+\sqrt{x+\sqrt{x}}}-\sqrt{x}
\end{array}\right)
$$

459. $\lim _{x \rightarrow+\infty} x\left(\sqrt{x^{2}}+2 x-2 \sqrt{x^{2}+x}+x\right)$

解 设 $x=\frac{1}{t}$, 则

$$
\begin{aligned}
& x\left(\sqrt{x^{2}+2 x}-2 \sqrt{x^{2}+x}+x\right) \\
= & \frac{\sqrt{1+2 t}-2 \sqrt{1+t}+1}{t^{2}} \\
= & \frac{(\sqrt{1+2 t}+1)^{2}-4(1+t)}{t^{2}(\sqrt{1+2 t}+1+2 \sqrt{1+t})}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{2(\sqrt{1+2 t}-1-t)}{t^{2}(\sqrt{1+2 t}+1+2 \sqrt{1+t})} \\
& =\frac{-2(\sqrt{1+2 t}-1-t)(1+\sqrt{1+2 t})^{2}}{t^{2}(\sqrt{1+2 t}+1+2 \sqrt{1+t})(1+\sqrt{1+2 t})^{2}} \\
& =\frac{-4}{(\sqrt{1+2 t}+1+2 \sqrt{1+t})(1+\sqrt{1+2 t})^{2}} . \\
& \quad \text { 当 } x \rightarrow+\infty \text { 时, } t \rightarrow 0, \text { 于是上式趋向丁 }-\frac{1}{4} .
\end{aligned}
$$

即
$\lim _{x \rightarrow+\infty} x\left(\sqrt{x^{2}+2 x}-2 \sqrt{x^{2}+x}+x\right)=-\frac{1}{4}$.
460. $\lim _{x \rightarrow+0}\left\{\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}-\sqrt{\frac{1}{x}-\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}\right)$.
䈌
$\lim _{x \rightarrow+9}\left(\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}-\sqrt{\frac{1}{x}-\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}\right)$
$=\lim _{x \rightarrow+0} \frac{\left(\frac{1}{x}+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}\right)-\left(\frac{1}{x}-\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}\right)}{\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}+\sqrt{\frac{1}{x}-\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}}$
$=\lim _{x \rightarrow+\infty} \frac{2 \sqrt{\frac{1}{x}}+\sqrt{\frac{1}{x}}}{\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}+\sqrt{\frac{1}{x}-\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x}}}}}}$

$$
\begin{aligned}
& =2 \lim _{x \rightarrow+0} \frac{\sqrt{1} \pm \sqrt{x}}{\sqrt{1+\sqrt{x+x \sqrt{x}}}+\sqrt{1-\sqrt{x+x \sqrt{x}}}} \\
& =1 .
\end{aligned}
$$

461. $\lim _{x \rightarrow \infty}\left(\sqrt[3]{x^{3}+x^{2}+1}-\sqrt[3]{x^{3}-x^{2}+1}\right)$

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow+\infty}\left(\sqrt[3]{x^{3}+x^{2}+1}-\sqrt[3]{\left.x^{3}-x^{2}+1\right)}\right. \\
& =\lim _{x \rightarrow \infty} \frac{2 x^{2}}{\sqrt[3]{\left(x^{3}+x^{2}+1\right)^{2}}+\sqrt[3]{\left(x^{3}+x^{2}+1\right)\left(x^{3}-x^{2}+1\right)}+\sqrt[3]{\left(x^{3}-x^{2}+\right)^{2}}} \\
& =\frac{2}{3} .
\end{aligned}
$$

462. $\lim _{x \rightarrow+\infty}\left(\sqrt[3]{x^{3}+3 x^{2}}-\sqrt{x^{2}}-2 x\right)$.

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow+\infty}\left(\sqrt[3]{x^{3}+3 x^{2}}-\sqrt{x^{2}-2 x}\right) \\
& =\lim _{x \rightarrow+\infty} \frac{\left(x^{3}+3 x^{2}\right)^{2}-\left(x^{2}-2 x\right)^{3}}{\sqrt[8]{\left(x^{3}+3 x^{2}\right)^{10}}+\sqrt{\left(x^{3}+3 x^{2}\right)^{8}\left(x^{2}-2 x\right)^{3}}+\cdots+\sqrt[8]{\left(x^{2}-2 x\right)^{15}}} \\
& =\lim _{x \rightarrow+\infty} \frac{x^{5}\left(12-\frac{3}{x}+\frac{8}{x^{2}}\right)}{\sqrt[8]{\left(x^{3}+3 x^{2}\right)^{10}}+\cdots+\sqrt[6]{\left(x^{2}-2 x\right)^{15}}} \\
& =\lim _{x \rightarrow+\infty} \frac{12-\frac{3}{x}+\frac{8}{x^{2}}}{\sqrt[6]{\left(1+\frac{3}{x}\right)^{10}}+\cdots+\sqrt[5]{\left(1-\frac{2}{x}\right)^{15}}}
\end{aligned}
$$

$=2$.
463. $\lim _{x \rightarrow \infty} x^{\frac{1}{3}}\left[(x+1)^{\frac{2}{3}}-(x-1)^{\frac{2}{3}}\right]$.

裸 $\lim _{x \rightarrow \infty} x^{\frac{1}{3}}\left[(x+1)^{\frac{4}{3}}-(x-1)^{\frac{2}{3}}\right)$

$$
=\lim _{x \rightarrow \infty} \frac{x^{\frac{1}{3}}\left[(x+1)^{\frac{2}{3}}-(x-1)^{\frac{2}{3}}\right) \cdot\left((x+1)^{\frac{4}{3}}+\left(x^{2}-1\right)^{\frac{2}{3}}+(x-1)^{\frac{4}{3}}\right)}{(x+1)^{\frac{4}{3}}+\left(x^{2}-1\right)^{\frac{2}{3}}+(x-1)^{\frac{4}{3}}}
$$

$$
\begin{aligned}
& =4 \lim _{x \rightarrow \infty} \frac{1}{\left(1+\frac{1}{x}\right)^{\frac{4}{3}}-\left(1-\frac{1}{x^{2}}\right)^{\frac{2}{3}}+\left(1-\frac{1}{x}\right)^{\frac{1}{3}}} \\
& =\frac{4}{3}
\end{aligned}
$$

464. $\lim _{x \rightarrow+\infty} x^{\frac{3}{2}}(\sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x})$.

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow+\infty} x^{\frac{3}{2}}(\sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x}) \\
& =\lim _{x \rightarrow+\infty} \frac{\frac{3}{2}(\sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x})(\sqrt{x+2}+2 \sqrt{x+1}+\sqrt{x})}{\sqrt{x+2}+2 \sqrt{x+1}+\sqrt{x}} \\
& =\lim _{x \rightarrow+\infty} \frac{2 \frac{3}{2}\left(\sqrt{x^{2}+2 x}-x-1\right)\left(\sqrt{x^{2}+2 x}+x+1\right)}{(\sqrt{x+2}+2 \sqrt{x+1}+\sqrt{x})\left(\sqrt{x^{2}+2 x}+x+1\right)} \\
& =-2 \lim _{x \rightarrow+\infty} \frac{1}{\left(\sqrt{1+\frac{2}{x}}+2 \sqrt{1+\frac{1}{x}}+1\right)\left(\sqrt{1+\frac{2}{x}}+1+\frac{1}{x}\right)} \\
& =-\frac{1}{4} .
\end{aligned}
$$

465. $\lim _{x \rightarrow+\infty}\left[\sqrt[n]{\left(x+a_{1}\right) \cdots\left(x+a_{n}\right)}-x\right]$

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow+\infty}\left[\sqrt[n]{\left(x+a_{1}\right) \cdots\left(x+a_{n}\right)}-x\right] \\
= & \lim _{x \rightarrow+\infty} \frac{\left(x+\alpha_{1}\right) \cdots\left(x+\alpha_{n}\right)-x^{n}}{\sum_{j=1}^{n}\left[\prod_{i=1}^{n}\left(x+\alpha_{i}\right)^{n-j}\right]^{j-1}} \\
= & \lim _{x \rightarrow+\infty} \frac{\left(\sum_{i=1}^{n} \alpha_{i}\right) x^{n-1}+\cdots+\prod_{i=1}^{n} \alpha_{i}}{\sum_{j=1}^{n}\left[\prod_{i=1}^{n}\left(x+\alpha_{i}\right)^{\frac{n-i}{n}}\right] x^{j-1}}
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow+\infty} \frac{\sum_{i=1}^{n} \alpha_{i}+o\left(\frac{1}{x}\right)}{\sum_{j=1}^{n}\left[\prod_{i=1}^{n}\left(1+\frac{a_{i}}{x}\right)^{\frac{n-j}{n}}\right]} \\
& =\frac{\sum_{i=1}^{n} a_{i}}{n} .
\end{aligned}
$$

466. $\lim _{x \rightarrow \infty} \frac{\left(x-\sqrt{x^{2}-1}\right)^{n}+\left(x+\sqrt{x^{2}-1}\right)^{n}}{x^{4}} \quad(n$ 表自然数).
解 $\lim _{x \rightarrow \infty} \frac{\left(x-\sqrt{x^{2}-1}\right)^{n}+\left(x+\sqrt{x^{2}-1}\right)^{*}}{x^{2}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow \infty}\left[\left(1-\sqrt{1-\frac{1}{x^{2}}}\right)^{n}+\left(1+\sqrt{1-\frac{1}{x^{2}}}\right)^{n}\right] \\
& =2^{n} .
\end{aligned}
$$

467. $\lim _{x \rightarrow 0} \frac{\left(\sqrt{1+x^{2}}+x\right)^{2}-\left(\sqrt{1+x^{2}}-x\right)^{n}}{x} \quad(n$ 表自然数)。
解 $\lim _{x \rightarrow 0} \frac{\left(\sqrt{1+x^{2}}+x\right)^{n}-\left(\sqrt{1+x^{2}}-x\right)^{n}}{x}$

$$
\begin{aligned}
= & \lim _{x \rightarrow 0} \frac{2 x}{x}\left[\left(x+\sqrt{1+x^{2}}\right)^{n-1}+\left(x+\sqrt{1+x^{2}}\right)^{n-2}\right. \\
& \left.\left(\sqrt{1+x^{2}}-x\right)+\cdots+\left(\sqrt{1+x^{2}}-x\right)^{n-1}\right]
\end{aligned}
$$

$$
=2 n
$$

468. 设二次方程式 $a x^{2}+b x+c=0$ 的系数 $a$ 趋于零, 系数 $b$ 与 $c$ 为常数，且 $b \neq 0$ ，试研究此二次方程式之二根 $x_{1}$及 $x_{2}$ 的性质。
解 $x_{1}=\frac{-b+\sqrt{b^{2}-4 a c}}{2 a}, x_{2}=\frac{-b-\sqrt{b^{2}-4 a c}}{2 a}$.

不失一般性，假设 $b>0$ ，于是，有 $\lim _{a \rightarrow 0} x_{2}=\infty$
及

$$
\begin{aligned}
\lim _{a \rightarrow 0} x_{1} & =\lim _{a \rightarrow 0} \frac{\left(-b+\sqrt{b^{2}-4 a c}\right)\left(-b-\sqrt{b^{2}-4 a c}\right)}{2 a\left(-b-\sqrt{b^{2}-4 a c}\right)} \\
& =-2 c \lim _{a \rightarrow 0} \frac{1}{b+\sqrt{b^{2}-4 a c}} \\
& =-\frac{c}{b} .
\end{aligned}
$$

469. 从条件:

$$
\lim _{x \rightarrow \infty}\left(\frac{x^{2}+1}{x+1}-a x-b\right)=0
$$

求裳数 $a$ 和 $b$ 。
解 $\frac{x^{2}+1}{x+1}-a x-b$

$$
=\frac{(1-a) x^{2}-(a+b) x+(1-b)}{x+1}
$$

按假设，上式的极限为零的必要条件是

$$
1-a=0 \quad \text { 及 } \quad a+b=0,
$$

解之，得

$$
a=1, \quad b=-1
$$

470. 从条件:

$$
\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}-x+1}-a_{1} x-b_{1}\right)=0
$$

和. $\lim _{x \rightarrow+\infty}\left(\sqrt{x^{2}-x+1}-a_{2} x-b_{2}\right)=0$
求常数 $a_{i}$ 和 $b_{i}(i=1,2)$.
解

$$
\begin{aligned}
& \sqrt{x^{2}-x+1}-a_{1} x-b_{1} \\
= & \frac{\left(1-a_{1}^{2}\right) x^{2}-\left(1+2 a_{1} b_{1}\right) x+\left(1-b_{1}^{2}\right)}{\sqrt{x^{2}-x+1}+a_{1} x+b_{1}}
\end{aligned}
$$

上式极限为零的必要条件是

$$
1-a_{1}^{2}=0 \quad \text { 及 } \quad 1+2 a_{1} b_{1}=0 \text {, }
$$

解之, 得

$$
a_{1}= \pm 1, \quad b_{1}=\mp \frac{1}{2}
$$

同理可得

$$
a_{2}= \pm 1, \quad b_{2}=\mp \frac{1}{2} .
$$

求下列的极限：
471. $\lim _{x \rightarrow 0} \frac{\sin 5 x}{x}$.

解 $\lim _{x \rightarrow 0} \frac{\sin 5 x}{x}=5 \lim _{x \rightarrow 0} \frac{\sin 5 x}{5 x}$
$=5.1=5$.
472. $\lim _{x \rightarrow \infty} \frac{\sin x}{x}$.

解 当 $x \rightarrow \infty$ 时， $\frac{1}{x}$ 为无穷小量，而 $|\sin x| \leqslant 1$ ，故 $\frac{\sin x}{x}$ 当 $x \rightarrow \infty$ 时为无穷小量, 即

$$
\lim _{x \rightarrow \infty} \frac{\sin x}{x}=0
$$

473. $\lim _{x \rightarrow \pi} \frac{\sin m x}{\sin n x}$ ( $m$ 及 $n$ 为整数).

解 设 $x=\pi+y$, 则当 $x \rightarrow \pi$ 时， $y \rightarrow 0$ 。于是，

$$
\begin{aligned}
& \lim _{x \rightarrow \pi} \frac{\sin m x}{\sin n x} \\
& =\lim _{y \rightarrow 0} \frac{(-1)^{m} \sin m y}{(-1)^{n} \sin n y} \\
& =(-1)^{m-x} \lim _{y \rightarrow 0} \frac{\sin m y}{m y} \cdot \frac{n y}{\sin n y} \cdot \frac{m}{n}
\end{aligned}
$$

$$
=(-1)^{m-n} \frac{m}{n}
$$

474. $\lim _{x \rightarrow 0} \frac{1-\cos x}{x^{2}}$.

$$
\text { 解 } \begin{aligned}
& \left.\lim _{x \rightarrow 0} \frac{1-\cos x}{x^{2}}=\lim _{x \rightarrow 0} \frac{2 \sin ^{2}\left(\frac{x}{2}\right)}{x^{2}}\right) \\
= & \frac{1}{2} \lim _{x \rightarrow 0}\left(\frac{\sin \frac{x}{2}}{\frac{x}{2}}\right)^{2}=\frac{1}{2} .
\end{aligned}
$$

475. $\lim _{x \rightarrow 0} \frac{\operatorname{tg} x-\sin x}{\sin ^{3} x}$.

船 $\lim _{x \rightarrow 0} \frac{\operatorname{tg} x-\sin x}{\sin ^{3} x} \leqslant \lim _{x \rightarrow 0} \frac{\frac{\sin x}{\cos x}-\sin x}{\sin ^{3} x}$

$$
=\lim _{x \rightarrow 0} \frac{1-\cos x}{\cos x \sin ^{2} x}
$$

$$
\begin{aligned}
& =\lim _{x+0} \frac{2 \sin ^{2} \frac{x}{2}}{4 \sin ^{2} \frac{x}{2} \cos ^{2} \frac{x}{2} \cos x} \\
& =\lim _{x \rightarrow 0} \frac{1}{2 \cos ^{2} \frac{x}{2} \cos x}=\frac{1}{2} .
\end{aligned}
$$

476. $\lim _{x \rightarrow 0} \frac{\sin 5 x-\sin 3 x}{\sin x}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sin 5 x-\sin 3 x}{\sin x} \\
& =\lim _{x \rightarrow 0} \frac{2 \cos 4 x \sin x}{\sin x} \\
& =2 \lim _{x \rightarrow 0} \cos 4 x=2 .
\end{aligned}
$$

477. $\lim _{x \rightarrow 0} \frac{\cos x-\cos 3 x}{x^{2}}$.

解 $\lim _{x \rightarrow 0^{2}} \frac{\cos x-\cos 3 x}{x^{2}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{2 \sin 2 x \sin x}{x^{2}} \\
& =4 \lim _{x \rightarrow 0}\left(\frac{\sin x}{x}\right)^{2} \cos x=4
\end{aligned}
$$

478. $\lim _{x \rightarrow 0} \frac{1+\sin x-\cos x}{1+\sin p x-\cos p x}$.

用 $\lim _{x \rightarrow 0} \frac{1+\sin x-\cos x}{1+\sin p x-\cos p x}$

$$
=\lim _{x \rightarrow 0} \frac{2 \sin ^{2} \frac{x}{2}+\sin x}{2 \sin ^{8} \frac{p x}{2}+\sin p x}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\sin \frac{x}{2}\left(\sin \frac{x}{2}+\cos \frac{x}{2}\right)}{\sin \frac{p x}{2}\left(\sin \frac{p x}{2}+\cos \frac{p x}{2}\right)} \\
& =\lim _{x \rightarrow 0} \frac{\sin \frac{x}{2}}{\frac{x}{2}} \cdot \frac{\frac{p x}{2}}{\sin \frac{p x}{2}} \cdot \frac{1}{p} \cdot \frac{\sin \frac{x}{2}+\cos \frac{x}{2}}{\sin \frac{p x}{2}+\cos \frac{p x}{2}} \\
& =\frac{1}{p} \quad(p \neq 0) .
\end{aligned}
$$

479. $\lim _{x \rightarrow \frac{\pi}{4}} \operatorname{tg} 2 x \operatorname{tg}\left(\frac{\pi}{4}-x\right)$.

解 $\lim _{x \rightarrow \frac{\pi}{4}} \operatorname{tg} 2 x \operatorname{tg}\left(\frac{\pi}{4}-x\right)$

$$
\begin{aligned}
& =\lim _{x \rightarrow \frac{\pi}{4}} \frac{\sin 2 x \sin \left(\frac{\pi}{4}-x\right)}{\cos 2 x \cos \left(\frac{\pi}{4}-x\right)} \\
& =\lim _{y \rightarrow 0} \frac{\cos 2 y \sin y}{\sin 2 y \cos y}=\lim _{y \rightarrow 0} \frac{\cos 2 y}{2 \cos ^{2} y} . \\
& =\frac{1}{2}
\end{aligned}
$$

其中 $x=\frac{\pi}{4}+y$.
480. $\lim _{x \rightarrow 1}(1-x) \operatorname{tg} \frac{\pi x}{2}$.

复 设 $x=1-y$ ，则

$$
\begin{aligned}
& \lim _{x \rightarrow 1}(1-x) \operatorname{tg} \frac{\pi x}{2}=\lim _{y \rightarrow 0} y \operatorname{ctg} \frac{\pi y}{2} \\
& =\lim _{y \rightarrow 0}\left[\frac{\frac{\pi y}{2}}{\sin \frac{\pi y}{2}} \cdot \frac{2}{\pi} \cdot \cos \frac{\pi y}{2}\right]=\frac{2}{\pi} .
\end{aligned}
$$

## 481. 证明等式：

(a) $\lim _{x \rightarrow \mathrm{a}} \sin x=\sin a$;
(6) $\lim _{x \rightarrow a} \cos x=\cos a$;
(в) $\operatorname{limtg}_{x \rightarrow a} x=\operatorname{tg} a\left(a \neq \frac{2 n-1}{2} \pi ; \pi=0, \pm 1, \pm 2, \cdots\right)$.

证 (a) $|\sin x-\sin a|=2\left|\sin \frac{x-a}{2}\right| \cdot\left|\cos \frac{x+a}{2}\right|$

$$
\leqslant 2\left|\sin \frac{x-a}{2}\right| \leqslant|x-a|
$$

任给 $\varepsilon>0$ ，要使

$$
|\sin x-\sin a|<\varepsilon,
$$

只颃 $|x-a|<\varepsilon$ ，取 $\delta=\varepsilon$ ，则当 $0<|x-a|<\delta$ 时，
$|\sin x-\sin a|<\varepsilon$.

此即 $\operatorname{limsin} x=\sin a$.
(6) $\lim _{x \rightarrow a} \cos x=\operatorname{limsin}_{x \rightarrow a}\left(\frac{\pi}{2}-x\right)$

$$
=\sin \left(\frac{\pi}{2}-a\right)=\cos a
$$

(B) $\operatorname{limtg}_{x \rightarrow a} x=\lim _{x \rightarrow a} \frac{\sin x}{\cos x}=\frac{\lim _{x \rightarrow a} \sin x}{\lim _{x \rightarrow a} \cos x}=\frac{\sin a}{\cos a}=\operatorname{tg} a$.

其中 $a \neq \frac{2 n-1}{2} \pi ; \quad n=0, \pm 1, \pm 2 \cdots$ 。

## 求下列的极限：

482. $\lim _{x \rightarrow a} \frac{\sin x-\sin a}{x-a}$.

$$
\text { 粠 } \begin{aligned}
& \lim _{x \rightarrow a} \frac{\sin x-\sin a}{x-a}=\lim _{x \rightarrow a} \frac{2 \cos \frac{x+a}{2} \sin \frac{x-a}{2}}{x-a} \\
= & \lim _{x \rightarrow a} \frac{\cos \frac{x+a}{2} \sin \frac{x-a}{2}}{\frac{x-a}{2}}=\cos a .
\end{aligned}
$$

483. $\lim _{x \rightarrow a} \frac{\cos x-\cos a}{x-a}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow a} \frac{\cos x-\cos a}{x-a} \\
& =\lim _{x \rightarrow a} \frac{-\sin \frac{x-a}{\frac{2}{a}}}{\frac{x}{2}} \cdot \sin \frac{x+a}{2} \\
& =-\sin a .
\end{aligned}
$$

484. $\lim _{x \rightarrow a} \frac{\operatorname{tg} x-\operatorname{tg} a}{x-a}$.

解 $\lim _{x \rightarrow a} \frac{\operatorname{tg} x-\operatorname{tg} a}{x-a}=\lim _{x \rightarrow a} \frac{\sin (x-a)}{(x-a) \cos x \cos a}$

$$
=\frac{1}{\cos ^{2} a}\left(a \neq \frac{2 k+1}{2} \pi ; k=0, \pm 1, \pm 2, \cdots\right) .
$$

485. $\lim _{x \rightarrow a} \frac{\operatorname{ctg} x-\operatorname{ctg} a}{x-a}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow a} \frac{\operatorname{ctg} x-\operatorname{ctg} a}{x-a} \\
& =-\lim _{x \rightarrow a} \frac{\sin (x-a)}{x-a} \cdot \frac{1}{\sin x \sin a} \\
& =-\frac{1}{\sin ^{2} a} \quad(a \neq k \pi \neq k=0 . \pm 1, \pm 2, \cdots) .
\end{aligned}
$$

486. $\lim _{x \rightarrow a} \frac{\sec x-\sec a}{x-a}$.

粠 $\lim _{x \rightarrow a} \frac{\sec x-\sec a}{x-a}=\lim _{x \rightarrow a} \frac{\cos a-\cos x}{(x-a) \cos x \cos a}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 4} \frac{\sin \frac{x+a}{2}-\frac{\sin \frac{x-a}{2}}{\cos x \cos a} \cdot \frac{x-a}{2}}{=\frac{\sin a}{\cos ^{2} a}\left(a \neq \frac{2 k+1}{2} \pi ; k=0, \pm 1, \pm 2, \cdots\right) .}
\end{aligned}
$$

487. $\lim _{x \rightarrow \infty} \frac{\operatorname{cosec} x-\operatorname{cosec} a}{x-a}$.

解 $\lim _{x \rightarrow a} \frac{\operatorname{cosec} x-\operatorname{cosec} a}{x-a}$

$$
\begin{aligned}
& =-\lim _{\rightarrow \rightarrow \pi} \frac{\sin x}{x}-\frac{\sin a}{a} \cdot \frac{1}{\sin x \sin a} \\
& =-\frac{\cos a}{\sin ^{2} a} \quad(a \neq k \pi ; k=0, \pm 1, \pm 2, \cdots) .
\end{aligned}
$$

*) 利用 482 题的结果。
488. $\lim _{x \rightarrow 0} \frac{\sin (a+2 x)-2 \sin (a+x)+\sin a}{x^{2}}$.

解 $\lim _{x \rightarrow 0} \frac{\sin (a+2 x)-2 \sin (a+x)+\sin a}{x^{2}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{[\sin (a+2 x)-\sin (a+x)]-[\sin (a+x)-\sin a]}{x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{2 \cos \left(a+\frac{3 x}{2}\right) \sin \frac{x}{2}-2 \cos \left(a+\frac{x}{2}\right) \sin \frac{x}{2}}{x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{2 \sin \frac{x}{2}\left[\cos \left(a+\frac{3 x}{2}\right)-\cos \left(a+\frac{x}{2}\right)\right]}{x^{2}} \\
& =-\lim _{x \rightarrow 0}\left(\frac{\sin \frac{x}{2}}{\frac{x}{2}}\right)^{2} \cdot \sin (a+x) \\
& =-\sin a .
\end{aligned}
$$

489. 

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\cos (a+2 x)-2 \cos (a+x)+\cos a}{x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{[\cos (a+2 x)-\cos (a+x)]-[\cos (a+x)-\cos a]}{x^{2}} \\
& \left.=\lim _{x \rightarrow 0}-2 x\right)-2 \cos (a+x)+\cos a \\
& x^{2} \\
& =-\lim _{x \rightarrow 0} \frac{-2 \sin \left(a+\frac{3 x}{2}\right) \sin \frac{x}{2}+2 \sin \left(a+\frac{x}{2}\right) \sin \frac{x}{2}}{x^{2}} \\
& =-\lim _{x \rightarrow 0}\left(\frac{\left.\sin \left(a+\frac{3 x}{2}\right)-\sin \left(a+\frac{x}{2}\right)\right]}{x^{2}}\right) \\
& =-\cos a . \\
& \left.\frac{x}{2}\right)^{2} \\
& =
\end{aligned}
$$

490. $\lim _{x \rightarrow 0} \frac{\operatorname{tg}(a+2 x)-2 \operatorname{tg}(a+x)+\operatorname{tg} a}{x^{2}}$.

$$
\begin{aligned}
\text { 解 } & \lim _{x \rightarrow 0} \frac{\operatorname{tg}(a+2 x)-2 \operatorname{tg}(a+x)+\operatorname{tg} a}{x^{2}} \\
= & \lim _{x \rightarrow 0} \frac{[\operatorname{tg}(a+2 x)-\operatorname{tg}(a+x)]-[\operatorname{tg}(a+x)-\operatorname{tg} a]}{x^{2}} \\
= & \lim _{x \rightarrow 0}\left\{\frac{\frac{\sin (a+2 x) \cos (a+x)-\cos (a+2 x) \sin (a+x)}{\cos (a+2 x) \cos (a+x)}}{x^{2}}\right. \\
& +\frac{-\cos a \sin (a+x)-\cos (a+x) \sin a}{\cos (a+x) \cos a} \\
= & \lim _{x \rightarrow 0} \frac{\sin x[\cos (a+x) \cos a-\cos (a+x) \cos (a+2 x)]}{x^{2} \cos a \cos (a+2 x) \cos (a+x)} \\
= & \lim _{x \rightarrow 0} \frac{\sin ^{2} x}{x^{2}} \cdot \frac{2 \sin (a+x)}{\cos a \cos (a+2 x) \cos (a+x)} \\
= & \left.\frac{2 \sin a}{\cos ^{3} a} \quad \frac{2 k+1}{2} \pi ; k=0, \pm 1, \pm 2, \cdots\right) .
\end{aligned}
$$

491. $\lim _{x \rightarrow 0} \frac{\operatorname{ctg}(a+2 x)-2 \operatorname{ctg}(a+x)+\operatorname{ctg} a}{x^{2}}$.

$$
\begin{aligned}
& \text { 解 } \quad \lim _{x \rightarrow 0} \frac{\operatorname{ctg}(a+2 x)-2 \operatorname{ctg}(a+x)+\operatorname{ctg} a}{x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{-\sin x \sin (a+x)(\sin a-\sin (a+2 x)]}{x^{2} \sin a \sin ^{2}(a+x) \sin (a+2 x)} \\
& =\lim _{x \rightarrow 0}\left(\frac{\sin x}{x}\right)^{2} \frac{2 \cos (a+x)}{\sin a \cdot \sin (a+x) \sin (a+2 x)} \\
& =\frac{2 \cos a}{\sin ^{3} a} \quad(a \neq k \pi ; k=0, \pm 1, \pm 2, \cdots) .
\end{aligned}
$$

492. $\lim _{x \rightarrow 0} \frac{\sin (a+x) \sin (a+2 x)-\sin ^{2} a}{x}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sin (a+x) \sin (a+2 x)-\sin ^{2} a}{x} \\
= & \lim _{x \rightarrow 0} \frac{\frac{1}{2}[\cos x-\cos (2 a+3 x)]-\sin ^{2} a}{x}
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\cos x-\cos (2 a+3 x)-(1-\cos 2 a)}{2 x} \\
& =\lim _{x \rightarrow 0}\left[-\frac{\sin ^{2} \frac{x}{2}}{x}+-\frac{\sin \frac{3 x}{2}}{\frac{3 x}{2}} \cdot \frac{3 \sin \left(2 a+\frac{3 x}{2}\right)}{2}\right] \\
& =\frac{3}{2} \sin 2 a .
\end{aligned}
$$

493. $\lim _{x \rightarrow \frac{x}{6}} \frac{2 \sin ^{2} x+\sin x-1}{2 \sin ^{2} x-3 \sin x+1}$.

解 $\lim _{x \rightarrow \frac{\pi}{6}} \frac{2 \sin ^{2} x-\sin x-1}{2 \sin ^{2} x-3 \sin x+1}$

$$
\begin{aligned}
& =\lim _{x \rightarrow \frac{\pi}{6}} \frac{(2 \sin x-1)(\sin x+1)}{(2 \sin x-1)(\sin x-1)} \\
& =\lim _{x \rightarrow \frac{\pi}{6}} \frac{\sin x+1}{\sin x-1}=-3 .
\end{aligned}
$$

494. $\lim _{x \rightarrow 0} \frac{1-\cos x \cos 2 x \cos 3 x}{1-\cos x .}$

解 因为

$$
\begin{aligned}
& 1-\cos x \cos 2 x \cos 3 x \\
& =1-\frac{1}{2}(\cos 4 x+\cos 2 x) \cos 2 x \\
& =1-\frac{1}{2} \cos 4 x \cos 2 x-\frac{1}{2} \cos ^{2} 2 x \\
& =1-\frac{1}{4}(\cos 6 x+\cos 2 x)-\frac{1}{4}(1-\cos 4 x) \\
& =\frac{1}{2}\left(\sin ^{2} x+\sin ^{2} 2 x+\sin ^{2} 3 x\right)
\end{aligned}
$$

所以，

$$
\lim _{x \rightarrow 0} \frac{1-\cos x \cos 2 x \cos 3 x}{1-\cos x}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\frac{1}{2}\left(\sin ^{2} x+\sin ^{2} 2 x+\sin ^{2} 3 x\right)}{2 \sin 2 \frac{x}{2}} \\
& =\frac{1}{4} \lim _{x \rightarrow 0}\left[\left(\left[\frac{\sin x}{\sin \frac{x}{2}}\right)^{2}+\left(\frac{\sin 2 x}{\sin \frac{x}{2}}\right)^{2}+\left(\frac{\sin 3 x}{\sin \frac{x}{2}}\right)^{2}\right]\right. \\
& =\frac{1}{4}(4+16+36)=14 .
\end{aligned}
$$

$$
\text { 495. } \lim _{x \rightarrow \frac{\pi}{3}} \frac{\sin \left(x-\frac{\pi}{3}\right)}{1} 2 \cos x \text {. }
$$

解 设 $x=\frac{\pi}{3}+y$, 则

$$
\begin{aligned}
& \lim _{x \rightarrow \frac{\pi}{3}} \frac{\left.\sin \left\lvert\, x-\frac{\pi}{3}\right.\right)}{1-2 \cos x}=\lim _{y \rightarrow 0} \frac{\sin y}{1-\cos y+\sqrt{3} \sin y} \\
= & \lim _{y \rightarrow 0} \frac{\frac{\sin y}{y}}{\frac{\sin \frac{y}{2}}{\frac{y}{2}} \sin \frac{y}{2}+\sqrt{3} \frac{\sin y}{y}}=\frac{1}{\sqrt{3}} .
\end{aligned}
$$

496. $\lim _{x \rightarrow \frac{x}{3}} \frac{\operatorname{tg}^{3} x-3 \operatorname{tg} x}{\cos \left(x+\frac{\pi}{6}\right)}$.

解 $\lim _{x \rightarrow \frac{\pi}{3}} \frac{\operatorname{tg}^{3} x-3 \operatorname{tg} x}{\cos \left(x+\frac{\pi}{6}\right)}=\lim _{x \rightarrow \frac{\pi}{3}} \frac{\operatorname{tg} x \cdot \frac{\sin ^{2} x-3 \cos ^{2} x}{\cos ^{2} x}}{\frac{\sqrt{3}}{2} \cos x-\frac{1}{2} \sin x}$

$$
=\lim _{x \rightarrow \frac{\pi}{3}} \frac{\operatorname{tg} x(\sin x+\sqrt{3} \cos x)}{-\frac{1}{2} \cos ^{2} x}=-24 .
$$

497. $\lim _{x \rightarrow 3} \frac{\operatorname{tg}(a+x) \operatorname{tg}(a-x)-\operatorname{tg}^{2} a}{x^{2}}$.

解 $\lim _{x \rightarrow 0} \frac{\operatorname{tg}(a+x) \operatorname{tg}(a-x)-\operatorname{tg}^{2} a}{x^{2}}$.

$$
\begin{aligned}
= & \lim _{x \rightarrow 0} \frac{\left(\frac{\operatorname{tg} a+\operatorname{tg} x}{1-\operatorname{tg} a t g}\right)\left(\frac{\operatorname{tg} a-\operatorname{tg} x}{1+\operatorname{tg} a \operatorname{tg} x}\right)-\operatorname{tg}^{2} a}{x^{2}} \\
= & \lim _{x \rightarrow 0} \frac{\operatorname{tg}^{2} x\left(\operatorname{tg}^{4} a-1\right)}{x^{2}\left(1-\operatorname{tg}^{2} a \operatorname{tg}^{2} x\right)}=\operatorname{tg}^{4} a-1=\frac{-\cos 2 a}{\cos ^{4} a} \\
& \left(a \neq \frac{2 k+1}{2} \pi_{;} k=0, \pm 1, \pm 2, \cdots\right) .
\end{aligned}
$$

498. $\lim _{x \rightarrow \frac{\pi}{4}} \frac{1-\operatorname{ctg}^{3} x}{2-\operatorname{ctg} x-\operatorname{ctg}^{3} x}$.

解 $\lim _{x \rightarrow \frac{\pi}{4}} \frac{1-\operatorname{ctg}^{3} x}{2-\operatorname{ctg} x-\operatorname{ctg}^{3} x}$

$$
\begin{aligned}
& =\lim _{x+\frac{\pi}{4}} \frac{\sin ^{3} x-\cos ^{3} x}{2 \sin ^{3} x-\sin ^{2} x \cos x-\cos ^{3} x} \\
& =\lim _{x+\frac{\pi}{4}} \frac{\sin ^{2} x+\sin x \cos x+\cos ^{2} x}{2 \sin ^{2} x+\sin x \cos x+\cos ^{2} x}=\frac{3}{4} .
\end{aligned}
$$

499. $\lim _{x \rightarrow 0} \frac{\sqrt{1+\operatorname{tg} x}-\sqrt{1+\sin x}}{x^{3}}$.

解 $\lim _{x \rightarrow 0} \frac{\sqrt{1+\operatorname{tg} x}-\sqrt{1+\sin x}}{x^{3}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\operatorname{tg} x-\sin x}{x^{3}(\sqrt{1+\operatorname{tg} x}+\sqrt{1+\sin x})} \\
& =\lim _{x \rightarrow 0} \frac{\sin x(1-\cos x)}{x^{3} \cos x(\sqrt{1+\operatorname{tg} x}+\sqrt{1+\sin x})}
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\sin x}{x} \cdot \frac{2 \sin ^{2} \frac{x}{2}}{4\left(\frac{x}{2}\right)^{2}} \\
& \frac{1}{\cos x(\sqrt{1+\operatorname{tg} x}+\sqrt{1+\sin x})} \\
& =\frac{1}{4} .
\end{aligned}
$$

500. $\lim _{x \rightarrow 0} \frac{x^{2}}{\sqrt{1+x \sin x}-\sqrt{\cos x}}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 0} \frac{x^{2}}{\sqrt{1+x \sin x}-\sqrt{\cos x}} \\
= & \lim _{x \rightarrow 0} \frac{x^{2}\left(\sqrt{1+x \sin x}+\frac{\sqrt{\cos x})}{\sqrt{1+x \sin x}-\sqrt{\cos x}}\right.}{=} \\
= & \lim _{x \rightarrow 0} \frac{\sqrt{1-x \sin x}+\sqrt{\cos x}}{\frac{\sin x}{x}+\frac{2 \sin ^{2} \frac{x}{2}}{x^{2}}}=\frac{4}{3} .
\end{aligned}
$$

501. $\lim _{x \rightarrow 0} \frac{\sqrt{\cos x}-\sqrt[3]{\cos x}}{\sin ^{2} x}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sqrt{\cos x}-\sqrt[3]{\cos x}}{\sin ^{2} x} \\
= & \lim _{x \rightarrow 0} \frac{-\sqrt[3]{\cos x}(1-\sqrt[6]{\cos x})}{\sin ^{2} x} \\
= & -\lim _{x \rightarrow 0} \frac{1-\cos x}{\sin ^{2} x} \cdot \frac{\cdots}{1+\sqrt[6]{\cos x}+\cdots+\sqrt[6]{\cos ^{5} x}} \\
= & -\lim _{x \rightarrow 0} \frac{2 \sin ^{2} \frac{x}{2}}{4\left(\frac{x}{2}\right)^{2}} \cdot \frac{x^{2}}{\sin ^{2} x} .
\end{aligned}
$$

$$
\begin{aligned}
& 1+\sqrt[6]{\cos x}+\cdots+\sqrt[8]{\cos ^{5} x} \\
& =1
\end{aligned}
$$

502. $\lim _{x \rightarrow 0} \frac{\sqrt{1-\cos x^{2}}}{1-\cos x}$.

$$
\text { 解 } \begin{aligned}
& \lim _{x \rightarrow 0} \frac{\sqrt{1-\cos x^{2}}}{1-\cos x}=\lim _{x \rightarrow 0} \frac{\sqrt{2} \sin \frac{x^{2}}{2}}{2 \sin ^{2} \frac{x}{2}} \\
&=\sqrt{2} \lim _{x \rightarrow 0} \frac{\sin \frac{x^{2}}{2}}{\frac{x^{2}}{2}} \cdot\left[\frac{\frac{x}{2}}{\sin \frac{x}{2}}\right]^{2}=\sqrt{2} .
\end{aligned}
$$

503. $\lim _{x \rightarrow 0} \frac{1-\sqrt{\cos x}}{1-\cos (\sqrt{x})}$.

解 $\lim _{x \rightarrow 0} \frac{1-\sqrt{\cos x}}{1-\cos (\sqrt{x})}=\lim _{x \rightarrow 0} \frac{1-\cos x}{2 \sin ^{2} \frac{\sqrt{x}}{2}(1+\sqrt{\cos x})}$

$$
=-\frac{1}{2} \lim _{x \rightarrow 0}\left(\frac{\sin \frac{x}{2}}{\frac{x}{2}}\right)^{2} \cdot\left[\frac{\frac{\sqrt{x}}{2}}{\sin \frac{\sqrt{x}}{2}}\right)^{2} \cdot \frac{x}{1+\sqrt{\cos x}}=0 .
$$

504. $\lim _{x \rightarrow 0} \frac{1}{\cos x \sqrt{\cos 2 x} \sqrt[3]{\cos 3 x}} x^{2}$.

解 不妨令 $x \in\left(-\frac{\pi}{4}, \frac{\pi}{4}\right)$ ，则

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{1-\cos x \sqrt{\cos 2 x} \sqrt[3]{\cos 3 x}}{x^{2}} \\
& =\lim _{x \rightarrow 0} \frac{1-\cos x+\cos x(1-\sqrt{\cos 2 x} \cdot \sqrt[3]{\cos 3 x})}{x^{2}}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2}+\lim _{x \rightarrow 0} \frac{1-\sqrt{\cos 2 x}+\sqrt{\cos 2 x}(1-\sqrt[3]{\cos 3 x})}{x^{2}} \\
= & \frac{1}{2}+\lim _{x \rightarrow 0} \frac{1-\cos 2 x}{x^{2}(1+\sqrt{\cos 2 x})} \\
& +\lim _{x \rightarrow 0} \frac{1-\cos 3 x}{x^{2}\left(1+\sqrt[3]{\cos 3 x}+\sqrt[3]{\cos ^{2} 3 x}\right)}=3 .
\end{aligned}
$$

505. $\lim _{x \rightarrow+\infty}(\sin \sqrt{x+1}-\sin \sqrt{x})$.

解 $\sin \sqrt{x+1}-\sin \sqrt{x}$

$$
=2 \sin \frac{\sqrt{x+1}-\sqrt{x}}{2} \cos \frac{\sqrt{x+1}+\sqrt{x}}{2} .
$$

$$
\text { 因为 } \sqrt{x+1}-\sqrt{x}=\frac{1}{\sqrt{x+1}+\sqrt{x}} \rightarrow 0
$$

$(x \rightarrow+\infty)$, 所以,

$$
\sin \frac{\sqrt{x \pm 1}-\sqrt{x}}{2} \rightarrow 0 \quad(x \rightarrow+\infty)
$$

又因 $\left|\cos \frac{\sqrt{x+1}-\sqrt{x}}{2}\right| \leqslant 1$.
故 $\quad \lim _{x \rightarrow+\infty}(\sin \sqrt{x+1}-\sin \sqrt{x})=0$.
506. (a) $\lim _{x \rightarrow 0}\left(\frac{1+x}{2+x}\right)^{\frac{1--\sqrt{x}}{1-x}}$; (6) $\lim _{x \rightarrow 1}\left(\frac{1+x}{2+x}\right)^{\frac{1-\sqrt{x}}{1-x}}$;
(в) $\lim _{x \rightarrow+\infty}\left(\frac{1+x}{2+x}\right)^{\frac{1-\sqrt{x}}{1-x}}$.

解 (a) $\lim _{x \rightarrow 0}\left(\frac{1+x}{2+x}\right)^{\frac{1-\sqrt{x}}{1-\frac{1}{x}}}=\frac{1}{2}$ ；

$$
\begin{aligned}
& \text { (6) } \lim _{x \rightarrow 1}\left(\frac{1+x}{2+x}\right)^{\frac{1-\sqrt{x}}{1-x}} \\
& =\lim _{x \rightarrow 1}\left(\frac{1+x}{2+x}\right)^{\frac{1}{1+\sqrt{x}}}=\sqrt{\frac{2}{3}} ;
\end{aligned}
$$

$$
\begin{aligned}
& \text { (B) } \lim _{x \rightarrow+\infty}\left(\frac{1+x}{2+x}\right)^{\frac{1-\frac{\sqrt{x}}{1-x}}{1}} \\
& =\lim _{x \rightarrow+\infty}\left(\frac{1+x}{2+x}\right)^{\frac{1}{1+\sqrt{x}}}=1^{0}=1,
\end{aligned}
$$

507. $\lim _{x \rightarrow \infty}\left(\frac{x+2}{2 x-1}\right)^{x^{2}}$.

解 $\lim _{x \rightarrow \infty}\left(\frac{x+2}{2 x-1}\right)^{x^{2}}=0$ 。
508. $\lim _{x \rightarrow \infty}\left(\frac{3 x^{2}-x+1}{2 x^{2}+x+1}\right)^{\frac{x^{3}}{1-x}}$.

解 因为当 $x \rightarrow \infty$ 时，

$$
\frac{3 x^{2}-x+1}{2 x^{2}+x+1} \rightarrow \frac{3}{2} .
$$

及
所以

$$
\frac{x^{3}}{1-x}=\frac{x^{2}}{\frac{1}{x}-1} \rightarrow-\infty,
$$

$$
\lim _{x \rightarrow \infty}\left(\frac{3 x^{2}-x+1}{2 x^{2}+x+1}\right)^{\frac{x^{3}}{1-x}}=0 .
$$

509. $\lim _{x \rightarrow \infty}\left(\sin ^{n} \frac{2 \pi n}{3 n+1}\right)$.

䄈 因为 $\left|\sin \frac{2 \pi n}{3 n+1}\right| \leqslant 1$, 所以

$$
\operatorname{limsin}_{n \rightarrow \infty} \frac{2 \pi n}{3 n+1}=0 .
$$

510. $\lim _{x \rightarrow \frac{\pi}{4}+0}\left[\operatorname{tg}\left(\frac{\pi}{8}+x\right)\right]^{\operatorname{tg} 2 x}$.

解 因为当 $x \rightarrow \frac{\pi}{4}+0$ 时，

$$
1<\operatorname{tg}\left(\frac{\pi}{8}+x\right)<+\infty
$$

及 $\operatorname{tg} 2 x \rightarrow-\infty$ 。
所以

$$
\lim _{x \rightarrow \frac{\pi}{4}+0}\left[\operatorname{tg}\left(\frac{\pi}{3}+x\right)\right]^{\operatorname{tg} \hat{x} x}=0
$$

511. $\lim _{x \rightarrow \infty}\left(\frac{x^{2}-1}{x^{2}+1}\right)^{\frac{x-1}{x+1}}$.

解 $\lim _{x \rightarrow \infty}\left(\frac{x^{2}-1}{x^{2}+1}\right)^{\frac{x-1}{x+1}}=1$.
512. $\lim _{x \rightarrow \infty}\left(\frac{x^{2}+1}{x^{2}-1}\right)^{x^{2}}$.

解 $\lim _{x \rightarrow \infty}\left(\frac{x^{2}+1}{x^{2}-1}\right)^{x^{2}}=\lim _{x \rightarrow \infty}\left(1+\frac{1}{\frac{x^{2}-1}{2}}\right)^{\frac{x^{2}-1}{2} \cdot z+1}=e^{2}$.
513. $\left.\lim _{x \rightarrow+\infty} \left\lvert\, \frac{x^{2}+2 x-1}{2 x^{2}-3 x-2}\right.\right)^{\frac{1}{x}}$.

解 $\lim _{x \rightarrow \infty}\left(\frac{x^{2}+2 x-1}{2 x^{2}-3 x-2}\right)^{\frac{1}{x}}=\left(\frac{1}{2}\right)^{0}=1$.
514. $\lim _{x \rightarrow 0} \sqrt[x]{1-2 x}$.

解 $\lim _{x \rightarrow 0} \sqrt[f]{1-2 x}=\lim _{x \rightarrow 0}[1+(-2 x)]^{\frac{1}{-2 x}}(-2)=e^{-2}$.
515. $\lim _{x \rightarrow \infty}\left(\frac{x+a}{x-a}\right)^{x}$.

解 $\lim _{x \rightarrow \infty}\left(\frac{x+a}{x-a}\right)^{x}=\lim _{x \rightarrow \infty}\left(1+\frac{1}{\frac{x-a}{2 a}}\right)^{\frac{x-a}{2 a} \cdot 2 a+a}=e^{2 a}$.
516. $\lim _{x \rightarrow+\infty}\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{2}}\right)^{*}\left(a_{1}>0, a_{2}>0\right)$.

解 $\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{3}}\right)^{x}=\left(\frac{a_{1}}{a_{2}}\right)^{x} \cdot\left(\frac{x+\frac{b_{1}}{a_{1}}}{x+\frac{b_{2}}{a_{2}}}\right)^{x}$
$=\left(\frac{a_{1}}{a_{2}}\right)^{x} \cdot\left(1+\frac{1}{x+\frac{b_{2}}{a_{2}}}\right) \frac{\frac{x+\frac{b_{2}}{a_{2}}}{\frac{b_{1}}{a_{1}}-\frac{b_{2}}{a_{2}}}\left(\frac{b_{1}}{a_{1}}-\frac{b_{2}}{a_{2}}\right)}{\frac{b_{1}}{a_{1}}-\frac{b_{2}}{a_{2}}}$
（1）当 $a_{1}=a_{2}=a$ 时，
$\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{2}}\right)^{x}=\left(1+\frac{1}{x+\frac{b_{2}}{a}}\right) \frac{\frac{x+\frac{b_{2}}{a}}{\frac{b_{1}-b_{2}}{a}} \cdot \frac{b_{1}-b_{2}}{a}-\frac{b_{2}}{a}}{\frac{b_{1}-b_{2}}{a}}$
干是，

$$
\lim _{x \rightarrow \infty}\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{2}}\right)^{x}=e^{\frac{b_{1}-b_{2}}{a_{1}}} .
$$

(2) 当 $a_{1}<a_{2}$ 时, $0<\frac{a_{1}}{a_{2}}<1$,

干是，

$$
\left(\frac{a_{1}}{a_{2}}\right)^{*} \rightarrow 0 \quad(x \rightarrow+\infty)
$$

而 $\quad\left(\frac{x+\frac{b_{1}}{a_{1}}}{x+\frac{b_{2}}{a_{2}}}\right)^{x} \rightarrow e^{\frac{b_{1}}{a_{1}}-\frac{b_{z}}{a_{2}}}$,
所以

$$
\lim _{x \rightarrow-\infty}\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{2}}\right)^{x}=0
$$

（3）当 $a_{1}>a_{2}$ 时， $\frac{a_{1}}{a_{2}}>1$ 。于是，

$$
\left(\frac{a_{1}}{a_{2}}\right)^{x} \rightarrow+\infty
$$

所以

$$
\lim _{x \rightarrow+\infty}\left(\frac{a_{1} x+b_{1}}{a_{2} x+b_{2}}\right)^{x}=+\infty
$$

517. $\lim _{x \rightarrow 0}\left(1+x^{2}\right)^{\operatorname{cts}^{2} x}$.

解 $\lim _{x \rightarrow 0}\left(1+x^{2}\right)^{\cot ^{2} x}$
$=\lim _{x \rightarrow 0}\left(1+x^{2}\right)^{\frac{1}{2}} \cdot\left(\frac{x}{\sin }\right)^{2} \cdot \cos ^{2} x=e$.
518. $\lim _{x \rightarrow 1}(1+\sin \pi x)^{\operatorname{ctg} x x}$.

解 $\lim _{x \rightarrow 1}(1+\sin \pi x)^{\text {these } x}$
$=\lim _{x \rightarrow 1}(1+\sin \pi x)^{\frac{1}{\operatorname{sintrx}}+\cos \pi x}=e^{-1}$.
519. $\lim _{x \rightarrow 0}\left(\frac{1+\operatorname{tg} x}{1+\sin x}\right)^{\frac{1}{\sin x}}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-296.jpg?height=444&width=1401&top_left_y=1751&top_left_x=339)
520. $\lim _{x \rightarrow \infty}\left(\frac{\sin x}{\sin a}\right)^{\frac{1}{x-a}}$.

解 $\lim _{x \rightarrow \alpha}\left(\frac{\sin x}{\sin a}\right)^{\frac{1}{x-a}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow a}\left(1+\frac{1}{\frac{\sin a}{\sin x-\sin a}}\right)^{\frac{\sin a}{\sin x-\sin a} \frac{\sin x-\sin a}{x-a} \cdot \frac{1}{\operatorname{tin} a}} \\
& =e^{\left(\operatorname{ctg}{ }^{*}\right)}(a \neq k \pi ; k=0, \pm 1, \pm 2, \cdots)
\end{aligned}
$$

* ) 利用 482 题的结果.

521. $\lim _{x \rightarrow 0}\left(\frac{\cos x}{\cos 2 x}\right)^{\frac{1}{x^{2}}}$.

情 $\left(\frac{\cos x}{\cos 2 x}\right)^{\frac{1}{x^{2}}}=\left(1+\frac{1}{\frac{\cos 2 x}{\cos x-\cos 2 x}}\right)^{\frac{\cos 2 x}{\cos x-\cos 2 x} \cdot \frac{\cos x-\cos 2 x}{x^{2} \cos 2 x}}$
因为

$$
\begin{aligned}
& \frac{\cos x-\cos 2 x}{x^{2}}=\frac{\cos x+1-2 \cos ^{2} x}{x^{2}} \\
& =\frac{1-\cos x}{x^{2}}(1+2 \cos x)=\frac{1+2 \cos x}{2} \cdot\left(\frac{\sin \frac{x}{2}}{\frac{x}{2}}\right)^{2} \rightarrow \frac{3}{2} \\
& \quad(x \rightarrow 0)
\end{aligned}
$$

所以，

$$
\lim _{x \rightarrow 0}\left(\frac{\cos x}{\cos 2 x}\right)^{\frac{1}{x^{2}}}=e^{\frac{3}{2}}
$$

522. $\lim (\operatorname{tg} x)^{\operatorname{tg} 2 x}$.
$x \rightarrow \frac{\pi}{4}$
解 $\lim (\operatorname{tg} x)^{\operatorname{tg} 2 x}=\lim (\operatorname{tg} x)^{\frac{3 \operatorname{tg} x}{2}}$ $x \rightarrow \frac{\pi}{4} \quad x \rightarrow \frac{\pi}{4}$
$=\lim _{x \rightarrow \frac{\pi}{4}}(1+\operatorname{tg} x-1)^{\frac{1}{\operatorname{tg} x-1} \cdot} \cdot \frac{-24 x}{4 x+1}=e^{-1}$.
523. $\lim (\sin x)^{\operatorname{trx} x}$ 。
$x \rightarrow \frac{\pi}{2}$

解 $\lim _{x}(\sin x)^{\operatorname{tg} x}=\lim \left(1+\operatorname{ctg}^{2} x\right)^{-\frac{\lg x}{2}}$
524. $\lim _{x \rightarrow 0}\left[\operatorname{tg}\left(\frac{\pi}{4}-x\right)\right]^{\operatorname{cig} \mathrm{I}}$.

解 $\lim _{x \rightarrow 0}\left[\operatorname{tg}\left(\frac{\pi}{4}-x\right)\right]^{\operatorname{ctg} x}=\lim _{x \rightarrow 0}\left(\frac{1-\operatorname{tg} x}{1+\operatorname{tg} x}\right)^{\operatorname{tgg} x}$

$$
=\lim _{x \rightarrow 0}\left(1+\frac{1}{\frac{1+\operatorname{tg} x}{-2 \operatorname{tg} x}}\right)^{\left.\frac{1+\operatorname{tg} x}{2 \cdot \lg x} \cdot \frac{-2}{1+\operatorname{lax} x^{2}}\right)}=e^{-z}
$$

525. $\lim _{x \rightarrow \infty}\left(\sin \frac{1}{x}+\cos \frac{1}{x}\right)^{x}$.

解 $\left(\sin \frac{1}{x}+\cos \frac{1}{x}\right)^{x}$
$=\left(1+\left(\sin \frac{1}{x}+\cos \frac{1}{x}-1\right)\right)^{\frac{1}{\sin \frac{1}{x}+\cos \frac{1}{x}-1}-\operatorname{cr}\left(\sin \frac{1}{x}+\cos \frac{1}{x}-1\right)}$
因为

$$
\begin{aligned}
& x\left(\sin \frac{1}{x}+\cos \frac{1}{x}-1\right)=\frac{\sin \frac{1}{x}}{\frac{1}{x}}-\frac{2 \sin \frac{1}{2 x} \sin \frac{1}{2 x}}{\frac{1}{2 x} \cdot 2} \\
& \rightarrow 1 \quad(x \rightarrow \infty),
\end{aligned}
$$

所以

$$
\lim _{x \rightarrow \infty}\left(\sin \frac{1}{x}+\cos \frac{1}{x}\right)^{x}=e
$$

526. $\lim _{x \rightarrow+0} \sqrt[x]{\cos \sqrt{x}}$.

解 $\lim _{x \rightarrow+\infty} \sqrt[x]{\cos \sqrt{x}}=\lim _{x \rightarrow+\infty} e^{\frac{1}{x} \cdot \ln \text { eses }} \sqrt{x}$

$$
\begin{aligned}
& =\lim _{x \rightarrow+0} e^{\left.-\frac{1}{x} \cdot 2 \sin ^{2} \frac{\sqrt{x}}{2} \cdots\right)}=e^{-\frac{1}{2} .}
\end{aligned}
$$

*) 原题为 $x \rightarrow 0$, 应改为 $x \rightarrow+0$ 。

* *) 利用 529 题的结果.

527. $\lim _{n \rightarrow \infty}\left(\frac{n+x}{n-1}\right)^{n}$.

解 $\lim _{n \rightarrow \infty}\left(\frac{n+x}{n-1}\right)^{n}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{\frac{n-1}{x+1}}\right)^{\frac{n-1}{x+1} \cdot(x+1)+1}=e^{x+1}$.
528. $\lim _{n \rightarrow \infty} \cos ^{x} \frac{x}{\sqrt{n}}$.

解 $\lim _{n \rightarrow \infty} \cos ^{*} \frac{x}{\sqrt{n}}=\lim _{n \rightarrow \infty}\left(1+\operatorname{tg}^{2} \frac{x}{\sqrt{n}}\right)^{-\frac{\pi}{2}}$
529. $\lim _{x \rightarrow 0} \frac{\ln (1+x)}{x}$.

解 $\lim _{x \rightarrow 0} \frac{\ln (1+x)}{x}=\lim _{x \rightarrow 0} \ln (1+x)^{\frac{1}{x}}=\ln e=1$.
530. $\lim _{x \rightarrow+\infty} x[\operatorname{lin}(x+1)-\ln x]$.

$$
\text { 解 } \begin{aligned}
\lim _{x \rightarrow+\infty} x[\ln (x+1)-\ln x] & =\lim _{x \rightarrow+\infty} \ln \left(1+\frac{1}{x}\right)^{x} \\
& =\ln e=1 .
\end{aligned}
$$

531. $\lim _{x \rightarrow a} \frac{\ln x-\ln a}{x \cdots a} \quad(a>0)$.

解 $\lim _{x \rightarrow a} \frac{\ln x-\ln a}{x-a}=\lim _{x \rightarrow a} \frac{\ln \frac{x}{a}}{x-a}$

$$
=\operatorname{limln}_{x \rightarrow a}\left(1+\frac{1}{\frac{a}{x-a}}\right)^{\frac{a}{x-a} \cdot \frac{1}{a}}=\ln e^{\frac{1}{a}}=\frac{1}{a} .
$$

532. $\lim _{x \rightarrow+\infty}[\sin \ln (x+1)-\sin \ln x]$.

解 $\sin \ln (x+1)-\sin \ln x$

$$
=2 \cos \frac{\ln (x+1)+\ln x}{2} \sin \frac{\ln (x+1)-\ln x}{2} .
$$

因为

$$
\ln (x+1)-\ln x=\ln \left(1+\frac{1}{x}\right) \rightarrow 0(x \rightarrow+\infty),
$$

所以

$$
\sin \frac{\ln (x+1)-\ln x}{2} \rightarrow 0 ;
$$

又因 $\cos \frac{\ln (x+1)+\ln x}{2}$ 为有界函数，所以

$$
\lim _{x \rightarrow+\infty}[\sin \ln (x+1)-\sin \ln x]=0
$$

533. $\lim _{x \rightarrow+\infty} \frac{\ln \left(x^{2}-x+1\right)}{\ln \left(x^{10}+x+1\right)}$.

解 $\lim _{x \rightarrow+\infty} \frac{\ln \left(x^{2}-x+1\right)}{\ln \left(x^{10}+x+1\right)}$

$$
\begin{aligned}
& =\lim _{x \rightarrow+\infty} \frac{2 \ln x+\ln \left(1-\frac{1}{x}+\frac{1}{x^{2}}\right)}{10 \ln x+\ln \left(1+\frac{1}{x^{9}}+\frac{1}{x^{10}}\right)} \\
& =\lim _{x \rightarrow+\infty} \frac{2+\frac{1}{\ln x} \cdot \ln \left(1+\frac{1}{x^{2}}-\frac{1}{x}\right)}{10+\frac{1}{\ln x} \cdot \ln \left(1+\frac{1}{x^{9}}+\frac{1}{x^{10}}\right)}=\frac{1}{5} .
\end{aligned}
$$

534. $\lim _{x \rightarrow \infty}\left(\lg \frac{100+x^{2}}{1+100 x^{2}}\right)$.

$$
\text { 解 } \quad \lim _{x \rightarrow \infty}\left(\lg \frac{100+x^{2}}{1+100 x^{2}}\right)=\lg \frac{1}{100}=-2 \text {. }
$$

535. $\quad \lim _{x \rightarrow+\infty} \frac{\ln \left(2+e^{3 x}\right)}{\ln \left(3+e^{2 x}\right)}$

解 $\lim _{x \rightarrow \infty} \frac{\ln \left(2+e^{3 x}\right)}{\ln \left(3+e^{2 x}\right)}=\lim _{x \rightarrow+\infty} \frac{3 x+\ln \left(2 e^{-3 x}+1\right)}{2 x+\ln \left(3 e^{-2 x}+1\right)}$

$$
\Longrightarrow \lim _{x \rightarrow+\infty} \frac{3+\frac{1}{x} \ln \left(2 e^{-3 x}+1\right)}{2+\frac{1}{x} \ln \left(3 e^{-z x}+1\right)}=\frac{3}{2} .
$$

536. $\lim _{x \rightarrow+\infty} \frac{\ln (1+\sqrt{x}+\sqrt[3]{x})}{\ln (1+\sqrt[3]{x}+\sqrt[3]{x})}$.

解 $\lim _{x \rightarrow+\infty} \frac{\ln (1+\sqrt{x}+\sqrt[3]{x})}{\ln (1+\sqrt[3]{x}+\sqrt[4]{x})}$.

$$
\begin{aligned}
& =\lim _{x \rightarrow+\infty} \frac{\frac{1}{2} \ln x+\ln \left(x^{-\frac{1}{2}}+1+x^{-\frac{1}{6}}\right)}{\frac{1}{3} \ln x+\ln \left(x^{-\frac{1}{3}}+1+x^{-\frac{1}{12}}\right)} \\
& =\lim _{x \rightarrow+\infty} \frac{\frac{1}{2}+\frac{1}{\ln x} \cdot \ln \left(x^{-\frac{1}{2}}+1+x^{-\frac{1}{6}}\right)}{\frac{1}{3}+\frac{1}{\ln x} \cdot \ln \left(x^{-\frac{1}{2}}+1+x^{-\frac{1}{12}}\right)}=\frac{3}{2} .
\end{aligned}
$$

537. $\lim _{h \rightarrow 0} \frac{\log (x+h)+\log (x-h)-2 \log x}{h^{2}}(x>0)$.

䍈 $\lim _{h \rightarrow 0} \frac{\log (x+h)+\log (x-h) \div 2 \log x}{h^{2}}$

$$
=\lim _{h \rightarrow 0} \frac{\log \left(x^{3}-h^{2}\right)-\log x^{2}}{h^{2}}
$$

$=\lim _{h \rightarrow 0}\left[-\frac{1}{x^{2}} \log \left(1-\frac{h^{2}}{x^{2}}\right)^{-\frac{x^{2}}{h^{2}}}\right)=-\frac{1}{x^{2}} \log e$.
538. $\lim _{x \rightarrow 0} \frac{\operatorname{lntg}\left(\frac{\pi}{4}+a x\right)}{\sin b x}$.

$$
\begin{aligned}
& \text { 解 } \quad \lim _{x \rightarrow 0} \frac{\operatorname{lntg}\left(\frac{\pi}{4}+a x\right)}{\sin b x} \\
& =\lim _{x \rightarrow 0} \ln \left[1+\left(\operatorname{tg}\left(\frac{\pi}{4}+a x\right)-1\right)\right] \frac{1}{\sin b x} \\
& = \\
& =\lim _{x \rightarrow 0} \ln \left[1+\frac{\sin \left(\frac{\pi}{4}+a x\right)-\cos \left(\frac{\pi}{4}+a x\right)}{\cos \left(\frac{\pi}{4}+a x\right)}\right]_{x \rightarrow 0}^{\frac{\frac{\pi}{4}}{\sin 6 x}} \\
& = \\
& =
\end{aligned}
$$

539. $\lim _{x \rightarrow 0} \frac{\ln \cos a x}{\ln \cos b x}$.

解 $\lim _{x \rightarrow 0} \frac{\ln \cos a x}{\ln \cos b x}$

$$
=\lim _{x \rightarrow 0}\left(\frac{\ln \cos a x}{\cos a x-1} \cdot \frac{\cos b x-1}{\ln \cos b x} \cdot \frac{\cos a x-1}{\cos b x-1}\right)
$$

$$
=\lim _{x \rightarrow 0} \frac{2 \sin ^{2} \frac{a x}{2}}{2 \sin ^{2} \frac{b x}{2}}=\frac{\alpha^{2}}{b^{2}} .
$$

$540^{+} \lim _{x \rightarrow 0}\left[\ln \frac{n x+\sqrt{1-n^{2} x^{2}}}{x+\sqrt{1-x^{2}}}\right]$.
解 $\lim _{x \rightarrow 0}\left[\ln \frac{n x+\sqrt{1-n^{2} x^{2}}}{x+\sqrt{1-x^{2}}}\right)=\ln 1=0$.
541. $\lim _{x \rightarrow 0} \frac{a^{x}-1}{x}(a>0)$.

解 设 $a^{x}-1=y$ ，则

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\lim _{y \rightarrow 0} \frac{y}{\log _{a}(1+y)}=\lim _{y \rightarrow 0} \frac{1}{\log _{a}(1+y)^{\frac{1}{y}}} \\
= & \frac{1}{\log _{a} e}=\ln a .
\end{aligned}
$$

542. $\lim _{x \rightarrow a} \frac{a^{x}-x^{a}}{x-a}(a>0)$.

解 $\frac{a^{x}-x^{a}}{x-a}=\frac{a^{a}\left(a^{x \cdot a}-\left(\frac{x}{a}\right)^{a}\right]}{x-a}$
$=a^{\pi} \cdot \frac{a^{x-a}-1}{x-a}-a^{e} \frac{\left(\frac{x}{a}\right)^{a}-1}{x-a}$
$=a^{a} \frac{a^{x-a}-1}{x-a}-a^{a} \frac{e^{x \ln \frac{x}{a}}-1}{a \ln \frac{x}{a}} \cdot \frac{a \ln \left(1+\frac{x-a}{a}\right)}{x-a}$,
当 $x \rightarrow a$ 时,等式第一项趋向 $a^{\alpha} \ln a$ ，而第二项趋向 $a^{a} \cdot 1$
$\cdot 1=a^{a}$ ，所以，

$$
\lim _{x \rightarrow a} \frac{a^{x}-x^{a}}{x-a}=a^{a} \ln a-a^{a}=a^{a} \ln \frac{a}{e}
$$

543. $\lim _{x \rightarrow a} \frac{x^{x}-a^{a}}{x-a} \quad(a>0)$.

解 $\frac{x^{x}-a^{a}}{x-a}=a^{a} \cdot \frac{e^{\ln x-a \ln }-1}{x \ln x-a \ln a} \cdot \frac{x \ln x-a \ln a}{x-a}$.
而当 $x \rightarrow a$ 时，

$$
\begin{aligned}
& \frac{x \ln x-a \ln a}{x-a}=\frac{x \ln x-x \ln a}{x-a}+\ln a \\
= & \frac{x}{a} \cdot \frac{\ln \left(1+\frac{x-a}{a}\right)}{\frac{x-a}{a}}+\ln a \rightarrow 1+\ln a=\ln e a .
\end{aligned}
$$

又

$$
\frac{e^{x \ln x-4 \ln x}-1}{x \ln x-a \ln a} \rightarrow 1(x \rightarrow a),
$$

## 所以

$$
\lim _{x \rightarrow a} \frac{x^{x}-a^{a}}{x-a}=a^{a} \ln e a .
$$

544. $\lim _{x \rightarrow 0}\left(x+e^{x}\right)^{\frac{1}{x}}$.

解 $\lim _{x \rightarrow 0}\left(x+e^{x}\right)^{\frac{1}{x}}=\lim _{x \rightarrow 0} e\left(1+\frac{x}{e^{x}}\right)^{\frac{x^{\frac{x}{x}} \cdot e^{-x}}{x}}=e \cdot e=e^{2}$.
545. $\lim _{x \rightarrow 0}\left(\frac{1+x \cdot 2^{x}}{1+x \cdot 3^{x}}\right)^{\frac{1}{x^{2}}}$.

晖 $\left(\frac{1+x \cdot 2^{x}}{1+x \cdot 3^{x}}\right)^{\frac{1}{x^{2}}}$

$$
=\left(1+\frac{1}{\frac{1+x \cdot 3^{x}}{x\left(2^{x}-3^{x}\right)}}\right)^{\frac{1+2 \cdot-3^{x}}{x\left(z^{x}-3^{x}\right)} \cdot \frac{x^{x}-3^{x}}{x\left(1+x \cdot 3^{2}\right)}} .
$$

因为

$$
\begin{aligned}
& \frac{2^{x}-3^{x}}{x\left(1+x \cdot 3^{x}\right)} \\
= & \frac{1}{1+x \cdot 3^{x}} \cdot\left(\frac{2^{x}-1}{x}-\frac{3^{x}-1}{x}\right) \rightarrow \\
\left.\ln 2-\ln 3^{*}\right) & \ln \frac{2}{3} \quad(x \rightarrow 0),
\end{aligned}
$$

所以

$$
\lim _{x \rightarrow 0}\left(\frac{1+x \cdot 2^{x}}{1+x \cdot 3^{x}}\right)^{\frac{1}{x^{2}}}=e^{\ln \frac{2}{3}}=\frac{2}{3}
$$

*) 利用 541 题的结果.
546. $\lim _{n \rightarrow \infty} \operatorname{tg}^{-}\left(\frac{\pi}{4}+\frac{1}{n}\right)$.

解 $\lim _{n \rightarrow \infty} \operatorname{tg}^{n}\left(\frac{\pi}{4}+\frac{1}{n}\right)=\lim _{n \rightarrow \infty}\left(\frac{1+\operatorname{tg} \frac{1}{n}}{1-\operatorname{tg} \frac{1}{n}}\right)^{n}$
547. $\lim _{x \rightarrow 0} \frac{e^{a x}-e^{\beta x}}{\sin \alpha x-\sin \beta x}$.

解 $\lim _{x \rightarrow \alpha} \frac{e^{\alpha x}-e^{\beta t}}{\sin \alpha x-\sin \beta x}=\lim _{x \rightarrow 0} \frac{e^{\beta x}\left[e^{(a \cdot \beta) x}-1\right]}{2 \cos \frac{a+\beta}{2} x \sin \frac{\alpha-\beta}{2} x}$

$$
=\lim _{x \rightarrow 0} \frac{e^{(\alpha-\beta) x}-1}{(\alpha-\beta) x} \cdot \frac{\frac{\alpha-\beta}{2} x}{\sin \frac{a-\beta}{2} x} \cdot \frac{e^{\beta x}}{\cos \frac{\alpha+\beta}{2} x}
$$

$$
=\ln e^{*)}=1
$$

*）利用 541 题的结果.
548. $\lim _{x \rightarrow a} \frac{x^{\alpha}-a^{\alpha}}{x^{\beta}-a^{\beta}} \quad(a>0)$.

算 $\frac{x^{\alpha}-a^{\alpha}}{x^{\beta}-a^{\beta}}=a^{-\beta} \cdot \frac{\left(\frac{x}{a}\right)^{a}-1}{\left(\frac{x}{a}\right)^{\beta}-1}$ 。

$$
=a^{-\beta} \cdot \frac{e^{\alpha \ln \frac{x}{a}}-1}{\alpha \ln \frac{x}{a}} \cdot \frac{\beta \ln \frac{x}{a}}{e^{\alpha_{0} \frac{x}{a}}-1} \cdot \frac{\alpha}{\beta} .
$$

当 $x \rightarrow a$ 时, $\ln \frac{x}{a} \rightarrow 0$ ，于是上式趋向 $\frac{\alpha}{\beta} a^{-\beta}$,

即

$$
\lim _{x \rightarrow a} \frac{x^{c}-a^{\alpha}}{x^{\beta}-a^{\beta}}=\frac{a}{\beta} a^{a-\beta} \quad(\beta \neq 0) .
$$

549. $\lim _{x \rightarrow b} \frac{a^{x}-a^{b}}{x-b} \quad(a>0)$.

解 $\lim _{x \rightarrow b} \frac{a^{x}-a^{b}}{x-b}=\lim _{x \rightarrow b} a^{b} \cdot \frac{a^{x-b}-1}{x-b}=a^{b} \ln a^{3}$.

* ) 利用 541 题的结果.

550. $\lim _{h \rightarrow 0} \frac{a^{x+h}+a^{x-h}-2 a^{x}}{h^{2}} \quad(a>0)$.

解 $\lim _{h \rightarrow 0} \frac{a^{x+h}+a^{x-k}-2 a^{x}}{h^{2}}=\lim _{h \rightarrow 0} a^{x} \cdot \frac{a^{\lambda}+a^{-h}-2}{h^{2}}$

$$
=\lim _{h \rightarrow 0} \frac{a^{x}}{a^{h}}\left(\frac{a^{h}-1}{h}\right)^{2}=a^{x} \ln ^{2} a^{*}
$$

*) 利用 541 题的结果.
551. $\lim _{x \rightarrow \infty} \frac{(x+a)^{x+a}(x+b)^{x+b}}{(x+a+b)^{2 x+a+k}}$.

解 $\lim _{x \rightarrow \infty} \frac{(x+a)^{x+a}(x+b)^{x+b}}{(x+a+b)^{x+a-b}}$
$=\lim _{x \rightarrow \infty} \frac{\left(1+\frac{a}{x}\right)^{x+a}\left(1+\frac{b}{x}\right)^{x+b}}{\left(1+\frac{a+b}{x}\right)^{2 x+*+b}}$.
$=\lim _{x \rightarrow \infty} \frac{\left(1+\frac{a}{x}\right)^{\frac{x}{a} a+a}\left(1+\frac{b}{x}\right)^{\frac{x}{b} b+b}}{\left(1+\frac{a+b}{x}\right)^{\frac{x}{a+b} \cdot[2(a+b)]+(a+b)}}$
$=\frac{e^{a} \cdot e^{b}}{e^{2(a+b)}}=e^{-(a+b)}$.
552. $\lim _{n \rightarrow \infty} n(\sqrt[n]{x}-1) \quad(x>0)$.

解 $\lim _{n \rightarrow \infty} n(\sqrt[n]{x}-1)=\lim _{n \rightarrow \infty} \frac{x^{\frac{1}{n}}-1}{\frac{1}{n}}=\ln x^{*}$.
*) 利用 541 题的结果。
553. $\lim _{n \rightarrow \infty} n^{2}(\sqrt[n]{x}-\sqrt[n+1]{x}) \quad(x>0)$.

解 $\lim _{x \rightarrow-\infty}(\sqrt[n]{x}-\sqrt[n+1]{x})$

$$
\begin{aligned}
& =\lim _{n \rightarrow \infty} \frac{x^{\frac{1}{2}}-x^{\frac{1}{x+1}}}{\frac{1}{n^{2}}}=\lim _{n \rightarrow \infty} \frac{x^{\frac{1}{x+1}}\left[x^{\frac{1}{n(x+1)}}-1\right]}{\frac{1}{n(n+1)}+\left(\frac{1}{n^{2}}-\frac{1}{n^{2}+n}\right)} \\
& =\lim _{n \rightarrow \infty} \frac{x^{\frac{1}{(n+1)}}-1}{\frac{1}{n(n+1)}} . \\
& \frac{x^{\frac{1}{n+1}} \cdot \frac{1}{n(n+1)}}{\frac{1}{n(n+1)}+\left(\frac{1}{n^{2}}-\frac{1}{n^{2}+n}\right)}=\ln x .
\end{aligned}
$$

554. $\lim _{n \rightarrow \infty}\left(\frac{a-1+\sqrt[n]{b}}{a}\right)^{\prime \prime} \quad(a>0, b>0)$.

解 $\lim _{a \rightarrow \infty}\left(\frac{a-1+\sqrt[2]{b}}{a}\right)^{n}$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-307.jpg?height=269&width=1028&top_left_y=1873&top_left_x=474)
$=\sqrt[9]{b}$.
555. $\lim _{n \rightarrow \infty}\left(\frac{\sqrt[2]{a}+\sqrt[2]{b}}{2}\right)^{\prime \prime} \quad(a>0, b>0)$.

解 $\lim _{x \rightarrow \infty}\left(\frac{\sqrt[n]{a}+\sqrt[n]{b}}{2}\right)^{*}$

$$
\begin{aligned}
& =e^{\left.\frac{1}{2}(\ln a+\ln b)^{-}\right)}=\sqrt{a b} \quad(a>0, b>0) . \\
& \text { *）利用 } 541 \text { 题的结果。 }
\end{aligned}
$$

556. $\lim _{x \rightarrow 0}\left(\frac{a^{x}+b^{x}+c^{x}}{3}\right)^{\frac{1}{x}} \quad(a>0, b>0, c>0)$.

解 利用 555 题的方法：

$$
\begin{aligned}
& \lim _{x \rightarrow 0}\left(\frac{a^{x}+b^{x}+c^{x}}{3}\right)^{\frac{1}{x}} \\
= & \lim _{x \rightarrow 0}\left(1+\frac{a^{x}+b^{x}+c^{x}}{3}-1\right) \frac{\frac{1}{a^{x}+b^{x}+x^{x}}-1}{3} \cdot \frac{a^{x}-1+b^{x}-1+c^{x}-1}{3 x} \\
= & \sqrt[3]{a b c} .
\end{aligned}
$$

557. $\lim _{x \rightarrow 0}\left(\frac{a^{x+1}+b^{x+1}+c^{x+1}}{a+b+c}\right)^{\frac{1}{x}} \quad(a>0, b>0, c>0)$.

解 利用 541 题的结果，得

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{a^{x+1}+b^{x-1}+c^{x+1}-a-b-c}{x(a+b+c)} \\
& =\frac{1}{a+b+c} \lim _{x \rightarrow 0}\left(a \cdot \frac{a^{x}-1}{x}+b \cdot \frac{b^{x}-1}{x}+c \cdot \frac{x^{x}-1}{x}\right) \\
& =\ln \left(a^{a} b^{b} c^{c}\right) \frac{1}{a+b+c},
\end{aligned}
$$

因而

$$
\begin{aligned}
& \lim _{x \rightarrow 0}\left(\frac{a^{x+1}+b^{x+1}+c^{x+1}}{a+b+c}\right)^{\frac{1}{x}} \\
= & \lim _{x \rightarrow 0}\left(1+\frac{a^{x+1}+b^{x+1}+c^{x+1}}{a+b+c}-1\right)\left(\frac{1}{\frac{a^{x+1}+b^{x+1}+c^{x+1}}{a+b+c}}\right) . \\
& -\frac{1}{x}\left(\frac{a^{x+1}+b^{x+1}+c^{x+1}}{a+b+c}-1\right)=\left(a^{x} b^{b} c^{c}\right)^{\frac{1}{a+b+c}} .
\end{aligned}
$$

558. $\lim _{x \rightarrow 0}\left(\frac{a^{x^{2}}-b^{x^{2}}}{a^{x}+b^{x}}\right)^{\frac{1}{x}} \quad(a>0, b>0)$,

解 $\lim _{x \rightarrow 0}\left(\frac{a^{x^{2}}-b^{x^{2}}}{a^{x}-b^{x}}\right)^{\frac{1}{x}}$
$=\lim _{x \rightarrow 0}\left(1+\frac{1}{\frac{a^{x}+b^{x}}{a^{x^{2}}+b^{2}-a^{x}-b^{x}}}\right) \cdot \frac{a^{x}+b^{x}}{a^{x^{2}}+b^{x^{2}}-a^{x}-b^{x}}$.
$\cdot\left[x\left(\frac{a^{x z}-1}{x^{2}}+\frac{k^{x z}-1}{x^{2}}\right)-\frac{a^{x}-1}{x}-\frac{b^{x}-1}{x}\right)-\frac{1}{a^{2}+\beta^{t}}$
$=e^{-\frac{1}{2}(\ln \alpha-\ln b)}=\frac{1}{\sqrt{a b}}$.
559. $\lim _{x \rightarrow 0} \frac{a^{x^{2}}-b^{x^{2}}}{\left(a^{x}-b^{x}\right)^{2}} \quad(a>0, b>0)$.

解 $\lim _{x \rightarrow 0} \frac{a^{x^{2}}-b^{x^{2}}}{\left(a^{x}-b^{x}\right)^{2}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0}\left(\frac{a^{x^{2}}-1}{x^{2}}-\frac{b^{x^{2}}-1}{x^{2}}\right) \cdot \frac{1}{\left(\frac{a^{\mp}-1}{x}-\frac{b^{x}-1}{x}\right)^{2}} \\
& =(\ln a-\ln b) \cdot \frac{1}{(\ln a-\ln b)^{2}}=\frac{1}{\ln a-\ln b} \\
& =\left(\ln \frac{a}{b}\right)^{-1}
\end{aligned}
$$

560. $\lim _{x \rightarrow a} \frac{a^{a^{x}}-a^{x^{a}}}{a^{x}-x^{a}} \quad(a>0)$.

令 $\lim _{x \rightarrow a} \frac{a^{a^{x}}-a^{x^{a}}}{a^{x}-x^{a}}=\lim _{x \rightarrow a} a^{a} \cdot \frac{a^{x}-x^{a}-1}{a^{x}-x^{a}}=a^{a} \ln a$.
561. (a) $\lim _{x \rightarrow-\infty} \frac{\ln \left(1+3^{x}\right)}{\ln \left(1+2^{x}\right)}$ ( ( 5 ) $\lim _{x \rightarrow+\infty} \frac{\ln \left(1+3^{x}\right)}{\ln \left(1+2^{x}\right)}$.

蛘 (a) $\lim _{x \rightarrow-\infty} \frac{\ln \left(1+3^{x}\right)}{\ln \left(1+2^{x}\right)}$

$$
=\lim _{x \rightarrow-\infty} \frac{\ln \left(1+3^{x}\right)}{3^{x}} \cdot \frac{2^{x}}{\ln (1+2 x)} \cdot\left(\frac{2}{3}\right)^{-x}
$$

$$
=1 \cdot 1 \cdot 0^{*)}=0
$$

* ）利用 529 题的结果。

$$
\text { (6) } \begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{\ln \left(1+3^{x}\right)}{\ln \left(1+2^{x}\right)}=\lim _{x \rightarrow+\infty} \frac{x \ln 3+\ln \left(1+3^{-x}\right)}{x \ln 2+\ln \left(1+2^{x}\right)} \\
= & \lim _{x \rightarrow+\infty} \frac{\ln 3+\frac{1}{x} \cdot \ln \left(1+3^{-x}\right)}{\ln 2+\frac{1}{x} \cdot \ln \left(1+2^{-x}\right)}=\frac{\ln 3}{\ln 2} .
\end{aligned}
$$

562. $\lim _{x \rightarrow+\infty} \ln \left(1+2^{x}\right) \ln \left(1+\frac{3}{x}\right)$.

解 $\lim _{x \rightarrow+\infty} \ln \left(1+2^{x}\right) \ln \left(1+\frac{3}{x}\right)$

$$
\begin{aligned}
& =\lim _{x \rightarrow+\infty} \frac{\ln \left(1+\frac{3}{x}\right)}{\frac{3}{x}} \cdot \frac{x \ln 2+\ln \left(2^{-x}+1\right)}{\frac{x}{3}} \\
& =3 \ln 2=\ln 8 .
\end{aligned}
$$

563. $\lim _{x \rightarrow 1}(1-x) \lg _{x} 2$.

粍 $\lim _{x \rightarrow 1}(1-x) \lg _{x} 2=\lim _{x \rightarrow 1} \frac{1-x}{\ln x} \cdot \ln 2$

$$
\left.=-\ln 2 \cdot \lim _{x \rightarrow 1} \frac{x-1}{\ln [1+(x-1)]}=-\ln 2 . \cdot\right)
$$

*）利用 529 题的结果。
564. 证明：

$$
\lim _{x \rightarrow+\infty} \frac{x^{*}}{a^{x}}=0 . \quad(a>1, n>0) .
$$

证 当 $x \geqslant 1$ 时，存在唯一的正整数 $k$ ，使

$$
k \leqslant x<k+1 \text {. }
$$

于是当 $n>0$ 时, 我们有

$$
\frac{x^{n}}{a^{x}}<\frac{(k+1)^{*}}{a^{k}}
$$

及

$$
\frac{x^{*}}{a^{x}}>\frac{k^{n}}{a^{k+1}}=\frac{k^{n}}{a^{k}} \cdot \frac{1}{a} .
$$

因为当 $x \rightarrow+\infty$ 时， $k \rightarrow+\infty$ ，所以有
$\lim _{x \rightarrow+\infty} \frac{(k+1)^{n}}{a^{k}}=\lim _{x \rightarrow+\infty} \frac{(k+1)^{n}}{a^{k+1}} \cdot a=0 \cdot a^{n}=0$
及

$$
\lim _{y \rightarrow+\infty} \frac{k^{x}}{a^{k+1}}=\lim _{x \rightarrow+\infty} \frac{k^{x}}{a^{k}} \cdot \frac{1}{a}=0 \cdot \frac{1}{a}{ }^{*)}=0
$$

于是,

$$
\lim _{x \rightarrow+\infty} \frac{x^{n}}{a^{x}}=0 .
$$

*) 利用 60 题的结果。
565. 证明：

$$
\lim _{x \rightarrow+\infty} \frac{\lg _{\mathrm{a}} x}{x^{2}}=0 \quad(a>1, \varepsilon>0)
$$

证 设 $\log _{a} x=y$, 则 $x=a^{y}$, 且当 $x \rightarrow+\infty$ 时, $y \rightarrow+$ ）．于是

$$
\lim _{x \rightarrow+\infty} \frac{\log _{a} x}{x^{e}}=\lim _{y \rightarrow+\infty} \frac{y}{\left(a^{y}\right)^{4}}=\lim _{y \rightarrow+\infty}\left(\frac{y^{\frac{1}{e}}}{a^{y}}\right)^{e}=0^{n},
$$

即

$$
\lim _{x \rightarrow+\infty} \frac{\log _{a} x}{x^{c}}=0
$$

*) 利用 564 题的结果。

## 求下列的极限：

566. 

(a) $\lim _{x \rightarrow 0} \frac{\ln \left(x^{2}+e^{2}\right)}{\ln \left(x^{4}+e^{2 x}\right)}$;
(6) $\lim _{x \rightarrow+\infty} \frac{\ln \left(x^{2}+e^{x}\right)}{\ln \left(x^{4}+e^{2 x}\right)}$.
解（a） $\lim _{x \rightarrow 0} \frac{\ln \left(x^{2}+e^{x}\right)}{\ln \left(x^{4}+e^{2 x}\right)}=\lim _{x \rightarrow 0} \frac{x+\ln \left(1+x^{2} e^{-x}\right)}{2 x+\ln \left(1+x^{4} e^{-2 x}\right)}$

$$
=\lim _{x \rightarrow 0} \frac{1+\frac{\ln \left(1+x^{2} e^{-x}\right)}{x^{2} e} \cdot x e^{x}}{2+\frac{\ln \left(1+x^{4} e^{-2 x}\right)}{x^{4} e^{2 z}} \cdot x^{3} e^{-2 x}}=\frac{1}{2} ;
$$

(6) $\lim _{x \rightarrow+\infty} \frac{\ln \left(x^{2}+e^{x}\right)}{\ln \left(x^{4}+e^{2 x}\right)}$
$=\lim _{x \rightarrow+\infty} \frac{1+\frac{\ln \left(1+x^{2} e^{-x}\right)}{x}}{2+\frac{\ln \left(1+x^{4} e^{-2 x}\right)}{x}}=\frac{1}{2}$,
其中利用了结果

$$
\lim _{x \rightarrow+\infty} x^{n} a^{-x}=0(n>0, a>1),
$$

因而

$$
x^{2} e^{-x} \rightarrow 0 \text { 及 } x^{4} e^{-2 x} \rightarrow 0 \quad(x \rightarrow+\infty) \text {. }
$$

567. $\lim _{x \rightarrow 0} \frac{\ln \left(1+x e^{x}\right)}{\ln \left(x+\sqrt{1+x^{2}}\right)}$.

䑲 $\lim _{x \rightarrow 0} \frac{\ln \left(1+x e^{x}\right)}{\ln \left(x+\sqrt{1+x^{2}}\right)}$
$=\lim _{x \rightarrow 0} \frac{\frac{\ln \left(1+x e^{x}\right)}{x e^{x}} \cdot x e^{x}}{\frac{1}{2} \ln \left(1+x^{2}\right)+\frac{\ln \left(1+\frac{x}{\sqrt{1+x^{2}}}\right)}{\frac{x}{\sqrt{1+x^{2}}}}+\frac{x}{\sqrt{1+x^{2}}}}$

$$
=\lim _{x \rightarrow 0} \frac{x e^{x}}{\frac{x}{\sqrt{1+x^{2}}}}=\lim _{x \rightarrow 0} e^{x} \sqrt{1+x^{2}}=1
$$

568. $\lim _{x \rightarrow \infty}[(x+2) \ln (x+2)-2(x+1) \ln (x+1)+x \ln x]$.

解 $\lim _{x \rightarrow \infty}[(x+2) \ln (x+2)-2(x+1) \ln (x+1)+x \ln x]$

$$
\begin{aligned}
& =\lim _{x \rightarrow \infty} \ln \frac{(x+2)^{x+2} \cdot x^{x}}{(x+1)^{2 x+2}}=\lim _{x \rightarrow \infty} \ln \frac{\left(1+\frac{2}{x}\right)^{\frac{x}{2} \cdot 2+2}}{\left(1+\frac{1}{x}\right)^{2 x+2}} \\
& =\ln \frac{e^{2}}{e^{2}}=0
\end{aligned}
$$

569. $\lim _{x \rightarrow+\infty}\left[\ln (x \ln a) \cdot \ln \left(\frac{\ln a x}{\ln \frac{x}{a}}\right)\right] \quad(a>1)$.

$$
\begin{aligned}
& \text { 解 } \lim _{x \rightarrow+\infty}\left[\ln (x \ln a) \cdot \ln \left(\frac{\ln a x}{\ln \frac{x}{a}}\right)\right] \\
& =\lim _{x \rightarrow 10} \ln \left(\frac{\ln a+\ln x}{\ln x-\ln a}\right)^{\ln x+\ln (\ln a)} \\
& =\lim _{x \rightarrow+0} \ln \left(1+\frac{2 \ln a}{\ln x-\ln a}\right)^{\frac{\ln x-\ln a}{2 \ln a} \cdot 2 \ln x \cdot \frac{\ln x+\ln (\ln a)}{\ln x-\ln a}} \\
& =\ln e^{\operatorname{lo} a^{2}}=\ln a^{2} \text {. } \\
& \text { 570. } \lim _{x \rightarrow+\infty}\left(\ln \frac{x+\sqrt{x^{2}+1}}{x+\sqrt{x^{2}-1}} \cdot \ln ^{-2} \frac{x+1}{x-1}\right) \text {. } \\
& \text { 解 } \lim _{x \rightarrow+\infty}\left(\ln \frac{x+\sqrt{x^{2}+1}}{x+\sqrt{x^{2}-1}} \cdot \ln =\frac{x+1}{x-1}\right) \\
& =\lim _{x \rightarrow+\infty} \frac{\ln \left(1+\frac{\sqrt{x^{2}}+1-\sqrt{x^{2}-1}}{x+\sqrt{x^{2}-1}}\right)}{\ln ^{2}\left(1+\frac{2}{x-1}\right)}=\lim _{x \rightarrow+\infty} \\
& {\left[\ln \left(1+\frac{2}{\left(x+\sqrt{x^{2}-1}\right)\left(\sqrt{x^{2}+1}+\sqrt{x^{2}-1}\right)}\right]^{\frac{\left(x+\sqrt{x^{2}-12}\right.}{\sqrt{2}}}\right.}
\end{aligned}
$$

$$
\begin{aligned}
& \left.\frac{\left(\sqrt{x^{2}-\frac{1}{2}}+\sqrt{x^{2}-1}\right)}{\sqrt{2}}\right) \cdot \frac{2}{\left(x+\sqrt{x^{2}-1}\right)\left(\sqrt{x^{2}+1}+\sqrt{x^{2}-1}\right.} \\
& \left.\quad=\lim _{x \rightarrow+\infty} \frac{2}{x-1}\right)^{2} \\
& \quad=\lim _{x \rightarrow+\infty} \frac{(x-1)^{2}}{2\left(1+\sqrt{x^{2}-1}\right)\left(\sqrt{x^{2}+1}+\sqrt{x^{2}-1}\right)} \\
& \quad=\frac{1}{8} .
\end{aligned}
$$

$$
\text { 571. } \begin{aligned}
\lim _{x \rightarrow 3} & \frac{\sqrt{1+x \sin x}-1}{e^{x^{2}}-1} \\
\text { 解 } & \lim _{x \rightarrow 0} \frac{\sqrt{1+x \sin x}-1}{e^{x^{2}}-1} \\
= & \lim _{x \rightarrow 0} \frac{x \sin x}{\left(e^{x^{2}}-1\right)(\sqrt{1+x \sin x}+1)} \\
= & \lim _{x \rightarrow 0} \frac{\frac{\sin x}{x}}{\frac{e^{x^{3}}-1}{x^{2}}(1+\sqrt{1+x \sin x})}=\frac{1}{2} .
\end{aligned}
$$

572. $\lim _{x \rightarrow 0} \frac{\cos \left(x e^{x}\right)-\cos \left(x e^{-x}\right)}{x^{3}}$.

解 $\lim _{x \rightarrow 0} \frac{\cos \left(x e^{x}\right)-\cos \left(x e^{-x}\right)}{x^{3}}$
$=\lim _{x \rightarrow 0} \frac{-2 \sin \frac{x\left(e^{x}+e^{-x}\right)}{2} \sin \frac{x\left(e^{x}-e^{-x}\right)}{2}}{x^{2}}$
$=-2 \lim _{x \rightarrow 0}\left[\frac{\sin \frac{x\left(e^{x}+e^{-x}\right)}{2}}{\frac{x\left(e^{x}+e^{-x}\right)}{2}} \cdot \frac{\sin \frac{x\left(e^{x}-e^{-x}\right)}{2}}{\frac{x\left(e^{x}-e^{-x}\right)}{2}} \cdot \frac{x^{2}\left(e^{4 x}-1\right)}{4 x^{3} e^{2 x}}\right]$
$=-2 \lim _{x \rightarrow 0} \frac{e^{4 x}-1}{4 x} \cdot \frac{1}{e^{2 x}}=-2$.
573. $\lim _{x \rightarrow-0}\left(2 e^{\frac{x}{x+1}}-1\right)^{\frac{x^{2}+1}{x}}$

解 $\lim _{x \rightarrow 0}\left(2 e^{\frac{x}{x+1}}-1\right)^{\frac{x^{2}+1}{x}}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 3}\left\{\left[1+2\left(e^{\left.\left.\left.\frac{x}{x+1}-1\right)\right] 2 e^{\frac{-1}{x+1}-1}\right\}^{\frac{2\left(x^{2}+17\right.}{x+1} \cdot \frac{\frac{x}{x+3}-1}{x}} \frac{x}{x+1}}\right.\right.\right. \\
& =e^{2}
\end{aligned}
$$

574. $\lim _{x \rightarrow 1}(2-x)^{x \sec \frac{x x}{2}}$.

解 $\lim _{x \rightarrow 1}(2-x)^{\sec \frac{\pi x}{2}}$
$=\lim _{x \rightarrow 1}\left[1+(-x+1)-\frac{1}{j 1-x} \cdot \frac{\frac{x(x-1)}{2}}{\sin \frac{\pi(x-1]}{2}} \cdot \frac{2}{\pi}=e^{\frac{2}{\mathrm{~F}}}\right.$.
575. $\lim _{x \rightarrow \frac{\pi}{2}} \frac{1-\sin ^{\alpha+\beta} x}{\sqrt{\left(1-\sin ^{\alpha} x\right)\left(1-\sin ^{\beta} x\right)}} \quad(\alpha>0, \beta>0)$.

解 $\lim _{x \rightarrow \frac{\pi}{2}} \frac{1-\sin ^{*+\beta} x}{\sqrt{\left(1-\sin ^{\sigma} x\left(1-\sin ^{\beta} x\right)\right.}}$
$=\lim _{x \rightarrow \frac{\pi}{2}} \frac{1-e^{(\alpha+\phi) \cdot \operatorname{lnsin} x}}{\sqrt{\left(1-e^{a \cdot \ln \sin x}\right)\left(1-e^{\beta \cdot \ln \sin x}\right)}}$
$=\lim _{x \rightarrow \frac{\pi}{2}}\left(\frac{1-e^{(\alpha+\beta) \cdot \operatorname{lng} x}}{(\alpha+\beta) \ln \sin x}\right) \cdot\left(\frac{\alpha \cdot \ln \sin x}{1-e^{\alpha \cdot \ln x: \operatorname{nin} x}}\right)^{\frac{1}{2}}$
$\cdot\left(\frac{\beta \cdot \ln \sin x}{1-e^{\beta \cdot \sin x}}\right)^{\frac{1}{2}} \cdot\left(\frac{(\alpha+\beta) \cdot \ln \sin x}{\sqrt{\alpha \beta} \cdot \ln \sin x}\right)=\frac{\alpha+\beta}{\sqrt{\alpha \beta}}$.

注 其中， $x$ 在 $\frac{\pi}{2}$ 的附近变化，故 $\sin x>0$ 。 576. $\lim _{x \rightarrow 0} \frac{\operatorname{sh}^{2} x}{\ln (\operatorname{ch} 3 x)}$ (参见 340 题).

解 $\lim _{x \rightarrow 0} \frac{\operatorname{sh}^{2} x}{\ln \left(\operatorname{ch}^{2} x\right)}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 0} \frac{\frac{\left(e^{2 x}-1\right)^{2}}{4 e^{2 x}}}{\ln \left[1+\frac{1}{2}\left(e^{\frac{3}{2} x}-e^{-\frac{3}{2} x}\right)^{2}\right]} \\
& =\lim _{x \rightarrow 0}\left(\frac{e^{2 x}-1}{2 x}\right)^{2} \cdot \frac{\frac{1}{2}\left(e^{\frac{3}{2} x}-e^{-\frac{3}{2} x}\right)^{2} \cdot e^{x}}{\ln \left[1+\frac{1}{2}\left(e^{\frac{3}{2} x}-e^{-\frac{3}{2} x}\right)^{2}\right]} \\
& \cdot\left(\frac{3 x}{e^{3 x}-1}\right)^{2} \cdot \frac{2}{9}=\frac{2}{9}
\end{aligned}
$$

577. $\lim _{x \rightarrow+\infty} \frac{\operatorname{sh} \sqrt{x^{2}+x}-\operatorname{sh} \sqrt{x^{2}-x}}{\operatorname{ch} x}$.

解 $\operatorname{sh} \sqrt{x^{2}+x}-\operatorname{sh} \sqrt{x^{2}-x}$

$$
=2 \operatorname{sh} \frac{\sqrt{x^{2}+x}-\sqrt{x^{2}-x}}{2} \cdot \operatorname{ch} \frac{\sqrt{x^{2}+x}+\sqrt{x^{2}-x}}{2}
$$

因为

$$
\begin{aligned}
& \sqrt{x^{2}+x}-\sqrt{x^{2}-x}=\frac{2 x}{\sqrt{x^{2}+x}+\sqrt{x^{2}-x}} \\
& =\frac{2}{\sqrt{1+\frac{1}{x}}+\sqrt{1-\frac{1}{x}}} \longrightarrow \\
& \frac{(x \rightarrow+\infty)}{\operatorname{ch} \frac{1}{2}\left(\sqrt{x^{2}+x}+\sqrt{x^{2}-x}\right)} \\
& \frac{\operatorname{ch} x}{}
\end{aligned}
$$

$$
=\frac{e^{\frac{\sqrt{x^{2}+x}+\sqrt{x^{2}-x}}{2}}+e^{-\frac{\sqrt{x^{2}+x}+\sqrt{x^{2}-x}}{2}}}{e^{x}+e^{-x}} \rightarrow 1,
$$

所以
$\lim _{x \rightarrow 0} \frac{\operatorname{sh} \sqrt{x^{2}+x}-\operatorname{sh} \sqrt{x^{2}-x}}{\operatorname{ch} x}=2 \operatorname{sh} \frac{1}{2}$.
578. $\lim _{x \rightarrow+\infty}(x-\operatorname{lnch} x)$

解 $\lim _{x \rightarrow+\infty}(x-\operatorname{lnch} x)$
$=\lim _{x \rightarrow+\infty}\left(x-\ln \frac{e^{2 x}+1}{2 e^{x}}\right)=\lim _{x \rightarrow+\infty}\left[2 x+\ln 2-\ln \left(1+e^{2 x}\right)\right]$
$=\lim _{x \rightarrow+\infty}\left[\ln 2-\ln \left(e^{-2 x}+1\right)\right]=\ln 2$.
579. $\lim _{x \rightarrow 0} \frac{e^{\sin 2 x}-e^{\sin x}}{\operatorname{th} x}$.

解 $\lim _{x \rightarrow 0} \frac{e^{\sin 2 x}-e^{\sin x}}{\operatorname{th} x}=\lim _{x \rightarrow 0} \frac{\left(e^{\min 2 x}-e^{\sin x}\right)\left(e^{2 x}+1\right)}{e^{2 x}-1}$
$=\lim _{x \rightarrow 0} \frac{\left(\frac{e^{\sin 2 x}-1}{\sin 2 x} \cdot \frac{\sin 2 x}{2 x}-\frac{e^{\sin } x-1}{\sin x} \cdot \frac{\sin x}{x} \cdot \frac{1}{2}\right)\left(e^{2 x}+1\right)}{\frac{e^{2 x}-1}{2 x}}$
$=\frac{\left(1-\frac{1}{2}\right)^{2}}{1}=1$.
580. $\lim _{n \rightarrow \infty}\left(\frac{\operatorname{ch} \frac{\pi}{n}}{\cos \frac{\pi}{n}}\right)^{n^{2}}$.

解 $\left(\frac{\operatorname{ch} \frac{\pi}{n}}{\cos \frac{\pi}{n}}\right)^{n^{2}}=\left(\frac{e^{\frac{\pi}{n}}+e^{-\frac{x}{n}}}{2 \cos \frac{\pi}{\dot{n}}}\right]^{4^{2}}$

$$
-\left(1+\frac{1}{2 \cos \frac{\pi}{n}}\right)^{\frac{\pi}{e^{\frac{\pi}{n}}+e^{-\frac{\pi}{n}}-2 \cos \frac{\pi}{n}}} \cdot \frac{x^{2}\left(\cdot \frac{\pi}{n}+e^{\left.-\frac{\pi}{n}-2 \cos \frac{\pi}{n}\right)}\right.}{2 \cos \frac{\pi}{n}}
$$

园为

$$
\begin{aligned}
& n^{2}\left(e^{\frac{\pi}{n}}+e^{-\frac{\pi}{n}}-2 \cos \frac{\pi}{n}\right) \\
& =n^{2}\left[\left(e^{\frac{\pi}{2 n}}-e^{-\frac{\pi}{2 n}}\right)^{2}+2\left(1-\cos \frac{\pi}{n}\right)\right] \\
& =n^{2}\left[\left(e^{\frac{\pi}{2 n}}-e^{-\frac{\pi}{2 n}}\right)^{2}+4 \sin ^{2} \frac{\pi}{2 n}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\left(\frac{e^{\frac{\pi}{2 n}}-1}{\frac{\pi}{2 n}} \cdot \frac{\pi}{2}-\frac{e^{-\frac{\pi}{2 n}}-1}{-\frac{\pi}{2 n}} \cdot \frac{\pi}{2}\right)^{2}+\pi^{2} \cdot\left(\frac{\sin \frac{\pi}{2 n}}{\frac{\pi}{2 n}}\right)^{2} \\
& \longrightarrow 2 \pi^{2} \cdot(n \rightarrow \infty),
\end{aligned}
$$

所以

$$
\lim _{x \rightarrow \infty}\left(\frac{\operatorname{ch} \frac{\pi}{n}}{\cos \frac{\pi}{n}}\right)^{n^{2}}=e^{x^{2}} .
$$

581. $\operatorname{limarcsin}_{x \rightarrow \infty} \frac{1-x}{1+x}$.

解 $\operatorname{limarcsin}_{x \rightarrow \infty} \frac{1-x}{1+x}=\arcsin (-1)=-\frac{\pi}{2}$.
582. $\lim _{x \rightarrow+\infty} \arccos \left(\sqrt{x^{2}+x}-x\right)$.

解 $\lim _{x \rightarrow+\infty} \arccos \left(\sqrt{x^{3}+x}-x\right)$
$=\lim _{x \rightarrow+\infty} \arccos \frac{x}{\sqrt{x^{2}+x}+x}=\arccos \frac{1}{2} \doteq \frac{\pi}{3}$.
583. $\operatorname{limarctg}_{x \rightarrow 2} \frac{x-4}{(x-2)^{2}}$.

解 $\operatorname{limartg}_{x \rightarrow 2} \frac{x-4}{(x-2)^{2}}=-\frac{\pi}{2}$ 。
584. $\lim _{x \rightarrow-\infty} \operatorname{arcctg} \frac{x}{\sqrt{1+x^{2}}}$.

解 $\lim _{x \rightarrow \infty} \operatorname{arcctg} \frac{x}{\sqrt{1+x^{2}}}=\operatorname{arcctg}(-1)=\frac{3}{4} \pi$.
585. $\lim _{h \rightarrow 0} \frac{\operatorname{arctg}(x+h)-\operatorname{arctg} x}{h}$.

解 $\lim _{h \rightarrow 0} \frac{\operatorname{arctg}(x+h)}{h}=\operatorname{arctg} x$
$=\lim _{h \rightarrow 0}\left[\frac{\operatorname{arctg} \frac{h}{1+x(x+h)}}{\frac{h}{1+x(x+h)}} \cdot \frac{1}{1+x(x+h)}\right]$
$=\frac{1}{1+x^{2}}$.
*）其中利用了结果： $\lim _{x \rightarrow 0} \frac{\operatorname{arctg} x}{x}=1$.
$\ln \frac{1+x}{1-x}$
586. $\lim _{x \rightarrow 0} \frac{\operatorname{arctg}(1+x)-\operatorname{arctg}(1-x)}{}$.

解 $\lim _{x \rightarrow 0} \frac{\ln \frac{1+x}{1-x}}{\operatorname{arctg}(1+x)-\operatorname{arctg}(1-x)}$
$=\lim _{x \rightarrow 0}\left[\frac{\ln \left(1+\frac{2 x}{1-x}\right)}{\frac{2 x}{1-x}} \cdot \frac{\frac{2 x}{2-x^{2}}}{\operatorname{arctg} \frac{2 x}{2-x^{2}}} \cdot \frac{2-x^{2}}{1-x}\right]=2$.
587. $\lim _{n \rightarrow-\mathrm{m}}\left[\operatorname{narctg} \frac{1}{n\left(x^{2}+1\right)+x} \cdot \operatorname{tg}^{n}\left(\frac{\pi}{4}+\frac{x}{2 n}\right)\right]$.

解 $\lim _{n \rightarrow \infty}\left[n \operatorname{arctg} \frac{1}{n\left(x^{2}+1\right)+x} \cdot \operatorname{tg}\left(\frac{\pi}{4}+\frac{x}{2 n}\right)\right]$
$=\lim _{n \rightarrow \infty}\left[\frac{\operatorname{arctg} \frac{1}{n\left(x^{2}+1\right)+x}}{\frac{1}{n\left(x^{2}+1\right)+x}} \cdot \frac{n}{n\left(x^{2}+1\right)+x}\right.$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-320.jpg?height=363&width=1106&top_left_y=775&top_left_x=355)
588. $\lim _{x \rightarrow \infty} x\left(\frac{\pi}{4}-\operatorname{arctg} \frac{x}{x+1}\right)$.

解 $\lim _{x \rightarrow \infty} x\left(\frac{\pi}{4}-\operatorname{arctg} \frac{x}{x+1}\right)=\lim _{x \rightarrow \infty} x \operatorname{arctg} \frac{1}{2 x+1}$
$=\lim _{x \rightarrow \infty} \frac{\operatorname{arctg} \frac{1}{2 x+1}}{\frac{1}{2 x+1}} \cdot \frac{x}{2 x+1}=\frac{1}{2}$.
589. $\lim _{x \rightarrow+\infty} x\left(\frac{\pi}{2}-\arcsin \frac{x}{\sqrt{x^{2}+1}}\right)$.

得 $\lim _{x \rightarrow+\infty} x\left(\frac{\pi}{2}-\arcsin \frac{x}{\sqrt{x^{2}+1}}\right)$

$$
\begin{aligned}
& =\lim _{x \rightarrow+\infty} x \arcsin \frac{1}{\sqrt{x^{2}+1}} \\
& =\lim _{x \rightarrow+\infty} \frac{\arcsin \frac{1}{\sqrt{x^{2}+1}}}{\frac{1}{\sqrt{x^{2}+1}}} \cdot \frac{x}{\sqrt{x^{2}+1}}=1^{*} .
\end{aligned}
$$

*）其中利用了结果： $\lim _{x \rightarrow 0} \frac{\arcsin x}{x}=1$.
590. $\lim _{n \rightarrow \infty}\left[1+\frac{(-1)^{n}}{n}\right]^{\operatorname{cosen}\left(n \sqrt{1+\pi^{2}}\right)}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-321.jpg?height=169&width=821&top_left_y=538&top_left_x=329)
$=\lim _{n \rightarrow \infty}\left[1+\frac{(-1)^{n}}{n}\right]^{\frac{n}{(-1)^{*}}} \cdot \frac{(-i)^{n}}{\sin \left(x \sqrt{1+n^{2}}\right)}$
$=\lim _{m \rightarrow \infty}\left[1+\frac{(-1)^{n}}{n}\right]^{\frac{n}{(-1)^{n}}} \cdot \frac{-1}{\operatorname{cin}\left(\pi n-x \sqrt{1+n^{2}}\right)}$
$=\lim _{n \rightarrow \infty}\left[1+\frac{(-1)^{n}}{n}\right]^{\frac{n}{(-1)^{n}} \cdot \frac{n x-n \sqrt{1+n^{2}}}{\sin \left(3-x-n \sqrt{1+n^{2}}\right)}}$

- $\frac{1}{n\left(\pi \sqrt{1+n^{2}}-n \pi\right)}$
$=e \lim _{-\rightarrow \infty} \frac{\sqrt{2^{2}+1+n}}{\left(x^{2}+1+a^{2}\right)}$
$=e^{\frac{2}{\pi}} \quad\left(n \pi-\pi \sqrt{1+n^{2}} \rightarrow 0\right)$.

591. $\lim _{x \rightarrow 0} \frac{1}{x^{100}} e^{-\frac{1}{x^{2}}}$.

解 设 $y=\frac{1}{x}$ ，则
*)利用 564 题的结果。
592. $\lim _{x \rightarrow+\infty} x \ln x$.

解 $y=\frac{1}{x}$ ，则

$$
\lim _{x \rightarrow+\infty} x \ln x=\lim _{y \rightarrow+\infty} \frac{-\ln y}{y}=0^{*)}
$$

*)利用 565 题的结果。
593. (a) $\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}+x}-x\right)$; (6) $\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}+x}-x\right)$.

解 (a) $\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}+x}-x\right)=+\infty$ ；
(6) $\lim _{x \rightarrow+\infty}\left(\sqrt{x^{2}+x}-x\right)=\lim _{x \rightarrow+\infty} \frac{x}{\sqrt{x^{2}+x}+x}=\frac{1}{2}$.
594. (a) $\lim _{x \rightarrow-\infty}\left(\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right)$;
(6) $\left.\lim _{x \rightarrow+\infty} \sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right)$.

解 (a) $\lim _{x \rightarrow \infty}\left(\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right)$
$=\lim _{x \rightarrow-\infty} \frac{2 x}{\sqrt{1+x+x^{2}}+\sqrt{1-x+x^{2}}}$
$=\lim _{x \rightarrow-\infty} \frac{-2}{\sqrt{\frac{1}{x^{2}}+\frac{1}{x}+1}+\sqrt{\frac{1}{x^{2}}-\frac{1}{x}+1}}{ }^{\prime}=-1$
*）当 $x \rightarrow-\infty$ 时， $x=-\sqrt{x^{2}}$.
(5) $\lim _{x \rightarrow+\infty}\left(\sqrt{1+x+x^{2}}-\sqrt{1-x+x^{2}}\right)$
$=\lim _{x \rightarrow+\infty} \frac{2}{\sqrt{\frac{1}{x^{2}}+\frac{1}{x}+1}+\sqrt{\frac{1}{x^{2}}-\frac{1}{x}+1}}{ }^{*}=1$.
*）当 $x \rightarrow+\infty$ 时， $x=\sqrt{x^{2}}$.
595. (a) $\lim _{x \rightarrow 1-0} \operatorname{arctg} \frac{1}{1-x}$; (6) $\lim _{\rightarrow \rightarrow 1+0} \operatorname{arctg} \frac{1}{1-x}$.

解 (a) $\lim _{x \rightarrow 1-0} \operatorname{arctg} \frac{1}{1-x}=\frac{\pi}{2}$ ；
(6) $\lim _{x \rightarrow 1+0} \operatorname{arctg} \frac{1}{1-x}=-\frac{\pi}{2}$.
596. (3) $\lim _{x \rightarrow-6} \frac{1}{1+e^{\frac{1}{x}}} ;$ (6) $\lim _{x \rightarrow+0} \frac{1}{1+e^{\frac{1}{x}}}$.

䊖 （a） $\lim _{x \rightarrow-0} \frac{1}{1+e^{\frac{1}{x}}}=1$ ；

$$
\text { (6) } \lim _{x \rightarrow+0} \frac{1}{1+e^{\frac{1}{x}}}=0 \text {. }
$$

597. (a) $\lim _{x \rightarrow-\infty} \frac{\ln \left(1+e^{x}\right)}{x}$; (6) $\lim _{x \rightarrow+\infty} \frac{\ln \left(1+e^{x}\right)}{x}$.

解 (a) $\lim _{x \rightarrow-\infty} \frac{\ln \left(1+e^{x}\right)}{x}=\lim _{x \rightarrow-\infty}\left[\frac{\ln \left(1+e^{x}\right)}{e^{x}} \cdot \frac{e^{x}}{x}\right]=0$ ；
(6) $\lim _{x \rightarrow+\infty} \frac{\ln \left(1+e^{x}\right)}{x}=\lim _{x \rightarrow+\infty}\left[1+\frac{\ln \left(e^{\cdots x}+1\right)}{x}\right]=1$.
598. 证明：
(a) 当 $x \rightarrow-\infty$ 时, $\frac{2 x}{1+x} \rightarrow 2+0$;
（6）当 $x \rightarrow+\infty$ 时， $\frac{2 x}{1+x} \rightarrow 2-0$ 。
证（a）当 $x<0$ 时，及当 $|x|$ 充分大以后，

$$
\frac{2 x}{1+x}>2
$$

于是

当 $x \rightarrow-\infty$ 时， $\frac{2 x}{1+x} \rightarrow 2+0$ ；
（6）当 $x>0$ 时，

$$
0<\frac{2 x}{1+x}<2
$$

于是，
当 $x \rightarrow+\infty$ 时, $\frac{2 x}{1+x} \rightarrow 2-0$.
599. 证明：
（a）当 $x \rightarrow-0$ 时， $2^{x} \rightarrow 1-0$ ；
（6）当 $x \rightarrow+0$ 时， $2^{x} \rightarrow 1+0$ 。

证（a）当 $x<0$ 时，

$$
0<2^{x}<1 .
$$

于是，
当 $x \rightarrow-0$ 时， $2^{x} \rightarrow 1-0$ ；
（6）当 $x>0$ 时，

$$
2^{x}>1
$$

于是，

$$
\text { 当 } x \rightarrow+0 \text { 时, } 2^{x} \rightarrow 1+0 \text {. }
$$

600. 设 $f(x)=x+\left[x^{2}\right]$, 求 $f(1), f(1-0), f(1+0)$.

解 $f(1)=2$ ；

$$
\begin{aligned}
& f(1-0)=\lim _{x \rightarrow+\infty}\left(x+\left[x^{2}\right]\right)=1+0=1 ; \\
& f(1+0)=\lim _{x \rightarrow 1+0}\left(x+\left[x^{2}\right]\right)=1+1=2 .
\end{aligned}
$$

601. 设 $f(x)=\operatorname{sgn}(\sin \pi x)$, 求 $f(n), f(n-0), f(n+\theta)(n=$ $0, \pm 1, \cdots)$.
楻 $f(n)=0$ ；

$$
\begin{aligned}
& f(n-0)=\lim _{x \rightarrow-0} \operatorname{sgn}(\sin \pi x)=(-1)^{n-1} ; \\
& f(n+0)=\lim _{x \rightarrow+n} \operatorname{sgn}(\sin \pi x)=(-1)^{n} .
\end{aligned}
$$

求：
602. $\lim _{x \rightarrow 0} x \sqrt{\cos \frac{1}{x}}$.

果 因为 $\sqrt{\cos \frac{1}{x}}$ 为有界函数，所以，

$$
\lim _{x \rightarrow 0} x \sqrt{\cos \frac{1}{x}}=0 .
$$

603. $\lim _{x \rightarrow 0} x\left[\frac{1}{x}\right]$.

318

解 因为

$$
\frac{1}{x}-1<\left[\frac{1}{x}\right] \leqslant \frac{1}{x} \quad(x \neq 0)
$$

当 $x>0$ 时

$$
1-x<x\left[\frac{1}{x}\right] \leqslant 1
$$

当 $x<0$ 时,

$$
1-x>x\left[\frac{1}{x}\right] \geqslant 1,
$$

于是,

$$
\lim _{x \rightarrow 0}\left[\frac{1}{x}\right]=1
$$

604. $\lim _{n \rightarrow \infty} \sin \left(\pi \sqrt{n^{2}+1}\right)$.

解 $\lim _{n \rightarrow \infty} \sin \left(\pi \sqrt{\pi^{2}+1}\right)$
$=\lim _{\pi \rightarrow \infty}(-1) n \sin \left(\pi \sqrt{n^{2}+1}-n \pi\right)$
$=\lim _{\pi \rightarrow \infty}(-1)^{n} \sin \frac{\pi}{\pi \sqrt{n^{2}+1}+n \pi}=0$.
605. limsin ${ }^{2}\left(\pi \sqrt{n^{2}+n}\right)$.
$4+\infty$
解 $\operatorname{limsin}^{2}\left(\pi \sqrt{n^{2}+n}\right)$
$=\lim _{n \rightarrow \infty} \frac{1}{2}\left[1-\cos \left(2 \pi \sqrt{n^{2}+n}\right)\right]$
$=\frac{1}{2} \lim _{n \rightarrow \infty}\left\{1-\cos \left[2 \pi\left(\sqrt{n^{2}+n}-n\right)\right]\right\}=1$.
606. $\lim _{n \rightarrow \infty} \operatorname{sinsin} \cdots \sin x$.

解 先设 $0 \leqslant x \leqslant \pi$ ，这时， $0 \leqslant \sin x \leqslant x$ ， $0 \leqslant \sin (\sin x) \leqslant \sin x$,
依次类推. 用数学归纳法，即可证得

$$
0 \leqslant \overbrace{\operatorname{sinsin} \cdots \sin }^{n t} x \leqslant \overbrace{\sin \sin \cdots \sin x}^{n},
$$

这说明 $\sin \sin \cdots \sin x$ 随着 $n$ 的增大而单调减少，于是由其有界性知被限

$$
\operatorname{limsinsin}_{x \rightarrow \sin }^{x}=\mu
$$

存在有限，且 $0 \leqslant \mu \leqslant 1$ ，因此

$$
\lim _{n \rightarrow \infty} \overbrace{\sin \sin \cdots \sin }^{\pi+} x=\sin (\lim _{n \rightarrow \infty} \overbrace{\sin \sin \cdots \sin }^{* \cdot 2+})
$$

即

$$
\sin \alpha=\mu
$$

故

$$
\mu=0 .
$$

同法可证，当 $\pi<x \leqslant 2 \pi$ 时，

$$
\overbrace{\text { limsinsin } \cdots \sin }^{x} x=0
$$

再利用 $\sin x$ 的周期性（周期为 $2 \pi$ ），得知对任 $-× x$ 值，施有 at
limsinsin $\cdots \sin x=0$.
607. 设 $\lim _{x \rightarrow 0} \varphi(x)=A$ 及 $\lim _{x \rightarrow 4} \psi(x)=B$ ，由此是否可推出 $\lim _{x \rightarrow 2} \psi(\varphi(x))=B ?$

研究这个例子：当 $x=\frac{p}{q}$ （其中 $p$ 和 $q$ 是互质的整数）时， $\varphi(x)=\frac{1}{q}$ ；当 $x$ 为无理数时， $\varphi(x)=0$ ；当 $x \neq 0$时， $\psi(x)=1$ ；当 $x=0$ 时， $\psi(x)=0$ ；并目 $x \rightarrow 0$ 。
解 不一定，例如对于函数
$\varphi(x)=\left\{\begin{array}{l}\frac{1}{q}, \text { 当 } x=\frac{p}{q} \text { （其中 } p \text { 和 } q \text { 互质）时； } \\ 0, \text { 当 } x \text { 为无理数时。 }\end{array}\right.$
及

$$
\psi(x)=\left\{\begin{array}{l}
1, \text { 当 } x \neq 0 \text { 时； } \\
0, \text { 当 } x=0 \text { 时. }
\end{array}\right.
$$

有

$$
\lim _{x \rightarrow 0} \varphi(x)=0(=A)
$$

及

$$
\lim _{x \rightarrow \infty} \psi(x)=1,
$$

但是，极限

$$
\lim _{x \rightarrow \rho} \psi(\varphi(x))
$$

却不存在。事实上，当 $x$ 以一串无理数列 $x_{n}$ 趋近于零时，有 $\varphi\left(x_{n}\right)=0$ ，因此 $\phi\left(\varphi\left(x_{n}\right)\right)=0(n=1,2, \cdots)$ ；而当 $x$ 以一串有理数列 $x^{\prime}{ }_{n}$ 趋近于零时， $\varphi\left(x_{n}^{\prime}\right) \neq 0$ ，因此， $\phi(\varphi$ $\left(x_{n}^{\prime}\right)$ ) $1(n=1,2, \cdots)$. 由此可知，当 $x \rightarrow 0$ 时，极限

$$
\lim _{x \rightarrow i} \psi(\varphi(x))
$$

不存在.
608. 证明哥西定理：若函数 $f(x)$ 定义于区间 $(a,+\infty)$ 上，且

$$
|f(x+1)-f(x)-A|<\frac{\varepsilon}{3}
$$

现设 $x>X_{0}+1$. 干是，恰有一个正整数 $n$ （依赖于 $x$ ），满足 $n \leqslant x-X_{0}<n+1$. 令 $\tau=x-X_{0}-n$ ，则 $0 \leqslant \tau<1, x=$ $X_{0}+t+n$. 我们有

$$
\begin{aligned}
\frac{f(x)}{x} & -A=\frac{n}{x}\left[\frac{f(x)-f\left(X_{0}+\tau\right)}{n}-A\right]+\frac{f\left(X_{0}+\tau\right)}{x} \\
& -\frac{\left(X_{0}+\tau\right) A}{x} .
\end{aligned}
$$

## 显然

$$
\begin{aligned}
& \left|\frac{n}{x}\left[\frac{f(x)-f\left(X_{0}+\tau\right)}{n}-A\right]\right| \\
& \leqslant\left|\frac{f\left(X_{0}+\tau+n\right)-f\left(X_{0}+\tau\right)}{n}-A\right| \\
& =\frac{1}{n}\left|\sum_{n=1}^{n}\left[f\left(X_{0}+\tau+k\right)-f\left(X_{0}+\tau+k-1\right)-A\right]\right| \\
& \leqslant \frac{1}{n} \sum_{n=1}^{n}\left|f\left(X_{0}+\tau+k\right)-f\left(X_{0}+\tau+k-1\right)-A\right| \\
& <\frac{1}{n} \cdot \frac{n \varepsilon}{3}=\frac{\varepsilon}{3} .
\end{aligned}
$$

由据定， $f(x)$ 在 $X_{0} \leqslant x<X_{0}+1$ 上有界，故存在正数 $X_{1}$ ，使当 $x>X_{1}$ 时，恒有

$$
\left|\frac{f\left(X_{0}+\tau\right)}{x}\right|<\frac{\epsilon}{3} \quad(0 \leqslant \tau<1)
$$

另外，显然存在正数 $X_{2}$ ，使当 $x>X_{2}$ 时，恒有

$$
\left|\frac{\left(X_{0}+1\right) A}{x}\right|<\frac{\varepsilon}{3} .
$$

令 $X=\max \left\{X_{0}+1, X_{1}, X_{2}\right\}$ 。于是，当 $x>X$ 时，必有

$$
\left|\frac{f(x)}{x}-A\right|<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon .
$$

由此可知

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=A
$$

敌（a）获证.
（5）由假定， $f(x) \geqslant c>0$ 。记 $\lim _{x \rightarrow+\infty} \frac{f(x+1)}{f(x)}=A^{\prime}$ 。显然 $A^{\prime}$ $\geqslant 0$. 下证 $A^{\prime}>0$ 。事实上, 若 $A^{\prime}=0$ ，则存在正数 $X_{0}$ ，使当 $x \geqslant X_{0}$ 时，必 $0<\frac{f(x+1)}{f(x)}<\frac{1}{2}$.于是

$$
\begin{aligned}
& 0<\frac{f\left(X_{0}+n\right)}{f\left(X_{0}\right)}=\frac{f\left(X_{0}+n\right)}{f\left(X_{0}+n-1\right)} \cdot \frac{f\left(X_{0}+n-1\right)}{f\left(X_{0}+n-2\right)} \cdots \\
& \cdot \frac{f\left(X_{0}+1\right)}{f\left(X_{0}\right)}<\left(\frac{1}{2}\right)^{n} .
\end{aligned}
$$

由此可知 $\lim _{x \rightarrow \infty} f\left(X_{\mathrm{c}}+n\right)=0$, 此显然与 $f(x) \geqslant c>0$ 矛盾,因此，有 $A^{\prime}>0$ 。

由于 $f(x) \geqslant c>0$ 且 $f(x)$ 在每个有穷区间 $(a, b)$ 内有界，故函数 $\ln f(x)$ 在毎个有穷区间 $(a, b)$ 内也有界，并且

$$
\lim _{x \rightarrow+\infty}[\ln f(x+1)-\ln f(x)]=\lim _{x \rightarrow+\infty} \ln \frac{f(x+1)}{f(x)}=
$$

$\ln A^{\prime}$.

于是，将（a）的结果用于函数 $\ln f(x)$ ，即知

$$
\lim _{x \rightarrow+\infty} \frac{\ln f(x)}{x}=\ln A^{\prime}
$$

故有

$$
\begin{aligned}
\lim _{x \rightarrow+\infty}[f(x)]^{\frac{1}{x}}=\lim _{x \rightarrow+\infty}\left[e^{\log (x)}\right]^{\frac{1}{x}}=\lim _{x \rightarrow+\infty} e^{\frac{\ln f(x)}{x}} \\
=e^{\ln A^{\prime}}=A^{\prime}
\end{aligned}
$$

证毕。
609. 证明若：（1）函数 $f(x)$ 定义于域 $x>a$ 内；（2）在每一个有

限的域 $a<x<b$ 内是有界的；（3） $\lim _{x \rightarrow+\infty}[f(x+1)-f(x)]$ $=+\infty$ (或一 $-\infty$ )，" 则

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=+\infty(\text { 或 }-\infty) .
$$

证 只要证明 $\lim _{x \rightarrow+\infty}[f(x+1)-f(x)]=+\infty$ 的情形，这时要证 $\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=+\infty$ （对于一 $-\infty$ 的情形，只要考虑函。数一 $f(x)$ 即可且结为 $+\infty$ 的情形). 任给 $G>0$ 。必存在正数 $X_{0}>a$ ，使当 $x \geqslant X_{0}$ 时，恒有

$$
f(x+1)-f(x)>4 G .
$$

现设 $x>2\left(X_{0}+1\right)$. 仿 608 题 (a)之正，恰有一个正整数 $n$ （依赖于 $x$ ），满足 $n \leqslant x-X_{0}<n+1$ 。令 $\tau=x-X_{0}-n$ ，则 $0 \leqslant r<1, x=X_{0}+r+n$ 。由于 $n+1>x-X_{0}>X_{0}+2$, 故 $n$ $>X_{0}+1>X_{0}+\tau$. 从而 $2 n>x$, 即

$$
\frac{n}{x}>\frac{1}{2} .
$$

又，我们有

$$
\frac{f(x)}{x}=\frac{n}{x} \cdot \frac{f(x)-f\left(X_{0}+\tau\right)}{n}+\frac{f\left(X_{0}+\tau\right)}{x}
$$

显然

$$
\begin{aligned}
& \frac{f(x)-f\left(X_{0}+\tau\right)}{n} \\
& =\frac{1}{n} \sum_{k=1}^{n}\left[f\left(X_{0}+\tau+k\right)-f\left(X_{0}+\tau+k-1\right)\right] \\
& >\frac{1}{n} \cdot 4 n G=4 G
\end{aligned}
$$

故

$$
\frac{n}{x} \cdot \frac{f(x)-f\left(X_{0}+\tau\right)}{n}>2 G
$$

由假定， $f(x)$ 在 $X_{0} \leqslant x<X_{0}+1$ 上有界，故存在正数 $X_{1}$ ，使当 $x>X_{1}$ 时,恒有

$$
\left.\frac{f\left(X_{3}+\tau\right)}{x} \right\rvert\,<G .
$$

令 $X=\max \left\{2\left(X_{0}+1\right), X_{1}\right\}$, 则当 $x>X$ 时, 恒有

$$
\frac{f(x)}{x}>G .
$$

由此可知

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=+\infty
$$

证毕。
*) 原题条件 (3) 误写为 $\lim _{x \rightarrow+\infty}[f(x+1)-f(x)]=\infty$ ，结论误写为 $\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=\infty$ 。例如，按下式定义 $[0,+\infty$ )上的函数 $f(x)$ ；

$$
f(x)=\left\{\begin{array}{l}
2 n, \text { 当 } 2 n \leqslant x<2 n+1 \text { 时; } \\
0, \text { 当 } 2 n+1 \leqslant x<2 n+2 \text { 时. }
\end{array}(=0,1,2, \cdots) .\right.
$$

则显然 $f(x)$ 满足原题的条件（1）和（2）（这时 $a=0$ ），并且 $\lim _{x \rightarrow+\infty}[f(x+1)-f(x)]=\infty$ ；但显然 $\lim \frac{f(x)}{x} \neq \infty$ （实际 $\lim _{x \rightarrow+\infty} \frac{f(x)}{x}$ 不存在, $\left.\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=0, \prod_{x \rightarrow+\infty} \frac{f(x)}{x}=1\right)$.
610. 证明, 若: (1) 函数 $f(x)$ 定义于域 $x>a$ 内；（2）在每一个有限的域 $a<x<b$ 内是有界的；(3)存在着有限的或无穷的（带确定符号的无穷，即 $+\infty$ 和 $-\infty$ ）*极限

$$
\lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{x^{2}}=l,
$$

则

$$
\lim _{x \rightarrow \infty} \frac{f(x)}{x^{n+1}}=\frac{l}{n+1}
$$

证 先证一条一般性的定理（ Stolz 定理在函数情形的推广）：著（1）函数 $f(x)$ 与 $g(x)$ 都定义予域 $x>a$ 内（2） $f$ （ $x$ ）与 $g(x)$ 在每一个有限域 $a<x<b$ 内有界，井且 $g(x)$当 $x<a$ 时满足 $g(x+1)>g(x)$ 且 $\lim _{x \rightarrow+\infty} g(x)=+\infty ;(3)$存在极限

$$
\lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{g(x+1)-g(x)}=l
$$

（ $l$ 为有限数或为 $+\infty$ 或为一 $-\infty$ ；
则必

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{g(x)}=l .
$$

证如下：
先设 $l$ 为有限数. 任给 $\epsilon>0$. 存在正数 $X_{0}>a$, 使当 $x$ $\geqslant X_{0}$ 时，恒有

$$
\left|\frac{f(x+1)-f(x)}{g(x+1)-g(x)}-l\right|<\frac{\varepsilon}{2} .
$$

现设 $x>X_{0}+1$. 于是，恰有一个正整数 $n$ （依赖于 $x$ ），使 $n \leqslant x-X_{0} \leqslant n+1$ 。令 $\tau=x-X_{0}-n$, 则 $0 \leqslant x<1, x=X_{0}+$ $\tau+n$. 我们有

$$
\begin{aligned}
& \frac{f(x)-f\left(X_{0}+\tau\right)}{g(x)-g\left(X_{0}+\tau\right)}-l \\
& =\sum_{k=1}^{n} \frac{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}{g(x)-g\left(X_{0}+\tau\right)} \\
& \cdot\left[\frac{f\left(X_{0}+\tau+k\right)-f\left(X_{0}+\tau+k-1\right)}{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}-l\right]
\end{aligned}
$$

而 $\left|\frac{f\left(X_{0}+\tau+k\right)-f\left(X_{0}^{\prime}+\tau+k-1\right)}{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}-l\right|<\frac{\varepsilon}{2}$

$$
(k=1,2, \cdots, n),
$$

又由于

$$
\begin{aligned}
g(x) & =g\left(X_{0}+\tau+n\right)>g\left(X_{0}+\tau+n-1\right) \\
& >g\left(X_{0}+\tau+n-2\right)>\cdots>g\left(X_{0}+\tau\right),
\end{aligned}
$$

从而

$$
\begin{aligned}
& \frac{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+r+k-1\right)}{g(x)-g\left(X_{0}+\tau\right)}>0 \\
& \quad(k=1,2, \cdots, n) ;
\end{aligned}
$$

由此可知

$$
\begin{aligned}
& \left|\frac{f(x)-f\left(X_{0}+\tau\right)}{g(x)-g\left(X_{0}+\tau\right)}-l\right| \\
& <\frac{\varepsilon}{2} \sum_{i=1}^{n} \frac{g\left(X_{0}+t+k\right)-g\left(X_{0}+\tau+k-1\right)}{g(x)-g\left(X_{0}+\tau\right)}=\frac{\varepsilon}{2} .
\end{aligned}
$$

容易直接验证等式

$$
\begin{gathered}
\frac{f(x)}{g(x)}-l=\left[1-\frac{g\left(X_{0}+r\right)}{g(x)}\right] \cdot\left[\frac{f(x)-f\left(X_{0}+\tau\right)}{g(x)-g\left(X_{0}+r\right)}-l\right] \\
+\frac{f\left(X_{0}+\tau\right)-\lg \left(X_{0}+\tau\right)}{g(x)} .
\end{gathered}
$$

由于 $\lim _{x \rightarrow+\infty} g(x)=+\infty$ ，并且 $f(x)$ 与 $g(x)$ 都在 $X_{0} \leqslant x<$ $X_{\mathrm{a}}+1$ 上有界，故必有正数 $X_{1}>a$ 存在，使当 $x>X_{1}$ 时，植有

$$
\left|\frac{g\left(X_{0}+\tau\right)}{g(x)}\right|<\frac{1}{2},\left|\frac{f\left(X_{0}+\tau\right)-\lg \left(X_{0}+\tau\right)}{g(x)}\right|>\frac{\varepsilon}{4} .
$$

令 $X=\max \left\{X_{0}+1, X_{1}\right\}$ 。于是，当 $x>X$ 时，佂有

$$
\left|\frac{f(x)}{g(x)}-l\right|<\frac{3}{2} \cdot \frac{\varepsilon}{2}+\frac{\varepsilon}{4}=\varepsilon .
$$

由此可知 $\lim _{x \rightarrow+\infty} \frac{f(x)}{g(x)}=l . l$ 为有限数时获证。

下设 $l=+\infty$ （若 $l=\cdots \infty$ ，则考虑函数 $-f(x)$ 即可化为 $l=+\infty$ 的情形）。任给 $G>0$ 。存在正数 $X_{\mathrm{n}}>a$ ，使当 $x \geqslant X_{0}$ 时，恒有

$$
\frac{f(x+1)-f(x)}{g(x+1)-g(x)}>4 G
$$

当 $x>X_{0}+1$ 时，仿前一段之证，有

$$
\begin{aligned}
& \frac{f(\tau)-f\left(X_{0}+\tau\right)}{g(\tau)-g\left(X_{0}+\tau\right)}=\sum_{k=1}^{n} \frac{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}{g(\tau)-g\left(X_{0}-\tau\right)} \\
& \cdot \frac{f\left(X_{0}+\tau+k\right)-f\left(X_{0}+\tau+k-1\right)}{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}
\end{aligned}
$$

从而

$$
\begin{aligned}
& \frac{f(x)-f\left(X_{0}+\tau\right)}{g(x)-g\left(X_{0}+\tau\right)} \\
& >4 G \sum_{k=1}^{n} \frac{g\left(X_{0}+\tau+k\right)-g\left(X_{0}+\tau+k-1\right)}{g(x)-g\left(X_{0}+\tau\right)} \\
& =4 G .
\end{aligned}
$$

易知

$$
\begin{aligned}
& \frac{f(x)}{g(x)}=\left[1-\frac{g\left(X_{0}+\tau\right)}{g(x)}\right] \cdot \frac{f(x)-f\left(X_{0}+\tau\right)}{g(x)-g\left(X_{0}+\tau\right)} \\
& +\frac{f\left(X_{0}+\tau\right)}{g(x)} .
\end{aligned}
$$

根据 $\lim _{x \rightarrow+\infty} g(x)=+\infty$ 以及 $f(x), g(x)$ 在 $X_{0} \leqslant x<X_{0}+1$
上的有界性，可取正数 $X_{1}>a$ ，使当 $x>X_{1}$ 时，恒有

$$
\left|\frac{g\left(X_{0}+\tau\right)}{g(x)}\right|<\frac{1}{2},\left|\frac{f\left(X_{0}+\tau\right)}{g(x)}\right|<G .
$$

令 $X=\max \left\{X_{0}+1, X_{1}\right\}$ 。于是, 当 $x>X$ 时, 恒有

$$
\frac{f(x)}{g(x)}>\frac{1}{2} \cdot 4 G-G=G .
$$

由此可知 $\lim _{x \rightarrow+\infty} \frac{f(x)}{g(x)}=+\infty$ 。所述一般性定理获证。
现在我们应用此一般定理来证明本题，在一般性定理中取 $g(x)=x^{n+1}$ 。显然此 $g(x)$ 满足 一 一般性定理的条件，并且

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{g(x+1)-g(x)}=\lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{(x+1)^{n+1}-x^{n+1}} \\
& =\lim _{x \rightarrow-\infty}-\frac{f(x+1)-f(x)}{(n+1) x^{n}+\frac{1}{2}(n+1) n x^{n-1}+\cdots+(n+1) x+1} \\
& =\lim _{x \rightarrow-\infty} \frac{f(x+1)-f(x)}{x^{n}} \\
& =-\frac{1}{(x+1)+\frac{1}{2}(n+1) n x^{-1}+\cdots+(n+1) x^{-n+1}+x^{-n}} \\
& =\frac{l}{n+1} .
\end{aligned}
$$

由此，根据此一般性定理，即得

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{x^{n+1}}=\lim _{x \rightarrow+\infty} \frac{f(x)}{g(x)}=\frac{l}{n+1} .
$$

## 证毕。

* ）原题所说的无穷，必须是带确定符号的无穷，即+或一 $\infty$ ；参看 609 遈末尾加的注。

注。608题的（a）和 609 题可直接从上述一般性定理推出。实际 上，只需令 $g(x)=x$ ，由

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{g(x+1)-g(x)} \\
= & \lim _{x \rightarrow+\infty} \frac{f(x+1)-f(x)}{(x+1)-x} \\
= & \lim _{x \rightarrow+\infty}[f(x+1)-f(x)]
\end{aligned}
$$

即知。
611. 证明：(a) $\lim _{n \rightarrow \infty}\left(1+\frac{x}{n}\right)^{x}=e^{x}$ ；
(6) $\lim _{\rightarrow \infty}\left(1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{2}}{n!}\right)=e^{x}$.

证（a）当 $x=0$ 时是显然的；当 $x \neq 0$ 时，令 $y_{4}=\frac{n}{x}$ ，由 71 题的结果，得

$$
\lim _{n \rightarrow \infty}\left(1+\frac{x}{n}\right)^{*}=\lim _{n \rightarrow \infty}\left(1+\frac{1}{y_{n}}\right)^{3 \cdot x}=e^{x}
$$

（6）当 $x=0$ 时是显然的，我们先讨论 $x>0$ 的倩形。由牛顿二项式定理知

$$
\begin{aligned}
& \left(1+\frac{x}{n}\right)^{n} \\
= & 1+x+\frac{x^{2}}{2!}\left(1-\frac{1}{n}\right)+\cdots+\frac{x^{n}}{n!}\left(1-\frac{1}{n}\right) \cdots\left(1-\frac{n-1}{n}\right) \\
\leqslant & 1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{*}}{n!} .
\end{aligned}
$$

另一方面, 当 $m>n$ 时有

$$
\begin{aligned}
& \left(1+\frac{x}{m}\right)^{-}>1+x+\frac{x^{2}}{2!}\left(1-\frac{1}{m}\right)+\cdots \\
& +\frac{x^{2}}{n!}\left(1-\frac{1}{m}\right) \cdots\left(1-\frac{n-1}{m}\right)
\end{aligned}
$$

令 $m \rightarrow \infty$ ( $n$ 保持不变), 得

$$
e^{x} \geqslant 1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{4}}{n!} .
$$

由此可知

$$
\lim _{n \rightarrow \infty}\left(1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{n}}{n!}\right)=e^{x} \quad(x>0) .
$$

由于

$$
\left(1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{2}}{n!}\right)\left(1-x+\frac{x^{2}}{2!}+\cdots+(-1)^{\frac{x^{4}}{n!}}\right)
$$

$=1+(-1)^{n}\left(\frac{x^{n}}{n!}\right)^{2}$,
而由 61 题知，对固定的 $x$ 有 $\lim _{n \rightarrow \infty} \frac{x^{*}}{n!}=0$ 。于是，对于 $x<0$ ，仍然有

$$
\lim _{x \rightarrow \infty}\left(1+x+\frac{x^{2}}{2!}+\cdots+\frac{x^{n}}{n!}\right)=e^{x} \quad(x<0)
$$

612. 证明: $\operatorname{limnsin}(2 \pi e n!)=2 \pi$ 。

证 由 72 题

$$
e=1+1+\frac{1}{2!}+\cdots+\frac{1}{k!}+\frac{\theta_{k}}{k!k},
$$

其中 $0<\theta_{*}<1$ ，因而
$\lim _{n \rightarrow \infty} n \sin (2 \pi e n!)$
$=\lim _{n \rightarrow \infty} n \sin \left[2 \pi n!\left(1+1+\frac{1}{2!}+\cdots+\frac{1}{(n+1)!}\right.\right.$

$$
\left.\left.+\frac{\theta_{n+1}}{(n+1) \dagger(n+1)}\right)\right]
$$

$=\lim _{n \rightarrow \infty} \frac{\sin \left[2 \pi\left(\frac{1}{n+1}+\frac{\theta_{n+1}}{(n+1)^{2}}\right)\right]}{2 \pi\left(\frac{1}{n+1}+\frac{\theta_{n+1}}{(n+1)^{2}}\right)} \cdot 2 \pi n\left(\frac{1}{n+1}+\frac{\theta_{n+1}}{(n+1)^{2}}\right)$
$=2 \pi$.
作下列函数的囷形：
613. (a) $y=1-x^{100}$;
(6) $y=\lim _{n \rightarrow \infty}\left(1-x^{25}\right) \quad(-1 \leqslant x \leqslant 1)$.

解 (a)如图1.238所示. 它关于 $y$ 轴对称。

$$
\text { (6) } y=\lim _{n \rightarrow \infty}\left(1-x^{2 n}\right)=\left\{\begin{array}{l}
1, \text { 若 }|x|<1 ; \\
0, \text { 若 }|x|=1 .
\end{array}\right. \text { 如图1.239 所 }
$$

示
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-338.jpg?height=647&width=1617&top_left_y=436&top_left_x=188)

图1.238
图1.239
614. (a) $y=\frac{x^{100}}{1+x^{100}} \quad(x \geqslant 0) ;$
(5) $y=\lim _{n \rightarrow \infty} \frac{x^{*}}{1+x^{4}} \quad(x \geqslant 0)$.

解 (a) 如图 1.240 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-338.jpg?height=620&width=727&top_left_y=1529&top_left_x=276)

图 1.240
（6）y=\{ $\left\{\begin{array}{l}0, \text { 若 } 0 \leqslant x<1 ; \\ \frac{1}{2}, \text { 若 } x=1 ; \\ 1, \text { 若 } 1<x<+\infty .\end{array}\right.$
332

如图1.241所示.
615. $y=\lim _{n \rightarrow \infty} \frac{x^{*}-x^{-\pi}}{x^{n}+x^{-n}} \quad(x \neq 0)$.

解 因为 $y=\lim _{\mathrm{k} \rightarrow \infty} \frac{x^{2 n}-1}{x^{3 n}+1}$ ，所以，

$$
y=\left\{\begin{array}{l}
-1, \text { 若 }|x|<1, x \neq 0 ; \\
0, \text { 荅 }|x|=1 ; \\
1, \text { 若 }|x|>1 .
\end{array}\right.
$$

如图1.242所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-339.jpg?height=595&width=795&top_left_y=1093&top_left_x=251)

图 1.242
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-339.jpg?height=458&width=715&top_left_y=1233&top_left_x=1102)

图1.243
616. $y=\lim _{n \rightarrow \infty} \sqrt{x^{2}+\frac{1}{n^{2}}}$.

解 $y=\sqrt{x^{2}}=|x|$ 。
如图1.243所示。
617. $y=\lim _{n \rightarrow \infty} \sqrt[n]{1+x^{4}} \quad(x \geqslant 0)$.

解 $y=\left\{\begin{array}{l}1, \text { 若 } 0 \leqslant x \leqslant 1, \\ x, \text { 若 } x>1 .\end{array}\right.$
如图1.244所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-340.jpg?height=657&width=632&top_left_y=411&top_left_x=304)

国1.244
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-340.jpg?height=723&width=712&top_left_y=415&top_left_x=1072)

图1.245
618. $y=\lim _{n \rightarrow \infty} \sqrt[n]{1+x^{n}+\left(\frac{x^{2}}{2}\right)^{n}} \quad(x \geqslant 0)$.

泽 $y= \begin{cases}1, & \text { 若 } 0 \leqslant x \leqslant 1 ; \\ x, & \text { 若 } 1<x<2 ; \\ \frac{x^{2}}{2}, & \text { 若 } 2 \leqslant x<+\infty .\end{cases}$
如图1.245所示。
619. $y=\lim _{n \rightarrow \infty} \frac{x^{x+2}}{\sqrt{2^{2 x}+x^{2 \pi}}}$
$(x \geqslant 0)$.
早
$y=\left\{\begin{array}{l}0, \text { 若 } 0 \leqslant x<2 ; \\ 2 \sqrt{2}, \text { 若 } x=2 ; \\ x^{2}, \text { 若 } x>2 .\end{array}\right.$
如图1.246所示.
620. (a) $y=\sin ^{1000} x$;
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-340.jpg?height=495&width=632&top_left_y=1803&top_left_x=1095)

图 1.246
(6) $y=\operatorname{limsin}^{28} x$.

解 (a) 如图 1.247 所示. 其图形始终在 $O x$ 轴上方.
（6） $y=\left\{\begin{array}{l}0, \text { 若 } x \neq(2 k+1) \frac{\pi}{2} \\ 1, \text { 若 } x=(2 k+1) \frac{\pi}{2}\end{array}\right.$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-341.jpg?height=418&width=1314&top_left_y=839&top_left_x=491)

图1.247
如图1.248所示
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-341.jpg?height=549&width=886&top_left_y=1550&top_left_x=245)

固 1.248
621. $y=\lim _{n \rightarrow \infty} \frac{\ln \left(2^{n}+x^{*}\right)}{n} \quad(x \geqslant 0)$.

解 $y=\left\{\begin{array}{l}\ln 2, \text { 若 } 0 \leqslant x \leqslant 2 ; \\ \ln x, \text { 若 } 2<x<+\infty .\end{array}\right.$
如图1.249所示.
622. $y=\lim _{n \rightarrow \infty}(x-1) \operatorname{arctg} x^{n}$.

解 $y=\left\{\begin{array}{l}0, \text { 若 }|x| \leqslant 1 ; \\ \frac{\pi}{2}(x-1),\end{array}\right.$
如图1.250 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-342.jpg?height=575&width=835&top_left_y=780&top_left_x=556)

图1.250
623. $y=\lim _{n \rightarrow \infty} \sqrt[n]{1+e^{(j+7)}}$.

解
$y=\left\{\begin{array}{l}1, \text { 若 } x \leqslant-1 ; \\ e^{x-1}, \text { 若 } x>-1 .\end{array}\right.$
如图1.251 所示.
624. $y=\lim _{t \rightarrow+\infty} \frac{x+e^{i x}}{1+e^{i x}}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-342.jpg?height=438&width=643&top_left_y=1403&top_left_x=1089)

图1.251
解
$y=\left\{\begin{array}{l}x, \text { 若 } x<0 ; \\ \frac{1}{2}, \text { 若 } x=0 ; \\ 1, \text { 若 } x>0 .\end{array}\right.$
如图 1.252 所示。
625. $y=\lim _{t \rightarrow x} \frac{1}{t-x} \ln \frac{t}{x}$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-342.jpg?height=483&width=649&top_left_y=1957&top_left_x=1092)

图1.252
$(x>0)$.
解

$$
\begin{gathered}
y=\lim _{t \rightarrow x} \frac{\ln \left(1+\frac{t-x}{x}\right)}{\frac{t-x}{x}} \\
\cdot-\frac{1}{x}=\frac{1}{x} .
\end{gathered}
$$

如图1.253所示。
626. 若有
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-343.jpg?height=601&width=744&top_left_y=382&top_left_x=1067)

图1.253
$\lim _{x \rightarrow \infty}[f(x)-(k x+b)]=0$,
则直线 $y=k x+b$ 称为曲线 $y=f(x)$ 的（斜）斩近线。利用这方程式推出渐近线存在的必要而且充分的条件。
解 先讨论渐近线从右边伸向无穷远的情形：

$$
\lim _{x \rightarrow+\infty}[f(x)-(k x+b)]=0 .
$$

而在 $x>0$ 时，

$$
\frac{f(x)}{x}=\frac{f(x)-(k x+b)}{x}+k+\frac{b}{x} .
$$

可见

$$
\lim _{x \rightarrow+\infty} \frac{f(x)}{x}=k
$$

又由(1)式得

$$
\lim _{x \rightarrow+\infty}[f(x)-k x]=b,
$$

即常数 $k, b$ 可由（2）、(3)式确定。反之，若极限 $\lim _{x \rightarrow+\infty} \frac{f(x)}{x}$存在，且为有限数 $k$ ，极限 $\lim _{x+\infty}[f(x)-k x]$ 存在且有限，等于 $b$, 则(1) 式成立, 即

$$
y=k x+b
$$

是一条渐近线。用完全类似的方法可以讨论 $x \rightarrow \infty$ 的情形。
627. 求下列曲线的渐近线并作其图形：
（a） $y=\frac{x^{2}}{x^{2}+x-2} ; \quad$ (6) $y>\sqrt{x^{2}+x}$;
(в) $y=\sqrt[3]{x^{2}-x^{3}} ; \quad$ (г) $y=\frac{x e^{x}}{e^{x-1}}$;
(n) $y=\ln \left(1+e^{x}\right) ; \quad$ (e) $y=x+\arccos \frac{1}{x}$;
(ж) $y=\frac{x^{1+x}}{(1+x)^{x}}$.

解 (a) 因为 $\lim _{x \rightarrow 1} y=\infty$ 及 $\lim _{x \rightarrow-2} y=\infty$ ，所以，直线 $x=1$ 及 $x$
$=-2$ 为曲线的垂直渐近绩. 其次，因为

$$
k=\lim _{x \rightarrow \infty} \frac{y}{x}=\lim _{x \rightarrow \infty} \frac{x^{2}}{x\left(x^{2}+x-2\right)}=0,
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-344.jpg?height=763&width=937&top_left_y=1463&top_left_x=508)

图1.254
而

$$
b=\lim _{x \rightarrow \infty}(y-k x)=\lim _{x \rightarrow \infty} \frac{x^{2}}{x^{2}+x-2}=1,
$$

所以， $y=1$ 为曲线的水平渐近线。
曲线通过原点。
当 $-2<x<1$ 时, $y<0$ ，故曲线在 $O x$ 轴的下方；
当 $x>1$ 或 $x<-2$ 时, $y>0$, 故曲线在 $O x$ 轴的上方。

适当描若于点；
$A(2,1), B(-\sqrt{2},-\sqrt{2}), C\left(4, \frac{8}{9}\right), D\left(-3, \frac{9}{4}\right), \cdots$,并用光滑曲线联接，即得图形（图1.254）。
(5) $k_{1}=\lim _{x \rightarrow+\infty} \frac{\sqrt{x^{2}+x}}{x}=1$,

$$
\begin{aligned}
& b_{1}=\lim _{x \rightarrow+\infty}\left(\sqrt{x^{2}+x}-x\right)=\frac{1}{2}, \\
& k_{2}=\lim _{x \rightarrow-\infty} \frac{\sqrt{x^{2}+x}}{x}=-1 \\
& b_{2}=\lim _{x \rightarrow-\infty}\left(\sqrt{x^{2}+x}-x\right)=-\frac{1}{2}
\end{aligned}
$$

于是, 直线 $y=x+\frac{1}{2}$ 及 $y=-x-\frac{1}{2}$ 为曲线的（斜）浙近线.

曲线 $y=\sqrt{x^{2}+x}$ 为双曲线

$$
\frac{\left(x+\frac{1}{2}\right)^{2}}{\frac{1}{4}}-\frac{y^{2}}{\frac{1}{4}}=1,
$$

在 $O x$ 轴上方的部分。
如图1.255 所示。
(в) $k=\lim _{x \rightarrow \infty} \frac{\sqrt[3]{x^{2}-x^{3}}}{x}=\lim _{x \rightarrow \infty} \sqrt[3]{\frac{1}{x}-1}=-1$,

$$
\begin{aligned}
b & =\lim _{x \rightarrow \infty}\left(\sqrt[3]{x^{2}-x^{3}}+x\right) \\
& =\lim _{x \rightarrow \infty} \frac{x^{3}+x^{2}-x^{3}}{\sqrt[3]{\left(x^{2}-x^{3}\right)^{2}}-x \sqrt[3]{x^{2}-x^{3}}+x^{2}} \\
& =\lim _{x \rightarrow \infty} \frac{1}{\sqrt[3]{\left(\frac{1}{x}-1\right)^{2}}-\sqrt[3]{\frac{1}{x}-1}+1}=\frac{1}{3} .
\end{aligned}
$$

## 斜浙近线为

$$
y=-x+\frac{1}{3} .
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-346.jpg?height=544&width=755&top_left_y=1096&top_left_x=268)

图 1.255
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-346.jpg?height=744&width=766&top_left_y=987&top_left_x=1053)

图1.256

曲线通过原点及点 $A(1,0)$.
当 $-\infty<x<1$ 时， $y>0$ ；而当 $x>1$ 时， $y<0$ 。
如图1.256所示。
（г）当 $x>0$ 时，

$$
\begin{aligned}
& k=\lim _{x \rightarrow+\infty} \frac{x e^{x}}{x\left(e^{x}-1\right)}=1, \\
& b=\lim _{x \rightarrow+\infty}\left[\frac{x e^{x}}{e^{x}-1}-x\right] \\
& =\lim _{x \rightarrow+\infty} \frac{x}{e^{x}-1}=0
\end{aligned}
$$

## 故渐近线为

$$
y=x ;
$$

当 $x<0$ 时,

$$
\begin{aligned}
& k=\lim _{x \rightarrow-\infty} \frac{x e^{x}}{x\left(e^{x}-1\right)}=0, \\
& b=\lim _{x=\infty} \frac{x e^{x}}{e^{x}-1}=0,
\end{aligned}
$$

故另一渐近线为

$$
y=0
$$

曲线在 $x=0$ 处无定义（以后可以说明它是"可去的间断"）。

因为 $y>0$ ，故图形始终在 $O x$ 轴的上方。
如图1.257所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-347.jpg?height=563&width=706&top_left_y=1432&top_left_x=292)

图1.257
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-347.jpg?height=503&width=661&top_left_y=1436&top_left_x=1097)

图1.258
（д）当 $x>0$ 时，

$$
\begin{aligned}
& k=\lim _{x \rightarrow+\infty} \frac{\ln \left(1+e^{x}\right)}{x}=\lim _{x \rightarrow+\infty}\left[\frac{x+\ln \left(e^{-x}+1\right)}{x}\right]=1, \\
& b=\lim _{x \rightarrow+\infty}\left[\ln \left(1+e^{x}\right)-x\right]=\lim _{x \rightarrow+\infty} \ln \left(e^{-x}+1\right)=0,
\end{aligned}
$$

故浙近线为

$$
y=x
$$

同法可求，当 $x<0$ 时的渐近线为

$$
y=0
$$

曲线通过点 $A(0, \ln 2)$.
如图1.258 所示.
(e) $k=\lim _{x \rightarrow \infty} \frac{x+\arccos \frac{1}{x}}{x}=1$,

$$
b=\lim _{x \rightarrow \infty}\left[\left(x+\arccos \frac{1}{x}\right)-x\right]=\frac{\pi}{2} ;
$$

故渐近线为

$$
y=x+\frac{\pi}{2}
$$

将函数 $y=x$ 及 $y=\arccos \frac{1}{x}$ (见 316 题)的图形按相加法即得，如图 1.259 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-348.jpg?height=527&width=601&top_left_y=1487&top_left_x=362)

图 1.259
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-348.jpg?height=575&width=823&top_left_y=1460&top_left_x=959)

图1.260

$$
\begin{aligned}
(\circledast) k & =\lim _{x \rightarrow \infty} \frac{x^{x}}{(1+x)^{x}}=\lim _{x \rightarrow \infty} \frac{1}{\left(1+\frac{1}{x}\right)^{x}}=\frac{1}{e}, \\
b & =\lim _{x \rightarrow \infty}\left[\frac{x^{1+x}}{(1+x)^{x}}-\frac{x}{e}\right]=\frac{1}{2 e},
\end{aligned}
$$

故渐近线为

$$
y=\frac{x}{e}+\frac{1}{2 e} .
$$

曲线通过原点。
如图1.260所示。
求下列极限：
628. $\lim _{n \rightarrow \infty}\left[\frac{x^{n+1}}{(n+1)!}+\frac{x^{n+2}}{(n+2)!}+\cdots+\frac{x^{2}}{(2 n)!}\right]$.

䐺 由于
$\left|\frac{x^{n+1}}{(n+1)!}+\cdots+\frac{x^{2 n}}{(2 n)!}\right| \leqslant \frac{|x|^{n+1}}{(n+1)!}+\cdots+\frac{|x|^{2 n}}{(2 n)!}$
$\leqslant \frac{|x|^{n+1}}{(n+1)!}\left(1+|x|+\cdots+|x|^{n-1}\right)$.
当 $|x|=1$ 时, 上式右端为 $\frac{n}{(n+1)!} \rightarrow 0(n \rightarrow \infty)$ ；
当 $|x| \neq 1$ 时，此式为 $\frac{|x|^{n+1}}{(n+1) 1} \cdot \frac{1-|x|^{n}}{1-|x|}$
$=\frac{1}{1-|x|} \cdot\left[\frac{|x|^{n+1}}{(n+1) \mid}-\frac{|x|}{n+1} \cdot \frac{\left(|x|^{2}\right)^{n}}{n!}\right]$.
由 61 题的结果知 $: \frac{|x|^{n+1}}{(n+1)!} \rightarrow 0, \frac{\left(|x|^{2}\right)^{n}}{n!} \rightarrow 0(n \rightarrow \infty)$,
故当 $n \rightarrow \infty$ 时有 $\frac{|x|^{n+1}}{(n+1)!} \cdot \frac{1-|x|^{n}}{1-|x|} \rightarrow 0$ 。
于甚，对于任意实数 $x$ ，有

$$
\lim _{n \rightarrow \infty}\left[\frac{x^{n+1}}{(n+1)!}+\frac{x^{n+2}}{(n+2)!}+\cdots+\frac{x^{2 n}}{(2 n)!}\right]=0 .
$$

629. $\lim _{x \rightarrow \infty}\left[(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right) \cdots\left(1+x^{2 n}\right)\right]$, 若 $|x|<1$.

解 因为

$$
\begin{aligned}
& 1+x=\frac{1-x^{2}}{1-x} \\
& 1+x^{2}=\frac{1-x^{4}}{1-x^{2}}
\end{aligned}
$$

$$
1+x^{2}=\frac{1-x^{2^{n+1}}}{1-x^{2^{n}}}
$$

所以,

$$
(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right) \cdots\left(1+x^{2 n}\right)=\frac{1-x^{2^{n!}}}{1-x} .
$$

又因 $|x|<1$, 故当 $n \rightarrow \infty$ 时, $x^{n^{n+1}} \rightarrow 0$ 。
最后，得到
$\lim _{n \rightarrow \infty}\left[(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right) \cdots\left(1+x^{2^{n}}\right)\right]=$ $\frac{1}{1-x}$.
630. $\lim _{x \rightarrow-\infty}\left(\cos \frac{x}{2} \cos \frac{x}{4} \cdots \cos \frac{x}{2^{n}}\right)$.

解 因为

$$
\begin{aligned}
& \sin x=2 \cos \frac{x}{2} \sin \frac{x}{2}=2^{2} \cos \frac{x}{2} \cos \frac{x}{4} \sin \frac{x}{4} \\
& =\cdots=2^{n} \cos \frac{x}{2} \cos \frac{x}{4} \cdots \cos \frac{x}{2^{n}} \sin \frac{x}{2^{n}}
\end{aligned}
$$

所以

$$
\begin{aligned}
& \lim _{n \rightarrow \infty}\left(\cos \frac{x}{2} \cdot \cos \frac{x}{4} \cdots \cos \frac{x}{2^{n}}\right)=\lim _{x \rightarrow \infty}\left(\frac{\sin x}{2^{n}} \cdot \frac{1}{\sin \frac{x}{2^{n}}}\right) \\
& =\lim _{x \rightarrow \infty}\left(\frac{\frac{x}{2^{n}}}{\sin \frac{x}{2^{n}}} \cdot \frac{\sin x}{x}\right)=\frac{\sin x}{x}(x \neq 0) .
\end{aligned}
$$

631. 令 $\quad \lim _{x \rightarrow 0} \frac{\varphi(x)}{\phi(x)}=1$,

其中 $\psi(x)>0$ 且当 $n \rightarrow \infty$ 时 $\alpha_{m n} \neq 0(m=1,2, \cdots n)$ ，换言之，当 $m=1,2, \cdots, n$ 且 $n>N(\varepsilon)$ 时 $\left|\sigma_{m n}\right|<\varepsilon$ 。再假定
$\alpha_{\text {mon }} \neq 0 .{ }^{\cdot 3}$
证明：

$$
\begin{aligned}
& \lim _{x \rightarrow \infty}\left[\varphi\left(\alpha_{1 n}\right)+\varphi\left(\alpha_{2 n}\right)+\cdots \varphi\left(\alpha_{n n}\right)\right] \\
& =\lim _{n \rightarrow \infty}\left[\phi\left(\alpha_{1 n}\right)+\psi\left(\alpha_{2 n}\right)+\cdots+\psi\left(\alpha_{n n}\right)\right],
\end{aligned}
$$

此处榐定等式（1）右端的极限存在。
证 任给 $\varepsilon>0$ ，存在 $\delta>0$ ，使当 $0<|x|<\delta$ 时，佰有

$$
\left|\frac{\varphi(x)}{\psi(x)}-1\right|<\epsilon
$$

从而（注意到 $\psi(x)>0$ ），

$$
(1-\varepsilon) \psi(x)<\varphi(x)<(1+\varepsilon) \psi(x)
$$

由 $\alpha_{m+1} \neq 0$ 以及 $\alpha_{m n}=0(m=1,2, \cdots, n)$ 知，必有正整数 $N$ $=N(\varepsilon)$ 存在, 使当 $n>N$ 时, 恒有

$$
0<\left|\alpha_{m n}\right|<\delta \quad(m=1,2, \cdots, n)
$$

于是

$$
\begin{aligned}
(1-\varepsilon) \psi\left(\alpha_{m n}\right) & <\varphi\left(\alpha_{m n}\right)<(1+\varepsilon) \psi\left(\alpha_{m n}\right) \\
& (n>N, m=1,2, \cdots, n) .
\end{aligned}
$$

特这 $n$ 个不等式相加，得

$$
\begin{gathered}
(1-\varepsilon) \sum_{m=1}^{n} \phi\left(a_{m n}\right)<\sum_{n=1}^{n} \varphi\left(a_{m n}\right)<(1+\varepsilon) \sum_{m=1}^{n} \psi\left(a_{m n}\right) \\
(n>N) .
\end{gathered}
$$

即

$$
1-\varepsilon<\frac{\sum_{m=1}^{n} \varphi\left(\alpha_{m}\right)}{\sum_{m=1}^{n} \psi\left(\alpha_{m n}\right)}<1+\varepsilon \quad(n>N)
$$

由此可知

$$
\lim _{n \rightarrow \infty} \frac{\sum_{m=1}^{n} \varphi\left(\alpha_{m x}\right)}{\sum_{m=1}^{n} \psi\left(\alpha_{m n}\right)}=1
$$

由假定，极限 $\lim _{n \rightarrow \infty} \sum_{m=1}^{n} \psi\left(\alpha_{m n}\right)$ 存在，故

$$
\begin{gathered}
\lim _{n \rightarrow \infty} \sum_{m=1}^{n} \varphi\left(\alpha_{m+n}\right)=\left(\lim _{n \rightarrow \infty} \frac{\sum_{m=1}^{n} \varphi\left(\alpha_{m n}\right)}{\sum_{m=1}^{n} \phi\left(\alpha_{m m}\right)}\right) \cdot\left(\lim _{n \rightarrow \infty} \sum_{m=1}^{n} \phi\left(\alpha_{m+}\right)\right) \\
=\lim _{n \rightarrow \infty} \sum_{m=1}^{n} \psi\left(\alpha_{m n}\right)
\end{gathered}
$$

证毕.

* ）编者注：此题应加上条件 $\alpha_{\text {m }} \neq 0$ （原书没有），因为 $\varphi(x)$ 或 $\phi(x)$ 都可能在 $x=0$ 处无定义. 另外, $m=1,2$, $\cdots, n$.
利用上边的定理，求

632. $\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\sqrt[3]{1+\frac{k}{n^{2}}}-1\right)$.

些 设 $x=\frac{k}{n^{2}}$ ，我们将首先说明它满足 631 题的条件。首先，

$$
\begin{aligned}
\lim _{x \rightarrow 0} \frac{\sqrt[3]{1+x}-1}{\frac{x}{3}} & =\lim _{x \rightarrow 0} \frac{\frac{x}{\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1+x}+1}}{\sqrt[x]{3}} \\
& =\lim _{x \rightarrow 0} \frac{3}{\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1+x}+1}=1 .
\end{aligned}
$$

其次， $\frac{k}{n^{2}}=0:(n \rightarrow \infty ; k=1,2, \cdots, n)$.
最后，

$$
\lim _{n \rightarrow \infty} \sum_{k=i}^{n} \frac{k}{3 n^{2}}=\frac{1}{6} \lim _{x \rightarrow \infty} \frac{n(n+1)}{n^{2}}=\frac{1}{6}
$$

所以，

$$
\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\sqrt[3]{1+\frac{k}{n^{2}}}-1\right)=\frac{1}{6}
$$

633. $\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\sin \frac{k a}{n^{2}}\right)$.

解 因为 $\lim _{x \rightarrow 0} \frac{\sin x}{x}=1$, 而且当 $n \rightarrow \infty$ 时 $\frac{k a}{n^{2}}=0$
$(k=1,2, \cdots, n)$.
又因 $\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{k a}{n^{2}}=\frac{a}{2}$ ，
故利用 631 题的结果，即得

$$
\lim _{n \rightarrow \infty} \sum_{n=1}^{n}\left(\sin \frac{k a}{n^{2}}\right)=\frac{a}{2}
$$

634. $\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(a a_{n^{2}}^{k}-1\right) \quad(a>0)$.

解 我们有 $\lim _{x \rightarrow 0}\left(\frac{a^{x}-1}{x} \cdot \frac{1}{\ln a}\right)=1$, 当 $n \rightarrow \infty$ 时， $\frac{k}{n^{2}}$.
$\ln a=0(k=1,2, \cdots, n)$ 且 $\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{k}{n^{2}} \ln a=\frac{1}{2} \ln a$ ；
因而

$$
\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(a z^{\frac{4}{2}}-1\right)=\frac{1}{2} \ln a
$$

635. $\lim _{n \rightarrow \infty} \prod_{k=1}^{n}\left(1+\frac{k}{n^{2}}\right)$.

解 设 $y=\prod_{k=1}^{n}\left(1+\frac{k}{n^{2}}\right), \ln y=\sum_{k=1}^{n} \ln \left(1+\frac{k}{n^{2}}\right)$.
我们考虑下列极限，

$$
\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \ln \left(1+\frac{k}{n^{2}}\right)
$$

因为

$$
\begin{gathered}
\lim _{x \rightarrow 0} \frac{\ln (1+x)}{x}=1, \\
\text { 又 } \frac{k}{n^{2}} \Rightarrow 0(n \rightarrow \infty \text { 时, } k=1,2, \cdots, n), \text { 且有 } \\
\lim _{n \rightarrow \infty} \sum_{k=1}^{x} \frac{k}{n^{2}}=\frac{1}{2},
\end{gathered}
$$

所以

$$
\lim _{n \rightarrow \infty} \ln y=\frac{1}{2}
$$

即 $\lim _{n \rightarrow \infty} \prod_{k=1}^{n}\left(1+\frac{k}{n^{2}}\right)=e^{\frac{1}{2}}=\sqrt{e}$.
636. $\lim _{n \rightarrow \infty} \prod_{i=1}^{n} \cos \frac{k a}{n \sqrt{n}}$.

解 设 $y=\prod_{k=1}^{n} \cos \frac{k a}{n \sqrt{n}}$, 当 $n$ 充分大时， $\cos \frac{k a}{n \sqrt{n}}>$ 0 , 此时,

$$
\begin{aligned}
& \ln y=\sum_{k=1}^{n} \ln \cos \frac{k a}{n \sqrt{n}} \\
& =-\frac{1}{2} \sum_{k=1}^{n} \ln \left(1+\operatorname{tg}^{2} \frac{k a}{n \sqrt{n}}\right) .
\end{aligned}
$$

因 $\lim _{x \rightarrow 0} \frac{\ln \left(1+\operatorname{tg}^{2} x\right)}{x^{2}}=1$, 又 $\frac{k a}{n \sqrt{n}}=0(n \rightarrow \infty$ 时, $k=1$, $2 \cdots, n$, , 且有

$$
\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{k^{2} a^{2}}{n^{3}}=\lim _{n \rightarrow \infty} \frac{n(n+1)(2 n+1) a^{2}}{6 n^{3}}=\frac{a^{2}}{3},
$$

所以

$$
\lim _{n \rightarrow \infty} \ln y=-\frac{a^{2}}{6}
$$

即

$$
\lim _{n \rightarrow \infty} \prod_{k=1}^{n} \cos \frac{k a}{n \sqrt{n}}=e^{-\frac{a^{2}}{n}}
$$

637. 叙列 $x_{n}$ 由以下的等式所给定：

$$
\begin{aligned}
& x_{1}=\sqrt{a}, x_{i}=\sqrt{a+\sqrt{a}}, x_{3}=\sqrt{a+\sqrt{a+\sqrt{a}}}, \\
& \cdots(a>0) .
\end{aligned}
$$

求 $\lim _{x \rightarrow \infty} x_{n}$.
䇺 首先，我们注意到此叙列显然是单调上升的. 其次，由 $x_{n}=\sqrt{a+x_{n-1}}$, 得 $x_{n}^{2}=a+x_{n-1}$,
即

$$
x_{n}=\frac{a}{x_{n}}+\frac{x_{n-1}}{x_{n}} .
$$

因为 $0<x_{n-1}<x_{n}$ ，即在（1）式右端第二项小于 1 ，所以，

$$
x_{n}<\frac{a}{x_{n}}+1
$$

又显然有 $x_{n}>\sqrt{a} \quad(n=2,3, \cdots)$.
将（3）式代入（2）式右端，即得

$$
x_{n}<\sqrt{a}+1
$$

故叙列 $\left\{x_{n}\right\}$ 是有界的。
根据极限存在的准则可知，叙列 $\left\{x_{*}\right\}$ 的极限 $\lim _{x \rightarrow \infty} x_{x}$ 存在，设其值为 $l$ 。

利用等式 $x_{n}^{2}=a+x_{n-1}$ ，两端取极限，得

$$
l^{2}=a+l,
$$

解之，得

$$
l=\frac{1 \pm \sqrt{1+4 a}}{2} \quad(a>0),
$$

负根不适合（因为 $x_{n}>0$ ），只取其正根，即

$$
\lim _{n \rightarrow \infty} x_{n}=\frac{1+\sqrt{1+4 a}}{2} .
$$

638. 函数叙列

$$
y_{n}=y_{n}(x) \quad(0 \leqslant x \leqslant 1)
$$

用以下的方法来确定：

$$
y_{1}=\frac{x}{2}, y_{n}=\frac{x}{2}-\frac{y_{n-1}^{2}}{2}(n=2,3, \cdots)
$$

求 $\lim _{\sigma \rightarrow \infty} y_{n}$.
解 当 $x=0$ 时， $y_{n}=0, n=1,2, \cdots$ ，则

$$
\lim _{n \rightarrow \infty} y_{n}=0
$$

当 $0<x \leqslant 1$ 时，用旧纳法可证 $y_{n}>0, n=1,2 ; \cdots$ ；
$y_{1}>0$ 。若 $y_{k}>0$ ，由 $x>y_{k-1}^{2}$ ，可得

$$
y_{k+1}=\frac{x}{2}-\frac{y_{k}^{2}}{2}=\frac{4 x-\left(x-y_{k-1}^{2}\right)^{2}}{8} \geqslant \frac{3 x}{8}>0 .
$$

因而有

$$
\begin{aligned}
& y_{1}-y_{3}=\frac{y_{2}^{2}}{2}>0 \\
& y_{2}-y_{4}=\frac{y_{3}^{2}-y_{1}^{2}}{2}<0
\end{aligned}
$$

用归纳法可证

$$
\begin{aligned}
& y_{2 n}-y_{2 n+2}<0 \\
& y_{2-1}-y_{2 n+1}>0 \quad(n=1,2, \cdots)
\end{aligned}
$$

即 $\frac{x}{2}=y_{1}>y_{s}>\cdots>0$,

$$
0<y_{2}<y_{4}<\cdots<\frac{x}{2} .
$$

可见叙列 $y_{1}, y_{3}, \cdots$ 及叙列 $y_{2}, y_{4}, \cdots$ 都是收敛的. 设极限分别为 $A_{1}, A_{2}$, 由

$$
y_{b_{n}}=\frac{x}{2}-\frac{y_{2 n-1}^{2}}{2}
$$

及

$$
y_{2 n+1}=\frac{x}{2}-\frac{y_{2 \pi}^{2}}{2}
$$

求极限得 $A_{2}=\frac{x}{2}+\frac{A_{1}^{2}}{2}, A_{1}=\frac{x}{2}-\frac{A_{2}^{2}}{2}$, 相减得

$$
A_{1}-A_{2}=\left(A_{1}-A_{2}\right) \frac{\left(A_{1}+A_{2}\right)}{2}
$$

而 $0 \leqslant A_{1} \leqslant \frac{x}{2} \leqslant \frac{1}{2}, 0 \leqslant A_{2} \leqslant \frac{x}{2} \leqslant \frac{1}{2}$, 故

$$
A_{1}=A_{2}=A .
$$

用极限定义直接可以证明：若 $\left\{y_{n}\right\}$ 的两个子叙列 $\left\{y_{n}\right\}$ 及 $\left\{y_{m-1}\right\}(n=1,2, \cdots)$ 收敛于同一个极限，则 $\left\{y_{n}\right\}$ 也收敛于这个极限，由

$$
A=\frac{x}{2}-\frac{A^{2}}{2}
$$

解得

即

$$
\begin{gathered}
A=\sqrt{1+x}-1 \\
\lim _{x \rightarrow \infty} y_{n}=\sqrt{1+x}-1 .
\end{gathered}
$$

639. 函数叙列

$$
y_{n}=y_{n}(x) \quad(0 \leqslant x \leqslant 1)
$$

用下面的方法来确定：

$$
y_{1}=\frac{x}{2}, y_{n}=\frac{x}{2}+\frac{y_{x-1}^{2}}{2} \quad(n=2,3, \cdots) .
$$

求 $\lim _{n \rightarrow \infty} y_{n}$.
解 显然， $y_{2} \geqslant y_{1}$ 。假设 $y_{n} \geqslant y_{n-1}$ ，则由

$$
y_{n+1}-y_{n}=\frac{y_{n}^{2}-y_{n-1}^{2}}{2}
$$

便可推出 $y_{x+1} \geqslant y_{n}$ 。
由数学归纳法便得知叙列 $\left\{y_{n}\right\}$ 单调上升。
现在我们证明这个叙列有界。显然

$$
0 \leqslant y_{1}<1 .
$$

设 $0 \leqslant y_{k}<1$, 则 $0 \leqslant y_{k}^{2}<1$ ，且 $0 \leqslant y_{k+1}<1$.
由数学归纳法便得知叙列 $\left\{y_{n}\right\}$ 有界。
这样，我们就证明了此叙列的极限

$$
\lim _{n \rightarrow \infty} y_{n}
$$

存在. 设其值为 $l$ (显然 $0 \leqslant l \leqslant 1$ ), 即得

$$
l=\frac{x}{2}+\frac{l^{z}}{2},
$$

解之, 得 $l=1 \pm \sqrt{1-x}$. 由于 $0 \leqslant l \leqslant 1$, 故必

$$
\lim _{n \rightarrow \infty} y_{4}=l=1-\sqrt{1-x}
$$

640. 为了求克卜勒方程式 ( V равнение Кеглера)

$$
x-\varepsilon \sin x=m \quad(0<\varepsilon<1)
$$

的近似解，假设

$$
x_{0}=m, x_{1}=m+\sin x_{0}, \cdots, x_{n}=m+\sin x_{n-1}
$$

…（逐次遭近法）。
证明有 $\xi^{*}=\lim _{n \rightarrow \infty} x_{n}$ ，且数 $\xi$ 为方程式（1）的唯一的根。
证 首先考虑 $\left|x_{m}-x_{n}\right|$ 。由于

$$
x_{2}-x_{1}=\varepsilon\left(\sin x_{1}-\sin x_{j}\right)=2 \varepsilon \sin \frac{x_{1}-x_{0}}{2} \cos \frac{x_{1}+x_{0}}{2},
$$

## 所以

$$
\begin{aligned}
& \left|x_{2}-x_{1}\right| \leqslant 2 \varepsilon\left|\sin \frac{x_{1}-x_{0}}{2}\right| \leqslant 2 \varepsilon \cdot \frac{\left|x_{2}-x_{0}\right|}{2} \\
& \quad=\varepsilon\left|x_{1}-x_{\mathrm{n}}\right| .
\end{aligned}
$$

同理可证

$$
\left|x_{3}-x_{2}\right| \leqslant \varepsilon^{2}\left|x_{1}-x_{0}\right|
$$

设

$$
\left|x_{n}-x_{n-1}\right| \leqslant \varepsilon^{-1}\left|x_{1}-x_{0}\right|,
$$

则有

$$
\begin{aligned}
& \left|x_{n+1}-x_{n}\right|=2 \varepsilon\left|\sin \frac{x_{n}-x_{n-1}}{2}\right| \cdot\left|\cos \frac{x_{n}+x_{n-1}}{2}\right| \\
& \leqslant \epsilon\left|x_{n}-x_{n-1}\right| \leqslant \epsilon^{*}\left|x_{1}-x_{0}\right| .
\end{aligned}
$$

由数学归纳法得知对于任意的自然数 $n$ ，均有 $\mid x_{n}-$ $x_{n-1}\left|\leqslant \epsilon^{n-1}\right| x_{1}-x_{0} \mid$ 。于是, 当 $m>n$ 时, 有

$$
\begin{aligned}
& \left|x_{m}-x_{n}\right| \leqslant\left|x_{m}-x_{m-1}\right|+\left|x_{m-1}-x_{m-z}\right|+\cdots \\
& +\left|x_{n+1}-x_{n}\right| \\
& \leqslant\left(\varepsilon^{m-1}+\varepsilon^{m-2}+\cdots+\varepsilon^{n}\right)\left|x_{1}-x_{0}\right| \\
& =\varepsilon^{n} \cdot \frac{1-\varepsilon^{m-n}}{1-\varepsilon} \cdot\left|x_{1}-x_{0}\right|
\end{aligned}
$$

而

$$
\left|x_{1}-x_{0}\right|=\varepsilon\left|\sin x_{0}\right| \leqslant \varepsilon,
$$

所以，

$$
\left|x_{m}-x_{n}\right| \leqslant \varepsilon^{++1} \cdot \frac{1-\varepsilon^{m-\varepsilon}}{1-\varepsilon}<\frac{\varepsilon^{n+1}}{1-\varepsilon} .
$$

由此知

$$
\left|x_{m}-x_{n}\right| \rightarrow 0 \quad(n \rightarrow \infty) .
$$

按哥西判别法得知极限

$$
\lim _{n \rightarrow \infty} x_{n}
$$

存在. 设其值为 $\boldsymbol{\xi}$ ，由等式

$$
x_{n}=m+\varepsilon \sin x_{n-1}
$$

取极限即得

$$
\xi=m+\varepsilon \sin \xi
$$

这就是说，变量 $x_{n}$ 的极限 $\boldsymbol{\xi}$ 是方程（1）的根。
最后，证明此根的唯一性。设 $\xi_{1}$ 是另一根，则

$$
\xi_{1}-\xi=\varepsilon\left(\sin \xi_{1}-\sin \xi\right),
$$

由此得

$$
\left|\xi_{1}-\xi\right| \leqslant \varepsilon\left|\xi_{1}-\xi\right| .
$$

因为 $0<\varepsilon<1$, 故 $\xi_{1}=\xi$ 。
于是，我们就证明了 $\xi$ 是方程（ 1 ）的唯一的根。
641. 若 $\omega_{k}(f)$ 为函数 $f(x)$ 在区间 $|x-\xi| \leqslant k(k>0)$ 上的振帽，则数

$$
\omega_{0}(f)=\lim _{k \rightarrow 0} \omega_{k}(f)
$$

称为函数 $f(x)$ 在 $\boldsymbol{\xi}$ 点的振虽。
求下列函数 $f(x)$ 在点 $x=0$ 的振幅；
(a) $f(x)=\sin \frac{1}{x}$;
(б) $f(x)=\frac{1}{x^{2}} \cos ^{2} \frac{1}{x} ;$
(B) $f(x)=x\left(2+\sin \frac{1}{x}\right) ;(\Gamma) f(x) \doteqdot \frac{1}{\pi} \operatorname{arctg} \frac{1}{x} ;$
(a) $f(x)=\frac{|\sin x|}{x} ; \quad$ (e) $f(x)=\frac{1}{1+e^{\frac{1}{x}}} ;$
(ж) $f(x)=(1+|x|)^{\frac{1}{x}}$.

解 (a) $\omega_{k}(f)=2, \omega_{0}(f)=2$ ；

$$
\begin{aligned}
& \text { (б) } \omega_{2}(f)=+\infty, \omega_{0}(f)=+\infty \\
& \text { (в) } \omega_{k}(f)=3 k-k=2 k, \omega_{0}(f)=0 ;
\end{aligned}
$$

$$
\begin{aligned}
& (г) \omega_{k}(f)=\frac{1}{\pi}\left[\operatorname{arctg} \frac{1}{k}-\operatorname{arctg} \frac{1}{(-k)}\right] \\
& \quad=\frac{2}{\pi} \operatorname{arctg} \frac{1}{k}, \\
& \omega_{0}(f)=\frac{2}{\pi} \cdot \frac{\pi}{2}=1 ; \\
& \text { (д) } \omega_{k}(f)=2, \omega_{0}(f)=2 ; \\
& \text { (е) } \omega_{k}(f)=\left|\frac{1}{1+e^{\frac{1}{2}}}-\frac{1}{1+e^{-\frac{1}{k}}}\right|, \omega_{0}(f)=1 ; \\
& \text { (ж) } \omega_{k}(f)=(1+k)^{\frac{1}{2}}-(1+k)^{-\frac{1}{k}, \omega_{0}(f)} \\
& =e-e^{-1}=2 \operatorname{sh} 1 .
\end{aligned}
$$

642. 命

$$
f(x)=\sin \frac{1}{x}
$$

证明；对于满足条件 $-1 \leqslant a \leqslant 1$ 的任何数 $\alpha$ ，可以选出叙列 $x_{n} \rightarrow 0(n=1,2, \cdots \cdot$ 使得

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=a .
$$

证

$$
\text { 村于确定的 } \alpha_{i}|\alpha| \leqslant 1 \text {, 总存在 } x_{0} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \text {, }
$$

使

$$
\sin x_{0}=\alpha
$$

令 $x_{n}=\frac{1}{2 n \pi+x_{0}}$, 则显然有

$$
\lim _{n \rightarrow \infty} x_{n}=0 .
$$

又因 ${ }_{-} f\left(x_{n}\right)=\sin \frac{1}{x_{n}}=\sin \left(2 n \pi+x_{0}\right)=\alpha$ ，
所以

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=\alpha .
$$

643. 设：(a) $f(x)=\sin ^{2} \frac{1}{x}+\frac{2}{\pi} \operatorname{arctg} \frac{1}{x}$ ；

$$
\begin{aligned}
& \text { (6) } f(x)=\left(2-x^{2}\right) \cos \frac{1}{x} \\
& \text { (в) } f(x)=\left(1+\cos ^{2} \frac{1}{x}\right)^{\operatorname{ma}^{2} \frac{1}{x}}
\end{aligned}
$$

求

$$
l=\lim _{x \rightarrow 0} f(x) \text { 和 } L=\lim _{x \rightarrow 0} f(x) .
$$

解 由 $l$ 及 $L$ 的定义, 容易求得

$$
\begin{aligned}
& \text { (а) } l=-1, \quad L=2 ; \\
& \text { (6) } l=-2, \quad L=2 ; \\
& \text { (в) } l=2, \quad L=e .
\end{aligned}
$$

644. 设：
(a) $f(x)=\sin x ;$ (б) $f(x)=x^{2} \cos ^{2} x$;
(B) $f(x)=2^{\operatorname{tin} x^{2}}$;
(r) $f(x)=\frac{x}{1+x^{2} \sin ^{2} x}(x \geqslant 0)$.

求

$$
l=\lim _{x \rightarrow \infty} f(x) \text { 和 } L=\lim _{x \rightarrow \infty} f(x) .
$$

籍 由 $l$ 及 $L$ 的定义，容易求得

$$
\begin{aligned}
& \text { (а) } l=-1, \quad L=1 ; \\
& \text { (б) } l=0, \quad L=+\infty ; \\
& \text { (в) } l=\frac{1}{2}, \quad L=2 ; \\
& \text { (г) } l=0, \quad l=+\infty
\end{aligned}
$$

## §6. 函数无穷小和无穷大的阶

10 符号

$$
\varphi(x)=O^{\prime}(\psi(x))
$$

表示函数 $\varphi(x)$ 利 $\phi(x)$ 在 $x \rightarrow a$ 的已知过程中题憼义地同影的无穷小或无穷大，就是说

$$
\lim _{x \rightarrow e} \frac{\varphi(x)}{\psi(x)}=k \quad(0<|k|<+\infty) .
$$

特别是, 若当 $x \rightarrow 0$ 时, 有

$$
\varphi(x)=O^{*}\left(x^{*}\right) \quad(n>0),
$$

则称 $\varphi(x)$ 为对于无穷小 $x$ 是 $n$ 除无穷小。
仿此, 若当 $x \rightarrow \infty$ 时, 有

$$
\varphi(x)=O^{*}\left(x^{*}\right) \quad(n>0),
$$

则称 $\varphi(x)$ 为对于无穷大 $x$ 是 $n$ 阶无穷大。

## $2^{\circ}$ 符号

$$
\varphi(x)=\sigma(\phi(x))
$$

表示当 $x \rightarrow a$ 时，函数 $\varphi(x)$ 比雨数 $\phi(x)$ 是较高阶的无穷小，或函数 $\varphi(x)$ 比画数 $\psi(x)$ 是较延阶的无突大，就是说

$$
\lim _{x \rightarrow+} \frac{\phi(x)}{\psi(x)}=0 .
$$

$3^{\circ}$ 若当 $x \rightarrow a$ 时，无穷小画数 $\varphi(x)$ 的阶（在广义的意义上）不低宇某一正的函数 $\phi(x)$ 无穷小的阶（或无穷大函数 $\varphi(x)$ 的阶不高于函数 $\psi(x)$ 无穷大的阩)，即

$$
\varlimsup_{x \rightarrow \infty} \frac{|\varphi(x)|}{\phi(x)}=k \quad(0 \leqslant k<+\infty),
$$

则约定写为：

$$
\varphi(x)=O(\phi(x))
$$

$4^{\circ}$ 若

$$
\lim _{x \rightarrow-m} \frac{\varphi(x)}{\phi(x)}=1,
$$

则称宓数 $\varphi(x)$ 稙 $\phi(x)$ 当 $x \rightarrow a$ 时为等升的〔 $\phi(x) \sim \phi(x)]$.
例如, 当 $x \rightarrow 0$ 时, 有:

$$
\begin{aligned}
& \sin x \sim x ; \quad \operatorname{tg} x \sim x \\
& a^{x}-1 \sim x \ln a(a>0) \\
& \sqrt[n]{1+x}-1 \sim \frac{x}{n} ; \quad \ln (1+x) \sim x
\end{aligned}
$$

一般地说来， $\phi(x)+\sigma(\varphi(x)) \sim \varphi(x)$.
当求两个函数比的极腿时，已知函数可用其等价的函数来代换。 645.

把园心角 $A O B=x$ （图

1. 261 ）当作 1 阶无穷小，求下列各量无穷小的阶：
（a）弦 $A B$ ；
(6) 矢 $C D$;
(B) 甪形 $A O B$ 的面积；
（「）三角形 $A B C$ 的面积；
（ $\boldsymbol{n}$ ）梯形 $A B B_{1} A_{1}$ 的面积；
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-364.jpg?height=504&width=609&top_left_y=1187&top_left_x=1140)

图 $1 \cdot 261$
(e) 弓形 $A B C$ 的面积:

角 (a) $A B=2 R \sin \frac{x}{2}$ ，式中 $R$ 为国的半径。
因为 $\frac{A B}{x}=\frac{2 R \sin \frac{x}{2}}{x} \rightarrow R(x \rightarrow 0)$ ，故弦 $A B$ 是关于 $x$ 的一阶无穷小.

$$
\text { (6) } C D=R-R \cos \frac{x}{2}=2 R \sin ^{2} \frac{x}{4}
$$

因为 $\frac{C D}{x^{2}} \rightarrow \frac{R}{8}$, 所以, 矢 $C D$ 是关于 $x$ 的二阶无穷小.
(B) 扇形 $A O B$ 的面积 $S=\frac{1}{2} R^{2} x$.

因为 $\frac{S}{x}=\frac{1}{2} R^{2}$, 所以， $S$ 是关于 $x$ 的一阶无穷小

$$
\text { (г) } \triangle A B C=\frac{1}{2}|A B| \cdot|C D|=2 R^{2} \sin \frac{x}{2} \sin ^{2} \frac{x}{4} \text {. }
$$

因为 $\frac{\triangle A B C}{x^{3}} \rightarrow \frac{R^{2}}{16}$, 所以， $\triangle A B C$ 的面积是关于 $x$ 的三阶无穷小.

$$
\text { (д) } A_{1} C=R \operatorname{tg} \frac{x}{2} \text {. }
$$

于是，梯形 $A B B_{1} A_{1}$ 的面积

$$
\begin{aligned}
A_{0} & =\frac{1}{2} \cdot 2 R \sin ^{2} \frac{x}{2}\left(2 R \sin \frac{x}{2}+2 R \operatorname{tg} \frac{x}{2}\right) \\
& =2 R^{2} \sin ^{9} \frac{x}{2}+2 R^{2} \sin ^{2} \frac{x}{2} \operatorname{tg} \frac{x}{2} .
\end{aligned}
$$

因为 $\frac{A_{0}}{x^{3}} \rightarrow \frac{R^{2}}{4}+\frac{R^{2}}{4}=\frac{R^{2}}{2}$ ，所以，面积 $A_{0}$ 是关于 $x$ 的三阶无穷小.
(e) 弓形 $A B C$ 的面积

$$
\begin{aligned}
p & =\frac{1}{2} R^{2} x-\frac{1}{2} \cdot 2 R \sin \frac{x}{2} \cdot R \cos \frac{x}{2} \\
& =\frac{R^{2}}{2}(x-\sin x) .
\end{aligned}
$$

由于 $x-\sin x$ 是奇沓数,故只需考虑 $x \rightarrow+0$ 时的情形。当 $x \in\left(0, \frac{\pi}{2}\right)$ 时, 有

$$
\begin{gathered}
x-\sin x \leqslant \operatorname{tg} x-\sin x=\frac{\sin x}{\cos x}(1-\cos x) \\
=\frac{\sin x \cdot 2 \sin ^{2} \frac{x}{2}}{\cos x}=O^{*}\left(x^{3}\right)
\end{gathered}
$$

而由 $x \geqslant 2 \sin \frac{x}{2}$, 又有

$$
\begin{gathered}
x-\sin x \geqslant 2 \sin \frac{x}{2}-\sin x=2 \sin \frac{x}{2}\left(1-\cos \frac{x}{2}\right) \\
=4 \sin \frac{x}{2} \sin ^{2} \frac{x}{4}=O^{*}\left(x^{3}\right) .
\end{gathered}
$$

于是, 当 $x$ 大于 0 而充分小时, 存在两常数 $A>0, B$ $>0$ ，使

$$
A x^{3} \leqslant x-\sin x \leqslant B x^{3},
$$

即弓形面积 $p$ 基本上是关于 $x$ 的三阶无穷小，实际上，尔后将会看到，有 $x-\sin x \sim \frac{1}{6} x^{3}$ (但要用到导数的概念)。
646. 命 $o(f(x))$ 为当 $x \rightarrow a$ 时比函数 $f(x)$ 有较低阶的任意无穷大函数, 且 $O(f(x))$ 为 $x \rightarrow a$ 时与函数 $f(x)$ 同阶（在广义的意义上）的任意无穷大函数，其中 $f(x)>0$ 。证明：(a) $\circ\{o[f(x)]\}=o[f(x)]$ ；
(5) $O\{o[f(x)]\}=o[f(x)] ;$
(в) $\{O[f(x)]\}=o[f(x)] ;$
(г) $O\{O[f(x)]\}=O[f(x)] ;$
(д) $O[f(x)]+o[f(x)]=O[f(x)]$;
(e) $O[f(x\}] \cdot O[g(x)]=O \llbracket f(x) g(x)]$.

证 (a) 因为
$\lim _{x \rightarrow a} \frac{o\{o f(x)]\}}{f(x)}=\lim _{x \rightarrow a} \frac{o\{o[f(x)]\}}{o\{f(x)]}: \frac{o[f(x)]}{f(x)}=0$,
故 $\quad o\{o[f(x)]\}=o[f(x)]$.
(6) 由 133 题 ( 5 ) 的结果,有

$$
\lim _{x \rightarrow a} \frac{|O\{o[f(x)]\}|}{f(x)}=\lim _{x \rightarrow a} \frac{|O\{o[f(x)]\}|}{o[f(x)]}
$$

- $\lim _{x \rightarrow a} \frac{o\{f(x)]}{f(x)}=0$,

故 $\quad \lim _{x \rightarrow a} \frac{O[o[f(x)]\}}{f(x)}$ 存在且等于 0 . 因此 $O\{o[f(x)]\}=o[f(x)]$.
(B) 仍由 133 题 (6) 的结果, 有
$\varlimsup_{x \rightarrow a} \frac{|o\{O[f(x)\}\}|}{f(x)}=\lim _{x \rightarrow \alpha}\left|\frac{o\{O[f(x)]\}}{O[f(x)]}\right|$

- $\lim _{x \rightarrow a} \frac{|O[f(x)]|}{f(x)}=0$,

故 $\lim _{s \rightarrow a} \frac{o\{O[f(x)]\}}{f(x)}=0$, 即
$o\{O[f(x)]\}=o[f(x)]$.
( r ) 由 132 題 ( 6 ) 的结果, 有

$$
\begin{gathered}
\lim _{x \rightarrow a} \frac{|O[O[f(x)]\}|}{f(x)} \leqslant \lim _{x \rightarrow a} \frac{|O\{O[f(x)]\}|}{O[f(x)]} \\
\cdot \lim _{x \rightarrow a} \frac{O[f(x)]}{f(x)}<+\infty,
\end{gathered}
$$

故 $O\{O[f(x)]\}=O[f(x)]$.
（」）由 131 题（6），有

$$
\begin{aligned}
& \lim _{x \rightarrow a} \frac{|O[f(x)]+o[f(x)]|}{f(x)} \leqslant \lim _{x \rightarrow a} \frac{|O[f(x)]|}{f(x)} \\
& +\lim _{x \rightarrow a} \frac{|o[f(x)]|}{f(x)}=\lim _{x \rightarrow a} \frac{|O[f(x)]|}{f(x)}<+\infty
\end{aligned}
$$

故 $O[f(x)]+o[f(x))=O[f(x)]$.
(e) 由 132 题 ( 6 )，有
$\lim _{x \rightarrow a} \frac{|O[f(x)] O[g(x)]|}{f(x) g(x)} \leqslant \lim _{x \rightarrow a} \frac{|O[f(x)]|}{f(x)}$

- $\lim _{x \rightarrow a} \frac{|O[g(x)]|}{g(x)}<+\infty$,

故

$$
O[f(x)] O[g(x)]=O[f(x) g(x)]
$$

647. 设 $x \rightarrow+0$ 和 $n>0$. 证明
(a) $C O\left(x^{n}\right)=O\left(x^{a}\right)$
（C 为常数）；
(6) $O\left(x^{n}\right)+O\left(x^{m}\right)=O\left(x^{n}\right) . \quad(n<m) ;$
(в) $O\left(x^{n}\right) O\left(x^{m}\right)=O\left(x^{n+m}\right)$.

证 (a) 由

$$
\lim _{x \rightarrow+\infty} \frac{\left|C O\left(x^{n}\right)\right|}{x^{n}}=|C| \lim _{x \rightarrow+0} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}}<+\infty,
$$

故

$$
C O\left(x^{*}\right)=O\left(x^{n}\right)
$$

(6) 由

$$
\begin{aligned}
& \operatorname{\varlimsup im}_{x \rightarrow+0} \frac{\left|O\left(x^{*}\right)+O\left(x^{m}\right)\right|}{x^{*}} \leqslant \operatorname{\prod im}_{x \rightarrow+0} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}} \\
& +\lim _{x \rightarrow+\infty}\left(\frac{\left|O\left(x^{m}\right)\right|}{x^{m}} \cdot x^{m-n}\right)=\lim _{x \rightarrow+0} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}}<+\infty,
\end{aligned}
$$

故

$$
O\left(x^{*}\right)+O\left(x^{m}\right)=O\left(x^{*}\right) \quad(n<m)
$$

(B) 由

$$
\begin{aligned}
& \lim _{x \rightarrow+0} \frac{\left|O\left(x^{n}\right) O\left(x^{m}\right)\right|}{x^{m+m}} \leqslant \lim _{x \rightarrow+0} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}} \\
& : \lim _{x \rightarrow+0} \frac{\left|O\left(x^{m}\right)\right|}{x^{m}}<+\infty,
\end{aligned}
$$

得知

$$
O\left(x^{*}\right) O\left(x^{* *}\right)=O\left(x^{*+*}\right) .
$$

648. 设 $x \rightarrow+\infty$ 和 $n>0$ 。证明
(a) $C O\left(x^{*}\right)=O\left(x^{*}\right) ;$
(6) $O\left(x^{*}\right)+O\left(x^{m}\right)=O\left(x^{*}\right) \quad(n>m)$.
(в) $O\left(x^{*}\right) O\left(x^{m}\right)=O\left(x^{+m}\right)$.

证 (a) 与（в）同 647 题（a）与（B）之证（只要将 $x \rightarrow+0$换为 $x \rightarrow+\infty$ ）。下证（6）：由于

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} \frac{\left|O\left(x^{n}\right)+O\left(x^{n}\right)\right|}{x^{*}} \\
& \leqslant \lim _{x \rightarrow+\infty} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}}+\lim _{x+\infty}\left(\frac{\left|O\left(x^{0}\right)\right|}{x^{*}} \cdot \frac{1}{x^{n-m}}\right) \\
& =\lim _{x \rightarrow+\infty} \frac{\left|O\left(x^{n}\right)\right|}{x^{n}}<+\infty,
\end{aligned}
$$

故

$$
O\left(x^{n}\right)+O\left(x^{*}\right)=O\left(x^{n}\right)(n>m) .
$$

649. 证明符号 真有下列性质：（1）反射性， $\varphi(x) \sim \varphi(x)$ ； （2）对称性：若 $\varphi(x) \sim \psi(x)$ ，则 $\phi(x) \sim \varphi(x)$ ；(3) 传递性：若 $\varphi(x) \sim \phi(x)$ 及 $\psi(x) \sim \chi(x)$ ，则 $\phi(x) \sim \chi(x)$ 。证 (1) 因为 $\frac{\varphi(x)}{\varphi(x)} \equiv 1 \rightarrow 1$, 所以， $\varphi(x) \sim \alpha(x)$ 。
(2) 因为 $\frac{\varphi(x)}{\psi(x)} \rightarrow 1$, 所以,$\frac{\psi(x)}{\varphi(x)} \rightarrow 1$.

即: 若 $\varphi(x) \sim \phi(x)$ ，则 $\psi(x) \sim \varphi(x)$ 。
(3) 因为 $\frac{\varphi(x)}{\phi(x)} \rightarrow 1, \frac{\psi(x)}{\chi(x)} \rightarrow 1$, 所以,

$$
\frac{\varphi(x)}{\chi(x)}=\frac{\varphi(x)}{\psi(x)} \cdot \frac{\psi(x)}{\chi(\dot{x})} \rightarrow 1,
$$

即： $\varphi(x) \sim \chi(x)$.
650. 设 $x \rightarrow+0$. 证明下列等式:
(a) $2 x-x^{2}=O^{\prime}(x) ;(6) x \sin \sqrt{x}=O^{*}\left(x^{\left.\frac{3}{2}\right) ;} ;\right.$
(в) $x \sin \frac{1}{x}=O(|x|) ;(\mathrm{r}) \ln x=o\left(\frac{1}{x^{2}}\right)(\epsilon>0) ;$
(д) $\sqrt{x+\sqrt{x+\sqrt{x}}} \sim \sqrt[1]{x}$;
(e) $\operatorname{arctg} \frac{1}{x}=O(1) ;(ж)(1+x)^{n}=1+n x+o(x)$.

证 由题设 $x \rightarrow+0$,于是
（a）因为 $\frac{2 x-x^{2}}{x} \rightarrow 2$ ，所以， $2 x-x^{2}=O^{*}(x)$ 。
（6）因为 $\frac{x \sin \sqrt{x}}{x \sqrt{x}} \rightarrow 1$ ，所以， $x \sin \sqrt{x}=O^{*}\left(x^{\frac{3}{2}}\right)$ 。
(в) 因为 $\left|x \sin \frac{1}{x}\right| \leqslant|x|(x \neq 0)$ ，所以，

$$
x \sin \frac{1}{x}=O(|x|)
$$

（г）因为 $\frac{\ln x}{\frac{1}{x^{*}}}=x^{*} \ln x \rightarrow 0$, 所以， $\ln x=o\left(\frac{1}{x^{*}}\right)$.
(д) 因为 $\lim _{x \rightarrow+0} \frac{\sqrt{x+\sqrt{x+\sqrt{x}}}}{x^{\frac{1}{8}}}$
$=\lim _{x \rightarrow+\infty} \sqrt{x^{\frac{3}{4}}+\sqrt{x^{\frac{1}{2}}+1}}=1$,
故 $\sqrt{x+\sqrt{x+\sqrt{x}}} \sim x^{\frac{1}{8}}$,
(e) 因为 $\left|\operatorname{arctg} \frac{1}{x}\right| \leqslant \frac{\pi}{2}(x \neq 0)$, 所以, $\operatorname{arctg} \frac{1}{x}=$ $O(1)$.

$$
\text { (ж) 因为 } \frac{(1+x)^{n x}-1-n x}{x}=\frac{1}{2} n(n-1) x+\cdots
$$

$\rightarrow 0$,
所以 $(1+x)^{n}-1-n x=o(x)$ ，即

$$
(1+x)^{n}=1+n x+o(x) .
$$

651. 设 $x \rightarrow+\infty$. 证明下列等式：
(a) $2 x^{3}-3 x^{2}+1=O \cdot\left(x^{3}\right) ;$
(б) $\frac{x+1}{x^{2}+1}=O^{*}\left(\frac{1}{x}\right)$;
(в) $x+x^{2} \sin x=O\left(x^{2}\right)$;
(г) $\frac{\operatorname{arctg} x}{1+x^{2}}=O^{*}\left(\frac{1}{x^{2}}\right)$;
(д) $\ln x=o\left(x^{0}\right) \quad(\varepsilon>0) ;$
(e) $x^{P} e^{-x}=o\left(\frac{1}{x^{2}}\right)$;
(ж) $\sqrt{x+\sqrt{x+\sqrt{x}}} \sim \sqrt{x}$;
(3) $x^{2}+x \ln ^{100} x \sim x^{2} ;$

拄 由题设 $x \rightarrow+\infty$ ，于是
(a) 因为 $\frac{2 x^{5}-3 x^{2}+1}{x^{3}} \rightarrow 2$, 所以

$$
2 x^{3}-3 x^{2}+1=O^{*}\left(x^{3}\right)
$$

（6）因为 $\frac{\frac{x+1}{x^{2}+1}}{\frac{1}{x}}=\frac{x(x+1)}{x^{2}+1} \rightarrow 1$ ，所以， $\frac{x+1}{x^{2}+1}=O^{2}\left(\frac{1}{x}\right)$.
(B) 因为 $\lim _{x \rightarrow+\infty} \frac{\left|x+x^{2} \sin x\right|}{x^{2}}=\lim _{x \rightarrow+\infty}\left|\frac{1}{x}+\sin x\right|$ $=1<+\infty$, 所以, $x+x^{2} \sin x=O\left(x^{2}\right)$.
（г）因为 $\frac{\frac{\operatorname{arctg} x}{1+x^{2}}}{\frac{1}{x^{2}}}=\frac{x^{2} \operatorname{arctg} x}{1+x^{2}} \rightarrow \frac{\pi}{2}$ ，所以，

$$
\frac{\operatorname{arctg} x}{1+x^{2}}=O^{*}\left(\frac{1}{x^{2}}\right)
$$

（a）因为 $\frac{\ln x}{x^{*}} \rightarrow 0$ ，所以，

$$
\ln x=o\left(x^{r}\right)
$$

（e）因为 $\frac{x^{y} e^{-x}}{\frac{1}{x^{2}}}=\frac{x^{p+2}}{e^{x}} \rightarrow 0$ ，所以，

$$
x^{p} e^{-x}=o\left(\frac{1}{x^{2}}\right) .
$$

(*) 因为 $\frac{\sqrt{x+\sqrt{x}+\sqrt{x}}}{\sqrt{x}}$
$=\sqrt{1+\sqrt{\frac{1}{x}+\sqrt{\frac{1}{x^{9}}}}} \rightarrow 1$, 所以, $\left.\sqrt{x+\sqrt{x+\sqrt{x}}}\right)$ $\sqrt{x}$.
（3）因为 $\frac{x^{2}+x \ln ^{100} x}{x^{2}}=1+\frac{\ln ^{100} x}{x} \rightarrow 1$, 所以 $x^{2}+x \ln ^{100} x \sim x^{2}$.
652. 证明当 $x$ 充分大时，下边的不等式成立：
(a) $x^{2}+10 x+100<0.001 x^{3}$;
(б) $\ln ^{1000} x<\sqrt{x} ;$ (в) $x^{10} e^{x}<e^{2 x}$.

证（a）因为当 $x \rightarrow+\infty$ 时， $\frac{x^{2}+10 x+100}{0.001 x^{3}} \rightarrow 0$ ，
所以，当 $x$ 充分大以后，有 $\frac{x^{2}+10 x+100}{0.001 \dot{x}^{3}}<1$ ，即

$$
x^{2}+10 x+100<0.001 x^{3}
$$

（6）因为当 $x \rightarrow+\infty$ 时，要 $\frac{\mathbf{1}^{1000} x}{\sqrt{x}} \rightarrow 0$ ，所以，当 $x$ 充分大以后，有 $\frac{\ln ^{1000} x}{\sqrt{x}}<1$ ，即

$$
\ln ^{1000} x<\sqrt{x} .
$$

（в）因为当 $x \rightarrow+\infty$ 时， $\frac{x^{10} e^{x}}{e^{2 x}}=\frac{x^{10}}{e^{x}} \rightarrow 0$ ，所以，当 $x$

充分大后，有 $\frac{x^{10} e^{x}}{e^{2 x}}<1$ ，即

$$
x^{10} e^{x}<e^{2 x} .
$$

653. 设 $x \rightarrow 0$. 选出下列函数的形如 $C x^{*}$ ( $C$ 为常数) 的主部,并求其对于无穷小变数 $x$ 的阶：
(a) $2 x-3 x^{3}+x^{5}$; (6) $\sqrt{1+x}-\sqrt{1-x}$;
(B) $\sqrt{1-2 x}-\sqrt[3]{1-3 x}$; ( r ) $\operatorname{tg} x-\sin x$.

解 所谓函数 $f(x)$ 的主部 $g(x)$ ，即满足

$$
\begin{aligned}
& \frac{f(x)}{g(x)} \rightarrow 1 \text { 或 } f(x)=g(x)+o(x)(x \rightarrow 0) . \\
& \text { (a) 因为 } \frac{2 x-3 x^{3}+x^{5}}{2 x} \rightarrow 1 \quad(x \rightarrow 0),
\end{aligned}
$$

故其主部为 $2 x$ ，它对于无穷小 $x$ 是一险的.
（6）因为 $\frac{\sqrt{1+x}-\sqrt{1-x}}{x}$
$=\frac{2}{\sqrt{1+x}+\sqrt{1-x}} \rightarrow 1(x \rightarrow 0)$,
故其主部为 $x$ ，它对于 $x$ 是一阶的。
(B) 因为 $\sqrt{1-2 x}-\sqrt[3]{1-3 x}$
$=\frac{3 x^{2}-8 x^{3}}{\sqrt[8]{(1-2 x)^{16}}+\sqrt{(1-2 x)^{12} \cdot(1-3 x)^{2}}+\cdots+\sqrt[8]{(1-3 x)^{10}}}$,
于是， $\frac{\sqrt{1-2 x}-\sqrt[3]{1-3 x}}{\frac{x^{2}}{2}} \rightarrow 1(x \rightarrow 0)$ ，故其主部为 $\frac{x^{2}}{2}$, 它对于 $x$ 是二阶的.
（ ）因为 $\operatorname{tg} \dot{x}-\sin x=\frac{2}{\cos x} \sin x \sin ^{2} \frac{x}{2}$ ，于是，
$\frac{\operatorname{tg} x-\sin x}{\frac{x^{3}}{2}} \rightarrow 1(x \rightarrow 0)$ ，故其主部为 $\frac{x^{2}}{2}$ ，它对于 $x$ 是三阶

的。
654. 设 $x \rightarrow+0$ ，证明无穷小
(a) $f(x)=\frac{1}{\ln x} ;$ ( 6$) f(x)=e^{-\frac{1}{x^{2}}}$,

无论对任何的 $n$ ，也不能与无穷小 $x^{2}(n>0)$ 相比较.
即：对于如此的 $n$ ，不能有等式 $\lim _{x \rightarrow+\infty} \frac{f(x)}{x^{n}}=k$ ，式中 $k$ 为异于零的有限量。
证 (a) 因为 $\lim _{x \rightarrow+0} x^{2} \ln x=0^{*}(n>0)$, 于是,

$$
\lim _{x \rightarrow+0} \frac{\frac{1}{\ln x}}{x^{*}}=\infty,
$$

即 $\frac{1}{\ln x}$ 不能与无穷小 $x^{n}$ 相比较 $(x \rightarrow+0)$ 。
（6）因为 $\lim _{x \rightarrow+0} \frac{e^{-\frac{1}{x^{2}}}}{x^{*}}=0^{\cdots}(n>0)$ ，所以， $e^{-\frac{1}{x^{2}}}$ 不能与无穷小 $x^{n}$ 相比较 $(x \rightarrow 0)$ 。

* ）参看 592 题。
*     * ）参看 591 题。

655. 设 $x \rightarrow 1$. 选出下列函数的形如 $C(x-1)^{n}$ 的主部, 并求其对于无穷小 $(x-1)$ 的阶：
（а） $x^{3}-3 x+2 ;$ (б) $\sqrt[3]{1-\sqrt{x}}$ ；(в) $\ln x$ ；
(г) $e^{x}-e ;(д) x^{x}-1$.

解 (a) 因为 $x^{3}-3 x+2=(x-1)^{2}(x+2)$, 又

$$
\frac{x^{3}-3 x+2}{3(x-1)^{2}} \rightarrow 1(x \rightarrow 1)
$$

故其主部为 $3(x-1)^{2}$, 对于 $(x-1)$ 是二阶无穷小
（б）因为 $\sqrt[3]{1-\sqrt{x}}=-\frac{\sqrt[3]{x-1}}{\sqrt[3]{1+\sqrt{x}}}$, 又

$$
\frac{\sqrt[3]{1-\sqrt{x}}}{-\frac{\sqrt[3]{x}-1}{\sqrt[3]{2}}} \rightarrow 1(x \rightarrow 1)
$$

故其主部为 $\frac{\sqrt[3]{1-x}}{\sqrt[3]{2}}$ ，对于 $(x-1)$ 是 $\frac{1}{3}$ 阶无穷小。
(в) 因为 $\frac{\ln x}{x-1}=\frac{\ln [1+(x-1)]}{x-1} \rightarrow 1(x \rightarrow 1)$,

故其主部为 $x-1$ ，对于 $(x-1)$ 是一阶无穷小。
（ r ）因为 $e^{x}-e=e\left(e^{x-1}-1\right)$ ，又

$$
\frac{e^{x-1}-1}{x-1} \rightarrow 1(x \rightarrow 1)
$$

故其主部为 $e(x-1)$ ，对于 $(x-1)$ 是一阶无穷小。

$$
\text { (if) 因 } x^{x}-1=e^{\tan x}-1 \text {, 又 }
$$

$\frac{e^{\tan x}-1}{x-1}=\frac{e^{x \ln x}-1}{x \ln x} \cdot \frac{x \ln [1+(x-1)]}{x-1} \rightarrow 1(x \rightarrow 1)$,故其主部为 $x-1$ ，对于（ $x-1$ ）是一阶无穷小。
656. 设 $x \rightarrow+\infty$ 。选出下列函数的形如 $C x^{n}$ 的主部, 并求其对于无穷大 $x$ 的阶：
（a） $x^{2}+100 x+10000 ;$ （6） $\frac{2 x^{5}}{x^{3}-3 x+1}$ ；
(в) $\sqrt[3]{x^{2}-x}+\sqrt{x} ;$ (г) $\sqrt{1+\sqrt{1+\sqrt{x}}}$.

解 （a）因为 $x^{2}+100 x+10000 \sim x^{2}(x \rightarrow+\infty)$ ，故主部为 $x^{2}$, 它对于无穷大 $x$ 是二阶的。
（5）因为 $\frac{\frac{2 x^{5}}{x^{3}-3 x+1}}{2 x^{2}}=\frac{2 x^{5}}{2 x^{5}-6 x^{3}+2 x^{2}}$,

$$
\rightarrow 1(x \rightarrow+\infty)
$$

故主部 $2 x^{2}$ ，它对于无穷大 $x$ 是二阶的。

$$
\text { (B) } \sqrt[3]{x^{2}-x}+\sqrt{x}=x^{\frac{2}{3}}\left(\sqrt[3]{\left(1-\frac{1}{x}\right)}+\sqrt[6]{\frac{1}{x}}\right) \text {, }
$$

于是,
$\frac{\sqrt[3]{x^{2}-x}+\sqrt{x}}{x^{\frac{2}{3}}}=\sqrt[3]{\left(1-\frac{1}{x}\right)}+\sqrt[6]{\frac{1}{x}} \rightarrow 1(x \rightarrow+$ $\infty$ ),
故主部为 $x^{\frac{2}{3}}$ ，它对于无穷大 $x$ 是 $\frac{2}{3}$ 岎的。

$$
\text { (r) 因为 } \frac{\sqrt{1+\sqrt{1+\sqrt{x}}}}{\sqrt[8]{x}} \rightarrow 1(x \rightarrow+\infty),
$$

故主部为 $\sqrt[8]{x}$ ，它对于无穷大 $x$ 是 $\frac{1}{8}$ 阶的：
657. 设 $x \rightarrow+\infty$. 选出下列函数的形如 $C\left(\frac{1}{x}\right)^{n}$ 的主部, 并求其对于无穷小 $\frac{1}{x}$ 的阶：
(a) $\frac{x+1}{x^{4}+1} ;$
(6) $\sqrt{x+1}-\sqrt{x}$;
(в) $\sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x}$; (г) $\frac{1}{x} \sin \frac{1}{x}$.

招（a）因为 $\frac{\frac{x+1}{x^{4}+1}}{\left(\frac{1}{x}\right)^{3}}=\frac{x^{3}(x+1)}{x^{4}} \rightarrow 1(x \rightarrow+\infty)$ ，
故主部为 $\left(\frac{1}{x}\right)^{3}$ ，它对于无穷小 $\frac{1}{x}$ 是 3 阶的。

$$
\text { (6) } \begin{aligned}
\text { 因为 } & \frac{\sqrt{x+1}-\sqrt{x}}{\frac{1}{2 \sqrt{x}}}=\frac{2 \sqrt{x}}{\sqrt{x+1}+\sqrt{x}} \\
& \rightarrow 1(x \rightarrow+\infty)
\end{aligned}
$$

故主部为 $\frac{1}{2}\left(\frac{1}{x}\right)^{\frac{1}{2}}$ ，它对于无穷小 $\frac{1}{x}$ 是 $\frac{1}{2}$ 阶的。

$$
\begin{aligned}
& \text { (B) } \sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x} \\
& =\frac{2 \sqrt{x(x+2)}-2(x+1)}{\sqrt{x+2}+\sqrt{x+2 \sqrt{x+1}}} . \\
& =\frac{-2}{(\sqrt{x+2}+\sqrt{x}+2 \sqrt{x+1})(\sqrt{x(x+2)}+x+1)} .
\end{aligned}
$$

于是, 由此得

$$
\frac{\sqrt{x+2}-2 \sqrt{x+1}+\sqrt{x}}{-\frac{1}{4} x^{\frac{1}{2}}}
$$

$$
\begin{aligned}
& =\frac{\left(\sqrt{1+\frac{2}{x}}+1+2 \sqrt{1+\frac{1}{x}}\right)}{\left(\sqrt{1+\frac{2}{x}}+1+\frac{1}{x}\right)} \\
& \rightarrow 1(x \rightarrow+\infty),
\end{aligned}
$$

故主部为 $-\frac{1}{4} x^{\frac{3}{2}}$ ，它对于无穷小 $\frac{1}{x}$ 是 $\frac{3}{2}$ 阶的。
（「）因为 $\frac{\frac{1}{x} \sin \frac{1}{x}}{\frac{1}{x^{2}}}=\frac{\sin \frac{1}{x}}{\frac{1}{x}} \rightarrow 1(x \rightarrow+\infty)$ ，
（а） $\frac{x^{2}}{x^{2}-1}$;（б） $\sqrt{\frac{1+x}{1-x}}$; (в) $\frac{x}{\sqrt[3]{1-x^{3}}}$;
（г） $\frac{1}{\sin \pi x}$; (ㄱ) $\frac{\ln x}{(1-x)^{2}}$;
解

$$
\begin{aligned}
& \text { (a) } \frac{x^{2}}{x^{2}-1}=\frac{x^{2}}{(x-1)(x+1)} \text {, 于是, } \\
& \frac{x^{2}}{x^{2}-1}=\frac{2 x^{2}}{x+1} \rightarrow 1(x \rightarrow 1),
\end{aligned}
$$

故主部为 $\frac{1}{2(x-1)}$ ，它对于无穷大 $\frac{1}{x-1}$ 是一阶的。

$$
\text { (6) 因为 } \begin{aligned}
& \frac{\sqrt{\frac{1+x}{1-x}}}{\sqrt{2}} \frac{1}{\sqrt{1-x}}
\end{aligned}=\frac{\sqrt{1+x}}{\sqrt{2}}
$$

故主部为 $\sqrt{2}\left(\frac{1}{1-x}\right)^{\frac{1}{2}}$ ，它对于无穷大 $\frac{1}{1-x}$ 是 $\frac{1}{2}$ 阶的。

$$
\text { （в）因为 } \frac{x}{\sqrt[3]{1-x^{3}}}=\frac{x}{\sqrt[3]{1-x}} \cdot \frac{1}{\sqrt[3]{1+x+x^{2}}} \text {, 于 }
$$

是，

$$
\frac{\frac{x}{\sqrt[3]{1-x^{3}}}}{\frac{1}{\sqrt[3]{3} \sqrt[3]{1-x}}} \rightarrow(x \rightarrow 1),
$$

故主部为 $\frac{1}{\sqrt[3]{3}}\left(\frac{1}{1-x}\right)^{\frac{2}{3}}$ ，它对于无穷大 $\frac{1}{x-1}$ 是 $\frac{1}{3}$ 阶的.

$$
\text { (r) 因为 } \frac{\frac{1}{\sin \pi x}}{\frac{1}{\pi(1-x)}}=\frac{\pi(1-x)}{\sin \pi(1-x)} \rightarrow 1(x \rightarrow 1) \text {, }
$$

故主部为 $\frac{1}{\pi}\left(\frac{1}{1-x}\right)$, 它对于无穷大 $\frac{1}{x-1}$ 是一阶的.

$$
\text { (д) } \begin{aligned}
\text { 因为 } & \frac{\frac{\ln x}{(1-x)^{2}}}{\frac{1}{x-1}}=\frac{\ln [1+(x-1)]}{x-1} \\
& \rightarrow 1(x \rightarrow 1)
\end{aligned}
$$

故主部为 $\frac{1}{x-1}$, 它对于无穷大 $\frac{1}{x-1}$ 是一阶的。
659. 设 $x \rightarrow+\infty$ 和 $f_{\mathrm{n}}(x)=x^{n}(n=1,2, \cdots)$ 。证明：
(1) $f_{n}(x)$ 中的每一个函数都比其前面的一个函数 $f_{\mathrm{s}-1}(x)$ 增加较快；
（2）函数 $e^{x}$ 比函数 $f_{n}(x)(n=1,2, \cdots)$ 中的每一个都增加得较快。
证 (1) 因为 $\frac{f_{n}(x)}{f_{n-1}(x)}=x \rightarrow+\infty$, 所以, $f_{n}(x)$ 比 $f_{n-1}(x)$ 增加较快.
（2）因为 $\frac{e^{x}}{x^{n}} \rightarrow+\infty(x \rightarrow+\infty, n$ 为任一固定的自然数），所以 $e^{x}$ 比 $f_{n}(x)$ 中的每一个都增加得较块。
660. 设 $x \rightarrow+\infty$ 和 $f_{n}(x)=\sqrt[7]{x}(n=1,2, \cdots)$. 证明：
(1) 函数 $f_{n}(x)$ 中的每一个都比其前面的一个函数 $f_{\mathrm{n}-1}(x)$ 增加得较悰；
(2) 函数 $f(x)=\ln x$ 比函数 $f_{n}(x)(n=1,2, \cdots)$ 中的每一个都增加得较慢。

证 (1) 因为 $\frac{f_{m}(x)}{f_{n-1}(x)}=x^{-\frac{1}{n(n-1)}}$

$$
\rightarrow 0(x \rightarrow+\infty),
$$

所以, $f_{n}(x)$ 比 $f_{k-1}(x)$ 增加得较慢.
（2）因为 $\frac{\ln x}{\sqrt[7]{x}} \rightarrow 0^{\prime}(x \rightarrow+\infty)$,
所以， $\ln x$ 比 $f_{\mathrm{N}}(x)$ 中的每一个增加得较慢。
*) 利用 565 题的结果。
661. 证明对于任意的函数叙列

$$
f_{1}(x), f_{2}(x), \cdots, f_{n}(x), \cdots\left(x_{0}<x<+\infty\right)
$$

可举出一函数 $f(x)$, 当 $x \rightarrow+\infty$ 时它比函数 $f_{n}(x)(n=$ $1,2, \cdots$ )中的每一个都增加得较快。
证 取正整数 $N>x_{0}$. 定义 $x_{0}<x<+\infty$ 上的函数 $f(x)$ 如下:

$$
f(x)=\left\{\begin{array}{l}
n\left(\sum_{i=1}^{n}\left|f_{k}(x)\right|+1\right), \text { 当 } n \leqslant x<n+1 \text { 时, } \\
\quad(n=N, N+1, \cdots) ; \\
0, \text { 当 } x_{0}<x<N \text { 时. }
\end{array}\right.
$$

于是，对任何正整数 $n$ ，当 $x>\max \{N, n\}$ 时，有

$$
\left|\frac{f_{n}(x)}{f(x)}\right|=\frac{\left|f_{n}(x)\right|}{[x]\left(\sum_{i=1}^{[x]}\left|f_{k}(x)\right|+1\right)}<\frac{1}{[x]}
$$

其中 $[x]$ 表 $x$ 的整数部分. 由此可知

$$
\lim _{x \rightarrow+\infty} \frac{f_{x}(x)}{f(x)}=0 \quad(n=1,2, \cdots),
$$

故当 $x \rightarrow+\infty$ 时, $f(x)$ 比 $f_{n}(x)(n=1,2, \cdots)$ 中的每个都增如得较快。

## § 7. 函数的连续性

1 "函数的连续性 设

$$
\lim _{x \rightarrow x_{0}} f(x)=f\left(x_{0}\right),
$$

即，若对于每一个 $\varepsilon>0$ ，都有 $\delta=\delta\left(\varepsilon, x_{0}\right)>0$ ，使当 $\left|x-x_{0}\right|<\delta$时，对于 $f(x)$ 的有意义的一切值，不等式

$$
\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon
$$

都成立，则称函数 $f(x)$ 当 $x=x_{0}$ 时（或在点 $x_{0}$ ）是连续的.
若函数 $f(x)$ 在集合 $\dot{X}$ 上的每一点都是连统的；则称函数 $f(x)$ 在已知集合 $X=\{x\}$ （区间，线段等等）上是连续佮。

若某值 $x=x_{0}$ 尼于函数 $f(x)$ 的定 叉域 $X=\{x\}$ 或为此穄合
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-381.jpg?height=76&width=1469&top_left_y=1347&top_left_x=322)换言之，函数在点 $x=x_{0}$ 没有定义，或 $(\sigma) \lim _{x \rightarrow x_{0}} f(x)$ 不存在，或（ B ）公式（1）的两端虽存乽义，但它们不相等了，题称 $x_{0}$ 为而数 $f(x)$ 的丕達续点。

分为：（1）策一类的不连绩点 $x_{0}$ ，对于这些点存在有单的有限的根限：

$$
f\left(x_{0}-0\right)=\lim _{x \rightarrow x_{0}-0} f(x) \text { 和 } f\left(x_{0}+0\right)=\lim _{x \rightarrow x_{0}+\infty} f(x) .
$$

（2）第二类的不透续点一其余的一切不连矣点.
差

$$
f\left(x_{1}+0\right)-f\left(x_{0}-0\right)
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-381.jpg?height=86&width=572&top_left_y=2170&top_left_x=322)
若等式

$$
f\left(x_{0}-0\right)=f\left(x_{0}+0\right)
$$

成立，制不连续点 $x_{0}$ 委为充峦化的. 若极限 $f\left(x_{0}-0\right)$ 或 $f\left(x_{0}+0\right)$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-381.jpg?height=81&width=1226&top_left_y=2487&top_left_x=324)

若等式

$$
f\left(x_{0}-0\right)=f\left(x_{0}\right)\left[\text { 或 } f\left(x_{0}+0\right)=f\left(x_{0}\right)\right]
$$

成立，则称函数 $f(x)$ 在点 $x_{0}$ 是左偩 (或右侧) 连续. 函数 $f(x)$ 在点 $x_{0}$ 连续的充分而且必要的条件为下面三个数相等：

$$
f\left(x_{0}-0\right)=f\left(x_{0}+0\right)=f\left(x_{0}\right) .
$$

$2^{\circ}$ 初等函数的连续性 若函数 $f(x)$ 和 $g(x)$ 在 $x=x_{1}$ 连续，则函数

$$
\begin{aligned}
& \text { (a) } f(x) \pm g(x), \quad(6) f(x) g(x) ; \\
& \text { (घ) } \frac{f(x)}{g(x)}\left[g\left(x_{0}\right) \neq 0\right]
\end{aligned}
$$

也在 $x=x_{0}$ 连续.
特殊情形：(a) 有理整函数

$$
\cdot P(x)=a_{0}+a_{1} x+\cdots+a_{n} x^{n}
$$

对任何的 $x$ 值都是连续的：(6) 有理分式函数

$$
R(x)=\frac{a_{0}+a_{1} x+\cdots+a_{n} x^{*}}{b_{0}+b_{1} x+\cdots+b_{m} x^{n}}
$$

对所有不使其分母为条的 $x$ 值，都是连续的。
一般地说，基本初等函数： $x^{*}, \sin x, \cos x, \operatorname{tg} x ; a^{x}, \log x, \mathrm{arc}$ $\sin x, \arccos x, \operatorname{arctg} x, \cdots$ 在一双使它们有意义的点都辇续。

较普遍的结果如下：若函数 $f(x)$ 当 $x=x_{0}$ 时迋续，及函数 $g(y)$ 当 $y=f\left(x_{0}\right)$ 时连续，则画数 $g(f(x))$ 当 $x=x_{0}$ 时连统。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-382.jpg?height=74&width=1349&top_left_y=1930&top_left_x=451) $[a, b]$ 内连续，则：(1) 函数 $f(x)$ 在此闲区间内是有界的，(2) 达到其下确界 $m$ 和上的界 $M$ （外尔什特接斯定理）：（3）在每一个区间 $(a, \beta) \subset[a, b]$ 中，函数具有介于 $f(\alpha)$ 和 $f(\beta)$ 间的一切中介值（哥西定理). 特例, 若 $f(a) \cdot f(\beta)<0$ ，则可找到一个数堆 $\gamma(a<\gamma<$ $\beta)$ ，使得 $\cdot f(\gamma)=0$ 。
662. 已给连续函数 $y=f(x)$ 的图形. 对于给定点 $a$ 与 给定数 $\varepsilon>0$ ，用几何方法表示出这样的数 $\delta>0$ ，使当 $\mid x-a!$
$<\delta$ 时, $|f(x)-f(a)|$
$<\varepsilon$.
解 如图 1.262
所示，如果 $\delta_{1}<\delta_{3}$ ，我们只要取

$$
\delta=\min \left(\delta_{1}, \delta_{2}\right),
$$

即有

$$
\delta=\delta_{1}
$$

于是,当 $|x-a|<\delta$ 时,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-383.jpg?height=532&width=743&top_left_y=568&top_left_x=1068)

$$
|f(x)-f(a)|<\varepsilon_{.}
$$

663. 要做一个金属的边长 $x_{0}=$

图 1.262
10 厘米的正方形薄片。若要其面积 $y=x^{2}$ 与预计的 $y_{0}=$ 100 平方厘米的差不超过（a）土 1 平方厘米；（6）土0.1平
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-383.jpg?height=75&width=1463&top_left_y=1459&top_left_x=354) $x$ 可以在什么范围内变更？
神 （a）要 $\left|x^{2}-100\right|<1$ ，只要

$$
99<x^{2}<101
$$

解之，得

$$
9.95<x<10.05
$$

(5) 要 $\left|x^{2}-100\right|<0.1$ ，只要

$$
\sqrt{100-0.1}<x<\sqrt{100+0.1}
$$

解之，得

$$
9.995<x<10.005 .
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-383.jpg?height=181&width=1121&top_left_y=2302&top_left_x=476)
解之，得

$$
\begin{aligned}
& 9.9995<x<10.0005 . \\
& \text { (г) 要 }\left|x^{2}-100\right|<\varepsilon \text {,只要 } \\
& \sqrt{100-\varepsilon}<x<\sqrt{100+\varepsilon .} .
\end{aligned}
$$

*）本来， $x$ 处应记成 $|x|$ ，在此仅考虑点 $x=10$ 处，故在其近傍 $x$ 值佰为正，因此，不必取绝对值了。
664. 立方体的边是在 2 米和 3 米之间，为了使计算这立方体的体积时发生的绝对误差不超过 $\epsilon$ 立方米，设（ a$) \varepsilon=0.1$立方米；（6） $\epsilon=0.01$ 立方米；（в） $\varepsilon=0.001$ 立方米，问測量此立方体的边 $x$ 时可允许有㐌样的绝对误差 $\Delta$ ?
解 要 $\left|x_{1}{ }^{3}-x_{2}{ }^{3}\right|<\mathrm{E}$ ，只要

$$
\left|x_{1}-x_{2}\right|\left(x_{1}^{2}+x_{1} x_{2}+x_{2}^{2}\right)<\varepsilon,
$$

即只要

$$
\left|x_{1}-x_{p}\right|<\frac{\varepsilon}{3 \times 3^{2}}=\frac{\varepsilon}{27},
$$

故有

$$
\begin{aligned}
& \text { (a) } \Delta<\frac{0.1}{27} \text { (米) }=3.7 \text { (豪米); } \\
& \text { (5) } \Delta<\frac{0.01}{27} \text { (米) }=0.37 \text { (毫米); } \\
& \text { (в) } \Delta<\frac{0.01}{27} \text { (米) }=0.037 \text { (毫米). }
\end{aligned}
$$

665. 问在 $x_{6}=100$ 的尽可能多大邻域内, 函数 $y=\sqrt{x}$ 图形的级坐标与 $y_{0}=10$ 之差小于 $\varepsilon=10^{-n}(n \geqslant 0)$ ? 求当 $n=$ $0,1,2,3$ 时这个邻域的大小。
解 要 $|\sqrt{x}-10|<10^{-n}$ ，只要

$$
10\left[1-10^{-(n+1)}\right]<\sqrt{x}<10\left[1+10^{-(n+1)}\right]
$$

即只要
378
$100\left[1-10^{-(x+1)}\right]^{2}<x<100\left[1+10^{-(a+1)}\right]^{2}$,
故得
（a）当 $n=0$ 时， $81<x<121$ ；
（б）当 $n=1$ 时， $98.01<x<102.01$ ；
（в）当 $n=2$ 时， $98.8001<x<100.2001$ ；
(г) 当 $n=3$ 时， $99.980001<x<100.020001$.
666. 利用《 $\varepsilon-\delta$ 论证法, 证明函数 $f(x)=x^{2}$ 当 $x=5$ 时连续。
填下表：

| $\varepsilon$ | 1 | 0.1 | 0.01 | 0.001 | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ |  |  |  |  |  |

证 任合 $\epsilon>0$ ，
要 $\left|x^{2}-25\right|<\varepsilon$ ，即 $|x-5||x+5|<e$,
不妨只就 $x=5$ 的某一邻域来考虑. 例如，取

$$
|x-5|<1 \text { 或 } 4<x<6,
$$

从而有

$$
0<x+5<11
$$

于是，只要

$$
|x-5|<\frac{\varepsilon}{11}
$$

取 $\delta=\min \left(\frac{\varepsilon}{11}, 1\right)$, 则当 $|x-5|<\delta$ 时, 恒有

$$
\left|x^{2}-5\right|<\epsilon,
$$

所以，函数 $y=x^{2}$ 在 $x=5$ 处连续.
填下表：

| $\varepsilon$ | 1 | 0.1 | 0.01 | 0.001 | $\epsilon$ | $\cdots$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\delta$ | 0.09 | 0.009 | 0.0009 | 0.00009 | $\min \left(\frac{\epsilon}{11}, \overline{1}\right)$ | $\cdots$ |

667. 设 $f(x)=\frac{1}{x}$ 和 $\varepsilon=0.001$. 对于数值 $x_{0}=0.1 ; 0.01 ; 0$. $001 ; \cdots$ 求出充分大的正数 $\delta=\delta\left(\dot{\varepsilon}_{1}, x_{0}\right)$ 使得可从不等式 $\left|x-x_{0}\right|<\delta$ 推出不等式

$$
\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon .
$$

可杏对于已知的 $\varepsilon=0.001$ 选出 $\delta>0$ 来，使它对于区间 $(0,1)$ 中的一切 $x_{0}$ 值都适用，换句话说，对于任意的值 $x_{0}$ $\in(0,1)$, 若 $\left|x-x_{0}\right|<\delta$, 则 $f(x)-f\left(x_{0}\right) \mid<\varepsilon ?$
解 $\left|f(x)-f\left(x_{0}\right)\right|=\frac{\left|x-x_{0}\right|}{|x|\left|x_{0}\right|}$.
由于 $\left|x_{0}\right|-|x| \leqslant\left|x-x_{0}\right|$ 或 $|x| \geqslant\left|x_{6}\right|-\left|x-x_{0}\right|$,故有

$$
\left|f(x)-f\left(x_{0}\right)\right| \leqslant \frac{\left|x-x_{0}\right|}{\left|x_{0}\right|^{2}-\left|x_{0}\right|\left|x-x_{\mathrm{c}}\right|}
$$

(在此，我们已假设了 $\left|x-x_{0}\right| \leqslant\left|x_{0}\right|$ ，这一点是可以办到的).

于是要 $\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon$ ，只要

$$
\frac{\left|x-x_{0}\right|}{\left|x_{0}\right|^{2}-\left|x_{0}\right|\left|x-x_{0}\right|}<\varepsilon,
$$

## 即只要

$$
\left|x-x_{\varepsilon}\right|<\frac{\varepsilon x_{0}{ }^{2}}{1+\varepsilon\left|x_{i}\right|} .
$$

取 $\delta=\frac{\varepsilon x_{0}{ }^{2}}{1+\varepsilon\left|x_{0}\right|}>0$, 则当 $\left|x-x_{0}\right|<\delta$ 时, 恒有

$$
\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon .
$$

我们取近似值， $\delta=0.001 x_{0}{ }^{2}(\varepsilon=0.001)$ 。
当 $x 0=0.1$ 时， $\delta=10^{-5}$;
当 $x_{0}=0.01$ 时， $\delta=10^{-7}$ ；
当 $x_{0}=0.001$ 时， $\delta=10^{-9}$ 。
由表达式（1）可知，对于不论怎样小的正数 $\delta$ （固定），则当 $\left|x-x_{0}\right|<\delta$ 及 $x_{0} \rightarrow 0$ 时， $f(x)-f\left(x_{0}\right) \mid$ 可任意地大。因此，无法选出一个公共的正数 $\delta$ 来。
668. 简明的用 $(\epsilon-\delta\rangle$ 的说法在肯定的意义上来表达下面的论断：函数 $f(x)$ 在点 $x_{0}$ 有定义，而在这一点不连续。
解 存在一个 $\varepsilon_{0}>0$ ，对于无论怎样小的 $\delta>0$ ，都有某 $\boldsymbol{x}$ 满足 $\left|\boldsymbol{x}-x_{0}\right|<\delta$ ，但

$$
\left|f(x)-f\left(x_{0}\right)\right| \geqslant \varepsilon_{0} .
$$

669. 设对于某些数 $\varepsilon>0$, 可找到对应的数 $\delta=\delta\left(\varepsilon, x_{0}\right)>0$,使得，只要 $\left|x-x_{0}\right|<\delta$ ，则

$$
\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon .
$$

设：（a）诸数 $\varepsilon$ 形成一有穷的集合；（6）数 $\varepsilon$ 形成分数 $\varepsilon=$ $\frac{1}{2^{n}}(n=1,2, \cdots)$ 的无穷集合。可否断定函数 $f(x)$ 在点 $x_{0}$连续？
楼（a）不能。因为 $\varepsilon$ 不能任意地小。
（Б）可以。事实上，对于任给的 $\varepsilon>0$ ，总可以取充分大的 $n$, 使 $\frac{1}{2^{n}}<\varepsilon$ 。于是, 存在 $\delta>0$, 使当 $\left|x-x_{0}\right|<\delta$ 时,恒有

$$
\left|f(x)-f\left(x_{0}\right)\right|<\frac{1}{2^{n}}<\varepsilon .
$$

## 670. 设已知函数

$$
f(x)=x+0.001[x]
$$

证明对于每一个 $\varepsilon>0.001$, 便可选出 $\delta=\delta(\varepsilon, x)>$ 0 , 使得：只要 $\left|x^{\prime}-x\right|<\delta$ ，则 $\left|f\left(x^{\prime}\right)-f(x)\right|<\varepsilon$ 。而对于 $0<\varepsilon \leqslant 0.001$, 这件事对于一切的值 $x$ 都不行。

在怎样的点这个函数失去了连续性？
证 当 $\varepsilon>0.001$, 且 $\left|x^{\prime}-x\right|<1$ 时,

$$
\begin{aligned}
& \left|f\left(x^{\prime}\right)-f(x)\right|=\mid x-x^{\prime}+0.001\left([x]-\left[x^{\prime}\right] \mid\right. \\
& \quad \leqslant\left|x-x^{\prime}\right|+0.001
\end{aligned}
$$

此时只要取 $\delta=\min \{\varepsilon-0.001,1\}$, 则当 $\left|x-x^{\prime}\right|<\delta$时恒有 $\left|f(x)-f\left(x^{\prime}\right)\right|<\varepsilon$.

当 $0<\varepsilon \leqslant 0.001$, 且 $x_{0}$ 不为整数时, 有整数 $n$, 使得 $n<x_{0}<n+1$ ，只要取

$$
\delta=\min \left(x_{0}-n, n+1-x_{0}, \varepsilon\right)>0,
$$

则当 $\left|x-x_{0}\right|<\delta$ 时, 有 $[x]=\left\{x_{0}\right]$ ，从而

$$
\left|f(x)-f\left(x_{0}\right)\right|=\left|x-x_{0}\right|<\delta \leqslant \varepsilon .
$$

而当 $x_{0}=n$ 为整数时, 则对于无论怎样选取正数 $\delta$, 总有 $\boldsymbol{x}$ 满足

$$
x<x_{0} \text { 及 } x_{0}-x<\delta \text {, }
$$

此时

$$
\left|f(x)-f\left(x_{0}\right)\right|=\left(x_{0}-x\right)+0.001>\varepsilon .
$$

于是，函数 $f(x)$ 在 $x=n$ (整数) 的点失去了连续性。
671. 设对于毎一个充分小的数 $\delta>0$, 都有 $\varepsilon=\varepsilon\left(\delta, x_{0}\right)>0$,使得：只要 $\left|x-x_{0}\right|<\delta$ ，则不等式 $\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon$成立. 从这里是否可得出函数 $f(x)$ 在 $x=x_{0}$ 连续?

由已知的不等式说明了函数 $f(x)$ 的什么性质?
解 不能。因为 $\epsilon$ 是由 $\delta$ 而确定的，它不能任意小。因此，只能说明函数 $f(x)$ 在点 $x_{1}$ 的近傍有界。事实上, $|f(x)|$ $<\left|f\left(x_{0}\right)\right|+\varepsilon$.
672. 设对于每一个数 $\varepsilon>0$, 都有数 $\delta=\delta\left(\varepsilon, x_{0}\right)>0$, 使得: 若 $\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon$, 则 $\left|x-x_{0}\right|<\delta$ 。
从这里是否可得出函数 $f(x)$ 在 $x=x_{0}$ 伡续?由这些不等式说明了函数的什么性质?
解 不对, 若函数 $f(x)$ 在有穷的区间 $(a, b)$ 内有定义,则只要取 $\delta=2(b-a)$ ，不等式 $\left|x-x_{0}\right|<\delta$ 恒成立. 若 $(a, b)$ 为无穷区间，例如，设 $b=+\infty$ ，则必然

$$
\lim _{x \rightarrow+\infty}|f(x)|=+\infty .
$$

事实上, 若不然, 则

$$
\lim _{x \rightarrow+\infty}|f(x)|=c<+\infty
$$

于是, 存在叙列 $x_{n}>a(n=1,2, \cdots), x_{n} \rightarrow+\infty$ 使 $f\left(x_{n}\right)$
$\rightarrow c$. 由此可知数列 $f\left(x_{n}\right)(n=1,2, \cdots)$ 有界, 令

$$
\varepsilon_{0}=\sup \left\{\left|f\left(x_{n}\right)\right|+\left|f\left(x_{0}\right)\right|+1\right\}>0
$$

显然

$$
\left|f\left(x_{n}\right)-f\left(x_{0}\right)\right|<\varepsilon_{6}(n=1,2, \cdots),
$$

但

$$
\lim _{n \rightarrow \infty}\left|x_{n}-x_{0}\right|=+\infty,
$$

故对此 $\varepsilon_{0}>0$, 不存在对应的 $\delta=\delta\left(\varepsilon_{0}, x_{0}\right)>0$, 此与假定矛盾. 由此可知，必有

$$
\lim _{x \rightarrow+\infty}|f(x)|=+\infty
$$

673. 设对于每一个数 $\delta>0$ 及每一个 $x=x_{o}$ ，都有数 $\varepsilon=E(\delta$ ，
$\left.x_{0}\right)>0$, 使得: 若 $\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon$ ，则 $\left|x-x_{0}\right|<\delta$ 。从这里是否应得函数 $f(x)$ 在 $x=x_{0}$ 连续？由已知的不等式说明了函数的什么性质？
解 不能。它只说明了反函数的连续性和单值性。
674. 利用《 $\varepsilon-\delta$ 》 论证法证明下列函数的连续性：(a) $a x+b$; （б) $x^{2}$; (в) $\boldsymbol{x}^{3}$ （г) $\sqrt{x}$; (ㄱ) $\sqrt[3]{x}$; (е) $\sin x$; (ж) $\cos x$; (3) arctg $\operatorname{tg}$.

证 (a) 设 $x_{0} \in(-\infty,+\infty)$.
任给 $\varepsilon>0$, 要 $\left|(a x+b)-\left(a x_{0}+b\right)\right|<\varepsilon$, 只要

$$
\left|x-x_{0}\right|<\frac{\varepsilon}{|a|} \quad(a \neq 0)
$$

取 $\delta=\frac{\varepsilon}{|a|}$, 则当 $\left|x-x_{0}\right|<\delta$ 时, 恒有

$$
\left|(a x+b)-\left(a x_{0}+b\right)\right|<\varepsilon .
$$

由于 $x_{0}$ 的任意性, 所以, $f(x)=a x+b$ 在 $(-\infty,+$ $\infty$ ) 内点点连续.
(5) $\left|x^{2}-x_{0}{ }^{2}\right|=\left|x-x_{0}\right| \cdot\left|x+x_{0}\right| \leqslant\left|x-x_{0}\right|$

- $\left(\left|x-x_{0}\right|+2\left|x_{0}\right|\right)$.

任给 $\varepsilon>0$ ，要 $\left|x^{2}-x_{0}{ }^{2}\right|<\varepsilon$ ，只要

$$
\left|x-x_{0}\right|^{2}+2\left|x_{0}\right|\left|x-x_{0}\right|-\epsilon<0,
$$

即只要 $\left|x-x_{0}\right|<\sqrt{x_{0}^{2}+\varepsilon}-\left|x_{0}\right|$.
取 $\delta=\sqrt{x_{0}{ }^{2}+\varepsilon}-\left|x_{0}\right|>0$, 则当 $\left|x-x_{0}\right|<\delta$ 时,恒有

$$
\left|x^{2}-x_{0}{ }^{2}\right|<\varepsilon .
$$

这就证明了 $f(x)=x^{2}$ 在 $(-\infty,+\infty)$ 内的连续性。
（B）由于 $\left|x^{3}-x_{0}{ }^{3}\right|=\left|x-x_{0}\right|\left|x^{2}+x_{0} x+x_{\mathrm{c}}{ }^{2}\right|$

$$
\leqslant\left|x-x_{0}\right|\left(\left|x^{2}\right|+|x|\left|x_{0}\right|+\left|x_{0}\right|^{2}\right),
$$

不妨设 $\left|x-x_{0}\right|<1$, 则有 $|x|<1+\left|x_{0}\right|$ 及

$$
\left|x^{3}-x_{0}{ }^{3}\right|<\left|x-x_{0}\right|\left(1+3\left|x_{0}\right|+3 x_{3}^{2}\right),
$$

任给 $\varepsilon>0$ ，取 $\delta=\min \left(1 \cdot \frac{\varepsilon}{1+3\left|x_{0}\right|+3 x_{0}^{2}}\right)$ ，则当 $\left|x-x_{\mathrm{c}}\right|<\delta$ 时，但有

$$
\left|x^{3}-x_{0}{ }^{3}\right|<\varepsilon
$$

由于 $x_{0}$ 的任意性，这就证明了 $x^{3}$ 在 $(-\infty,+\infty$ ）内的连续性。
（г）由于 $\left|\sqrt{x}-\sqrt{x_{0}}\right|=\frac{\left|x-x_{0}\right|}{\sqrt{x}+\sqrt{x_{0}}}$
$<\frac{\left|x-x_{0}\right|}{\sqrt{x_{0}}} \quad\left(x_{0}>0\right)$.
任给 $\varepsilon>0$, 取 $\delta=\varepsilon \sqrt{x_{0}}$, 即可得证.
若 $x_{0}=0$,则取 $\delta=\varepsilon^{2}$ 。
(a) 由于

$$
\begin{aligned}
& \left\lvert\, \sqrt[3]{x}-\sqrt[3]{x_{0}}=\frac{\left|x-x_{0}\right|}{\left|x^{\frac{2}{3}}+\left(x x_{0}\right)^{\frac{1}{3}}+x_{0}^{\frac{2}{3}}\right|}\right. \\
& <\frac{\left|x-x_{0}\right|}{\left|\sqrt[3]{x_{0}{ }^{2}}\right|}\left(x_{0} \neq 0, x x_{0}>0\right)
\end{aligned}
$$

取 $\delta=\min \left\{\left|\dot{x_{0}}\right|, \varepsilon \sqrt[3]{x_{0}{ }^{2}}\right\}$ 即可得证.
若 $x_{0}=0$,则取 $\delta=\varepsilon^{3}$ 。
(e) 由于

$$
\left|\sin x-\sin x_{0}\right|=2\left|\sin \frac{x-x_{0}}{2}\right|\left|\cos \frac{x+x_{0}}{2}\right|
$$

$$
\leqslant\left|x-x_{j}\right|,
$$

取 $\delta=\varepsilon$ ，即可得证。
（※）由于

$$
\begin{aligned}
& \left|\cos x-\cos x_{0}\right|=2\left|\sin \frac{x-x_{0}}{2}\right|\left|\sin \frac{x+x_{c}}{2}\right| \\
& \quad \leqslant\left|x-x_{0}\right|
\end{aligned}
$$

取 $\varepsilon=\delta$ ，即可得证。
（3）由 $\left|\operatorname{arctg} x-\operatorname{arctg} x_{0}\right|=\left|\operatorname{arctg} \frac{x-x_{0}}{1+x x_{0}}\right|$,
又因 $|y|<\frac{\pi}{2}$ 时， $|y| \leqslant|\operatorname{tg} y|$ ，

## 故有

$$
\left|\operatorname{arctg} x-\operatorname{arctg} x_{0}\right| \leqslant\left|\frac{x-x_{0}}{1+x x_{0}}\right|
$$

当 $x_{0}>0$ 时,不妨就 $\left|x-x_{0}\right|<\left|x_{0}\right|=x_{0}$ 进行讨论, 此时

$$
\begin{aligned}
&\left|1+x x_{0}\right|>1 \text {, 则 } \\
&\left|\operatorname{arctg} x-\operatorname{arctg} x_{0}\right| \leqslant\left|x-x_{0}\right|
\end{aligned}
$$

当 $x_{0}<0$ 时可同样讨论.
所以，取 $\delta=\min \left(\varepsilon,\left|x_{0}\right|\right)\left(x_{0}=0\right.$ 时，取 $\left.\delta=\varepsilon\right)$ ，
则当 $\left|x-x_{0}\right|<\delta$ 时，恒有
$\left|\operatorname{arctg} x-\operatorname{arctg} x_{0}\right|<\varepsilon$.
由于 $x_{0}$ 的任意性，所以 $\operatorname{arctg} x$ 在（ $-\infty,+\infty$ ）内连续。研究下列函数的连续性并绘出其图形：
675. $\quad f(x)=|x|$.

解 $\quad\left||x|-\left|x_{0}\right|\right| \leqslant\left|x-x_{0}\right|$ ，
取 $\delta=\varepsilon$, 即可证得在任一点的连续性, 如图 1.263所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-393.jpg?height=484&width=695&top_left_y=432&top_left_x=201)

图1.263
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-393.jpg?height=541&width=695&top_left_y=392&top_left_x=1046)

图1.264
676. $f(x)=\left\{\begin{array}{c}\frac{x^{2}-4}{x-2}, \\ \text { A } x \neq 2, \text { 若 } x=2 .\end{array}\right.$

解 $\lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2} \frac{x_{2}-4}{x-2}$

$$
=\lim _{x \rightarrow 2}(x+2)=4
$$

因此，当 $A=4$ 时， $f(x)$ 在点 $x=2$ 处连续；而当 $A \neq 4$时， $f(x)$ 在点 $x=2$ 处不连续。至于在点 $x \neq 2$ 处显然是连续的，并且 $f(x)=x+2(x \neq 2)$ 。

如图1.264所示.
677. 若 $x \neq 1, f(x)$
$=\frac{1}{(1+x)^{2}}$ ，而 $f(-1)$
是任意的。
解 因为

$$
\lim _{x \rightarrow-1} f(x)=+\infty
$$

故函数 $f(x)$ 在点
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-393.jpg?height=552&width=521&top_left_y=1754&top_left_x=1276)

图1.265
$x=-1$ 处不连续。
在点 $x \neq-1$ 处函数 $f(x)$ 显然是连续的.

如图 1.265 所示.
678. (a) 若 $x \neq 0$,

$$
f_{1}(x)=\left|\frac{\sin x}{x}\right| \text {, 而 } f_{1}(0)=1 \text {; }
$$

(6) 若 $x \neq 0$,

$$
f_{2}(x)=\frac{\sin x}{\mid x} \text {, 而 } f_{2}(0)=1
$$

解 (a) 因为 $\lim _{x \rightarrow 1} f_{1}(x)=1=f_{1}(0)$, 故 $f_{1}(x)$ 点点连续.
(6) 因 $\lim _{x \rightarrow+0} f_{2}(x)=1, \lim _{x \rightarrow-0} f_{2}(x)=-1$ ，故 $\lim _{x \rightarrow 0} f_{2}(x)$不存在, 因此 $f_{2}(x)$ 在点 $x=0$ 处不连续, 其余各点均连续。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-394.jpg?height=861&width=1465&top_left_y=1260&top_left_x=244)

图1.266
其中（a）的图形关于 $O y$ 轴对称（图1.266），而（6）的图形关于原点对称（图1.267）。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-395.jpg?height=749&width=1594&top_left_y=399&top_left_x=197)

降1.267
679. 若 $x \neq 0, f(x)=\sin \frac{1}{x}$ ，而 $f(0)$ 是任意的。

解 在 $x \neq 0$ 的点 $f(x)$ 均为连续，而在 $x=0$ 不连续 （因为 $\lim _{x \rightarrow 0} f(x)$ 不存在）。图形关于原点对称，图1.268仅为 $x>0$ 的一部分。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-395.jpg?height=666&width=975&top_left_y=1757&top_left_x=509)

图1.268
680. 若 $x \neq 0, f(x)=x \sin \frac{1}{x}$, 而 $f(0)=0$.

解 $\lim _{x \rightarrow 0} f(x)=$
$f(0)$, 点点连续.
图形关于 $O y$
轴 对称，如图1. 269 所示.

当 $x \rightarrow \infty$ 时,
$y \rightarrow 1$,且当 $|x|>$
$\frac{2}{\pi}$ 时 $0<y<1$.
681. 若 $x \neq 0, f(x)=$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-396.jpg?height=584&width=820&top_left_y=619&top_left_x=915)

图1.269
$e^{-\frac{1}{x^{2}}, \text { 而 } f(0)=0 . ~}$解 $\lim _{x \rightarrow 0} f(x)=0=f(0)$ ，点点连续。

图形关于 $O y$ 轴对称，如图 1.270 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-396.jpg?height=733&width=1103&top_left_y=1621&top_left_x=425)

国 1.270
当 $x \rightarrow \infty$ 时， $y \rightarrow 1$ ，且 $0<y<1$ 。
682. 若 $x \neq 1, f(x)=\frac{1}{1+e^{\frac{x^{2}-1}{x}}}$, 而 $f(1)$ 是任意的.

解 $\lim _{x \rightarrow-1} f(x)=1, \lim _{x+1+0} f(x)=0$,
除点 $x=1$ 外其余点点连续.
$\lim _{x \rightarrow \infty} f(x)=\frac{1}{2}$. 如图 1.271 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-397.jpg?height=487&width=740&top_left_y=933&top_left_x=224)

图 1.27 .1
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-397.jpg?height=555&width=615&top_left_y=890&top_left_x=1069)

医 1.272
683. 若 $x \neq 0, f(x)=x \ln x^{2}$, 而 $f(0)=a$.

解 $\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} x \ln x^{2}=0$
当 $a=0$ 时,点点连续;而当 $a \neq 0$ 时,除点 $x=0$ 处
不连续, 其余点点连续. 图形关于原点对称, 如图 1.272所示。
684. $f(x)=\operatorname{sgn} x$.

解 当 $x<0$ 时, $f(x)=-1$;
当 $x>0$, 时, $f(x)=1$ ；
当 $x=0$ 时, $f(x)=0$.
除点 0 外, 点点连续.
如图1.273所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-397.jpg?height=435&width=612&top_left_y=1916&top_left_x=1185)

图1.273
685. $f(x)=[x]$.

解 除当 $x=k(k$ 为整
数）外，其余点点连续。
如图1.274 所示.
686. $f(x)=\sqrt{x}-[\sqrt{x}]$.

解 当 $x=k^{2}(k=1$ ，
$2, \cdots$ ）时不连续. 当 $k^{2}$
$\leqslant x<(k+1)^{2}$ 时,
$f(x)=\sqrt{x}-k . f[(k-$
$\left.1)^{2}\right]=0$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-398.jpg?height=592&width=767&top_left_y=432&top_left_x=1067)

图1.274

如图 1.275 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-398.jpg?height=575&width=1118&top_left_y=1277&top_left_x=389)

图 1.275
求出下列函数的不连续点，并研究这些点的性质：
$687 . y=\frac{x}{(1+x)^{2}}$.
解 $x=-1$ 为无穷型不连续点。
$688 . y=\frac{1+x}{1+x^{3}}$.
解 因 $\lim _{x \rightarrow-1} \frac{1+x}{1+x^{3}}=\lim _{x \rightarrow-1} \frac{1}{x^{2}-x+1}=\frac{1}{3}$ ，

故 $x=-1$ 为"可移去"的不连续点，
689. $y=\frac{x^{2}-1}{x^{3}-3 x+2}$.

解

$$
\frac{x^{2}-1}{x^{3}-3 x+2}=\frac{(x-1)(x+1)}{(x-1)^{2}(x+2)}
$$

$x=1$ 及 $x=-2$ 均为无穷型不连续点。
690. $y=\frac{\frac{1}{x}-\frac{1}{x}+\frac{1}{1}}{\frac{1}{x-1}-\frac{1}{x}}$.

解 因为 $\lim _{x \rightarrow-1} y=\infty, \lim _{x \rightarrow 0} y=-1$ ， 及 $\lim _{x \rightarrow 1} y=0$ ，
所以， $x=-1$ 为无穷型不连续点，而 $x=0$ 及 $x=1$ 为 "可移去"的不连续点。
$691 . y=\frac{x}{\sin x}$.
解 因 $\lim _{x \rightarrow 0} y=1$ 及 $\lim _{x \rightarrow k^{*}} y=\infty$ （ $k$ 为不等于零的整数），
所以， $x=0$ 为"可移去"的不连续点，而 $x=k \pi(~ c= \pm 1$ ， $\pm 2, \cdots$ ) 为无穷型不连续点.
$692 . y=\sqrt{\frac{1-\cos \pi x}{4-x^{2}}}$.
角 $\lim _{x \rightarrow 2} y=\lim _{x \rightarrow 2} \sqrt{\frac{2 \pi \sin ^{2} \frac{\pi}{2}(2-x)}{\frac{\pi}{2}(2-x) \cdot 2(2+x)}}=0$.
同理， $\lim _{x \rightarrow-2} y=0$ ，
所以， $x=2$ 及 $x=-2$ 为"可移去"的不连续点。
693. $y=\cos ^{2} \frac{1}{x}$.

解 因 $\lim _{x \rightarrow 0} y$ 不存在，" 故 $x=0$ 为第二类不连续点.

* ) 左右极限均不存在.

694. $y=\operatorname{sgn}\left(\sin \frac{\pi}{x}\right)$.

解 $x=0$ 为第二类不连续点.
因为 $\lim y=(-1)^{k}, \lim y=(-1)^{k-1}$, 故 $x=\frac{1}{k}$

$$
\quad(k= \pm 1, \pm 2, \cdots)
$$

为第一类不连续点。
695. $y=\frac{\cos \frac{\pi}{x}}{\cos \frac{\pi}{x}}$.

解 $x=\frac{2}{2 k+1}(k=0, \pm 1, \pm 2, \cdots)$ 为"可移去"的不连续点。
696. $y=\operatorname{arctg} \frac{1}{x}$.

晖 因 $\lim _{x \rightarrow+\infty} \operatorname{arctg} \frac{1}{x}=\frac{\pi}{2}, \operatorname{limarc}^{2} \operatorname{tg} \frac{1}{x}=-\frac{\pi}{2}$,

$$
\text { 故 } x=0 \text { 为第一类不连续点. }
$$

697. $y=\sqrt{x} \operatorname{arctg} \frac{1}{x}$.

解 $\lim _{x \rightarrow 0} y=0, x=0$ 为"可移去"的不连续点.
698. $y=e^{x+\frac{3}{2}}$.

解 因为 $\lim _{x \rightarrow+0} y=+\infty, \lim _{x \rightarrow-0} y=0$ ，
所以， $x=0$ 为第二类不连续点。
$699 . y=\frac{1}{\ln x}$.
解 因为 $\lim _{x \rightarrow 0} y=0, \lim _{x \rightarrow 1-0} y=-\infty, \lim _{x \rightarrow 1+p} y=+\infty$ ，
所以， $x=0$ 为"可移去"的不连续点，而 $x=1$ 为无

穷型不连续点,
$700^{+} y=\frac{1}{1-e^{\frac{x}{1-x}}}$.
解 因为 $\lim _{x \rightarrow 1+0} y=1, \lim _{x \rightarrow 1-0} y=0, \lim _{x \rightarrow+0} y=-\infty$ ， $\lim _{x \rightarrow-0} y=+\infty$ ，所以 $x=1$ 为第一类不连续点，而 $x=0$ ，为无穷型不连续点。
研究下列㖤数的连续
性并绘出其大略图形。
701. $y=\operatorname{sgn}(\sin x)$ 。

解 $x=k \pi(k=0$,
$\pm 1, \pm 2, \cdots)$ 。
图1.276
为第一类不连续点。
如图1.276所示。
702. $y=x-〔 x 〕$.

解 $x=k(k=0, \pm 1$ ，
$\pm 2, \cdots$ )
为第一类不连续点。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-401.jpg?height=384&width=680&top_left_y=1344&top_left_x=1125)

图1.277
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-401.jpg?height=581&width=741&top_left_y=1834&top_left_x=1137)

图1.278
，土 $1, \pm 2, \cdots$ ）时 $y=0$ 。

如图1.279所示.
705. $y=x^{2}-\left[x^{2}\right]$.

䉽 $x= \pm \sqrt{k}(k=$
$1,2, \cdots)$ 为第一类不连
续点。
如图1.280所示.
706. $y=\left[\frac{1}{x}\right]$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-402.jpg?height=501&width=732&top_left_y=386&top_left_x=1047)

图 1.279
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-402.jpg?height=447&width=695&top_left_y=1093&top_left_x=1069)

图 1.280.

了 $x>0$ 的部分，
并且在图形中两轴比例不一致，即 已经过"压缩"变换。 707. $y=x\left[\frac{1}{x}\right]$.

解 $x=0$ 为"可移去"的不连续点，因为 $\lim _{x \rightarrow 0} y=1$ 。

$$
x=\frac{1}{k}(k= \pm
$$

$1, \pm 2, \cdots)$ 为第一类不连续点。

图1.282仅画了
当 $x>0$ 的部分，并且
两轴所 取的单位不一
致。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-402.jpg?height=506&width=720&top_left_y=1957&top_left_x=1082)

图1.281
708. $y=\operatorname{sgn}\left(\cos \frac{1}{x}\right)$.

解 $x=0$ 为第二 类不连续点。

凡使 $\cos \frac{1}{x}=0$ 的
点, 即 $x=\frac{2}{(2 k-1) \pi}$
$(k=0, \pm 1, \pm 2, \cdots)$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-403.jpg?height=577&width=906&top_left_y=451&top_left_x=1015)

为第一类不连续点。
图1.283仅画了
当 $k=0, \pm 1, \pm 2$ 时
的情形，图形关于 $O y$
轴对称。
709. $y=\left[\frac{1}{x^{2}}\right] \operatorname{sgn}\left(\sin \frac{\pi}{x}\right)$.

解 $x=0$ 为第二类不
连续点。

$$
\begin{aligned}
& x= \pm \frac{1}{k} \quad \text { 及 } x= \\
& \pm \frac{1}{\sqrt{k}}(k=1,2 \cdots)
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-403.jpg?height=766&width=670&top_left_y=1113&top_left_x=1204)

图1.283

为第一类不连续点。
图1.284仅画了 $x>0$ 时的一部分、又两轴所取的比例单位不同。
710. $y=\operatorname{ctg} \frac{\pi}{x}$ 。

解 凡使 $\sin \frac{\pi}{x}=0$ ，即

$$
x=\frac{1}{k}(k= \pm 1, \pm 2, \cdots)
$$

为无穷型不连续点. $x=0$ 为第二类不连续点.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-404.jpg?height=1597&width=1338&top_left_y=721&top_left_x=276)

图 1.284
图形关于原点对称，如图1.285所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-405.jpg?height=575&width=884&top_left_y=346&top_left_x=529)

图1.285
当 $x \rightarrow-\infty$ 时, $y \rightarrow-\infty$ ；
当 $x \rightarrow+\infty$ 时, $y \rightarrow+\infty$.
711. $y=\sec ^{2} \frac{1}{x}$.

解 $x=\frac{2}{(2 k+1) \pi}(k=0, \pm 1, \pm 2, \cdots)$ 为无穷型不连续点。
$x=0$ 为第二类不连续点。
图形关于 $O y$ 轴对称，当 $x \rightarrow+\infty$ 时， $y \rightarrow 1$ 。
如图1.286所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-405.jpg?height=575&width=881&top_left_y=1894&top_left_x=639)

图1.286
712. $y=(-1)^{\left[x^{2}\right)}$.

解 $x= \pm \sqrt{n}(n=1,2, \cdots)$ 为第一类不连续点。
图形关于 $O y$ 轴对
称。
$\lim _{x \rightarrow{ }_{\sqrt{n}}} y=(-1)^{n-1}$,
$\lim _{\sqrt{x}+0^{2}} y=(-1)^{x}$.
如图1.287所示。
713. $y=\operatorname{arctg}\left(\frac{1}{x}+\frac{1}{x-1}\right.$
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-406.jpg?height=467&width=847&top_left_y=589&top_left_x=930)

图 1.287
$\left.+\frac{1}{x-2}\right)$.
解 $x=0, x=1$ 和 $x=2$ 为第一类不连续点。

$$
\lim _{x \rightarrow-0} y=-\frac{\pi}{2}, \lim _{x \rightarrow 1-0} y=-\frac{\pi}{2},
$$

$$
\lim _{x \rightarrow 2-0} y=-\frac{\pi}{2}, \lim _{x \rightarrow+0} y=\frac{\pi}{2},
$$

$\lim _{x \rightarrow 1+0} y=\frac{\pi}{2}, \lim _{x \rightarrow 2+\infty} y=\frac{\pi}{2}$,
$\lim _{x \rightarrow+\infty} y=0, \lim _{x \rightarrow-\infty} y=0$.
如图 1.288 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-406.jpg?height=515&width=1040&top_left_y=1967&top_left_x=465)

图 1.288
714. $y=\frac{1}{x^{2} \sin ^{2} x .}$

解 $x=k \pi(k=0$,
$\pm 1, \pm 2, \cdots$ ）为无
穷型不连续点。
图形关于 $O y$ 轴对
称，如图1.289所
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-407.jpg?height=415&width=927&top_left_y=375&top_left_x=910)

示。
715. $y=\frac{1}{\sin \left(x^{2}\right)}$.

解 $x= \pm \sqrt{k \pi}(k=$
$0,1,2, \cdots)$ 为无穷型
不连续点。
图形关于 $O y$ 轴对
称，如图1.290所示。
图中只画了 $x>0$ 的一部分。
716. $y=\ln \frac{x^{2}}{(x+1)(x-3)}$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-407.jpg?height=686&width=750&top_left_y=959&top_left_x=1055)

图 1.289

图 1.290
解 $x=-1$ 和 $x=3$ 为无穷型不连续点。
定义域为 $x<-1$ 或 $x>3$ 。
当 $x<\frac{-3}{2}$ 时, $0<\frac{x^{2}}{x^{2}-2 x-3}<1$, 故

$$
\ln \frac{1}{(x+1)(x-3)}<0
$$

当 $x>\frac{-3}{2}$ 时,
$\frac{x^{2}}{x^{2}-2 x-3}>1$
故 $\ln \frac{1}{(x+1)(x-3)}$
$>0$.

$$
\text { 当 } x \rightarrow \infty \text { 时, } y \rightarrow 0 \text {. }
$$

如图1.291所示。
717. $y=e^{-\frac{1}{x}}$.

解 $x=0$ 为第二
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-408.jpg?height=707&width=809&top_left_y=252&top_left_x=1000)

图 1.291

类不连续点。
$\lim _{x \rightarrow \infty} y=1, \lim _{x \rightarrow+\infty} y=0, \lim _{x \rightarrow-\cdots} y=+\infty$.
如图1.292 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-408.jpg?height=612&width=878&top_left_y=1302&top_left_x=572)

图 1.292 。
718. $y=1-e^{-\frac{1}{x^{2}}}$.

解 因 $\lim _{x \rightarrow 0} y=1$ ，
故 $x=0$ 为"可移去"
的不连续点。
图形关于 $O y$ 轴对
称，如图1.293所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-408.jpg?height=457&width=714&top_left_y=2013&top_left_x=1025)

图 1.293
719. $y=\mathrm{th} \frac{2 x}{1-x^{2}}$.

解 $x= \pm 1$ 为第
一类不连续点。
$\lim _{x \rightarrow 1-0} y=1$ ，
$\lim _{x \rightarrow 1+0} y=-1$.
图形关于原点对称，
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-409.jpg?height=550&width=929&top_left_y=296&top_left_x=940)

图1.294

如图1.294所示。
研究下列函数的连续珄并作出其图形：
720. $y=\lim _{n \rightarrow \infty} \frac{1}{1+x^{n}}(x \geqslant 0)$.
$\begin{cases}1, & \text { 当 } 0 \leqslant x<1\end{cases}$
解 $y= \begin{cases}0, & \text { 当 } x>1 ; \\ \frac{1}{2}, & \text { 当 } x=1 .\end{cases}$
$x=1$ 为第一类不连续点。
如图1.295所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-409.jpg?height=458&width=692&top_left_y=1824&top_left_x=314)

图1.295
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-409.jpg?height=586&width=778&top_left_y=1697&top_left_x=1050)

图 1.296
$721 . y=\lim _{n \rightarrow \mathrm{x}, n^{x}+n^{-x}} \frac{n^{x}-n^{-x}}{n^{-1}}$.
会 $y= \begin{cases}1, & \text { 当 } x>0 ; \\ 0, & \text { 当 } x=0 ; \\ -1, & \text { 当 } x<0,\end{cases}$
即 $y=\operatorname{sgn} x$.
$x=0$ 为第一类不连续点，如图1.296所示。
722. $y=\lim _{n \rightarrow \infty} \sqrt[x]{1+x^{2 n}}$.

## 解

$y= \begin{cases}1, & \text { 当 }|x| \leqslant 1 ; \\ x^{2}, & \text { 当 }|x|>1 .\end{cases}$
处处连续，如图1.297所示。
723. $y=\lim _{x \rightarrow \infty} \cos ^{2 n} x$.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-410.jpg?height=558&width=849&top_left_y=932&top_left_x=975)

異1.297
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-410.jpg?height=406&width=869&top_left_y=1619&top_left_x=956)

图 I. 298
724. $y=\lim _{x \rightarrow \infty} \frac{x}{1+(2 \sin x)^{2 n}}$.

整 $y= \begin{cases}x, & \text { 粦 }|x-k \pi|<\frac{\pi}{6} ; \\ \frac{x}{2}, & \text { 当 } x=k \pi \pm \frac{\pi}{6} ; \\ 0, & \text { 当 } \frac{\pi}{6}<|x-k \pi|<\frac{5 \pi}{6} .\end{cases}$
$(k=0, \pm 1, \pm 2, \cdots)$
$x=k \pi \pm \frac{\pi}{6}$ 为第一类不连续点。
如图1.299所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-411.jpg?height=518&width=909&top_left_y=1106&top_left_x=436)

图1.299
725. $y=\lim _{n \rightarrow \infty}[\operatorname{xarctg}(n \operatorname{ctg} x)]$.

解 $y= \begin{cases}\frac{\pi}{2} x, & \text { 当 } k \pi<x<k \pi+\frac{\pi}{2} ; \\ -\frac{\pi}{2} x, & \text { 当 } k \pi+\frac{\pi}{2}<x<k \pi+\pi ; \\ 0, & \text { 当 } x=k \pi+\frac{\pi}{2} .\end{cases}$
（ $k=0, \pm 1, \pm 2, \cdots)$
$x=\frac{k \pi}{2}(k \neq 0)$ 为第一类不连续点, 如图 1.300 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-412.jpg?height=593&width=818&top_left_y=366&top_left_x=493)

图1.300
726. $y=\lim _{n \rightarrow \infty} \frac{x+x^{2} e^{x x}}{1+e^{x *}}$.

解 $y= \begin{cases}x, & \text { 当 } x \leqslant 0 ; \\ x^{2}, & \text { 当 }>0 .\end{cases}$
处处连续, 如图 1. 301 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-412.jpg?height=529&width=526&top_left_y=1420&top_left_x=314)

图1.301
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-412.jpg?height=432&width=749&top_left_y=1549&top_left_x=1030)

图1.302
727. $y=\lim _{t \rightarrow+\infty} \frac{\ln \left(1+e^{\pi}\right)}{\ln \left(1+e^{e}\right)}$.

解 $y= \begin{cases}0, & \text { 当 } x \leqslant 0 ; \\ x, & \text { 当 } x>0 .\end{cases}$
处处连续，如图 1.302 所示.
728. $y=\lim _{x \rightarrow+\infty}(1+x)$ th $t x$.

## 解

$y=\left\{\begin{array}{l}-(1+x), \text { 当 } x<0 ; \\ 0, \quad \text { 当 } x-0 ; \\ 1+x, \quad \text { 当 } x>0 .\end{array}\right.$
$x=0$ 为第一类不连续点。
如图 1.303 所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-413.jpg?height=569&width=820&top_left_y=889&top_left_x=207)

图1.303
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-413.jpg?height=483&width=507&top_left_y=912&top_left_x=1163)

图1.304

## 729. 函数

$$
f(x)=\left\{\begin{array}{l}
2 x, \text { 若 } 0 \leqslant x \leqslant 1 ; \\
2-x, \text { 若 } 1<x \leqslant 2 .
\end{array}\right.
$$

是杏为连续函数？
解 $x=1$ 为第一类不连续点, 在 $[0,2]$ 上 $f(x)$ 不是连续函数.
如图1.304所示。
730. 设：
$f(x)=\left\{\begin{array}{l}e^{x}, \text { 若 } x<0 ; \\ a+x, \text { 若 } x \geqslant 0 .\end{array}\right.$
当怎样选择数 $a$ ，函数 $f(x)$ 方为连续的？
解 因 $\lim _{x \rightarrow 0} f(x)=a$ 及 $\lim _{x \rightarrow-0} f(x)=1$ ，
而 $f(0)=a$ ，故当 $a=1$ 时，

$$
\lim _{x \rightarrow 0} f(x)=f(0)
$$

此即说明函数 $f(x)$ 在 $x=0$ 处连续；至于当 $x \neq 0$ 时， $f$ （ $x$ ）显然连续。

于是，我们选择数 $a=1$ ，则函数 $f(x)$ 在整个数轴上为连续的，如图1,305所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-414.jpg?height=561&width=800&top_left_y=833&top_left_x=431)

图 1.305
731. 研究下列函数的连续性并说明不连续点的性质，设：
(a) $f(x)=\left\{\begin{array}{l}x^{2}, \text { 当 } 0 \leqslant x \leqslant 1, \\ 2-x, \text { 当 } 1<x \leqslant 2 ;\end{array}\right.$
（6） $f(x)=\left\{\begin{array}{l}x, \text { 当 }|x| \leqslant 1, \\ 1, \text { 当 }|x|>1 ;\end{array}\right.$
(в) $f(x)=\left\{\begin{array}{l}\cos \frac{\pi x}{2}, \text { 当 }|x| \leqslant 1, \\ |x-1|, \text { 当 }|x|>1 ;\end{array}\right.$
（г） $f(x)=\left\{\begin{array}{l}\operatorname{ctg}^{2} \pi x, \text { 当 } x \text { 为非整数； } \\ 0, \text { 当 } x \text { 为整数； }\end{array}\right.$
（ㄱ） $f(x)=\left\{\begin{array}{l}\sin \pi x, \text { 当 } x \text { 为有理数， } \\ 0, \text { 当 } x \text { 为无理数. }\end{array}\right.$
解 (a)连续函数。
（6） $x=-1$ 为第一类不连续点。
(в) $x=-1$ 为第一类不连续点。
（ $\Gamma$ ） $x=k(k=0, \pm 1, \pm 2, \cdots)$ 为无穷型不连续点。
（ $) x \neq k(k=0, \pm 1, \pm 2, \cdots)$ 为第二类不生续点。
732. 函数 $d=d(x)$ 是数轴 $O x$ 上的点 $x$ 与由线 $0 \leqslant x \leqslant 1$ 及 2 $\leqslant x \leqslant 3$ 所构成点集间的最短距离. 求函数 $d$ 的解析表示式，作出其恩形并研究其连续性。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-415.jpg?height=458&width=847&top_left_y=930&top_left_x=593)

图 1.306
解

$$
d=\left\{\begin{array}{l}
-x,-\infty<x<0 \\
0,0 \leqslant x \leqslant 1 ; \\
x-1,1<x \leqslant \frac{3}{2} \\
2-x, \frac{3}{2}<x<2 \\
0,2 \leqslant x \leqslant 3 ; \\
x-3,3<x<+\infty
\end{array}\right.
$$

处处连续，如图 1.306 所示。
733. 图形 $E$ 是由高为 1 底为 1 的等腰三角形及底为 1 高为 2及 3 的二矩形所构成（图 1.307）。函数 $S=S(y)(0 \leqslant y<$ $+\infty)$ 是图形 $E$ 介于平行线 $Y=0$ 及 $Y=y$ 之间的那一部分面积；而函数 $b=b(y)(0 \leqslant y<+\infty)$ 是用平行线 $Y=y$

去截图形所得截痕之长. 求函数 $S$ 及 $b$ 的解析表示式，作出它们的图形并研究其连续性。
解

$$
S=\left\{\begin{array}{l}
3 y-\frac{y^{2}}{2}, \text { 当 } 0 \leqslant y \leqslant 1 ; \\
\frac{1}{2}+2 y, \text { 当 } 1<y \leqslant 2 ; \\
\frac{5}{2}+y, \text { 当 } 2<y \leqslant 3 ; \\
\frac{11}{2}, \text { 当 } 3<y<+\infty .
\end{array}\right.
$$

处处连续，如图 1. 308 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-416.jpg?height=590&width=750&top_left_y=1324&top_left_x=316)

图1.307
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-416.jpg?height=638&width=718&top_left_y=1326&top_left_x=1109)

图1.308

对于函数 $b=b(y)$ 根据假设，则有如下解析表示式：
$b=\left\{\begin{array}{l}3-y, \text { 当 } 0 \leqslant y \leqslant 1 ; \\ 2, \text { 当 } 1<y \leqslant 2 ; \\ 1, \text { 当 } 2<y \leqslant 3 ; \\ 0, \text { 当 } 3<y<+\infty .\end{array}\right.$
$y=2$ 及 $y=3$ 为第一类不连续点，如图1. 309 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-417.jpg?height=589&width=698&top_left_y=445&top_left_x=613)

图1.309
734. 证明迪里黑里函数

$$
\chi(x)=\lim _{m \rightarrow \infty}\left\{\lim _{\| \rightarrow \infty} \cos ^{n}(\pi m!x)\right\}
$$

当 $x$ 取任一值时都是不连续的。
证 记 $f(m, n)=\cos ^{n}(\pi m \mid x)$ 。
当 $x$ 为有理数时，总可认为 $m>p$ ，其中 $x=\frac{q}{p}(p, q$为互质的整数)，于是 $f(m, n)=1$ ，教此时

$$
\chi(x)=1
$$

当 $x$ 为无理数时，则对任一固定的 $m$ 而言，
$|\cos (\pi m \mid x)|<1$, 从而

$$
\lim _{n \rightarrow \infty} \cos ^{n}(\pi m \mid x)=0,
$$

故此时 $\chi(x)=0$.总之，
$\chi(x)=\left\{\begin{array}{l}1, \text { 当 } x \text { 为有理数时， } \\ 0, \text { 当 } x \text { 为无理数时， }\end{array}\right.$
由实数的稠密性可知；对于 $x$ 的任意值在其任一邻域内均含有无限个有理数和宏理数，因而 $\chi(x)$ 的值总在

1 和 0 这两数中取一个. 这样， $\chi(x)$ 的极限就不存在. 于是，当 $x$ 取任一值时， $\chi(x)$ 都是不连续的。
735. 设有函数

$$
f(x)=x \cdot \chi(x),
$$

式中 $\chi(x)$ 为迪里黑里函数（参阅上例），研究此函数 $f$ （ $x$ ）的连续性。作出这函数的略图。

解

$$
x \cdot \chi(x)=\left\{\begin{array}{l}
x, \text { 当 } x \text { 为有理数时: } \\
0, \text { 当 } x \text { 为无理数及 } 0 \text { 时, }
\end{array}\right.
$$

因此，
$\lim _{x \rightarrow 0} x \cdot \chi(x)=0$ 等于在 $x=0$ 处的函数值，故当 $x$ 文 0 时， $x \cdot \chi(x)$ 不连续，而当 $x=0$ 时， $x \cdot \chi(x)$ 连续，姻图 1.310 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-418.jpg?height=627&width=878&top_left_y=1434&top_left_x=609)

图1.310
736. 证明黎晏函数
$f(x)=\left\{\begin{array}{l}\frac{1}{n}, \text { 若 } x=\frac{m}{n}, \text { 其中 } m \text { 和 } n \text { 为互质的整数, } \\ 0, \text { 若 } x \text { 为无理数。 }\end{array}\right.$
当 $x$ 取任一个有理值时是不连续的，而当 $x$ 取任一个无理值时是连续的。作出这个通数的路图。

证 不失一般性，我们仅就区间 $[0,1]$ 讨论，图1.311为 $f(x)$ 在 $x \in[0,2]$ 时的略图。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-419.jpg?height=638&width=881&top_left_y=595&top_left_x=639)

图 1.311
对于任意的 $x_{0} \in[0,1]$ 来说，若任取 $\varepsilon>0$ ，则满足不等式 $n<\frac{1}{\boldsymbol{\varepsilon}}$ 的自然数 $n$ 至多只有有限个，即在 $[0,1]$ 中至多只有有限个有理数 $\frac{m}{n}$ ，使得 $f\left(\frac{m}{n}\right)=\frac{1}{n} \geqslant \varepsilon$ 。因而我们可以取 $\delta>0$ ，使得 $x_{0}$ 的邻域 $\left(x_{0}-\delta, x_{0}+\delta\right)$ 内不含有这样的有理数（若 $x_{0}$ 为有理数，则可能除去 $x_{0}$ ）。于是，只要 $0<\left|x-x_{0}\right|<\delta$ ，不论 $x$ 是否为有理数，都成立 $|f(x)|<$ $\varepsilon$. 即证明了对于 $[0,1]$ 中任意点 $x_{0}$ ，都成立

$$
f\left(x_{0}+0\right)=f\left(x_{0}-0\right)=0 .
$$

若 $x_{0}$ 为无理数，则 $f\left(x_{0}\right)=0$ ，可见 $f(x)$ 在 $x_{0}$ 连续；若 $x_{0}$ 是有理数，则 $f\left(x_{0}\right) \neq 0$ ，函数 $f(x)$ 在 $x_{0}$ 点有可移间断。
737. 若 $x$ 是既约有理分数 $\frac{m}{n}(n \geqslant 1)$ 时, $f(x)=\frac{n x}{n+1}$; 若 $x$ 是无理数时， $f(x)=|x|$ 。

试研究函数 $f(x)$ 的连续性并作出此函数的略图。证 当 $x<0$ 时， $f(x)$ 泉然不连续，而对于正有理数 $\xi=$ $\frac{m}{n}, f(\xi)=\frac{m}{n+1}$. 若我们取一列无理数 $x_{k}$ 趋于 $\xi$, 则 $\lim _{x_{k} \rightarrow \ell} f$ $\left(x_{k}\right)=\frac{m}{n} \neq \frac{m}{n+1}$ ，故 $f(x)$ 在正有理数点也不连续。当 $\xi$为正无理数时，由于对任意的 $\varepsilon>0$ ，满足 $\frac{1}{q}>\varepsilon$ 的自然数 $q$ 至多只有有限个. 与 736 题类似可证 $f(x)$ 在点 $x=\xi$连续. 如图 1.312 所示.
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-420.jpg?height=606&width=784&top_left_y=1153&top_left_x=579)

图 1.312
738. 函数 $f(x)=\frac{1-\cos x}{x^{2}}$ 除 $x=0$ 外，对于自变数 $x$ 的一切值都有定义。为了使此函数当 $x=0$ 是连续的, 则在 $x=0$这一点应当以甚公数值作为函数的值?
㬴 因为

$$
\lim _{x \rightarrow 0} \frac{1-\cos x}{x^{2}}=\frac{1}{2}
$$

所以，应取 $f(0)=\frac{1}{2}$ ，那么， $f(x)$ 当 $x=0$ 时是连缕的。
739. 证明不管复样选取数 $f(1)$, 函数 $f(x)=\frac{1}{1-x}$ 在 $x=1$ 是不连续的。
证 因为 $\lim _{x \rightarrow i+0} f(x)=-\infty, \lim _{z \rightarrow 1-0} f(x)=+\infty$ ，所以，我们无法选择 $f(1)$ 使之成为连续的.
740. 当 $x=0$ 时,函数 $f(x)$ 失去意义, 定义 $f(0)$ 的数值, 使得 $f(x)$ 在点 $x=0$ 连续, 若:
(a) $f(x)=\frac{\sqrt{1+x}-1}{\sqrt[3]{1+x}-1}$;
(6) $f(x)=\frac{\operatorname{tg} 2 x}{x} ;$
(B) $f(x)=\sin x \sin \frac{1}{x} ; \quad$ (5) $f(x)=(1+x)^{\frac{1}{x}} ;$
(a) $f(x)=\frac{1}{x^{2}}-\frac{1}{x^{2}} ; \quad$ (e) $f(x)=x^{x}(x>0)$;
(ж) $f(x)=x \ln ^{2} x$.
(1) $\lim _{x \rightarrow 0} \frac{\sqrt{1+x}-1}{\sqrt[3]{1+x}-1}$

$$
=\lim _{x \rightarrow 0} \frac{x\left(\sqrt[3]{(1+x)^{2}}+\sqrt[3]{1+x}+1\right)}{x(\sqrt{1+x}+1)}=\frac{3}{2},
$$

取 $f(0)=\frac{3}{2}$ 即行.
(6) $f(0)=2$.
(B) 因为 $\lim _{x \rightarrow 0} \sin x \sin \frac{1}{x}=0$, 故取 $f(0)=0$.
(r) 因为 $\lim _{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$ ，故取 $f(0)=e$.
(д) 因为 $\lim _{x \rightarrow 0} \frac{1}{x^{2}} e^{-\frac{1}{x^{2}}}=0$ ，故取 $f(0)=0$ 。
(e) 因为 $\lim _{x \rightarrow 0} x^{x}=1$ ，故取 $f(0)=1$ 。
（ऊ）因为 $\lim _{x \rightarrow 0} x \ln ^{2} x=0$ ，故取 $f(0)=0$ 。
741. 设：（a）函数 $f(x)$ 当 $x=x_{0}$ 时是连续的，而函数 $g(x)$ 当 $x$ $=x_{0}$ 时是不连续的；（ 6 ）当 $x=x_{0}$ 时函数 $f(x)$ 和 $g(x)=$者都是不连续的，则此二函数的和 $f(x)+g(x)$ 在已的点 $x_{0}$ 是否必为不连续的？举出适当的例子。
解 (a) $f(x)+g(x)$ 必为不连续的. 事实上，
设 $\quad F(x)=f(x)+g(x)$
对于函数 $F(x)-f(x)=g(x)$ ，如果 $F(x)$ 在 $x_{0}$ 连续，则有 $\lim _{x \rightarrow \mathrm{x}_{0}} g(x)=\lim _{x \rightarrow x_{0}}[F(x)-f(x)]$

$$
=\lim _{x \rightarrow x_{0}} F(x)-\lim _{x \rightarrow x_{0}} f(x)=F\left(x_{0}\right)-f\left(x_{0}\right)=g\left(x_{0}\right) .
$$

因此当 $g(x)$ 有意义的话，那么 $g\left(x_{0}\right)=F\left(x_{0}\right)-f\left(x_{0}\right)=$ $\lim _{x \rightarrow x_{0}} g(x)$ ，这与假设是矛盾的，故 $F(x)$ 在点 $x_{0}$ 不连续；若 $g\left(x_{0}\right)$ 没有意义，那么当然它在 $x_{0}$ 点不连续.
(6) 不，例如，

$$
f(x)=\left\{\begin{array}{l}
1, \text { 当 } x \geqslant 0, \\
-1, \text { 当 } x<0 .
\end{array} \text { 及 } g(x)=\left\{\begin{array}{l}
-1, \text { 当 } x \geqslant 0, \\
1, \text { 当 } x<0 .
\end{array}\right.\right.
$$

它们在点 $x=0$ 处均不连续，但其和 $f(x)+g(x) \equiv$ 0 却处处连续.
742. 设：(a) 函数 $f(x)$ 在点 $x_{0}$ 连续，而 $g(x)$ 在点 $x_{0}$ 不连续； （6）当 $x=x_{0}$ 时 $f(x)$ 和 $g(x)$ 二者都是不连续的. 则此二函数的乘积 $f(x) g(x)$ 在已知点 $x_{0}$ 是否必为不连续？举出适当的例子。
解 (a)不。例如，

$$
g(x)=\left\{\begin{array}{l}
1, \text { 当 } x \geqslant 0 \\
-1, \text { 当 } x<0
\end{array} \text { 及 } f(x)=0 .\right.
$$

它们满足假设条件，其中 $f(x)$ 处处连续，而 $g(x)$ 在点 $x=0$ 不连续, 但 $f(x) g(x) \equiv 0$ 处处连续.
（6）不，例如，

$$
f(x)=\left\{\begin{array}{l}
1, \text { 当 } x \geqslant 0 \\
-1, \text { 当 } x<0
\end{array} \text { ，及 } g(x)=f(x)\right. \text {. }
$$

它们均在点 $x=0$ 处不连续，但其乘积 $f(x) g(x) \equiv$ 1 却处处连续。
743. 可否断定不连续函数平方后仍为不连续函数？举出处处都有不连续点的函数，而平方后是连续函数的例子。
解 不能。例如 742 题（6）之例。
又对于函数
$f(x)=\left\{\begin{array}{l}-1, \text { 当 } x \text { 为有理数， } \\ 1, \text { 当 } x \text { 为无理数， }\end{array}\right.$
处处不连续，但平方后所得函数 $f^{2}(x) \equiv 1$ 却处处连续.
744. 研究函数 $f[g(x)]$ 及 $g[f(x)]$ 的连续性，设：
(a) $f(x)=\operatorname{sgn} x$ 及 $g(x)=1+x^{2}$ ；
(б) $f(x)=\operatorname{sgn} x$ 及 $g(x)=x\left(1-x^{2}\right)$ ；
(в) $f(x)=\operatorname{sgn} x$ 及 $g(x)=1+x-[x]$.

解 (a) $f[g(x)]=1$ 处处连续；
而 $g[f(x)]=\left\{\begin{array}{l}2, x \neq 0 ; \\ 1, \text { 当 } x=0,\end{array}\right.$
在 $x=0$ 点不连续。
（6）因为 $g(x)=x\left(1-x^{2}\right)$ 当 $x<-1$ 或 $0<x<1$ 时为正，而当 $-1<x<0$ 或 $x>1$ 时为负，故

$$
f[g(x)]=\left\{\begin{array}{l}
1, \text { 当 } x<-1 ; \\
0, \text { 当 }=-1 ; \\
-1, \text { 当 }-1<x<0 ; \\
0, \text { 当 } x=0 ; \\
1, \text { 当 } 0<x<1 ; \\
0, \text { 当 } x=1 ; \\
-1, \text { 当 } x>1 .
\end{array}\right.
$$

在点 $x=-1, x=0, x=1$ 处不连续。而 $g[f(x)]=0$ 却处处连续。
（B） $f[g(x)] \equiv 1$ 处处连续。
$g[f(x)] \equiv 1$ 也处处连续。

## 745. 设

$$
f(u)=\left\{\begin{array}{l}
u, 0<u \leqslant 1 ; \\
2-u, \text { 当 } 1<u<2,
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-424.jpg?height=147&width=1212&top_left_y=1497&top_left_x=382)

## 研究复合函数 $y=f(u)$ 的连续性，其中 $u=\varphi(x)$ 。

解 当 $x$ 为有理数时， $u=x$ ，且 $0<u<1$ ，故 $f(u)=x$ ；当 $x$ 为无理数时， $u=2-x$ 且 $1<u<2$ ，故 $f(u)=2-u=$ $x$ 。从而 $f[\phi(x)] \equiv x$ 处处连续；
746. 证明若 $f(x)$ 为连续函数，则下列函数也是连㫨的：

$$
F(x)=|f(x)|
$$

证 设 $x_{0}$ 为任一连续点，则对于任给的 $\epsilon>0$ ，总存在一个正数 $\delta$ ，使当 $\left|x-x_{0}\right|<\delta$ 时，佰有 $\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon$ 。
由 $\left|\left|f(x)-\left|f\left(x_{0}\right)\right|\right| \leqslant\right| f(x)-f\left(x_{0}\right)$ ；知

$$
\left||f(x)|-\left|f\left(x_{0}\right)\right|\right|<\varepsilon,
$$

故 $F(x)$ 在点 $x_{0}$ 也连续。
418
747. 证明若函数 $f(x)$ 是连续的，则通数

$$
f_{r}(x)=\left\{\begin{array}{l}
-c, \text { 若 } f(x)<-c, \\
f(x), \text { 若 } \mid f(x) \leqslant c, \\
c, \text { 若 } f(x)>c,
\end{array}\right.
$$

（式中 $c$ 为任意的正数）也是连续函数。
证 易知

$$
f_{\mathrm{r}}(x)=\frac{1}{2}(|c+f(x)|-|c-f(x)|)
$$

于是，利用 746 题的结果，即知 $f_{c}(x)$ 是连续函数。
748. 证明若函数 $f(x)$ 在闭区间 $[a, b]$ 上连续, 则函数

$$
m(x)=\inf _{k \rightarrow x}\{f(\xi)\} \text { 和 } M(x)=\sup _{x<k}\{f(\xi)\}
$$

在 $[a, b]$ 上也是连续的.
证 只证 $m(x)$ 在 $[a, b]$ 连续. $M(x)$ 连续性之证完全类似. 设 $x_{0} \in[a, b]$ 。先证 $m(x)$ 在点 $x_{0}$ 右连续。任给 $\varepsilon>0$ 。由于 $f(x)$ 在点 $x_{0}$ 连续,故存在 $\delta>0$, 使当 $\mid x-x_{0}<\delta$时，恒有

$$
\left|f(x)-f\left(x_{0}\right)\right|<\varepsilon .
$$

于是, 当 $x_{0}<x<x_{0}+\delta$ 时, 有

$$
f(x)>f\left(x_{0}\right)-\varepsilon \geqslant m\left(x_{0}\right)-\varepsilon .
$$

而当 $a \leqslant x \leqslant x_{0}$ 时， $f(x) \geqslant m\left(x_{0}\right)>m\left(x_{0}\right)$ 一 $\varepsilon_{\text {明 由此可知 }}$当 $x_{0}<x<x_{0}+\delta$ 时， $m(x) \geqslant m\left(x_{0}\right)-\varepsilon$ 。又因 $m(x)$ 显然是递减的，故

$$
m\left(x_{0}\right) \geqslant m(x) \geqslant m\left(x_{0}\right)-\epsilon\left(\text { 当 } x_{0}<x<x_{0}+\delta \text { 时 }\right) .
$$

由此可知 $\lim _{x \rightarrow x_{0}+0} m(x)=m\left(x_{\mathrm{Q}}\right)$ ，即 $m(x)$ 在 $x_{0}$ 右连续. 下证左连续，不妨设 $f(x)$ 在 $\left[a, x_{0}\right]$ 的最小值在点 $x=x_{0}$ 达到，即 $m\left(x_{0}\right)=f\left(\dot{x}_{0}\right)$ （否则，若 $m\left(x_{0}\right)=f\left(x_{1}\right), a \leqslant x_{1}<$
$x_{0}$. 则显然知，当 $x<x<x_{0}$ 时 $m(x)=m\left(x_{0}\right)$ ，从而左连续)。任给 $\varepsilon>0$ 。仿上述, 存在 $\delta>0$, 使当 $x_{0}-\delta<x<x_{\mathrm{c}}$时，恒有

$$
f(x)<f\left(x_{0}\right)+\varepsilon=m\left(x_{0}\right)+\varepsilon,
$$

因此 $m(x)<m\left(x_{0}\right)+\varepsilon$, 从而

$$
m\left(x_{0}\right) \leqslant m(x)<m\left(x_{0}\right)+\varepsilon\left(\text { 当 } x_{0}-\delta<x<x_{0}\right. \text { 时). }
$$

由此可知 $\lim _{x \rightarrow x_{0} \cdot 0} m(x)=m\left(x_{0}\right)$, 即 $m(x)$ 在 $x_{1}$ 左连续.
证毕。
749. 证明 若函数 $f(x)$ 和 $g(x)$ 是连续的, 则函数
$\varphi(x)=\min [f(x), g(x)]$ 和 $\psi(x)=\max [f(x), g(x)]$
也是连续的。
证 由 $\varphi(x)=\frac{1}{2}[f(x)+g(x)-|f(x)-g(x)|]$ 。

$$
\psi(x)=\frac{1}{2}[f(x)+g(x)+|f(x)-g(x)|]
$$

利用 746 题的结果，即知 $\varphi(x), \psi(x)$ 为连续的。
750. 设函数 $f(x)$ 在闭区间 $[a, b]$ 上有定义并有界，证明函数
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-426.jpg?height=110&width=1451&top_left_y=1758&top_left_x=411) $b^{6}$ 是左方连续的. 而西数

$$
\bar{m}(x)=\inf _{x \leqslant\{x}\{f(\xi)\} \text { 和 } \bar{M}(x)=\sup _{x \leqslant \xi \leqslant}\{f(\xi)\}
$$

在闭区间 $[a, b]$ 是右方连续的 ${ }^{*}$ ．
证 设 $x_{0} \in(a, b]$ ，要证 $m(x)$ 在 $x_{0}$ 左方连续. 由于 $f$ $(x)$ 在 $[a, b]$ 上有界，故 $m(x)$ 恒为有限，任给 $\varepsilon>0$ ，必存在一点 $\xi_{0} \in\left[a, x_{0}\right)$ ，使得

$$
f\left(\xi_{0}\right)<m\left(x_{0}\right)+\varepsilon_{.}
$$

于是，当 $\xi_{0}<x<x_{0}$ 时，必有 $m\left(x_{0}\right) \leqslant m(x) \leqslant f\left(\xi_{0}\right)<m$
$\left(x_{0}\right)+\varepsilon$ ，由此可知 $\lim _{x \rightarrow x_{1}-6} m(x)=m\left(x_{0}\right)$ 。故 $m(x)$ 在 $x_{0}$ 点左方连续。

同法可证 $M(x)$ 在 $[a, b]$ 也为左方连续.

* $) \bar{m}(x)$ 和 $\bar{M}(x)$ 在 $[a, b]$ 右方连续的结论是错误的，今举反例以明之，例如，对于有界函数

$$
\begin{aligned}
f_{1}(x) & =\left\{\begin{array}{l}
1, \text { 当 } a \leqslant x \leqslant p ; \\
0, \text { 当 } p<x \leqslant b .
\end{array}\right. \\
f_{2}(x) & =\left\{\begin{array}{l}
-1, \text { 当 } a \leqslant x \leqslant p ; \\
0, p<x \leqslant b .
\end{array}\right.
\end{aligned}
$$

分别有

$$
\bar{m}(x)=f_{1}(x), \bar{M}(x)=f_{2}(x),
$$

显然它们在点 $p$ 不是右方连续的。
若定义 $\bar{m}(x)=\operatorname{in}_{x<\leqslant, b} f\{f(\xi)\} ; \bar{M}(x)=\sup _{x<\in \in b}\{f(\xi)\}$ ，则可证明 $\bar{m}(x)$ 与 $\bar{M}(x)$ 在 $[a, b]$ 右方连续。
751. 证明若函数 $f(x)$ 于区间 $a \leqslant x<+\infty$ 上连续，且有有限的 $\lim _{x \rightarrow+\infty} f(x)$ ，则此函数在已知区间上是有界的。
证. 记 $A=\lim _{x \rightarrow+\infty} f(x)$, 取 $\varepsilon=1$, 则存在 $X>a$, 使当 $x>$ $X$ 时，恒有 $|f(x)|<|A|+1$ ，又因 $f(x)$ 在 $[a, X]$ 上连续，因而有界，即存在常数 $M_{1}$ ，使当 $x \in[a, X]$ 时，恒有 $|f(x)|<M_{1}$, 取 $M=\max \left(|A|+1, M_{1}\right)$ ，
则 $x \in[a,+\infty)$ 时，恒有

$$
|f(x)|<M
$$

752. 设函数 $f(x)$ 在区间 $\left(x_{0},+\infty\right)$ 上连续并有界, 证明对于任何数 $T$ ，可求得叙列 $x_{n} \rightarrow+\infty$ ，使

$$
\lim _{n \rightarrow \infty}\left[f\left(x_{n}+T\right)-f\left(x_{n}\right)\right]=0
$$

证 不妨设 $T>0$, 记 $g(y)=f\left(x_{0}+(y+1) T\right)-f\left(x_{0}+\right.$ $y T), y \geqslant 1$. 取一叙列 $\left\{\varepsilon_{n}\right\}(n=1,2, \cdots)$, 且当 $n \rightarrow \infty$ 时, $\varepsilon_{n}$ $\rightarrow 0$ 。易见， $g(y)$ 是 $[1,+\infty)$ 上连续且有界的函数，今按下法取 $x_{1}=x_{0}+k_{1} T$ ，使 $\left|g\left(k_{1}\right)\right|<\varepsilon_{1} \mid$ 如果 $g(1), g(2)$ 异号，则由连续函数介值定理，存在 $k_{i}$ ，且 $1<k_{1}<2$ ，使得 | $g\left(k_{1}\right) \mid=0<\varepsilon_{1}$, 这时取 $x_{1}=x_{0}+k_{1} T$. 若 $g(1)$ 与 $g(2)$ 同号，且 $g(1), g(2), g(3), g(4) \cdots$ 都是同号的，不妨设它们均大于 0 ，那么我们可以证明，必存在一个自然数 $k_{1} \geqslant$ 1 , 使 $g\left(k_{1}\right)<\varepsilon_{1}$. 因为, 若对一切自然数 $n, g(n) \geqslant \varepsilon_{1}$, 则由 $g(y)$ 的定义，

$$
\begin{aligned}
& f\left(x_{0}+2 T\right) \geqslant \varepsilon_{1}+f\left(x_{0}+T\right), \\
& f\left(x_{0}+3 T \geqslant \varepsilon_{1}+f\left(x_{0}+2 T\right),\right. \\
& f\left(x_{0}+4 T\right) \geqslant \varepsilon_{1}+f\left(x_{0}+3 T\right),
\end{aligned}
$$

$$
f\left(x_{n}+n T\right) \geqslant \varepsilon_{1}+f\left[x_{0}+(n-1) T\right] .
$$

则 $f\left(x_{0}+n T\right) \geqslant(n-1) \varepsilon_{1}+f\left(x_{0}+T\right)$ ，这与 $f(x)$ 在 $\left(x_{0}\right.$, $+\infty)$ 内有界矛盾, 故必存在自然数 $k_{1}$, 使得 $\left|g\left(k_{1}\right)\right|<$ $\varepsilon_{1}$, 取 $x_{1}=x_{0}+k_{1} T$ 。然后，取自然数 $p_{2}>k_{1}+1$ 。通过考虑 $g\left(p_{2}\right), g\left(p_{2}+1\right), \cdots$ 的符号; 仿上，可取 $x_{2}=x_{0}$ 年 $k_{2} T, k_{2}$ $>k_{1}+1$, 使 $\left|g\left(k_{2}\right)\right|<\varepsilon_{2}$ 。依此类推，我们就可得到一叙列 $\left\{x_{n}\right\}$ 适合要求。
753. 若 $\varphi(x)$ 和 $\psi(x)$ 为连续周期函数, 当 $-\infty<x<+\infty$ 时,有定义且

$$
\lim _{x \rightarrow+\infty}[\phi(x)-\psi(x)]=0
$$

证明

$$
\varphi(x) \doteq \phi(x) .
$$

证 先证明 $\varphi(x)$ 和 $\psi(x)$ 的周期相同，设 $\varphi(x)$ 的周期为
$p$ ，则 $\varphi(x+p)=\varphi(x)$ ，由于当 $x \rightarrow \infty$ 时， $\varphi(x+p)-\varphi(x$ $+p) \rightarrow 0$ 即得
$\lim _{x \rightarrow \infty}[\varphi(x)-\psi(x+p)]=0$
以及

$$
\begin{aligned}
& \lim _{x \rightarrow \infty}[\phi(x)-\phi(x+p)] \\
= & \lim _{x \rightarrow \infty}\left[\varphi(x)-\psi(x+p]-\lim _{x \rightarrow \infty}[\phi(x)-\phi(x)]=0 .\right.
\end{aligned}
$$

我们再来正明 $\phi(x)$ 的周期也是 $p$ ，若不然，则至少存在一个 $x_{0}$ ，使 $\phi\left(x_{0}\right) \neq \psi\left(x_{0}+p\right)$ 。且设 $\psi(x)$ 周期为 $q$ ， $N$ 为任意正整数， $x=x_{0}+N q$ ，以及 $a=\mid \psi\left(x_{0}\right)-\phi\left(x_{0}+\right.$ $p) \mid>0$ ，此时恒有 $|\psi(x)-\psi(x+p)|=\alpha$ 。但由（1）式，对充分大的 $x$, 必成立 $|\psi(x)-\psi(x+p)|<\alpha$ ，这显然是矛盾的。

最后证明 $\varphi(x)=\phi(x)$ ，若结论不成立，则至少存在 $\cdots$ 一个 $x_{1}$ ，使 $\varphi\left(x_{1}\right) \neq \psi\left(x_{1}\right)$ 。记 $\beta=\mid \varphi\left(x_{1}\right)-\psi\left(x_{1}\right)>0$ ，则对任意 $x=x_{1}+N p$, 恒有 $|\varphi(x)-\phi(x)|=\beta$, 这与 $\lim _{x \rightarrow+\infty}[\varphi$ $(x)-\phi(x)]=0$ 矛盾。于是， $\phi(x) \equiv \psi(x)$ 。证毕。
754. 证明单调有界函数的一切不连续点皆为第一类的不连续点。
证 不妨设 $f(x)$ 为单调增函数，取其定义域 $A$ 中的任意点 $x_{0}$ ，且设 $x_{0}$ 不是 $A$ 的左端点，由于 $x<x_{0}$ 时显然有 $f(x) \leqslant f\left(x_{0}\right)$ 。由关于单调函数的极限定理知 $f\left(x_{f}-0\right)$ $=\lim _{x \rightarrow x_{0} \rightarrow-0} f(x) \leqslant f\left(x_{0}\right)$. 可见若 $f(x)$ 在 $x_{0}$ 点不连续，则函数在该点只可能有柾度，即第一类呵断点。
755. 证明若函数 $f(x)$ 具有下列诸性质：(1)在闭区间[a,b]上有定义且单调，(2)取介于 $f(a)$ 和 $f(b)$ 之间所有的数作

为其函数值, 则此函数在 $[a, b]$ 上连续.
证 用反证法，不妨设单调函数 $f(x)$ 为递增的且在 $x_{0}$间断 $\left(x_{0} \in[a, b]\right)$ ，由 754 题知 $x_{\mathrm{e}}$ 只能是第一类间断点，则 $f\left(x_{0}\right)-f\left(x_{0}-0\right)$ 及 $f\left(x_{0}+0\right)-f\left(x_{0}\right)$ 中至少有一个大于零，例如 $f\left(x_{0}\right)-f\left(x_{0}-0\right)>0$ 。于是，由函数 $f(x)$的单调性知， $f(x)$ 无法取到 $f\left(x_{0}-0\right)$ 和 $f\left(x_{0}\right)$ 之间的数值。

这与题设函数 $f(x)$ 的性质（2）矛盾，从而 $f(x)$ 在 $[a, b]$ 上连续.
756. 证明：函数

$$
f(x)=\sin \frac{1}{x-a} \text {, 若 } x \neq a \text { 及 } f(a)=0 \text {, }
$$

在任意闭区间 $[a, b]$ 上取介于 $f(a)$ 和 $f(b)$ 之间的一切中介值，但在 $[a, b]$ 上并不连续。
证 。 事实上, 只要 $a<b$, 则 $f(x)$ 在 $[a, b]$ 上取 $[-1,1]$ 之间的一切值，当然更取 $f(a)=0$ 与 $f(b)(f(b) \mid \leqslant 1)$ 之间的一切值。但显然有 $f(x)$ 在 $x=a$ 处不连续。
757. 证明：若函数 $f(x)$ 在区间 $(a, b)$ 内连续，且 $x_{1}, x_{1}, \cdots, x_{n}$为此区间中的任意值，则在它们之间可找到一个数值 $\boldsymbol{\xi}$ ，使得

$$
f(\xi)=\frac{1}{n}\left[f\left(x_{1}\right)+f\left(x_{2}\right)+\cdots+f\left(x_{n}\right)\right]
$$

证 不妨设 $a<x_{1} \leqslant x_{2} \leqslant \cdots \leqslant x_{n}<b$, 此时设 $x_{1} \neq x_{n}$ ，当 $x_{1}=x_{n}$ 结论显然珹立。

由于 $f(x)$ 在 $\left[x_{1}, x_{n}\right]$ 上连续，于是， $f(x)$ 在 $\left[x_{1}, x_{n}\right]$上聚得最大值和最小值：

$$
m \leqslant f(x) \leqslant M, \quad x \in\left[x_{1}, x_{n}\right] .
$$

从而有

$$
m \leqslant \frac{1}{n} \sum_{i=1}^{n} f\left(x_{i}\right) \leqslant M
$$

由连续函数的性质，总存在 $\xi \in\left[x_{1}, x_{*}\right]$ ，使

$$
f(\xi)=\frac{1}{n} \sum_{i=1}^{n} f\left(x_{i}\right)
$$

758. 设函数 $f(x)$ 在区间 $(a, b)$ 上连续,且

$$
l=\underline{\lim }_{x \rightarrow \alpha+\theta} f(x) \text { 及 } L=\varlimsup_{x \rightarrow a+0} f(x) .
$$

证明对于任境的数 $\lambda$,䰹处 $l \leqslant \lambda \leqslant L$, 则有叙列 $x_{k} \rightarrow a$ $+0(n=1,2, \cdots)$ ，使得

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=\lambda .
$$

证 当 $\lambda=l$ 或 $\lambda=L$ 时结论都是显然的。因此设

$$
l<\lambda<L .
$$

由条件有 $\left\{a_{n}\right\}$ 及 $\left\{b_{n}\right\}, a_{n} \rightarrow a+0, b_{n} \rightarrow a+0$,

$$
\text { 且 } \lim _{n \rightarrow \infty} f\left(a_{n}\right)=l, \lim _{n \rightarrow \infty} f\left(b_{n}\right)=L .
$$

于是, 存在自然数 $N$, 使当 $n>N$ 时, 恒有

$$
f\left(a_{n}\right)<\lambda \text { 及 } f\left(b_{n}\right)>\lambda .
$$

再由 $f(x)$ 的连续性知，在 $a_{n}$ 及 $b_{n}$ 之间存在 $x_{n}$ ，使

$$
f\left(x_{n}\right)=\lambda(n>N) .
$$

这样选取的 $\left\{x_{n}\right\}$ ，由于 $a_{n} \rightarrow a+0, b_{n} \rightarrow a+0$ ，故 $x_{n} \rightarrow a$ +0 ，从而

$$
\lim _{n \rightarrow \infty} f\left(x_{n}\right)=\lambda
$$

## §8. 反函数. 用参数表示的函数

$1^{\circ}$ 名函数的存在及其连续性 若函数 $y=f(x)$ 具有下列性质；（1）

在区间 $(a, b)$ 上有定义并连续；(2)在 ${ }^{\text {画格的意义上说来，于此区间上是 }}$单调的，则有单值的反函数 $x=f^{-1}(y)$ ，此函数在区间 $(A, B)$ 上有定义并迋续，而且在严格的意义上说来，是相应地单调的，其中

$$
A=\lim _{x \rightarrow+\infty} f(x) \text { 和 } B=\lim _{x \rightarrow-\infty} f(x) \text {. }
$$

任何一个单值连续函数 $x=g(y)$ ，它在其有定义的最大区域上迼合方程 $f(g(y))=y$ ，则被了解为已知连续函数 $y=f(x)$ 的多值反函数的一个单值连续分枝。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-432.jpg?height=70&width=1466&top_left_y=930&top_left_x=295)上有定义并且是迋续的，且函数 $\varphi(t)$ 在此区间上是严格地单调的，则方程组

$$
x=\varphi(t), y=\psi(t)
$$

在区间 $(a, b)$ 上把 $y$ 定义成 $x$ 的单值连续函数：

$$
y=\phi\left[\varphi^{-1}(x)\right],
$$

其中 $a=\lim _{t \rightarrow+0} \varphi(t) 及 b=\lim _{t \rightarrow-0} \varphi(t)$.

## 759. 求线性分式函数

$$
y=\frac{a x+b}{c x+d}(a d-b c \neq 0)
$$

的反函数. 在念样的情形下，反函数与已知函数相同？
角 由 $y=\frac{a x+b}{c x+d}$ 解之得反函数为

$$
y=\frac{-d x+b}{c x-a} \text { 或写成 } x=\frac{-y d+b}{y c-a} .
$$

欲反函数与已知函数相問，只颁

$$
\frac{a x+b}{c x+d}=\frac{-x d+b}{c x-a}
$$

解之得

$$
a+d=0,
$$

此即所求的兵泮.
760. 设

$$
y=x+[x],
$$

求反函数 $x=x(y)$ ，
解 若当 $k \leqslant x<k+1$, 即当

$$
2 k \leqslant y<2 k+1
$$

时, $[x]=k(k=0, \pm 1, \pm 2, \cdots)$, 此时 $y=x+k$, 即反函数为 $x=y-k$.
761. 证明：有唯一的连续通数 $y=y(x)(-\infty<x<+\infty)$ 满足于克卜勒方程

$$
y-\varepsilon \sin y=x(0 \leqslant \varepsilon<1) .
$$

证 由 640 题知叙列

$$
\begin{aligned}
& y_{0}=x, \\
& y_{1}=x+\sin y_{0}, \\
& y_{2}=x+\varepsilon \sin y,
\end{aligned}
$$

$$
y_{\pi}=x+e \sin y_{n-1},
$$

的极限 $y(x)$ 为克卜勒方程 $y$ - $\sin y=x$ 的唯一的根。现在证明 $y=y(x)$ 是连续的. 我们只须证明当 $x \rightarrow x_{0}$时, $y(x) \rightarrow y\left(x_{0}\right)$. 为此, 我们考虑

$$
\begin{aligned}
& \left|y_{n}(x)-y_{n}\left(x_{0}\right)\right| \\
& =\left|\left(x-x_{0}\right)+\varepsilon\left[\sin y_{n-3}(x)-\sin y_{n-1}\left(x_{0}\right)\right]\right| \\
& \leqslant\left|x-x_{0}\right|+\varepsilon\left|y_{n-1}(x)-y_{n-1}\left(x_{0}\right)\right|
\end{aligned}
$$

逐论应用此不等式，即得

$$
\begin{aligned}
& \left|y_{n}(x)-y_{n}\left(x_{0}\right)\right| \\
& \leqslant\left|x-x_{0}\right|\left(1+\varepsilon+\varepsilon^{2}+\cdots+\varepsilon^{n-1}+\varepsilon^{n}\right) \\
& =\left|x-x_{0}\right| \cdot \frac{1-\varepsilon^{+1}}{1-\varepsilon} \leqslant \frac{1}{1-\varepsilon}\left|x-x_{0}\right|
\end{aligned}
$$

令 $n \rightarrow \infty$ ，便有

$$
\left|y(x)-y\left(x_{0}\right)\right| \leqslant \frac{1}{1-\varepsilon}\left|x-x_{0}\right|(0 \leqslant \varepsilon<1) .
$$

于是，显然有 $\lim _{x \rightarrow x_{0}} y(x)=y\left(x_{0}\right)$ 。这就证明了 $y(x)$ 的连续性。

## 762. 证明：方程

$$
\operatorname{ctg} x=k x
$$

对于每一个实数 $k(-\infty<k<+\infty)$ 在区间 $0<x<\pi$ 中有唯一连续的根 $x=x(k)$ 。
证 令 $f(x)=\frac{\operatorname{ctg} x}{x}$ 。泉然，在 $(0, \pi)$ 上 $\operatorname{ctg} x$ 和 $\frac{1}{x}$ 都是连续的严格减函数，从而 $f(x)$ 在 $(0, \pi)$ 上也是连续的严格减函数，并且，很明显

$$
\lim _{x \rightarrow+0} f(x)=+\infty, \lim _{x \rightarrow-0} f(x)=-\infty .
$$

由此可知，对每一实数 $k(-\infty<k<+\infty)$ ，恰有一个 $x \in$ $(0, \pi)$ ，使 $f(x)=k$ ，即 $\operatorname{ctg} x=k x$ 。另外，由于 $f(x)=\frac{\operatorname{ctg} x}{x}$在 $(0, \pi)$ 上是连续的严格减函数，故 $k=f(x)$ 的反函数 $x$ $=x(k)=f^{-1}(k)$ 存在而且是 $-\infty<k<+\infty$ 上的连续的严格减函数。此 $x=x(k)$ 即方程 $\operatorname{ctg} x=k x$ 的根。

综上述，可知：对任何 $-\infty<k<+\infty$ ，方程 $\operatorname{ctg} x=$ $k x$ 在 $(0, \pi)$ 上具有唯一的根 $x=x(k)$ ，而且 $x(k)$ 是 $k(-$ $\infty<k<+\infty$ )的连续的严格减函数. 证毕.
763. 非单调的函数 $y=f(x)(-\infty<x<+\infty)$ 可否有单值的反函数？
解 可以，例如函数
$y=\left\{\begin{array}{l}x, \text { 若 } x \text { 为有理数, } \\ -x, \text { 若 } x \text { 为无理数. }\end{array}\right.$
在区间 $(-\infty,+\infty)$ 上为单值的，但不是单调的函数，而其反函数仍为此函数本身。
764. 在甚么情形下, 函数 $y=f(x)$ 和反莉数 $x=f^{-1}(y)$ 是同一的函数？
解 为统一坐标起见，我们把 $y=f(x)$ 的反函数记成为 $y=f^{-1}(x)$ 。

按题设应有

$$
f^{-1}(x) \equiv f(x),
$$

即 $x=f(f(x))$ ，这就是所求的条件。
765. 证明不阵续函数

$$
y=\left(1+x^{2}\right) \operatorname{sgn} x
$$

的反函数是连续函数.
证 易见 $\operatorname{sgn} y=\operatorname{sgn} x$ 及 $\operatorname{sgn}^{2} x=\left\{\begin{array}{l}1, x \neq 0 \\ 0, x=0\end{array}\right.$, 则
$y \operatorname{sgn} y=\left(1+x^{2}\right) \operatorname{sgn}^{2} x$. 于是反函数在 $|y| \geqslant 1$ 及 $y=0$ 有定义:
$x=\left\{\begin{array}{l}\sqrt{y s g n y-1}, \text { 当 } y \geqslant 1 \text { 时; } \\ -\sqrt{y s g n y-1}, \text { 当 } y \leqslant-1 \text { 时； } \\ 0 \quad \text { 当 } y=0 \text { 时。 }\end{array}\right.$
易见上述函数在其定义域内连续。
766. 证明：若函数 $f(x)$ 在闭区间 $[a, b]$ 上有定义并且是严格地单调的，且

则

$$
\begin{aligned}
\lim _{n \rightarrow \infty} f\left(x_{n}\right) & =f(a) \quad\left(a \leqslant x_{n} \leqslant b\right), \\
& \lim _{a \rightarrow \infty} x_{n}
\end{aligned}
$$

证 不妨设函数 $f(x)$ 在 $[a, b]$ 上严格单调下降. 如果结论不真，則在 $(a, b)$ 内总夲在一个 $a_{1}$ 及叙列 $\left\{x_{n}\right\}$ 的一个 "子列 $\left\{\ddot{x}_{n_{k}}\right\}$ ，使

$$
x_{n_{k}}>a_{1} .
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-436.jpg?height=72&width=787&top_left_y=701&top_left_x=406)

$$
f\left(x_{n_{k}}\right)<f\left(a_{1}\right)<f(a) .
$$

于题； $f(a)=\lim _{* \rightarrow \infty} f\left(x_{n_{k}}\right) \leqslant f\left(\dot{a}_{1}\right)$ ，得出矛盾，
因此，有

$$
\lim _{n \rightarrow \infty} x_{n}=a .
$$

求下列函数的反函数的连续的单值枝：
767. $y=x^{2}$ 。

解 反函数的单值迋续分枝为

$$
x=\sqrt{y} \quad(0 \leqslant y<+\infty)
$$

及 $x=-\sqrt{y},(0 \leqslant y<+\infty)$.
768. $y=2 x-x^{2}$.

啴 由于 $x^{2}-2 x+y=0$ ，故

$$
x=\frac{2 \pm \sqrt{4-4 y}}{2}=1 \pm \sqrt{1-y}
$$

于是单值连续分枝为
$x=1-\sqrt{1-y}$ 及 $x=1+\sqrt{1-y} \quad(-\infty<y \leqslant 1$ ).
769. $y=\frac{2 x}{1+x^{2}}$.

峥 由于 $x^{2} y+2 x+y=0$ ，故

$$
x=\left\{\begin{array}{l}
\frac{1 \pm \sqrt{1-y^{2}}}{y}, \\
0, \quad \text { 当 } y \neq 0 \text { 时； } \\
0 \text { 当 } y=0 \text { 时. }
\end{array}\right.
$$

又由于

$$
\begin{aligned}
& \lim _{y \rightarrow 0} \frac{1-\sqrt{1-y^{2}}}{y}=\lim _{y \rightarrow 0} \frac{y^{2}}{y\left(1+\sqrt{1-y^{2}}\right)}=0, \\
& \lim _{y \rightarrow 0} \frac{1+\frac{\sqrt{1-y^{2}}}{y}=\infty}{}=\infty,
\end{aligned}
$$

故反函数的连续分支为

$$
\begin{aligned}
& x=\frac{1-\sqrt{1-y^{2}}}{y}(-1 \leqslant y \leqslant 1) \\
\text { 及 } & x=\frac{1+\sqrt{1-y^{2}}}{y}(0<|y| \leqslant 1) .
\end{aligned}
$$

770. $y=\sin x$.

解 单值连续分枝为

$$
x=(-1)^{k} \arcsin y+k \pi \quad(k=0, \pm 1, \pm 2, \cdots)
$$

$(y \mid \leqslant 1)$.
771. $y=\cos x$.

解 单值连续分枝为
$x=2 k \pi \pm \arccos y(k=0, \pm 1, \pm 2, \cdots)(|y| \leqslant 1)$.
772. $y=\operatorname{tg} x$.

献 单值连续分枝为

$$
x=\operatorname{arctg} y+k \pi(k=0, \pm 1, \pm 2 \cdots)
$$

( $-\infty<y<+\infty$ ).
773. 证明连续函数 $y=1+\sin x$ 对应于区间 $0<x<2 \pi$ 的值的集合是一线段。
证 显然,当 $x \in(0,2 \pi)$ 时, $-1 \leqslant \sin x \leqslant 1$, 从而 $0 \leqslant 1+$ $\sin x \leqslant 2$ 。而由于 $\left.y\right|_{x-\frac{\pi}{2}}=2,\left.y\right|_{x=\frac{\pi x}{2}} ^{2}=0$ 。而 $y=1+\sin x$ 是 $\left[\frac{\pi}{2}, \frac{3 \pi}{2}\right]$ 上的连续函数，故由介值定理知当 $x$ 从 $\frac{\pi}{2}$ 变到 $\frac{3 \pi}{2}$ 时, $y$ 取 0 到 2 之间的一切数值. 由此可知当 $0<x<$
$2 \pi$ 时， $y$ 的值的集合是线段 $[0,2]$ 。
774. 证明等式

$$
\arcsin x+\arccos x=\frac{\pi}{2} .
$$

证 令 $\varphi=\arcsin x$, 则得 $\sin \varphi=x$ ，从面

$$
\cos \left(\frac{\pi}{2}-\varphi\right)=\sin \varphi=x
$$

因为 $-\frac{\pi}{2} \leqslant \mu \leqslant \frac{\pi}{2}$, 故 $0 \leqslant \frac{\pi}{2}-\varphi \leqslant \pi$; 而在 $[0, \pi]$ 内有唯一的数，它的余弦等于 $x$ 。因此，得

$$
\frac{\pi}{2}-p=\arccos x,
$$

即

$$
\arcsin x+\arccos x=\frac{\pi}{2}
$$

775. 证明等式

$$
\operatorname{arctg} x+\operatorname{arctg} \frac{1}{x}=\frac{\pi}{2} \operatorname{sgn} x \quad(x \neq 0)
$$

证 当 $x>0$ 时, 令 $\varphi=\operatorname{arctg} x$, 则得 $\operatorname{tg} \varphi=x$, 且 $0<\varphi<$ $\frac{\pi}{2}$ 。 又 $\operatorname{ctg}\left(\frac{\pi}{2}-\varphi\right)=\operatorname{tg} \varphi=x$ ，故

$$
\operatorname{tg}\left(\frac{\pi}{2}-\varphi\right)=\frac{1}{x}
$$

因为 $0<\frac{\pi}{2}-\varphi<\frac{\pi}{2}$, 而在 $\left(0, \frac{\pi}{2}\right)$ 内仅有唯一的数, 使其正切等于 $\frac{1}{x}$ ，故

$$
\frac{\pi}{2}-\varphi=\operatorname{arctg} \frac{1}{x},
$$

即当 $x>0$ 时, $\operatorname{arctg} x+\operatorname{arctg} \frac{1}{x}=\frac{\pi}{2}$.

当 $x<0$ 时，令 $\varphi=\operatorname{arctg} x$ ，则得 $\operatorname{tg} \varphi=x$ ，且 $-\frac{\pi}{2}<\varphi<$ 0. 又

$$
\operatorname{ctg}\left(-\frac{\pi}{2}-\varphi\right)=\operatorname{tg} \varphi=x \text {, 即 } \operatorname{tg}\left(-\frac{\pi}{2}-\varphi\right)=\frac{1}{x} \text {, }
$$

因为 $-\frac{\pi}{2}<-\frac{\pi}{2}-\varphi<0$, 而在 $\left(-\frac{\pi}{2}, 0\right)$ 内有唯一的数，使其正切等于 $\frac{1}{x}$ ，故

$$
-\frac{\pi}{2}-\varphi=\operatorname{arctg} \frac{1}{x},
$$

即当 $x<0$ 时, $\operatorname{arctg} x+\operatorname{arctg} \frac{1}{x}=-\frac{\pi}{2}$ 。总之，当 $x \neq 0$ 时，

$$
\operatorname{arctg} x+\operatorname{arctg} \frac{1}{x}=\frac{\pi}{2} \operatorname{sgn} x .
$$

776. 证明反正切相加的定理：

$$
\operatorname{arctg} x+\operatorname{arctg} y=\operatorname{arctg} \frac{x+y}{1-x y}+\varepsilon \pi,
$$

式中 $\varepsilon=\varepsilon(x, y)$ 为取值： $0,1,-1$ 三者之一的函数.
当已知 $x$ 的值时, 对于怎样的 $y$ 值，函数 $\varepsilon$ 可能不连续？在 $O x y$ 平面上作出画数 $\varepsilon$ 连续的对应域，并求此函数在所求得的域内的数值。
证 由于

$$
-\frac{\pi}{2}<\operatorname{arctg} y<\frac{\pi}{2} 及-\frac{\pi}{2}<\operatorname{arctg} x<\frac{\pi}{2},
$$

故有

$$
\begin{aligned}
& -\pi<\operatorname{arctg} x+\operatorname{arctg} y<\pi . \\
& \text { 若 } x \text { 和 } y \text { 的符号相反,则 } \\
& -\frac{\pi}{2}<\operatorname{arctg} x+\operatorname{arctg} y<\frac{\pi}{2} .
\end{aligned}
$$

若 $x>0$ 和 $y>0$ ，则
$0<\operatorname{arctg} x+\operatorname{arctg} y<\pi$.
再看这个和是位于 $\left(0, \frac{\pi}{2}\right)$ 还是 $\left(\frac{\pi}{2}, \pi\right)$ 。条件

$$
0<\operatorname{arctg} x+\operatorname{arctg} y<\frac{\pi}{2},
$$

即

$$
\operatorname{arctg} x<\frac{\pi}{2}-\operatorname{arctg} y
$$

它相当于 $x<\operatorname{tg}\left(\frac{\pi}{2}-\operatorname{arctg} y\right)=\operatorname{tg}(\operatorname{arcctg} y)=\frac{1}{y}$,也即 $x y<1$.

因此，当 $x>0, y>0, x y<1$ 时，此和位于 $\left(0, \frac{\pi}{2}\right)$ 。同法可证，当 $x>0, y>0, x y>1$ 时，此和位于 $\left(\frac{\pi}{2}, \pi\right)$.

仿此，又可证得：当 $x<0, y<0, x y<1$ 时，此和位于 $\left(-\frac{\pi}{2}, 0\right)$ ；当 $x<0, y<0, x y>1$ 时，此和位于 $\left(-\pi,-\frac{\pi}{2}\right)$.

总之，若 $x<1$ ，则此和位于 $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ ；若 $x>0, x y$ $>1$, 则此和位于 $\left(\frac{\pi}{2}, x\right)$; 若 $x<0, x y>1$, 则此和位于 $\left(-\pi,-\frac{\pi}{2}\right)$.

其欢，我们考甞此和的正切

$$
\operatorname{tg}(\operatorname{arctg} x+\operatorname{arctg} y)=\frac{x+y}{1-x y}
$$

现令 $u=\operatorname{arctg} x+\operatorname{arctg} y, v=\operatorname{arctg} \frac{x+y}{1-x y}$ ，则得

$$
\operatorname{tg} \boldsymbol{u}=\operatorname{tg} v .
$$

因为 $-\frac{\pi}{2}<u<\frac{\pi}{2}$, 故当 $-\frac{\pi}{2}<u<\frac{\pi}{2}$ 时,$u=v$; 当 $\frac{\pi}{2}<u<$ $\pi$ 时， $v+\pi=u$ ；当 $-\pi<u<-\frac{\pi}{2}$ 时， $u=-\pi+v$ 。因此，我们证得：

$$
\operatorname{arctg} x+\operatorname{arctg} y=\left\{\begin{array}{l}
\operatorname{arctg} \frac{x+y}{1-x y}, \text { 若 } x y<1 ; \\
\pi+\operatorname{arctg} \frac{x+y}{1-x y}, \\
-\pi>>0, x y>1 ; \\
-\pi+\operatorname{arctg} \frac{x+y}{1-x y}, \text { 若 } x>0, x y>1 ;
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-441.jpg?height=912&width=855&top_left_y=1280&top_left_x=723)

图 1.313
当 $x$ 固定时, 若 $y=\frac{1}{x}$, 则 $\varepsilon$ 不连续，因为此时（例如设 $x>0$ ），当 $y>\frac{1}{x}$ 时 $\epsilon \equiv 1$ ，而当 $y<\frac{1}{x}$ 时 $\epsilon \equiv 0$ 。

如图1.313所示, 曲线 $x y=1$ 为函数 $\varepsilon=\varepsilon(x, y)$ 的不连续域。

$$
\text { 当 } x y<1 \text { 时, } \varepsilon=0 \text {; 当 } x>0, x y>1 \text { 时, } \varepsilon=1 \text {; 当 } x<
$$

$0, x y>1$ 时, $\varepsilon=-1$.
777. 证明反正弦相加的定理：
$\arcsin x+\arcsin y=(-) \arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right)$ + Eп

$$
(|x| \leqslant 1,|y| \leqslant 1),
$$

式中, 若 $x y \leqslant 0$ 或 $x^{2}+y^{2} \leqslant 1, \varepsilon=0$; 若 $x y>0$ 及 $x^{2}+y^{2}>$ $1, \varepsilon=\operatorname{sgn} x$.
证 令 $u=\arcsin x+\arcsin y(|x| \leqslant 1,|y| \leqslant 1)$,
即得

$$
\sin u=x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}} .
$$

由此, 还不能断定

$$
u=\arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right) .
$$

事实上， $u$ 及 $v=\arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right)$ 可以位在不同的区间内，其中 $v$ 始终位在 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 内，而 $\boldsymbol{u}$ 可有

## 三种情形：

情形 I: $-\frac{\pi}{2} \leqslant u \leqslant \frac{\pi}{2}$.
若 $x y \leqslant 0$, 则不是 $0 \leqslant x \leqslant 1$ 及 $-1 \leqslant y \leqslant 0$ 就是 $-1 \leqslant$ $x \leqslant 0$ 及 $0 \leqslant y \leqslant 1$ ，不论明一种棈况，总有

$$
0 \leqslant \arcsin x \leqslant \frac{\pi}{2} \text { 及 }-\frac{\pi}{2} \leqslant \arcsin y \leqslant 0 \text { (或交换) }
$$

因而

$$
-\frac{\pi}{2} \leqslant \arcsin x+\arcsin y=u \leqslant \frac{\pi}{2} .
$$

若 $x>0, y>0$ 时, 显然有 $u \geqslant 0$. , 条件 $u \leqslant \frac{\pi}{2}$
即

$$
u=\arcsin x+\arcsin y \leqslant \frac{\pi}{2},
$$

相当于
$\arcsin x \leqslant \frac{\pi}{2}-\arcsin y=\arccos y$.
由于正弦在第一象限内是增函数，故这又相当于 $\sin (\arcsin x) \leqslant \sin (\arccos y)$ ，
或 $x \leqslant \sqrt{1-y^{2}}$, 即 $x^{2}+y^{2} \leqslant 1$ 。
同法可证，若 $x<0, y<0$ 时，必 $u \leqslant 0$ 。且条件 $-\frac{\pi}{2} \leqslant u$ 相当于 $x^{2}+y^{2} \leqslant 1$.

情形 I : $\frac{\pi}{2}<u \leqslant \pi$.
在 $\frac{\pi}{2}<u \leqslant \pi$ 时，必 $x>0, y>0$ 。条件

$$
\frac{\pi}{2}<\arcsin x+\arcsin y \leqslant \pi,
$$

即

$$
\arcsin x>\frac{\pi}{2}-\arcsin y
$$

两端取正弦，即得 $x^{2}+y^{2}>1$ 。
情形： $-\pi \leqslant u<-\frac{\pi}{2}$ ，
在这种情形下必 $x<0, y<0$ 。条件
$-\pi \leqslant \arcsin x+\arcsin y<-\frac{\pi}{2}$,
即

$$
\frac{\pi}{2}<\arcsin (-x)+\arcsin (-y) \leqslant \pi
$$

因此，即 $x^{2}+y^{2}>1$ 。
总之，当 $x y \leqslant 0$ 或 $x y>0$ 但 $x^{2}+y^{2} \leqslant 1$ 时，必有 $-\frac{\pi}{2}$ $\leqslant u \leqslant \frac{\pi}{2} ;$ 当 $x>0, y>0, x^{2}+y^{2}>1$ 时，必 $\frac{\pi}{2}<u \leqslant \pi$ ；当 $x$ $<0, y<0, x^{2}+y^{2}>1$ 时，必 $-\pi \leqslant u<-\frac{\pi}{2}$ 。

但当 $-\frac{\pi}{2} \leqslant u \leqslant \frac{\pi}{2}$ 时， $u=v$ ；当 $\frac{\pi}{2}<u \leqslant \pi$ 时， $u=\pi-$ $v_{0}$ 当 $-\pi \leqslant u<-\frac{\pi}{2}$ 时， $u=-\pi-v$ 。

## 因此，最后得

$\arcsin x+\arcsin y$
$\int \arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right)$ ，
若 $x y \leqslant 0$ 或 $x^{2}+y^{2} \leqslant 1$ ；
$=\left\{\begin{array}{c}\pi-\arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right), \\ \text { 若 } x>0, y>0, x^{2}+y^{3}>1 ; \\ -\pi-\arcsin \left(x \sqrt{1-y^{2}}+y \sqrt{1-x^{2}}\right),\end{array}\right.$
其 $x<0, y<0 ; x^{2}+y^{2}>1$.
即
$\arcsin x+\arcsin y$
$=(-1) \operatorname{srcsin}\left(x \sqrt{1-y^{2}}+y \sqrt{1-x}\right)+\varepsilon \pi$,
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-444.jpg?height=138&width=1001&top_left_y=2058&top_left_x=322)

$$
(|x| \leqslant 1,|y| \leqslant 1)
$$

778. 证明反余弦相加的定理：
$\arccos x+\arccos y$
$=(-1)^{\operatorname{arc}} \cos \left(x y-\sqrt{1-x^{2}} \sqrt{1-y^{2}}\right)+2 \varepsilon \pi$

$$
(|x| \leqslant 1,|y| \leqslant 1)
$$

其中, 若 $x+y \geqslant 0, \varepsilon=0$ ；若 $x+y<0, \varepsilon=1$.
证 由基本的不等式
$0 \leqslant \arccos x \leqslant \pi \quad$ 及 $\quad 0 \leqslant$ arc cos $y \leqslant \pi$ ，
有 $0 \leqslant a r e \cos x+\operatorname{arc} \cos y \leqslant 2 \pi$.
若 $\quad 0 \leqslant \arccos x+\arccos y \leqslant \pi$ ，
则 arc cos $x \leqslant \pi-\arccos y$.
由于 arccos $x$ 及 $\pi$ —arcecs $y$ 都含在 $[0, \pi]$ 内，而在此区间内余弦是减画数，故有

$$
x \geqslant \cos (\pi-\operatorname{arc} \cos y)=-y,
$$

即

$$
x+y \geqslant 0
$$

同法可证得：若
$\pi<\arccos x+\arccos y \leqslant 2 \pi$,
则

$$
x+y<0
$$

又由于
$\cos (\arccos x+\arccos y)=x y-\sqrt{1-x^{2}} \sqrt{1-y^{2}}$,故知

$$
u=\arccos x+\arccos y
$$

及 $\quad v=\arccos \left(x y-\sqrt{1-x^{2}} \cdot \sqrt{1-y^{2}}\right)$
有同一的余弦. 因 $v$ 始终在 0 与 $\pi$ 之间，故知：
若 $0 \leqslant u \leqslant \pi$, 则 $u=u$; 若 $\pi<u \leqslant 2 \pi$, 则 $u=2 \pi-v$ 。
因此，最后得
arc $\cos x+$ arc $\cos y$

$$
=\left\{\begin{array}{l}
\arccos \left(x y-\sqrt{1-x^{2}} \sqrt{1-y^{2}}\right), \\
\quad \text { 若 } x+y \geqslant 0 ; \\
2 \pi-\arccos \left(x y-\sqrt{1-x^{2}} \sqrt{1-y^{2}}\right), \\
\text { 若 } x+y<0,
\end{array}\right.
$$

此即所行证明的公式。
779. 作函数的图形：
（a） $y=\arcsin x-\arcsin \sqrt{1-x^{2}}$;
(6) $y=\arcsin 2 x \sqrt{1-x^{2}}-2 \arcsin x$.

解 (a)利用 777 题的结果得知：
由于 $x^{2}+\left(-\sqrt{1-x^{2}}\right)^{2}=1$ ，故
$y=\arcsin x+\arcsin \left(-\sqrt{1-x^{2}}\right)$

$$
\begin{aligned}
& =\arcsin \left(x \sqrt{1-\left(1-x^{2}\right)}-\sqrt{1-x^{2}} \sqrt{1-x^{2}}\right) \\
& =\arcsin \left(x|x|-1+x^{2}\right)
\end{aligned}
$$

当 $-1 \leqslant x \leqslant 0$ 时， $y=-\frac{\pi}{2}$ ；当 $0<x \leqslant 1$ 时， $y=\arcsin$ （ $2 x^{2}-1$ ）。可以证明，
$\arcsin \left(2 x^{2}-1\right)-2 \arcsin x=-\frac{\pi}{2}$, 故有

$$
y=\left\{\begin{array}{l}
-\frac{\pi}{2}, \text { 当 }-1 \leqslant x \leqslant 0 \text { 时, } \\
2 \arcsin x-\frac{\pi}{2}, \text { 当 } 0<x \leqslant 1 \text { 时, }
\end{array}\right.
$$

如图1 - 314 所示。
（6）由于
2 arc $\sin x=\arcsin x+\arcsin x$

$$
=\left\{\begin{array}{l}
\arcsin \left(2 x \sqrt{1-x^{2}}\right), \text { 若 }|x| \leqslant \frac{1}{\sqrt{2}} ; \\
\pi \operatorname{sgn} x-\arcsin \left(2 x \sqrt{1-x^{2}}\right), \text { 若 }|x|>\frac{1}{\sqrt{2}},
\end{array}\right.
$$

故当 $-1 \leqslant x<-\frac{1}{\sqrt{2}}$ 时, $y=-(\pi+4 \arcsin x)$ ；

$$
\text { 当 }-\frac{1}{\sqrt{2}} \leqslant x \leqslant \frac{1}{\sqrt{2}} \text { 时， } y=0 \text { ； }
$$

当 $\frac{1}{\sqrt{2}}<x \leqslant 1$ 时， $y=\pi-4 \arcsin x$.
如图1－315所示。
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-447.jpg?height=609&width=578&top_left_y=1323&top_left_x=382)

图 1.314
![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-447.jpg?height=664&width=506&top_left_y=1253&top_left_x=1135)

图1.315
780. 函数 $y=y(x)$ 由下面的方程给出：

$$
x=\operatorname{arctg} t, y=\operatorname{arcctg} t \quad(-\infty<t<+\infty),
$$

求此函数. 在怎样的域上此函数才有定义？
解 由条件 $-\frac{\pi}{2}<x<\frac{\pi}{2}, 0<y<\pi$ 且

$$
\operatorname{tg} x=t, \operatorname{ctg} y=t,
$$

即得

$$
\operatorname{ctg} y=\operatorname{tg} x=\operatorname{ctg}\left(\frac{\pi}{2}-x\right),
$$

从而当 $-\frac{\pi}{2}<x<\frac{\pi}{2}$ 时, 有

$$
y=\frac{\pi}{2}-x
$$

781. 设

$$
x=\operatorname{ch} t, y=\operatorname{sh} t \quad(-\infty<t<+\infty)
$$

参数 $t$ 变化的域怎样，即可枫变数 $y$ 为变数 $x$ 的单值函数？求在各个域上 $y$ 的表示式。
解 由于 $x=\mathrm{ch} t, y=\mathrm{sh} t$ ，故

$$
x^{2}-y^{2}=\operatorname{ch}^{2} t-\operatorname{sh}^{2} t=1
$$

当 $\mathrm{sh} t=\frac{e^{t}-e^{-t}}{2} \geqslant 0$ 时, 即 $e^{t} \geqslant e^{-t}$ 或 $e^{2 x} \geqslant 1$ 或 $t \geqslant 0$ 时,

$$
y=\sqrt{x^{2}-1}
$$

当 $t \leqslant 0$ 时, $y=-\sqrt{x^{2}-1}$.
不论 $t$ 为何值， $x \geqslant 1$ ，故 $\sqrt{x^{2}-1}$ 有意义. $t=0$ 是函数 $y$ $=y(x)$ 单值区域的分界值。

## 782. 要使方程组

$$
x=\varphi(t), \quad y=\psi(t)
$$

把 $y$ 定义为 $x$ 的单值函数的必要而且充分的条件是甚公？
解 其必要而且充分的条件为，使 $\varphi(t)=x$ 的一切 $t$ 值，函数 $\phi(t)$ 应有同一的值。下面加以证明。先证必要性。若不然，则存在 $x^{*}$ 及 $t_{1} \neq t_{2}$ ，使

$$
\varphi\left(t_{1}\right)=\varphi\left(t_{2}\right)=x^{*} \text { 且 } \psi\left(t_{1}\right) \neq \psi\left(t_{2}\right) \text {, }
$$

于是，对于这样的 $x^{*}$ ，一方面有 $y_{1}=\psi\left(t_{1}\right)$ 及 $y_{2}=\psi\left(t_{2}\right)$ ，

另一方面又有 $y_{1} \neq y_{2}$ ，这样 $y$ 就不定义为 $x$ 的单值函数.因此，使 $\varphi(t)=x$ 的一切 $t$ 值， $\psi(t)$ 应有同一的值。

再证充分性. 设所述条件满足，则对于任一 $x^{*} \in$ $\{\varphi(t)\}$ ，有 $t^{\prime \prime}$ 使

$$
\varphi\left(t^{*}\right)=x^{*}, \quad \psi\left(t^{+}\right)=y^{*}
$$

有意义，这样定义的函数 $y=y(x)$ 不因 $t^{*}$ 的不同选取而不同，因此它由 $x^{*}$ 唯一确定，从而 $y$ 定义为 $x$ 的单值函数。
783. 在怎样的条件下，二方程组

$$
x=\varphi(t), \quad y=\phi(t) \quad(a<t<b)
$$

及 $\quad x=\varphi[\chi(\tau)], y=\phi[\chi(\tau)] \quad(\alpha<\tau<\beta)$
定义出同一的函数 $y=y(x) ?$
解 当 $\alpha<\tau<\beta$ 时,函数 $\chi(\tau)$ 的值的集应为区间（ $\alpha$ ， b).
784. 设函数 $\varphi(x)$ 和 $\phi(x)$ 在区间 $(a, b)$ 内有定义并且是连续的，且

$$
A=\inf _{c<x<b} \varphi(x), \quad B=\sup _{\Delta<x<b} \varphi(x) .
$$

在怎样的场合下，有定义在区间 $(A, B)$ 上的单值函数 $f(x)$ ，使得

$$
\text { 当 } a<x<b \text { 时, } \psi(x)=f[\varphi(x)] \text { ? }
$$

解 显然，要求对于使 $\varphi(x)=u$ 的一切 $x$ 值（其中 $u$ 为区间（ $A, B$ ）中的任一给定的数），函数 $\psi(x)$ 应取同一的值. 满足了这个条件就可以了。这时，对 $u \in(A, B)$ 可定义

$$
f(u)=\psi(x),
$$

其中 $x$ 为满足 $\varphi(x)=u(a<x<b)$ 的任何数. 上述条件

保证了这样定义的 $f(u)$ 是单值的.

## § 9. 函数的一致连续性

$1^{0}$. 致连续性的定义 若对于每一个 $\varepsilon>0$ 都存在有 $\delta=$ $\delta(\varepsilon)>0$ ，且对于使 $f(x)$ 有意义的任何数值 $x^{\prime} x^{\prime \prime} \in X$ ，由不等式

$$
\left|x^{\prime}-x^{n}\right|<\delta
$$

可得不等式

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon,
$$

则称函数 $f(x)$ 在已殒集合（区间、线段等） $X=\{x\}$ 上为一致连续的。
$2^{\circ}$ 康托尔定理 在有界的闭区问 $[a, b]$ 上有定义的连续函数 $f(x)$ 在此仏区间上一致连续。
785. 某工厂的车问制造正方形薄板，其边 $x$ 可取由 1 厘米到 10 厘米之间的值. 为了使不论何种边长（在上述的范围内）的薄板的面积 $y$ 与原设计的面积差皆小于 $\varepsilon$ ，问可以多大的公差 $\delta$ 对这些薄板的边长加工，设（a） $\varepsilon=1$ 平方厘米， (6) $\varepsilon=0.01$ 平方厘米； $(\mathrm{B}) \epsilon=0.0001$ 平方厘米，计算 $\delta$ 的值.
解 $y=x^{2}$ 。由于，

$$
\left|x^{\prime 2}-x^{\prime 2}\right|=\left|x^{\prime}-x^{\prime \prime}\right|\left|x^{\prime}+x^{\prime \prime}\right| \leqslant 20\left|x^{\prime}-x^{\prime \prime}\right|,
$$

于是对于任给的 $\epsilon>0$ ，要 $\left|x^{\prime 2}-x^{\prime 2}\right|<\varepsilon$ 时，只要 $\mid x^{\prime}-$ $x^{\prime \prime} \left\lvert\,<\frac{\varepsilon}{20}\right.$ 即可。

干是，在加工薄板边长时，只要取公差 $\delta \leqslant \frac{\varepsilon}{20}$ ，当 $\mid x^{\prime}-$ $x^{\prime \prime} \mid<\delta$ 时，即可满足要求。
（a）当 $\varepsilon=1$ 厘米 $^{2}$ 时， $\delta \leqslant \frac{1}{20}=0.05$ 厘米 $=0.5$ 毫米；
（ 6 ）当 $\varepsilon=0.01$ 厘米 $^{2}$ 时， $\delta \leqslant \frac{0.01}{20}=0.0005$ 厘米
$=0.005$ 毫米；
（B）当 $\epsilon=0.0001$ 厘米 $^{2}$ 时， $\delta \leqslant \frac{0.0001}{20}$
$=0.000005$ 厘米 $=0.00005$ 毫米.
786. ${ }^{+}$圆柱形勒简之宽度为 $\boldsymbol{\varepsilon}$ ，长度为 $\delta$ ，将鞘筒套在曲线 $y=$ $\sqrt[3]{x}$ 上且沿此曲线滑动，但筒之轴须保持平行于 $O x$ 轴。为了使此筒顺利地经过此曲线上由不等式 $-10 \leqslant x \leqslant$ 10 所限定的部分，问 $\delta$ 应等于甚么？设（a） $\varepsilon=1$ ；( ( $) \varepsilon=$ $0.1 ;(\mathrm{B}) \varepsilon=0.001 ;(\mathrm{r}) \varepsilon$ 为任意小数。
解 $y=\sqrt[3]{x}$ ，对于 $y^{\prime} \neq y^{\prime \prime}$ ，由于

$$
\begin{aligned}
\left|y^{\prime}-y^{\prime \prime}\right| & =\left|\frac{y^{\prime 3}-y^{\prime \prime 3}}{y^{\prime 2}+y^{\prime} y^{\prime \prime}+y^{\prime \prime 2}}\right| \\
& =\left|\frac{y^{\prime 3}-y^{\prime 33}}{\frac{3}{4}\left(y^{\prime}+y^{\prime \prime}\right)^{2}+\frac{1}{4}\left(y^{\prime}-y^{\prime \prime}\right)^{2}}\right| \\
& \leqslant \frac{\left|y^{\prime 3}-y^{\prime \prime 3}\right|}{\frac{1}{4}\left|y^{\prime}-y^{\prime \prime}\right|^{2}}
\end{aligned}
$$

即

$$
\frac{1}{4}\left|y^{\prime}-y^{\prime \prime}\right|^{3} \leqslant\left|y^{\prime 3}-y^{\prime 3}\right|=\left|x^{\prime}-x^{\prime \prime}\right| \text { 或 } \mid y^{\prime}-
$$

$y^{\prime \prime} \mid \leqslant \sqrt[3]{4\left|x^{\prime}-x^{\prime \prime}\right|}$ 。对于任给的 $\varepsilon>0$, 要 $\left|y^{\prime}-y^{\prime \prime}\right|<$ $\varepsilon$, 只要 $4\left|x^{\prime}-x^{\prime \prime}\right|<\varepsilon^{3}$, 或 $\left|x^{\prime}-x^{\prime \prime}\right|<\frac{\varepsilon^{3}}{4}$ 即可。

取 $0<\delta<\frac{\varepsilon^{3}}{4}$, 则当 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta$ 时, 恒有

$$
\left|\sqrt[3]{x^{T}}-\sqrt[3]{x^{17}}\right|<\varepsilon
$$

（a）当 $\varepsilon=1$ 时， $\delta<\frac{1}{4}$ ；
（6）当 $\varepsilon=0.1$ 时， $\delta<2.5 \times 10^{2}$ ；
（B）当 $\mathrm{E}=0.001$ 时， $\delta<2.5 \times 10^{-79}$ ；
（ $\Gamma$ ）当 $\varepsilon$ 为任意小数时， $\delta<\frac{\epsilon^{3}}{4}(\varepsilon \leqslant 1)$ 。
787. 以《 $\varepsilon-\delta\rangle$ 的说法在肯定的意义上表达下面论断的意义;函数 $f(x)$ 在某集合（区间，线段）上连续，但在此集合上并不一致连续。
解 设集合为 $\boldsymbol{E}$ 。所需论断的《 $\varepsilon-\delta$ 》说明如下：对于任给的 $\varepsilon>0$ ，及 $x_{0} \in E$ ，总存在一个数 $\delta\left(E_{1}, x_{0}\right)>0$ ，使当 $\left|x-x_{0}\right|<\delta\left(\varepsilon, x_{0}\right)$ 时,恒有

$$
|f(x)-f(x 0)|<\varepsilon .
$$

同时，至少存在一个 $\varepsilon_{0}>0$ ，使对于任意给定的 $\delta>0$ ，都可找到 $x_{1}, x_{2} \in E$ ，满足 $\left|x_{1}-x_{2}\right|<\delta$ ，但是

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \geqslant \varepsilon_{0} .
$$

7B8. 证明：函数

$$
f(x)=\frac{1}{x}
$$

在区间 $(0,1)$ 上是连续的，但在此区间上并非一致连续的。
证 连续性是显然的，现证其不一致连续. 考虑（ 0,1 ）上的两串点

$$
x_{n}=\frac{1}{n}, \quad x_{x}^{\prime}=\frac{1}{n+1}
$$

则当 $0<\varepsilon_{0}<1$ 时，不论 $\delta>0$ 取得多小，只要 $n$ 取得充分大,总可以使

$$
\left|x_{t}-x_{n}{ }^{\prime}\right|=\frac{1}{n(n+1)}<\delta
$$

但是，

$$
\left|f\left(x_{n}\right)-f\left(x_{n}{ }^{\prime}\right)\right|=1>\varepsilon_{0} .
$$

因而， $f(x)=\frac{1}{x}$ 在 $(0,1)$ 上并非一致连续。
789. 证明：函数

$$
f(x)=\sin \frac{\pi}{x}
$$

在区间 $(0,1)$ 上是连续的并且有界，但在比区间上并非 - - 致连续的。

证 当 $x \neq 0$ 时，由基本初等函数在其定义域的连续性可知， $f(x)$ 是连续的，同时，由于 $|f(x)| \leqslant 1$ ，因而它也是有界的。

现考虑 $(0,1)$ 上的两多点 $x_{n}=\frac{2}{n}, x_{n}{ }^{\prime}=\frac{2}{n+1}$, 则当 $0<\varepsilon_{0}<1$ 时，不论 $\delta>0$ 取得多小，只要 $n$ 充分大，总可以使

$$
\left|x_{n}-x_{n}{ }^{\prime}\right|=\frac{2}{n(n+1)}<\delta,
$$

但是

$$
\left|f\left(x_{n}\right)-f\left(x_{n^{\prime}}\right)\right|=1>\varepsilon_{0} .
$$

因而， $f(x)$ 在 $(0,1)$ 上并非一致连续。
790. 证明：函数

$$
f(x)=\sin x^{2}
$$

在无穷区间 $-\infty<x<+\infty$ 上是连续的并且有界，但在此区间上并非一致连续的。
证 函数 $f(x)$ 的连续性及其有界性是显然的. 现证其

## 不一致连续性。

考虑 $(-\infty,+\infty)$ 上的两串点

$$
x_{n}=\sqrt{\frac{n \pi}{2}}, \quad x_{n}{ }^{\prime}=\sqrt{\frac{(n+1) \pi}{2}} .
$$

则当 $0<\varepsilon_{0}<1$ 时, 不论 $\delta>0$ 如何选取, 只要 $n$ 充分大,总可以使

$$
\left|x_{n}-x_{n}{ }^{\prime}\right|=\frac{\frac{\pi}{2}}{\sqrt{\frac{n \pi}{2}}+\sqrt{\frac{n+1}{2} \pi}}<\delta,
$$

但是，

$$
\left|f\left(x_{n}\right)-f\left(x_{n}{ }^{\prime}\right)\right|=1>\varepsilon_{0} .
$$

因而， $f(x)$ 在 $(-\infty,+\infty)$ 上并非一致连续.
791. 证明: 若函数 $f(x)$ 在域 $a \leqslant x<+\infty$ 上有定义并且是连续的，而且

$$
\lim _{x \rightarrow+\infty} f(x)
$$

存在，则 $f(x)$ 在此域上是一致连续的。
证 任给 $\varepsilon>0$. 由于 $\lim _{\pi \rightarrow+\infty} f(x)$ 存在，故必存在 $X>a$ ，使当 $x^{\prime}>X, x^{\prime \prime}>X$ 时，恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon .
$$

由于 $f(x)$ 在 $[a, X+1]$ 连续，故一致连续，从而必有正数 $\delta^{\prime}$ 存在, 使当 $x^{\prime} \in[a, X+1], x^{\prime \prime} \in[a, X+1], \mid x^{\prime}$ $-x^{\prime \prime} \mid<\delta^{\prime}$ 时, 恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon,
$$

令 $\delta=\min \left\{\delta^{\prime}, 1\right\}$ 。现设 $x^{\prime}, x^{\prime \prime}$ 为满足 $\alpha \leqslant x^{\prime}<+\infty, \alpha$ $\leqslant x^{\prime \prime}<+\infty,\left|x^{\prime}-x^{\prime \prime}\right|<\delta$ 的任何两点. 由于 $\left|x^{\prime}-x^{\prime \prime}\right|$
$<\delta$ ，故 $x^{\prime}$ 与 $x^{\prime \prime}$ 或同时属于 $[a, X+1]$ ，或同时满足 $x^{\prime}$ $>X, x^{\prime \prime}>X$ 。因此，恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon,
$$

故 $f(x)$ 在 $a \leqslant x<+\infty$ 上一致连续. 证毕.
792. 证明：无界函数

$$
f(x)=x+\sin x
$$

于全轴 $-\infty<x<+\infty$ 上一致连续。
证 $\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|=\mid\left(x^{\prime}-x^{\prime \prime}\right)+\left(\sin x^{\prime}-\right.$ $\left.\sin x^{\prime \prime}\right) \mid$

$$
\leqslant\left|x^{\prime}-x^{\prime \prime}\right|+\left|\sin x^{\prime}-\sin x^{\prime \prime}\right| \leqslant 2\left|x^{\prime}-x^{\prime \prime}\right| .
$$

对于任给的 $\varepsilon>0$, 取 $\delta=\frac{\epsilon}{2}>0$, 则当 $-\infty<x^{\prime}<$ $+\infty,-\infty<x^{\prime \prime}<+\infty,\left|x^{\prime}-x^{\prime \prime}\right|<\delta$ 时, 恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon,
$$

故 $f(x)$ 在 $-\infty<x<+\infty$ 上一致连续.
793. 函数 $f(x)=x^{2}$ 在下列区间中是否为一致连续的：（a）（一 $l, l$ ), 这里 s 为随便多大的正数；（6）在区间（ $-\infty,+\infty$ ）上?
解 当 $x_{1}, x_{2} \in(-l, l)$ 时，

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \leqslant 2 I\left|x_{1}-x_{2}\right| .
$$

对于任给的 $\varepsilon>0$, 取 $\delta=\frac{\varepsilon}{2 l}$, 则当 $\left|x_{1}-x_{2}\right|<\delta$, 且 $x_{1}$, $x_{2} \in(-l, l)$ 时, 恒有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon,
$$

故 $f(x)$ 在 $(-l, l)$ 上一致连续。
（6）取 $\epsilon_{0}=1$ ，不论 $\delta>0$ 取得歹小，只要 $n$ 充分大，我们总可以使 $x^{\prime}{ }_{n}=n+\frac{1}{n}, x^{\prime \prime}{ }_{n}=n$ 的埋离 $\left|x_{n}{ }^{\prime}-x_{n}{ }^{n}\right|$
$=\frac{1}{n}<\delta$, 但是,

$$
\left\lvert\, f\left(x_{\mathrm{n}}^{\prime}\right)-f\left(x_{n}^{\prime \prime}\right)_{1}=2+\left(\frac{1}{n}\right)^{2}>\varepsilon_{0}\right.
$$

可见 $f(x)$ 在 $(-\infty,+\infty)$ 上非一數连续。
研究下列函数在已知域上的一致连续性：
794. $f(x)=\frac{x}{4-x^{2}}(-1 \leqslant x \leqslant 1)$.

解 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\left|\frac{x_{1}}{4-x^{2}}-\frac{x_{2}}{4-x_{2}^{2}}\right|$

$$
=\left|\frac{4+x_{1} x_{2}}{\left(4-x_{1}^{2}\right)\left(4-x_{2}^{2}\right)}\right|\left|x_{1}-x_{2}\right|
$$

由于 $\left|\frac{4+x_{1} x_{2}}{\left(4-x_{1}^{2}\right)\left(4-x_{2}^{2}\right)}\right|<\frac{4+1}{3 \cdot 3}=\frac{5}{9}<1$,
故对于任给的 $\varepsilon>0$ ，取 $\delta=\varepsilon$ ，则对满足 $\left|x_{1}-x_{2}\right|<\delta$ 的 $x_{1}, x_{2}\left(x_{1}, x_{2}\right.$ 属于（ $\left.-1,1\right]$ ）值，均有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon .
$$

因而 $f(x)$ 在区间 $[-1,1]$ 上一致连续.
795. $f(x)=\ln x(0<x<1)$.

解 考虑 $x_{n}=\frac{1}{n}, x_{n}^{\prime}=\frac{1}{2 n}$ ，则当 $0<\varepsilon_{0}<\ln 2$ 时，不论 $\delta$ 如何选取，只要 $n$ 充分大，我们总可以使

$$
\left|x_{n}-x_{n}^{\prime}\right|=\frac{1}{2 n}<\delta,
$$

但是，

$$
\left|f\left(x_{n}\right)-f\left(x^{\prime}{ }_{n}\right)\right|=\ln 2>\varepsilon .
$$

因而 $f(x)$ 在区间 $(0,1)$ 内并非一致连续.
796. $f(x)=\frac{\sin x}{x}(0<x<\pi)$.

解 由于 $\lim _{x \rightarrow 0} \frac{\sin x}{x}=1$ ，我们定义函数

$$
F(x)=\left\{\begin{array}{rc}
1 & , x=0 \\
\frac{\sin x}{x} & 0<x<\pi \\
0 & x=\pi
\end{array}\right.
$$

易见 $F(x)$ 在 $[0, \pi]$ 上连续，根据康托尔定理便知， $F(x)$在 $[0, \pi]$ 上一致连续，从而 $f(x)$ 也在 $(0, \pi)$ 上一致连续。 797. $f(x)=e^{x} \cos \frac{1}{x}(0<x<1)$.

解 取 $\varepsilon_{i l}=1$ ，令 $x_{n}=\frac{2}{(2 n+1) \pi}, x_{n}{ }^{\prime}=\frac{1}{n \pi}(n$ 为正整数），显然 $x_{n} 、 x_{n}^{\prime}$ 均属于（ 0,1 ）。不论 $\delta>0$ 取得多么小，只要 $n$ 充分大，总有

$$
\left|x_{n}-x_{n}^{\prime}\right|=\frac{1}{(2 n+1) n \pi}<\delta \text {, }
$$

但是，

$$
\left|f\left(x_{n}\right)-f\left(x^{\prime}{ }_{n}\right)\right|=e^{\frac{1}{n}}>1=\varepsilon_{0} .
$$

因而 $f(x)=e^{x} \cos \frac{1}{x}$ 在 $(0,1)$ 上非一致连续。
798. $f(x)=\operatorname{arctg} x(-\infty<x<+\infty)$.

解 由于 $f(x)$ 在区间 $(-\infty, 1] 、[0,+\infty)$ 上连紏，且有

$$
\lim _{x \rightarrow+\infty} \operatorname{arc} \operatorname{tg} x=\frac{\pi}{2}, \lim _{x \rightarrow-\infty} \operatorname{arc} \operatorname{tg} x=-\frac{\pi}{2},
$$

由 791 题知 $f(x)$ 在 $[0,+\infty)$ 及 $(-\infty, 1]$ 上均一致连续。

于是, 对于任给的 $\varepsilon>0$, 存在 $\delta_{1}(\varepsilon)>0$, 当 $x_{1} 、 x_{2} \in$ $(-\infty, 1],\left|x_{1}-x_{2}\right|<\delta_{1}(\varepsilon)$ 时, 恒有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon
$$

成立。
又存在 $\delta_{2}(\varepsilon)>0$ ，当 $x_{1}, x_{2} \in(0,+\infty),\left|x_{1}-x_{2}\right|<$ $\delta_{2}(\varepsilon)$ 时, 恒有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon
$$

成立。
今取 $\delta(\varepsilon)=\min \left\{1, \delta_{1}(\varepsilon), \delta_{2}(\varepsilon)\right\}$, 则当 $x_{1}, x_{2} \in(-$ $\infty,+\infty),\left|x_{1}-x_{2}\right|<\delta(\varepsilon)$ 时， $x_{1}$ 与 $x_{2}$ 必或同时属于 $(-\infty, 1]$ ，或同时属于 $\{0,+\infty)$ ，故恒有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon,
$$

即 $f(x)$ 在 $(-\infty,+\infty)$ 上 一致连续。
799. $f(x)=\sqrt{x}(1 \leqslant x<+\infty)$.

解 考虑 $\left[1,+\infty\right.$ ) 内任意两点 $x_{1}, x_{2}$.

$$
\left|\sqrt{x_{1}}-\sqrt{x_{2}}\right|=\left|\frac{x_{1}-x_{2}}{\sqrt{x_{1}}+\sqrt{x_{2}}}\right| \leqslant \frac{\left|x_{1}-x_{2}\right|}{2} .
$$

于是, 对于任给的 $\varepsilon>0$, 取 $\delta=2 \varepsilon$, 则当 $\left|x_{1}-x_{2}\right|<\delta$, $x_{1}, x_{2} \in(1,+\infty)$ 时, 恒有

$$
\left|\sqrt{x_{1}}-\sqrt{x_{2}}\right|<\frac{1}{2} \cdot 2 \varepsilon=\varepsilon
$$

因而 $f(x)=\sqrt{x}$ 在区间( $1,+\infty$ )上一致连续. 800. $f(x)=x \sin x(0 \leqslant x<+\infty)$.

解 考虑点 $x_{n}=2 n \pi+\frac{1}{n}, x_{*}{ }^{\prime}=2 n \pi$, 则

$$
\left|x_{n}-x_{n}^{\prime}\right|=\frac{1}{n}
$$

而

$$
\begin{gathered}
\left|f\left(x_{n}\right)-f\left(x_{n}^{\prime}\right)\right|=\left(2 \pi \pi+\frac{1}{n}\right) \sin \frac{1}{n} \\
=2 n \pi \sin \frac{1}{n}+\frac{1}{n} \sin \frac{1}{n}
\end{gathered}
$$

由于

$$
\lim _{n \rightarrow \infty} \frac{1}{n} \sin \frac{1}{n}=0,
$$

及 $\lim _{n \rightarrow \infty} 2 n \pi \sin \frac{1}{n}=\lim _{n \rightarrow \infty}\left(2 \pi \cdot \frac{\sin \frac{1}{n}}{\frac{1}{n}}\right)=2 \pi$,
所以，

$$
\left|f\left(x_{n}\right)-f\left(x_{n}^{\prime}\right)\right| \rightarrow 2 \pi \quad(n \rightarrow \infty) .
$$

现取 $\varepsilon_{0}=2 \pi-1$. 于是，不论 $\delta>0$ 取得多么小，只要 $n$ 充分大, 总有 $\left|x_{n}-x_{n}{ }^{\prime}\right|<\delta$, 并且

$$
\left|f\left(x_{n}\right)-f\left(x_{n}^{\prime}\right)\right|>\varepsilon_{0}=2 \pi-1 .
$$

因而 $f(x)=x \sin x$ 在区间 $[0,+\infty)$ 上非一致连续.
801. 证明：函数 $f(x)=\frac{|\sin x|}{x}$ 在每个区间

$$
J_{1}=(<1<x<0) \text { 及 } J_{2}=(0<x<1)
$$

上是一致连续的，但在它们的和

$$
J_{1}+J_{2}=\{0<|x|<1\}
$$

上并非一致连续的.
证 在 $J_{1}=(-1<x<0)$ 上 $f(x)=-\frac{\sin x}{x}$, 在 $J_{2}=$ $(0<x<1)$ 上 $f(x)=\frac{\sin x}{x}$ ，它们的一致连续性由 796 题可知.
由于

$$
\begin{aligned}
& \lim _{x \rightarrow+\infty} f(x)=\lim _{x \rightarrow+\infty} \frac{\sin x}{x}=1, \\
& \lim _{x \rightarrow-0} f(x)=-\lim _{x \rightarrow-0} \frac{\sin x}{x}=-1,
\end{aligned}
$$

故必存在 $\eta>0(\eta<1)$, 使当 $0<x_{1}<\eta, 一 \eta<x_{2}<0$

时恒有 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|>1$. 现取 $\varepsilon_{0}=1$, 则不论 $\delta>0$取得多么小,都可取两点 $x_{1}{ }^{\prime}$ 种 $x_{2}{ }^{\prime}$, 使 $0<x_{1}{ }^{\prime}<\min \{\eta$, $\left.\frac{\delta}{2}\right\},-\min \left\{\eta, \frac{\delta}{2}\right\}<x_{2}{ }^{\prime}<0$ 。于是 $\left|x_{1}{ }^{\prime}-x_{2}{ }^{\prime}\right|<\delta$, 但是，

$$
\left|f\left(x_{1}^{\prime}\right)-f\left(x_{2}^{\prime}\right)\right|>\varepsilon_{p}=1 .
$$

由此可知 $f(x)$ 在 $J_{1}+J_{z}=\{0<|x|<1\}$ 上非一致连续。
802. 对于 $\varepsilon>0$ ，求使函数 $f(x)$ 在已知区间上满足一致连续的条件的 $\delta=\delta(\varepsilon)$ （任何的!）设：
(a) $f(x)=5 x-3 \quad(-\infty<x<+\infty)$;
(6) $f(x) x^{2}-2 x-1 \quad(-2 \leqslant x \leqslant 5)$;
(B) $f(x)-\frac{1}{x} \quad(0.1 \leqslant x \leqslant 1) ;$
(г) $f(x)=\sqrt{x} \quad(0 \leqslant x<+\infty)$;
(л) $f(x)=2 \sin x-\cos x \quad(-\infty<x<+\infty)$;
(e) $f(x)=x \sin \frac{1}{x}(x \neq 0)$ 及 $f(0)=0(0 \leqslant x \leqslant \pi)$.

艪（a） $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=5\left|x_{1}-x_{2}\right|$.
只需取 $\delta=\frac{E}{5}$ 即行。

$$
\text { (б) }\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\left|x_{1}-x_{2}\right| \cdot\left|x_{1}+x_{2}-2\right| \text {. }
$$

由于 $-2 \leqslant x \leqslant 5$, 故 $\left|x_{1}+x_{2}-2\right| \leqslant 8$ ，于是只需取 $\delta$ $=\frac{\varepsilon}{8}$ 即行。

$$
\text { (в) }\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\frac{\left|x_{1}-x_{2}\right|}{x_{1} x_{2}} \leqslant \frac{\left|x_{1}-x_{2}\right|}{0.01} \text {. }
$$

只需取 $\delta=0.01 \varepsilon$ 。
（г）对于 $a \geqslant 0, b \geqslant 0$ ，显然有不等式 $\sqrt{a+b} \leqslant \sqrt{a}+\sqrt{b}$
成立。
对于任给的 $\mathrm{\varepsilon}>0$, 取 $\delta=\mathrm{\varepsilon}^{2}$, 则当 $\left|x_{1}-x_{2}\right|<\delta, x_{1}$ 、 $x_{2} \in(0,+\infty)$ 时,

$$
\sqrt{x_{1}}<\sqrt{x_{2}+\delta} \leqslant \sqrt{x_{2}}+\sqrt{\delta}=\sqrt{x_{2}}+\varepsilon ;
$$

同理可有

$$
\sqrt{x_{2}}<\sqrt{x_{1}+\delta} \leqslant \sqrt{x_{1}}+\sqrt{\delta}=\sqrt{x_{1}}+\varepsilon
$$

则恒有

$$
\left|\sqrt{x_{1}}-\sqrt{x_{2}}\right|<\varepsilon .
$$

(л) $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \leqslant 2\left|\sin x_{1}-\sin x_{2}\right|+\mid \cos x_{1}-$ $\cos x_{2}$

$$
\left.\leqslant 2\left|x_{1}-x_{2}\right|+\left|\left(\frac{\pi}{2}-x_{1}\right)-\left(\frac{\pi}{2}-x_{3}\right)\right|=3 \right\rvert\, x_{1}-
$$

$x_{2}$
只需取 $\delta=\frac{E}{3}$.
（c）任给 $\varepsilon>0$ 。当 $x_{1}, x_{2} \in\left(\frac{\varepsilon}{3}, \pi\right)$ 时，有

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\left|x_{1} \sin \frac{1}{x_{1}}-x_{2} \sin \frac{1}{x_{2}}\right|
$$

$$
\begin{aligned}
& =\left|x_{1} \sin \frac{1}{x_{1}}-x_{1} \sin \frac{1}{x_{2}}+x_{1} \sin \frac{1}{x_{2}}-x_{2} \sin \frac{1}{x_{2}}\right| \\
& \leqslant\left|x_{1}\right| \cdot\left|\sin \frac{1}{x_{1}}-\sin \frac{1}{x_{2}}\right|+\left|x_{1}-x_{2}\right| \cdot\left|\sin \frac{1}{x_{2}}\right| \\
& \leqslant\left|x_{1}\right| \cdot\left|\frac{1}{x_{1}}-\frac{1}{x_{2}}\right|+\left|x_{1}-x_{2}\right|
\end{aligned}
$$

$$
=\left(\frac{1}{x_{2}}+1\right) \cdot\left|x_{1}-x_{2}\right| \leqslant \frac{3+\varepsilon}{\varepsilon}\left|x_{i}-x_{2}\right| .
$$

取 $\delta-\min \left\{\frac{\varepsilon}{3}, \frac{\varepsilon^{2}}{3+\varepsilon}\right\}$ 。现设 $x_{1}, x_{2} \in[0, \pi]$ 满足 $\mid x_{1}-$ $x_{2} \mid<\delta$,下证必有 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon$ 。
不妨设 $x_{1}<x_{2}$. 若 $x_{1} \geqslant \frac{\varepsilon}{3}$, 则 $x_{1}, x_{2}$ 均属于 $\left[\frac{\varepsilon}{3}, \pi\right]$, 故由上述, 知
$\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \leqslant \frac{3+\varepsilon}{\varepsilon} \cdot\left|x_{1}-x_{2}\right|<\frac{3+\varepsilon}{\varepsilon} \cdot \frac{\varepsilon_{2}}{3+\varepsilon}=$ $\varepsilon$.
若 $0 \leqslant x_{1}<\frac{\varepsilon}{3}$, 则 $x_{2}=x_{2}-x_{1}+x_{1}<\delta+\frac{\varepsilon}{3} \leqslant \frac{2 \varepsilon}{3}$.于是

$$
\begin{gathered}
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\left|x_{1} \sin \frac{1}{x_{1}}-x_{2} \sin \frac{1}{x_{2}}\right| \\
\leqslant\left|x_{1}\right|+\left|x_{2}\right|<\frac{\varepsilon}{3}+\frac{2 \varepsilon}{3}=\varepsilon \text { (当 } x_{1}>0 \text { 时), } \\
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=\left|0-x_{2} \sin \frac{1}{x_{2}}\right| \\
\leqslant\left|x_{2}\right|<\frac{2 \varepsilon}{3}<\varepsilon, \\
\left(\text { 当 } x_{1}=0\right. \text { 时) }
\end{gathered}
$$

总上述，只要 $x_{1}, x_{2} \in[0, \pi],\left|x_{1}-x_{2}\right|<\delta$ ，就有 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\varepsilon$.
803. 需要尽量地把闭区间 $[1,10]$ 划分为几个被此相等的线段，才能使得函数 $f(x)=x^{2}$ 在这些线段中的每一段上的振幅是小于 0.0001 ？
解 设分为相等的 $n$ 段，则对于毎段中的任意两点均有 $\left|x_{1}-x_{2}\right| \leqslant \frac{9}{n}$. 于是,

$$
\begin{aligned}
\left|x_{1}^{2}-x_{2}^{2}\right| & =\left|x_{1}+x_{2}\right|\left|x_{1}-x_{2}\right| \leqslant \frac{(10+10) 9}{n} \\
& =\frac{180}{n} .
\end{aligned}
$$

按题设，我们只需 $\frac{180}{n}<0.0001$ ，也即

$$
n>1800000
$$

因此，应把〔 $1,10 〕$ 等分成至少为 1800000 个的等长的线段，就能满足要求。
804. 证明：在区间 $(a, b)$ 上有穷个一致连续函数的和与它们的乘积在此区间内仍是一致连续的。
证 由于有穷个函数相加或相乘可逐次分絴成两个函数相加或相乘，故我们只需考虑两个函数的情况。

设 $f(x)$ 与 $g(x)$ 都在有限区间 $(a, b)$ 上一致连续，要证 $f(x)+g(x)$ 与 $f(x) g(x)$ 也在 $(a, b)$ 上一致连续。任给 $\varepsilon>0$ 。由于 $f(x)$ 在 $(a, b)$ 上一致连续，故有 $\delta_{1}>0$ 存在，使对于（ $a, b$ ）中任何两点 $x^{\prime}$ 与 $x^{\prime \prime}$ ，只要 $\left|x^{\prime}-x^{\prime \prime}\right|<$ $\delta_{1}$, 就有 $\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\frac{\varepsilon}{2}$. 又由于 $g(x)$ 在 $(a, b)$ 上一致连续，故又有 $\delta_{2}>0$ 存在，使对于 $(a, b)$ 中任何两点 $x^{\prime}$ 与 $x^{\prime \prime}$ ，只要 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta_{2}$ ，就有 $\left|g\left(x^{\prime}\right)-g\left(x^{\prime \prime}\right)\right|<$ $\frac{\varepsilon}{2}$. 令 $\delta=\min \left\{\delta_{1}, \delta_{2}\right\}$, 则当 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta\left(x^{\prime}, x^{\prime \prime}\right.$ 为 $(a$,
b）中任何两点）时，恒有

$$
\begin{aligned}
& \left|\left[f\left(x^{\prime}\right)+g\left(x^{\prime}\right)\right]-\left[f\left(x^{\prime \prime}\right)+g\left(x^{\prime \prime}\right)\right]\right| \leqslant \mid f\left(x^{\prime}\right) \\
& -f\left(x^{\prime \prime}\right)\left|+\left|g\left(x^{\prime}\right)-g\left(x^{\prime \prime}\right)\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon .\right.
\end{aligned}
$$

故 $f(x)+g(x)$ 在 $(a, b)$ 上一致连续. 下证 $f(x) g(x)$ 在 $(a, b)$ 上一致连续. 为此先证一个结论：若函数 $F(x)$ 在

有限区间 $(a, b)$ 上一致连续，则 $F(x)$ 在 $(a, b)$ 上必有界。事实上，对于任意给定的 $\varepsilon>0$ ，都有 $\delta>0$ 存在，使对于 $(a, b)$ 屮任何两点 $x^{\prime}, x^{\prime \prime}$ ，只要 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta$ ，就有 $\left|F\left(x^{\prime}\right)-F\left(x^{\prime \prime}\right)\right|<\varepsilon$. 特别, 当 $a<x^{\prime}<a+\delta, a<x^{\prime \prime}$ $<a+\delta$ 时, 必有 $\left|F\left(x^{\prime}\right)-F\left(x^{\prime \prime}\right)\right|<\varepsilon$; 当 $b-\delta<x^{\prime}$ $<b, b-\delta<x^{\prime \prime}<b$ 时，也必有 $\left|F\left(x^{\prime}\right)-F\left(x^{\prime \prime}\right)\right|<\varepsilon$ 。因此，根涺柯西收敛准则，知 $F(a+1)-\lim _{x \rightarrow a+0} F(x)$ 与 $F(b-0)=\lim _{x \rightarrow b-0} F(x)$ 都存在（有限）。现在 $[a, b]$ 上定义函数 $F^{*}(x)$ ；

$$
F^{*}(x)=\left\{\begin{array}{l}
F(x), \text { 当 } a<x<b \text { 时; } \\
F(a+0), \text { 当 } x=a \text { 时; } \\
F(b-0), \text { 当 } x=b \text { 时. }
\end{array}\right.
$$

显然， $F^{*}(x)$ 在闭区间 $[a, b]$ 上连续，从而有界，由此可知 $F(x)$ 在 $(a, b)$ 与有界。

根据刚才已证的结论，存在常数 $L>0$ 与 $M>0$ ，使

$$
|f(x)| \leqslant L,|g(x)| \leqslant M(a<x<b) .
$$

任给 $\varepsilon>0$, 根据 $f(x)$ 与 $g(x)$ 在 $(a, b)$ 上的一致连续姓，可取 $\delta>0$, 使对于 $(a, b)$ 中任何两点 $x^{\prime}$ 与 $x^{\prime \prime}$ ，只要 $\mid x^{\prime}$ $-x^{\prime \prime} \mid<\delta$, 就有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\frac{\varepsilon}{2 M},\left|g\left(x^{\prime}\right)-g\left(x^{\prime \prime}\right)\right|<\frac{\varepsilon}{2 L} .
$$

由此可知,

$$
\begin{aligned}
& \left|f\left(x^{\prime}\right) g\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right) g\left(x^{\prime \prime}\right)\right| \\
& =\mid\left[f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right] \\
& g\left(x^{\prime}\right)+f\left(x^{\prime \prime}\right)\left[g\left(x^{\prime}\right)-g\left(x^{\prime \prime}\right)\right] \mid \\
& <\frac{\varepsilon}{2 M} \cdot M+\frac{\varepsilon}{2 L} \cdot L=\varepsilon .
\end{aligned}
$$

故得知 $f(x) g(x)$ 在 $(a, b)$ 上一致连续。
注。当（ $a, b$ ）是无穷区间时， $(a, b)$ 上一致连续函数 $f(x)$与 $g(x)$ 的和 $f(x)+g(x)$ 必世一致连续，但乘积 $f(x) g(x)$ 不一定一致连续. 例如，设 $(a, b)=(-\infty,+$ $\infty)$ ，函数 $f(x)=x$ 在 $(-\infty,+\infty)$ 上一致连续，则函数 $[f(x)]^{2}=x^{2}$ 在 $(-\infty,+\infty$ ) 上不一致连续（参看793题(6)).
805. 证明：若单调有界的函数 $f(x)$ 在有穷或无穷的区间（ $a$ ， b）上是连续的，则此函数在区间 $(a, b)$ 上是一致连续的。证 分三种情形论之。
(i) 设 $(a, b)$ 是有限区间。由于 $f(x)$ 在 $(a, b)$ 上单调有界，故极限 $f(a+0)=\lim _{x \rightarrow a-0} f(x)$ 与 $f(b-0)=\lim _{x \rightarrow h-b} f(x)$都存在（有限）。按下式定义 $[a, b]$ 上的函数 $f^{*}(x)$ ：

$$
f^{*}(x)=\left\{\begin{array}{l}
f(x), \text { 当 } a<x<b \text { 时; } \\
f(a+0), \text { 当 } x=a \text { 时； } \\
f(b-0), \text { 当 } x=b \text { 时. }
\end{array}\right.
$$

显然 $f^{\circ}(x)$ 在 $[a, b]$ 上连续，从而一致连续，当然在 $(a$ ， b）上也一致连续，故 $f(x)$ 在 $(a, b)$ 上一致连续。 (ii) $a$ 为有限数, $b=+\infty$ 。此时,令

$$
f^{*}(x)=\left\{\begin{array}{l}
f(x), \text { 当 } a<x<+\infty \text { 时; } \\
f(a+0), \text { 当 } x=a \text { 时. }
\end{array}\right.
$$

则 $f^{*}(x)$ 在 $a \leqslant x<+\infty$ 上连续，且 $\lim _{x \rightarrow+\infty} f^{*}(x)=$ $\lim _{x \rightarrow+\infty} f(x)$ 存在（有限），故根据 791 题的结果知 $f^{*}(x)$ 在 $a \leqslant x<-\infty$ 一致连续，从而 $f(x)$ 在 $a<x<+\infty$ 一致连续.

若 $a=-\infty, b$ 为有限数。考虑函数 $g(x)=f(-x)$ ， $(-b<x<+\infty)$ 即化成刚才证明了的左端点是有限数右端点是 $+\infty$ 的情形。
(iii) $a=-\infty, b=+\infty$ 。任给 $\varepsilon>0$. 利用（ii）已证的结果， $f(x)$ 在 $0<x<+\infty$ 上 一致连续，故存在 $\delta_{1}>0$ ，使当 $x^{\prime}$ 与 $x^{\prime \prime}$ 都属于 $(0,+\infty)$ 且 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta_{1}$ 时, 恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon .
$$

同样利用（ii）已证的结果， $f(x)$ 在 $-\infty<x<1$ 上一致连续，故对于同一个 $\varepsilon$ ，存在 $\delta_{3}>0$ ，使当 $x^{\prime}$ 与 $x^{\prime \prime}$ 都属于 $(-\infty, 1)$ 且 $\left|x^{\prime}-x^{\prime \prime}\right|<\delta_{2}$ 时, 恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon .
$$

现令 $\delta=\min \left\{1, \delta_{1}, \delta_{2}\right\}$, 则当 $-\infty<x^{\prime}<+\infty,-\infty$ $<x^{\prime \prime}<+\infty,\left|x^{\prime}-x^{\prime \prime}\right|<\delta$ 时， $x^{\prime}$ 与 $x^{\prime \prime}$ 必或是同属于区间 $(0,+\infty)$, 或是同属于区间（ $-\infty, 1$ ）。因此，恒有

$$
\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right|<\varepsilon
$$

由此可知， $f(x)$ 在 $(-\infty,+\infty$ )上一致连续. 证毕。
806. 证明：在有穷区间 $(a, b)$ 上有定义而且是连续的函数 $f(x)$ ，可用连续的方法昰拓到闭区间 $[a, b]$ 上，其必要且充分的条件是函数 $f(x)$ 在区间 $(a, b)$ 上是一致连续的。证 必要性：若 $f(x)$ 可用连续的方法延拓到材区间 ( $a$ ， $b]$ 上，则 $f(x)$ 在 $[a, b]$ 上连续，从而 一致连续，当然在 ( $a, b$ ) 上也是一致连续的.

充分性：若 $f(x)$ 在 $(a, b)$ 上一致连续。根据 804 题的证明过程，知 $f(a+0)=\lim _{x \rightarrow a+0} f(x)$ 与 $f(b-0)=$ $\lim _{x \rightarrow-b} f(x)$ 都存在（有限）。按下式定义 $[a, b]$ 上的函数：

$$
f^{*}(x)=\left\{\begin{array}{l}
f(x), \text { 当 } a<x<b \text { 时; } \\
f(a+0), \text { 当 } x=a \text { 时; } \\
f(b-0), \text { 当 } x=b \text { 时. }
\end{array}\right.
$$

显然， $f^{*}(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 上 $f^{*}(x) \equiv f(x)$ 。故 $f^{2}(x)$ 是 $f(x)$ 在 $[a, b]$ 上的连续延拓. 证毕。 807. 函数

$$
\omega_{f}(\delta)=\sup \left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|
$$

（式中 $x_{1}$ 和 $x_{2}$ 为 $(a, b)$ 中受条件 $\left|x_{1}-x_{2}\right| \leqslant \delta$ 限制的任意两点）称为函数 $f(x)$ 在区间 $(a, b)$ 上的连续模数.

证明：函数 $f(x)$ 在区间 $(a, b)$ 上是一致连续的必要且充分的条件是

$$
\lim _{\delta \rightarrow-0} \omega_{f}(\delta)=0
$$

证 必要性：设 $f(x)$ 在 $(a, b)$ 一致连续。任给 $\varepsilon>0$ ，存在 $\delta^{\prime}>0$ ，使 $(a, b)$ 中任何两点 $x_{1}, x_{2}$ ，只要 $\left|x_{1}-x_{2}\right|<$ $\delta^{\prime}$ 就有 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\frac{\varepsilon}{2}$. 现设 $0<\delta<\delta^{\prime}$, 则当 $\mid x_{1}$ $-x_{2} \mid \leqslant \delta$ 时, 必 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|<\frac{\varepsilon}{2}$, 从而

$$
\omega_{f}(\delta)=\sup \left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \leqslant \frac{\varepsilon}{2}<\varepsilon
$$

由此可知， $\lim _{\delta \rightarrow+\infty} \omega_{f}(\delta)=0$ 。
充分性：设

$$
\lim _{\delta \rightarrow+\infty} \omega_{f}(\delta)=0
$$

任给 $\varepsilon>0$ ，存在 $\delta^{\prime}>0$ ，使当 $0<\delta<\delta^{\prime}$ 时，恒有

$$
\omega_{f}(\delta)<\varepsilon
$$

现设 $x_{1}$ 与 $x_{2}$ 是 $(a, b)$ 中满足 $\left|x_{1}-x_{2}\right|<\delta^{\prime}$ 的任何两点.

若 $x_{1}=x_{2}$, 则显然

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|=0<\varepsilon ;
$$

若 $x_{1} \neq x_{2}$ 。令 $\left|x_{1}-x_{2}\right|=\delta^{\prime}$, 则 $0<\delta^{*}<\delta^{\prime}$, 于是

$$
\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right| \leqslant \omega_{i}\left(\delta^{*}\right)<\varepsilon
$$

由此可知, $f(x)$ 在 $(a, b)$ 内一致连续. 证毕。
808. 设：
(a) $f(x)=x^{3}(0 \leqslant x \leqslant 1) ;$
(б) $f(x)=\sqrt{x}(0 \leqslant x<a)$ 及 $(a<x<+\infty)$;
(в) $f(x)=\sin x+\cos x(0 \leqslant x \leqslant 2 \pi)$.

对函数 $f(x)$ 的连续槙数 $\omega_{f}(\delta)$ (参阅前题) 作下形的估价

$$
\omega_{f}(\delta) \leqslant C \delta^{2},
$$

式中 $C$ 和 $\alpha$ 为常数.
解 (a) $\left|x_{3}^{1}-x_{2}^{3}\right|=\left|x_{1}-x_{2}\right|\left|x_{1}^{2}+x_{1} x_{2}+x_{2}^{2}\right| \leqslant 3 \delta$,干是，

$$
\omega_{f}(\delta) \leqslant 3 \delta .
$$

(Б) 当 $0 \leqslant x \leqslant a$ 时 [参看 802 题 ( $(\mathrm{r}$ ) 的证明过程]

$$
\left|\sqrt{x_{1}}-\sqrt{x_{2} \mid}\right| \leqslant \sqrt{\left|x_{1}-x_{2}\right|} \leqslant \sqrt{\delta},
$$

于是,

$$
\omega_{f}(\delta) \leqslant \sqrt{\delta} ;
$$

当 $a<x<+\infty$ 时

$$
\left|\sqrt{x_{1}}-\sqrt{x_{2}}\right|=\frac{\left|x_{1}-x_{2}\right|}{\sqrt{x_{1}}+\sqrt{x_{2}}} \leqslant \frac{\delta}{2 \sqrt{a}},
$$

千是，

$$
\omega_{f}(\delta) \leqslant \frac{\delta}{2 \sqrt{a}}
$$

$$
\text { (B) } f(x)=\sqrt{2} \sin \left(x+\frac{\pi}{4}\right) \text {, }
$$

故

$$
\left|\sqrt{2} \sin \left(x_{1}+\frac{\pi}{4}\right)-\sqrt{2} \sin \left(x_{2}+\frac{\pi}{4}\right)\right|
$$

$$
=\sqrt{2} \cdot 2\left|\cos \frac{x_{1}+x_{2}+\frac{\pi}{2}}{2} \sin \frac{x_{1}-x_{2}}{2}\right|
$$

$$
\leqslant \sqrt{2} \cdot 2 \cdot \frac{\left|x_{1}-x_{2}\right|}{2}=\sqrt{2} \delta,
$$

于是

$$
\omega_{f}(\delta) \leqslant \sqrt{2} \delta .
$$

## § 10. 函数方程

809. 证明：对于 $x$ 和 $y$ 的一切实数值满足方程

$$
f(x+y)=f(x)+f(y)
$$

的唯 一的连续函数 $f(x)(-\infty<x<+\infty)$ 是齐次线性函数：

$$
f(x)=a x,
$$

式中 $a=f(1)$ 是任意的常数。
证 先证：若 $f(x)$ 满足（1），则对任何有理数 $c$ ，必有

$$
f(c x)=c f(x) \quad(-\infty<x<+\infty)
$$

事实上，当 $m$ 与 $n$ 为正整数时，有

$$
\begin{aligned}
f(m x) & =f(x+(m-1) x)=f(x)+f((m-1) x) \\
& =f(x)+f(x)+f((m-2) x)=\cdots \\
& =f(x)+f(x)+\cdots+f(x)=m f(x) ; \\
f(x)= & f\left(n \cdot \frac{x}{n}\right)=n f\left(\frac{x}{n}\right), \text { 故 } f\left(\frac{x}{n}\right)=\frac{1}{n} f(x) .
\end{aligned}
$$

于是

$$
f\left(\frac{m}{n} x\right)=m f\left(\frac{x}{n}\right)=\frac{m}{n} f(x)
$$

又在（1）中令 $y=0$ ，得 $f(x)=f(x)+f(0)$ ，故 $f(0)=$ 0 ；又在（1）中令 $y=-x$ ，并注意已证的结果 $f(0)=0$ ，得 $f(-x)=-f(x)$.
于是

$$
f\left(-\frac{m}{n} x\right)=-f\left(\frac{m}{n} x\right\}=-\frac{m}{n} f(x)
$$

故对任何有理数 $c$, 有 $f(c x)=c f(x)(-\infty<x<+$ $\infty$ ). 下面, 我们利用 $f(x)$ 的连续性证明对任何无理数 $c$,此式也成立。事实上, 设 $c$ 为无理数. 取一串有理数 $c_{n}$, 使 $c_{n} \rightarrow c(n \rightarrow \infty)$. 于是

$$
f\left(C_{n} x\right)=C_{n} f(x),(n=1,2 \cdots)
$$

在此式两端令 $n \rightarrow \infty$ 取极限，并注意到函数 $f$ 在点 $c x$ 连续，即得 $f(c x)=c f(x)$ 。于是，对任何实数 $x$ 和 $c$ ，有 $f(c x)=c f(x)$. 由此可知, 对任何实数 $x$, 有

$$
f(x)=f(x \cdot 1)=x f(1)=a x,
$$

其中 $a=f(\mathbf{1})$. 证毕。
810. 证明：满足方程（1）的单调函数 $f(x)$ 是齐次线性的。

证 由 809 题之证明过程, 知：对任何有理数 $c$ ，有

$$
f(c x)=c f(x) \quad(-\infty<x<+\infty) .
$$

下面，我们利用 $f(x)$ 的单调性证明此式对任何无理数 $c$成立. 为确定起见，设 $f(x)$ 是单调递增的，设 $c$ 是无理数, 要证 $f(c x)=c f(x)(-\infty<x<+\infty)$. 只就 $x>0$ 讨论之（ $x \leqslant 0$ 时可类偩讨论）。取两串有理数 $\left\{c_{x}\right\}$

与\{ $\left\{c_{n}{ }^{\prime}\right\}$ 使：

$$
c_{1}<c_{2}<c_{3}<\cdots<c<\cdots<c_{3}{ }^{\prime}<c_{2}^{\prime}<c_{1}^{\prime},
$$

并且 $c_{n} \rightarrow c_{1} c_{n}{ }^{\prime} \rightarrow c(n \rightarrow \infty)$ 。由于 $x>0$, 故 $c_{1} x<c_{2} x<c_{3} x<\cdots c x<\cdots<c_{3}{ }^{\prime} x<c_{2}{ }^{\prime} x<c_{1}{ }^{\prime} x$,并且 $c_{n} x \rightarrow c x, c_{n}{ }^{\prime} x \rightarrow c x(n \rightarrow \infty)$. 另外, 我们有

$$
f\left(c_{n} x\right)=c_{n} x, f\left(c_{n}^{\prime} x\right)=c_{n}^{\prime} x(n=1,2, \cdots) .
$$

由于 $f(x)$ 是单调递增的，故在点 $c x$ 的左、右极限均存在有限，并且满足

$$
f(c x-0) \leqslant f(c x) \leqslant f(c x+0) .
$$

在前面两个等式中令 $n \rightarrow \infty$ 取极限，得

$$
f(c x-0)=c x, \quad f(c x+0)=c x .
$$

由此可知 $f(c x)=c x$.
以下证明同 809 题，不再重复。
811. 证明：满足方程（1）且在某小区间（ $-\varepsilon, \varepsilon$ ）中为有界的函数 $f(x)$ ，是线性齐次函数，
证 由 809 题的证明过程，知：对任何有理数 $c$ ，有

$$
f(c x)=c f(x)(-\infty<x<+\infty) .
$$

下面，我们利用 $f(x)$ 在（ $-\varepsilon, \varepsilon$ ）中的有界性来证明对于任何无理数 $c$ ，此式也成立。用反证法，假定对于某无理数 $c_{0}$ 以及某实数 $x_{0}$ ，有 $f\left(c_{n} x_{0}\right) \neq c_{0} f\left(x_{0}\right)$ 。令 $f\left(c_{0} x_{0}\right)$ $-c_{0} f\left(x_{0}\right)=\alpha$ ，则 $\alpha \neq 0$ 。今取一串有理数 $\left\{c_{n}\right\}$ ，使 $c_{n} \rightarrow$ $c_{0}(n \rightarrow \infty)$. 于是，对于任何正整数 $m$ ，有

$$
\begin{aligned}
& f\left[m\left(c_{0}-c_{n}\right) x_{0}\right]=m f\left[\left(c_{0}-c_{n}\right) x_{0}\right] \\
& =m\left[f\left(c_{0} x_{0}\right)-f\left(c_{n} x_{0}\right)\right] \\
& =m\left(c_{0}-c_{n}\right) f\left(x_{0}\right)+m a, \\
& \quad(n=1,2,3 \cdots ; m=1,2,3 \cdots) .
\end{aligned}
$$

任给 $G>0$ 。先取定一个正整数 $m$ ，使 $m>\frac{2 G}{|\alpha|}$ 。对此 $m$ ，再取定一个正整数 $n$ ，使

$$
\left|m\left(c_{0}-c_{n}\right)\right| x_{3}\left|<\varepsilon,\left|m\left(c_{0}-c_{n}\right) f\left(x_{0}\right)\right|<G .\right.
$$

令 $\bar{x}=m\left(c_{0}-c_{n}\right) x_{0}$. 于是 $\bar{x} \in(-\varepsilon, \mathfrak{E})$, 并且

$$
|f(\bar{x})| \geqslant|m \alpha|-\left|m\left(c_{0}-c_{n}\right) f\left(x_{0}\right)\right|>2 G-G=G .
$$

由所给 $G>0$ 的任意性, 即知 $f(x)$ 在 $(-\varepsilon, \varepsilon)$ 无界, 此与假定矛盾. 于是，对任何无理数 $c$ ，也有

$$
f(c x)=c f(x) .
$$

以下证明同 809 题，不再重复。
812. 证明：对 $x$ 和 $y$ 的一切值满足方程

$$
f(x+y)=f(x) f(y)
$$

的唯一不恒等于零的连续函数 $f(x)(-\infty<x<+\infty)$是指数函数：

$$
f(x)=a^{x},
$$

式中 $a=f(1)$ 为正的常数。
证 先证必 $f(x)>0(-\infty<x<+\infty)$ 。事实上, 由 $f(x)=f\left(\frac{x}{2}+\frac{x}{2}\right)=\left(f\left(\frac{x}{2}\right)\right]^{2}$, 知 $f(x) \geqslant 0$ 。由于 $f(x) \neq 0$ ，故存在 $x_{0}$ 使 $f\left(x_{0}\right)>0$ 。在（2）中令 $x=x_{0}, y$ $=0$, 得 $f\left(x_{0}\right)=f\left(x_{0}\right) f(0)$, 故 $f(0)=1$ ；又在（2）中令 $y=-x$, 得 $1=f(0)=f(x) f(-x)$, 故 $f(x) \neq 0$, 由此可知

$$
f(x)>0(-\infty<x<+\infty) .
$$

当 $m$ 与 $n$ 为正整数时，

$$
\begin{array}{r}
f(m x)=f((m-1) x+x)=f((m-1) x) \cdot f(x) \\
=f((m-2) x) \cdot f(x) \cdot f(x)=\cdots=[f(x)]^{n} ; \\
f(x)=f\left(n \cdot \frac{x}{n}\right)=\left(f\left|\frac{x}{n}\right|\right]^{n}, \text { 即 } f\left(\frac{x}{n}\right)=
\end{array}
$$

$[f(x)]^{\frac{1}{n}}$.
于是

$$
\left.f\left(\frac{m}{n} x\right)=\left[f^{\prime} \frac{x}{n}\right)\right]^{\prime \prime}=[f(x)]^{\frac{m}{n}}
$$

又有

$$
f\left(-\frac{m}{n} x\right\}=[f(-x)]^{\frac{m}{n}}=(f(x))^{-\frac{m}{n}}
$$

由此可知，对任何有理数 $c$ ，有

$$
f(c x)=[f(x)] \cdot(-\infty<x<+\infty) .
$$

根据 $f(x)$ 的连续性，仿 809 之证易知此式对任何无理数也成立。因此，对于任何实数 $c$ 可 $x$ ，有

$$
f(c x)=[f(x)]^{x},
$$

从而 $f(x)=f(x \cdot 1)=\llbracket f(1)]^{x}=a^{x}, a=f(1)>0$.
注，也可利用 809 题的结果来证. 前面已证 $f(x)>$ $0(-\infty<x<+\infty)$ 。令 $F(x)=\log _{x} f(x)$, 这里 $a=$ $f(1)>0$ 。于是 $F(x)$ 是 $-\infty<x<+\infty$ 上的连续函数，满足（1）式：

$$
\begin{aligned}
F(x+y) & =\log _{a} f(x+y)=\log _{a} f(x) f(y) \\
& =\log _{a} f(x)+\log _{a} f(y)=F(x)+F(y) .
\end{aligned}
$$

故由 809 题的结果，知 $F(x)=a^{*} x$ ，这里
$a^{*}=F(1)=\log _{a} f(1)=\log _{a} a=1$ ，从而 $F(x)=x$ 。由此可知 $f(x)=a^{x}$ 。
813. 证明：在区间 $(0, \varepsilon)$ 中有界并满足方程（2）的不恒等于零的函数 $f(x)$ 是指数函数.
证 由 812 的证明知: $f(x)>0(-\infty<x<+\infty)$, 并且对任何有理数 $c$, 有 $f(c x)=[f(x)]^{c}$ 。

下证对任何无理数 $c$, 也有

$$
f(c x)=[f(x)]^{c}(-\infty<x<+\infty)
$$

用反证法. 假定对某无理数 $c_{0}$ ，及某实数 $x_{0}$ ，有 $f\left(c_{0} x_{0}\right) \neq$ $\left.=f\left(x_{0}\right)\right] c_{0}$ 。显然 $x_{0} \neq 0$ （因为 $f(0)=1$ ）。不妨设 $x_{0}>0$ 。我们有 $f\left(c_{0} x_{\mathrm{c}}\right)=\beta\left[f\left(x_{0}\right)\right]^{r_{0}}, \beta>0, \beta \neq 1$ 。不妨设 $\beta>$ 1. 取一串有理数 $c_{n}$, 使 $c_{1}<c_{2}<c_{3}<\cdots<c_{4}$, 且 $c_{n} \rightarrow c_{9}(n$ $\rightarrow \infty$ ）。于是，对任何正整数 $m$ ，有

$$
\begin{aligned}
& f\left[m\left(c_{0}-c_{n}\right) x_{0}\right]=\left\{f\left[\left(c_{\theta}-c_{n}\right) x_{0}\right]\right\}^{m} \\
& =f\left(c_{0} x_{0}\right)^{m} \cdot f\left(-c_{n} x_{0}\right)^{m}=\beta^{m} \cdot\left[f\left(x_{0}\right)\right]^{m\left(c_{0}-c_{n}\right)}
\end{aligned}
$$

现任给 $G>0$. 先取定一个正整数 $m$, 使 $\beta^{m}>2 G$. 然后,再取一个 $n$, 使

$$
0<m\left(c_{0}-c_{\mathrm{z}}\right) x_{0}<\varepsilon,\left[f\left(x_{0}\right)\right]^{m\left(c_{0}-c_{\mathrm{n}}\right)}>\frac{1}{2} .
$$

于是, 令 $\vec{x}=m\left(c_{0}-c_{n}\right) x_{0}$, 则 $\bar{x} \in(0, \varepsilon)$, 且 $f(\vec{x})>2 G$ - $\frac{1}{2}=G$, 故 $f(x)$ 在 $(0, \varepsilon)$ 无界，此与假定矛盾。注意，若 $\beta<1$, 则需取 $c_{1}>c_{2}>c_{3}>\cdots>c_{0}, c_{3} \rightarrow c$ 并考虔 $f[$ — $\left.m\left(c_{0}-c_{n}\right) x_{0}\right]=\beta^{-m}\left[f\left(x_{0}\right)\right]-m\left[c_{0}-i_{2}\right]$. 由此可知，对任何无理数 $c, f(c x)=(f(x))^{c}$ 也成立。

以下证明同于 812 题，不再重复。
814. 证明：对于 $x$ 和 $y$ 的一切正值满足方程

$$
f(x y)=f(x)+f(y)
$$

的唯一不恒等于零的连续函数 $f(x)(0<x<+\infty)$ 是对数函数：

$$
f(x)=\log _{x} x
$$

式中 $a$ 为正的常数。
证 在 $f(x y)=f(x)+f(y)$ 中令 $y=1$, 得 $f(1)=0$ 。

由于 $f(x) \neq 0$ ，故存在 $x_{0}>0$ 使 $f\left(x_{0}\right) \neq 0$ 。先设 $f\left(x_{0}\right)$ $>0$ 。

由于 $f\left(x_{0}^{2}\right)=f\left(x_{0}\right)+f\left(x_{0}\right)=2 f\left(x_{0}\right), f\left(x_{0}^{*}\right)=$ $2 f\left(x_{0}^{2}\right)=4 f\left(x_{0}\right), \cdots$, 利用旧纳法, 易知 $f\left(x_{0}^{2 *}\right)=$ $2 n f\left(x_{0}\right) \rightarrow+\infty(n \rightarrow \infty)$ 。故可取某正整数 $n$ ，使 $f\left(x_{0}^{2 n}\right)$ $>1$. 于是, 根据连续函数性质知, 在 1 与 $x_{0}^{2 n}$ 之间必存在某 $a$ （显然 $a>0$ ）使 $f(a)=1$ 。现考虑函数 $F(x)=$ $f\left(a^{*}\right)(-\infty<x<+\infty)$. 显然 $F(x)$ 连续且满足 (1) 式:

$$
\begin{aligned}
F(x+y) & =f\left(a^{x+y}\right)=f\left(a^{x} \cdot a^{y}\right)=f\left(a^{x}\right)+f\left(a^{y}\right) \\
& =F(x)+F(y)
\end{aligned}
$$

于是，根据 809 题的结果知 $F(x)=a^{*} x(-\infty<x<+$ $\infty)$ ，其中 $a^{*}=F(1)=f(a)=1$ 。千是 $F(x)=x$ ，即

$$
f\left(a^{2}\right)=x ;
$$

令 $a^{x}=y$, 则 $x=\log _{a} y$, 于是

$$
f(y)=\log _{a} y(0<y<+\infty) .
$$

若 $f\left(x_{0}\right)<0$, 则可考虑函数 $g(x)=-f(x)$.
于是 $g\left(x_{0}\right)>0$ 且 $g(x)$ 也满足 $g(x y)=g(x)+g(y)$,故根据刚才已证的结果，知 $g(y)=\log _{a} y(0<y<+$ $\infty)$ ，其中 $a>0$ 。即 $-f(y)=\log _{a} y$ ，或 $f(y)=-\log _{a} y$ 。令 $a^{*}=\frac{1}{a}$, 则 $a^{*}>0$ 且 $-\log _{a} y=\log _{a} . y$, 故

$$
f(y)=\log _{a}, y \quad(0<y<+\infty),
$$

其中 $a^{\circ}>0$ 。证毕。
815. 证明：对于 $x$ 和 $y$ 的一切正值满足方程

$$
f(x y)=f(x) f(y)
$$

的唯一不恒等于零的连续函数 $f(x)(0<x<+\infty)$ 是

悬函数：

$$
f(x)=x^{a}
$$

式中 $a$ 为常数。
证 考察函数 $F(x)=f\left(e^{x}\right)(-\infty<x<+\infty)$, 财 $F(x)$ 在 $-\infty<x<+\infty$ 伡续不恒为零，且满足（2）式：

$$
\begin{aligned}
F(x+y) & =f\left(e^{-x}\right)=f\left(e^{x} \cdot e^{y}\right)=f\left(e^{x}\right) f\left(e^{y}\right) \\
& =F(x) F(y) .
\end{aligned}
$$

于是, 根据 812 题的结果知

$$
F(x)=b^{x} \quad(-\infty<x<+\infty),
$$

其中 $b>0$, 即 $f\left(e^{x}\right)=b^{x}(-\infty<x<+\infty)$ 。
令 $e^{x}=y$ ，则 $y>0$ ；泉然，存在唯一的 $a(-\infty<a<+$ $\infty$ ），使 $e^{a}=b$ 。于是

$$
f(y)=b^{T}=e^{a x}=y^{a} \quad(0<y<+\infty) .
$$

证毕.
816. 求对于 $x$ 和 $y$ 的一切实数值满足方程（3）的一切连续函数 $f(x)(-\infty<x<+\infty)$ 。
证 因为 $f(x y)=f(x) f(y)$ ，所以 $f(1)=f(1) f(1)$ ，于是 $f(1)=0$ 或 $f(1)=1$ 。

当 $f(1)=0$ 时，对于任意实数 $x$ ，均有

$$
f(x)=f(1) f(x) \equiv 0 .
$$

当 $f(1)=1$ 时，由于 $f(1)=f((-1) \cdot(-1))=$ $f(-1) f(-1)=1$ ，所以 $f(-1)= \pm 1$ 。下面分两种情况讨论：
$1^{\circ}$ 当 $f(-1)=1$ 时，由于

$$
f(-x)=f(-1) f(x)=f(x),
$$

所以在这种情形下就可把问题归结为对 $0<x<+\infty$ 中 470

的 $x$ 进行讨论。而对于 $x>0$ ，我们已证得 $f(x)=x^{a}$ ，式中 $a$ 为常数 ${ }^{*}$ 。然后再利用 $f(-x)=f(x)$ ，即得

$$
f(x)=|x|^{0} .
$$

为保证 $f(x)$ 在 $(-\infty,+\infty)$ 中连续, 需 $a \geqslant 0$ 。
$2^{\circ}$ 当 $f(-1)=-1$ 时，同 $1^{\circ}$ 可得

$$
f(x)=\operatorname{sgn} x \cdot|x|^{a} \quad(a \geqslant 0) .
$$

综 步所述, 所求的函数为（1） $f(x) \Longrightarrow 0$ ；或（2） $f(x)$
$=|x|^{a}(a \geqslant 0)$; 或 $(3) / f(x)=\operatorname{sgn} x \cdot|x|^{a}(a \geqslant 0)$.
*) 利用 815 题的结果。
817. 证明：不连续函数

$$
f(x)=\operatorname{sgn}, x
$$

满足方程（3）。
证 由 $f(x)=\operatorname{sgn} x$ 知， $f(x y)=\operatorname{sgn}(x y)$ 。
分三种情况讨论：
$1^{0}$ 当 $x y>0$ 时， $x$ 与 $y$ 同号，此时 $\operatorname{sgn}(x y)=\operatorname{sgn} x \cdot \operatorname{sgn} y=1 ;$
$2^{\circ}$ 当 $x y<0$ 时， $x$ 与 $y$ 异号，此时
$\operatorname{sgn}(x y)=\operatorname{sgn} x \cdot \operatorname{sgn} y=-1 ;$
$3^{\circ}$ 当 $x y=0$ 时，在实数域内， $x$ 与 $y$ 中至少有一个为 0 ，于是

$$
\operatorname{sgn}(x y)=\operatorname{sgn} x \cdot \operatorname{sgn} y=0
$$

总之，不论哪一种情形，均有

$$
\operatorname{sgn}(x y)=\operatorname{sgn} x \cdot \operatorname{sgn} y,
$$

也即函数 $f(x)=\operatorname{sgn} x$ 满足方程

$$
f(x y)=f(x) f(y) .
$$

818. 求对于 $x$ 和 $y$ 的一切实数值满足方程

$$
f(x+y)+f(x-y)=2 f(x) f(y)
$$

的一切连续函数 $f(x)(-\infty<x<+\infty)$.
解 亚见函数

$$
f(x)=\cos a x \text { 或 } f(x)=\operatorname{ch} a x
$$

满足所给方程.下面我们将指出满足所给方程的函数具有上述形式，为此，在方程中令 $y=0$ ，得

$$
2 f(x)=2 f(x) f(0),
$$

则当 $f(x)$ 丰 0 时 $f(0)=1$. 又令 $x=0$ 得

$$
f(y)+f(-y)=2 f(y),
$$

所以

$$
f(-y)=f(y) .
$$

由 $f(x)$ 的连续性，故知存在 $c>0$ ，使当 $x \in[0, c]$时， $f(x)>0$ 。设 $f(c)=a$ 。下面分两种情况讨论：

1 当 $0<a \leqslant 1$ 时,
于是存在 $\theta: 0 \leqslant \theta<\frac{\pi}{2}$, 使得

$$
f(c)=\cos \theta
$$

从而

$$
\begin{gathered}
f(2 c)=2[f(c)]^{2}-f(0)=2 \cos ^{2} \theta-1=\cos 2 \theta, \\
f(3 c)=2 f(2 c) f(c)-f(c)=2 \cos 2 \theta \cos \theta-\cos \theta \\
=\cos 3 \theta .
\end{gathered}
$$

利用数学归纳法易证，对于一切正整数 $n$ ，均有

$$
f(n c)=\cos n \theta .
$$

又

$$
\left[f^{\prime}\left(\frac{1}{2} c\right)\right]^{2}=\frac{1}{2}[f(0)+f(c)]=\frac{1}{2}(1+\cos \theta)
$$

$$
=\cos ^{2} \frac{\theta}{2},
$$

由于 $f(x)>0$ ，故取正根，则得

$$
f\left(\frac{1}{2} c\right)=\cos \frac{\theta}{2}
$$

同样，利用数学扫纳法可得，对于一切正整数 $n$ ，均有

$$
f\left(\frac{1}{2^{2}} c\right)=\cos \left(\frac{1}{2^{n}} \theta\right) .
$$

重复应用（ $1^{\prime}$ ）到（ $2^{\prime}$ ）的推理过程于（ $4^{\prime}$ ），可知对于一切正整数 $m$ ，均有

$$
f\left(\frac{m}{2^{*}} c\right)=\cos \left(\frac{m}{2^{n}} \theta\right) .
$$

因此，对于 $\frac{m}{2^{n}}$ 型的正实数 $x_{n}$ ，有

$$
f\left(c x_{n}\right)=\cos \left(\theta x_{n}\right)
$$

又因任一正实数 $x$ 皆可表成 $\frac{m}{2^{n}}$ 型数列的极限，所以利用极限过程易得

$$
f(c x)=\cos (\theta x)
$$

由于 $f(-y)=f(y)$ ，故（ $6^{\prime}$ ）式对 $x<0$ 也成立。至于当 $x=0$ 时， $f(c x)=\cos (9 x)$ 显然成立。因此，对于一 $\infty<x<+\infty$ 的一切实数，均有 $f(c x)=\cos (\theta x)$ 。把 $c x$ 换成 $x$ ，并令 $\frac{\theta}{c}=a$ ，则得

$$
f(x)=\cos a x
$$

$2^{\circ}$ 当 $a>1$ 时，于是存在这样的 $\theta$ ，使得

$$
f(c)=a=\operatorname{ch} \theta
$$

根据双曲余弦的关系式，再重复上面的推理过程，可得

$$
f(x)=\mathrm{chax}
$$

当 $a=0$ 时， $f(x) \equiv 1$ 。
综上所述，所求的函数为

$$
f(x)=\cos a x \text { 或 } f(x)=\operatorname{chax} .
$$

819. 求对于 $x$ 和 $y$ 的一一切实数值满足方程组：

$$
\begin{aligned}
& f(x+y)=f(x) f(y)-g(x) g(y) \\
& g(x+y)=f(x) g(y)+f(y) g(x)
\end{aligned}
$$

及

$$
f(0)=1 \text { 和 } g(0)=0
$$

的一切有界连续函数 $f(x)$ 和 $g(x)(-\infty<x<+\infty)$.
解 考虑函数

$$
F(x)=f^{2}(x) \div g^{2}(x),
$$

则

$$
\begin{aligned}
& F(x+y)=f^{2}(x+y)+g^{2}(x+y)=[f(x) f(y) \\
& \quad-g(x) g(y)]^{2}+[f(x) g(y)+f(y) g(x)]^{2} \\
& =F(x) F(y), \\
& \text { 由于 } F(0)=1 \text { 及 } F(x) \neq 0 \text {, 故 } \\
& \quad F(x)=a^{x} \quad(-\infty<x<+\infty),
\end{aligned}
$$

式中 $a=F(1)$ 为正的常数 ${ }^{*}$ 。
由于 $f(x)$ 及 $g(x)$ 有界, 故只能有 $a=1$ 。因此，对于一切实数 $x$, 有 $f^{2}(x)+g^{2}(x)=1$ 。
因为

$$
0=g(0)=g(x-x)=f(x) g(-x)+f(-x) g(x)
$$

及

$$
\begin{aligned}
1 & =f(0)=f(x-x) \\
& =f(x) f(-x)-g(-x) g(x)
\end{aligned}
$$

$$
\begin{gathered}
\text { 上面一式分别乘以 } g(-x) \text { 及 } f(-x) \text {, 然后相加, 得 } \\
f(-x)=f(x) \cdot\left[f^{2}(-x)+g^{2}(-x)\right]=f(x) ;
\end{gathered}
$$

如果上面二式分別乘以 $f(-x)$ 及 $g(-x)$ ，然后相减，得

$$
g(-x)=-g(x)\left[g^{2}(-x)+f^{2}(-x)\right]=-g(x) .
$$

从而可得

$$
\begin{aligned}
& f(x+y)+f(x-y)=f(x) f(y)-g(x) g(y) \\
& \quad+f(x) f(-y)-g(x) g(-y)=2 f(x) f(y) .
\end{aligned}
$$

于是, 考虞到 $f(x)$ 的有界性, 可得

$$
f(x)=\cos a x^{* *)}
$$

再由 $f^{2}(x)+g^{2}(x)=1$ 可得

$$
g(x)= \pm \sin a x .
$$

*）利用 812 题的结果.

*     * ) 利用 818 题的结果.

820. 设

$$
\Delta f(x)=f(x+\Delta x)-f(x)
$$

及

$$
\Delta^{2} f(x)=\Delta\{\Delta f(x)\}
$$

分别为函数 $f(x)$ 的一阶、二阶有限差.
证明：若函数 $f(x)(-\infty<x<+\infty)$ 是连续的且

$$
\Delta^{2} f(x) \equiv 0,
$$

则此函数是线性函数，即

$$
f(x)=a x+b,
$$

式中 $a$ 和 $b$ 为常数。
证 由 $\Delta^{2} f(x) \equiv 0$ 得

$$
\begin{aligned}
& f\left(x+\Delta_{1} x+\Delta_{2} x\right)-f\left(x+\Delta_{2} x\right) \\
& \quad \equiv f\left(x+\Delta_{1} x\right)-f(x) .
\end{aligned}
$$

令 $x=0$, 得

$$
f\left(\Delta_{1}+\Delta_{2}\right)-f\left(\angle_{2}\right) \equiv f\left(\Delta_{1}\right)-f(0) .
$$

令 $\Delta_{i}-n \Delta_{1}$, 得

$$
f\left[(n+1) \Delta_{1}\right]-f\left(n \triangle_{1}\right) \equiv f\left(\Delta_{1}\right)-f(0) .
$$

利用数学归纳法，可得
$f\left[(n+1) \Delta_{1}\right]-f(0) \equiv(n+1)\left[f\left(\Delta_{1}\right)-f(0)\right]$.

关系式（'）可写成

$$
f\left(\Delta_{1}\right)-f(0)=\frac{1}{n}\left[f\left(n \Delta_{1}\right)-f(0)\right]
$$

在上式中令 $n \Delta_{1}=m$ ，再利用（1'）郎得

$$
f\left(\frac{m}{n}\right)-f(0)=\frac{m}{n}[f(1)-f(0)],
$$

所以

$$
f\left(\frac{m}{n}\right)=a \cdot \frac{m}{n}+b,
$$

式中 $a=f(1)-f(0)$ 及 $b=f(0)$ 均为常数。
于是，对于有理数 $x$ ，均有

$$
f(x)=a x+b .
$$

对于无理数 $x$ ，利用 $f(x)$ 的连续性，即可证得上式仍成立。事实上，取有理数列 $x_{n} \rightarrow x$ ，则

$$
\lim _{x \rightarrow} f\left(x_{*}\right)=f(x)
$$

$$
x_{n} \rightarrow x^{\prime}
$$

另一方面

$$
\lim _{x_{n} \rightarrow x} f\left(x_{n}\right)=\lim _{x_{n} \rightarrow x}\left(a x_{n}+b\right)=a x+b
$$

因此，对于一切实数 $x$ ，均有

$$
f(x)=a x+b
$$


[^0]:    - 以后若没有相反的时带说明，数这个字我们将理解为实数.

[^1]:    ![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-029.jpg?height=58&width=1491&top_left_y=2384&top_left_x=294)
    ![](https://cdn.mathpix.com/cropped/2024_12_19_942ee334c42b8934f038g-029.jpg?height=64&width=1577&top_left_y=2438&top_left_x=214)在俄文第三版中改正。

