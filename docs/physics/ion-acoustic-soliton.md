# イオン音波ソリトン
本稿ではプラズマの基礎方程式からK-dV方程式を導出し、それがソリトン解を持つことを示します。プラズマでのK-dV方程式とイオン音波ソリトンはWashimiらによって1966年に理論的に予測され [^Washimi_1966]、その4年後にIkeziらによって実験で観測されました [^Ikezi_1970]。

なお英語での引用が必要であれば拙著 [^KondoK_APSOS_2026]にも記載しておりますので参照ください。

## 導出
連続の式、イオンの運動方程式、電子の断熱応答の式、Poisson方程式を支配方程式系として導出します [^Watanabe_book] [^Wadachi_book]。支配方程式を書き下すと下記になります。

$$
\frac{\partial n}{\partial t}+\frac{\partial}{\partial x}(nv) = 0 
$$

$$
M\left(\frac{\partial v}{\partial t}+v\frac{\partial v}{\partial x}\right) = -Ze\frac{\partial \phi}{\partial x}
$$

$$
n_e = n_0\mathrm{exp}\left(\frac{e\phi}{T_e}\right)
$$

$$
\frac{\partial^2 \phi}{\partial x}=4\pi e(n_e-Zn)
$$

これを下記の表の通りに規格化します。規格化された量をチルダをつけて表します。

|物理量|規格化因子|関係式|
|-|-|-|
|イオン密度$n$|無限遠でのイオン密度$n_0/Z$|$n=(n_0/Z)\tilde{n}$|
|電子密度$n_{e0}$|無限遠での電子密度$n_0$|$n_{e}=n_0\tilde{n}_e$|
|長さ$x$|デバイ長$\lambda_D = \sqrt{\frac{T_e}{4\pi n_0 e^2}}$|$x=\tilde{x}\lambda_D$|
|時間$t$|イオンプラズマ振動数$\omega_{pi}=\sqrt{\frac{4\pi n_0 Z e^2}{M}}$|$t=\tilde{t}/\omega_{pi}$|
|速度$v$|イオン音速$c_s=\sqrt{\frac{ZT_e}{M}}$|$v=\tilde{v}c_s$|
|ポテンシャル$\phi$|$\frac{T_e}{e}$ ($e\phi/T_e=\tilde{\phi}$)|$\phi=T_e\tilde{\phi}/e$|

これらを適用した支配方程式系は下記の通りになります。

$$
\frac{\partial \tilde{n}}{\partial \tilde{t}}
+\frac{\partial}{\partial \tilde{x}}(\tilde{n}\tilde{v}) = 0 \tag{1}
$$

$$
\frac{\partial \tilde{v}}{\partial \tilde{t}}
+\tilde{v}\frac{\partial \tilde{v}}{\partial \tilde{x}} 
= -\frac{\partial \tilde{\phi}}{\partial \tilde{x}} \tag{2}
$$

$$
\tilde{n}_e = \mathrm{exp}\left(\tilde{\phi}\right) \tag{3}
$$

$$
\frac{\partial^2 \tilde{\phi}}{\partial \tilde{x}^2} = \tilde{n}_e-\tilde{n} \tag{4}
$$

ここで分布関数に$f(x,t)=f_0 + \epsilon f_1 + \epsilon^2 f_2 \cdots$ なる摂動展開を行います。$f_0$は平衡状態でのMaxwell分布を表します。すると各物理量は摂動項に対応して

$$
\tilde{n} = 1 + \epsilon \tilde{n}_1+ \epsilon^2 \tilde{n}_2 + \cdots
$$
$$
\tilde{n}_e = 1 + \epsilon \tilde{n}_{e1}+ \epsilon^2 \tilde{n}_{e2} + \cdots
$$
$$
\tilde{v} = \epsilon \tilde{v}_1+ \epsilon^2 \tilde{v}_2 + \cdots 
$$
$$
\tilde{\phi}  = 1 + \epsilon \tilde{\phi}_1+ \epsilon^2 \tilde{\phi}_2 + \cdots
$$

のように摂動展開が行えます。時空間の変数$(x,t)$に対しては次のような変数変換（**Gardner-Morikawa変換**）[^Gardner_Morikawa_1960]を行います。

$$
\xi = \epsilon^{1/2}(\tilde{x}-\tilde{t}) \tag{5}
$$
$$
\tau = \epsilon^{3/2}\tilde{t} \tag{6}
$$

次数は分散関係$\omega(k)$の3次の項までを考慮することに対応しています。$\tilde{x}-\tilde{t}$は音速で移動する系へ移ることを意味しています。最初にイオン音波ソリトンでのK-dV方程式を導出したWashimiらは逆に$k(\omega)$を3次まで展開して$\tau$の代わりに$\eta=\epsilon^{3/2}x$と置いています[^Washimi_1966]が、結果として得られる方程式は変わりません。本稿では渡辺[^Watanabe_book]や和達[^Wadachi_book]に従って$\tau$を用いています。

これらと微分の連鎖律から微分演算子を計算しておくと、

$$
\frac{\partial }{\partial \tilde{t}} = -\epsilon^{1/2}\frac{\partial }{\partial \xi} + \epsilon^{3/2}\frac{\partial }{\partial \tau}
$$
$$
\frac{\partial }{\partial \tilde{x}} = \epsilon^{1/2}\frac{\partial }{\partial \xi}
$$

となります。これらを代入して(1)-(4)を摂動展開し、$\epsilon$の次数が同じ項を比較して関係式を導出していきましょう。まず最低次の項を見ていくと次の通りです。

(1),(2): $\epsilon^{3/2}$が最低次で、

$$
-\frac{\partial \tilde{n}_1}{\partial \xi}+\frac{\partial \tilde{v}_1}{\partial \xi} = 0 
$$

$$
-\frac{\partial \tilde{v}_1}{\partial \xi}=-\frac{\partial \tilde{\phi}_1}{\partial \xi} 
$$

となります。$\xi\to\pm\infty$で摂動項が0となることを使って積分すると

$$
\tilde{n}_1 = \tilde{v}_1 = \tilde{\phi}_1 \tag{7}
$$

となります。

(3): expをマクローリン展開してから代入すると、$\epsilon^{1}$が最低次となり、

$$
\tilde{n}_{e1}=\tilde{\phi}_1 \tag{8}
$$

(4): 同じく$n_e$はマクローリン展開しておいて$\epsilon^{1}$を比較すると

$$
\tilde{n}_{e1}=\tilde{n}_{1} \tag{9}
$$

となります。したがって1次の規格化した物理量はすべて等しいという関係式が得られます。

次の項について見てみると、

$$
\frac{\partial \tilde{n}_1}{\partial \tau}
-\frac{\partial \tilde{n}_2}{\partial \xi}
+\frac{\partial \tilde{v}_2}{\partial \xi}
+\frac{\partial }{\partial \xi}(\tilde{n}_1\tilde{v}_1)=0 \tag{10}
$$

$$
-\frac{\partial \tilde{v}_2}{\partial \xi}
+\frac{\partial \tilde{v}_1}{\partial \tau}
+\tilde{v}_1\frac{\partial \tilde{v}_1}{\partial \xi}
=-\frac{\partial \tilde{\phi}_2}{\partial \xi} \tag{11}
$$

$$
\tilde{n}_{e2}=\tilde{\phi}_2+\frac{1}{2}\tilde{\phi}_1^2 \tag{12}
$$

$$
\frac{\partial^2 \tilde{\phi}_1}{\partial \xi^2} = \tilde{n}_{e2}-\tilde{n}_2 \tag{13}
$$

となります。まず(10)と(11)から $\frac{\partial \tilde{v}_2}{\partial \xi}$ を消去し、1次の量を $n_1$に統一すると

$$
2\frac{\partial \tilde{n}_1}{\partial \tau}
-\frac{\partial \tilde{n}_2}{\partial \xi}
+3\tilde{n}_1\frac{\partial \tilde{n}_1}{\partial \xi}
+\frac{\partial \tilde{\phi}_2}{\partial \xi}=0 \tag{14}
$$

となります。一方(12)と(13)から$n_{e2}$を消去すると

$$
\frac{\partial^2 n_1}{\partial \xi^2}=\phi_2+\frac{1}{2}\phi_1^2 -n_2
$$

となります。両辺を$\xi$で偏微分して(14)から$\frac{\partial \tilde{n}_2}{\partial \xi}$を消去して整理すると2次の項はすべて消えて

$$
\frac{\partial \tilde{n}_1}{\partial \tau}
+\tilde{n}_1\frac{\partial \tilde{n}_1}{\partial \xi}
+\frac{1}{2}\frac{\partial^3 \tilde{n}_1}{\partial \xi^3}=0 \tag{15}
$$

が導出されます。このタイプの偏微分方程式を**KdV(Korteweg-de Vries)方程式**と呼びます。

この方程式を元の座標系$(x,t)$での方程式に戻すことを考えましょう。$(\xi, \tau)$の定義から

$$
\frac{\partial }{\partial \xi} = \epsilon^{-1/2}\frac{\partial}{\partial \tilde{x}} \tag{16}
$$

$$
\frac{\partial }{\partial \tau} 
= \epsilon^{-3/2}\frac{\partial}{\partial \tilde{x}}
+\epsilon^{-3/2}\frac{\partial}{\partial \tilde{t}} \tag{17}
$$

だから、(15)に代入すると

$$
\epsilon^{-3/2} \frac{\partial \tilde{n}_1}{\partial \tilde{t}}
+\epsilon^{-3/2} \frac{\partial \tilde{n}_1}{\partial \tilde{x}}
+\epsilon^{-1/2} \tilde{n}_1\frac{\partial \tilde{n}_1}{\partial \tilde{x}}
+\epsilon^{-3/2} \frac{1}{2}\frac{\partial^3 \tilde{n}_1}{\partial \tilde{x}^3}=0 \tag{18}
$$

となります。ここで$\tilde{n}_1 \simeq \epsilon^{-1} (\tilde{n}-1)$だから代入すると$\epsilon$の次数はすべて$\epsilon^{-5/2}$でそろって静止系でのKdV方程式

$$
\frac{\partial \tilde{n}}{\partial \tilde{t}}
+\tilde{n}\frac{\partial \tilde{n}}{\partial \tilde{x}}
+\frac{1}{2}\frac{\partial^3 \tilde{n}}{\partial \tilde{x}^3}=0 \tag{19}
$$

<!-- が得られます。なおMoving frame $(\tilde{x}', \tilde{t}')$ でも同様に$\epsilon$を消去して

$$
\frac{\partial \tilde{n}}{\partial \tilde{t}'}
+\tilde{n}\frac{\partial \tilde{n}}{\partial \tilde{x}'}
+\frac{1}{2}\frac{\partial^3 \tilde{n}}{\partial \tilde{x}'^3}=0 \tag{19}
$$

とすることができます。 -->

KdV方程式の1ソリトン解を求める方法は別記事でまとめる予定です。(19)は$\alpha=1,\beta=1/2$の場合なので、

$$
\tilde{n}=1+3(M-1)\mathrm{sech}^2\left(
    \sqrt{\frac{M-1}{2}}(\tilde{x} -\tilde{U}\tilde{t})
    \right) \tag{20}
$$

<!-- $$
\tilde{n} = 3\tilde{U} \mathrm{sech}^2\left(
    \sqrt{\frac{\tilde{U}}{2}}(\tilde{x} -\tilde{U}\tilde{t})
    \right) \tag{20}
$$ -->

となります。ここで$M=U/C_s$はマッハ数です。ここでソリトンの幅を

$$
\tilde{D} \equiv \sqrt{\frac{2}{\tilde{U}}} \tag{21}
$$

で定義すると、(15),(16)と1次の関係式(7)から規格化のチルダを外して

$$
M-1 = \frac{\delta n}{3n_0} = \frac{e\phi}{3T_e} = \frac{2\lambda_D^2}{D^2} \tag{22}
$$

を得ます。なお$\delta n$はソリトンの振幅です。なお$D$と半値全幅$D_H$の関係は$\mathrm{sech}(D_H/2)=1/2$から

$$
D_H=2\mathrm{arccosh}(\sqrt{2})\times D \simeq 1.7627 \times D \tag{23}
$$
$$
D=0.567\times D_H \tag{24}
$$

となります。

## 参考文献
[^Ikezi_1970]:  H. Ikezi, R. J. Taylor and D. R. Baker, Phys. Rev. Lett. **25**, 11 (1970). <br> <https://doi.org/10.1103/PhysRevLett.25.11>
[^Washimi_1966]: H. Washimi and T. Taniuchi, Phys. Rev. Lett. **17**, 19 (1966). <br> <https://doi.org/10.1103/PhysRevLett.17.996>
[^Ichikawa_1988]: 市川芳彦, 「プラズマにおける非線形現象の諸問題(2)」, プラズマ・核融合学会誌 **59**, 5, 337-361. 1988. <br> <https://doi.org/10.1585/jspf1958.59.337> <br> 逓減摂動法の物理的な解釈について詳しく書かれている。
[^Saeki_2007]: 佐伯紘一, 「1.5 静電波ソリトンと無衝突衝撃波の基礎実験」, プラズマ・核融合学会誌 **83**, 1, 74-80. 2007. <br> <http://www.jspf.or.jp/Journal/PDF_JSPF/jspf2007_01/jspf2007_01-74.pdf>
[^Watanabe_book]: 渡辺慎介, 「ソリトン物理入門」. 培風館 (1985). <br> <https://ndlsearch.ndl.go.jp/books/R100000002-I000001750721> <br> 和書で丁寧にまとめられているため読みやすい。
[^Wadachi_book]: 和達三樹, 「非線形波動」. 岩波書店 (2000). <br> <https://ndlsearch.ndl.go.jp/books/R100000002-I000002903820> <br> 手に入りやすいが渡辺よりはやや難しい。
[^Gardner_Morikawa_1960]: C. S. Gardner and G. K. Morikawa, Courant Inst. Math. Sci. Rept, NYO-9082 (1960). <br> <https://archive.org/details/similarityinas00gard>
 [^KondoK_APSOS_2026]: K. Kondo, R. Matsui, and K. Imadera, APS Open Sci. **1**, 000051 (2026). <br> <https://doi.org/10.1103/qxpb-4w5y>