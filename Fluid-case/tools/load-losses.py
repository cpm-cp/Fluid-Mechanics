# Import modules
import numpy as np
from Reynold_number import regimen_flow, Reynolds_number

def friction_factor(diameter: float, rugosity: float, velocity: float, density: float = None, dynamic_viscosity: float = None, cinematic_viscosity: float = None) -> float:
    """Calculate the friction factor if the regimen flow is laminar or turbulent.

    Args:
        diameter (float): Diameter value.
        velocity (float): Velocity to transport the substance.
        density (float, optional): Density of the substance. Defaults to None.
        dynamic_viscosity (float, optional): Dynamic viscosity. Defaults to None.
        cinematic_viscosity (float, optional): Cinematic viscosity. Defaults to None.
        rugosity (float): rugosity by the material to transport fluid

    Returns:
        float: Friction value.
    """
    reynolds = Reynolds_number(diameter, velocity, density, dynamic_viscosity, cinematic_viscosity)
    flow_regime = regimen_flow(diameter, velocity, density, dynamic_viscosity, cinematic_viscosity)

    if flow_regime == "The flow regime is Laminar":
        friction_value = 64 / reynolds
    elif flow_regime == "The flow regime is Turbulent":
        friction_value = 0.25 / (np.log10((1 / 3.7 * (diameter / rugosity)) + (5.74 / reynolds**0.9)))**2

    return friction_value

def friction_losses(leght:float, diameter: float, rugosity: float, velocity: float, density: float = None, dynamic_viscosity: float = None, cinematic_viscosity: float = None) -> float:
    """This function calculate the friction losses for a pipe system in function to the Reynold number and friction factor.

    Args:
        leght (float): Leght to the system (pipe line).
        diameter (float): diameter by the transport the fluid.
        rugosity (float): rugosity by the material to transport fluid.
        velocity (float): velocity to transport.
        density (float, optional): density to the substance. Defaults to None.
        dynamic_viscosity (float, optional): dinamic viscosity by the substance. Defaults to None.
        cinematic_viscosity (float, optional): cinematic viscosity by the substance. Defaults to None.

    Returns:
        float: Friction losses value.
    """
    friction_fact = friction_factor(diameter, rugosity, velocity, density, dynamic_viscosity, cinematic_viscosity)
    gravity = 9.81 # m/s^2
    friction_loss = friction_fact * (leght / diameter) * (velocity**2 / 2 * gravity)
    
    return friction_loss

# # Example usage
# diameter = 0.1
# velocity = 1
# density = 1000
# dynamic_viscosity = 0.001
# cinematic_viscosity = None
# rugosity = 0.0012
# leght = 18

# friction_fact = friction_losses(leght, diameter, rugosity, velocity, density, dynamic_viscosity, cinematic_viscosity)
# print(friction_fact)
