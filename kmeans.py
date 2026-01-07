import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns

# 1. LOAD DATA
df = pd.read_csv(r"D:\Document\Project Dasprog\ML Kmeans\ispu_dki_all t.csv")
df.columns = df.columns.str.lower().str.strip()

# 2. PILIH FITUR (TANPA LABEL) + IMPUTASI
features = ['pm25', 'pm10', 'so2', 'co', 'o3', 'no2']

# (imputasi median global)
df_ml = df[features].copy()
df_ml = df_ml.fillna(df_ml.median(numeric_only=True))

# 3. STANDARDISASI
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_ml)

# 4. K-MEANS
k = 3
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
df_ml['cluster'] = clusters

# Gabungkan kembali ke dataframe utama (pakai index yang sama)
df = df.loc[df_ml.index].copy()
df['cluster'] = clusters

# 5. VISUALISASI (CO vs CLUSTER)
#    -> jangan overwrite scaler training, buat scaler khusus CO
co_scaler = StandardScaler()
df['co_z'] = co_scaler.fit_transform(df[['co']])

plt.figure(figsize=(10,6))
sns.stripplot(
    data=df,
    x='cluster',
    y='co_z',
    hue='stasiun',
    jitter=True,
    alpha=0.7
)

plt.title("Distribusi CO (Z-score) per Cluster K-Means")
plt.xlabel("Cluster")
plt.ylabel("CO (Z-score)")
plt.legend(title="Stasiun", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 6. DISTRIBUSI CLUSTER vs ISPU
print("\nDistribusi Cluster vs ISPU:")
print(pd.crosstab(df['cluster'], df['categori']))

# 7. STATISTIK POLUTAN PER CLUSTER (mean mentah, tetap boleh untuk laporan)
cluster_stats = (
    df.groupby('cluster')[features]
    .mean()
    .round(2)
)
print("\nRata-rata Polutan per Cluster (nilai asli):")
print(cluster_stats)

# 8. DISTRIBUSI ISPU (%)
cluster_ispu = (
    pd.crosstab(df['cluster'], df['categori'], normalize='index') * 100
).round(2)
print("\nDistribusi ISPU per Cluster (%):")
print(cluster_ispu)

# 9. TABEL INTERPRETASI CLUSTER (DOMINANSI BERBASIS Z-SCORE)
#    -> lebih valid karena K-Means dilatih di ruang standar
df_z = pd.DataFrame(X_scaled, columns=features, index=df_ml.index)
df_z['cluster'] = clusters

# rata-rata z-score per cluster
z_cluster_mean = df_z.groupby('cluster')[features].mean().round(2)

print("\nRata-rata Z-score per Cluster (ruang standardisasi):")
print(z_cluster_mean)

interpretasi = []
for c in z_cluster_mean.index:
    # polutan "paling tinggi relatif terhadap rata-rata dataset"
    polutan_dominan = z_cluster_mean.loc[c].sort_values(ascending=False).index[:2]
    ispu_dominan = cluster_ispu.loc[c].idxmax()

    interpretasi.append({
        "Cluster": c,
        "Polutan Dominan (Z-score)": ", ".join(polutan_dominan),
        "ISPU Dominan": ispu_dominan
    })

tabel_interpretasi = pd.DataFrame(interpretasi)

print("\nTabel Interpretasi Cluster (lebih fair):")
print(tabel_interpretasi)