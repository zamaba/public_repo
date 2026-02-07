import json
import streamlit as st
from streamlit.components.v1 import html

# Mermaid diagram: corrected value flows and escaped characters for robust rendering
# Corrected flow: ChinaGov refined materials now feed into Power and Hyperscalers directly.
MERMAID_DIAGRAM = """
graph LR
    %% =====================
    %% GLOBAL STYLING
    %% =====================
    classDef china fill:#fee2e2,stroke:#ef4444,stroke-width:2px;
    classDef us fill:#dbeafe,stroke:#3b82f6,stroke-width:2px;
    classDef jp fill:#fef3c7,stroke:#f59e0b,stroke-width:2px;
    classDef nl fill:#f0fdf4,stroke:#22c55e,stroke-width:2px;
    classDef tw fill:#faf5ff,stroke:#a855f7,stroke-width:2px;
    classDef infra fill:#f3f4f6,stroke:#374151,stroke-width:2px;
    classDef capital fill:#ecfeff,stroke:#0891b2,stroke-width:2px;
    classDef constraint stroke-dasharray: 5 5;
    classDef valueBox fill:#fff7ed,stroke:#c2410c,stroke-width:2px;

    %% =====================
    %% LAYER 1 - RAW MATERIALS
    %% =====================
    subgraph L1["1. Raw Materials"]
        REE["Rare Earths<br/>Nd - Y"]:::china
        ChinaGov["China Mining and Refining<br/>~90% Global Monopoly"]:::china
        REE --> ChinaGov
    end

    %% =====================
    %% LAYER 2 - DESIGN AND TOOLS
    %% =====================
    subgraph L2["2. Design and Critical Tools"]
        EDA["EDA Software<br/>Synopsys - Cadence"]:::us
        ASML["EUV Lithography<br/>ASML Monopoly"]:::nl
        Nikon["DUV Lithography"]:::jp
        TEL["Deposition and Etch<br/>Tokyo Electron"]:::jp
        Design["AI Chip Design<br/>NVIDIA - AMD - Huawei"]
    end

    %% =====================
    %% LAYER 3 - FABRICATION
    %% =====================
    subgraph L3["3. Fabrication"]
        TSMC["TSMC Foundry<br/>~60% Advanced Share"]:::tw
        Samsung["Samsung Foundry"]
        SMIC["SMIC Fab<br/>7nm (Constrained)"]:::china
    end

    %% =====================
    %% LAYER 4 - COMPUTE AND POWER
    %% =====================
    subgraph L4["4. Compute and Power Bottleneck"]
        Hyperscalers["Hyperscalers<br/>AWS - Google - Meta - Azure"]:::us
        Stargate["Project Stargate<br/>&#36;100B-&#36;500B JV"]
        Power["Baseload Power<br/>Nuclear - Grid"]:::infra
        Cooling["Thermal Systems<br/>Liquid and Seawater"]:::infra
    end

    %% =====================
    %% LAYER 5 - CAPITAL
    %% =====================
    subgraph L5["5. Capital Stack"]
        Goldman["Goldman Sachs<br/>Capital Solutions"]:::us
        VC["Private Credit<br/>GIC - CPP - Blue Owl"]:::capital
    end

    %% =====================
    %% CORE VALUE FLOW
    %% =====================
    ChinaGov --> Power
    ChinaGov --> Hyperscalers
    EDA --> Design
    ASML --> TSMC
    Nikon --> TSMC
    TEL --> TSMC
    Design --> TSMC
    TSMC --> Hyperscalers
    Hyperscalers --> Stargate
    Stargate --> Power
    Power --> Cooling

    %% =====================
    %% CAPITAL FLOWS
    %% =====================
    Goldman --> Stargate
    VC --> Stargate

    %% =====================
    %% GEOPOLITICAL CONSTRAINTS
    %% =====================
    ChinaGov -. "Export Leverage" .-> ASML:::constraint
    ASML -. "EUV Export Controls" .-> SMIC:::constraint
    EDA -. "Advanced Node Limits" .-> Design:::constraint
    Power -. "Grid Lag: 5-7 Years" .-> Cooling:::constraint

    %% =====================
    %% VALUE CONTEXT (SYSTEM-LEVEL)
    %% =====================
    subgraph Scale["System-Level Scale"]
        GlobalImpact["&#36;15.7T Global Impact (2030)"]:::valueBox
        FabCapEx["&#36;5T-&#36;7T Required for Global Fabs"]:::valueBox
        AISpend["&#36;1T AI CapEx by 2027"]:::valueBox
        DCUnit["&#36;12B per 250MW Data Center"]:::valueBox
        ChinaFund["&#36;41B China State Chip Fund"]:::valueBox
    end

    %% =====================
    %% CONTEXT ANCHORS
    %% =====================
    GlobalImpact -.-> Hyperscalers
    FabCapEx -.-> TSMC
    AISpend -.-> Stargate
    DCUnit -.-> Power
    ChinaFund -.-> SMIC

    %% =====================
    %% CLASS ASSIGNMENTS
    %% =====================
    class ChinaGov,SMIC,REE china;
    class EDA,Hyperscalers,Goldman us;
    class Nikon,TEL jp;
    class ASML nl;
    class TSMC tw;
"""

# Expanded intelligence layers with high-depth analysis of chokepoints
LAYER_MARKDOWN = {
    "AI Supply Chain: Overview": """
The AI supply chain is undergoing a fundamental transformation, shifting from a focus on software code to a massive, resource-intensive industrial marathon. This explorer identifies the critical chokepoints where technical, geopolitical, and environmental constraints collide in a "25,000-mile journey."

The primary systemic challenge is the clash of timescales. While AI models iterate and double in complexity every few months, the physical infrastructure they require, including foundries, reactors, and transmission lines, takes years or even decades to deploy. This mismatch is why compute progress is now gated by "land and steel" rather than just "math and logic."

The economic stakes are historic. Estimates suggest AI could add $15.7 trillion to the global economy by 2030, exceeding the current combined output of China and India. To capture this value, scaling has become the primary driver of capital expenditure, leading to a projected $1 trillion investment by hyperscalers in the coming years.

The setting for this race has moved from Silicon Valley offices to the "Silicon Prairie" of data centers. Frontier models are now being forged with concrete and unprecedented amounts of electricity, as the industry races to build AI factories that dwarf the compute capacity of the previous cloud computing era.

By navigating the layers on the right, you can investigate the unique moats that define the struggle for AI supremacy, from the atomic purity of silicon to the complex financial engineering used to fund $500 billion infrastructure joint ventures.
""",
    "Layer 1 - Resource and Extraction": """
### 1. The Resource and Extraction Phase (Layer 1)

**Layer Challenges:** The foundation of the AI era relies on geological scarcity. While elements like silicon are abundant, the Rare Earth Elements (REEs) required for high-performance hardware exist in low concentrations and are notoriously difficult to separate and refine without severe environmental degradation.

**The Chinese Refining Monopoly:** China currently maintains a 90% global monopoly over REE refining. This is a critical strategic lever; these refined materials are essential for producing the high-performance permanent magnets used in server cooling fans, storage drive motors, and the gas and nuclear turbines that power data centers.

**The Purity Standard:** Quartz sand must be purified to 9N (99.9999999%) to become semiconductor-grade silicon. Through the Czochralski method, single-crystal silicon ingots are grown and sliced into thin wafers. Any microscopic impurity at this stage can cause faults that render a multi-billion transistor chip completely non-functional.

**Environmental and Ethical Friction:** The high environmental cost of traditional refining (like acid leaching) creates an ESG barrier for Western firms, reinforcing a dependency on existing Chinese infrastructure. Furthermore, rapid hardware cycles are projected to generate waste equivalent to 13 billion iPhones annually by 2030, creating a massive end-of-life challenge.

**Strategic Decoupling:** To break this geological dependency, Western firms are investing in circular economy initiatives. Techniques like phytomining (using plants to extract soil metals) and advanced recycling from decommissioned GPUs are being researched to recover materials and insulate the supply chain from geopolitical export restrictions.
""",
    "Layer 2 - Design and Tooling": """
### 2. The Design and Tooling Moat (Layer 2)

**Layer Challenges:** This layer represents the knowledge moat. The software and machinery required to build modern AI chips are the result of decades of cumulative industrial experience that cannot be replicated through simple capital investment.

**EDA Gatekeepers:** American firms like Synopsys and Cadence dominate Electronic Design Automation (EDA). This software is the only way to manage the complexity of designing billions of transistors. EDA is the ultimate gatekeeper; without it, advanced architectural concepts like FinFET or GAAFET cannot be physically realized on silicon.

**The EUV Chokepoint:** The Netherlands' ASML is the solo global provider of Extreme Ultraviolet (EUV) lithography. These machines use light wavelengths so small they are absorbed by air, requiring a vacuum environment. This technology is mandatory for producing chips at 5nm and below, making it the primary target for international export controls.

**Japanese Specialized SME:** Japanese firms like Tokyo Electron and Nikon provide the critical etching and Deep Ultraviolet (DUV) tools. While less advanced than EUV, these tools are essential for the multi-patterning techniques used to maximize older 7nm and 14nm process nodes, making Japan a vital partner in Western alliances.

**Architectural Freezing:** By restricting access to these tools, Western nations have effectively frozen the development roadmap for unaligned competitors. This makes it economically impossible for them to scale indigenous frontier AI, as they are forced to innovate around older, less efficient hardware while the global leaders pull further ahead.
""",
    "Layer 3 - Fabrication": """
### 3. The 25,000-Mile Fabrication Loop (Layer 3)

**Layer Challenges:** Fabrication is geographically concentrated and extremely high-risk. A single fab takes years to build and requires a specialized talent pool that exists in only a handful of regions worldwide.

**Taiwan-Centricity:** TSMC produces around 60% of the world's advanced node chips. This geographic concentration creates a single point of failure for the global digital economy, driving the US and EU to offer massive subsidies to lure foundries back to domestic soil and insulate the AI economy from regional shocks.

**The Packaging Bottleneck:** The bottleneck has moved from making chips to stacking them. Techniques like CoWoS (Chip-on-Wafer-on-Substrate) are the current limit on NVIDIA's output. This microscopic fusion of logic GPUs and high-bandwidth memory (HBM) chiplets is notoriously difficult to scale, even when logic chip yields are high.

**The Yield Economics:** Fabs must achieve a 60-80% success rate per wafer to be profitable. New entrants often see yields as low as 10%, meaning they lose money on every wafer produced. This yield gap creates a massive financial barrier that prevents new players from reaching commercial parity with industry veterans.

**The Logistical Odyssey:** A single high-performance GPU may travel 25,000 miles globally, moving between foundries in Taiwan, testing facilities in Southeast Asia, and data centers in the US, before it is ever deployed. Any disruption, from a canal blockage to a trade tariff, impacts the global AI CapEx cycle immediately.
""",
    "Layer 4 - Power and Infrastructure": """
### 4. The Power and Infrastructure Bottleneck (Layer 4)

**Layer Challenges:** AI compute demand is advancing at digital speed, while power infrastructure moves at permitting speed. We have reached the physical limit of what existing, 40-year-old electrical grids can support.

**Exponential Power Density:** Modern AI factories require 50x more power density per server rack than the cloud data centers of five years ago. This surge has ended a decade of flat power demand in the United States, catching utilities off guard and creating a massive backlog for grid connections.

**The 7-Year Grid Lag:** Permitting and building a new natural gas plant or interregional transmission line typically takes 5-7 years. AI labs cannot wait this long, forcing them to become their own power utilities and seek unconventional behind-the-meter energy sources.

**The Nuclear Renaissance:** To secure 24/7 carbon-free baseload power, Microsoft, Google, and Amazon are restarting shuttered reactors (like Three Mile Island) and investing in Small Modular Reactors (SMRs). Nuclear is the only carbon-neutral source that matches the multi-GW scale required for projects like Stargate.

**Thermal Innovation:** Traditional air cooling is insufficient for the density of GPU clusters. The shift to liquid cooling and seawater passive cooling projects (like China's Highlander underwater centers) is now a requirement to prevent hardware from melting under its own heat, driving a total redesign of data center architecture.
""",
    "Layer 5 - Capital Stack": """
### 5. Financial Engineering and Capital Stack (Layer 5)

**Layer Challenges:** AI infrastructure represents a new asset class that traditional banking is not yet fully equipped to handle. The massive $12B cost of a single data center unit, combined with rapid hardware obsolescence, creates unique underwriting risks.

**The Obsolescence Mismatch:** A data center building lasts 30 years, but the $9 billion of GPUs inside may be obsolete in only 3 years. This mismatch makes traditional long-term real estate loans difficult to secure, forcing a reliance on high-grade structured capital and innovative financing.

**Capital Recycling:** Investment banks like Goldman Sachs create liquidity by refinancing stabilized, cash-flowing data centers into Asset-Backed Securities (ABS). This allows developers to pull their equity out of completed projects and recycle it into the next wave of infrastructure, sustaining the $1T CapEx cycle.

**The Rise of Private Credit:** With over $4 trillion in global dry powder, financial sponsors (like GIC, CPP, and Blue Owl) are filling the gap left by traditional banks. They treat AI infrastructure as a long-term utility play, offering the steady returns required by pension and insurance funds.

**Data Center Diplomacy:** Countries are now treating AI infrastructure like sovereign embassies. By offering tax reforms, land grants, and data residency laws, they aim to host the AI factories that will anchor the digital economy of the next fifty years, treating compute as the new strategic commodity.
""",
    "Sources and References": """
### Primary Sources for this Analysis

* **Kinaxis:** [The Supply Chain of AI (Faye Baker)](https://www.kinaxis.com/en/blog/supply-chain-ai) - Analysis of REE refining, the 25,000-mile chip journey, and the 13B iPhone e-waste projection.
* **Goldman Sachs:** [Powering the AI Era (Global Investment Banking)](https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/powering-the-ai-era/report.pdf) - Source for the $1T hyperscale CapEx projections, the 5-7 year grid bottleneck, and the SASB capital recycling cycle.
* **IAPS:** [Introduction to AI Chip Making in China](https://www.iaps.ai/research/how-ai-chips-are-made) - Source for technical details on EUV and DUV lithography chokepoints, SMIC node progress, and atomic-level silicon purity.
""",
}

NODE_TO_LAYER = {
    "REE": "Layer 1 - Resource and Extraction",
    "ChinaGov": "Layer 1 - Resource and Extraction",
    "EDA": "Layer 2 - Design and Tooling",
    "ASML": "Layer 2 - Design and Tooling",
    "Nikon": "Layer 2 - Design and Tooling",
    "TEL": "Layer 2 - Design and Tooling",
    "Design": "Layer 2 - Design and Tooling",
    "TSMC": "Layer 3 - Fabrication",
    "Samsung": "Layer 3 - Fabrication",
    "SMIC": "Layer 3 - Fabrication",
    "Hyperscalers": "Layer 4 - Power and Infrastructure",
    "Stargate": "Layer 4 - Power and Infrastructure",
    "Power": "Layer 4 - Power and Infrastructure",
    "Cooling": "Layer 4 - Power and Infrastructure",
    "Goldman": "Layer 5 - Capital Stack",
    "VC": "Layer 5 - Capital Stack",
}


def render_mermaid(diagram: str, height: int = 800) -> None:
    node_map = json.dumps(NODE_TO_LAYER)
    html(
        f"""
        <style>
            #mermaid-container {{ width: 100%; height: 520px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
            .mermaid {{ width: 100%; height: 100%; }}
        </style>
        <div id="mermaid-container"><div class="mermaid" id="graph-div">{diagram}</div></div>
        <script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
        <script type="module">
            import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
            mermaid.initialize({{ startOnLoad: false, theme: "neutral", securityLevel: 'loose', flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }} }});
            async function render() {{
                const element = document.querySelector("#graph-div");
                const {{ svg }} = await mermaid.render('rendered-svg', element.textContent);
                element.innerHTML = svg;
                const svgElement = document.querySelector("#rendered-svg");
                if (svgElement) {{
                    svgElement.style.width = "100%"; svgElement.style.height = "100%";
                    svgPanZoom(svgElement, {{ zoomEnabled: true, panEnabled: true, controlIconsEnabled: true, fit: true, center: true, minZoom: 0.1, maxZoom: 10 }});
                }}
            }}
            render();
        </script>
        """,
        height=height,
    )


def main() -> None:
    st.set_page_config(page_title="AI Supply Chain Explorer", layout="wide")
    st.title("AI Supply Chain Explorer")
    st.markdown(
        "Interactive map of the global AI hardware, power, and capital ecosystem."
    )

    col1, col2 = st.columns([2, 1.2])
    layer_options = list(LAYER_MARKDOWN.keys())

    if "selected_layer" not in st.session_state:
        st.session_state.selected_layer = layer_options[0]

    with col1:
        st.subheader("System Interaction Map")
        render_mermaid(MERMAID_DIAGRAM)
        st.caption(
            "Select an intelligence layer on the right for deep-dive analysis and source references."
        )

    with col2:
        st.subheader("Layer Intelligence")
        selected_layer = st.radio(
            "Select a Layer to Investigate:",
            options=layer_options,
            key="layer_nav_radio",
        )
        st.divider()
        st.markdown(LAYER_MARKDOWN[selected_layer])

    st.divider()
    st.subheader("Key Market Metrics (Data-Validated)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Global Economic Impact (2030)", "$15.7 Trillion")
    m2.metric("Projected AI CapEx (2027)", "$1.0 Trillion")
    m3.metric("China REE Mono-Refining", "90%")


if __name__ == "__main__":
    main()
