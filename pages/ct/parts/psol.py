import streamlit as st
from pages.ct.fun import table

psol = ['Cu(N₃)₂: 6.3 x 10⁻¹⁰',
        'PbBr₂: 6.3 x 10⁻⁶ ',
        'PtBr₄: 3.2 x 10⁻⁴¹',
        'AgBr: 5.0 x 10⁻¹³',
        'BaCO₃: 5.0 x 10⁻⁹',
        'CaCO₃: 4.5 x 10⁻⁹',
        'CdCO₃: 1.0 x 10⁻⁸',
        'PbCO₃: 1.5 x 10⁻¹³',
        'CoCO₃: 8.0 x 10⁻¹³ ',
        'CuCO₃: 2.5 x 10⁻¹⁰',
        'FeCO₃: 3.5 x 10⁻¹',
        'Li₂CO₃: 2.5 x 10⁻²',
        'MgCO₃: 3.5 x 10⁻⁸',
        'NiCO₃: 6.6 x 10⁻⁹',
        'AgCO₃: 8.1 x 10⁻¹²',
        'ZnCO₃: 1.5 x 10⁻¹',
        'Hg₂(CN)₂: 5.0 x 10⁻⁴⁰',
        'PbCl₂: 1.5 x 10⁻⁵',
        'CuCl: 1.9 x 10⁻⁷',
        'Hg₂Cl₂: 1.1 x 10⁻¹⁸',
        'AuCl: 2.0 x 10⁻¹³',
        'AuCl₃: 3.2 x 10⁻²⁵',
        'AgCl: 1.7 x 10⁻¹⁰',
        'BaCrO₄: 1.2 x 10⁻¹⁰',
        'CaCrO₄: 7.1 x 10⁻⁴',
        'PbCrO₄: 1.8 x 10⁻¹⁴',
        'Ag₂CrO₄: 1.2 x 10⁻¹²',
        'AgCrO₄: 2.4 x 10⁻¹²',
        'PbCl₂: 1.5 x 10⁻⁵',
        'Fe₄(P₂O₇)₃: 2.5 x 10⁻²³',
        'PbI₂: 8.0 x 10⁻⁹',
        'BaF₂: 1.7 x 10⁻⁶',
        'CaF₂: 3.9 x 10⁻¹',
        'PbF₂: 3.7 x 10⁻⁸',
        'LiF: 1,7 x 10⁻³',
        'AlPO₄: 1.3 x 10⁻²⁰',
        'Ba₃(PO₄)₂: 1.3 x 10⁻²⁹',
        'Ca₃(PO₄)₂: 1.0 x 10⁻²⁵',
        'Ag₃PO₄: 1.3 x 10⁻²⁰',
        'Zr₃(PO₄)₄: 1.0 x 10⁻¹³²',
        'BaHPO₄: 4.0 x 10⁻⁸',
        'Al(HO)₃: 2.7 x 10⁻³²',
        'Ca(HO)₂: 7.9 x 10⁻⁶',
        'Cd(HO)₂: 1.2 x 10⁻¹⁴',
        'Pb(HO)₂: 2.8 x 10⁻¹⁶',
        'Co(HO)₂: 2.5 x 10⁻¹⁶',
        'Cu(HO)₂: 1.6 x 10⁻¹⁹',
        'Sn(HO)₂: 2.0 x 10⁻²⁶',
        'Sn(HO)₄: 1.0 x 10⁻⁵⁷',
        'Fe(HO)₂: 7.9 x 10⁻¹⁵',
        'Fe(HO)₃: 1.5 x 10⁻³⁹',
        'Mg(HO)₂: 9.0 x 10⁻¹²',
        'Hg(HO)₂: 2.5 x 10⁻²⁶',
        'Ni(HO)₂: 2.8 x 10⁻¹⁶',
        'Pd(HO)₄: 6.3 x 10⁻⁷¹',
        'Pt(HO)₂: 1.0 x 10⁻³⁵',
        'Zn(HO)₂: 1.9 x 10⁻¹⁷',
        'Cr(IO3)₃: 5.0 x 10⁻⁶',
        'BiI₃: 8.1 x 10⁻¹⁹',
        'PbI₂: 8.0 x 10⁻⁹',
        'CuI: 1.0 x 10⁻¹²',
        'HgI₂: 4.0 x 10⁻²⁹',
        'AgI: 8.3 x 10⁻¹⁷',
        'MgC₂O₄: 8.6 x 10⁻⁵',
        'NiC₂O₄: 4.0 x 10⁻¹⁰',
        'KIO₄: 3.7 x 10⁻⁴',
        'CsMnO₄: 8.3 x 10⁻⁵',
        'Sb₂S₃: 1.0 x 10⁻⁹³',
        'Bi₂S₃: 1.0 x 10⁻⁹⁷',
        'BaSO₄: 1,0 x 10⁻¹⁰',
        'CaSO₄: 2.4 x 10⁻⁵',
        'PbSO₄: 1.6 x 10⁻⁸',
        'Hg₂SO₄: 7.4 x 10⁻⁷',
        'SrSO₄: 3.2 x 10⁻⁷',
        'Ag₂SO₄: 1.5 x 10⁻⁵',
        'BaSO₃: 8.0 x 10⁻⁷',
        'CaSO₃: 1.3 x 10⁻⁸',
        'CdS: 7.0 x 10⁻²⁷',
        'PbS: 3.2 x 10⁻²⁸',
        'CuS: 8.0 x 10⁻³⁷',
        'FeS: 1.0 x 10⁻¹⁹',
        'HgS: 2.0 x 10⁻⁵³',
        'NiS: 3.0 x 10⁻²¹',
        'Ag₂S: 7.9 x 10⁻⁵¹',
        'ZnS: 2.0 x 10⁻²⁵',
        'Hg(SCN)₂: 2.8 x 10⁻²⁰',
        'AgSCN: 1.16 x 10⁻¹²',
        'BaS₂O₃: 1.6 x 10⁻⁵',
        'AuCl₃: 3.2 x 10⁻²⁵']

def psol_table():
    table(psol)