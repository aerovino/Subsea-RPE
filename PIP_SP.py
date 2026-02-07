import math
import pandas as pd
import streamlit as st

st.set_page_config(page_title="PIP to Single Pipe - Calculator", page_icon="Icon.png", layout="wide")

st.title("PIP to Single Pipe - Calculator")

st.title("PIP - Geometric Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Inner Pipe")
    OD_IP = st.number_input("Inner Pipe Outer Diameter, OD_IP (mm)", value=273.1, min_value=0.0, step=1.0, format="%.2f")
    WT_IP = st.number_input("Inner Pipe Wall Thickness, WT_IP (mm)", value=14.3, min_value=0.0, step=1.0, format="%.2f")
    IT = st.number_input("Insulation Thickness, IT (mm)", value=20.0, min_value=0.0, step=1.0, format="%.2f")
    ID_IP = float(OD_IP) - 2 * WT_IP
with col2:
    st.header("Outer Pipe")
    OD_OP = st.number_input("Outer Pipe Outer Diameter, OD_OP (mm)", value=406.4, min_value=0.0, step=1.0, format="%.2f")
    WT_OP = st.number_input("Outer Pipe Wall Thickness, WT_OP (mm)", value=17.5, min_value=0.0, step=1.0, format="%.2f")
    AC_CT_OP = st.number_input("Anti-Corrosion Coating Thickness, AC_CT_OP (mm)", value=2.5, min_value=0.0, step=1.0, format="%.2f")
    ID_OP = float(OD_OP) - 2 * WT_OP
with col3:
    st.header("Centraliser")
    CT = st.number_input("Centraliser Thickness, CT (mm)", value=40.0, min_value=0.0, step=1.0, format="%.2f")
    CL = st.number_input("Centraliser Length, CL (mm)", value=50.0, min_value=0.0, step=1.0, format="%.2f")
    CS = st.number_input("Centraliser Spacing, CS (mm)", value=2160.0, min_value=0.0, step=1.0, format="%.2f")

st.title("Material Properties")

col1, col2 = st.columns(2)
with col1:
    st.header("Inner Pipe")
    E_IP = st.number_input("Inner Pipe Young's Modulus, E_IP (GPa)", value=200.0, min_value=0.0, step=0.1, format="%.2f")
    nu_IP = st.number_input("Inner Pipe Poisson Ratio, nu_IP (-)", value=0.3, min_value=0.0, step=0.1, format="%.2f")
    a_IP = st.number_input("Inner Pipe Thermal Expansion Coefficient, a_IP (10^-5/C)", value=1.100, min_value=0.0, step=.001, format="%.3f")
    
with col2:
    st.header("Outer Pipe")
    E_OP = st.number_input("Outer Pipe Young's Modulus, E_OP (GPa)", value=207.0, min_value=0.0, step=0.1, format="%.2f")
    nu_OP = st.number_input("Outer Pipe Poisson Ratio, nu_OP (-)", value=0.3, min_value=0.0, step=0.1, format="%.2f")
    a_OP = st.number_input("Outer Pipe Thermal Expansion Coefficient, a_OP (10^-5/C)", value=1.170, min_value=0.0, step=.001, format="%.3f")


st.title("Density Parameters")
col1, col2 = st.columns(2)
with col1:
    SD_IP = st.number_input("Inner Pipe Steel Density, SD_IP (kg/m³)", value=7850.0, min_value=0.0, step=1.0, format="%.2f")
    CD_IP = st.number_input("Inner Pipe Content Density, CD_IP (kg/m³)", value=835.0, min_value=0.0, step=1.0, format="%.2f")
    ID = st.number_input("Insulation Density, ID (kg/m³)", value=160.0, min_value=0.0, step=1.0, format="%.2f")
   
with col2:
    SD_OP = st.number_input("Outer Pipe Steel Density, SD_OP (kg/m³)", value=7850.0, min_value=0.0, step=1.0, format="%.2f")
    SWD = st.number_input("Sea Water Density, SWD (kg/m³)", value=1025.0, min_value=0.0, step=1.0, format="%.2f")
    CD = st.number_input("Centraliser Density, CD (kg/m³)", value=0.0, min_value=0.0, step=1.0, format="%.2f")