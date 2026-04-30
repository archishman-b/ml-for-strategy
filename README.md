# ML for Strategy — Field Guide & Hands-On Notebooks

> A practitioner's reference for ML in strategy consulting, analytics, and product engagements.  
> Built by [Archishman Bandyopadhyay](https://archishman-b.github.io/career-intelligence-map/) as part of a public strategy × AI portfolio.

---

## 📖 Start Here: The Master Playbook

**[→ ML Strategy Playbook (live)](https://archishman-b.github.io/ml-for-strategy/ML_Strategy_Playbook.html)**

A self-contained interactive reference covering 25 models across 7 families. Designed for strategy professionals who need to commission, review, and act on data science work — without writing code.

**What's inside:**
- 9 business-question categories (Predict, Quantify, Forecast, Segment, Explain, Intervene, Time, Detect, Understand)
- Interactive model selector — answer 3 questions, get a model recommendation with rationale
- Full quick-reference table: all 25 models at a glance
- Per-model: how it works, 4–6 real use case scenarios, tradeoffs, and *questions to ask your data science team*
- Evaluation & metrics reference
- 30-question pre-launch checklist (from data → deployment → monitoring → governance)

---

## 💻 Hands-On Notebooks

For each model: concept refresh → full worked example → edge cases → scenarios with code → what good vs red-flag output looks like.

| # | Model | Notebook | Family |
|---|-------|----------|--------|
| 1.1 | Logistic Regression | [01_logistic_regression.ipynb](notebooks/01_logistic_regression.ipynb) | Classification |
| 1.2 | Decision Tree | [02_decision_tree.ipynb](notebooks/02_decision_tree.ipynb) | Classification |
| 1.3 | Random Forest | [03_random_forest.ipynb](notebooks/03_random_forest.ipynb) | Classification |
| 1.4 | Gradient Boosting | [04_gradient_boosting.ipynb](notebooks/04_gradient_boosting.ipynb) | Classification |
| 1.5 | Naive Bayes | [05_naive_bayes.ipynb](notebooks/05_naive_bayes.ipynb) | Classification |
| 2.1 | Ridge / Lasso | [06_ridge_lasso_regression.ipynb](notebooks/06_ridge_lasso_regression.ipynb) | Regression |
| 2.2 | Gradient Boosting Reg. | [07_gbr_regression.ipynb](notebooks/07_gbr_regression.ipynb) | Regression |
| 2.3 | Quantile Regression | [08_quantile_regression.ipynb](notebooks/08_quantile_regression.ipynb) | Regression |
| 3.1 | K-Means | [09_kmeans.ipynb](notebooks/09_kmeans.ipynb) | Clustering |
| 3.2 | Hierarchical | [10_hierarchical_clustering.ipynb](notebooks/10_hierarchical_clustering.ipynb) | Clustering |
| 3.3 | GMM | [11_gmm.ipynb](notebooks/11_gmm.ipynb) | Clustering |
| 4.1 | PCA | [12_pca.ipynb](notebooks/12_pca.ipynb) | Dimensionality |
| 4.2 | UMAP | [13_umap.ipynb](notebooks/13_umap.ipynb) | Dimensionality |
| 5.1–5.3 | Time Series (Baseline/ARIMA/ML) | [16_time_series_forecasting.ipynb](notebooks/16_time_series_forecasting.ipynb) | Time Series |
| 6.1 | Survival Analysis | [14_survival_analysis.ipynb](notebooks/14_survival_analysis.ipynb) | Specialised |
| 6.2 | Uplift Modelling | [15_uplift_modelling.ipynb](notebooks/15_uplift_modelling.ipynb) | Specialised |
| 6.3 | Anomaly Detection | [18_anomaly_detection.ipynb](notebooks/18_anomaly_detection.ipynb) | Specialised |
| 6.4 | A/B Testing & Causal | [19_causal_inference.ipynb](notebooks/19_causal_inference.ipynb) | Specialised |
| 7.1–7.2 | Neural Nets & LLMs | [17_neural_networks.ipynb](notebooks/17_neural_networks.ipynb) | Modern AI |

---

## 📁 Data

Five sample datasets in `data/` used across all notebooks:

| File | Rows | Description | Used for |
|------|------|-------------|----------|
| `customers.csv` | 800 | Demographics, tenure, spend, churn flag | Classification, survival, clustering |
| `pricing.csv` | 600 | Product pricing, volume, margin, discount | Regression, quantile |
| `campaign.csv` | 500 | Treatment/control assignment, conversion | Uplift, A/B testing |
| `timeseries.csv` | 60 months | Revenue by region and category | All forecasting models |
| `anomalies.csv` | 1,000 | Transactions, ~3% flagged anomaly rate | Anomaly detection |

---

## 🗺 Portfolio

| Project | Description |
|---------|-------------|
| [Career Intelligence Map](https://archishman-b.github.io/career-intelligence-map/) | Skills & career analytics dashboard |
| [Portfolio Roadmap](https://archishman-b.github.io/portfolio-roadmap/) | Full 50-week build plan |
| [DataBridge](https://archishman-b.github.io/databridge/databridge.html) | No-code data workbench |
| **ML Strategy Playbook** | This repo |

---

*Strategy × AI × Product — building in public.*
