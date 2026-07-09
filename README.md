# In Silico Analysis of Potato and Groundnut Rhizosphere Microbiomes
**Author:** T Sai Deva Harshini Talluri

##  How to Run the Dashboard Locally
1. Clone this repository: `git clone https://github.com/saidevaharshinitalluri-genomics/Rhizosphere-Microbiome-Pipeline.git`
2. Navigate to the folder: `cd Rhizosphere-Microbiome-Pipeline`
3. Install requirements: `pip install streamlit pandas`
4. Run the app: `streamlit run app.py`

---

## 1. Abstract
The rhizosphere microbiome plays a foundational role in plant health, nutrient acquisition, and crop yield. This study executed an end-to-end 16S rRNA bioinformatics and machine learning pipeline to characterize and differentiate the soil microbiomes of Potato and Groundnut crops. Amplicon Sequence Variants (ASVs) were analyzed using a multi-omics approach encompassing Compositional Data Analysis (CoDA), differential abundance testing, and network analysis. A Random Forest machine learning classifier was trained to predict crop types based strictly on microbial signatures, achieving 100% accuracy. Explainable AI (SHAP) and literature-based functional synthesis were utilized to identify and characterize the core biomarkers driving these distinct microenvironments.

## 2. Objectives
* **Taxonomic Profiling:** To map and compare the community composition of Potato and Groundnut rhizospheres.
* **Ecological Diversity:** To evaluate within-sample richness (Alpha Diversity) and between-sample dissimilarity (Beta Diversity) with rigorous statistical validation.
* **Biomarker Discovery:** To identify statistically significant, differentially abundant bacteria driving the differences between the two crop soils.
* **Predictive Modeling:** To train a machine learning algorithm capable of predicting the host crop exclusively from its microbial footprint.
* **Systems Level Interactions:** To visualize microbial synergy and competition through co-occurrence networks.
* **Functional Assessment:** To deduce the ecological roles of the top diagnostic biomarkers using a targeted scientific literature synthesis.

## 3. Methodology

### 3.1 Data Acquisition & Quality Control
* **Data Source:** 16S rRNA gene sequencing data was processed into Amplicon Sequence Variants (ASVs). 
* **Quality Control:** Sequencing depth was visualized per sample to ensure robust read counts, confirming that neither crop type was under-sequenced and that the data was statistically viable for downstream analysis.
* **Taxonomic Alignment:** ASVs were globally aligned against the **SILVA v138.1** reference database using the VSEARCH algorithm, enforcing a strict 97% sequence identity threshold.

### 3.2 Statistical & Diversity Analysis
* **Alpha Diversity:** Within-sample richness and evenness were calculated using the Shannon Diversity Index. Significance was tested using a non-parametric Mann-Whitney U test.
* **Beta Diversity:** Spatial clustering of the microbiomes was visualized via Principal Coordinates Analysis (PCoA) computed on a Bray-Curtis dissimilarity matrix.
* **PERMANOVA:** Permutational Multivariate Analysis of Variance (999 permutations) was executed to mathematically validate the significance of the Beta Diversity clustering.
* **Differential Abundance:** Centered Log-Ratio (CLR) transformations were applied to the data. Welch's T-test was utilized, followed by Benjamini-Hochberg False Discovery Rate (FDR) correction to eliminate false positives.

### 3.3 Machine Learning & Explainable AI
* **Model Training:** A Random Forest Classifier was trained (80/20 train-test split) to predict the crop environment based on ASV abundance.
* **Performance Metrics:** The model was evaluated using Accuracy, Precision, Recall, F1-Score, and a Receiver Operating Characteristic (ROC) curve.
* **Feature Importance:** SHapley Additive exPlanations (SHAP) values were calculated using a TreeExplainer to decode the algorithm and rank the exact ASVs driving the predictions.

### 3.4 Network & Functional Analysis
* **Co-occurrence Networks:** A biological network was constructed using Spearman’s rank correlation on the top 50 most abundant taxa. A threshold of |r| > 0.40 was applied to isolate significant synergistic (positive) and competitive (negative) interactions.
* **Functional Synthesis:** Due to the Phylum/Order-level resolution limits of the 16S data, automated predictive databases (FAPROTAX/PICRUSt2) were bypassed. Functional potential was instead inferred by cross-referencing the top SHAP-identified biomarkers with established agricultural microbiology literature.

## 4. Results & Discussion

### 4.1 Community Composition & Diversity
The taxonomic mapping successfully identified the core microbial constituents of both crop soils. 
* **Beta Diversity:** The Bray-Curtis PCoA plot revealed a distinct, visual separation between the Potato and Groundnut samples. The PERMANOVA results confirmed this structural divergence is highly statistically significant, proving that crop type fundamentally dictates the surrounding microbiome.
* **Alpha Diversity:** Shannon Index boxplots illustrated the variance in community evenness and richness, highlighting specific ecological pressures exerted by different root exudates.

### 4.2 Biomarker Discovery
The Benjamini-Hochberg FDR-corrected differential abundance analysis successfully isolated the specific bacteria responsible for the soil differences. 
* The **Volcano Plot** visualized these effect sizes, clearly defining taxa that were significantly upregulated in either Potato or Groundnut soils. 
* The **Core Microbiome Heatmap** provided a hierarchical clustering of the top 20 most abundant Genera, showing clear abundance block-patterns unique to each crop.

### 4.3 Machine Learning Performance
The Random Forest Classifier achieved a flawless **100% classification accuracy**. 
* The ROC curve demonstrated a perfect Area Under the Curve (AUC), proving the predictive power of the soil microbiome. 
* The model relied heavily on specific taxonomic features, which were extracted and visualized using the **SHAP Summary Plot**. This Explainable AI integration transitioned the project from a "black-box" prediction into an interpretable biological discovery tool.

### 4.4 Systems Biology & Co-occurrence
The microbial network analysis (Spearman |r| > 0.40) mapped the social dynamics of the soil. The resulting visualization highlighted critical "hub" taxa. Green edges denoted mutualistic synergies (shared environmental preferences), while red edges highlighted competitive exclusion, mapping the complex survival dynamics occurring in the rhizosphere.

### 4.5 Rhizosphere Functional Analysis (Literature Synthesis)
Cultivation-independent studies show that the dominant diagnostic taxa identified by the SHAP analysis play critical roles in soil biogeochemistry and agricultural health. 

| Taxon Identified | Major Ecological & Soil Functions | Agricultural Significance |
| :--- | :--- | :--- |
| **Planctomycetota** | Degradation of complex organic biopolymers (chitin, cellulose). | Crucial for nutrient turnover; breaks down crop residue. |
| **Phycisphaerae** | Heterotrophic breakdown of plant-derived polysaccharides. | Responds dynamically to active root exudates. |
| **Tepidisphaerales** | Specialized carbohydrate utilization and plant cell wall breakdown. | Supports structural soil health around tuber/pod development. |
| **WD2101 soil group** | Highly linked to carbon cycling and organic nitrogen facilitation. | Serves as a core indicator of healthy, active microbiomes. |

These taxa specialize in the breakdown of complex biopolymers, signifying a robust carbon-cycling capacity that is critical for supporting below-ground tuber and pod development.

## 5. Conclusion
This study successfully demonstrates that Potato and Groundnut crops engineer highly distinct, statistically significant microbiome profiles in their surrounding soil. By integrating multi-omics statistics with a 100% accurate Random Forest classifier and SHAP explainability, this pipeline isolated the precise microbial biomarkers driving these differences. Furthermore, network and literature-based functional analyses revealed that these microbiomes are highly structured, competitive ecosystems optimized for carbon cycling and organic biopolymer degradation. This end-to-end framework provides a robust foundation for future predictive agricultural models and bio-fertilizer development.
