from geopy import distance

efhk_coords = (60.3172, 24.963301)
efvu_coords = (68.087196, 27.123899)
distance_result = distance.distance((efhk_coords), (efvu_coords))
print(distance_result)