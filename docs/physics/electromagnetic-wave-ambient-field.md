# 背景磁場のある電磁波
背景磁場のある場合の電磁波の分散関係を導出する。背景磁場と電磁波の相互作用は背景磁場と電磁波の電場、磁場、波数とどの向きに平行かで下記の3通りに分類される。

1. 背景磁場が電場 $\bm{E}_1$ に平行 $\to$ Oモード
1. 背景磁場が磁場 $\bm{B}_1$ に平行 $\to$ Xモード
1. 背景磁場が波数 $\bm{k}$ に平行

なお一般の角度についてはAppleton-Hartreeの関係式として知られている。

## 基礎方程式
まず基礎方程式を書き下しておこう。背景磁場 $\bm{B}_0$ のある系での高周波の振動を考える。つまりcold ionを仮定して $T_i = 0$とする。電子の運動方程式、Maxwell方程式、電流の式を線形化して電磁波の揺動による電場 $\bm{E}_1$ と磁場 $\bm{B}_1$ とすると

$$
    m_e n_0 \frac{\partial \bm{v}}{\partial t} 
        = -en_0 \bm{E}-\frac{e}{c}n_0 \bm{v}\times\bm{B}_0 
        \tag{1.1}
$$

$$
    \nabla\times\bm{E}_1 = -\frac{1}{c}\frac{\partial \bm{B}_1}{\partial t} 
    \tag{1.2}
$$

$$
    \nabla\times\bm{B}_1 = \frac{4\pi}{c}\bm{j}
        +\frac{1}{c}\frac{\partial \bm{E}}{\partial t} 
        \tag{1.3}
$$

$$
    \bm{j} = -en_0\bm{v} \tag{1.4}
$$

となる。

## (1) $\bm{B}_0 \parallel \bm{E}_1$ : Oモード（通常波）
まず電磁波の磁場 $\bm{B}_1$ が背景磁場 $\bm{B}_0$に垂直な場合を考える。つまり電磁波の電場 $\bm{E}_1$ は背景磁場に平行である。

この場合、電子は電磁波の電場によって往復運動をするが、背景磁場と往復運動は平行であるためローレンツ力は0になり磁場は粒子に力を及ぼさない。したがって分散関係も背景磁場のない場合と変わらず

$$
    \omega^2 = \omega_p^2 + k^2 c^2 \tag{2.1}
$$

である。このモードをOモード（ordinary mode, 通常波）と呼ぶ。

## (2) $\bm{B}_0 \parallel \bm{B}_1$ : Xモード（異常波）
z方向に背景磁場 $\bm{B}_0 = B_0 \bm{e}_z$ のある系に、背景磁場に平行な磁場を持つ電磁波を入射するとする。つまり波数$\bm{k}=k\bm{e}_x$とし、背景電場がない場合の偏光を電場の向きがy方向とする。

このとき、電子は電場の方向に振動するのでy方向の速度 $v_y$ を持つ。この速度は背景磁場と垂直なので電子にはローレンツ力が働いてx方向の運動も誘起される。電子がx方向に動くということはそれに従って電場も誘起されると考えられるので、レーザーの揺動電場は$\bm{E}_1 = E_x \bm{e}_x + E_y \bm{e}_y$となる。

$E_x, E_y$ それぞれの成分について電子の運動方程式(1.1)をFourier変換しながら書き下すと

$$
    -i \omega m_e v_x = -e E_x -\frac{e}{c} v_y B_0 \tag{3.1}
$$

$$
    -i \omega m_e v_y = -e E_y +\frac{e}{c} v_x B_0 \tag{3.2}
$$

となる。次にファラデーの法則(1.2)はz成分を考えて

$$
    kE_y = \frac{\omega}{c} B_1 \tag{3.3}
$$

となる。次にアンペールの法則(1.3)は$x,y$の2つの成分について

$$
    0 = -\frac{4\pi en_0}{c}v_x - \frac{i\omega}{c}E_x \tag{3.4}
$$

$$
    -ikB_1 = -\frac{4\pi en_0}{c}v_y - \frac{i\omega}{c}E_y \tag{3.5}
$$

となる。まずは$v_x, v_y$を消去するために(3.4), (3.5)を用いて

$$
    v_x = -\frac{i\omega}{4\pi n_0 e}E_x \tag{3.6}
$$

$$
    v_y = \frac{ikB_1 c}{4\pi n_0 e}B_1 -\frac{i\omega}{4\pi n_0 e}E_y \tag{3.7}
$$

となる。さらに(3.3)を(3.7)代入すると

$$
    v_y = \left(
        \frac{ik^2c^2}{4\pi n_0 e \omega}
        -\frac{i\omega}{4\pi n_0 e}
    \right)E_y 
    \tag{3.8}
$$

となる。(3.6), (3.8)を(3.1),(3.2)に代入して

$$
    0 = \left(e-\frac{\omega^2 m_e}{4\pi n_0 e}\right) E_x 
        +\frac{eB_0}{c} \left(
            \frac{ik^2c^2}{4\pi n_0 e\omega} -\frac{i\omega}{4\pi n_0e}\right) E_y
    \tag{3.9}
$$

$$
    0 = -\frac{eB_0}{c}\frac{i\omega}{4\pi n_0 e} E_x 
    + \left(i\omega m_e\left(
        \frac{ik^2 c^2}{4\pi n_0 e\omega} -\frac{i\omega}{4\pi n_0 e}\right) +e
    \right) E_y
    \tag{3.10}
$$

を得る。ここで、$E_x, E_y$は互いに虚数倍になっているので、振動の位相が $\pi/2$ ずれていて$(E_x, E_y)$は楕円上を振動する。

非自明な波動$(E_x, E_y)$が存在するためには連立方程式の(3.9),(3.10)の係数行列の行列式が0でなければならないので、

$$
    \left(1-\frac{\omega^2}{\omega_{pe}^2}\right)
    \left(1+\frac{k^2c^2}{\omega_{pe}^2}-\frac{\omega^2}{\omega_{pe}^2}\right)
    +\frac{\omega_{ce}^2 k^2c^2}{\omega_{pe}^4} 
    -\frac{\omega^2 \omega_{ce}^2}{\omega_{pe}^4} = 0
    \tag{3.11}
$$

を得る。ここで

$$
    \omega_{pe}^2 \equiv \frac{4\pi n_0 e^2}{m_e} \tag{3.12}
$$

$$
    \omega_{ce} \equiv \frac{eB_0}{m_e c} \tag{3.13}
$$

でそれぞれ電子のプラズマ振動数、サイクロトロン周波数を表す。(3.11)がXモードの分散関係式である。

見通しをよくするために $k^2 c^2 / \omega^2 = \cdots$の形に直したい。まず $k^2 c^2 / \omega_{pe}^2$ に着目して整理すると

$$
    \frac{k^2 c^2}{\omega_{pe}^2} 
    = \frac{\frac{\omega^2 \omega_{ce}^2}{\omega_{pe}^4}
    -\left( 1-\frac{\omega^2}{\omega_{pe}^2}\right)^2}
    {1-\frac{\omega^2}{\omega_{pe}^2}+\frac{\omega_{ce}^2}{\omega_{pe}^2}}
    \tag{3.14}
$$

となる。両辺 $\omega_{pe}^2 / \omega^2$ 倍して分母を変換すると

$$
    \frac{k^2c^2}{\omega^2} 
    = \frac{
        \frac{\omega_{ce}^2}{\omega_{pe}^2} 
        - \frac{\omega_{pe}^2}{\omega^2}\left(1-\frac{\omega^2}{\omega_{pe}^2}\right)^2
        }{
            1-\frac{\omega^2}{\omega_{pe}^2}+\frac{\omega_{ce}}{\omega_{pe}^2}
        }
        \tag{3.15}
$$

となる。ここで混成周波数を

$$
    \omega_{eH}^2 \equiv \omega_{pe}^2 + \omega_{ce}^2
$$

と定義すると、分散関係は最終的に

$$
    \frac{k^2c^2}{\omega^2} =1-\frac{\omega_{pe}^2}{\omega^2}\frac{\omega^2-\omega_{pe}^2}{\omega^2 -\omega_{eH}^2} 
    \tag{3.16}
$$

となる。

カットオフを示すためには(3.16)のゼロ点を考えればよい。実際に$k=0$を(3.16)に代入すると

$$
    0 = 1-\frac{\omega_{pe}^2}{\omega^2}\frac{\omega^2-\omega_{ce}^2}{\omega^2-\omega_{eH}^2}
    \tag{3.17}
$$

となる。移項して整理すると

$$
    \frac{\omega_{pe}^2}{\omega^2} = \frac{\omega^2-\omega_{eH}^2}{\omega^2-\omega_{ce}^2}
$$

となり、混成周波数を分解して整理すると

$$
    \frac{\omega_{pe}^2}{\omega^2} = 1-\frac{\omega_{ce}^2}{\omega^2-\omega_{pe}^2}
$$

となる。移項して分母を$\omega^2$で約分すると

$$
    1-\frac{\omega_{pe}^2}{\omega^2}=\frac{\frac{\omega_{ce^2}}{\omega^2}}{1-\frac{\omega_{pe}^2}{\omega^2}}
$$

となるから、分母を払うと

$$
\left(1-\frac{\omega_{pe}^2}{\omega^2}\right)^2=\frac{\omega_{ce^2}}{\omega^2}
$$

となる。平方根を取ると

$$
1-\frac{\omega_{pe}^2}{\omega^2}=\pm\frac{\omega_{ce}}{\omega}
$$

となるので、整理すると

$$
\omega^2 \pm \omega_{ce}\omega-\omega_{pe}^2=0
$$

となるから、解の公式からこの解は

$$
\omega_L = \frac{\omega_{ce}}{2}+\sqrt{\omega_{pe}^2+\frac{\omega_{ce}^2}{4}}
\tag{3.18}
$$

$$
\omega_R = -\frac{\omega_{ce}}{2}+\sqrt{\omega_{pe}^2+\frac{\omega_{ce}^2}{4}}
\tag{3.19}
$$

となる。これらはそれぞれ左回り偏光、右回り偏光に対応している。

$\omega - (c^2k^2)/\omega^2$ グラフを見ながら考えてみよう。このグラフでは$\omega_{pe} = 2.0$, 
$\omega_{ce} = 2.5$と設定しており、$\omega_L= 3.61$, $\omega_R= 1.11$, $\omega_{eH}= 3.20$である。実際に電磁波が伝播できる領域は分散関係の曲線が点線より上にある領域のみである。

* まず$\omega$の小さな領域（$\omega < 1$）では伝播することができずカットオフされる。
* $\omega = \omega_L$で最初のゼロ点を迎え、それ以降は伝播する。
* $\omega_L < \omega < \omega_{eH}$で$\omega_{eH}$に近づくにつれて曲線は$k\to+\infty$に漸近する。これは共鳴（resonance）を意味する。
* それを超えると再びカットオフ領域$\omega_{eH} < \omega < \omega_{R}$に入り、伝搬できない。
* $\omega_R < \omega$に入ると再び伝播可能となる。

![figure](images/xmode.png)


<!-- ## (3) $\bm{B}_0 \parallel \bm{k}$ : 背景磁場に沿って伝播する電磁波

最後に電磁波の伝播方向が背景磁場と平行でz方向の場合を考える。

この場合、電場によるy方向の振動によってローレンツ力はz方向に生じる。したがって電子はx-y平面上で運動することが予想される。

まず電場はOモード同様に電子が運動することによってx,y方向の2つの成分を持つ。磁場は伝播方向と垂直な面にのみ生じるが、Xモードの場合はx,yの運動によって生じる磁場はz方向しか存在しえないので、結果1成分のみとなる。一方で平行伝播の場合は伝播方向に垂直な面では磁場もx,yの2つの成分を考える必要がある。

基礎方程式であるアンペール則、ファラデー則、電子の運動方程式を書き下すと

$$
i\bm{k}\times\bm{E}_1 = \frac{i\omega}{c}\bm{B}_1 \tag{4.1}
$$

$$
i\bm{k}\times\bm{B}_1 = -\frac{4\pi n_0 e}{c}\bm{v}-\frac{i\omega}{c}\bm{E}_1 \tag{4.2}
$$

$$
-i\omega m_e \bm{v} = -e\bm{E}_1 -\frac{e}{c}\bm{{v}}\times\bm{B}_0 \tag{4.3}
$$

となる。仮定から

$$
    \bm{k} = (0,0,k) \tag{4.4}
$$

$$
    \bm{B}_0 = (0,0,B_0) \tag{4.5}
$$


$$
    \bm{E}_1 = (E_x, E_y, 0) \tag{4.6}
$$

$$
    \bm{B}_1 = (B_x, B_y, 0) \tag{4.7}
$$

$$
    \bm{v} = (v_x, v_y, 0) \tag{4.8}
$$

となるから、(4.1)-(4.3)の各x,y成分を見ると

$$
-ikE_y = \frac{i\omega}{c}B_x \tag{4.9}
$$

$$
ikE_x = \frac{i\omega}{c}B_y \tag{4.10}
$$

$$
-ikB_y = -\frac{4\pi n_0 e}{c}v_x -\frac{i\omega}{c}E_x \tag{4.11}
$$

$$
ikB_x = -\frac{4\pi n_0 e}{c}v_y -\frac{i\omega}{c}E_y \tag{4.12}
$$

$$
-i\omega m_e v_x = -eE_x -\frac{e}{c}v_y B_0 \tag{4.13}
$$

$$
-i\omega m_e v_y = -eE_y +\frac{e}{c}v_x B_0 \tag{4.14}
$$

となる。まず(4.11),(4.12)に(4.9),(4.10)を代入して$B_x,B_y$を消去すると、

$$
v_x = -\frac{c}{4\pi n_0 e}\left(
    \frac{i\omega}{c}-i\frac{ck^2}{\omega}
\right)E_x \tag{4.15}
$$

$$
v_y = -\frac{c}{4\pi n_0 e}\left(
    \frac{i\omega}{c}-i\frac{ck^2}{\omega}
\right)E_y \tag{4.15}
$$

となる。これを(4.13), (4.14)に代入して連立させると

$$
0 = \left(
    \frac{c\omega m_e}{4\pi n_0 e}
    \left(
        \frac{\omega}{c}-\frac{ck^2}{\omega} +e
    \right)
\right)E_x
-\frac{eB_0}{c}\frac{c}{4\pi n_0 e}\left(
    \frac{i\omega}{c}-\frac{ick^2}{\omega}
\right)E_y \tag{4.16}
$$

$$
0 = \frac{eB_0}{c}\frac{c}{4\pi n_0 e}\left(
    \frac{i\omega}{c}-\frac{ick^2}{\omega}
\right)E_x
+\left(
    \frac{c\omega m_e}{4\pi n_0 e}
    \left(
        \frac{\omega}{c}-\frac{ck^2}{\omega} +e
    \right)
\right)E_y
 \tag{4.17}
$$

となる。(4.16),(4.17)が非自明解を持つためには係数行列が0でなければならないので

（工事中）
 -->
## 参考文献
* 7.11 Electromagnetic waves in magnetized plasmas. Introduction to plasma theory. D. R. Nicholson. Wiley. 1983.
* 4.15 Electromagnetic Waves Perpendicular to $B_0$. Introduction to Plasma Physics. F. F. Chen. Springer. 1974. https://doi.org/10.1007/978-1-4757-0459-4