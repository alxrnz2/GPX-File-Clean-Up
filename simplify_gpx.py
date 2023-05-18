import gpxpy
import gpxpy.gpx

def remove_time_and_extensions(input_file, output_file):
    # Parse the input GPX file
    with open(input_file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Remove other data points as needed via point.[data]...
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                point.time = None
                point.extensions = {}

    # Write the cleaned GPX data to the output file
    with open(output_file, 'w') as gpx_file:
        gpx_file.write(gpx.to_xml())

# Run the function; modify file names for desired GPX files in current directory
remove_time_and_extensions('input.gpx', 'output.gpx')
