import gpxpy
import gpxpy.gpx
from geopy.distance import geodesic

def smooth_gpx_file(input_file, output_file, max_distance_meters=10):
    # Parse the input GPX file
    with open(input_file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    new_gpx = gpxpy.gpx.GPX()

    for track in gpx.tracks:
        new_track = gpxpy.gpx.GPXTrack()
        new_gpx.tracks.append(new_track)
        for segment in track.segments:
            new_segment = gpxpy.gpx.GPXTrackSegment()
            new_track.segments.append(new_segment)
            prev_point = None
            for point in segment.points:
                if prev_point is None or geodesic((prev_point.latitude, prev_point.longitude), (point.latitude, point.longitude)).meters > max_distance_meters:
                    new_segment.points.append(point)
                    prev_point = point

    # Write the smoothed GPX data to the output file
    with open(output_file, 'w') as gpx_file:
        gpx_file.write(new_gpx.to_xml())

# Run the function; change file names to desired GPX files in current directory
smooth_gpx_file('input.gpx', 'output.gpx', 10)
