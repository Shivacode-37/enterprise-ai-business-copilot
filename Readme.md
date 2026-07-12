# 📊 AI-Driven Business Analyst Copilot

### Profit Leakage Detection & Structural Risk Intelligence System

---

## 🚀 Overview

The **AI-Driven Business Analyst Copilot** is a structured analytics system designed to detect profit leakage, structural inefficiencies, and operational volatility from transactional business data.

Unlike traditional BI dashboards that only display KPIs, this system integrates deterministic validation logic, volatility modeling, stability classification, and intent-driven reasoning to deliver decision-ready business intelligence.

---

## 🎯 Problem Statement

Most analytics dashboards:

* Report metrics but do not detect structural inefficiencies
* Fail to identify volatility and instability patterns
* Lack interpretability and risk classification
* Cannot translate business questions into structured answers

This project addresses those limitations by combining analytics engineering with deterministic reasoning.

---

## 🏗 Architecture

<pre class="overflow-visible! px-0!" data-start="1229" data-end="1483"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Raw Transaction Data
        ↓
KPI & Metrics Engine
        ↓
Structural Risk Validation Layer
        ↓
Volatility & Stability Modeling
        ↓
Business </span><span>Summary</span><span> Layer
        ↓
Deterministic </span><span>Q</span><span>&</span><span>A</span><span> Engine
        ↓
Interactive Streamlit Dashboard
</span></span></code></div></div></pre>

The system follows a modular, layered architecture to ensure explainability, maintainability, and extensibility.

---

## 📊 Core Capabilities

### 1️⃣ KPI & Metrics Engine

* Total revenue and profit calculation
* Profit margin computation
* Loss order percentage analysis
* Dimension-level aggregation using Pandas

---

### 2️⃣ Structural Risk Detection

Identifies:

* Category-level inefficiencies
* Persistent loss patterns
* Structural collapse signals

Uses frequency analysis across time dimensions.

---

### 3️⃣ Volatility & Stability Modeling

Measures operational instability using:

* Standard deviation of loss ratios
* Cross-period consistency checks
* Stability classification (Stable / Moderate / Unstable)

Enables differentiation between structural risk and volatility risk.

---

### 4️⃣ Business Health Scoring

Generates a deterministic health score using:

* Profitability metrics
* Loss concentration modeling
* Weighted risk penalties

Produces executive-level risk classification.

---

### 5️⃣ Deterministic Q&A Engine

Implements intent-based routing to translate business queries into structured metric-driven responses.

Supports questions such as:

* “What is the business health score?”
* “How many orders are loss-making?”
* “Which category is most risky?”
* “Is the business stable?”

Designed without LLM dependency to ensure reliability and auditability.

---

### 6️⃣ Interactive Dashboard

Built using:

* Streamlit
* Plotly visualizations
* KPI cards
* Risk diagnostics tables
* Executive summary panel
* Business Q&A interface

Provides a stakeholder-ready analytical interface.

---

## 🛠 Technology Stack

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* Modular Architecture Design

---

## 📂 Project Structure

<pre class="overflow-visible! px-0!" data-start="3290" data-end="3480"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>ai-business-analyst-copilot/
│
├── </span><span>src</span><span>/
│   ├── metrics_engine</span><span>.py</span><span>
│   ├── ai_reasoning</span><span>.py</span><span>
│   └── data_processing</span><span>.py</span><span>
│
├── data/
│   └── sample_dataset</span><span>.csv</span><span>
│
├── app</span><span>.py</span><span>
└── README</span><span>.md</span><span>
</span></span></code></div></div></pre>

---

## ▶️ Running the Application

### Install dependencies

<pre class="overflow-visible! px-0!" data-start="3544" data-end="3591"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install streamlit pandas plotly
</span></span></code></div></div></pre>

### Launch dashboard

<pre class="overflow-visible! px-0!" data-start="3615" data-end="3647"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>streamlit run app.py
</span></span></code></div></div></pre>

Upload a CSV dataset to generate diagnostics and insights.

---

## 📈 Example Business Insights Generated

* Identification of categories with high structural inefficiency
* Detection of unstable loss behavior across time periods
* Volatility-driven risk prioritization
* Executive-level profitability health scoring

---

## 🧠 Design Principles

* Deterministic reasoning before generative AI
* Structured validation and explainability
* Separation of computation and reasoning layers
* Risk-aware decision intelligence
* Scalable architecture for future AI integration
