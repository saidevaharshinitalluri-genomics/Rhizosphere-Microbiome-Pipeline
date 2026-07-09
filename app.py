import streamlit as st
import pandas as pd
import os

# Configure the page settings for a wide layout
st.set_page_config(page_title="Rhizosphere Microbiome Analysis", layout="wide")
st.title("In Silico Taxonomic Profiling : Rhizosphere Microbiome Analysis Of Potato And Groundnut")

# Define 11 explicit tabs to separate the analytical workflow completely
tabs = st.tabs([
    "1. Overview", 
    "2. Alignment & Taxonomy", 
    "3. Community Composition", 
    "4. Alpha Diversity", 
    "5. Beta Diversity", 
    "6. PERMANOVA Statistics", 
    "7. Differential Abundance (FDR)", 
    "8. Biomarker Visuals", 
    "9. Microbial Networks", 
    "10. ML Benchmarking", 
    "11. Explainable AI (SHAP)"
])

# Tab 1: Overview & Quality Control
with tabs[0]:
    st.header("Project Overview")
    st.write("This application presents an end-to-end 16S rRNA analysis pipeline.")
    st.write("Methodologies applied include VSEARCH alignment against the SILVA database, Compositional Data Analysis (CoDA) statistics, Benjamini-Hochberg FDR correction, predictive machine learning algorithms, and functional pathway prediction via literature synthesis.")
    
    st.divider()
    
    st.subheader("Quality Control: Sequencing Depth")
    st.write("Before proceeding with diversity metrics, sequencing depth was verified to ensure robust Amplicon Sequence Variant (ASV) read counts across all Potato and Groundnut soil samples, confirming the data is statistically viable.")
    if os.path.exists("read_depth_check.png"): 
        st.image("read_depth_check.png", use_container_width=True)

# Tab 2: Alignment & Taxonomy
with tabs[1]:
    st.header("Sequence Alignment & Taxonomy Mapping")
    st.write("Amplicon Sequence Variants (ASVs) were aligned globally against the SILVA v138.1 database using the VSEARCH algorithm. A strict 97% sequence identity threshold was enforced to determine taxonomic assignments.")
    if os.path.exists("taxonomy_final.csv"):
        st.write("Preview of finalized taxonomy matrix:")
        st.dataframe(pd.read_csv("taxonomy_final.csv").head(15), use_container_width=True)

# Tab 3: Community Composition
with tabs[2]:
    st.header("Phylum-Level Community Composition")
    st.write("The bar chart below illustrates the relative abundance of microbial phyla distributed across all experimental soil samples.")
    if os.path.exists("phylum_stacked_bar.png"): 
        st.image("phylum_stacked_bar.png", use_container_width=True)
    if os.path.exists("phylum_composition.csv"): 
        st.write("Underlying Compositional Data:")
        st.dataframe(pd.read_csv("phylum_composition.csv").head(10), use_container_width=True)

# Tab 4: Alpha Diversity
with tabs[3]:
    st.header("Alpha Diversity (Within-Sample Richness)")
    st.write("Shannon Diversity Index was computed to assess both the richness and evenness of the microbial communities within individual samples. Statistical significance between crop types was evaluated using a non-parametric Mann-Whitney U test.")
    if os.path.exists("alpha_diversity_boxplot.png"): 
        st.image("alpha_diversity_boxplot.png")

# Tab 5: Beta Diversity
with tabs[4]:
    st.header("Beta Diversity (Between-Sample Dissimilarity)")
    st.write("Principal Coordinates Analysis (PCoA) was performed on a Bray-Curtis dissimilarity matrix to visualize spatial clustering of microbiome profiles based on the crop type.")
    if os.path.exists("pcoa_plot.png"): 
        st.image("pcoa_plot.png", caption="Bray-Curtis Principal Coordinates Analysis")

# Tab 6: PERMANOVA
with tabs[5]:
    st.header("PERMANOVA Statistical Proof")
    st.write("Permutational Multivariate Analysis of Variance (PERMANOVA) was executed with 999 permutations to mathematically validate that the Beta Diversity clustering observed is statistically significant, ruling out random variation.")
    if os.path.exists("permanova_result.csv"): 
        st.dataframe(pd.read_csv("permanova_result.csv"), use_container_width=True)

# Tab 7: Differential Abundance
with tabs[6]:
    st.header("Differential Abundance Testing (FDR Corrected)")
    st.write("To identify specific biomarker bacteria, Welch's T-test was applied to Centered Log-Ratio (CLR) transformed abundances. P-values were subsequently corrected using the Benjamini-Hochberg False Discovery Rate (FDR) methodology to eliminate false positives.")
    if os.path.exists("differential_abundance_fdr.csv"): 
        st.dataframe(pd.read_csv("differential_abundance_fdr.csv"), use_container_width=True)

# Tab 8: Biomarker Visualizations
with tabs[7]:
    st.header("Biomarker Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Volcano Plot")
        st.write("Visualizing biological effect size (Fold Change) against statistical significance (Adjusted P-Value).")
        if os.path.exists("volcano_plot.png"): 
            st.image("volcano_plot.png", use_container_width=True)
    with col2:
        st.subheader("Core Microbiome Heatmap")
        st.write("Hierarchical clustering applied strictly to the top 20 most abundant Genera.")
        if os.path.exists("core_microbiome_heatmap.png"): 
            st.image("core_microbiome_heatmap.png", use_container_width=True)

# Tab 9: Networks
with tabs[8]:
    st.header("Microbial Co-occurrence Networks")
    st.write("This network map visualizes significant synergistic and antagonistic relationships between bacterial genera. Edges are drawn exclusively for Spearman rank correlations where the absolute coefficient exceeds 0.40.")
    if os.path.exists("network_plot.png"): 
        st.image("network_plot.png", caption="Spearman correlations (|rho| > 0.40)")

# Tab 10: Machine Learning
with tabs[9]:
    st.header("Machine Learning Algorithm Benchmarks")
    st.write("Three distinct supervised learning algorithms were trained to predict crop type based exclusively on the underlying microbial signature.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Accuracy Metrics")
        if os.path.exists("ml_metrics.csv"): 
            st.dataframe(pd.read_csv("ml_metrics.csv"), hide_index=True)
    with col2:
        st.subheader("Receiver Operating Characteristic (ROC)")
        if os.path.exists("roc_curve.png"): 
            st.image("roc_curve.png", caption="Area Under the Curve (AUC) for the Random Forest Classifier")

# Tab 11: SHAP
with tabs[10]:
    st.header("Explainable AI (SHAP)")
    st.write("SHapley Additive exPlanations (SHAP) values were calculated using a TreeExplainer to decode the 'Black Box' of the Random Forest model. This plot reveals the specific Amplicon Sequence Variants (ASVs) that exerted the highest impact on the algorithm's decision-making process.")
    if os.path.exists("shap_summary.png"): 
        st.image("shap_summary.png", use_container_width=True)