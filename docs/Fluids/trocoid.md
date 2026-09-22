# ゲルストナーのトロコイド波
一様な重力のもとで完全流体の表面に起こる波を考えましょう。[^imai_book]。このような大きなスケールでは粘性は無視できます。

波の進行方向に$x$軸、$x$と垂直で重力の逆向きに$y$軸を取ります。水面の波はこの2次元での問題と位置付けられますが、一般に解析的に解くことは難しく、下記のような仮定でのモデルが存在します。

* 長い波：波の波長が水の深さと比べて非常に大きく、上下方向の加速度が無視できるとする。うねりや津波、潮汐はこの近似によって説明できる。
* 表面波：振幅が十分小さく線形に近似できる。

上記の仮定を必要としない解析解として**ゲルストナー（Gerstner）のトロコイド解**があります。本記事ではそれを記述します。

## 導入
支配方程式系はラグランジュ形式で記述します。ラグランジュ形式での連続の式と運動方程式は時刻$t=0$での位置を$(a,b)$として下記のようになります。

$$
\frac{\partial (x,y)}{\partial (a,b)} = \mathrm{const}. \tag{1}
$$

$$
\frac{\partial^2 x}{\partial t^2}\frac{\partial x}{\partial a} + \frac{\partial^2 y}{\partial t^2}\frac{\partial y}{\partial a} = -\frac{\partial}{\partial a}\left(\frac{p}{\rho}+gy\right) \tag{2}
$$

$$
\frac{\partial^2 x}{\partial t^2}\frac{\partial x}{\partial b} + \frac{\partial^2 y}{\partial t^2}\frac{\partial y}{\partial b} = -\frac{\partial}{\partial b}\left(\frac{p}{\rho}+gy\right) \tag{3}
$$

いま、$k,c$を任意定数として

$$
x=a+\frac{1}{k}\mathrm{e}^{kb}\sin(k(a-ct)) \tag{4}
$$

$$
y=b-\frac{1}{k}\mathrm{e}^{kb}\cos(k(a-ct)) \tag{5}
$$

という解を仮定し、これが支配方程式系を満たすことを示します。まず(1)は

$$
\frac{\partial (x,y)}{\partial (a,b)} = \left|
    \begin{matrix}
        \displaystyle \frac{\partial x}{\partial a} & \displaystyle \frac{\partial x}{\partial b} \\
        \displaystyle \frac{\partial y}{\partial a} &  \displaystyle \frac{\partial y}{\partial b}
    \end{matrix}
    \right| \\
     = \displaystyle \frac{\partial x}{\partial a}\frac{\partial y}{\partial b} - \frac{\partial x}{\partial b}\frac{\partial y}{\partial a} \\
    = (1+\mathrm{e}^{kb}\cos[k(a-ct)])(1-\mathrm{e}^{kb}\cos[k(a-ct)])
     - (\mathrm{e}^{kb}\sin[k(a-ct)])(\mathrm{e}^{kb}\sin[k(a-ct)]) \\
    =1-2\mathrm{e}^{2kb}\cos^2 [k(a-ct)]-2\mathrm{e}^{2kb}\sin^2[k(a-ct)] \\
    =1-\mathrm{e}^{2kb}
$$

これは時間$t$によらず定数なので、連続の式は満たされていることがわかります。次に運動方程式について調べるために、主要な偏微分について計算しておくと

$$
\frac{\partial^2 x}{\partial t^2} = -kc^2\mathrm{e}^{kb}\sin[k(a-ct)] \\
\frac{\partial x}{\partial a} = 1+\mathrm{e}^{kb}\cos[k(a-ct)] \\
\frac{\partial x}{\partial b} = \mathrm{e}^{kb}\sin[k(a-ct)] \\
\frac{\partial^2 y}{\partial t^2} = kc^2\mathrm{e}^{kb}\cos[k(a-ct)] \\
\frac{\partial y}{\partial a} = \mathrm{e}^{kb}\sin[k(a-ct)] \\
\frac{\partial y}{\partial b} = 1-\mathrm{e}^{kb}\cos[k(a-ct)] \\
$$

なので、(2)、(3)はそれぞれ

$$
\frac{\partial}{\partial a}\left(\frac{p}{\rho}+gy\right) = -\left(\frac{\partial^2 x}{\partial t^2}\frac{\partial x}{\partial a} + \frac{\partial^2 y}{\partial t^2}\frac{\partial y}{\partial a}\right) \\
= \displaystyle kc^2\mathrm{e}^{kb}\sin[k(a-ct)] \\
$$
$$
= \frac{\partial}{\partial a}\left(-c^2\mathrm{e}^{kb}\cos[k(a-ct)] + \frac{1}{2}c^2\mathrm{2}^{2kb} + C\right) \tag{6}
$$

$$
\frac{\partial}{\partial b}\left(\frac{p}{\rho}+gy\right) = 
-\left(\frac{\partial^2 x}{\partial t^2}\frac{\partial x}{\partial b} + \frac{\partial^2 y}{\partial t^2}\frac{\partial y}{\partial b} \right)\\
    = -kc^2\mathrm{e}^{kb}\cos[k(a-ct)] -kc^2 \mathrm{e}^{2kb} 
$$
$$
    = \frac{\partial}{\partial b}\left(-c^2\mathrm{kb}\cos[k(a-ct)] + \frac{1}{2}c^2\mathrm{e}^{2kb} + C\right) \tag{7}
$$

となります。したがって$(6)\times da + (7)\times db$を計算すると、全微分の形になるから積分を実行できて

$$
\frac{p}{\rho}+gy = -c^2\mathrm{e}^{kb}\cos[k(a-ct)] + \frac{1}{2}c^2\mathrm{e}^{2kb} + C
$$

となります。ここで$C$は積分定数です。これに(5)を使ってyを消去して

$$
\frac{p}{\rho} = -gb +\left(\frac{g}{k}-c^2\right)\mathrm{e}^{kb}\cos[k(a-ct)]+ \frac{1}{2}c^2\mathrm{2}^{2kb} +C
$$

となります。任意定数について$c=\sqrt{\frac{g}{k}}$を満たす場合を考えると、$t$依存項が消えて流体粒子が常に定常な圧力を受ける運動を記述できます。この場合

$$
\frac{p}{\rho} = -gb+\frac{g}{2k}\mathrm{e}^{2kb}+C
$$

となります。$b=\mathrm{const.}$となる粒子には同じ圧力がかかるので、$b=\mathrm{const.}$面が等圧面であることがわかります。水面の粒子を$b=0$としてそこでの圧力を$p_{\infty}$とすると、積分定数を消去して

$$
p=p_{\infty}-\rho g(b-b_0)+\frac{\rho}{2}c^2\left(\mathrm{e}^{2kb}-\mathrm{e}^{2kb_0}\right)
$$

となります。

## 解の性質

(4),(5)が解を構成することがわかったところで、その性質を調べてみましょう。等圧面の形状を調べるため$\theta = k(c-ct)$と置いて(4),(5)から$a$を消去すると、

$$
x-ct=\frac{\theta}{k}+\frac{1}{k}\mathrm{e}^{kb}\sin\theta \tag{8} 
$$
$$
y=b-\frac{1}{k}\mathrm{e}^{kb}\cos\theta \tag{9}
$$

となります。$t$を固定したときの波面を考えてみると、水平に移動する成分$\theta$と円上を回転する成分$\sin\theta, \cos\theta$とに分かれます。これは幾何学的には滑らずに転がる円とその同心円上の固定点が描く軌跡を意味し、この式で描かれる曲線を一般に**トロコイド曲線**といいます。

(8)(9)の第2項から流体粒子は半径 $\mathrm{e}^{kb}/k$ で円運動を行います。したがって粒子の $x$ - $p_x$ 位相空間を見ると渦となります。 $b \gt 0$ ではトロコイドはループとなるので、物理的に妥当な解では$b\le 0$です。水深が深い$b\ll 0$の領域では波面は緩やかですが、浅くなるにつれて急峻になります。$b=0$ではサイクロイドとなり頂点が急峻となります。

```{figure} images/trocoid.png
:name: fig-trocoid
:width: 100%

$b=0$（青線）、$-1$（橙線）、$-2$（緑線）
```

## 参考文献
[^imai_book]: 今井功. 「第6章 水の波」、「流体力学」（物理テキストシリーズ）、岩波書店. 1993.
