def city_function(city,country,population=''):
    if population:
        formatted_string=city.title()+","+country.title()+" - "+population
    else:
        formatted_string=city.title()+","+country.title()
    return formatted_string