#!/usr/bin/env python3
"""
Generate PROFESSIONAL IEEE-quality figures with dramatic visual improvements
- Large, readable fonts (18-22pt)
- Professional color schemes
- Thick borders and lines
- Optimal sizing for publication
- Clean, modern design
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import matplotlib as mpl

# Professional IEEE style settings
plt.style.use('seaborn-v0_8-darkgrid')
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.labelsize'] = 22
mpl.rcParams['axes.titlesize'] = 24
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18
mpl.rcParams['legend.fontsize'] = 16
mpl.rcParams['axes.linewidth'] = 2.5
mpl.rcParams['grid.alpha'] = 0.25
mpl.rcParams['grid.linewidth'] = 1.0
mpl.rcParams['lines.linewidth'] = 3.0

# Professional color palette
COLORS = {
    'red': '#E53935',
    'blue': '#1E88E5',
    'orange': '#FB8C00',
    'green': '#43A047',
    'purple': '#8E24AA',
    'teal': '#00897B',
    'pink': '#D81B60',
    'indigo': '#3949AB',
    'lime': '#7CB342',
    'cyan': '#00ACC1'
}

# Figure 1: Model Performance Trade-off with LEGEND
def generate_fig1():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Data: (Processing Time, Quality Score, Model Size)
    models = {
        'olmOCR-7B': (36, 95, 7000, COLORS['red']),
        '4B': (81, 60, 4000, COLORS['blue']),
        '8B': (150, 75, 8000, COLORS['orange']),
        '30B-MoE': (300, 85, 30000, COLORS['green'])
    }

    # Plot each model
    for name, (time, quality, size, color) in models.items():
        bubble_size = (size / 30) * 3  # Larger bubbles
        ax.scatter(time, quality, s=bubble_size, c=color, alpha=0.75,
                  edgecolors='black', linewidth=3.0, zorder=3, label=name)

    ax.set_xlabel('Processing Time (minutes)', fontweight='bold', labelpad=10)
    ax.set_ylabel('Extraction Quality Score (%)', fontweight='bold', labelpad=10)
    ax.grid(True, alpha=0.3, linestyle='--', zorder=1, linewidth=1.5)
    ax.set_xlim(-10, 330)
    ax.set_ylim(55, 100)

    ax.set_xticks([0, 50, 100, 150, 200, 250, 300])
    ax.set_yticks([60, 70, 80, 90, 100])

    # Add legend
    ax.legend(loc='lower right', frameon=True, fancybox=True, shadow=True,
             framealpha=0.95, edgecolor='black', facecolor='white')

    # Thicker spines
    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    plt.tight_layout()
    plt.savefig('fig1_model_performance.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig1_model_performance.png")

# Figure 2: Page Distribution with VALUE LABELS
def generate_fig2():
    fig, ax = plt.subplots(figsize=(12, 7))

    categories = ['Data Tables', 'Graphs', 'Metadata', 'Blank/Irrelevant']
    counts = [691, 319, 264, 79]
    colors = [COLORS['green'], COLORS['blue'], COLORS['orange'], '#9E9E9E']

    y_pos = np.arange(len(categories))

    bars = ax.barh(y_pos, counts, color=colors, edgecolor='black',
                   linewidth=2.5, height=0.65)

    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts)):
        width = bar.get_width()
        ax.text(width + 20, bar.get_y() + bar.get_height()/2,
               f'{count}', ha='left', va='center', fontsize=18, fontweight='bold')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=20, fontweight='bold')
    ax.set_xlabel('Number of Pages', fontweight='bold', labelpad=10)
    ax.grid(axis='x', alpha=0.3, linestyle='--', zorder=0, linewidth=1.5)
    ax.set_xlim(0, 800)
    ax.set_axisbelow(True)
    ax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])

    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    plt.tight_layout()
    plt.savefig('fig2_page_distribution.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig2_page_distribution.png")

# Figure 3: Prompt Comparison with VALUE LABELS
def generate_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    categories = ['Baseline', 'QC-Enhanced']

    # Processing Time
    times = [36, 280]
    colors_time = [COLORS['blue'], COLORS['red']]

    bars1 = ax1.bar(categories, times, color=colors_time, edgecolor='black',
                    linewidth=2.5, width=0.55)

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 10,
                f'{int(height)}', ha='center', va='bottom',
                fontsize=18, fontweight='bold')

    ax1.set_ylabel('Processing Time (minutes)', fontweight='bold', labelpad=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--', zorder=0, linewidth=1.5)
    ax1.set_ylim(0, 320)
    ax1.set_axisbelow(True)
    ax1.tick_params(axis='x', labelsize=20)

    # Classification Error Rate
    error_rates = [43, 0]
    colors_error = [COLORS['red'], COLORS['green']]

    bars2 = ax2.bar(categories, error_rates, color=colors_error, edgecolor='black',
                    linewidth=2.5, width=0.55)

    # Add value labels
    for bar in bars2:
        height = bar.get_height()
        if height > 0:
            ax2.text(bar.get_x() + bar.get_width()/2, height + 2,
                    f'{int(height)}%', ha='center', va='bottom',
                    fontsize=18, fontweight='bold')
        else:
            ax2.text(bar.get_x() + bar.get_width()/2, 2,
                    '0%', ha='center', va='bottom',
                    fontsize=18, fontweight='bold')

    ax2.set_ylabel('Classification Error Rate (%)', fontweight='bold', labelpad=10)
    ax2.grid(axis='y', alpha=0.3, linestyle='--', zorder=0, linewidth=1.5)
    ax2.set_ylim(0, 52)
    ax2.set_axisbelow(True)
    ax2.tick_params(axis='x', labelsize=20)

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_linewidth(2.5)

    plt.tight_layout()
    plt.savefig('fig3_prompt_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig3_prompt_comparison.png")

# Figure 4: Consolidation Funnel with VALUE LABELS
def generate_fig4():
    fig, ax = plt.subplots(figsize=(12, 7))

    stages = ['Raw Column\nVariants', 'After Text\nNormalization',
              'Semantic\nGrouping', 'Final ML\nSchema']
    counts = [2856, 875, 318, 147]
    colors = ['#EF9A9A', '#FFB74D', '#64B5F6', '#81C784']

    y_pos = np.arange(len(stages))

    bars = ax.barh(y_pos, counts, color=colors, edgecolor='black',
                   linewidth=2.5, height=0.65)

    # Add value labels
    for i, (bar, count) in enumerate(zip(bars, counts)):
        width = bar.get_width()
        ax.text(width + 80, bar.get_y() + bar.get_height()/2,
               f'{count}', ha='left', va='center', fontsize=18, fontweight='bold')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=19, fontweight='bold')
    ax.set_xlabel('Number of Column Patterns', fontweight='bold', labelpad=10)
    ax.grid(axis='x', alpha=0.3, linestyle='--', zorder=0, linewidth=1.5)
    ax.set_xlim(0, 3200)
    ax.set_axisbelow(True)
    ax.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000])

    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    plt.tight_layout()
    plt.savefig('fig4_consolidation.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig4_consolidation.png")

# Figure 5: Scalability with REGRESSION EQUATION
def generate_fig5():
    fig, ax = plt.subplots(figsize=(11, 8))

    doc_sizes = np.array([17, 23, 28, 35, 42, 46, 55, 63, 189, 421])
    proc_times = np.array([6.7, 12, 18, 25, 35, 40, 50, 36, 295, 874])

    # Linear regression
    coeffs = np.polyfit(doc_sizes, proc_times, 1)
    poly = np.poly1d(coeffs)
    x_line = np.linspace(0, 450, 100)
    y_line = poly(x_line)

    # Plot regression line with equation
    ax.plot(x_line, y_line, 'r--', linewidth=4, alpha=0.8, zorder=2,
            label=f'y = {coeffs[0]:.2f}x + {coeffs[1]:.1f}')

    # Plot scatter points
    ax.scatter(doc_sizes, proc_times, s=300, c=COLORS['blue'], alpha=0.8,
              edgecolors='black', linewidth=2.5, zorder=3)

    ax.set_xlabel('Document Size (pages)', fontweight='bold', labelpad=10)
    ax.set_ylabel('Processing Time (minutes)', fontweight='bold', labelpad=10)
    ax.grid(True, alpha=0.3, linestyle='--', zorder=1, linewidth=1.5)
    ax.set_xlim(-20, 460)
    ax.set_ylim(-50, 950)

    ax.set_xticks([0, 100, 200, 300, 400])
    ax.set_yticks([0, 200, 400, 600, 800])

    # Add legend with equation
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True,
             framealpha=0.95, edgecolor='black', facecolor='white', fontsize=18)

    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

    plt.tight_layout()
    plt.savefig('fig5_scalability.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig5_scalability.png")

# Figure 6: PROFESSIONAL FLOWCHART with shadows and gradients
def generate_fig6():
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.set_xlim(0, 18)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Define stages
    stages = [
        (1.8, 3.0, 'PDF to\nImages\n(200 DPI)'),
        (4.5, 3.0, 'Page\nClassification'),
        (7.2, 3.0, 'Table\nDetection'),
        (9.9, 3.0, 'Data\nExtraction'),
        (12.6, 3.0, 'Validation &\nStandardization'),
        (15.3, 3.0, 'JSON/CSV\nOutput')
    ]

    box_width = 2.4
    box_height = 2.0

    # Professional gradient color scheme
    colors = ['#E3F2FD', '#BBDEFB', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5']

    # Draw boxes with shadows
    for idx, (x, y, label) in enumerate(stages):
        # Shadow
        shadow = FancyBboxPatch(
            (x - box_width/2 + 0.05, y - box_height/2 - 0.05),
            box_width, box_height,
            boxstyle="round,pad=0.1",
            edgecolor='none',
            facecolor='gray',
            alpha=0.3,
            zorder=1
        )
        ax.add_patch(shadow)

        # Main box
        box = FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.1",
            edgecolor='#0D47A1',
            facecolor=colors[idx],
            linewidth=3.5,
            zorder=2
        )
        ax.add_patch(box)

        # Text
        ax.text(x, y, label, ha='center', va='center',
               fontsize=16, fontweight='bold', color='#0D47A1', zorder=3)

    # Draw professional arrows
    arrow_y = 3.0
    for i in range(len(stages) - 1):
        x1 = stages[i][0] + box_width/2 + 0.1
        x2 = stages[i+1][0] - box_width/2 - 0.1

        arrow = FancyArrowPatch(
            (x1, arrow_y), (x2, arrow_y),
            arrowstyle='-|>',
            mutation_scale=35,
            linewidth=4.0,
            color='#0D47A1',
            zorder=1
        )
        ax.add_patch(arrow)

    # Background
    bg_rect = Rectangle((0, 0), 18, 6, facecolor='white', edgecolor='none', zorder=0)
    ax.add_patch(bg_rect)

    plt.tight_layout()
    plt.savefig('fig6_workflow.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Generated fig6_workflow.png")

# Main execution
if __name__ == "__main__":
    print("=" * 80)
    print("GENERATING PROFESSIONAL IEEE-QUALITY FIGURES")
    print("=" * 80)

    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()

    print("=" * 80)
    print("SUCCESS! All figures generated with professional enhancements:")
    print("  ✓ Large fonts (18-22pt) - highly readable")
    print("  ✓ Value labels on all bar charts")
    print("  ✓ Legends with model names")
    print("  ✓ Thick borders (2.5-4pt) - print quality")
    print("  ✓ Professional color schemes")
    print("  ✓ Shadows and depth on flowchart")
    print("  ✓ 300 DPI resolution")
    print("  ✓ Optimal sizing for IEEE publications")
    print("=" * 80)
