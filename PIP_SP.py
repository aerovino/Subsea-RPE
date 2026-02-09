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
    PIP_BS_method = st.selectbox("PIP Bending Stiffness Method", ("Sum", "Carrier"), index=0)
with col2:
    SD_OP = st.number_input("Outer Pipe Steel Density, SD_OP (kg/m³)", value=7850.0, min_value=0.0, step=1.0, format="%.2f")
    SWD = st.number_input("Sea Water Density, SWD (kg/m³)", value=1025.0, min_value=0.0, step=1.0, format="%.2f")
    CD = st.number_input("Centraliser Density, CD (kg/m³)", value=0.0, min_value=0.0, step=1.0, format="%.2f")
    D_corr = st.number_input("Anti-Corrosion Coating Density, D_corr (kg/m³)", value=985.0, min_value=0.0, step=1.0, format="%.2f")

# Mass and Weight Calculation
m_steel_IP = A_in * SD_IP / 1e6   
m_steel_OP = A_out * SD_OP / 1e6
m_steel_total = m_steel_IP + m_steel_OP
m_ins = A_ins * ID / 1e6
m_corr = A_corr * D_corr / 1e6
m_centraliser = math.pi / 4 *  ( (OD_IP + 2 * CT )**2 - (OD_IP )**2 ) * CL / CS * CD / 1e6
m_IPC_oper = (A_fluid * CD_IP) / 1e6
m_IPC_SW = (A_fluid * SWD) / 1e6
m_buoyant = math.pi / 4 * OD_overall**2 * SWD / 1e6
m_sub_empty = m_steel_total + m_ins + m_corr + m_centraliser - m_buoyant
m_sub_oper = m_sub_empty + m_IPC_oper
m_sub_SW = m_sub_empty + m_IPC_SW
w_sub_empty = m_sub_empty * 9.81
w_sub_oper = m_sub_oper * 9.81
w_sub_SW = m_sub_SW * 9.81
st.write(f"**Inner Pipe Steel Mass per Unit Length, m_steel_IP (kg  / m):** {m_steel_IP:.2f}")
st.write(f"**Outer Pipe Steel Mass per Unit Length, m_steel_OP (kg  / m):** {m_steel_OP:.2f}")
st.write(f"**Total Steel Mass per Unit Length, m_steel_total (kg  / m):** {m_steel_total:.2f}")
st.write(f"**Insulation Mass per Unit Length, m_ins (kg  / m):** {m_ins:.2f}")
st.write(f"**Anti-Corrosion Coating Mass per Unit Length, m_corr (kg  / m):** {m_corr:.2f}")
st.write(f"**Centraliser Mass per Unit Length, m_centraliser (kg  / m):** {m_centraliser:.2f}")
st.write(f"**Inner Pipe Content Mass per Unit Length- Operation, m_IPC_oper (kg  / m):** {m_IPC_oper:.2f}")
st.write(f"**Inner Pipe Content Mass per Unit Length- Sea Water, m_IPC_SW (kg  / m):** {m_IPC_SW:.2f}")
st.write(f"**Buoyant Mass per Unit Length, m_buoyant (kg  / m):** {m_buoyant:.2f}")
st.write(f"**Submerged mass per Unit Length- Empty, w_sub_empty (kg  / m):** {m_sub_empty:.2f}")
st.write(f"**Submerged mass per Unit Length- Operation, w_sub_oper (kg  / m):** {m_sub_oper:.2f}")
st.write(f"**Submerged mass per Unit Length- Sea Water, w_sub_SW (kg  / m):** {m_sub_SW:.2f}")
st.write(f"**Submerged Weight per Unit Length- Empty, w_sub_empty (N / m):** {w_sub_empty:.2f}")
st.write(f"**Submerged Weight per Unit Length- Operation, w_sub_oper (N / m):** {w_sub_oper:.2f}")
st.write(f"**Submerged Weight per Unit Length- Sea Water, w_sub_SW (N / m):** {w_sub_SW:.2f}")

# Moment of Inertia and Stiffness Calculation
I_IP = (math.pi / 64) * (OD_IP**4 - ID_IP**4)
I_OP = (math.pi / 64) * (OD_OP**4 - ID_OP**4)
I_PIP = I_IP + I_OP
EA_PIP = E_IP * A_in / 1e3 + E_OP * A_out / 1e3
if PIP_BS_method == "Sum":  
    EI_IP = E_IP * I_IP / 1e6  
    EI_OP = E_OP * I_OP / 1e6  
    EI_PIP = EI_IP + EI_OP
else:
    EIy_PIP = E_OP * I_OP / 1e6
st.write(f"**Inner Pipe Moment of Inertia, I_IP (mm⁴):** {I_IP:.2f}")
st.write(f"**Outer Pipe Moment of Inertia, I_OP (mm⁴):** {I_OP:.2f}")
st.write(f"**Total Moment of Inertia, I_PIP (mm⁴):** {I_PIP:.2f}")
st.write(f"**Total Equivalent Bending Stiffness, EI_PIP (kN·m²):** {EI_PIP:.2f}")
st.write(f"**Total Axial Stiffness, EA_PIP (kN):** {EA_PIP:.2f}")

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
