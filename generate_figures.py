#!/usr/bin/env python3
"""
Generate clean figures for IEEE conference paper
All titles and descriptions removed - text only in LaTeX captions
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Set style for professional appearance
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['grid.alpha'] = 0.3

# Figure 1: Model Performance Trade-off
def generate_fig1():
    fig, ax = plt.subplots(figsize=(8, 6))

    # Data: (Processing Time, Quality Score, Model Size)
    models = {
        'olmOCR-7B': (36, 95, 7000),
        '4B': (81, 60, 4000),
        '8B': (150, 75, 8000),
        '30B-MoE': (300, 85, 30000)
    }

    colors = ['#ff7f7f', '#7fbfff', '#ffbf7f', '#7fff7f']

    for (name, (time, quality, size)), color in zip(models.items(), colors):
        # Bubble size proportional to model size
        bubble_size = (size / 100) * 2
        ax.scatter(time, quality, s=bubble_size, c=color, alpha=0.6,
                  edgecolors='black', linewidth=1.5)

    ax.set_xlabel('Processing Time (minutes)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Extraction Quality Score (%)', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 320)
    ax.set_ylim(55, 100)

    plt.tight_layout()
    plt.savefig('fig1_model_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig1_model_performance.png")

# Figure 2: Page Distribution
def generate_fig2():
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Data Tables', 'Graphs', 'Metadata', 'Blank/Irrelevant']
    counts = [691, 319, 264, 79]
    colors = ['#5cb85c', '#5bc0de', '#f0ad4e', '#d9d9d9']

    y_pos = np.arange(len(categories))

    ax.barh(y_pos, counts, color=colors, edgecolor='black', linewidth=1.2)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=11)
    ax.set_xlabel('Number of Pages', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.set_xlim(0, 750)

    plt.tight_layout()
    plt.savefig('fig2_page_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig2_page_distribution.png")

# Figure 3: Prompt Comparison
def generate_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Processing Time
    categories = ['Baseline', 'QC-Enhanced']
    times = [36, 280]
    colors_time = ['#5bc0de', '#ff7f7f']

    ax1.bar(categories, times, color=colors_time, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Processing Time (minutes)', fontsize=11, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim(0, 300)

    # Classification Error Rate
    error_rates = [43, 0]
    colors_error = ['#ff7f7f', '#5cb85c']

    ax2.bar(categories, error_rates, color=colors_error, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Classification Error Rate (%)', fontsize=11, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    ax2.set_ylim(0, 50)

    plt.tight_layout()
    plt.savefig('fig3_prompt_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig3_prompt_comparison.png")

# Figure 4: Consolidation Funnel
def generate_fig4():
    fig, ax = plt.subplots(figsize=(10, 6))

    stages = ['Raw Column\nVariants', 'After Text\nNormalization',
              'Semantic\nGrouping', 'Final ML\nSchema']
    counts = [2856, 875, 318, 147]
    colors = ['#ff9999', '#ffcc99', '#99ccff', '#99ff99']

    y_pos = np.arange(len(stages))

    ax.barh(y_pos, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=11)
    ax.set_xlabel('Number of Column Patterns', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.set_xlim(0, 3000)

    plt.tight_layout()
    plt.savefig('fig4_consolidation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig4_consolidation.png")

# Figure 5: Scalability
def generate_fig5():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Data from the original figure
    doc_sizes = [17, 23, 28, 35, 42, 46, 55, 63, 189, 421]
    proc_times = [6.7, 12, 18, 25, 35, 40, 50, 36, 295, 874]

    # Linear regression
    coeffs = np.polyfit(doc_sizes, proc_times, 1)
    poly = np.poly1d(coeffs)
    x_line = np.linspace(0, 450, 100)
    y_line = poly(x_line)

    # Plot
    ax.scatter(doc_sizes, proc_times, s=150, c='#5bc0de', alpha=0.6,
              edgecolors='black', linewidth=1.5)
    ax.plot(x_line, y_line, 'r--', linewidth=2, alpha=0.7)

    ax.set_xlabel('Document Size (pages)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Processing Time (minutes)', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 450)
    ax.set_ylim(-50, 950)

    plt.tight_layout()
    plt.savefig('fig5_scalability.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig5_scalability.png")

# Figure 6: Workflow
def generate_fig6():
    fig, ax = plt.subplots(figsize=(14, 4))

    # Turn off axis
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4)
    ax.axis('off')

    # Define box positions and labels
    boxes = [
        (1, 2, 'PDF to\nImages'),
        (3.2, 2, 'Page\nClassification'),
        (5.4, 2, 'Table\nDetection'),
        (7.6, 2, 'Data\nExtraction'),
        (9.8, 2, 'Validation &\nStandardization')
    ]

    box_width = 1.8
    box_height = 1.5

    # Draw boxes
    for x, y, label in boxes:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.1",
                             edgecolor='black',
                             facecolor='#c8e6f5',
                             linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
               fontsize=10, fontweight='bold')

    # Draw arrows between boxes
    arrow_y = 2
    for i in range(len(boxes) - 1):
        x1 = boxes[i][0] + box_width/2
        x2 = boxes[i+1][0] - box_width/2
        arrow = FancyArrowPatch((x1, arrow_y), (x2, arrow_y),
                               arrowstyle='->',
                               mutation_scale=25,
                               linewidth=2.5,
                               color='black')
        ax.add_patch(arrow)

    plt.tight_layout()
    plt.savefig('fig6_workflow.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig6_workflow.png")

# Main execution
if __name__ == "__main__":
    print("Generating clean figures for IEEE conference paper...")
    print("=" * 60)

    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()

    print("=" * 60)
    print("All figures generated successfully!")
    print("\nFigures are clean with:")
    print("  ✓ No embedded titles")
    print("  ✓ No text labels/values in plots")
    print("  ✓ Only essential axis labels")
    print("  ✓ Professional IEEE conference format")
