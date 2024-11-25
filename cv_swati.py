#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
import re
import requests
#---------------------------------------------------------------------------------------------------------------------------------
### Custom Graphics
#---------------------------------------------------------------------------------------------------------------------------------
button_css = """
<style>
    .download-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: #ffffff;
        background-color: #4CAF50;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .download-button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }

    .download-button:active {
        background-color: #3e8e41;
        transform: translateY(0);
    }
</style>
"""
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Resume | Swati Banerjee",
                   layout="wide",
                   page_icon= "📑",              
                   initial_sidebar_state="collapsed")
#----------------------------------------
st.title(f""":blue[Swati Banerjee]""")
#----------------------------------------
col1, col2 = st.columns((0.92,0.08))
with col1:
    st.info('**Manager | Competent analytics and engineering professional offering 8+ years’ experience in predictive modelling, data science, machine learning, deep learning, generative AI and project & people management.**')
with col2:
    with st.popover("**:blue[:pushpin: Contact]**", help="click to get contact details"): 
            st.markdown('**Mobile : (91) 98742 13287 | Email : <a href="mailto:swati.banerjee008@gmail.com">swati.banerjee008@gmail.com</a>**', 
            unsafe_allow_html=True)  
#----------------------------------------
# Set the background image
st.divider()

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

  
#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["**Competencies**","**Skills**","**Work Experience**","**Education**","**Certification**", "**Projects**","**Resume**", "**Connect**"])

#---------------------------------------------------------------------------------------------------------------------------------
### Competencies
#---------------------------------------------------------------------------------------------------------------------------------

with tab1:

    st.markdown('''
            
            - Strong knowledge of statistical, data science, machine learning (ML), deep learning, NLP (understanding & generation) & Generative AI.
            - Cross functional work experience and collaborated with stakeholders, identifying and gathering analytical requirements for customer, product and project’s needs.
            - Leveraged analytics to drive business development, productivity and process improvement and marketing strategies. 
            - Expertise in feature engineering and end-to-end model lifecycle (development, deployment & validation).
            - Works on collection optimization, customer propensity models (cross-up sell, acquisition, segmentation, CLV, retention, win backs and monetization), pricing & promotion & sales spend optimization, recommendation systems, market-mix-modelling.             
            - Knowledge on requirement gathering – projects & contracts management (agile), design, development, risk analysis and implementation and people management – experience of handing team member. 
            
            ''')
    
    st.divider()

    st.markdown('''
            
            - Cross domain work experience **CPG, Energy, Utilities, Logistics, Retail, Supply chain (operations)**.
         
            ''')

#---------------------------------------------------------------------------------------------------------------------------------
### Skills
#---------------------------------------------------------------------------------------------------------------------------------

with tab2:
        
    st.markdown('''
            
            **Languages**:
                
            - Python
            - R
            - SQL
            - VBA 
            
            ''')
    
    st.divider()    

    st.markdown('''
            
            **Software**:
                
            - SAS 
            - MS Office 
            - MS Projects 
            - STAAD Pro V8i 
            - Power BI 
            - Alteryx 
            - Docker
            
            ''')
    
    st.divider()  
    
    st.markdown('''
            
            **Cloud Module**:
                
            - AWS 
            - Azure Machine Learning
            
            ''')

#---------------------------------------------------------------------------------------------------------------------------------
### Work Experience
#---------------------------------------------------------------------------------------------------------------------------------

with tab3:
     
        st.markdown('''
            
            **Clariant | Data Scintist (Manager) | Mumbai(India) | Oct'21 -**
                
            - Works as a part of Global team of **'Competence Centre - Data Science'** which analyses and generate data-driven strategies to improve growth of different business unit (BU). 
            - Working of energy & production optimization ML Model based on the sensor data and create front-end API.
            - Working as a part for the project to develop customer lifecycle management model for BUs to prepare data-driven customised solutions for diverse needs and analyse the model risk management & validation.
            - Worked on ‘demand forecasting’ and ‘inventory optimization’ for a supply chain process and logistics improvements and price-promotion and sales spend optimization for our ‘Global Business Services (GBS)’.
            - Create dashboard based on data-driven analytics and generate insights based on it. 
            - Developed ‘Streamlit app’ of different ‘Generative AI & LLM’ use cases foe different BU’s.
            
            ''')
        
        st.divider()

        st.markdown('''
            
            **Thyssenkrupp | Assistant Manager | Mumbai(India) | Nov'19 - Sep'21**
                
            - Works as part of “Data Analytics as a Service” to generate continuously refined algorithms to optimize the process. 
            - Worked end to end (data extraction, data cleaning, model development & validation) on multiple projects of collection optimization using different classification techniques.
            - Customer's database is used as inputs for the model data, selected significant variables and give the predicted score using logistic regression or another statistical technique which is given more accuracy and also doing monthly rollout. Define the
                different business strategies and treatment strategies to the customers that optimize the desired output and monitoring the model every 4 months’ basis.
            - Find trend and seasonality patterns in process development and detect to derive optimum solutions and forecast future pattern using time series forecasting (ARIMA &ARIMAX).
            - Create dashboard based on data-driven analytics and generate insights based on it. 
            - Prepare the dashboard through visual analytics to represent the solutions of the business problems and generate the meaningful insights.
            
            ''')

        st.divider()

        st.markdown('''
            
            **Jacobs | Senior Engineer | Mumbai(India) | Oct'17 - Nov'19**
                
            - Identify the churn and non-churn customer base as probability basic for process using logistic classification techniques. 
            - Analyse the overall satisfaction level amongst the customers to identify the most significant parameters regarding IT and tech support services every quarter basis using multiple linear regression modelling to identify and provide business report
                to work on their strategy.
            
            ''')  

        st.divider()

        st.markdown('''
            
            **Tebodin | Discipline Engineer | Mumbai(India) | Oct'15 - Apr'17**
                
            - Implement decisive approaches to solve operations problems by identifying significant parameters.
            - Simulate many scenarios of complex pattern recognitions to overcome the skcepticism in the area and leverage precisely the potentials to remain operational improvements.
            
            ''')  
        
        st.divider()

        st.markdown('''
            
            **GS E&C | Engineer | Gurgaon(India) | Mar'14 - Feb'15**
                
            - Design, analysis & develop different 3D model of the industrial structures in petrochemical plants.
            - Supervise the drafting procedures of designed structures.
            - Resolving the client comments and review the 3d model as per projects and industry standards.                    
            
            ''') 

        st.divider()

        st.markdown('''
            
            **Mott Macdonald | Design Engineer | Kolkata & Mumbai(India),Muscat(Oman) | Nov'10 - Feb'14**
                
            - Design, analysis & develop different 3D model of the industrial structures in petrochemical plants.
            - Supervise the drafting procedures of designed structures.
            - Resolving the client comments and review the 3d model as per projects and industry standards.                    
            - Bill of Quantities preparation & up dation.      
                             
            ''')    

        st.divider()

        st.markdown('''
            
            **Maknan Consultancy | Assistant Engineer | Kolkata(India) | Aug'08 - Nov'10**
                
            - Design, analysis & develop different 3D model of the industrial structures in petrochemical plants.
            - Supervise the drafting procedures of designed structures.                 
            - Bill of Quantities preparation & up dation.      
                             
            ''')
                   
#---------------------------------------------------------------------------------------------------------------------------------
### Education
#---------------------------------------------------------------------------------------------------------------------------------

with tab4:

    # Define the columns
    col1, col2, col3, col4 = st.columns(4)

    # Define the container style
    container_style = """
    <style>
    .education-container {
        padding: 15px;
        background-color: #fdfefe;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
        text-align: center;
    }
    .education-container:hover {
        background-color: #e0e0e0;
    }
    .education-container p {
        margin: 5px 0;
        font-weight: bold;
        color: #333;
    }
    .education-button {
        margin-top: 10px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #d0d3d4;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
    }
    .education-button:hover {
        background-color: #d0d3d3;
    }
    </style>
    """

    st.markdown(container_style, unsafe_allow_html=True)

    # Education 1
    with col1:
        st.markdown(
            """
            <div class="education-container">
                <p>Master of Science (MSc.) in Data Science (Pursuing)</p>
                <p>Vellore Institute of Technology | 2024 -</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Education 2
    with col2:
        st.markdown(
            """
            <div class="education-container">
                <p>PGP (Data Science & Business Analytics)</p>
                <p>University of Texas at Austin | 2020 - 2021</p>
                <a href="https://drive.google.com/file/d/1hNrlSPT6ROe651BRu_9HSoR6JRlwuwKS/view?usp=sharing" target="_blank" class="education-button">
                    Click to view certificate
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Education 3
    with col3:
        st.markdown(
            """
            <div class="education-container">
                <p>PGDM (Operations)</p>
                <p>Welingkar Institute of Management | 2018 - 2020</p>
                <a href="https://drive.google.com/file/d/1RofIodKzxFugg27evYMZOgz9rPPZFUdT/view?usp=sharing" target="_blank" class="education-button">
                    Click to view certificate
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Education 4
    with col4:
        st.markdown(
            """
            <div class="education-container">
                <p>Bachelor of Technology (B. Tech)</p>
                <p>Jalpaiguri Govt. Engg College | 2004 - 2008</p>
                <a href="https://drive.google.com/file/d/1DB01GNXPUC48ja0JyhOPoshZ-NAYsG1u/view?usp=sharing" target="_blank" class="education-button">
                    Click to view certificate
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )


#---------------------------------------------------------------------------------------------------------------------------------
### Certification
#---------------------------------------------------------------------------------------------------------------------------------

with tab5:

    # Define the columns
    col1, col2, col3, col4 = st.columns(4)

    # Define the container style
    container_style = """
    <style>
    .certificate-container {
        padding: 20px;
        background-color: #fdfefe;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
        text-align: center;
    }
    .certificate-container:hover {
        background-color: #e0e0e0;
    }
    .certificate-container p {
        margin: 5px 0;
        font-weight: bold;
        color: #333;
    }
    .certificate-button {
        margin-top: 10px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #d0d3d4;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
    }
    .certificate-button:hover {
        background-color: #d0d3d3;
    }
    </style>
    """

    st.markdown(container_style, unsafe_allow_html=True)

    # Certificate 1
    with col1:
        st.markdown(
            """
            <div class="certificate-container">
                <p>Scrum Product Owner (CSPO) (Scrum Alliance)</p>
                <p>Member ID: 001366732</p>
                <a href="https://drive.google.com/file/d/1XTCj-rcFVx8mgOcM4kiTid_uIkb6nDXc/view?usp=sharing" target="_blank" class="certificate-button">
                    Click to view certificate
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Certificate 2
    with col2:
        st.markdown(
            """
            <div class="certificate-container">
                <p>Financial Modelling Valuation & Risk Analysis</p>
                <p>The Wall Street School</p>
                <a href="https://drive.google.com/file/d/1pX-8CSQwMIA6Qthz6DFD_V1oQMXwrUs2/view?usp=sharing" target="_blank" class="certificate-button">
                    Click to view certificate
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

#---------------------------------------------------------------------------------------------------------------------------------
### Projects
#---------------------------------------------------------------------------------------------------------------------------------

with tab6:
     
    projects = [
        {
            "name": "1. Knowledge DataBase", 
            "url": "https://dl-kdb.streamlit.app/",
            "description": "A comprehensive database for storing and accessing knowledge, with advanced search and categorization features."
        },
        {
            "name": "2. Machine Learning CookBook", 
            "url": "https://machine-learning-cookbook.streamlit.app/",
            "description": "A collection of machine learning recipes and code snippets to help you solve common ML tasks quickly."
        },        
        {
            "name": "3. Machine Learning (ML) Studio", 
            "url": "https://ml-studio.streamlit.app/",
            "description": "An interactive platform for experimenting with various machine learning models and algorithms."
        },
        {
            "name": "4. Forecasting App", 
            "url": "https://ts-app.streamlit.app/",
            "description": "A tool for time series forecasting, helping you predict future trends based on historical data."
        },   
        {
            "name": "5. Anomaly Detection App", 
            "url": "https://anomaly-det.streamlit.app/",
            "description": "An app designed to detect anomalies in datasets, useful for identifying outliers and unusual patterns."
        },          
        {
            "name": "6. Digi-e | Generative AI Playground", 
            "url": "https://genai-playground.streamlit.app/",
            "description": "A playground for experimenting with generative AI models, allowing you to create text, images, and more."
        },
        {
            "name": "7. PDF Playground", 
            "url": "https://pdf-playground.streamlit.app/",
            "description": "An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs."
        },    
        {
            "name": "8. Image Playground", 
            "url": "https://image-playground.streamlit.app/",
            "description": "A lightweight image-processing streamlit app that supports the following operations: upload image,crop,remove background,mirror,convert,rotate,change brightness."
        },   
        {
            "name": "9. ML Code Generator", 
            "url": "https://ml-code-gen.streamlit.app/",
            "description": "An easy-to-use, open-source application to generate python codes for machine learning algorithms."
        }      
    ]

    #st.write("Click on a project name to navigate to the specific path:")

    container_style = """
    <style>
    .project-container {
        padding: 10px;
        background-color: #fdfefe;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
        text-align: center;
    }
    .project-container:hover {
        background-color: #e0e0e0;
    }
    .project-container a {
        text-decoration: none;
        font-weight: bold;
        color: #0073e6;
    }
    .project-container a:hover {
        color: #005bb5;
    }
    .project-description {
        font-size: 0.9em;
        color: #555;
        margin-top: 5px;
    }
    </style>
    """

    st.markdown(container_style, unsafe_allow_html=True)

    # Create columns
    cols = st.columns(4)

    # Place each project in the columns with descriptions
    for i, project in enumerate(projects):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="project-container">
                    <a href="{project['url']}" target="_blank">{project['name']}</a>
                    <p class="project-description">{project['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

#---------------------------------------------------------------------------------------------------------------------------------
### Resume
#---------------------------------------------------------------------------------------------------------------------------------

with tab7:
    
    with st.container(height=750,border=True):

        file_name = "Resume" 
        file_id = "1fJ6PrVQHZUmfDdBsrJeFVVZ4E_L6MAp6"
        download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
        pdf_view_link = f"https://drive.google.com/file/d/{file_id}/preview"

        st.markdown(f"""
            <iframe src="{pdf_view_link}" width="100%" height="600px">
            #<iframe src="{pdf_view_link}" width="100%" height="1000px" style="border:none;">
            </iframe>
            """, unsafe_allow_html=True)

    st.markdown(f"""
                <a href="{download_link}" download>
                <button style="padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px; cursor:pointer;">
                Click to download {file_name}
                </button>
                </a>
                """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Contacts
#---------------------------------------------------------------------------------------------------------------------------------

with tab8:

    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfrti0KgrA-iljS2TU45Lqd092iy8Ldgpp3o8rqGHdaaxRtiQ/viewform?embedded=true"
    #st.markdown("Please fill out the form below to get in touch with me:")

    st.markdown(f"""
        <iframe src="{form_url}" width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        """, unsafe_allow_html=True)
