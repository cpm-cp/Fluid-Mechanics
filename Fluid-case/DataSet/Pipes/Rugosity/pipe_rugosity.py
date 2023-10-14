def rugosity_value(material:str, unit:str = "m") -> float:
    """This function extract the rugosity value for a specific material's list:

    - glass
    - plastic
    - extruded pipe
    - steel
    - galvanized steel
    - ductyl iron covered 
    - ductyl iron no-covered
    - concrete  
    - riveted iron 

    Args:
        material (str): Pipe material.
        unit (str, optional): Unit to return the rugosity value. Defaults to "m".

    Returns:
        float: Rugosity value in meters or foot.
    """
    rugosity = {
        "glass": {"m": 3.0e-07, "ft": 1.0e-06},
        "plastic": {"m": 3.0e-07, "ft": 1.0e-06},
        "extruded pipe": {"m": 3.0e-07, "ft": 1.0e-06},
        "steel": {"m": 3.0e-07, "ft": 1.0e-06},
        "galvanized steel": {"m": 3.0e-07, "ft": 1.0e-06},
        "ductyl iron coverd": {"m": 3.0e-07, "ft": 1.0e-06},
        "ductyl iron no-covered": {"m": 3.0e-07, "ft": 1.0e-06},
        "concrete": {"m": 3.0e-07, "ft": 1.0e-06},
        "riveted iron": {"m": 3.0e-07, "ft": 1.0e-06}
    }

    try:
        return rugosity[material][unit]
    except KeyError:
        return f"Material '{material}' or unit '{unit}' not found in the dictionary."