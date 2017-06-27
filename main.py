'''
Created on Jun 26, 2017

@author: Justin Veyna
'''

"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
MASTER_DICT = {2016: {'New York': {'joint': [(0, 0.04), (17050, 0.045), (23450, 0.0525), (27750, 0.059), (42750, 0.0645), (160500, 0.0665), (321050, 0.0685), (2140900, 0.0882)], 'individual': [(0, 0.04), (8450, 0.045), (11650, 0.0525), (13850, 0.059), (21300, 0.0645), (80150, 0.0665), (214000, 0.0685), (1070350, 0.0882)]}, 'Montana': {'joint': [(0, 0.01), (2900, 0.02), (5100, 0.03), (7800, 0.04), (10500, 0.05), (13500, 0.06), (17400, 0.069)], 'individual': [(0, 0.01), (2900, 0.02), (5100, 0.03), (7800, 0.04), (10500, 0.05), (13500, 0.06), (17400, 0.069)]}, 'Illinois': {'joint': '3.75% of federal', 'individual': '3.75% of federal'}, 'Tennessee': {'joint': [(0, 0.06)], 'individual': [(0, 0.06)]}, 'Nevada': {'joint': 'none', 'individual': 'none'}, 'Mississippi': {'joint': [(0, 0.03), (5000, 0.04), (10000, 0.05)], 'individual': [(0, 0.03), (5000, 0.04), (10000, 0.05)]}, 'Rhode Island': {'joint': [(0, 0.0375), (60850, 0.0475), (138300, 0.0599)], 'individual': [(0, 0.0375), (60850, 0.0475), (138300, 0.0599)]}, 'Nebraska': {'joint': [(0, 0.0246), (6120, 0.0351), (36730, 0.0501), (59180, 0.0684)], 'individual': [(0, 0.0246), (3060, 0.0351), (18370, 0.0501), (29590, 0.0684)]}, 'Arizona': {'joint': [(0, 0.0259), (20000, 0.0288), (50000, 0.0336), (100000, 0.0424), (300000, 0.0454)], 'individual': [(0, 0.0259), (10000, 0.0288), (25000, 0.0336), (50000, 0.0424), (150000, 0.0454)]}, 'Wyoming': {'joint': 'none', 'individual': 'none'}, 'Colorado': {'joint': '4.63% of federal', 'individual': '4.63% of federal'}, 'Michigan': {'joint': '4.25% of federal AGI', 'individual': '4.25% of federal AGI'}, 'California': {'joint': [(0, 0.01), (15700, 0.02), (37220, 0.04), (58744, 0.06), (81546, 0.08), (103060, 0.093), (526444, 0.103), (631732, 0.113), (1000000, 0.123), (1052886, 0.133)], 'individual': [(0, 0.01), (7850, 0.02), (18610, 0.04), (29372, 0.06), (40773, 0.08), (51530, 0.093), (263222, 0.103), (315866, 0.113), (526443, 0.123), (1000000, 0.133)]}, 'Florida': {'joint': 'none', 'individual': 'none'}, 'Kentucky': {'joint': [(0, 0.02), (3000, 0.03), (4000, 0.04), (5000, 0.05), (8000, 0.058), (75000, 0.06)], 'individual': [(0, 0.02), (3000, 0.03), (4000, 0.04), (5000, 0.05), (8000, 0.058), (75000, 0.06)]}, 'Ohio': {'joint': [(0, 0.00495), (5200, 0.0099), (10400, 0.0198), (15650, 0.02476), (20900, 0.02969), (41700, 0.03465), (83350, 0.0396), (104250, 0.04597), (208500, 0.04997)], 'individual': [(0, 0.00495), (5200, 0.0099), (10400, 0.0198), (15650, 0.02476), (20900, 0.02969), (41700, 0.03465), (83350, 0.0396), (104250, 0.04597), (208500, 0.04997)]}, 'Pennsylvania': {'joint': [(0, 0.0307)], 'individual': [(0, 0.0307)]}, 'Kansas': {'joint': [(0, 0.027), (30000, 0.046)], 'individual': [(0, 0.027), (15000, 0.046)]}, 'Washington': {'joint': 'none', 'individual': 'none'}, 'Oklahoma': {'joint': [(0, 0.005), (2000, 0.01), (5000, 0.02), (7500, 0.03), (9800, 0.04), (12200, 0.05)], 'individual': [(0, 0.005), (1000, 0.01), (2500, 0.02), (3750, 0.03), (4900, 0.04), (7200, 0.05)]}, 'Maruland': {'joint': [(0, 0.02), (1000, 0.03), (2000, 0.04), (3000, 0.0475), (150000, 0.05), (175000, 0.0525), (225000, 0.055), (300000, 0.0575)], 'individual': [(0, 0.02), (1000, 0.03), (2000, 0.04), (3000, 0.0475), (100000, 0.05), (125000, 0.0525), (150000, 0.055), (250000, 0.0575)]}, 'Oregon': {'joint': [(0, 0.05), (6500, 0.07), (16300, 0.09), (250000, 0.099)], 'individual': [(0, 0.05), (3350, 0.07), (8400, 0.09), (125000, 0.099)]}, 'New Mexico': {'joint': [(0, 0.017), (8000, 0.032), (16000, 0.047), (24000, 0.049)], 'individual': [(0, 0.017), (5500, 0.032), (11000, 0.047), (16000, 0.049)]}, 'Hawaii': {'joint': [(0, 0.014), (4800, 0.032), (9600, 0.055), (19200, 0.064), (28800, 0.068), (38400, 0.072), (48000, 0.076), (72000, 0.079), (96000, 0.0825)], 'individual': [(0, 0.014), (2400, 0.032), (4800, 0.055), (9600, 0.064), (14400, 0.068), (19200, 0.072), (24000, 0.076), (36000, 0.079), (48000, 0.0825)]}, 'Indiana': {'joint': '3.3% of federal', 'individual': '3.3% of federal'}, 'New Hampshire': {'joint': [(0, 0.05)], 'individual': [(0, 0.05)]}, 'Alaska': {'joint': 'none', 'individual': 'none'}, 'Maine': {'joint': [(0, 0.058), (42099, 0.0675), (74999, 0.0715)], 'individual': [(0, 0.058), (21049, 0.0675), (37499, 0.0715)]}, 'Connecticut': {'joint': [(0, 0.03), (20000, 0.05), (100000, 0.055), (200000, 0.06), (400000, 0.065), (500000, 0.069), (1000000, 0.0699)], 'individual': [(0, 0.03), (10000, 0.05), (50000, 0.055), (100000, 0.06), (200000, 0.065), (250000, 0.069), (500000, 0.0699)]}, 'Wisconsin': {'joint': [(0, 0.04), (14820, 0.0584), (29640, 0.0627), (326330, 0.0765)], 'individual': [(0, 0.04), (11150, 0.0584), (22230, 0.0627), (244750, 0.0765)]}, 'Iowa': {'joint': [(0, 0.0036), (1554, 0.0072), (3108, 0.0243), (6216, 0.045), (13896, 0.0612), (23310, 0.0648), (31080, 0.068), (46620, 0.0792), (69930, 0.0898)], 'individual': [(0, 0.0036), (1554, 0.0072), (3108, 0.0243), (6216, 0.045), (13896, 0.0612), (23310, 0.0648), (31080, 0.068), (46620, 0.0792), (69930, 0.0898)]}, 'Massachusetts': {'joint': [(0, 0.051)], 'individual': [(0, 0.051)]}, 'Vermont': {'joint': [(0, 0.0355), (69900, 0.068), (160450, 0.078), (240000, 0.088), (421900, 0.0895)], 'individual': [(0, 0.0355), (39900, 0.068), (93400, 0.078), (192400, 0.088), (415600, 0.0895)]}, 'Texas': {'joint': 'none', 'individual': 'none'}, 'West Virginia': {'joint': [(0, 0.03), (10000, 0.04), (25000, 0.045), (40000, 0.06), (60000, 0.065)], 'individual': [(0, 0.03), (10000, 0.04), (25000, 0.045), (40000, 0.06), (60000, 0.065)]}, 'Georgia': {'joint': [(0, 0.01), (1000, 0.02), (3000, 0.03), (5000, 0.04), (7000, 0.05), (10000, 0.06)], 'individual': [(0, 0.01), (750, 0.02), (2250, 0.03), (3750, 0.04), (5250, 0.05), (7000, 0.06)]}, 'Washington DC': {'joint': [(0, 0.04), (10000, 0.06), (40000, 0.065), (60000, 0.085), (350000, 0.0875), (1000000, 0.0895)], 'individual': [(0, 0.04), (10000, 0.06), (40000, 0.065), (60000, 0.085), (350000, 0.0875), (1000000, 0.0895)]}, 'New Jersey': {'joint': [(0, 0.014), (20000, 0.0175), (50000, 0.0245), (70000, 0.035), (80000, 0.05525), (150000, 0.0637), (500000, 0.0897)], 'individual': [(0, 0.014), (20000, 0.0175), (35000, 0.035), (40000, 0.05525), (75000, 0.0637), (500000, 0.0897)]}, 'Delaware': {'joint': [(2000, 0.022), (5000, 0.039), (10000, 0.048), (20000, 0.052), (25000, 0.0555), (60000, 0.066)], 'individual': [(2000, 0.022), (5000, 0.039), (10000, 0.048), (20000, 0.052), (25000, 0.0555), (60000, 0.066)]}, 'Alabama': {'joint': [(0, 0.02), (1000, 0.04), (6000, 0.05)], 'individual': [(0, 0.02), (500, 0.04), (3000, 0.05)]}, 'Missouri': {'joint': [(0, 0.015), (1000, 0.02), (2000, 0.025), (3000, 0.03), (4000, 0.035), (5000, 0.04), (6000, 0.045), (7000, 0.05), (8000, 0.055), (9000, 0.06)], 'individual': [(0, 0.015), (1000, 0.02), (2000, 0.025), (3000, 0.03), (4000, 0.035), (5000, 0.04), (6000, 0.045), (7000, 0.05), (8000, 0.055), (9000, 0.06)]}, 'Minnesota': {'joint': [(0, 0.0535), (36820, 0.0705), (146270, 0.0785), (259420, 0.0985)], 'individual': [(0, 0.0535), (25180, 0.0705), (82740, 0.0785), (155650, 0.0985)]}, 'Virginia': {'joint': [(0, 0.02), (3000, 0.03), (5000, 0.05), (17000, 0.0575)], 'individual': [(0, 0.02), (3000, 0.03), (5000, 0.05), (17000, 0.0575)]}, 'North Carolina': {'joint': [(0, 0.0575)], 'individual': [(0, 0.0575)]}, 'Utah': {'joint': [(0, 0.05)], 'individual': [(0, 0.05)]}, 'North Dakota': {'joint': [(0, 0.011), (62600, 0.0204), (151200, 0.0227), (230450, 0.0264), (411500, 0.029)], 'individual': [(0, 0.011), (37450, 0.0204), (90750, 0.0227), (189300, 0.0264), (411500, 0.029)]}, 'Idaho': {'joint': [(0, 0.016), (2904, 0.036), (5808, 0.041), (8712, 0.051), (11616, 0.061), (14520, 0.071), (21780, 0.074)], 'individual': [(0, 0.016), (1452, 0.036), (2940, 0.041), (4356, 0.051), (5808, 0.061), (7260, 0.071), (10890, 0.074)]}, 'South Dakota': {'joint': 'none', 'individual': 'none'}, 'Arkansas': {'joint': [(0, 0.009), (4299, 0.025), (8399, 0.035), (12599, 0.045), (20999, 0.06), (35099, 0.069)], 'individual': [(0, 0.009), (4299, 0.025), (8399, 0.035), (12599, 0.045), (20999, 0.06), (35099, 0.069)]}, 'Louisiana': {'joint': [(0, 0.02), (25000, 0.04), (100000, 0.06)], 'individual': [(0, 0.02), (12500, 0.04), (50000, 0.06)]}, 'South Carolina': {'joint': [(0, 0), (2920, 0.03), (5840, 0.04), (8760, 0.05), (11680, 0.06), (14600, 0.07)], 'individual': [(0, 0), (2920, 0.03), (5840, 0.04), (8760, 0.05), (11680, 0.06), (14600, 0.07)]}}, 2017: {'New York': {'joint': [(0, 0.04), (17150, 0.045), (23600, 0.0525), (27900, 0.059), (43000, 0.0645), (161550, 0.0665), (323200, 0.0685), (2155350, 0.0882)], 'individual': [(0, 0.04), (8500, 0.045), (11700, 0.0525), (13900, 0.059), (21400, 0.0645), (80650, 0.0665), (215400, 0.0685), (1077550, 0.0882)]}, 'Montana': {'joint': [(0, 0.01), (2900, 0.02), (5200, 0.03), (7900, 0.04), (10600, 0.05), (13600, 0.06), (17600, 0.069)], 'individual': [(0, 0.01), (2900, 0.02), (5200, 0.03), (7900, 0.04), (10600, 0.05), (13600, 0.06), (17600, 0.069)]}, 'Illinois': {'joint': '3.75% of federal', 'individual': '3.75% of federal'}, 'Tennessee': {'joint': [(0, 0.05)], 'individual': [(0, 0.05)]}, 'Nevada': {'joint': 'none', 'individual': 'none'}, 'Mississippi': {'joint': [(0, 0.03), (5000, 0.04), (10000, 0.05)], 'individual': [(0, 0.03), (5000, 0.04), (10000, 0.05)]}, 'Rhode Island': {'joint': [(0, 0.0375), (61300, 0.0475), (139400, 0.0599)], 'individual': [(0, 0.0375), (61300, 0.0475), (139400, 0.0599)]}, 'Nebraska': {'joint': [(0, 0.0246), (6170, 0.0351), (37030, 0.0501), (59660, 0.0684)], 'individual': [(0, 0.0246), (3090, 0.0351), (18510, 0.0501), (29830, 0.0684)]}, 'Arizona': {'joint': [(0, 0.0259), (20357, 0.0288), (50890, 0.0336), (101779, 0.0424), (305336, 0.0454)], 'individual': [(0, 0.0259), (10179, 0.0288), (25445, 0.0336), (50890, 0.0424), (152668, 0.0454)]}, 'Wyoming': {'joint': 'none', 'individual': 'none'}, 'Colorado': {'joint': '4.63% of federal', 'individual': '4.63% of federal'}, 'Michigan': {'joint': '4.25% of federal AGI', 'individual': '4.25% of federal AGI'}, 'California': {'joint': [(0, 0.01), (16030, 0.02), (38002, 0.04), (59978, 0.06), (83258, 0.08), (105224, 0.093), (537500, 0.103), (644998, 0.113), (1074996, 0.123), (1074996, 0.133)], 'individual': [(0, 0.01), (8015, 0.02), (19001, 0.03), (29989, 0.04), (41629, 0.08), (52612, 0.093), (268750, 0.103), (322499, 0.113), (537498, 0.123), (1000000, 0.133)]}, 'Florida': {'joint': 'none', 'individual': 'none'}, 'Kentucky': {'joint': [(0, 0.02), (3000, 0.03), (4000, 0.04), (5000, 0.05), (8000, 0.058), (75000, 0.06)], 'individual': [(0, 0.02), (3000, 0.03), (4000, 0.04), (5000, 0.05), (8000, 0.058), (75000, 0.06)]}, 'Ohio': {'joint': [(0, 0.00495), (5250, 0.0099), (10500, 0.0198), (15800, 0.02476), (21100, 0.02969), (42100, 0.03465), (84200, 0.0396), (105300, 0.04597), (210600, 0.04997)], 'individual': [(0, 0.00495), (5250, 0.0099), (10500, 0.0198), (15800, 0.02476), (21100, 0.02969), (42100, 0.03465), (84200, 0.0396), (105300, 0.04597), (210600, 0.04997)]}, 'Pennsylvania': {'joint': [(0, 0.0307)], 'individual': [(0, 0.0307)]}, 'Kansas': {'joint': [(0, 0.027), (30000, 0.046)], 'individual': [(0, 0.027), (15000, 0.046)]}, 'Washington': {'joint': 'none', 'individual': 'none'}, 'Oklahoma': {'joint': [(0, 0.005), (2000, 0.01), (5000, 0.02), (7500, 0.03), (9800, 0.04), (12200, 0.05)], 'individual': [(0, 0.005), (1000, 0.01), (2500, 0.02), (3750, 0.03), (4900, 0.04), (7200, 0.05)]}, 'Maruland': {'joint': [(0, 0.02), (1000, 0.03), (2000, 0.04), (3000, 0.0475), (150000, 0.05), (175000, 0.0525), (225000, 0.055), (300000, 0.0575)], 'individual': [(0, 0.02), (1000, 0.03), (2000, 0.04), (3000, 0.0475), (100000, 0.05), (125000, 0.0525), (150000, 0.055), (250000, 0.0575)]}, 'Oregon': {'joint': [(0, 0.05), (6700, 0.07), (16900, 0.09), (250000, 0.099)], 'individual': [(0, 0.05), (3350, 0.07), (8450, 0.09), (125000, 0.099)]}, 'New Mexico': {'joint': [(0, 0.017), (8000, 0.032), (16000, 0.047), (24000, 0.049)], 'individual': [(0, 0.017), (5500, 0.032), (11000, 0.047), (16000, 0.049)]}, 'Hawaii': {'joint': [(0, 0.014), (4800, 0.032), (9600, 0.055), (19200, 0.064), (28800, 0.068), (38400, 0.072), (48000, 0.076), (72000, 0.079), (96000, 0.0825)], 'individual': [(0, 0.014), (2400, 0.032), (4800, 0.055), (9600, 0.064), (14400, 0.068), (19200, 0.072), (24000, 0.076), (36000, 0.079), (48000, 0.0825)]}, 'Indiana': {'joint': '3.23% of federal', 'individual': '3.23% of federal'}, 'New Hampshire': {'joint': [(0, 0.05)], 'individual': [(0, 0.05)]}, 'Alaska': {'joint': 'none', 'individual': 'none'}, 'Maine': {'joint': [(0, 0.058), (42250, 0.0675), (100000, 0.0715), (200001, 0.1015)], 'individual': [(0, 0.058), (21100, 0.0675), (50000, 0.0715), (200001, 0.1015)]}, 'Connecticut': {'joint': [(0, 0.03), (20000, 0.05), (100000, 0.055), (200000, 0.06), (400000, 0.065), (500000, 0.069), (1000000, 0.0699)], 'individual': [(0, 0.03), (10000, 0.05), (50000, 0.055), (100000, 0.06), (200000, 0.065), (250000, 0.069), (500000, 0.0699)]}, 'Wisconsin': {'joint': [(0, 0.04), (14980, 0.0584), (29960, 0.0627), (329810, 0.0765)], 'individual': [(0, 0.04), (11230, 0.0584), (22470, 0.0627), (247350, 0.0765)]}, 'Iowa': {'joint': [(0, 0.0036), (1573, 0.0072), (3146, 0.0243), (6292, 0.045), (14157, 0.0612), (23595, 0.0648), (31460, 0.068), (47190, 0.0792), (70785, 0.0898)], 'individual': [(0, 0.0036), (1573, 0.0072), (3146, 0.0243), (6292, 0.045), (14157, 0.0612), (23595, 0.0648), (31460, 0.068), (47190, 0.0792), (70785, 0.0898)]}, 'Massachusetts': {'joint': [(0, 0.051)], 'individual': [(0, 0.051)]}, 'Vermont': {'joint': [(0, 0.0355), (63350, 0.068), (153100, 0.078), (233350, 0.088), (416700, 0.0895)], 'individual': [(0, 0.0355), (37950, 0.068), (91900, 0.078), (191650, 0.088), (416700, 0.0895)]}, 'Texas': {'joint': 'none', 'individual': 'none'}, 'West Virginia': {'joint': [(0, 0.03), (10000, 0.04), (25000, 0.045), (40000, 0.06), (60000, 0.065)], 'individual': [(0, 0.03), (10000, 0.04), (25000, 0.045), (40000, 0.06), (60000, 0.065)]}, 'Georgia': {'joint': [(0, 0.01), (1000, 0.02), (3000, 0.03), (5000, 0.04), (7000, 0.05), (10000, 0.06)], 'individual': [(0, 0.01), (750, 0.02), (2250, 0.03), (3750, 0.04), (5250, 0.05), (7000, 0.06)]}, 'Washington DC': {'joint': [(0, 0.04), (10000, 0.06), (40000, 0.065), (60000, 0.085), (350000, 0.0875), (1000000, 0.0895)], 'individual': [(0, 0.04), (10000, 0.06), (40000, 0.065), (60000, 0.085), (350000, 0.0875), (1000000, 0.0895)]}, 'New Jersey': {'joint': [(0, 0.014), (20000, 0.0175), (50000, 0.0245), (70000, 0.035), (80000, 0.05525), (150000, 0.0637), (500000, 0.0897)], 'individual': [(0, 0.014), (20000, 0.0175), (35000, 0.035), (40000, 0.05525), (75000, 0.0637), (500000, 0.0897)]}, 'Delaware': {'joint': [(2000, 0.022), (5000, 0.039), (10000, 0.048), (20000, 0.052), (25000, 0.0555), (60000, 0.066)], 'individual': [(2000, 0.022), (5000, 0.039), (10000, 0.048), (20000, 0.052), (25000, 0.0555), (60000, 0.066)]}, 'Alabama': {'joint': [(0, 0.02), (1000, 0.04), (6000, 0.05)], 'individual': [(0, 0.02), (500, 0.04), (3000, 0.05)]}, 'Missouri': {'joint': [(0, 0.015), (1008, 0.02), (2016, 0.025), (3024, 0.03), (4032, 0.035), (5040, 0.04), (6048, 0.045), (7056, 0.05), (8064, 0.055), (9072, 0.06)], 'individual': [(0, 0.015), (1008, 0.02), (2016, 0.025), (3024, 0.03), (4032, 0.035), (5040, 0.04), (6048, 0.045), (7056, 0.05), (8064, 0.055), (9072, 0.06)]}, 'Minnesota': {'joint': [(0, 0.0535), (37110, 0.0705), (147450, 0.0785), (261510, 0.0985)], 'individual': [(0, 0.0535), (25390, 0.0705), (83400, 0.0785), (156911, 0.0985)]}, 'Virginia': {'joint': [(0, 0.02), (3000, 0.03), (5000, 0.05), (17000, 0.0575)], 'individual': [(0, 0.02), (3000, 0.03), (5000, 0.05), (17000, 0.0575)]}, 'North Carolina': {'joint': [(0, 0.05499)], 'individual': [(0, 0.05499)]}, 'Utah': {'joint': [(0, 0.05)], 'individual': [(0, 0.05)]}, 'North Dakota': {'joint': [(0, 0.011), (63400, 0.0204), (153100, 0.0227), (233350, 0.0264), (416700, 0.029)], 'individual': [(0, 0.011), (37950, 0.0204), (91900, 0.0227), (191650, 0.0264), (416700, 0.029)]}, 'Idaho': {'joint': [(0, 0.016), (2908, 0.036), (5816, 0.041), (8724, 0.051), (11632, 0.061), (14540, 0.071), (21810, 0.074)], 'individual': [(0, 0.016), (1454, 0.036), (2908, 0.041), (4362, 0.051), (5816, 0.061), (7270, 0.071), (10905, 0.074)]}, 'South Dakota': {'joint': 'none', 'individual': 'none'}, 'Arkansas': {'joint': [(0, 0.009), (4299, 0.025), (8499, 0.035), (12799, 0.045), (21299, 0.06), (35099, 0.069)], 'individual': [(0, 0.009), (4299, 0.025), (8499, 0.035), (12799, 0.045), (21299, 0.06), (35099, 0.069)]}, 'Louisiana': {'joint': [(0, 0.02), (25000, 0.04), (100000, 0.06)], 'individual': [(0, 0.02), (12500, 0.04), (50000, 0.06)]}, 'South Carolina': {'joint': [(0, 0), (2930, 0.03), (5860, 0.04), (8790, 0.05), (11720, 0.06), (14650, 0.07)], 'individual': [(0, 0), (2930, 0.03), (5860, 0.04), (8790, 0.05), (11720, 0.06), (14650, 0.07)]}}, 2015: {'New York': {'joint': [(7900, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.04), (8400, 0.045), (11600, 0.0525), (13750, 0.059), (21150, 0.0645), (79600, 0.0665), (212500, 0.0685), (1062650, 0.0882)]}, 'Montana': {'joint': [(4370, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.01), (2800, 0.02), (5000, 0.03), (7600, 0.04), (10300, 0.05), (13300, 0.06), (17000, 0.069)]}, 'Illinois': {'joint': None, 'individual': '3.75% of federal'}, 'Tennessee': {'joint': [('n.a.', '>')], 'individual': [(0, 0.06)]}, 'Nevada': {'joint': None, 'individual': 'none'}, 'Mississippi': {'joint': [(2300, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.03), (5000, 0.04), (10000, 0.05)]}, 'Rhode Island': {'joint': [(8275, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0375), (60500, 0.0475), (137650, 0.0599)]}, 'Nebraska': {'joint': [(5800, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0246), (3050, 0.0351), (18280, 0.0501), (29460, 0.0684)]}, 'Arizona': {'joint': [(5009, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0259), (10000, 0.0288), (25000, 0.0336), (50000, 0.0424), (150000, 0.0454)]}, 'Wyoming': {'joint': None, 'individual': 'none'}, 'Colorado': {'joint': None, 'individual': '4.63% of federal'}, 'Michigan': {'joint': None, 'individual': '4.25% of federal AGI'}, 'California': {'joint': [(3992, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.01), (7749, 0.02), (18371, 0.04), (28995, 0.06), (40250, 0.08), (50689, 0.093), (259844, 0.103), (311812, 0.113), (519867, 0.123), (1000000, 0.133)]}, 'Florida': {'joint': None, 'individual': 'none'}, 'Kentucky': {'joint': [(2440, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.02), (3000, 0.03), (4000, 0.04), (5000, 0.05), (8000, 0.058), (75000, 0.06)]}, 'Ohio': {'joint': [('n.a.', '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0053), (5200, 0.0106), (10400, 0.0211), (15650, 0.0264), (20900, 0.0317), (41700, 0.037), (83350, 0.0423), (104250, 0.0491), (208500, 0.0533)]}, 'Pennsylvania': {'joint': [('n.a.', '>')], 'individual': [(0, 0.0307)]}, 'Kansas': {'joint': [(3000, '>'), (None, '>')], 'individual': [(0, 0.027), (15000, 0.046)]}, 'Washington': {'joint': None, 'individual': 'none'}, 'Oklahoma': {'joint': [(5950, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.005), (1000, 0.01), (2500, 0.02), (3750, 0.03), (4900, 0.04), (7200, 0.05), (8700, 0.0525)]}, 'Maruland': {'joint': [(2000, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.02), (1000, 0.03), (2000, 0.04), (3000, 0.0475), (100000, 0.05), (125000, 0.0525), (150000, 0.055), (250000, 0.0575)]}, 'Oregon': {'joint': [(2145, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.05), (3350, 0.07), (8400, 0.09), (125000, 0.099)]}, 'New Mexico': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.017), (5500, 0.032), (11000, 0.047), (16000, 0.049)]}, 'Hawaii': {'joint': [(2200, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.014), (2400, 0.032), (4800, 0.055), (9600, 0.064), (14400, 0.068), (19200, 0.072), (24000, 0.076), (36000, 0.079), (48000, 0.0825), (150000, 0.09), (175000, 0.1), (200000, 0.11)]}, 'Indiana': {'joint': None, 'individual': '3.3% of federal'}, 'New Hampshire': {'joint': [('n.a', '>')], 'individual': [(0, 0.05)]}, 'Alaska': {'joint': None, 'individual': 'none'}, 'Maine': {'joint': [(6300, '>'), (None, '>')], 'individual': [(5199, 0.065), (20899, 0.0795)]}, 'Connecticut': {'joint': [('n.a.', '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.03), (10000, 0.05), (50000, 0.055), (100000, 0.06), (200000, 0.065), (250000, 0.067)]}, 'Wisconsin': {'joint': [(10250, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.04), (11090, 0.0584), (22190, 0.0627), (244270, 0.0765)]}, 'Iowa': {'joint': [(1950, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0036), (1539, 0.0072), (3078, 0.0243), (6156, 0.045), (13851, 0.0612), (23085, 0.0648), (30780, 0.068), (46170, 0.0792), (69255, 0.0898)]}, 'Massachusetts': {'joint': [('n.a.', '>')], 'individual': [(0, 0.0515)]}, 'Vermont': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0355), (37450, 0.068), (90750, 0.078), (189300, 0.088), (411500, 0.0895)]}, 'Texas': {'joint': None, 'individual': 'none'}, 'West Virginia': {'joint': [('n.a.', '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.03), (10000, 0.04), (25000, 0.045), (40000, 0.06), (60000, 0.065)]}, 'Georgia': {'joint': [(2300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.01), (750, 0.02), (2250, 0.03), (3750, 0.04), (5250, 0.05), (7000, 0.06)]}, 'Washington DC': {'joint': [(5200, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.04), (10000, 0.06), (40000, 0.07), (60000, 0.085), (350000, 0.0895)]}, 'New Jersey': {'joint': [('n.a.', '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.014), (20000, 0.0175), (35000, 0.035), (40000, 0.0553), (75000, 0.0637), (500000, 0.0897)]}, 'Delaware': {'joint': [(3250, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(2000, 0.022), (5000, 0.039), (10000, 0.048), (20000, 0.052), (25000, 0.0555), (60000, 0.066)]}, 'Alabama': {'joint': [(2500, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.02), (500, 0.04), (3000, 0.05)]}, 'Missouri': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.015), (1000, 0.02), (2000, 0.025), (3000, 0.03), (4000, 0.035), (5000, 0.04), (6000, 0.045), (7000, 0.05), (8000, 0.055), (9000, 0.06)]}, 'Minnesota': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0535), (25070, 0.0705), (82360, 0.0785), (154950, 0.0985)]}, 'Virginia': {'joint': [(3000, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.02), (3000, 0.03), (5000, 0.05), (17000, 0.0575)]}, 'North Carolina': {'joint': [(7500, '>')], 'individual': [(0, 0.0575)]}, 'Utah': {'joint': [('(l)', '>')], 'individual': [(0, 0.05)]}, 'North Dakota': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.0122), (36900, 0.0227), (89350, 0.0252), (186350, 0.0293), (405100, 0.0322)]}, 'Idaho': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.016), (1428, 0.036), (2857, 0.041), (4286, 0.051), (5715, 0.061), (7144, 0.071), (10717, 0.074)]}, 'South Dakota': {'joint': None, 'individual': 'none'}, 'Arkansas': {'joint': [(2000, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.01), (4299, 0.025), (8399, 0.035), (12599, 0.045), (20999, 0.06), (35099, 0.07)]}, 'Louisiana': {'joint': [('n.a.', '>'), (None, '>'), (None, '>')], 'individual': [(0, 0.02), (12500, 0.04), (50000, 0.06)]}, 'South Carolina': {'joint': [(6300, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>'), (None, '>')], 'individual': [(0, 0), (2880, 0.03), (5760, 0.04), (8640, 0.05), (11520, 0.06), (14400, 0.07)]}}}


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Tax Finder. " \
                    "Please tell me the year, state, filing status, and yearly income by saying, " \
                    "2016, California, individual, 200,000"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me the year, state, filing status, and yearly income by saying, " \
                    "2016, California, individual, 200,000"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = ""
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}

def tax_find(intent, session):
    session_attributes = {}
    reprompt_text = None
    
    year = intent["slots"]["Year"]["value"]
    state = intent["slots"]["State"]["value"]
    odd_states = ["Alaska", "Colorado", "Florida", "Illinois", "Indiana", "Michigan", "Nevada", "South Dakota", "Texas", "Washington", "Wyoming"]
    filing_status = intent["slots"]["FilingStatus"]["value"]
    income = intent["slots"]["Income"]["value"]
    if state in odd_states:
        speech_output = "I cannot find the tax rate for this state."
    else:
        i = 0
        while income > MASTER_DICT[year][state][filing_status][i][0]:
            i+=1
        tax = MASTER_DICT[year][state][filing_status][i-1][1]
        speech_output = "The income tax is " + str(tax*100)+ " percent"
    should_end_session = True

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "TaxFindIntent":
        return tax_find(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
