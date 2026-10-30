# KdV方程式の保存量

ここでは、渡辺のテキスト[^watanabe_book]にしたがって、一般係数のKdV方程式

$$
    \frac{\partial n}{\partial t} +c \frac{\partial^3 n}{\partial x^3} 
    +d n\frac{\partial n}{\partial x} = 0 \tag{1.1}
$$

の保存量を導出してみましょう。

## 1次の保存量
(1.1)を変形すると

$$
    \frac{\partial n}{\partial t} = -\frac{\partial }{\partial x}\left( 
        c\frac{\partial^2 n}{\partial x^2} 
        +\frac{d}{2} n^2\right) \tag{1.2}
$$

となります。これを境界条件（$x\to \pm \infty$で$n$やその微分は0）のもとで$x\to\pm\infty$で積分すると

$$
    \frac{d}{dt}\int^\infty_{-\infty}n dx = 0 
$$

となり、すなわち

$$
    I_1 = \int^\infty_{-\infty}n dx \tag{1.3}
$$

が時間変化しない保存量であることを示しています。イオン音波ソリトンで$n$に対して考えるとこれは粒子数の保存を意味します。

## 2次の保存量
次に2次の保存量を計算してみましょう。(1.1)の両辺に$n$をかけると

$$
    n\frac{\partial n}{\partial t} 
    +c n\frac{\partial^3 n}{\partial x^3} 
    +d n^2 \frac{\partial n}{\partial x} = 0 \tag{1.4}
$$

となります。第一項は合成関数の微分から

$$
    n\frac{\partial n}{\partial t} 
    = \frac{\partial}{\partial t} \left(\frac{n^2}{2}\right) \tag{1.5}
$$

となります。第二項の計算は、微分の連鎖律と合成関数の微分から

$$    
    n\frac{\partial^3 n}{\partial x^3} = 
    \frac{\partial }{\partial x} \left(n \frac{\partial^2 n}{\partial x^2} \right)
    -\frac{\partial n}{\partial x}\frac{\partial^2 n}{\partial x^2}
$$

$$
    = \frac{\partial }{\partial x} \left(
        n \frac{\partial^2 n}{\partial x^2} 
        -\frac{1}{2}\left(\frac{\partial n}{\partial x}\right)^2
        \right)
    \tag{1.6}
$$

となります。第三項も合成関数の微分で

$$
    n^2\frac{\partial n}{\partial x} = \frac{1}{3}\frac{\partial}{\partial x} n^3
$$

なので、これらを合わせて(1.4)を整理すると

$$
    \frac{\partial}{\partial t} \left(\frac{n^2}{2}\right)　
    +c\frac{\partial}{\partial x}\left(
        n \frac{\partial^2 n}{\partial x^2} 
        -\frac{1}{2}\left(\frac{\partial n}{\partial x}\right)^2
        \right)
    +\frac{d}{3}\frac{\partial}{\partial x} (n^3) = 0
$$

となり、1次と同じ境界条件で積分すると第一項以外が消えて

$$
    I_2 = \int^\infty_{-\infty} \left(\frac{n^2}{2}\right)dx \tag{1.7}
$$

となります。これが2次の保存則です。$u$に対して考えればエネルギー保存に対応しています。

## 3次の保存量
次に、(1.1)式の両辺に$n^2$をかけて

$$
    n^2 \frac{\partial n}{\partial t} 
    +c n^2 \frac{\partial^3 n}{\partial x^3} 
    +d n^3\frac{\partial n}{\partial x} = 0 \tag{1.8} 
$$

を計算しましょう。まず第一項は

$$
    n^2 \frac{\partial n}{\partial t} = \frac{1}{3}\frac{\partial}{\partial t}(n^3) \tag{1.9}
$$

となります。第二項を計算していくと、まず微分の連鎖律から

$$
    \frac{\partial}{\partial x}\left(n^2 \frac{\partial^2 n}{\partial x^2}\right)
    = n^2 \frac{\partial^3 n}{\partial x^3} 
    +2n\frac{\partial n}{\partial x}\frac{\partial^2 n}{\partial x^2}
$$

$$
    n^2 \frac{\partial^3 n}{\partial x^3} 
    = \frac{\partial}{\partial x}\left(n^2 \frac{\partial^2 n}{\partial x^2}\right)
    -2n\frac{\partial n}{\partial x}\frac{\partial^2 n}{\partial x^2} \tag{1.10}
$$

となります。(10)の第二項を整理するために、(1.1)より

$$
    n\frac{\partial n}{\partial x}
    = -\frac{1}{d}\left(
        \frac{\partial n}{\partial t} +c\frac{\partial^3 n}{\partial x^3}
    \right)
    \tag{1.11}
$$

を用いて、

$$
    n^2 \frac{\partial^3 n}{\partial x^3} 
    = \frac{\partial}{\partial x}\left(n^2 \frac{\partial^2 n}{\partial x^2}\right)
    +\frac{2}{d}\left(
        \frac{\partial n}{\partial t} +c\frac{\partial^3 n}{\partial x^3}
    \right)\frac{\partial^2 n}{\partial x^2} \tag{1.12}
$$

となります。第二項を展開して出てくる1番目の項を整理すると

$$
    \frac{\partial n}{\partial t}\frac{\partial^2 n}{\partial x^2}
    = \frac{\partial}{\partial x}\left(
        \frac{\partial n}{\partial x}\frac{\partial n}{\partial t}
        \right) 
    -\frac{\partial^2 n}{\partial t \partial x}\frac{\partial n}{\partial x}
$$
$$
    = \frac{\partial}{\partial x}\left(
        \frac{\partial n}{\partial x}\frac{\partial n}{\partial t}
        \right) 
    -\frac{1}{2}\frac{\partial}{\partial t}\left(
        \frac{\partial n}{\partial x}
        \right) ^2 \tag{1.13}
$$

となります。第二項を展開して出てくる2番目の項は

$$
    \frac{\partial^2 n}{\partial x^2}\frac{\partial^3 n}{\partial^3 x}
    = \frac{1}{2} \frac{\partial}{\partial x}\left(\frac{\partial^2 n}{\partial x^2}\right)^2 \tag{1.14}
$$

なので、第二項は最終的に

$$
    n^2 \frac{\partial^3 n}{\partial x^3} 
    = \frac{\partial}{\partial x}\left(
        n^2 \frac{\partial^2 n}{\partial x^2}
    +\frac{2}{d}
        \frac{\partial n}{\partial x}\frac{\partial n}{\partial t}
    +\frac{1}{d}\left(
        \frac{\partial n}{\partial x}
        \right) ^2  
        \right)
    -\frac{1}{d}\frac{\partial}{\partial t}\left(
        \frac{\partial n}{\partial x}
        \right) ^2  
        \tag{1.15}
$$

となります。(1.8)式の第三項は

$$
    n^3\frac{\partial n}{\partial x} 
    = \frac{1}{4}\frac{\partial}{\partial x}(n^4) \tag{1.16}
$$

なので、最終的に(1.8)式をこれまで同様に積分すると、$\frac{\partial}{\partial t}$の項だけが残って、3次の保存量

$$
    I_3 = \int^\infty_{-\infty} \left(\frac{n^3}{3} -\frac{c}{d}\left(
        \frac{\partial n}{\partial x}
        \right) ^2　\right)dx
$$

が得られます。これは実はKdV方程式のハミルトニアンに対応しています[^Nutku_1984]。KdV方程式にこのような保存量が無限に存在することはGardner変換を用いることで証明されます[^Miura_1968][^Oikawa_2013]。

<!-- # 保存量が無限に存在する証明
保存量が無限に存在することをGardner変換を用いて証明しましょう[^Miura_1968][^Oikawa_2013]。次の変換を**Gardner変換**と呼ぶ。

$$
    u = w +\epsilon w_x +\epsilon^2 w^2 \tag{2.17}
$$

これをKdV方程式(1.1)に代入すると、

（工事中）

(2.17)を変形すると

$$
    w = u -\epsilon w_x -\epsilon^2 w^2
$$

となる。これを再び(2.17)に代入すると

$$
    w = u -\epsilon u_x +\epsilon^2 (u_{xx}+u) +\cdots
$$

となる。このように代入を繰り返すことで$\epsilon$の無限級数に展開することができる。これが任意の$\epsilon$で成り立つので、保存則は無限に存在する。 -->

# 参考文献
[^watanabe_book]: 渡辺慎介、「3-5 K-dV方程式の保存量」.「ソリトン物理入門」. 培風館.
[^Nutku_1984]: Y. Nutku. Hamiltonian formulation of the KdV equation.  J. Math. Phys. 1984.<br> <https://doi.org/10.1063/1.526395>
[^Miura_1968]: R. M. Miura et. al. Korteweg‐de Vries Equation and Generalizations. II. Existence of Conservation Laws and Constants of Motion. J. Math. Phys. 1968. <br> <https://doi.org/10.1063/1.1664701>
[^Oikawa_2013]: 及川正行. 第5章 逆散乱法. 〔連載〕非線形波動 ― ソリトンを中心として ―.  日本流体力学学会誌（ながれ）. 2013. <br> <https://www.nagare.or.jp/publication/nagare/archive/2013/1.html>