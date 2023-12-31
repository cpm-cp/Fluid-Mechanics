from pandas import DataFrame

# Table to: Acero cédula 40
steel_cc_40 = {
    "Nominal pipe size": ["1/8", "1/4", "3/8", "1/2", "3/4", "1", "1 1/4", "1 1/2", "2", "2 1/2", "3", "3 1/2", "4", "5", "6", "8", "10", "12", "14", "16", "18", "20", "24"],
    "ND (mm)": [6, 8, 10, 15, 20, 25, 32, 40, 50, 65, 80, 90, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600],
    "External diameter (in)": [0.405, 0.540, 0.675, 0.840, 1.050, 1.315, 1.660, 1.900, 2.375, 2.875, 3.500, 4.000, 4.500, 5.563, 6.625, 8.625, 10.750, 12.750, 14.000, 16.000, 18.000, 20.000, 24.000],
    "External diameter (m)": [0.0103, 0.0137, 0.0171, 0.0213, 0.0267, 0.0334, 0.0422, 0.0483, 0.0603, 0.0730, 0.0889, 0.1016, 0.1143, 0.1413, 0.1683, 0.2191, 0.2731, 0.3239, 0.3556, 0.4064, 0.4572, 0.5080, 0.6096],
    "Wall thickness (in)": [0.068, 0.088, 0.091, 0.109, 0.113, 0.133, 0.140, 0.145, 0.154, 0.203, 0.216, 0.226, 0.237, 0.258, 0.280, 0.322, 0.365, 0.406, 0.437, 0.500, 0.562, 0.593, 0.687],
    "Wall thickness (m)": [0.00173, 0.00224, 0.00231, 0.00277, 0.00287, 0.00338, 0.00356, 0.00368, 0.00391, 0.00516, 0.00549, 0.00574, 0.00602, 0.00655, 0.00711, 0.00818, 0.00927, 0.01031, 0.01110, 0.01270, 0.01427, 0.01506, 0.01745],
    "Inside diameter (in)": [0.269, 0.364, 0.493, 0.622, 0.824, 1.049, 1.380, 1.610, 2.067, 2.469, 3.068, 3.548, 4.026, 5.047, 6.065, 7.981, 10.020, 11.938, 13.126, 15.000, 16.876, 18.814, 22.626],
    "Inside diameter (ft)": [0.0224, 0.0303, 0.0411, 0.0518, 0.0687, 0.0874, 0.1150, 0.1342, 0.1723, 0.2058, 0.2557, 0.2957, 0.3355, 0.4206, 0.5054, 0.6651, 0.8350, 0.9948, 1.094, 1.250, 1.406, 1.568, 1.886],
    "Inside diameter (m)": [0.006833, 0.009246, 0.012522, 0.015799, 0.020930, 0.026645, 0.035052, 0.040894, 0.052502, 0.062713, 0.077927, 0.090119, 0.102260, 0.128194, 0.154051, 0.202717, 0.254508, 0.303225, 0.333400, 0.381000, 0.428650, 0.477876, 0.574700],
    "Flow area (ft²)": [0.000394, 0.000723, 0.00133, 0.00211, 0.00370, 0.00600, 0.01039, 0.01414, 0.02333, 0.03326, 0.05132, 0.06868, 0.08840, 0.13900, 0.20060, 0.34720, 0.54790, 0.77710, 0.93960, 1.22700, 1.55300, 1.93100, 2.79200],
    "Flow area (m²)": [3.660e-05, 6.717e-05, 1.236e-04, 1.960e-04, 3.437e-04, 5.574e-04, 9.653e-04, 1.314e-03, 2.168e-03, 3.090e-03, 4.768e-03, 6.381e-03, 8.213e-03, 1.291e-02, 1.864e-02, 3.226e-02, 5.090e-02, 7.219e-02, 8.729e-02, 1.140e-01, 1.443e-01, 1.794e-01, 2.594e-01]
}

df_cc_40 = DataFrame(steel_cc_40)
df_cc_40["Nominal pipe size"] = df_cc_40["Nominal pipe size"].str.replace(" ", "+")


# Table to: Acero cédula 80
steel_cc_80 = {
    "Nominal pipe size": ["1/8", "1/4", "3/8", "1/2", "3/4", "1", "1 1/4", "1 1/2", "2", "2 1/2", "3", "3 1/2", "4", "5", "6", "8", "10", "12", "14", "16", "18", "20", "24"],
    "ND (mm)": [6, 8, 10, 15, 20, 25, 32, 40, 50, 65, 80, 90, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 600],
    "External diameter (in)": [0.405, 0.540, 0.675, 0.840, 1.050, 1.315, 1.660, 1.900, 2.375, 2.875, 3.500, 4.000, 4.500, 5.563, 6.625, 8.625, 10.750, 12.750, 14.000, 16.000, 18.000, 20.000, 24.000],
    "External diameter (m)": [0.0103, 0.0137, 0.0171, 0.0213, 0.0267, 0.0334, 0.0422, 0.0483, 0.0603, 0.0730, 0.0889, 0.1016, 0.1143, 0.1413, 0.1683, 0.2191, 0.2731, 0.3239, 0.3556, 0.4064, 0.4572, 0.5080, 0.6096],
    "Wall thickness (in)": [0.095, 0.119, 0.126, 0.147, 0.154, 0.179, 0.191, 0.200, 0.218, 0.276, 0.300, 0.318, 0.337, 0.375, 0.432, 0.500, 0.593, 0.687, 0.750, 0.842, 0.937, 1.031, 1.218],
    "Wall thickness (m)": [0.00241, 0.00302, 0.00320, 0.00373, 0.00391, 0.00455, 0.00485, 0.00508, 0.00554, 0.00701, 0.00762, 0.00808, 0.00856, 0.00953, 0.01097, 0.01270, 0.01506, 0.01745, 0.01905, 0.02139, 0.02380, 0.02619, 0.03094],
    "Inside diameter (in)": [0.215, 0.302, 0.423, 0.546, 0.742, 0.957, 1.278, 1.500, 1.939, 2.323, 2.900, 3.364, 3.826, 4.813, 5.761, 7.625, 9.564, 11.376, 12.500, 14.314, 16.126, 17.938, 21.564],
    "Inside diameter (m)": [0.0055, 0.0077, 0.0107, 0.0139, 0.0188, 0.0243, 0.0325, 0.0381, 0.0493, 0.0590, 0.0737, 0.0854, 0.0972, 0.1223, 0.1463, 0.1937, 0.2429, 0.2890, 0.3175, 0.3636, 0.4096, 0.4556, 0.5477],
    "Inside diameter (ft)": [0.01772, 0.02507, 0.03501, 0.04528, 0.06102, 0.07890, 0.10535, 0.12336, 0.15978, 0.19357, 0.23950, 0.27887, 0.31693, 0.39990, 0.47402, 0.25000, 0.79766, 0.94088, 1.04167, 1.17997, 1.34219, 1.51393, 1.77938],
    "Flow area (ft²)": [0.000253, 0.000497, 0.000976, 0.001625, 0.00300, 0.00499, 0.00891, 0.01227, 0.02051, 0.02944, 0.04590, 0.06174, 0.07986, 0.1263, 0.1810, 0.3174, 0.4986, 0.7056, 0.8521, 1.117, 1.418, 1.755, 2.535],
    "Flow area (m²)": [0.000024, 0.000047, 0.000090, 0.000152, 0.000278, 0.000464, 0.000830, 0.001140, 0.001909, 0.002734, 0.004266, 0.005728, 0.007420, 0.011747, 0.016810, 0.029468, 0.046339, 0.065597, 0.079173, 0.103834, 0.131768, 0.163026, 0.235600]

}

df_cc_80 = DataFrame(steel_cc_80)
df_cc_80["Nominal pipe size"] = df_cc_80["Nominal pipe size"].str.replace(" ", "+")


def search_steel(delta: int, nominal_size:str) -> tuple:
    """Extract the most important parameters for comercial pipe lines to Steel cc 40 and cc 80.
    Can be modidy to extract more info to the DataFrame.

    Args:
        delta (int): Caliber to pipe.
        nominal_size (str): Nominal pipe size inches. 

    Returns:
        tuple: Inside diamter(in), Inside diamter(m), Flow area(ft^2), Flow area(m^2)
    """
    if delta == 40:
        data = steel_cc_40
    elif delta == 80:
        data = steel_cc_80
    else:
        return "Invalid delta value. Use 40 or 80."

    try:
        index = data['Nominal pipe size'].index(nominal_size)
        diameter_inches = data['Inside diameter (in)'][index]
        diameter_meters = data['Inside diameter (m)'][index]
        area_sqft = data['Flow area (ft²)'][index]
        area_sqm = data['Flow area (m²)'][index]

        return diameter_inches, diameter_meters, area_sqft, area_sqm

    except ValueError:
        return "Nominal size not found in the data."