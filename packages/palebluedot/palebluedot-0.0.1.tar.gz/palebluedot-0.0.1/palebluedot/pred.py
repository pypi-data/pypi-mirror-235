from orbit_predictor.locations import Location
from orbit_predictor.groundtrack import compute_groundtrack
from orbit_predictor.sources import NoradTLESource
import rasterio
from rasterio.transform import Affine, from_gcps
from rasterio.control import GroundControlPoint
from datetime import datetime, timedelta


def date_range(start, end, step):
    while start < end:
        yield start
        start += step


radar = Location("RADAR", 45.500764, -73.617044, 130)
source = NoradTLESource.from_file("data/noaa.txt")
predictor = source.get_predictor("NOAA 15")
passing = next(predictor.passes_over(radar, datetime(2023, 5, 25, 23, 50)).iter_passes())
track = compute_groundtrack(
    predictor,
    date_range(passing.aos, passing.los, timedelta(milliseconds=500))
)


# tl = GroundControlPoint(0, 0, -83.70113410256013, 42.307951446432604)
# bl = GroundControlPoint(1024, 0, -83.69940501521428, 42.307603183805234)
# br = GroundControlPoint(1024, 1280, -83.698829074736, 42.3091785425499)
# tr = GroundControlPoint(0, 1280, -83.70055820297041, 42.309526812647555)

# top = GroundControlPoint(120, 0, *track[0])
# middle = GroundControlPoint(120, 500, *track[500])
# bottom = GroundControlPoint(120, 1000, *track[1000])

# x = from_gcps([top, middle, bottom])
# breakpoint()


# file = rasterio.open(
#     "out.tif",
#     "w",
#     driver="GTiff",



geojson = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [[lon, lat] for lon, lat, _ in track],
        },
    }],
}

from json import dumps
print(dumps(geojson))
