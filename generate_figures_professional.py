#!/usr/bin/env python3
"""
Generate IEEE-ready figures sized for correct column width rendering.

IEEE single column = 3.5 inches. All source figures are saved at 2x print
size so fonts at 16pt render to exactly 8pt in the final PDF.

  - 0.8\\columnwidth display (2.8"): source figsize width = 5.6"
  - \\columnwidth display  (3.5"): source figsize width = 7.0"

Font sizes used:
  - axis labels / text labels: 16 pt  → 8 pt in paper
  - tick labels              : 14 pt  → 7 pt in paper (acceptable)
  - value annotations        : 14 pt  → 7 pt in paper
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# ------------------------------------------------------------------
# Global rcParams – tuned for 2x-scale IEEE figures
# ------------------------------------------------------------------
plt.rcParams.update({
    'font.family'       : 'sans-serif',
    'font.sans-serif'   : ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size'         : 16,          # base – renders ~8 pt in paper
    'axes.labelsize'    : 16,
    'axes.titlesize'    : 16,
    'xtick.labelsize'   : 14,
    'ytick.labelsize'   : 14,
    'legend.fontsize'   : 14,
    'axes.linewidth'    : 1.5,
    'grid.alpha'        : 0.3,
    'grid.linewidth'    : 0.8,
    'lines.linewidth'   : 2.0,
})

BLUE    = '#1E88E5'
RED     = '#E53935'
ORANGE  = '#FB8C00'
GREEN   = '#43A047'
GREY    = '#757575'

# ==================================================================
# Fig 1 – Model performance bubble chart   (0.8\columnwidth → 5.6" src)
# ==================================================================
def generate_fig1():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))

    models = {
        'olmOCR-7B': (36,  95,  7000, RED),
        '4B'       : (81,  60,  4000, BLUE),
        '8B'       : (150, 75,  8000, ORANGE),
        '30B-MoE'  : (300, 85, 30000, GREEN),
    }

    for name, (t, q, sz, c) in models.items():
        ax.scatter(t, q, s=sz / 60, c=c, alpha=0.75,
                   edgecolors='black', linewidth=1.5, zorder=3, label=name)

    ax.set_xlabel('Processing Time (min)', fontweight='bold')
    ax.set_ylabel('Quality Score (%)', fontweight='bold')
    ax.set_xlim(-10, 330)
    ax.set_ylim(55, 100)
    ax.set_xticks([0, 100, 200, 300])
    ax.set_yticks([60, 70, 80, 90, 100])
    ax.grid(True, linestyle='--', zorder=1)
    ax.legend(loc='lower right', frameon=True, framealpha=0.9,
              edgecolor='black', handlelength=1.0, handletextpad=0.4)
    for sp in ax.spines.values():
        sp.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig1_model_performance.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig1_model_performance.png")


# ==================================================================
# Fig 2 – Page distribution bar chart   (0.8\columnwidth → 5.6" src)
# ==================================================================
def generate_fig2():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))

    cats   = ['Data Tables', 'Graphs', 'Metadata', 'Blank/Irrelevant']
    counts = [691, 319, 264, 79]
    colors = [GREEN, BLUE, ORANGE, GREY]

    y = np.arange(len(cats))
    bars = ax.barh(y, counts, color=colors, edgecolor='black',
                   linewidth=1.2, height=0.6)

    for bar, cnt in zip(bars, counts):
        ax.text(bar.get_width() + 12, bar.get_y() + bar.get_height() / 2,
                str(cnt), va='center', fontsize=13, fontweight='bold')

    ax.set_yticks(y)
    ax.set_yticklabels(cats, fontsize=14)
    ax.set_xlabel('Number of Pages', fontweight='bold')
    ax.set_xlim(0, 780)
    ax.set_xticks([0, 200, 400, 600])
    ax.grid(axis='x', linestyle='--', zorder=0)
    ax.set_axisbelow(True)
    for sp in ax.spines.values():
        sp.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig2_page_distribution.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig2_page_distribution.png")


# ==================================================================
# Fig 3 – Prompt comparison dual bar   (\columnwidth → 7.0" src)
# ==================================================================
def generate_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.8))

    cats = ['Baseline', 'QC-Enhanced']

    # Left: processing time
    vals1  = [36, 280]
    cols1  = [BLUE, RED]
    bars1  = ax1.bar(cats, vals1, color=cols1, edgecolor='black',
                     linewidth=1.2, width=0.5)
    for b in bars1:
        ax1.text(b.get_x() + b.get_width() / 2, b.get_height() + 8,
                 str(int(b.get_height())),
                 ha='center', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Processing Time (min)', fontweight='bold')
    ax1.set_ylim(0, 320)
    ax1.grid(axis='y', linestyle='--', zorder=0)
    ax1.set_axisbelow(True)
    ax1.tick_params(axis='x', labelsize=14)
    for sp in ax1.spines.values():
        sp.set_linewidth(1.5)

    # Right: error rate
    vals2 = [43, 0]
    cols2 = [RED, GREEN]
    bars2 = ax2.bar(cats, vals2, color=cols2, edgecolor='black',
                    linewidth=1.2, width=0.5)
    for b in bars2:
        h = b.get_height()
        label = f'{int(h)}%'
        y_pos = h + 1.5 if h > 0 else 1.5
        ax2.text(b.get_x() + b.get_width() / 2, y_pos,
                 label, ha='center', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Classification Error Rate (%)', fontweight='bold')
    ax2.set_ylim(0, 52)
    ax2.grid(axis='y', linestyle='--', zorder=0)
    ax2.set_axisbelow(True)
    ax2.tick_params(axis='x', labelsize=14)
    for sp in ax2.spines.values():
        sp.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig3_prompt_comparison.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig3_prompt_comparison.png")


# ==================================================================
# Fig 4 – Consolidation funnel bar chart   (0.8\columnwidth → 5.6" src)
# ==================================================================
def generate_fig4():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))

    stages = ['Raw Variants', 'Text Norm.', 'Semantic Group.', 'Final Schema']
    counts = [2856, 875, 318, 147]
    colors = ['#EF9A9A', '#FFB74D', '#64B5F6', '#81C784']

    y = np.arange(len(stages))
    bars = ax.barh(y, counts, color=colors, edgecolor='black',
                   linewidth=1.2, height=0.6)

    for bar, cnt in zip(bars, counts):
        ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height() / 2,
                str(cnt), va='center', fontsize=13, fontweight='bold')

    ax.set_yticks(y)
    ax.set_yticklabels(stages, fontsize=14)
    ax.set_xlabel('Number of Column Patterns', fontweight='bold')
    ax.set_xlim(0, 3300)
    ax.set_xticks([0, 1000, 2000, 3000])
    ax.grid(axis='x', linestyle='--', zorder=0)
    ax.set_axisbelow(True)
    for sp in ax.spines.values():
        sp.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig4_consolidation.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig4_consolidation.png")


# ==================================================================
# Fig 5 – Scalability scatter + regression   (0.8\columnwidth → 5.6" src)
# ==================================================================
def generate_fig5():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))

    doc_sizes  = np.array([17, 23, 28, 35, 42, 46, 55, 63, 189, 421])
    proc_times = np.array([6.7, 12, 18, 25, 35, 40, 50, 36, 295, 874])

    coeffs = np.polyfit(doc_sizes, proc_times, 1)
    poly   = np.poly1d(coeffs)
    x_line = np.linspace(0, 440, 200)

    ax.plot(x_line, poly(x_line), 'r--', linewidth=2.5, alpha=0.85, zorder=2,
            label=f'y = {coeffs[0]:.2f}x {coeffs[1]:+.1f}')
    ax.scatter(doc_sizes, proc_times, s=60, c=BLUE, alpha=0.85,
               edgecolors='black', linewidth=1.2, zorder=3)

    ax.set_xlabel('Document Size (pages)', fontweight='bold')
    ax.set_ylabel('Processing Time (min)', fontweight='bold')
    ax.set_xlim(-10, 450)
    ax.set_ylim(-50, 950)
    ax.set_xticks([0, 100, 200, 300, 400])
    ax.set_yticks([0, 200, 400, 600, 800])
    ax.grid(True, linestyle='--', zorder=1)
    ax.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='black')
    for sp in ax.spines.values():
        sp.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig5_scalability.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig5_scalability.png")


# ==================================================================
# Fig 6 – Workflow flowchart   (\columnwidth → 7.0" src)
# ==================================================================
def generate_fig6():
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    ax.set_xlim(0, 7.0)
    ax.set_ylim(0, 2.8)
    ax.axis('off')

    stages = [
        (0.60, 1.40, 'PDF to\nImages\n(200 DPI)'),
        (1.75, 1.40, 'Page\nClassify'),
        (2.90, 1.40, 'Table\nDetect'),
        (4.05, 1.40, 'Data\nExtract'),
        (5.20, 1.40, 'Validate &\nStandardize'),
        (6.35, 1.40, 'JSON/CSV\nOutput'),
    ]

    bw = 1.00   # box width
    bh = 1.10   # box height

    # gradient blue palette
    face_colors = ['#E3F2FD', '#BBDEFB', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5']
    edge_color  = '#0D47A1'

    for idx, (x, y, label) in enumerate(stages):
        # drop shadow
        shadow = FancyBboxPatch((x - bw/2 + 0.025, y - bh/2 - 0.025),
                                bw, bh, boxstyle='round,pad=0.05',
                                facecolor='#BDBDBD', edgecolor='none',
                                alpha=0.4, zorder=1)
        ax.add_patch(shadow)

        box = FancyBboxPatch((x - bw/2, y - bh/2),
                             bw, bh, boxstyle='round,pad=0.05',
                             facecolor=face_colors[idx],
                             edgecolor=edge_color,
                             linewidth=2.0, zorder=2)
        ax.add_patch(box)

        # text – 16 pt renders to 8 pt at \columnwidth
        ax.text(x, y, label, ha='center', va='center',
                fontsize=16, fontweight='bold', color='#0D47A1', zorder=3)

    # arrows
    for i in range(len(stages) - 1):
        x1 = stages[i][0]   + bw/2 + 0.03
        x2 = stages[i+1][0] - bw/2 - 0.03
        arrow = FancyArrowPatch((x1, 1.40), (x2, 1.40),
                                arrowstyle='-|>',
                                mutation_scale=18,
                                linewidth=2.5,
                                color=edge_color, zorder=1)
        ax.add_patch(arrow)

    plt.tight_layout(pad=0.1)
    plt.savefig('fig6_workflow.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ fig6_workflow.png")


# ==================================================================
if __name__ == '__main__':
    print('Generating IEEE-sized figures (fonts render ≥8pt in paper)...')
    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()
    print('Done.')
