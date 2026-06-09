# free-energy-framework-tutorial

自由エネルギーフレームワークのチュートリアル論文を読みながら、ベイズ推定・勾配上昇・予測誤差ノードによる実装を確認するための学習用リポジトリです。

## 内容

このフォルダには、3つの練習問題に対応する Python ファイルがあります。

- `exercise1_size_estimation.py`
  - 観測 `u=2` を固定し、候補 `v` ごとの事後分布 `p(v|u)` を数値的に計算します。
- `exercise2_phi_simulation.py`
  - 事後分布全体ではなく、代表値 `phi` を勾配上昇で更新し、もっともらしいサイズへ近づけます。
- `exercise3_factor_graph_simulation.py`
  - `phi`、事前誤差 `epsilon_p`、感覚誤差 `epsilon_u` を別ノードとして持つ形で、予測符号化風の時間発展をシミュレーションします。

各ファイルの数理的な解説は `docs/` にあります。

## セットアップ

環境を汚さないため、仮想環境を使います。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy matplotlib
```

このリポジトリでは `.venv/` は Git 管理対象外です。

## 実行方法

仮想環境を有効化した状態で実行します。

```bash
python exercise1_size_estimation.py
python exercise2_phi_simulation.py
python exercise3_factor_graph_simulation.py
```

画面表示が不要で PNG だけ生成したい場合は、次のように実行できます。

```bash
MPLBACKEND=Agg MPLCONFIGDIR=.mplconfig python exercise1_size_estimation.py
MPLBACKEND=Agg MPLCONFIGDIR=.mplconfig python exercise2_phi_simulation.py
MPLBACKEND=Agg MPLCONFIGDIR=.mplconfig python exercise3_factor_graph_simulation.py
```

`.mplconfig/` は Matplotlib のローカル設定・キャッシュ用で、Git 管理対象外です。

## 生成される画像

実行すると、各スクリプトから PNG が生成されます。

- `exercise1_size_plot.png`
- `exercise2_phi_trajectory.png`
- `exercise3_factor_graph_plot.png`

PNG ファイルは `.gitignore` で除外しています。

## ドキュメント

- `docs/exercise1_size_estimation.md`
  - ベイズの定理と `p(v|u)` のグラフの意味
- `docs/exercise2_phi_simulation.md`
  - `F` の最大化、`dphi/dt = dF/dphi`、`phi` の時間発展
- `docs/exercise3_factor_graph_simulation.md`
  - 予測誤差ノード、式(13)(14)、因子グラフ形式での実装

## 参考文献

- Rafal Bogacz, *A tutorial on the free-energy framework for modelling perception and learning*
- DOI: `10.1016/j.jmp.2015.11.003`
- The original article is distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
