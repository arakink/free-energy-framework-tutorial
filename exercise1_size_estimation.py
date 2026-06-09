import numpy as np
import matplotlib.pyplot as plt


def normpdf(x: np.ndarray | float, mean: np.ndarray | float, sigma: float) -> np.ndarray:
    """
    正規分布の確率密度を計算する。

    Args:
        x: 確率密度を評価する値
        mean: 正規分布の平均
        sigma: 正規分布の標準偏差

    Returns:
        x における正規分布の確率密度
    """
    coef = 1.0 / (np.sqrt(2.0 * np.pi) * sigma)
    return coef * np.exp(-0.5 * ((x - mean) / sigma) ** 2)


def g(v: np.ndarray) -> np.ndarray:
    """
    サイズから期待される観測値を計算する生成関数。

    Args:
        v: サイズの値

    Returns:
        各サイズに対する期待観測値
    """
    return v ** 2


def main() -> None:
    """
    事後分布 p(v|u) を数値的に計算し、グラフとして保存する。
    """
    v_p = 3.0
    sigma_p = 1.0
    sigma_u = 1.0
    u = 2.0

    min_v = 0.01
    dv = 0.01
    max_v = 5.0
    v_range = np.arange(min_v, max_v + 0.5 * dv, dv)

    numerator = normpdf(v_range, v_p, sigma_p) * normpdf(u, g(v_range), sigma_u)
    normalization = np.sum(numerator * dv)
    p = numerator / normalization

    plt.figure(figsize=(7, 4.5))
    plt.plot(v_range, p, "k")
    plt.xlabel("v")
    plt.ylabel("p(v|u)")
    plt.xlim(min_v, max_v)
    plt.tight_layout()
    plt.savefig("exercise1_posterior_size_plot.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
