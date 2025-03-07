import streamlit as st
from navbar import navbar
from styles import load_styles
from footer import footer

# Set Page Configuration
st.set_page_config(
    page_title="MediMind AI | Healthcare Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom styles
load_styles()

# Display navbar
navbar()

# Hero Section with Modern Design
st.markdown(
    """
    <div class="hero" id="home">
        <div class="hero-content">
            <h1>
                <span style="color: #2D8CFF;">Medi</span><span style="color: #34C759;">Mind</span> AI
            </h1>
            <h2 style="margin-top: 0; color: #4A5568; font-size: 1.5rem; font-weight: 500;">Transforming Healthcare with Artificial Intelligence</h2>
            <p>Experience the future of healthcare with our AI-powered platform. Get instant insights from patient reports, manage hospital operations efficiently, and access reliable medical information with ease.</p>
            <div style="display: flex; justify-content: center; gap: 15px;">
                <a class="btn" href="#diagnostics">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
                        <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                    </svg>
                    Start Diagnosis
                </a>
                <a class="btn btn-outline" href="#search">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    Search Medical Info
                </a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Create two columns for main content
col1, col2 = st.columns([2, 1])

with col1:
    # Diagnostics Section
    st.markdown(
        """
        <div class="card" id="diagnostics">
            <div class="section-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2D8CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                </svg>
                <h2 style="margin: 0 0 0 10px;">Upload Patient Reports</h2>
            </div>
            <p>Simply upload your medical reports and our AI will analyze them for insights and recommendations.</p>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_file = st.file_uploader("Drag and drop your patient report (PDF)", type="pdf", key="pdf")
    
    if uploaded_file:
        st.markdown(
            """
            <div class="success-message">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#34C759" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Report uploaded successfully! Processing your document...
            </div>
            
            <div style="margin-top: 20px;">
                <h3 style="color: var(--text-dark); font-size: 1.2rem; font-weight: 600;">AI Analysis:</h3>
                <div style="background-color: white; padding: 15px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <p style="color: var(--text-dark); margin: 0;">
                        <span style="color: var(--primary); font-weight: 500;">Key Findings:</span><br>
                        • Blood pressure: 120/80 mmHg (Normal)<br>
                        • Glucose levels: 5.4 mmol/L (Normal)<br>
                        • Cholesterol: 5.2 mmol/L (Borderline high)<br>
                        <br>
                        <span style="color: var(--primary); font-weight: 500;">Recommendations:</span><br>
                        • Follow-up in 6 months<br>
                        • Consider lifestyle modifications to address cholesterol
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Hospital Operations Section
    st.markdown(
        """
        <div class="card" id="operations">
            <div class="section-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2D8CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                    <line x1="8" y1="21" x2="16" y2="21"></line>
                    <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
                <h2 style="margin: 0 0 0 10px;">Hospital Operations</h2>
            </div>
            <p>Upload hospital data for AI-powered insights on resource allocation, patient flow, and more.</p>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_excel = st.file_uploader("Upload hospital data (Excel)", type=["xls", "xlsx"], key="excel")
    
    if uploaded_excel:
        st.markdown(
            """
            <div class="success-message">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#34C759" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Hospital data uploaded successfully! Analyzing data...
            </div>
            
            <div style="margin-top: 20px;">
                <h3 style="color: var(--text-dark); font-size: 1.2rem; font-weight: 600;">Operational Insights:</h3>
                <div style="background-color: white; padding: 15px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <p style="color: var(--text-dark); margin: 0;">
                        <span style="color: var(--primary); font-weight: 500;">Key Metrics:</span><br>
                        • Average wait time: 27 minutes<br>
                        • Bed utilization: 78%<br>
                        • Staff efficiency: 85%<br>
                        <br>
                        <span style="color: var(--primary); font-weight: 500;">Recommendations:</span><br>
                        • Optimize staffing during peak hours (10am-2pm)<br>
                        • Implement streamlined intake process
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Search Medical Information Section
    st.markdown(
        """
        <div class="card" id="search">
            <div class="section-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2D8CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <h2 style="margin: 0 0 0 10px;">Medical Information</h2>
            </div>
            <p>Search for reliable information about medical conditions, treatments, and procedures.</p>
        """,
        unsafe_allow_html=True
    )
    
    search_query = st.text_input("Search medical topics", placeholder="e.g., diabetes, hypertension", key="search")
    
    search_button = st.button("Search", key="search_button")
    
    if search_query and search_button:
        st.markdown(
            f"""
            <div style="margin-top: 20px;">
                <h3 style="color: var(--text-dark); font-size: 1.2rem; font-weight: 600;">Results for "{search_query}":</h3>
                <div style="background-color: white; padding: 15px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 15px;">
                    <h4 style="color: var(--primary); margin-top: 0; font-size: 1rem;">Overview</h4>
                    <p style="color: var(--text-dark); margin: 0;">Information about {search_query} would appear here, sourced from medical databases and literature...</p>
                </div>
                
                <div style="background-color: white; padding: 15px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <h4 style="color: var(--primary); margin-top: 0; font-size: 1rem;">Related Topics</h4>
                    <p style="color: var(--text-dark); margin: 0;">
                        • Topic 1<br>
                        • Topic 2<br>
                        • Topic 3
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Quick Contact
    st.markdown(
        """
        <div class="card" id="contact">
            <div class="section-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2D8CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
                <h2 style="margin: 0 0 0 10px;">Contact Us - </h2>
                <h4>9823123139</h4>
            </div><p>Have questions? Reach out to our support team for assistance.</p>
             
        """,
        unsafe_allow_html=True
    )
footer()