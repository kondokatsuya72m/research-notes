# ポインティングベクトル
本稿ではポインティングベクトルの導出を示し、それがエネルギー保存と関連付けられることを説明します。

質点系での電磁場について考えましょう。質点の運動方程式は

$$
    m_i\frac{d\bm{v}}{dt} = q_i \left(\bm{E} +\frac{\bm{v}}{c}\times \bm{B}\right )
    \tag{1.1}
$$

となります。このような質点系でのエネルギーを考えましょう。そのためにまず左辺を運動エネルギーにするために両辺に$\bm{v}_i$をかけます。そして質点全体の総和を取り、質点系を包む領域$V$で積分すると、

$$
    \sum_i \frac{d}{dt}\left(\frac{1}{2}m_i v_i^2\right) = \sum_i \int_V d^3x \left(
        q_i \delta^3(\bm{x}-\bm{r}_i) \bm{v}_i \cdot\bm{E} 
        +q_i\delta^3(\bm{x}-\bm{r}_i) \bm{v}_i \cdot \left(\frac{\bm{v}_i}{c}\times \bm{B}\right)
    \right)
    \tag{1.2}
$$

となります。ここで右辺第二項は同じ項を含むスカラー三重積なので0になるので

$$
    \sum_i \frac{d}{dt}\left(\frac{1}{2}m_i v_i^2\right)= \sum_i \int_V d^3x \left(
        q_i \delta^3(\bm{x}-\bm{r}_i) \bm{v}_i \cdot\bm{E} 
    \right)
    \tag{1.3}
$$

となります。これは磁場は仕事をしないということに対応します [^Sunagawa_2023]。

次にMaxwell方程式を適用していきましょう。Ampereの法則より、

$$
    \nabla \times \bm{B} =  \frac{4\pi}{c} \sum_i q_i \delta^3(\bm{x}-\bm{r}_i) \bm{v}_i + \frac{1}{c}\frac{\partial\bm{E}}{\partial t} \tag{1.4}
$$

なので、これを代入できるようにするために$\bm{E}$との内積を取って

$$
    \sum_i q_i \delta^3(\bm{x}-\bm{r}_i) \bm{E}\cdot\bm{v}_i 
    = \frac{c}{4\pi}\bm{E}\cdot(\nabla\times\bm{B})
    -\frac{1}{4\pi}\bm{E}\cdot\frac{\partial \bm{E}}{\partial t}
    \tag{1.5}
$$

となります。(1.5)を(1.3)に代入して

$$
  \sum_i \frac{d}{dt}\left(\frac{1}{2}m_i v_i^2\right) = \int_V d^3x\left(
    \frac{c}{4\pi}\bm{E}\cdot(\nabla\times\bm{B})-\frac{1}{4\pi}\bm{E}\cdot\frac{\partial \bm{E}}{\partial t}
  \right)
  \tag{1.6}
$$

となります。ここで

$$
    U_{EM}=\frac{1}{8\pi}(\bm{E}\cdot\bm{E}+\bm{B}\cdot\bm{B})
    \tag{1.7}
$$

という量を考えましょう。これは電場と磁場のエネルギーの総和になっています。これの時間微分は

$$
    \frac{\partial U_{EM}}{\partial t}= \frac{1}{4\pi}\left(
        \bm{E}\cdot\frac{\partial \bm{E}}{\partial t}+\bm{B}\cdot\frac{\partial \bm{B}}{\partial t}
        \right)
        \tag{1.8}
$$

となり、さらにFaradayの法則

$$
    \nabla \times \bm{E} =-\frac{1}{c}\frac{\partial \bm{B}}{\partial t} \tag{1.9}
$$

を用いて、

$$
    \bm{E}\cdot\frac{\partial \bm{E}}{\partial t}
    = 4\pi \frac{\partial U_{EM}}{\partial t}
    +c\bm{B}\cdot(\nabla\times\bm{E})
    \tag{1.10}
$$

を得ます。(1.10)を(1.6)に代入すると

$$
  \sum_i \frac{d}{dt}\left(\frac{1}{2}m_i v_i^2\right)= \int_V d^3x\left(
    \frac{c}{4\pi}\left(
        \bm{E}\cdot(\nabla\times\bm{B}) -\bm{B}\cdot(\nabla\times\bm{E})
        \right)
        -\frac{\partial U_{EM}}{\partial t}
    \right)
    \tag{1.11}
$$

となり、ベクトル解析の公式から

$$
    \bm{E}\cdot(\nabla\times\bm{B}) -\bm{B}\cdot(\nabla\times\bm{E}) = \nabla\cdot(\bm{E}\times\bm{B})
    \tag{1.12}
$$

なので、(1.11)は最終的に

$$
  \sum_i \frac{d}{dt}\left(\frac{1}{2}m_i v_i^2\right) = \int_V d^3x\left(
        \frac{c}{4\pi}\nabla\cdot(\bm{E}\times\bm{B})
        -\frac{\partial U_{EM}}{\partial t}
    \right)
    \tag{1.13}
$$

となります。ここでポインティングベクトル$\bm{S}$を

$$
    \bm{S} \equiv \frac{c}{4\pi}\nabla\cdot(\bm{E}\times\bm{B})
$$

と定義すると[^nakasho]、(1.13)は

$$
  \frac{d}{dt}\left(\sum_i \frac{1}{2}m_i v_i^2+\int  U_{EM}d^3x\right) 
  =\int_S \bm{S} \cdot d\bm{s}
    \tag{1.14}
$$

となります。ここで電磁場のエネルギーは時間のみに依存するとして偏微分を常微分に置き換え、$\bm{S}$はガウスの定理で面微分に変換しました。この式の左辺は運動エネルギーと電磁場のエネルギーの総和の時間発展を表しており、右辺はそれが流速ベクトル$\bm{S}$の領域の境界面での積分に等しいということを示しています。つまりここからポインティングベクトルはエネルギーの流れを表していることがわかりました。

<!-- ## 例：平面波

具体例として、$x$方向に伝播する電磁波を考えてみましょう。電磁波の電場と磁場はそれぞれ

$$
\bm{E}(x,t)= \bm{E}_0 \sin(\omega t -kx)
$$

$$
\bm{B}(x,t)=\bm{B}_0 \sin(\omega t -kx)
$$

で与えられます。このポインティングベクトルを計算してみると

$$
\bm{S} = \bm{E}_0 \times \bm{B}_0 \sin^2(\omega t-kx)
$$

となります。電磁波では電場と磁場は直交するので振幅部分は$E_0B_0$とできます。三角関数の倍角公式を使うと

$$
\bm{S} = \frac{E_0B_0}{2}(1-\cos(2(\omega t-kx))) \bm{e}_x
$$

となります。周期平均すると$E_0B_0/2$となり、電磁波は単位面積あたり$E_0B_0/2$のエネルギーを持った流れであると言えます。 -->

## 参考文献
[^nakasho]: 電磁場のエネルギーと運動量, 宇宙物理メモ <br> https://github-nakasho.github.io/astroelec/em_energy_momentum

[^Sunagawa_2023]: 第2章 Maxwellの方程式の一般的性質, 理論電磁気学, 砂川重信, 紀伊国屋書店. 2023年.