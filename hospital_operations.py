import streamlit as st
from datetime import datetime
from navbar import navbar
from footer import footer
# Page configuration
st.set_page_config(
    page_title="MediMind - Patient Information",
    page_icon="🏥",
    layout="wide"
)

# Import styles and components from your existing files
def load_styles():
    # Custom CSS for a modern, clean healthcare UI
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');
            
            :root {
                --primary: #2D8CFF;
                --primary-light: #E6F1FF;
                --secondary: #34C759;
                --text-dark: #2D3748;
                --text-light: #718096;
                --bg-light: #F7FAFC;
                --bg-white: #FFFFFF;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            }
            
            /* Base Styling */
            .stApp {
                background-color: var(--bg-light);
                font-family: 'Poppins', sans-serif;
            }
            
            h1, h2, h3, h4, h5 {
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
            }
            
            p {
                font-family: 'Poppins', sans-serif;
                color: var(--text-light);
                line-height: 1.6;
            }
            
            /* Navbar Styling */
            .navbar {
                background-color: var(--bg-white);
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: var(--shadow);
                border-radius: 12px;
                margin-bottom: 20px;
                position: relative;
                z-index: 100;
            }
            
            .navbar-links {
                display: flex;
                align-items: center;
            }
            
            .navbar a {
                text-decoration: none;
                margin: 0 15px;
                color: var(--text-dark);
                font-weight: 500;
                font-size: 16px;
                transition: 0.3s;
                padding: 8px 15px;
                border-radius: 6px;
            }
            
            .navbar a:hover {
                background-color: var(--primary-light);
                color: var(--primary);
            }
            
            /* Branding */
            .brand {
                font-size: 24px;
                font-weight: 700;
                font-family: 'Montserrat', sans-serif; 
                color: var(--primary);
                display: flex;
                align-items: center;
            }
            
            /* Form Elements */
            .stTextInput > div > div > input {
                border-radius: 8px !important;
                padding: 10px 15px !important; 
                border: 1px solid #E2E8F0 !important;
            }
            
            .stTextInput > div > div > input:focus {
                border-color: var(--primary) !important;
                box-shadow: 0 0 0 2px rgba(45, 140, 255, 0.2) !important;
            }
            
            button {
                border-radius: 8px !important;
                padding: 10px 20px !important;
                background-color: var(--primary) !important;
                color: white !important;
                font-weight: 500 !important;
            }
            
            /* Form sections */
            .form-section {
                background-color: var(--bg-white);
                border-radius: 12px;
                padding: 25px;
                margin-bottom: 20px;
                box-shadow: var(--shadow);
                transition: transform 0.3s;
            }
            
            .form-section:hover {
                transform: translateY(-3px);
            }
            
            .section-title {
                color: var(--primary);
                font-weight: 600;
                font-size: 18px;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                font-family: 'Montserrat', sans-serif;
            }
            
            .section-icon {
                margin-right: 10px;
                color: var(--primary);
            }
            
            /* Privacy Notice */
            .privacy-notice {
                background-color: var(--primary-light);
                border-left: 4px solid var(--primary);
                padding: 15px;
                border-radius: 4px;
                margin: 15px 0;
                font-size: 14px;
                color:var(--text-light);
            }
            
            /* Footer */
            .footer {
                text-align: center;
                padding: 20px;
                background-color: var(--bg-white);
                color: var(--text-light);
                border-radius: 12px;
                box-shadow: var(--shadow);
                margin-top: 30px;
            }
            
            /* Responsive adjustments */
            @media (max-width: 768px) {
                .navbar {
                    flex-direction: column;
                    text-align: center;
                }
                
                .navbar-links {
                    margin-top: 15px;
                    flex-wrap: wrap;
                    justify-content: center;
                }
                
                .navbar a {
                    margin: 5px;
                }
            }
            
            /* Custom Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: #f1f1f1;
            }
            
            ::-webkit-scrollbar-thumb {
                background: #d1d5db;
                border-radius: 4px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: #a0aec0;
            }
            
            /* Main content container */
            .main-content {
                padding: 0 20px;
                max-width: 1200px;
                margin: 0 auto;
            }
            
            /* Form header */
            .form-header {
                background-color: var(--bg-white);
                border-radius: 12px;
                padding: 25px;
                margin-bottom: 20px;
                box-shadow: var(--shadow);
                border-left: 4px solid var(--primary);
            }
            
            /* Buttons */
            .btn {
                background-color: var(--primary);
                color: white !important;
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none !important;
                font-size: 16px;
                font-weight: 600;
                box-shadow: 0 4px 6px rgba(45, 140, 255, 0.2);
                transition: 0.3s;
                display: inline-block;
                border: none;
                width: 100%;
                text-align: center;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(45, 140, 255, 0.25);
            }
            
            .btn-outline {
                background-color: transparent;
                color: var(--primary) !important;
                border: 2px solid var(--primary);
            }
            
            .btn-outline:hover {
                background-color: var(--primary-light);
            }
            
            /* Streamlit default padding adjustment */
            .block-container {
                padding-top: 2rem !important;
                padding-bottom: 2rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


# Load the custom styles
load_styles()

# Load the navbar
navbar()

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Form header
st.markdown(
    """
    <div class="form-header">
        <h2 style="color: var(--primary); margin: 0;">Patient Information Form</h2>
        <p style="margin: 8px 0 0 0;">Please fill out the patient details accurately for better care and diagnosis.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Basic Information Section
st.markdown(
    """
    <div class="form-section">
        <div class="section-title">
            <span class="section-icon">👤</span> Basic Information
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("Patient Name", placeholder="Enter full name")
    patient_id = st.text_input("Patient ID", placeholder="Enter patient ID")

with col2:
    doctor_name = st.text_input("Doctor's Name", placeholder="Enter doctor's name")
    dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime.now())

st.markdown('</div>', unsafe_allow_html=True)  # Close form section

# Contact Information Section
st.markdown(
    """
    <div class="form-section">
        <div class="section-title">
            <span class="section-icon">📱</span> Contact Information
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    phone = st.text_input("Phone Number", placeholder="Enter phone number")
    address = st.text_area("Address", placeholder="Enter current address", height=100)

with col2:
    email = st.text_input("Email Address", placeholder="Enter email address")
    emergency_contact = st.text_input("Emergency Contact", placeholder="Name and phone number")

st.markdown('</div>', unsafe_allow_html=True)  # Close form section

# Medical Information Section
st.markdown(
    """
    <div class="form-section">
        <div class="section-title">
            <span class="section-icon">🏥</span> Medical Information
        </div>
    """,
    unsafe_allow_html=True
)

symptoms = st.text_area("Current Symptoms", placeholder="Describe current symptoms", height=100)
allergies = st.text_area("Allergies", placeholder="List any known allergies", height=100)
medications = st.text_area("Current Medications", placeholder="List current medications and dosages", height=100)
medical_history = st.text_area("Medical History", placeholder="Relevant medical history", height=100)

st.markdown('</div>', unsafe_allow_html=True)  # Close form section

# Insurance Information Section
st.markdown(
    """
    <div class="form-section">
        <div class="section-title">
            <span class="section-icon">📋</span> Insurance Information
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    insurance_provider = st.text_input("Insurance Provider", placeholder="Enter provider name")
    policy_number = st.text_input("Policy Number", placeholder="Enter policy number")

with col2:
    group_number = st.text_input("Group Number", placeholder="Enter group number")
    insurance_phone = st.text_input("Insurance Phone", placeholder="Enter contact number")

st.markdown('</div>', unsafe_allow_html=True)  # Close form section

# Buttons
st.markdown('<div class="form-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<a href="#" class="btn btn-outline">Clear Form</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="#" class="btn">Submit Patient Data</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close form section

# Privacy Information Box
st.markdown(
    """
    <div class="privacy-notice">
        <strong>Privacy Notice:</strong> All patient data is securely stored and protected according to HIPAA guidelines. 
        Your information is only accessible to authorized healthcare providers. We prioritize patient confidentiality and data security.
    </div>
    """,
    unsafe_allow_html=True
)

# Close main content container
st.markdown('</div>', unsafe_allow_html=True)

# Load the footer
footer()