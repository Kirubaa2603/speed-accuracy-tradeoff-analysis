import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.formula.api as smf


df = pd.read_csv("data.csv") 
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
df.info()
print("\nMissing Values:\n", df.isnull().sum())
print("\nSummary Statistics:\n", df[['rt', 'response_accuracy', 'Angular_difference']].describe())


condition_summary = df.groupby('condition')[['rt', 'response_accuracy']].mean()
print("\nCondition Summary:\n", condition_summary) 

condition_diff = df.groupby(['condition', 'Angular_difference'])[['rt', 'response_accuracy']].mean()
print("\nCondition x Angular Difference Summary:\n", condition_diff) 


model_clustered = smf.ols(
    'response_accuracy ~ C(condition) * C(Angular_difference)', 
    data=df
).fit(cov_type='cluster', cov_kwds={'groups': df['subj_idx']})

print("\n--- ROBUST CLUSTERED REGRESSION TABLE (PUBLICATION-GRADE) ---")
print(model_clustered.summary())


df_subj = df.groupby(['subj_idx', 'condition', 'Angular_difference'])['response_accuracy'].mean().reset_index()
pivot_accuracy = condition_diff['response_accuracy'].unstack()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))


sns.heatmap(pivot_accuracy, annot=True, cmap="YlGnBu", fmt=".3f", cbar=True, cbar_kws={'label': 'Accuracy'}, ax=axes[0])
axes[0].set_xlabel("Rotation difficulty (0° easy, 100° hard)", fontsize=11)
axes[0].set_ylabel("Condition", fontsize=11)
axes[0].set_title('A. Speed-Accuracy Interaction Heatmap', fontsize=12, fontweight='bold')


sns.pointplot(
    data=df_subj, 
    x='Angular_difference', 
    y='response_accuracy', 
    hue='condition', 
    markers=['o', 's'], 
    linestyles=['-', '--'], 
    capsize=0.1, 
    err_kws={'linewidth': 1.5},
    palette='Set2',
    ax=axes[1]
)
axes[1].set_xlabel("Rotation Difficulty (0° easy, 100° hard)", fontsize=11)
axes[1].set_ylabel("Mean Response Accuracy", fontsize=12)
axes[1].set_title("B. Performance with 95% Confidence Intervals", fontsize=12, fontweight='bold')
axes[1].legend(title="Condition")
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()