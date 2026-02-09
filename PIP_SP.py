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
with col2:
    st.header("Outer Pipe")
    OD_OP = st.number_input("Outer Pipe Outer Diameter, OD_OP (mm)", value=406.4, min_value=0.0, step=1.0, format="%.2f")
    WT_OP = st.number_input("Outer Pipe Wall Thickness, WT_OP (mm)", value=17.5, min_value=0.0, step=1.0, format="%.2f")
    AC_CT_OP = st.number_input("Anti-Corrosion Coating Thickness, AC_CT_OP (mm)", value=2.5, min_value=0.0, step=1.0, format="%.2f")
with col3:
    st.header("Centraliser")
    CT = st.number_input("Centraliser Thickness, CT (mm)", value=40.0, min_value=0.0, step=1.0, format="%.2f")
    CL = st.number_input("Centraliser Length, CL (mm)", value=50.0, min_value=0.0, step=1.0, format="%.2f")
    CS = st.number_input("Centraliser Spacing, CS (mm)", value=2160.0, min_value=0.0, step=1.0, format="%.2f")
# Geomtric Properties Calculation
ID_IP = float(OD_IP) - 2 * WT_IP
ID_OP = float(OD_OP) - 2 * WT_OP
OD_overall = float(OD_OP) + 2 * AC_CT_OP
A_in = math.pi / 4 * (OD_IP**2 - ID_IP**2)
A_out = math.pi / 4 * (OD_OP**2 - ID_OP**2)
A_steel = A_in + A_out
A_ins = math.pi / 4 * ( (OD_IP + 2 * IT)**2 - OD_IP**2)
A_corr = math.pi / 4 * (OD_overall**2 - OD_OP**2)
A_fluid = math.pi / 4 * ID_IP**2
st.write(f"**Inner Pipe Inner Diameter, ID_IP (mm):** {ID_IP:.2f}")
st.write(f"**Outer Pipe Inner Diameter, ID_OP (mm):** {ID_OP:.2f}")
st.write(f"**Overall Outer Diameter, OD_overall (mm):** {OD_overall:.2f}")
st.write(f"**Inner Pipe Cross-sectional Area, A_in (mm²):** {A_in:.6f}")
st.write(f"**Outer Pipe Cross-sectional Area, A_out (mm²):** {A_out:.6f}")
st.write(f"**Steel Cross-sectional Area, A_steel (mm²):** {A_steel:.6f}")
st.write(f"**Insulation Cross-sectional Area, A_ins (mm²):** {A_ins:.6f}")
st.write(f"**Anti-Corrosion Coating Cross-sectional Area, A_corr (mm²):** {A_corr:.6f}")
st.write(f"**Fluid Cross-sectional Area, A_fluid (mm²):** {A_fluid:.6f}")

st.title("Material Properties")
col1, col2 = st.columns(2)
with col1:
    st.header("Inner Pipe")
    E_IP = st.number_input("Inner Pipe Young's Modulus, E_IP (GPa)", value=200.0, min_value=0.0, step=0.1, format="%.2f")
    nu_IP = st.number_input("Inner Pipe Poisson Ratio, nu_IP (-)", value=0.3, min_value=0.0, step=0.1, format="%.2f")
    a_IP = st.number_input("Inner Pipe Thermal Expansion Coefficient, a_IP (10^-5/°C)", value=1.100, min_value=0.0, step=.001, format="%.3f")
    
with col2:
    st.header("Outer Pipe")
    E_OP = st.number_input("Outer Pipe Young's Modulus, E_OP (GPa)", value=207.0, min_value=0.0, step=0.1, format="%.2f")
    nu_OP = st.number_input("Outer Pipe Poisson Ratio, nu_OP (-)", value=0.3, min_value=0.0, step=0.1, format="%.2f")
    a_OP = st.number_input("Outer Pipe Thermal Expansion Coefficient, a_OP (10^-5/°C)", value=1.170, min_value=0.0, step=.001, format="%.3f")

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

st.title("Temperature")
col1, col2 = st.columns(2)
with col1:
    T_IP = st.number_input("Inner Pipe Temperature, T_IP (°C)", value=112.0, min_value=0.0, step=0.1, format="%.2f")
    Ta_min = st.number_input("Minimum Ambient Temperature, Ta_min (°C)", value=4.0, min_value=0.0, step=0.1, format="%.2f")
   
with col2:
    T_OP = st.number_input("Outer Pipe Temperature, T_OP (°C)", value=47.5, min_value=0.0, step=0.1, format="%.2f")
    Ta_max = st.number_input("Maximum Ambient Temperature, Ta_max (°C)", value=10.0, min_value=0.0, step=0.1, format="%.2f")

st.title("Pressure and Load")
col1, col2 = st.columns(2)
with col1:
    P_IP_as_laid = st.number_input("Inner Pipe Pressure- As Laid, P_IP_as_laid (MPa)", value=0.0, min_value=0.0, step=0.1, format="%.2f")
    P_IP_oper = st.number_input("Inner Pipe Pressure- Operation, P_IP_oper (MPa)", value=32.5, min_value=0.0, step=0.1, format="%.2f")
    P_IP_st = st.number_input("Inner Pipe Pressure- System Test, P_IP_st (MPa)", value=37.38, min_value=0.0, step=0.1, format="%.2f")
    P_OP_ap = st.number_input("Outer Pipe Annulus Pressure, P_OP_ap (MPa)", value=0.0, min_value=0.0, step=0.1, format="%.2f")
   
with col2:
    h_ref = st.number_input("Reference Elevation, h_ref (m)", value=40.0, min_value=0.0, step=0.1, format="%.2f")
    H_in = st.number_input("Inner Pipe Residual Tension, H_in (kN)", value=0.0, min_value=0.0, step=0.1, format="%.2f")
    H_out = st.number_input("Outer Pipe Residual Tension, H_out (kN)", value=0.0, min_value=0.0, step=0.1, format="%.2f")

st.title("Equivanet Single Pipe Parameters")
col1, col2 = st.columns(2)
with col1:
    E_eq = st.number_input("Equivalent Young's Modulus, E_eq (GPa)", value=207.0, min_value=0.0, step=0.1, format="%.2f")
    nu_eq = st.number_input("Equivalent Poisson Ratio, nu_eq (-)", value=0.3, min_value=0.0, step=0.1, format="%.2f")
    a_eq = st.number_input("Equivalent Thermal Expansion Coefficient, a_eq (10^-5/°C)", value=1.170, min_value=0.0, step=.001, format="%.3f")
   
with col2:
    H_eq = st.number_input("Equivalent Residual Tension, H_eq (kN)", value=0.0, min_value=0.0, step=0.1, format="%.2f")
    P_eq_oper = st.number_input("Equivalent Pressure- Operation, P_eq_oper (MPa)", value=28.9, min_value=0.0, step=0.1, format="%.2f")
    P_eq_st = st.number_input("Equivalent Pressure- System Test, P_eq_st (MPa)", value=33.24, min_value=0.0, step=0.1, format="%.2f")

