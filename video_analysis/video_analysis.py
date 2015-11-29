import pickle
import os
import sys
import numpy as np
from face_analyser import analyse_video

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data_analysis'))
if not path in sys.path:
    sys.path.insert(1, path)
del path
from get_heartrates import get_heartrates, get_interesting_heartrates

# PATH_TO_HEARTAV =  "E:\\HeartAV"
PATH_TO_HEARTAV =  "E:\\HeartAV"
WINDOW_SIZE = 4

heartrates = get_heartrates(PATH_TO_HEARTAV)
intersting_heartrates = get_interesting_heartrates(PATH_TO_HEARTAV)

def write_cache(cache_file, data):
    with open(cache_file,'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


#  [[description, time, bpm]]
face_data = {}
specifications = {}
for subject_state in intersting_heartrates.keys():
    times = []
    data_for_subject = intersting_heartrates[subject_state]

    start_of_section = int(data_for_subject[0][1])
    last_time = start_of_section
    for datum in data_for_subject:
        start = int(datum[1])
        end = start + WINDOW_SIZE
        if start == last_time and start - start_of_section <= 20:
            last_time = end
        else:
            print(start_of_section, last_time)
            times.append((start_of_section, last_time))
            start_of_section = start
            last_time = end

    try:
        (data, times) = analyse_video(subject_state, times, heartrates, path_to_heartav=PATH_TO_HEARTAV)
        specifications[subject_state] = times
        face_data[subject_state] = (data, times)
    except Exception as e:
        print(str(e))

write_cache('spec.pickle', specifications)
write_cache('results.pickle', face_data)



#
# times = []
# data_for_subject = intersting_heartrates['38_01']
#
# start_of_section = int(data_for_subject[0][1])
# last_time = start_of_section
# for datum in data_for_subject:
#     start = int(datum[1])
#     end = start + WINDOW_SIZE
#     if start == last_time and start - start_of_section <= 20:
#         last_time = end
#     else:
#         print(start_of_section, last_time)
#         times.append((start_of_section, last_time))
#         start_of_section = start
#         last_time = end
#
# try:
#     (data, times) = analyse_video('38_01', times, heartrates, path_to_heartav=PATH_TO_HEARTAV)
#     print data
#     print times
#     specifications['38_01'] = times
# except Exception as e:
#     print(str(e))