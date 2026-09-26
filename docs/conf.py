# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Research notes'
copyright = '2026, Katsuya Kondo'
author = 'Katsuya Kondo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
"sphinx.ext.mathjax"]

templates_path = ['_templates']
exclude_patterns = []

source_suffix={".md":"markdown",
".rst": "restructuredtext"}

myst_enable_extensions = [
    "dollarmath",
    "amsmath"
]

mathjax3_config = {
    "tex": {
        "macros": {
            "bm": ["\\boldsymbol{#1}", 1],
        }
    }
}

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_math_renderer="mathjax"

html_theme_options={
    "description"="当サイトではアクセス数の把握のためにCookie技術およびGoogleアナリティクスを使用しています。このデータは匿名で収集されており、個人を特定するものではありません。この機能はCookieを無効にすることで収集を拒否することが出来るので、お使いのブラウザの設定をご確認ください。この規約に関しての詳細は<a href=https://marketingplatform.google.com/about/analytics/terms/jp/>Googleアナリティクスサービス利用規約</a>のページや<a href="https://policies.google.com/technologies/ads?hl=ja">Googleポリシーと規約ページ</a>をご覧ください。"
}

