import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="ByteResponse",
    page_icon="🚀",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .hero-title {
        font-size:40px !important;
        font-weight: bold;
        color: #0A84FF;
        text-align: center;
    }
    .section-header {
        font-size:26px !important;
        font-weight: bold;
        margin-top: 30px;
    }
    .normal-font {
        font-size:18px !important;
    }
</style>
""", unsafe_allow_html=True)

# Hero Title
st.markdown('<p class="hero-title">Welcome to ByteResponse</p>', unsafe_allow_html=True)

# Divider
st.divider()

# Company Objective Section
with st.expander("Our Objective"):
    st.markdown(
        '''
        <p class="normal-font">
        At ByteResponse, we specialize in the <b>research, analysis, development, and deployment</b> of cutting-edge SaaS (Software as a Service) products. 
        Our focus is on delivering scalable, innovative, and high-performance solutions that empower businesses to grow, optimize operations, and unlock new opportunities.<br><br>

        Beyond SaaS development, we extend our expertise to <b>custom AI solutions</b>, tailoring intelligent systems to solve complex business challenges. 
        From predictive analytics to process automation, we harness the latest advancements in artificial intelligence to create bespoke solutions that drive measurable results.<br><br>

        Our commitment lies in combining <b>deep research</b>, <b>strategic analysis</b>, and <b>agile development</b> to transform ideas into impactful, market-ready products. 
        We operate at the intersection of technology and innovation — bringing clarity, intelligence, and execution to every project we undertake.
        </p>
        ''', 
        unsafe_allow_html=True
    )

# About Us Section
with st.expander("About Us"):
    st.markdown('<p class="normal-font">At ByteResponse, we are dedicated to pushing innovation through comprehensive research, strategic analysis, seamless development, and scalable deployment of SaaS products. Our passion extends to crafting tailored AI solutions that empower businesses to achieve smarter outcomes.</p>', unsafe_allow_html=True)

# Services Section
with st.expander("Our Services"):
    st.markdown('<p class="normal-font">We offer a suite of services designed to empower businesses and entrepreneurs:</p>', unsafe_allow_html=True)
    st.markdown("""
    - SaaS Product Development
    - AI-Driven Business Solutions
    - Research and Analytical Services
    - Custom AI Consulting
    """)

# Areas of Interest / Survey
with st.expander("Areas of Interest"):
    st.markdown('<p class="normal-font">We are shaping our future products and services based on your needs. Your feedback is invaluable in helping us deliver solutions that matter.</p>', unsafe_allow_html=True)
    st.markdown("""
    👉 [Participate in Our Survey Here](https://tally.so/r/mRjkyd)
    """)

# Contact Section
with st.expander("Contact Us"):
    st.markdown('<p class="normal-font">Feel free to reach out to us!</p>', unsafe_allow_html=True)
    st.markdown("""
    **Email:** [contact@byteresponse.com](mailto:contact@byteresponse.com)
    """)

# Footer
st.markdown("""
---
Made by ByteResponse. All rights reserved.
""")