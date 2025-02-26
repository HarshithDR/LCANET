# LCANet: Enhanced Lipreading System with Cascaded Attention Mechanisms

## Overview
**LCANet** is an end-to-end lipreading system designed to detect mismatches between lip movements and audio content, addressing challenges in sentence-level audio-visual synchronization. By building on the foundational **LipNet architecture**, this project integrates cascaded attention mechanisms and **CTC (Connectionist Temporal Classification)** to enhance temporal alignment and achieve high accuracy in lipreading tasks. This project has significant applications in **video forensics**, **deepfake detection**, **content authentication**, and **accessibility for the hearing impaired**.

Using the **GRID Corpus dataset**, the project demonstrates improvements in **Continuous Error Rate (CER)** and **Word Error Rate (WER)** through key modifications such as **Bi-Directional LSTM layers** for sequence learning and cascaded attention mechanisms for improved lip-audio synchronization. The enhanced LCANet system showcases measurable progress, advancing the field of lip-reading and audio-visual analysis.

---

## Key Features

1. **Enhanced LipNet Architecture**:
   - Replaced GRU layers with **Bi-Directional LSTM layers** for better understanding of long-sequence dependencies.
   - Extended the model to analyze entire spoken sentences (sentence-level recognition).

2. **Cascaded Attention Mechanisms**:
   - Adopted cascaded attention techniques from LCANet for precise temporal alignment between lip movements and audio content.
   - Allowed the model to focus on critical lip features across frames for accurate recognition.

3. **Improved Metrics**:
   - Achieved better performance in terms of **Continuous Error Rate (CER)** and **Word Error Rate (WER)**.
   - Results validated on the **GRID Corpus** dataset.

4. **Applications**:
   - **Video Forensics**: Detect tampered or manipulated video content.
   - **Accessibility for Hearing Impaired**: Enhance automated solutions to assist individuals with hearing impairments.
   - **Deepfake Detection**: Identify discrepancies between lip movements and audio to detect deepfakes.
   - **Surveillance**: Enable silent speech recognition for security and monitoring purposes.

---

## Methodology

1. **Dataset**:
   - **GRID Corpus**:
     - Consists of 450 training and 50 testing video clips, with synchronized audio-visual recordings.
     - Provides a standard benchmark for evaluating lipreading models.

2. **Preprocessing**:
   - Cropped video frames and converted them into tensors for model input.
   - Standardized data formats to maintain consistent input quality.

3. **Model Architecture**:
   - **LipNet Modifications**:
     - Replaced GRU with **Bi-Directional LSTMs** for better sequence learning and long-term dependencies.
   - **Cascaded Attention Mechanism**:
     - Focused on enhancing temporal alignment across video sequences.
   - **Loss Function**:
     - Used **CTC (Connectionist Temporal Classification)** loss to penalize temporal misalignments.

4. **Model Implementation**:
   - **Software and Tools**: 
     - **TensorFlow** for training and evaluation.
     - **OpenCV** for video processing.
     - **NumPy** for data manipulation.
     - **Matplotlib** for result visualization.
   - **Training Configuration**:
     - Batch size: 2 (due to memory constraints).
     - Dataset: 450 video clips for training, 50 for testing.
     - Epochs: 100, allowing the model to converge effectively.

---

## Results

### Performance Metrics

| **Metric**        | **LipNet** | **LCANet** | **Our Model** |
|--------------------|------------|------------|---------------|
| **CER (%)**        | 1.9        | 1.3        | 0.29          |
| **WER (%)**        | 4.8        | 2.9        | 1.38          |

- **Continuous Error Rate (CER)** and **Word Error Rate (WER)** were drastically reduced compared to the original LipNet and LCANet implementations.
- Doubling the number of epochs while maintaining a small batch size improved model performance.

### Loss Comparison

| **Model**          | **Loss**  | **Batch Size** | **Dataset Size** | **Epochs** |
|--------------------|-----------|----------------|------------------|------------|
| LipNet             | 4.27      | 64             | 25,330           | 50         |
| LCANet             | 4.16      | 64             | 25,330           | 50         |
| Our Model          | 3.90      | 2              | 450              | 100        |

> **Note**: Batch size and dataset size were reduced due to memory constraints.

---

## Applications

1. **Deepfake and Video Forensics**:
   - Detects lip-speech mismatches to identify tampered or manipulated content.
2. **Accessibility Solutions**:
   - Assists individuals with hearing impairments by providing accurate lipreading tools.
3. **Security and Surveillance**:
   - Enables lipreading in silent environments or poor audio conditions.
4. **Research in Speech Perception**:
   - Contributes to understanding the relationship between visual and auditory speech processing.

---

## Future Scope

1. **Transformer-Based Approaches**:
   - Explore transformer models for further improvements in sequence modeling.
2. **Diverse Datasets**:
   - Extend evaluations to more diverse and real-world datasets to generalize the system.
3. **Real-Time Applications**:
   - Develop a real-time lipreading system for surveillance and accessibility tools.
4. **Advanced Attention Mechanisms**:
   - Apply more sophisticated attention techniques for precise temporal alignment.

---

## Contributors

- **Harshith Deshalli Ravi**  
  [GitHub](https://github.com/HarshithDR)

- **Sachin Shivanna**  
  [GitHub](https://github.com/Sachin-Shivanna)
---

## References

1. Assael, Y., Shillingford, B., Whiteson, S., & de Freitas, N. (2016). **LipNet: End-to-End Sentence-Level Lipreading**.  
   [Paper Link](https://arxiv.org/abs/1611.01599)  

2. Xu, K., Li, D., Cassimatis, N., & Wang, X. (2018). **LCANet: End-to-End Lipreading with Cascaded Attention-CTC**.  
   [Paper Link](https://arxiv.org/pdf/1803.04988)  

3. GRID Corpus Dataset:  
   [GRID Corpus Link](https://spandh.dcs.shef.ac.uk/gridcorpus/)

4. GitHub Repository:  
   [LipNet Reference Repo](https://github.com/rizkiarm/LipNet)

---

## Contact

For questions or collaboration, feel free to reach out to **Harshith Deshalli Ravi** at [GitHub](https://github.com/HarshithDR).
