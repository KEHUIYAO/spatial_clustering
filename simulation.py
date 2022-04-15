import geopandas as gpd
import matplotlib.pyplot as plt
import libpysal
import scipy.stats
import numpy

# read a shape file 
gdf = gpd.read_file('Cincinnati_Community_Council_Boundaries/Cincinnati_Community_Council_Boundaries.shp')

print(type(gdf))  
print(gdf.head())

# plot it on the map
ax = gdf.plot()
plt.show()

# graph structure
w_rook = libpysal.weights.Rook.from_dataframe(gdf)
print(w_rook.neighbors[0])

# generate expected counts for each location
def generate_expected_counts(n, mu):
    """generate expected counts for each location.

    Assume there are n locations, and generate counts for each location following Poisson(mu).

    Args:
        n (int): number of locations.
        mu (float): mean parameter mu for Poisson distribution.

    Returns:
        numpy.ndarray: a vector of expected counts for each location
    """

n_units = gdf.shape[0]
