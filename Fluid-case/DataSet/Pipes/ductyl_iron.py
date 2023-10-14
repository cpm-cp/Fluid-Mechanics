from pandas import DataFrame
    

# Table to: Ductyl iron
ductyl_iron = {
    "Nominal pipe size": ["4", "6", "8", "10", "12", "14", "16", "18", "20", "24", "30", "36", "42", "48"],
    "ND (mm)": [100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 750, 900, 1050, 1200],
    "External diameter (in)": [4.80, 6.90, 9.05, 11.10, 13.20, 15.30, 17.40, 19.50, 21.60, 25.80, 32.00, 38.30, 44.50, 50.80],
    "External diameter (m)": [0.1219, 0.1753, 0.2299, 0.2819, 0.3353, 0.3886, 0.4420, 0.4953, 0.5486, 0.6553, 0.8128, 0.9728, 1.1303, 1.2903],
    "Wall thickness (in)": [0.315, 0.315, 0.315, 0.325, 0.345, 0.375, 0.395, 0.405, 0.425, 0.425, 0.465, 0.505, 0.535, 0.585],
    "Wall thickness (m)": [0.008001, 0.008001, 0.008001, 0.008255, 0.008763, 0.009525, 0.010033, 0.010287, 0.010795, 0.010795, 0.011811, 0.012827, 0.013589, 0.014859],
    "Inside diameter (in)": [4.17, 6.27, 8.42, 10.45, 12.51, 14.55, 16.61, 18.69, 20.75, 24.95, 31.07, 37.29, 43.43, 49.63],
    "Inside diameter (ft)": [0.348, 0.523, 0.702, 0.871, 1.043, 1.213, 1.384, 1.558, 1.729, 2.079, 2.589, 3.108, 3.619, 4.136],
    "Inside diameter (m)": [0.1059, 0.1593, 0.2139, 0.2654, 0.3178, 0.3696, 0.4219, 0.4747, 0.5271, 0.6337, 0.7892, 0.9472, 1.1031, 1.2606],
    "Flow area (ft²)": [0.0948, 0.2144, 0.3867, 0.5956, 0.8536, 1.155, 1.505, 1.905, 2.348, 3.395, 5.265, 7.584, 10.287, 13.434],
    "Flow area (m²)": [0.00881, 0.01993, 0.03594, 0.05535, 0.07933, 0.1073, 0.1398, 0.1771, 0.2182, 0.3155, 0.4893, 0.7049, 0.9561, 1.2485]
}
df_Fe_ductyl = DataFrame(ductyl_iron)

def search_ductyl_iron(nominal_size: str, type: str = None) -> tuple:
    if type == None:
        data = ductyl_iron
    else:
        return "Non type to search"
    
    try:
        index = data['Nominal pipe size'].index(nominal_size)
        diameter_inches = data['Inside diameter (in)'][index]
        diameter_meters = data['Inside diameter (m)'][index]
        area_sqft = data['Flow area (ft²)'][index]
        area_sqm = data['Flow area (m²)'][index]

        return diameter_inches, diameter_meters, area_sqft, area_sqm

    except ValueError:
        return "Nominal size not found in the data."