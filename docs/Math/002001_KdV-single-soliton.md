# KdV方程式の1ソリトン解
ここでは次のKdV方程式の1ソリトン解を導出します。

$$
\frac{\partial f}{\partial \tau} +\alpha f\frac{\partial f}{\partial \xi}+\beta\frac{\partial^3 f}{\partial\xi^3}=0
$$

実際には、例えば$f\to f/\alpha$と置き換えると非線形項の係数も1のKdV方程式へ移行できる [^watanabe_book] ように、係数の自由度は1つ低くすることができます。ここではそのような乗り換えをせずに$\alpha,\beta$を含む形の1ソリトン解を導出します。

ここで次の仮定をおきましょう。

1. $x\to\pm\infty$ で $f\to 0, f'\to 0, f''\to 0$である。
1. 常に $ f \gt 0 $ である。
1. 初期条件 $f'(0)=0$ を満たす。
1. 定常解である。つまり波形が時間変化しない。

条件4から$f=f(\xi -c\tau)$という解を考えます。ここで$c$は伝播速度を表します。これをKdV方程式に代入すると、

$$
-cf' + \alpha ff'+\beta f'''=0
$$

となります。これを$x=x$から$\infty$で積分して

$$
-cf+\frac{\alpha}{2}f^2 +\beta f'' =0　
$$

となります。$f'$をかけると各項はさらに積分できて、

$$
-\frac{c}{2}f^2+\frac{\alpha}{6}f^3+\frac{\beta}{2}(f')^2 =0
$$

となります。これを$f'$について整理すると次になります。

$$
f'=\pm\sqrt{\frac{c}{\beta}}f\sqrt{1-\frac{\alpha}{3c}f} \tag{1}
$$

ここで初期条件についての仮定$f'(0)=0$から$x=0$で

$$
1-\frac{\alpha}{3c}f(0)=0 \Leftrightarrow f(0)=\frac{3c}{\alpha}
$$

を得ます。

(1)は変数分離型の微分方程式 [^kasahara_book] なので、整理して$x=0$から$x=x$まで積分を実行すると、下限には初期条件をそのまま代入して

$$
\pm\sqrt{\frac{c}{\beta}}x= \int^{f(x)}_{\frac{3c}{\alpha}}\frac{df}{f\sqrt{1-\frac{\alpha}{3c}f}}
$$

となります。

ここで$u=1/f$という変数変換を行います。すると

$$
du=-\frac{df}{f^2}=-u^2df
$$

だから、

$$
\pm\sqrt{\frac{c}{\beta}}x= -\int^{1/f(x)}_{\frac{\alpha}{3c}}\frac{du}{u\sqrt{1-\frac{\alpha}{3cu}}} \\
=-\int^{1/f(x)}_{\frac{\alpha}{3c}}\frac{du}{\sqrt{u^2-\frac{\alpha u}{3c}}}
$$

となります。平方完成して

$$
\pm\sqrt{\frac{c}{\beta}}x= -\int^{1/f(x)}_{\frac{\alpha}{3c}}\frac{du}{\sqrt{\left(u-\frac{\alpha}{6c}\right)^2-\frac{\alpha^2}{36c^2}}} \\
$$

となるから、$v=u-\alpha/6c$と置き換えて

$$
\pm\sqrt{\frac{c}{\beta}}x= -\int^{\frac{1}{f(x)}-\frac{\alpha}{3c}}_{\frac{\alpha}{6c}}\frac{du}{\sqrt{v^2 - \left(\frac{\alpha}{6c}\right)^2}}
$$

となります。ここで次の積分の公式を用います。双曲線関数を用いると容易に証明できます。

$$
\int \frac{dx}{\sqrt{x^2-a^2}}=\log(x+\sqrt{x^2-a^2})
$$

を用いると、

$$
\pm\sqrt{\frac{c}{\beta}}x 
= -\log\left( 
    \frac{1}{f(x)}-\frac{\alpha}{6c}+
    \sqrt{
        \left(
            \frac{1}{f(x)}-\frac{\alpha}{6c}
            \right)^2
    }\right)
    +\log\left(\frac{\alpha}{6c}\right)
$$

となり、整理して

$$
\pm\sqrt{\frac{c}{\beta}}x 
= -\log\left( 
    \frac{6c}{\alpha f} -1 + \sqrt{
        \left( \frac{6c}{\alpha f}-1\right)^2-1
    }
    \right)
$$

となります。指数関数を取って

$$
\frac{6c}{\alpha f} -1 + \sqrt{
    \left( \frac{6c}{\alpha f}-1\right)^2-1
    }
    =\exp\left(\pm\sqrt{\frac{c}{\beta}}x\right)
$$

となります。左辺に平方根を残してそれ以外を右辺へ移項して両辺二乗すると

$$
\left( \frac{6c}{\alpha f}-1\right)^2-1 
= \left(
    \exp\left(\pm\sqrt{\frac{c}{\beta}}x\right)
    -\left( \frac{6c}{\alpha f} -1 \right)
    \right)^2
$$

となり、右辺を展開して整理すると

$$
    2\exp\left(\pm\sqrt{\frac{c}{\beta}}x\right)\left( \frac{6c}{\alpha f}-1\right)
    = \exp\left(\pm 2\sqrt{\frac{c}{\beta}}x\right)+1
$$

となります。両辺$2\exp\left(\pm\sqrt{\frac{c}{\beta}}x\right)$で割ると

$$
\frac{6c}{\alpha f}-1 
    = \frac{\mathrm{e}^{\pm\sqrt{\frac{c}{\beta}}x}+\mathrm{e}^{\pm\sqrt{\frac{c}{\beta}}x}}{2}
    = \mathrm{cosh}\left(\sqrt{\frac{c}{\beta}}x \right)
$$

となります。coshは偶関数なので$\pm$はここでうまく消えます。双曲線関数の半角の公式を用いて

$$
\frac{6c}{\alpha f} = 1 +\mathrm{cosh}\left(\sqrt{\frac{c}{\beta}}x \right) \\
=2\mathrm{cosh}^2 \left( \frac{1}{2}\sqrt{\frac{c}{\beta}}x \right)
$$

となり、最終的に

$$
f(\xi-c\tau) 
    = \frac{6c}{2\alpha}
        \mathrm{sech}^2 \left(
            \frac{1}{2}\sqrt{\frac{c}{\beta}}(\xi -c\tau)
            \right) \tag{2}
$$

を得ます。

$A\equiv 3c/\alpha$ とおきます。このとき$c=(\alpha /3) A$だから、(2)は

$$
    f=A \mathrm{sech}^2 \left(
            \frac{1}{2}\sqrt{\frac{A}{3}\frac{\alpha}{\beta}} (\xi -\frac{\alpha A}{3}\tau)
            \right) 
$$

となります。つまりソリトンの特徴（振幅、幅、速度）は1つの自由度で決定されることがわかります。

# 参考文献
[^watanabe_book]: 渡辺慎介、「2-5 K-dV方程式の係数の変更」.「ソリトン物理入門」.p31-35. 培風館.
[^kasahara_book]: 笠原浩司、「2.1 変数分離型」.「微分方程式の基礎」 p7（数理科学ライブラリー）, 朝倉書店.