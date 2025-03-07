import streamlit as st
from PIL import Image
import base64
from navbar import navbar
from footer import footer

# Import custom CSS
from styles import load_styles

# Set Page Configuration
st.set_page_config(
    page_title="Diagnostics - MediMind",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom styles
load_styles()

# Import custom components
# Note: These are placeholders for your actual navbar and footer imports
# from components.navbar import navbar
# from components.footer import footer

# Helper functions
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Custom CSS for Navbar and Footer (since we're using the imported ones)
st.markdown("""
<style>
    /* Additional styling specific to this page */
    .upload-section {
        margin-top: 20px;
        margin-bottom: 30px;
    }
    
    .section-container {
        background-color: var(--bg-white);
        border-radius: 12px;
        padding: 25px;
        box-shadow: var(--shadow);
        margin-bottom: 25px;
    }
    
    .upload-area {
        border: 2px dashed var(--primary-light);
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        transition: all 0.3s;
        background-color: white;
    }
    
    .upload-area:hover {
        border-color: var(--primary);
        transform: translateY(-5px);
    }
    
    .icon-large {
        font-size: 48px;
        color: var(--primary);
        margin-bottom: 15px;
    }
    
    .results-box {
        background-color: rgba(45, 140, 255, 0.05);
        border-radius: 8px;
        padding: 20px;
        margin-top: 15px;
    }
    
    .result-item {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .result-icon {
        margin-right: 10px;
        color: var(--primary);
        font-size: 20px;
    }
    
    .how-it-works-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 20px;
    }
    
    .step-card {
        text-align: center;
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: var(--shadow);
        flex: 1;
        min-width: 200px;
        transition: transform 0.3s;
    }
    
    .step-card:hover {
        transform: translateY(-5px);
    }
    
    .step-icon {
        font-size: 36px;
        color: var(--primary);
        margin-bottom: 15px;
    }
    
    .step-number {
        background-color: var(--primary);
        color: white;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 10px;
    }
    
    .security-banner {
        display: flex;
        align-items: center;
        background-color: #0D92F4;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
        
    }
    
    .security-icon {
        font-size: 24px;
        margin-right: 15px;
        color: var(--primary);
    }
    
    /* Placeholder for analysis visuals */
    .analysis-placeholder {
        height: 300px;
        background-color: #f8f9fa;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
        border: 1px dashed #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

# Main content
def main():
    
    navbar()
    
    # Since we don't have the actual navbar() function, let's create a placeholder
    
    # Hero Section
    with st.container():
        st.markdown('''
        <div class="hero">
            <div class="hero-content">
                <h1>Medical Report Analysis</h1>
                <p>Upload your medical report to receive AI-powered insights and explanations.</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Report Upload Section
    with st.container():
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><i>📋</i> Upload Your Medical Report</div>', unsafe_allow_html=True)
        
        # File uploader with custom styling
        uploaded_file = st.file_uploader("", type=["pdf"], key="medical_report")
        
        # Display additional information about upload
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown('<div class="security-banner" ><span class="security-icon">🔒</span> <strong>Your data is secure</strong>: All medical reports are encrypted and processed securely. Your data is never shared with third parties and is automatically deleted after analysis.</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<p style="text-align: right; color: var(--text-light);">Maximum file size: 20MB</p>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

    # Analysis Results Section (shown only when a file is uploaded)
    if uploaded_file is not None:
        with st.container():
            st.markdown('<div class="section-container">', unsafe_allow_html=True)
            st.markdown('<div class="section-header"><i>🔬</i> Analysis Results</div>', unsafe_allow_html=True)
            
            # Add a loading spinner to indicate processing
            with st.spinner("Processing your medical report..."):
                # Simulate processing time
                import time
                time.sleep(2)
            
            # Success message
            st.success("✅ Report successfully analyzed!")
            
            # Tabs for different views of the results
            tab1, tab2, tab3 = st.tabs(["Summary", "Detailed Report", "Recommendations"])
            
            with tab1:
                st.markdown("<h3>Key Findings</h3>", unsafe_allow_html=True)
                st.markdown('''
                <div class="results-box">
                    <div class="result-item">
                        <span class="result-icon">🔍</span>
                        <div>
                            <strong>Primary Observations:</strong> Normal blood pressure, elevated cholesterol levels
                        </div>
                    </div>
                    <div class="result-item">
                        <span class="result-icon">⚠</span>
                        <div>
                            <strong>Areas of Concern:</strong> LDL cholesterol above recommended range
                        </div>
                    </div>
                    <div class="result-item">
                        <span class="result-icon">✅</span>
                        <div>
                            <strong>Normal Results:</strong> Blood glucose, kidney function, liver enzymes
                        </div>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
                
            with tab2:
                st.markdown("<h3>Comprehensive Analysis</h3>", unsafe_allow_html=True)
                
                # Example visualization placeholder
                st.markdown('<div class="analysis-placeholder">Interactive report visualization would appear here</div>', unsafe_allow_html=True)
                
                # Example of detailed metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Total Cholesterol", value="220 mg/dL", delta="20 mg/dL")
                    st.metric(label="Blood Pressure", value="120/80 mmHg", delta="-5 mmHg")
                    
                with col2:
                    st.metric(label="Blood Glucose", value="85 mg/dL", delta="-3 mg/dL")
                    st.metric(label="HDL Cholesterol", value="45 mg/dL", delta="2 mg/dL")
                    
                # Sample technical details (collapsible)
                with st.expander("Technical Details"):
                    st.write("""
                    *Laboratory Values:*
                    - WBC: 7.2 x10^3/uL (Normal range: 4.5-11.0)
                    - RBC: 5.0 x10^6/uL (Normal range: 4.5-5.9)
                    - Hemoglobin: 14.2 g/dL (Normal range: 13.5-17.5)
                    - Hematocrit: 42% (Normal range: 41-50%)
                    - Platelets: 250 x10^3/uL (Normal range: 150-450)
                    """)
                
            with tab3:
                st.markdown("<h3>Personalized Recommendations</h3>", unsafe_allow_html=True)
                
                st.markdown('''
                <div class="results-box">
                    <div class="result-item">
                        <span class="result-icon">🥗</span>
                        <div>
                            <strong>Dietary Changes:</strong> Consider adopting a Mediterranean diet to help lower cholesterol levels
                        </div>
                    </div>
                    <div class="result-item">
                        <span class="result-icon">🏃</span>
                        <div>
                            <strong>Exercise:</strong> Aim for at least 150 minutes of moderate aerobic activity weekly
                        </div>
                    </div>
                    <div class="result-item">
                        <span class="result-icon">🔄</span>
                        <div>
                            <strong>Follow-up:</strong> Schedule a follow-up lipid panel in 3 months
                        </div>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
                
                # Call-to-action button
                st.markdown('<a href="#" class="btn">Download Full Report</a>', unsafe_allow_html=True)
                
            st.markdown('</div>', unsafe_allow_html=True)

    # How It Works Section
    with st.container():
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><i>🔎</i> How It Works</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('''
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-icon">📤</div>
                <h3 style = "color: #4C585B;">Upload</h3>
                <p>Upload your medical report in PDF format. We support reports from most healthcare providers.</p>
            </div>
            ''', unsafe_allow_html=True)
            
        with col2:
            st.markdown('''
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-icon">🧠</div>
                <h3 style = "color: #4C585B;">Analysis</h3>
                <p>Our AI analyzes your report, identifying key findings and translating medical terminology.</p>
            </div>
            ''', unsafe_allow_html=True)
            
        with col3:
            st.markdown('''
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-icon">📊</div>
                <h3 style = "color: #4C585B;">Results</h3>
                <p>Receive a clear, easy-to-understand summary with explanations and recommendations.</p>
            </div>
            ''', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        

    footer()
    
    

main()