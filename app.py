import streamlit as st


# Configuration for the page
st.set_page_config(
    page_title="CarbonLens",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS for better styling
# st.markdown("""
#     <style>
#         .big-number {
#             font-size: 36px;
#             font-weight: bold;
#             color: #0f5132;
#         }
#         .description {
#             font-size: 14px;
#             color: #666;
#         }
#         .metric-card {
#             background-color: #f8f9fa;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         }
#         .stApp {
#             background-color: #ffffff;
#         }
#         h1 {
#             color: #1f5c3d;
#         }
#     </style>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
    .big-number {
        font-size: 36px;
        font-weight: bold;
        color: #00ff9d;
    }
    .description {
        font-size: 14px;
        color: #a3a3a3;
    }
    .metric-card {
        background-color: #262626;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .stApp {
        background-color: #0e1117;
    }
    h1 {
        color: #00ff9d;
    }
</style>
""", unsafe_allow_html=True)

HARDWARE_TYPES = ['A100 PCIe 40/80GB',
 'A100 SXM4 80 GB',
 'AGX Xavier',
 'AMD RX480',
 'GIGABYTE GTX 1660 OC',
 'GTX 1080 Ti',
 'GTX 1080',
 'GTX 750',
 'GTX TITAN X',
 'Quadro K6000',
 'Quadro P6000',
 'RTX 2080 Ti',
 'RTX 2080',
 'RTX 8000',
 'T4',
 'Tesla K40c',
 'Tesla K80',
 'Tesla M40 24GB',
 'Tesla P100',
 'Tesla P40',
 'Tesla V100-PCIE-16GB',
 'Tesla V100-SXM2-16GB',
 'Tesla V100-SXM2-32GB',
 'Titan RTX',
 'Titan V',
 'TITAN X Pascal',
 'Titan Xp',
 'TPUv2 Chip',
 'TPUv3 Chip',
 'RTX 3080',
 'RTX 3080 TI',
 'RTX 3090',
 'RTX 4090',
 'RTX A4000',
 'RTX A5000',
 'RTX A6000',
 'Intel Xeon E5-2699',
 'Intel Xeon E5-2630v4',
 'Intel Xeon E5-2650',
 'Intel Xeon Gold 5220',
 'Intel Xeon Gold 6148',
 'L4',
 'AMD EPYC 7763',
 'AMD EPYC 7282',
 'AMD EPYC 7702']

PROVIDERS = ['Google Cloud Platform',
 'Amazon Web Services',
 'Azure',
 'OVHCloud',
 'CoreWeave',
 'Seeweb']

REGION_MAPPING = {'Google Cloud Platform': ['asia-east1',
  'asia-east2',
  'asia-northeast1',
  'asia-northeast2',
  'asia-south1',
  'asia-southeast1',
  'australia-southeast1',
  'europe-north1',
  'europe-west1',
  'europe-west2',
  'europe-west3',
  'europe-west4',
  'europe-west6',
  'northamerica-northeast1',
  'southamerica-east1',
  'us-central1',
  'us-east1',
  'us-east4',
  'us-west1',
  'us-west2',
  'us-west3'],
 'Amazon Web Services': ['ap-east-1',
  'ap-northeast-1',
  'ap-northeast-2',
  'ap-northeast-3',
  'ap-south-1',
  'ap-southeast-1',
  'ap-southeast-2',
  'ca-central-1',
  'cn-north-1',
  'cn-northwest-1',
  'eu-central-1',
  'eu-north-1',
  'eu-west-1',
  'eu-west-2',
  'eu-west-3',
  'sa-east-1',
  'us-east-1',
  'us-east-2',
  'us-gov-east-1',
  'us-gov-west-1',
  'us-west-1',
  'us-west-2'],
 'Azure': ['australiacentral',
  'australiacentral2',
  'australiaeast',
  'australiasoutheast',
  'brazilsouth',
  'canadacentral',
  'canadaeast',
  'centralindia',
  'centralus',
  'eastasia',
  'eastus',
  'eastus2',
  'francecentral',
  'francesouth',
  'japaneast',
  'japanwest',
  'koreacentral',
  'koreasouth',
  'northcentralus',
  'northeurope',
  'southafricanorth',
  'southafricawest',
  'southcentralus',
  'southeastasia',
  'southindia',
  'uksouth',
  'ukwest',
  'westcentralus',
  'westeurope',
  'westindia',
  'westus',
  'westus2'],
 'OVHCloud': ['bhs', 'gra'],
 'CoreWeave': ['LAS1', 'LGA1', 'ORD1'],
 'Seeweb': ['fro2']}

GPU_POWER = {'A100 PCIe 40/80GB': 250,
 'A100 SXM4 80 GB': 400,
 'AGX Xavier': 30,
 'AMD RX480': 150,
 'GIGABYTE GTX 1660 OC': 120,
 'GTX 1080 Ti': 250,
 'GTX 1080': 180,
 'GTX 750': 250,
 'GTX TITAN X': 250,
 'Quadro K6000': 225,
 'Quadro P6000': 250,
 'RTX 2080 Ti': 250,
 'RTX 2080': 215,
 'RTX 8000': 260,
 'T4': 70,
 'Tesla K40c': 245,
 'Tesla K80': 300,
 'Tesla M40 24GB': 250,
 'Tesla P100': 250,
 'Tesla P40': 250,
 'Tesla V100-PCIE-16GB': 300,
 'Tesla V100-SXM2-16GB': 250,
 'Tesla V100-SXM2-32GB': 300,
 'Titan RTX': 280,
 'Titan V': 250,
 'TITAN X Pascal': 250,
 'Titan Xp': 250,
 'TPUv2 Chip': 221,
 'TPUv3 Chip': 283,
 'RTX 3080': 320,
 'RTX 3080 TI': 350,
 'RTX 3090': 350,
 'RTX 4090': 300,
 'RTX A4000': 140,
 'RTX A5000': 230,
 'RTX A6000': 300,
 'Intel Xeon E5-2699': 145,
 'Intel Xeon E5-2630v4': 85,
 'Intel Xeon E5-2650': 105,
 'Intel Xeon Gold 5220': 125,
 'Intel Xeon Gold 6148': 150,
 'L4': 72,
 'AMD EPYC 7763': 280,
 'AMD EPYC 7282': 120,
 'AMD EPYC 7702': 200}

CARBON_REGION = {'Amazon Web Services': {'ap-east-1': 0.702,
  'ap-northeast-1': 0.516,
  'ap-northeast-2': 0.517,
  'ap-northeast-3': 0.516,
  'ap-south-1': 0.92,
  'ap-southeast-1': 0.419,
  'ap-southeast-2': 0.802,
  'ca-central-1': 0.02,
  'cn-north-1': 0.68,
  'cn-northwest-1': 0.68,
  'eu-central-1': 0.615,
  'eu-north-1': 0.047,
  'eu-west-1': 0.617,
  'eu-west-2': 0.623,
  'eu-west-3': 0.105,
  'sa-east-1': 0.205,
  'us-east-1': 0.3678,
  'us-east-2': 0.5682,
  'us-gov-east-1': 0.5682,
  'us-gov-west-1': 0.29760000000000003,
  'us-west-1': 0.24059999999999998,
  'us-west-2': 0.29760000000000003},
 'Azure': {'australiacentral': 0.9,
  'australiacentral2': 0.9,
  'australiaeast': 0.802,
  'australiasoutheast': 0.805,
  'brazilsouth': 0.205,
  'canadacentral': 0.0693,
  'canadaeast': 0.02,
  'centralindia': 0.92,
  'centralus': 0.7366,
  'eastasia': 0.702,
  'eastus': 0.3678,
  'eastus2': 0.3678,
  'francecentral': 0.105,
  'francesouth': 0.105,
  'japaneast': 0.516,
  'japanwest': 0.516,
  'koreacentral': 0.517,
  'koreasouth': 0.517,
  'northcentralus': 0.5682,
  'northeurope': 0.617,
  'southafricanorth': 1.009,
  'southafricawest': 1.009,
  'southcentralus': 0.4604,
  'southeastasia': 0.419,
  'southindia': 0.92,
  'uksouth': 0.623,
  'ukwest': 0.623,
  'westcentralus': 0.29760000000000003,
  'westeurope': 0.569,
  'westindia': 0.92,
  'westus': 0.24059999999999998,
  'westus2': 0.29760000000000003},
 'CoreWeave': {'LAS1': 0.47458, 'LGA1': 0.28275, 'ORD1': 0.4245},
 'Google Cloud Platform': {'asia-east1': 0.557,
  'asia-east2': 0.702,
  'asia-northeast1': 0.516,
  'asia-northeast2': 0.516,
  'asia-south1': 0.92,
  'asia-southeast1': 0.419,
  'australia-southeast1': 0.802,
  'europe-north1': 0.211,
  'europe-west1': 0.267,
  'europe-west2': 0.623,
  'europe-west3': 0.615,
  'europe-west4': 0.569,
  'europe-west6': 0.016,
  'northamerica-northeast1': 0.0345,
  'southamerica-east1': 0.205,
  'us-central1': 0.5662999999999999,
  'us-east1': 0.3678,
  'us-east4': 0.3678,
  'us-west1': 0.29760000000000003,
  'us-west2': 0.24059999999999998,
  'us-west3': 0.2721},
 'OVHCloud': {'bhs': 0.02, 'gra': 0.105},
 'Seeweb': {'fro2': 0.0}}

kgC02PerKm = (3.98 * 1e-4 * 1e3) / 1.609344
kgCoalBurnedPerKg = 9.05 * 1e-4 * 1e3 * 2.204623
kgC02SequestratedBySeedling = 0.06 * 1e3

def calculate_co2_emissions(hardware_type, num_gpus, hours, provider, region):
    """
    Calculate CO2 emissions based on input parameters.
    To be implemented later.
    """
    co2_emission = GPU_POWER[hardware_type] * num_gpus * hours * CARBON_REGION[provider][region] / 1000
    return co2_emission

def calculate_equivalent_distance(co2_emissions):
    """
    Calculate equivalent distance driven by an average passenger vehicle.
    To be implemented later.
    """
    eqDriven = round(co2_emissions / kgC02PerKm, 2)
    return eqDriven

def calculate_equivalent_coal(co2_emissions):
    """
    Calculate equivalent coal burned.
    To be implemented later.
    """
    eqCoal = round(co2_emissions / kgCoalBurnedPerKg, 2)
    return eqCoal

def calculate_equivalent_trees(co2_emissions):
    """
    Calculate equivalent CO2 sequestrated by seedling trees in 10 years.
    To be implemented later.
    """
    eqTrees = round(co2_emissions / kgC02SequestratedBySeedling, 2)
    return eqTrees

def calculate_llm_emissions(num_queries):
        """
        Calculate CO2 emissions for Large Language Models.
        """
        # CO2 emissions per query
        co2_emission_per_query = 4.2e-3
        co2_emissions = num_queries * co2_emission_per_query * 24 * 365
        return co2_emissions

# Give title to sidebar as Services
st.sidebar.title("Services")

# make a radio button to select the page. format them prettily
page = st.sidebar.radio("Select a Service", ["Model Training CO2 Emissions", "LLM API CO2 Emissions"])

# Input section

if page == "Model Training CO2 Emissions":
    st.title("CarbonLens")
    st.subheader("🏭 ML Model CO2 Emissions Calculator")
    
    st.markdown("### Input Parameters")
    col1, col2 = st.columns(2)

    with col1:
        col11, col12 = st.columns(2)
        with col11:
            hardware_type = st.selectbox("Hardware Type", HARDWARE_TYPES)
        with col12:
            num_gpus = st.number_input("Number of GPUs", min_value=1, step=1, value=1)
        # take hours input as a float
        hours = st.number_input("Duration (hours)", min_value=0.0, step=0.1, value=1.0)

    with col2:
        provider = st.selectbox("Cloud Provider", PROVIDERS)
        region = st.selectbox(
            "Region",
            REGION_MAPPING[provider],
            key="region"
        )

    # Calculate emissions when user clicks the button
    if st.button("Calculate Emissions", type="primary"):
        co2_emissions = calculate_co2_emissions(hardware_type, num_gpus, hours, provider, region)
        
        # Display total emissions
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Total CO2 Emissions")
            st.markdown(f"""
                <div class="metric-card">
                    <span class="big-number">{co2_emissions:,.2f}</span>
                    <span style="font-size: 24px;"> kg CO2 equivalent</span>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('### Equivalent to')
            st.markdown(f"""
                <div class="metric-card">
                    <span class="big-number">{co2_emissions / 1000:,.2f}</span>
                    <span style="font-size: 24px;"> Carbon Credits</span>
                </div>
            """, unsafe_allow_html=True)

        
        # Display equivalent metrics
        st.markdown("### Environmental Impact Equivalents")
        
        # Create three columns for equivalents
        col1, col2, col3 = st.columns(3)
        
        # Column 1: Equivalent distance
        with col1:
            distance = calculate_equivalent_distance(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{distance:,.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">Kms</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Driven by an average passenger vehicle</span>
                    </div>
                """, unsafe_allow_html=True)
        
        # Column 2: Equivalent coal
        with col2:
            coal = calculate_equivalent_coal(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{coal:,.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">Kgs</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Of coal burned</span>
                    </div>
                """, unsafe_allow_html=True)
        
        # Column 3: Equivalent trees
        with col3:
            trees = calculate_equivalent_trees(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{trees:,.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">trees</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Of CO2 sequestrated by seedling trees in 10 years</span>
                    </div>
                """, unsafe_allow_html=True)

        # Add information about the calculation
        # st.markdown("### Calculation Details")
        # st.markdown(f"""
        # - **Hardware**: {hardware_type}
        # - **Duration**: {hours} hours
        # - **Provider**: {provider}
        # - **Region**: {region}
        # """)

    

elif page == f"LLM API CO2 Emissions":
    st.title("CarbonLens")

    st.markdown("### ☁️ Hidden Emissions of using Large Language Models")
    st.markdown("""#### Did you Know?
##### ChatGPT releases 42,000 Kgs of CO2 per day, equivalent to driving 100,000 Kms in an average passenger vehicle.
""")

    st.markdown("#### Input Parameters")

    num_queries = st.number_input("Number of queries per hour", min_value=0, step=1, value=1)

    if st.button("Calculate Emissions", type="primary"):
        st.write("Calculating emissions for", num_queries, "queries per hour")

        # Calculate emissions when user clicks the button
        co2_emissions = calculate_llm_emissions(num_queries)
        
        # Display total emissions
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Total CO2 Emissions in a given year")
            st.markdown(f"""
                <div class="metric-card">
                    <span class="big-number">{co2_emissions:.2f}</span>
                    <span style="font-size: 24px;"> kg CO2 equivalent</span>
                </div>
            """, unsafe_allow_html=True)

        # Display equivalent metrics
        st.markdown("### Environmental Impact Equivalents")

        # Create three columns for equivalents
        col1, col2, col3 = st.columns(3)

        # Column 1: Equivalent distance
        with col1:
            distance = calculate_equivalent_distance(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{distance:.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">Kms</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Driven by an average passenger vehicle</span>
                    </div>
                """, unsafe_allow_html=True)

        # Column 2: Equivalent coal
        with col2:
            coal = calculate_equivalent_coal(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{coal:.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">Kgs</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Of coal burned</span>
                    </div>
                """, unsafe_allow_html=True)

        # Column 3: Equivalent trees
        with col3:
            trees = calculate_equivalent_trees(co2_emissions)
            left_col, right_col = st.columns([1, 1])
            with left_col:
                st.markdown(f"""
                    <div class="metric-card">
                        <span class="big-number">{trees:.1f}</span>
                        <br/>
                        <span class="description" style="font-size: 16px;">trees</span>
                    </div>
                """, unsafe_allow_html=True)
            with right_col:
                st.markdown("""
                    <div style="padding-top: 20px;">
                        <span class="description" style="font-size: 16px;">Of CO2 sequestrated by seedling trees in 10 years</span>
                    </div>
                """, unsafe_allow_html=True)

        # Add information about the calculation

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    Team Members:
    - [Akhil Dua](https://www.linkedin.com/in/akhil--dua/)
    - [Arihant Sheth](https://www.linkedin.com/in/arihantsheth/)
    - [Mahima Jagadeesh Patel](https://www.linkedin.com/in/mahima-jagadeesh-patel-8641441a3/)
    - [Reuben Mathew](https://www.linkedin.com/in/iamreubengm/)
    """)

with col2:
    st.markdown("""
You can find the code for this project on [GitHub](https://github.com/AryaStark13/CMU-BNY-Datathon)
            
You can find our submission notebook [here](https://colab.research.google.com/drive/1NoLJQ5fjS00PnTC9FNXzQB_4NukTVwS0?usp=sharing)
            
You can find our final video submission [here](https://drive.google.com/file/d/1kJrBznn2JJ77qxepGrLWU6I-xTOgI61o/view?usp=sharing)
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ to help reduce ML's carbon footprint for CMU BNY Mellon Datathon 2024")