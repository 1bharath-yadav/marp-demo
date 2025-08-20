# chart.py
# Author: Technical Writer
# Contact: 24f1001694@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def generate_synthetic_engagement_data():
    # Simulate customer engagement (hours spent) for user segments over days
    np.random.seed(42)
    segments = ['New', 'Returning', 'Premium', 'Churn-risk']
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    data = np.random.gamma(shape=2.0, scale=1.5,
                           size=(len(segments), len(days))) * 10
    df = pd.DataFrame(data, index=segments, columns=days)
    return df


def create_and_save_heatmap(df):
    sns.set_style('whitegrid')               # professional styling
    sns.set_context('talk')                 # presentation-ready text sizes

    plt.figure(figsize=(8, 8), dpi=64)       # 8in × 64 DPI = 512 px
    # perceptually uniform palette
    cmap = sns.color_palette('viridis', as_cmap=True)

    ax = sns.heatmap(
        df,
        cmap=cmap,
        annot=True,
        fmt=".1f",
        linewidths=0.5,
        linecolor='gray',
        cbar_kws={'shrink': 0.8, 'label': 'Engagement (hours)'}
    )

    ax.set_title('Weekly Customer Engagement by Segment', pad=20)
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Customer Segment')

    plt.tight_layout()
    plt.savefig('chart.png', dpi=64, bbox_inches='tight')
    plt.close()


def main():
    df = generate_synthetic_engagement_data()
    create_and_save_heatmap(df)


if __name__ == "__main__":
    main()
