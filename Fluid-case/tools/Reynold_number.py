# Create functions.

# Reynolds number
def Reynolds_number(dimater:float, velocity:float, density:float = None, dinamic_viscosity:float = None, cinematic_viscosity:float = None) -> float:
    """This function calculate the dimensionaless Reynold number in function to diamete, velocity, substance density and dinamic or cinematic viscosity. 
    Remember that all parameters should be have the same dimensional consistence.

    Args:
        dimater (float): Diameter value.
        velocity (float): Veclocity to transport the substance.
        density (float, optional): Density by the select substance. Defaults to None.
        dinamic_viscosity (float, optional): Dinamic viscosity. Defaults to None.
        cinematic_viscosity (float, optional): Cinematic viscosity. Defaults to None.

    Returns:
        float: Dimensionaless Reynolds number value.
    """
    if density and dinamic_viscosity != None and cinematic_viscosity == None:
        n_Reynolds = (velocity * dimater * density) / dinamic_viscosity
    else:
        n_Reynolds = (velocity * dimater) / cinematic_viscosity
    
    return n_Reynolds

def regimen_flow(diameter: float, velocity: float, density: float = None, dynamic_viscosity: float = None, cinematic_viscosity: float = None) -> str:
    """This function recognizes the flow regime based on Reynolds number calculation.

    Args:
        diameter (float): Diameter value.
        velocity (float): Velocity to transport the substance.
        density (float, optional): Density of the substance. Defaults to None.
        dynamic_viscosity (float, optional): Dynamic viscosity. Defaults to None.
        cinematic_viscosity (float, optional): Cinematic viscosity. Defaults to None.

    Returns:
        str: The flow regime.
    """
    reynolds = Reynolds_number(diameter, velocity, density, dynamic_viscosity, cinematic_viscosity)
    if reynolds > 0 and reynolds < 2000:
        regimen_flow = "The flow regime is Laminar"
    elif reynolds >= 2000 and reynolds < 4000:
        regimen_flow = "The flow regime is Transition"
    else:
        regimen_flow = "The flow regime is Turbulent"
    return regimen_flow

