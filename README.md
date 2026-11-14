 Speed-Accuracy Trade-Off (SAT) Behavioral Analysis

An exploratory data analysis and statistical modeling pipeline examining human cognitive performance under speed pressure and spatial rotation load. 

---
 Overview
The Speed-Accuracy Trade-Off (SAT) is a core phenomenon in cognitive psychology and human-computer interaction: when people are rushed, accuracy drops; when they take their time, performance improves. 

This project analyzes a behavioral dataset of **18,808 trials across 160 participants** to investigate how instruction sets (speed vs. accuracy) interact with cognitive task difficulty ($0^\circ$ vs. $100^\circ$ spatial rotation).

Methodological Approach & Statistical Rigor
Working with trial-level behavioral data comes with a major statistical trap: **pseudoreplication** (treating thousands of trials as independent observations, which artificially inflates degrees of freedom and yields false-positive $p$-values). 

To ensure the statistics are publication-grade, the pipeline bypasses naive trial-level OLS and implements a **Clustered OLS Regression** (`cov_type='cluster'`), grouping standard errors by participant (`subj_idx`). This preserves all 18,808 data points while correctly accounting for intra-participant correlation.

 Key Findings
* **Baseline Performance (~91.9%):** Under accuracy instructions at $0^\circ$ rotation, participants maintain a high accuracy baseline ($\beta = 0.9189, p < 0.001$).
* **The Cost of Speed (~5.1% drop):** Shifting instructions to prioritize speed incurs an immediate accuracy penalty ($\beta = -0.0505, p = 0.010$).
* **The Cost of Mental Load (~9.5% drop):** Increasing spatial rotation difficulty to $100^\circ$ significantly impairs spatial transformation processing ($\beta = -0.0946, p < 0.001$).
* **Non-Additive Interaction ($\beta = -0.0563, p = 0.001$):** Speed pressure and task difficulty interact non-additively. When participants face high rotation complexity *while* being rushed, performance degrades significantly faster than expected from independent main effects.

Visualizations
The script generates a dual-panel figure combining:
1. **Interaction Heatmap:** A clear matrix view displaying exact cell means across conditions and difficulty levels.
2. **Point Plot with 95% Confidence Intervals:** Illustrates participant-level variability and highlights the statistical separation between speed and accuracy conditions.

