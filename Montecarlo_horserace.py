import numpy as np
from collections import Counter

# モデルの平均と標準偏差
horses = {
    'A': (73.0, 0.8),
    'B': (74.5, 1.0),
    'C': (73.5, 1.2)
}

n_trials = 100000
results = []

for _ in range(n_trials):
    # 各馬のタイムをランダムに生成
    sampled = {k: np.random.normal(mu, sigma) for k, (mu, sigma) in horses.items()}
    # タイムで並べ替えて着順を記録
    ordered = tuple(sorted(sampled, key=sampled.get))
    results.append(ordered)

# 結果を集計
counts = Counter(results)

# 出現確率を表示
for pattern, count in counts.most_common():
    prob = count / n_trials * 100
    print(f"{pattern}: {prob:.2f}%")
