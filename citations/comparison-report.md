# Comparison Report: NWB Data Reuse (Notion) vs Automated Citation Discovery

## 1. Summary

| Metric | Count |
|--------|------:|
| Notion entries (total) | 69 |
| Notion entries with DOI | 66 |
| Notion entries without standard DOI | 3 |
| Automated citations (unique DOIs) | 37 |
| Automated citation rows (total) | 75 |
| Overlap (DOIs in both) | 7 |
| In Notion only (DOI-based) | 59 |
| In Notion only (non-DOI) | 3 |
| In Automated only | 30 |

## 2. What Our Automated Discovery Missed (papers in Notion but not in our citations)

**Total missed: 62** (3 non-DOI, 9 Allen-only, 50 with standard DOI)

### 2a. Non-DOI URLs (cannot be found via DOI matching)

**Count: 3**

| Brief Citation | URL | Year | Datasets |
|----------------|-----|------|----------|
| Azabou et al. Multi-session, multi-task neural decoding from distinct ... | https://openreview.net/forum?id=IuU0wcO0mo | 2025 | Allen Brain Observatory Visual Coding (Optical Phy... |
| Kapoor et al. Latent Diffusion for Neural Spiking Data. NeurIPS 2024. | https://proceedings.neurips.cc/paper_files/paper/2024/file/d60b6b7f0ba6bf07d975b3bbdacea702-Paper-Conference.pdf | 2024 | DANDI:000128 |
| Chen et al. Neural Embeddings Rank: Aligning 3D latent dynamics with m... | https://proceedings.neurips.cc/paper_files/paper/2024/file/ffe78e2b3c80439e6dfd3f7f38cfa888-Paper-Conference.pdf | 2024 | DANDI:000128 |

### 2b. Allen Brain Observatory references (no separate DANDI IDs)

**Count: 9**

| Brief Citation | DOI | Year | Datasets |
|----------------|-----|------|----------|
| Guarino et al. Convergent information flows explain recurring firing p... | https://doi.org/10.1038/s41593-025-02128-5 | 2025 | Allen Brain Observatory Visual Coding (Optical Physiology) |
| Olarinre et al. Relative timing and coupling of neural population burs... | https://doi.org/10.1101/2025.02.18.638950 | 2025 | Allen Brain Observatory Visual Coding Neuropixels |
| Gonzalez-Ferrer et al. HIPPIE: A Multimodal Deep Learning Model for El... | https://doi.org/10.1101/2025.03.14.642461 | 2025 | Allen Brain Observatory Visual Coding Neuropixels |
| Tolossa et al. A conserved code for anatomy: Neurons throughout the br... | https://doi.org/10.1101/2024.07.11.603152 | 2024 | Allen Brain Observatory Visual Coding Neuropixels |
| Mendoza-Halliday et al. A ubiquitous spectrolaminar motif of local fie... | http://dx.doi.org/10.1038/s41593-023-01554-7 | 2024 | Allen Brain Observatory Visual Coding Neuropixels |
| Tang et al. Stimulus type shapes the topology of cellular functional n... | https://doi.org/10.1038/s41467-024-49704-0 | 2024 | Allen Brain Observatory Visual Coding Neuropixels |
| Lowet et al. Theta and gamma rhythmic coding through two spike output ... | http://dx.doi.org/10.1016/j.celrep.2023.112906 | 2023 | Allen Brain Observatory Visual Coding Neuropixels |
| Purandare and Mehta. Mega-scale movie-fields in the mouse visuo-hippoc... | http://dx.doi.org/10.7554/eLife.85069 | 2023 | Allen Brain Observatory Visual Coding Neuropixels |
| Petersen et al. CellExplorer: A framework for visualizing and characte... | http://dx.doi.org/10.1016/j.neuron.2021.09.002 | 2021 | Allen Brain Observatory Visual Coding Neuropixels |

### 2c. Genuine misses (has DOI, references DANDI datasets)

**Count: 50**

| Brief Citation | DOI | Year | DANDI Datasets | Also Allen? |
|----------------|-----|------|----------------|-------------|
| Livezey et al. The geometry of correlated variability leads to hi... | https://doi.org/10.1152/jn.00313.2024 | 2025 | https://doi.org/10.6080/K0VT1Q93 |  |
| Zeisler et al. Consistent hierarchies of single-neuron timescales... | https://doi.org/10.1523/JNEUROSCI.2155-24.2025 | 2025 | DANDI:000004 |  |
| Masset et al. Multi-timescale reinforcement learning in the brain... | https://doi.org/10.1038/s41586-025-08929-9 | 2025 | DANDI:000251 |  |
| Adhinarta et al. WormID-Bench: A Benchmark for Whole-Brain Activi... | https://doi.org/10.1101/2025.01.06.631621 | 2025 | DANDI:000541, DANDI:000714, DANDI:000692, DANDI:00... |  |
| Russo et al. Thalamic feedback shapes brain responses evoked by c... | https://doi.org/10.1038/s41467-025-58717-2 | 2025 | DANDI:000458 |  |
| Rupprecht et al. Spike inference from calcium imaging data acquir... | https://doi.org/10.1101/2025.03.03.641129 | 2025 | DANDI:000168 |  |
| Roos et al. Modeling Organoid Population Electrophysiology Dynami... | https://doi.org/10.1101/2025.03.02.641081 | 2025 | DANDI:000041 |  |
| Windolf et al. DREDge: robust motion correction for high-density ... | https://doi.org/10.1038/s41592-025-02614-5 | 2025 | DANDI:000397, DANDI:000957 |  |
| Ryoo et al. Generalizable, real-time neural decoding with hybrid ... | https://doi.org/10.48550/arXiv.2506.05320 | 2025 | DANDI:000688, DANDI:000128 |  |
| Sabatini & Kaufman. Reach-dependent reorientation of rotational d... | https://doi.org/10.1038/s41467-024-51308-7 | 2024 | DANDI:000070 |  |
| Pham et al. Deep-prior ODEs augment fluorescence imaging with che... | https://doi.org/10.1038/s41467-024-53232-2 | 2024 | DANDI:000168 |  |
| Zheng et al. Perpetual step-like restructuring of hippocampal cir... | https://doi.org/10.1016/j.celrep.2024.114702 | 2024 | DANDI:000552 |  |
| Hu & Quon. scPair: Boosting single cell multimodal analysis by le... | https://doi.org/10.1038/s41467-024-53971-2 | 2024 | DANDI:000020 |  |
| Asiminas et al. Protocol to study oxygen dynamics in the in vivo ... | https://doi.org/10.1016/j.xpro.2024.103334 | 2024 | DANDI:000891 |  |
| Harris et al. Tracking the Distance to Criticality in Systems wit... | https://doi.org/10.1103/PhysRevX.14.031021 | 2024 | DANDI:000713 |  |
| Cambrainha et al. Criticality at work: scaling in the mouse corte... | https://doi.org/10.48550/arXiv.2410.23508 | 2024 | DANDI:000713 |  |
| Salimi et al. Gamma frequency connectivity in frontostriatal netw... | https://doi.org/10.1162/netn_a_00416 | 2024 | DANDI:001039 |  |
| Vetter et al. Generating realistic neurophysiological time series... | https://doi.org/10.1016/j.patter.2024.101047 | 2024 | DANDI:000055 |  |
| Stringer et al. Rastermap: a discovery method for neural populati... | https://doi.org/10.1038/s41593-024-01783-4 | 2024 | DANDI:000130 |  |
| Hart et al. Pheromone representation in the ant antennal lobe cha... | http://dx.doi.org/10.1016/j.cub.2024.05.031 | 2024 | DANDI:000467 |  |
| Bahl et al. Using deep learning to quantify neuronal activation f... | http://dx.doi.org/10.1038/s41467-023-44503-5 | 2024 | DANDI:000020 |  |
| Furumichi et al. A deep generative model integrating single-cell ... | http://dx.doi.org/10.1101/2024.03.29.587341 | 2024 | DANDI:000008 |  |
| Mehrotra et al. Hyperpolarization-activated currents drive neuron... | http://dx.doi.org/10.1016/j.cub.2024.05.048 | 2024 | DANDI:000939 |  |
| Pachitariu et al. Spike sorting with Kilosort4. Nature Methods. | http://dx.doi.org/10.1038/s41592-024-02232-7 | 2024 | DANDI:000028, DANDI:000231, DANDI:000410 |  |
| Ma et al. ElecFeX is a user-friendly toolbox for efficient featur... | http://dx.doi.org/10.1016/j.crmeth.2024.100791 | 2024 | DANDI:000020 |  |
| Lee et al. Spyglass: a framework for reproducible and shareable n... | http://dx.doi.org/10.1101/2024.01.25.577295 | 2024 | DANDI:000059 |  |
| Lee et al. PhysMAP - interpretable in vivo neuronal cell type ide... | http://dx.doi.org/10.1101/2024.02.28.582461 | 2024 | https://doi.org/10.25378/janelia.8869115 |  |
| Magland et al. Neurosift: DANDI exploration and NWB visualization... | http://dx.doi.org/10.21105/joss.06590 | 2024 | DANDI:000409 |  |
| Zhong et al. Hierarchical Working Memory and a New Magic Number. ... | https://doi.org/10.1101/2024.08.14.607952 | 2024 | DANDI:000207 |  |
| Kendrick et al. Transcriptomically-measured gene expression predi... | https://doi.org/10.1101/2024.08.26.609746 | 2024 | DANDI:000020, DANDI:000023 |  |
| Azabou et al. A unified, scalable framework for neural population... | http://dx.doi.org/10.48550/arXiv.2310.16046 | 2023 | DANDI:000688, DANDI:000070, DANDI:000128, DANDI:00... |  |
| Wei et al. Associations between in vitro, in vivo and in silico c... | http://dx.doi.org/10.1038/s41467-023-37844-8 | 2023 | DANDI:000021 |  |
| Viejo et al. Pynapple, a toolbox for data analysis in neuroscienc... | http://dx.doi.org/10.7554/eLife.85786 | 2023 | DANDI:000021, DANDI:000207 |  |
| Perkins et al. Simple decoding of behavior from a complicated neu... | http://dx.doi.org/10.7554/eLife.89421.1 | 2023 | DANDI:000127, DANDI:000130, DANDI:000128, DANDI:00... |  |
| Patel et al. High-performance neural population dynamics modeling... | http://dx.doi.org/10.21105/joss.05023 | 2023 | DANDI:000128 |  |
| Cai et al. FIOLA: an accelerated pipeline for fluorescence imagin... | http://dx.doi.org/10.1038/s41592-023-01964-2 | 2023 | DANDI:000054 |  |
| Bernaerts et al. Combined statistical-mechanistic modeling links ... | http://dx.doi.org/10.1101/2023.03.02.530774 | 2023 | DANDI:000008 |  |
| Easthope et al. Cortical control of posture in fine motor skills:... | http://dx.doi.org/10.3389/fnhum.2023.1139569 | 2023 | https://doi.org/10.6084/m9.figshare.c.4617263.v4 |  |
| Schneider et al. Learnable latent embeddings for joint behavioura... | http://dx.doi.org/10.1038/s41586-023-06031-6 | 2023 | DANDI:000127 | Yes |
| Nguyen et al. Fast Temporal Wavelet Graph Neural Networks. Tempor... | https://doi.org/10.48550/arXiv.2302.08643 | 2023 | DANDI:000055 |  |
| Arbabi et al. Investigating microglia-neuron crosstalk by charact... | http://dx.doi.org/10.1016/j.isci.2023.107329 | 2023 | DANDI:000209, DANDI:000020 |  |
| Burman et al. Active cortical networks promote shunting fast syna... | http://dx.doi.org/10.1016/j.neuron.2023.08.005 | 2023 | DANDI:000458 |  |
| Rimehaug et al. Uncovering circuit mechanisms of current sinks an... | http://dx.doi.org/10.7554/eLife.87169 | 2023 | DANDI:000021 | Yes |
| Eom et al. Statistically unbiased prediction enables accurate den... | http://dx.doi.org/10.1038/s41592-023-02005-8 | 2023 | DANDI:000168 |  |
| Johansen et al. Projecting RNA measurements onto single cell atla... | http://dx.doi.org/10.1038/s41467-023-40744-6 | 2023 | DANDI:000020, DANDI:000023 |  |
| Keshtkaran et al. A large-scale neural network training framework... | http://dx.doi.org/10.1038/s41592-022-01675-0 | 2022 | DANDI:000070 |  |
| Talukder et al. Deep Neural Imputation: A Framework for Recoverin... | https://doi.org/10.48550/arXiv.2206.08094 | 2022 | DANDI:000055 |  |
| Durand et al. Acute head-fixed recordings in awake mice with mult... | http://dx.doi.org/10.1038/s41596-022-00768-6 | 2022 | DANDI:000021 |  |
| Gala et al. Consistent cross-modal identification of cortical neu... | http://dx.doi.org/10.1038/s43588-021-00030-1 | 2021 | DANDI:000020 |  |
| Ye and Pandarinath. Representation learning for neural population... | http://dx.doi.org/10.51628/001c.27358 | 2021 | DANDI:000070 |  |

## 3. What Notion Missed (citations we found that Notion doesn't have)

**Total unique DOIs in automated but not in Notion: 30**

| Citation DOI | DANDI Dataset(s) | Citation Title | Year |
|-------------|------------------|----------------|------|
| 10.1038/s41467-023-41755-z | DANDI:000301 | Neural mechanisms for the localization of unexpected externa... | 2023 |
| 10.1038/s41586-025-08790-w | DANDI:000402 | Functional connectomics spanning multiple areas of mouse vis... | 2025 |
| 10.1038/s41592-025-02849-2 | DANDI:001460 | Spatiotemporal focusing enables all-optical in situ histolog... | 2025 |
| 10.1038/s41597-022-01280-y | DANDI:000055 | AJILE12: Long-term naturalistic human intracranial neural re... | 2022 |
| 10.1038/s41597-022-01728-1 | DANDI:000231 | A detailed behavioral, videographic, and neural dataset on o... | 2022 |
| 10.1038/s41597-023-02214-y | DANDI:000037 | Responses of pyramidal cell somata and apical dendrites in m... | 2023 |
| 10.1038/s41597-024-02943-8 | DANDI:000469 | Dataset of human-single neuron activity during a Sternberg w... | 2024 |
| 10.1038/s41597-024-03029-1 | DANDI:000623 | Multimodal single-neuron, intracranial EEG, and fMRI brain r... | 2024 |
| 10.1038/s41597-025-06115-0 | DANDI:000713 | Mouse Hippocampal Sharp-Wave Ripple Dataset Curated From Pub... | 2025 |
| 10.1038/s41597-025-06285-x | DANDI:000563, DANDI:000617, DANDI:000690, DANDI:001174, DANDI:001195, DANDI:001349, DANDI:001354, DANDI:001359, DANDI:001361, DANDI:001366, DANDI:001375, DANDI:001433 | Facilitating analysis of open neurophysiology data on the DA... | 2025 |
| 10.1088/1741-2552/ae0966 | DANDI:000458 | Statistical characterization of cortical–thalamic dynamics e... | 2025 |
| 10.1093/gigascience/giac108 | DANDI:000292, DANDI:000293 | An <i>in vitro</i> whole-cell electrophysiology dataset of h... | 2022 |
| 10.1101/2023.06.02.543483 | DANDI:000488 | Differential encoding of temporal context and expectation un... | 2023 |
| 10.1101/2024.04.28.591397 | DANDI:000472, DANDI:000541, DANDI:000565, DANDI:000692, DANDI:000714, DANDI:000715, DANDI:000776 | Unifying community-wide whole-brain imaging datasets enables... | 2024 |
| 10.1101/2025.07.17.663965 | DANDI:000563, DANDI:000617, DANDI:000690, DANDI:001174, DANDI:001195, DANDI:001349, DANDI:001354, DANDI:001359, DANDI:001361, DANDI:001366, DANDI:001375, DANDI:001433 | Facilitating analysis of open neurophysiology data on the DA... | 2025 |
| 10.1101/2025.10.17.682993 | DANDI:000167 | Improved inference of latent neural states from calcium imag... | 2025 |
| 10.12751/g-node.sdxr1v | DANDI:000713 |  |  |
| 10.1523/jneurosci.0381-24.2024 | DANDI:000167 | A Perspective on Neuroscience Data Standardization with Neur... | 2024 |
| 10.5281/zenodo.13930779 | DANDI:000888 |  |  |
| 10.5281/zenodo.13935289 | DANDI:000889 |  |  |
| 10.5281/zenodo.13935291 | DANDI:000889 |  |  |
| 10.5281/zenodo.8408660 | DANDI:000678 |  |  |
| 10.64898/2026.01.06.697952 | DANDI:001688 | High performance sorting of motor unit action potentials wit... | 2026 |
| 10.64898/2026.01.08.698522 | DANDI:000020 | A robust low-dimensional manifold organizes neuronal respons... | 2026 |
| 10.7554/elife.105955 | DANDI:001195 | Separable dorsal raphe dopamine projections mimic the facets... | 2025 |
| 10.7554/elife.105955.3 | DANDI:001195 | Separable dorsal raphe dopamine projections mimic the facets... | 2025 |
| 10.7554/elife.83289 | DANDI:000235, DANDI:000236, DANDI:000237, DANDI:000238 | Model discovery to link neural activity to behavioral tasks | 2023 |
| 10.7554/elife.85786.3 | DANDI:000207 | Pynapple, a toolbox for data analysis in neuroscience | 2023 |
| 10.7554/elife.89421.3 | DANDI:000127, DANDI:000128, DANDI:000129, DANDI:000130, DANDI:000138, DANDI:000139, DANDI:000140 | An emerging view of neural geometry in motor cortex supports... | 2025 |
| 10.7554/elife.98666 | DANDI:001552 | Mesolimbic dopamine ramps reflect environmental timescales | 2025 |

Of these 30 unique DOIs:

- **11** cite dandisets also referenced in Notion (Notion missed these papers)
- **19** cite dandisets NOT referenced in Notion at all (different datasets)

## 4. Counts by Processing Source

### 4a. Automated citations by citation_source

| Source | Count |
|--------|------:|
| crossref | 71 |
| opencitations | 4 |

### 4b. Notion entries by type

| Type | Count |
|------|------:|
| Journal Article | 44 |
| Preprint | 16 |
| Conference Paper | 6 |
| Protocol | 3 |

### 4c. Notion entries by year

| Year | Count |
|------|------:|
| 2025 | 18 |
| 2024 | 27 |
| 2023 | 18 |
| 2022 | 3 |
| 2021 | 3 |

## 5. Analysis of Overlap

**Papers found in both sources: 7**

| DOI | Notion Citation | Year | Notion Datasets | Auto DANDI IDs | Auto Source |
|-----|----------------|------|-----------------|----------------|-------------|
| 10.1038/s41593-025-02114-x | Wang et al. Brain-wide analysis reveals movement encodi... | 2025 | DANDI:000363 | 000363 | crossref |
| 10.1038/s41596-024-01120-w | Lees et al. Standardized measurements for monitoring an... | 2025 | DANDI:000402 | 000402 | crossref |
| 10.1088/1741-2552/ad1787 | Taeckens and Shah. A spiking neural network with contin... | 2024 | DANDI:000140 | 000140 | opencitations |
| 10.1101/2025.01.26.634933 | Clark et al. Symmetries and Continuous Attractors in Di... | 2025 | DANDI:000939 | 000939 | crossref |
| 10.1101/2025.04.04.647222 | Nigrisoli et al. Statistical Characterization of Cortic... | 2025 | DANDI:000458 | 000458 | crossref |
| 10.1126/science.adf0805 | Chartrand et al. Morphoelectric and transcriptomic dive... | 2023 | DANDI:000020 | 000630 | crossref |
| 10.21105/jose.00309 | Juavinett and Magdaleno-Garcia. nwb4edu: an Online Text... | 2025 | DANDI:000053,DANDI:000006 | 000053 | crossref |
