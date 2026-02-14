# Figure Regeneration Requirements

The following figures need to be regenerated to remove embedded titles and text descriptions. All text should only appear in LaTeX captions, not in the images themselves.

## Figure 1: fig1_model_performance.png
**Current issues:**
- Title "VLM Performance Trade-off" embedded in image
- Model names as text labels (olmOCR-7B, 4B, 8B, 30B-MoE)

**Required changes:**
- Remove title completely
- Keep bubble visualization but remove text labels
- Keep axes labels (Processing Time, Extraction Quality Score)

## Figure 2: fig2_page_distribution.png
**Current issues:**
- Title "Page Type Distribution Across 15 Reports (N=1,374)" embedded in image
- Count and percentage text inside bars (e.g., "691 (51.1%)")

**Required changes:**
- Remove title completely
- Remove text labels from inside bars
- Keep y-axis category labels (Data Tables, Graphs, Metadata, Blank/Irrelevant)
- Keep x-axis label (Number of Pages)

## Figure 3: fig3_prompt_comparison.png
**Current issues:**
- Subfigure labels "(a) Processing Time" and "(b) Classification Accuracy"
- Text labels "280m", "36m", "43%", "0%" on bars

**Required changes:**
- Remove subfigure titles
- Remove value labels from bars
- Keep axes labels and bar categories (Baseline, QC-Enhanced)

## Figure 4: fig4_consolidation.png
**Current issues:**
- Title "Data Consolidation Pipeline" embedded in image
- Text labels showing values (2856, 875, 318, 147) on bars
- Y-axis labels with descriptive text

**Required changes:**
- Remove title completely
- Remove numeric labels from bars
- Simplify y-axis labels or remove if caption explains stages
- Keep x-axis label (Number of Column Patterns)

## Figure 5: fig5_scalability.png
**Current issues:**
- Title "Processing Time vs Document Size" embedded in image
- Legend text "Linear fit: y=1.95x+-72.02" in figure

**Required changes:**
- Remove title completely
- Remove legend text from inside figure
- Keep axes labels (Document Size (pages), Processing Time (minutes))
- Keep scatter points and regression line

## Figure 6: fig6_workflow.png
**Current issues:**
- Title "Three-Stage Extraction Workflow" embedded in image
- Descriptive text inside boxes (PDF to Images (200 DPI), Page Classification, etc.)

**Required changes:**
- Remove title completely
- Remove or minimize text in workflow boxes
- Consider using simple boxes/arrows only
- OR keep minimal single-word labels (PDF, Classify, Detect, Extract, Validate)

## How to Regenerate

The figures should be regenerated using the original plotting code/data with the following general principles:

1. **No titles** - All titles go in LaTeX \caption{} only
2. **Minimal text** - Remove descriptive text, percentages, values from within figures
3. **Keep axis labels** - Essential for understanding the data
4. **Clean design** - Professional appearance suitable for IEEE conference format
5. **Consistent style** - Use similar fonts, colors across all figures
