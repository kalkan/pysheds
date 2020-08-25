from pysheds.grid import Grid

grid = Grid.from_raster('n30w100_con', data_name='dem')
grid.read_raster('n30w100_dir', data_name='dir')
grid.view('dem')

# Determine D8 flow directions from DEM
# ----------------------
# Fill depressions in DEM
grid.fill_depressions('dem', out_name='flooded_dem')
    
# Resolve flats in DEM
grid.resolve_flats('flooded_dem', out_name='inflated_dem')
    
# Specify directional mapping
dirmap = (64, 128, 1, 2, 4, 8, 16, 32)
    
# Compute flow directions
# -------------------------------------
grid.flowdir(data='inflated_dem', out_name='dir', dirmap=dirmap)
grid.view('dir')