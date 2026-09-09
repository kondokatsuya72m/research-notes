# 電磁ポテンシャルとゲージ変換
本稿では電磁場の電磁ポテンシャルとゲージ変換について説明します [^Sunagawa_2012]。静電場の静電ポテンシャル$\phi_s$と静磁場のベクトルポテンシャル$\bm{A}$は次のように定義されます。

$$
\bm{E} = -\nabla\phi_s \tag{1.1}
$$

$$
\bm{B} = \nabla \times \bm{A} \tag{1.2}
$$

このうち(1.2)は$\nabla\cdot\bm{B}=0$に基づいて定義されるので時間変化のある電磁場でも成り立ちます。一方で(1.1)は静電場に基づいているので、変位電流の効果を取り込むためにファラデーの法則を使った一般的な形に拡張する必要があります。ファラデーの法則を書き下すと

$$
\nabla\times\bm{E} = -\frac{1}{c}\frac{\partial \bm{B}}{\partial t} \tag{1.3}
$$

なので、これに(1.2)を代入して微分演算の順番を入れ替えると

$$
\nabla\times\bm{E} = -\nabla\times\frac{1}{c}\frac{\partial \bm{A}}{\partial t} \tag{1.4}
$$

となり、

$$
\nabla \times \left(\bm{E}+ \frac{1}{c}\frac{\partial \bm{A}}{\partial t}\right) = 0 \tag{1.5}
$$

となります。したがって

$$
\bm{E}+ \frac{1}{c}\frac{\partial \bm{A}}{\partial t} = -\nabla \phi \tag{1.6}
$$

と置くことができます。これが誘導電場を含めた電場のポテンシャルです。この$\phi$と$\bm{A}$を合わせて**電磁ポテンシャル**と呼びます。その定義を改めて書き下すと

$$
\bm{E} = -\nabla \phi - \frac{1}{c}\frac{\partial \bm{A}}{\partial t} \tag{1.7}
$$

$$
\bm{B} = \nabla \times \bm{A} \tag{1.8}
$$

となります。

Maxwell方程式のうちファラデーの法則$\nabla\times\bm{E}$、磁場の発散の式$\nabla\cdot\bm{B}$の式はこれらの式の前提条件になっているので自明になります。ガウスの法則$\nabla\cdot\bm{E}$とアンペールの法則$\nabla\times\bm{B}$の式は

$$
\nabla^2\phi +\frac{1}{c}\frac{\partial}{\partial t}(\nabla\cdot\bm{A}) = -4\pi \rho \tag{1.9}
$$

$$
\nabla^2 \bm{A} -\nabla(\nabla\cdot\bm{A}) 
= \frac{4\pi}{c}\bm{i} +\frac{1}{c^2}\frac{\partial}{\partial t}(\nabla\phi) \tag{1.10}
$$

となります。これが電磁ポテンシャル形式でのMaxwell方程式です。

## ゲージ変換
電磁ポテンシャルは一意ではなく、任意なスカラー関数$u$を用いて変換することができます。具体的に言えば、

$$
\phi' = \phi -\frac{\partial u}{\partial t} \tag{2.1}
$$

$$
\bm{A}' = \bm{A} + \nabla{u} \tag{2.2}
$$

で定義される新たな電磁ポテンシャル$(\phi', \bm{A}')$も同じ表式の$\bm{E},\bm{B}$を与え、Maxwell方程式を満たします。このように電磁ポテンシャルを変換することを**ゲージ変換**といいます[^Sunagawa_2012]。

## クーロンゲージ
(1.9)と(1.10)をより見通しよく記述するためのゲージを探してみましょう。まず(1.9)式に着目して、$\nabla\cdot\bm{A}_c=0$となるようなゲージを考えましょう。すると(1.9)、(1.10)は

$$
\nabla^2\phi_c  = -4\pi \rho \tag{3.1}
$$

$$
\nabla^2 \bm{A}_c
= \frac{4\pi}{c}\bm{i} -\frac{1}{c}\frac{\partial}{\partial t}(\nabla\phi) \tag{3.2}
$$

となります。定常な場を考えて$\partial/\partial t=0$とすると、(3.1),(3.2)は4本のポアソン方程式になります。このようなゲージを**クーロンゲージ**と呼びます。

## ローレンツゲージ
より対称性の高いゲージ変換を考えましょう。(1.9)で$\nabla\cdot\bm{A}$を消したいわけですが、もし

$$
\nabla\cdot \bm{A}_L = -\frac{1}{c}\frac{\partial \phi_L}{\partial t} \tag{4.1}
$$

なる関係が成り立つならば、(1.9)は

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2 }{\partial t^2}\right)\phi_L 
= 4\pi\rho \tag{4.2}
$$

なる関係が成り立ちます。これは真空$\rho=0$では$\phi$について波動方程式となっており見通しがよいといえるでしょう。さらに(1.10)を(4.1)を使って$\phi$が消えるように変形してみると

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2 }{\partial t^2}\right)\bm{A}_L 
= \frac{4\pi}{c}\bm{i} \tag{4.3}
$$

となります。すなわちMaxwell方程式を4本の波動方程式で記述できたことになり、有用なゲージ変換が施せたといえるでしょう。このようなゲージを**ローレンツゲージ**と呼びます [^Sunagawa_2023]。

これにさらに次のような４次元演算子を定義してみます。

$$
\Box = \left(\nabla^2-\frac{1}{c^2}\frac{\partial^2 }{\partial t^2}\right) \tag{4.4}
$$

$$
\bm{A}_4 = (\phi, A_x, A_y, A_z) \tag{4.5}
$$

$$
\bm{i}_4 = (c\rho, i_x, i_y, i_z) \tag{4.6}
$$

(4.4)で定義される演算子をダランベルシアンと呼びます。これらの定義を用いると(4.2),(4.3)は

$$
\Box \bm{A}_4 = \frac{4\pi}{c}\bm{i}_4 \tag{4.7}
$$

と1本の方程式で記述することができます。これがミンコフスキー空間でのMaxwell方程式です。

## 参考文献
[^Sunagawa_2012]: 第5章 マクスウェルの方程式, 電磁気学 (物理テキストシリーズ), 砂川重信, 岩波書店. 2012年.

[^Sunagawa_2023]: 第8章 電磁波, 理論電磁気学, 砂川重信, 紀伊国屋書店. 2023年.