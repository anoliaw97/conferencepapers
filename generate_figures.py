#!/usr/bin/env python3
"""
Generate professional figures for IEEE conference paper
All titles and descriptions removed - text only in LaTeX captions
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

# Set style for professional IEEE conference appearance
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica']
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linewidth'] = 0.8

# Figure 1: Model Performance Trade-off
def generate_fig1():
    fig, ax = plt.subplots(figsize=(10, 7))

    # Data: (Processing Time, Quality Score, Model Size)
    models = {
        'olmOCR-7B': (36, 95, 7000),
        '4B': (81, 60, 4000),
        '8B': (150, 75, 8000),
        '30B-MoE': (300, 85, 30000)
    }

    colors = ['#E57373', '#64B5F6', '#FFB74D', '#81C784']

    for (name, (time, quality, size)), color in zip(models.items(), colors):
        # Bubble size proportional to model size (larger for better visibility)
        bubble_size = (size / 50) * 3
        ax.scatter(time, quality, s=bubble_size, c=color, alpha=0.7,
                  edgecolors='black', linewidth=2.0, zorder=3)

    ax.set_xlabel('Processing Time (minutes)', fontweight='bold')
    ax.set_ylabel('Extraction Quality Score (%)', fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--', zorder=1)
    ax.set_xlim(0, 320)
    ax.set_ylim(55, 100)

    # Add ticks for better readability
    ax.set_xticks([0, 50, 100, 150, 200, 250, 300])
    ax.set_yticks([60, 70, 80, 90, 100])

    # Thicker spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig1_model_performance.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig1_model_performance.png")

# Figure 2: Page Distribution
def generate_fig2():
    fig, ax = plt.subplots(figsize=(11, 6))

    categories = ['Data Tables', 'Graphs', 'Metadata', 'Blank/Irrelevant']
    counts = [691, 319, 264, 79]
    colors = ['#66BB6A', '#42A5F5', '#FFA726', '#BDBDBD']

    y_pos = np.arange(len(categories))

    bars = ax.barh(y_pos, counts, color=colors, edgecolor='black', linewidth=1.8, height=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)
    ax.set_xlabel('Number of Pages', fontweight='bold')
    ax.grid(axis='x', alpha=0.3, linestyle='--', zorder=0)
    ax.set_xlim(0, 750)
    ax.set_axisbelow(True)

    # Add better x-axis ticks
    ax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])

    # Thicker spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig2_page_distribution.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig2_page_distribution.png")

# Figure 3: Prompt Comparison
def generate_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Processing Time
    categories = ['Baseline', 'QC-Enhanced']
    times = [36, 280]
    colors_time = ['#42A5F5', '#EF5350']

    bars1 = ax1.bar(categories, times, color=colors_time, edgecolor='black',
                    linewidth=2.0, width=0.6)
    ax1.set_ylabel('Processing Time (minutes)', fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--', zorder=0)
    ax1.set_ylim(0, 300)
    ax1.set_axisbelow(True)

    # Classification Error Rate
    error_rates = [43, 0]
    colors_error = ['#EF5350', '#66BB6A']

    bars2 = ax2.bar(categories, error_rates, color=colors_error, edgecolor='black',
                    linewidth=2.0, width=0.6)
    ax2.set_ylabel('Classification Error Rate (%)', fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--', zorder=0)
    ax2.set_ylim(0, 50)
    ax2.set_axisbelow(True)

    # Thicker spines for both subplots
    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig3_prompt_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig3_prompt_comparison.png")

# Figure 4: Consolidation Funnel
def generate_fig4():
    fig, ax = plt.subplots(figsize=(11, 6))

    stages = ['Raw Column\nVariants', 'After Text\nNormalization',
              'Semantic\nGrouping', 'Final ML\nSchema']
    counts = [2856, 875, 318, 147]
    colors = ['#EF9A9A', '#FFCC80', '#90CAF9', '#A5D6A7']

    y_pos = np.arange(len(stages))

    bars = ax.barh(y_pos, counts, color=colors, edgecolor='black',
                   linewidth=1.8, height=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages)
    ax.set_xlabel('Number of Column Patterns', fontweight='bold')
    ax.grid(axis='x', alpha=0.3, linestyle='--', zorder=0)
    ax.set_xlim(0, 3000)
    ax.set_axisbelow(True)

    # Add better x-axis ticks
    ax.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000])

    # Thicker spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig4_consolidation.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig4_consolidation.png")

# Figure 5: Scalability
def generate_fig5():
    fig, ax = plt.subplots(figsize=(10, 7))

    # Data from the original figure
    doc_sizes = [17, 23, 28, 35, 42, 46, 55, 63, 189, 421]
    proc_times = [6.7, 12, 18, 25, 35, 40, 50, 36, 295, 874]

    # Linear regression
    coeffs = np.polyfit(doc_sizes, proc_times, 1)
    poly = np.poly1d(coeffs)
    x_line = np.linspace(0, 450, 100)
    y_line = poly(x_line)

    # Plot regression line first
    ax.plot(x_line, y_line, 'r--', linewidth=3, alpha=0.8, zorder=2,
            label=f'y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}')

    # Plot scatter points on top
    ax.scatter(doc_sizes, proc_times, s=200, c='#42A5F5', alpha=0.8,
              edgecolors='black', linewidth=2.0, zorder=3)

    ax.set_xlabel('Document Size (pages)', fontweight='bold')
    ax.set_ylabel('Processing Time (minutes)', fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--', zorder=1)
    ax.set_xlim(0, 450)
    ax.set_ylim(-50, 950)

    # Add better axis ticks
    ax.set_xticks([0, 100, 200, 300, 400])
    ax.set_yticks([0, 200, 400, 600, 800])

    # Thicker spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('fig5_scalability.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig5_scalability.png")

# Figure 6: Professional Workflow Flowchart
def generate_fig6():
    fig, ax = plt.subplots(figsize=(16, 5))

    # Turn off axis
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Define box positions and labels (centered vertically)
    boxes = [
        (1.5, 2.5, 'PDF to\nImages\n(200 DPI)'),
        (4.0, 2.5, 'Page\nClassification'),
        (6.5, 2.5, 'Table\nDetection'),
        (9.0, 2.5, 'Data\nExtraction'),
        (11.5, 2.5, 'Validation &\nStandardization'),
        (14.0, 2.5, 'JSON/CSV\nOutput')
    ]

    box_width = 2.2
    box_height = 1.8

    # Professional color scheme
    box_colors = ['#E3F2FD', '#BBDEFB', '#90CAF9', '#64B5F6', '#42A5F5', '#2196F3']

    # Draw boxes
    for idx, (x, y, label) in enumerate(boxes):
        # Create rounded rectangle box
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.08",
                             edgecolor='#1565C0',
                             facecolor=box_colors[idx],
                             linewidth=2.5,
                             zorder=2)
        ax.add_patch(box)

        # Add text with better formatting
        ax.text(x, y, label, ha='center', va='center',
               fontsize=13, fontweight='bold', color='#0D47A1',
               zorder=3)

    # Draw professional arrows between boxes
    arrow_y = 2.5
    for i in range(len(boxes) - 1):
        x1 = boxes[i][0] + box_width/2 + 0.05
        x2 = boxes[i+1][0] - box_width/2 - 0.05

        arrow = FancyArrowPatch((x1, arrow_y), (x2, arrow_y),
                               arrowstyle='-|>',
                               mutation_scale=30,
                               linewidth=3.0,
                               color='#1565C0',
                               zorder=1)
        ax.add_patch(arrow)

    # Add a subtle background
    bg_rect = Rectangle((0, 0), 16, 5, facecolor='white', edgecolor='none', zorder=0)
    ax.add_patch(bg_rect)

    plt.tight_layout()
    plt.savefig('fig6_workflow.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Generated fig6_workflow.png")

# Main execution
if __name__ == "__main__":
    print("=" * 70)
    print("Generating PROFESSIONAL figures for IEEE conference paper...")
    print("=" * 70)

    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()

    print("=" * 70)
    print("All figures generated successfully!")
    print("\nProfessional IEEE conference quality features:")
    print("  ✓ Larger, readable font sizes (14-16pt)")
    print("  ✓ Proper figure dimensions and aspect ratios")
    print("  ✓ No embedded titles (only in LaTeX captions)")
    print("  ✓ Clean, professional color schemes")
    print("  ✓ Thicker lines and borders for print quality")
    print("  ✓ High resolution (300 DPI)")
    print("  ✓ Professional flowchart design (Fig 6)")
    print("=" * 70)
