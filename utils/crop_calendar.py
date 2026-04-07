crop_calendar_dict = {
    "rice": [
        {"phase": "Sowing & Seedling", "duration": "Days 1-20", "action": "Ensure soil is flooded for land preparation (puddling). Apply base NPK fertilizer.", "icon": "fa-seedling"},
        {"phase": "Vegetative & Tillering", "duration": "Days 21-60", "action": "Maintain shallow water level. Apply top dressing of Nitrogen to encourage tillering.", "icon": "fa-leaf"},
        {"phase": "Reproductive (Panicle Initiation)", "duration": "Days 61-90", "action": "Critical water stage. Ensure fields do not dry out. Monitor for stem borers.", "icon": "fa-sun"},
        {"phase": "Ripening & Harvesting", "duration": "Days 91-120", "action": "Drain water 10-15 days before harvest to allow grains to mature and harden.", "icon": "fa-tractor"}
    ],
    "maize": [
        {"phase": "Sowing & Emergence", "duration": "Days 1-15", "action": "Sow seeds 2-3 inches deep in moist soil. Apply baseline Phosphorous.", "icon": "fa-seedling"},
        {"phase": "Rapid Vegetative Growth", "duration": "Days 16-50", "action": "Apply heavy Nitrogen top-dressing. Keep weed-free during this vigorous growth stage.", "icon": "fa-leaf"},
        {"phase": "Tasseling & Silking", "duration": "Days 51-75", "action": "Highly sensitive to water stress. Ensure adequate irrigation for proper pollination.", "icon": "fa-fan"},
        {"phase": "Grain Fill & Maturity", "duration": "Days 76-110", "action": "Reduce watering. Harvest when husks dry and kernels dent.", "icon": "fa-tractor"}
    ],
    "cotton": [
        {"phase": "Sowing & Stand Establishment", "duration": "Days 1-30", "action": "Plant in warm, moist soil. Protect young seedlings from early pests.", "icon": "fa-seedling"},
        {"phase": "Vegetative & Squaring", "duration": "Days 31-60", "action": "Begin light irrigation. First flower buds (squares) start to appear.", "icon": "fa-leaf"},
        {"phase": "Flowering & Boll Development", "duration": "Days 61-110", "action": "Peak water and nutrient demand. Frequently scout for bollworms. Do not let soil crack.", "icon": "fa-sun"},
        {"phase": "Boll Opening & Harvest", "duration": "Days 111-150+", "action": "Stop irrigation to encourage uniform boll opening. Pick cotton when dry.", "icon": "fa-tractor"}
    ],
    "coffee": [
        {"phase": "Nursery & Transplanting", "duration": "Months 1-6", "action": "Raise seedlings in shaded nursery. Transplant at start of rainy season.", "icon": "fa-seedling"},
        {"phase": "Vegetative Establishment", "duration": "Years 1-3", "action": "Prune for structure. Establish shade trees. Apply balanced NPK fertilizers regularly.", "icon": "fa-leaf"},
        {"phase": "Flowering & Pinhead", "duration": "Year 3 (Rain Response)", "action": "Blossoms trigger after initial spring rains. Requires dry period prior.", "icon": "fa-sun"},
        {"phase": "Cherry Development & Harvest", "duration": "Year 3-4 (Harvest Season)", "action": "Cherries mature over 7-9 months. Hand-pick only deep red cherries for premium quality.", "icon": "fa-tractor"}
    ],
    "apple": [
        {"phase": "Dormancy & Pruning", "duration": "Winter", "action": "Prune dead wood and shape canopy. Apply dormant oil sprays for overwintering pests.", "icon": "fa-snowflake"},
        {"phase": "Bud Break & Bloom", "duration": "Spring", "action": "Ensure bees are active for pollination. Protect from late spring frosts.", "icon": "fa-seedling"},
        {"phase": "Fruit Set & Development", "duration": "Summer", "action": "Thin excess fruit. Apply irrigation and calcium sprays to prevent bitter pit.", "icon": "fa-apple-alt"},
        {"phase": "Maturation & Harvest", "duration": "Late Summer/Fall", "action": "Harvest when background color turns yellow/green depending on variety.", "icon": "fa-tractor"}
    ],
    # Generalized mapping for other crops to ensure full dictionary coverage without excessive text length
    "default_fruit": [
        {"phase": "Planting/Orchard Setup", "duration": "Year 1", "action": "Prepare pits, add organic manure. Plant saplings and establish irrigation.", "icon": "fa-seedling"},
        {"phase": "Vegetative Growth", "duration": "Years 1-3", "action": "Train canopy, apply balanced NPK, and control weeds.", "icon": "fa-leaf"},
        {"phase": "Flowering", "duration": "Seasonal", "action": "Withhold heavy irrigation to induce flowering. Protect blossoms from pests.", "icon": "fa-sun"},
        {"phase": "Fruiting & Harvest", "duration": "Seasonal", "action": "Resume steady watering. Harvest when fruit reaches optimum color and brix (sugar) levels.", "icon": "fa-tractor"}
    ],
    "default_pulse": [
        {"phase": "Sowing", "duration": "Days 1-15", "action": "Treat seeds with Rhizobium culture. Sow in well-drained soil.", "icon": "fa-seedling"},
        {"phase": "Vegetative", "duration": "Days 16-40", "action": "Requires one light weeding. Very sensitive to water-logging.", "icon": "fa-leaf"},
        {"phase": "Flowering & Pod Formation", "duration": "Days 41-70", "action": "Critical stage for irrigation. Spray mild insecticide if pod borers are spotted.", "icon": "fa-sun"},
        {"phase": "Maturity & Harvest", "duration": "Days 71-100", "action": "Harvest when pods turn brown and leaves dry and drop off completely.", "icon": "fa-tractor"}
    ]
}

# Apply default pulses where specific pulse isn't defined explicitly to save space
pulses = ["chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbean", "blackgram", "lentil"]
for p in pulses:
    if p not in crop_calendar_dict:
        crop_calendar_dict[p] = crop_calendar_dict["default_pulse"]

# Apply default fruits where specific fruit isn't defined explicitly
fruits = ["pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "orange", "papaya", "coconut"]
for f in fruits:
    if f not in crop_calendar_dict:
        crop_calendar_dict[f] = crop_calendar_dict["default_fruit"]

# Apply default cash crop for the remaining
crop_calendar_dict["jute"] = [
    {"phase": "Sowing", "duration": "Days 1-20", "action": "Sow broadcast or in lines. Requires fine seedbed.", "icon": "fa-seedling"},
    {"phase": "Vegetative", "duration": "Days 21-100", "action": "Weed manually. Requires hot and highly humid climate to grow rapidly.", "icon": "fa-leaf"},
    {"phase": "Harvesting", "duration": "Days 101-120", "action": "Harvest at the small pod stage for best fiber quality. Cut close to the ground.", "icon": "fa-tractor"},
    {"phase": "Retting", "duration": "Post-Harvest", "action": "Submerge tied bundles in slow running, clean water to separate fiber.", "icon": "fa-water"}
]

# Vegetable growth calendars
crop_calendar_dict['tomato'] = [
    {"phase": "Nursery & Transplanting", "duration": "Days 1-25", "action": "Sow seeds in nursery trays. Transplant seedlings when 15-20 cm tall into well-prepared beds.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 26-50", "action": "Apply nitrogen fertilizer. Support plants with stakes. Remove suckers to improve air flow.", "icon": "fa-leaf"},
    {"phase": "Flowering & Fruit Set", "duration": "Days 51-75", "action": "Ensure regular watering. Spray calcium solution to prevent blossom end rot. Monitor for pests.", "icon": "fa-sun"},
    {"phase": "Ripening & Harvest", "duration": "Days 76-100", "action": "Harvest when fruits turn red/orange. Pick regularly to encourage further fruiting.", "icon": "fa-tractor"},
]

crop_calendar_dict['potato'] = [
    {"phase": "Land Preparation & Planting", "duration": "Days 1-15", "action": "Prepare well-drained, loose soil. Plant seed tubers 5-8 cm deep in rows.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 16-50", "action": "Earth up soil around plants when 15 cm tall. Apply split doses of nitrogen fertilizer.", "icon": "fa-leaf"},
    {"phase": "Tuber Initiation", "duration": "Days 51-75", "action": "Reduce irrigation slightly. This is the critical tuber bulking stage. Avoid waterlogging.", "icon": "fa-sun"},
    {"phase": "Maturity & Harvest", "duration": "Days 76-100", "action": "Stop watering when leaves turn yellow. Harvest tubers 2 weeks after the vines die back.", "icon": "fa-tractor"},
]

crop_calendar_dict['onion'] = [
    {"phase": "Nursery & Transplanting", "duration": "Days 1-30", "action": "Sow seeds in nursery. Transplant 6-8 week old seedlings 10 cm apart in rows.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 31-60", "action": "Apply nitrogen to boost leafy growth. Keep beds weed-free. Water regularly but avoid excess.", "icon": "fa-leaf"},
    {"phase": "Bulb Development", "duration": "Days 61-90", "action": "Reduce nitrogen and increase potassium. Bulbs swell during this stage. Stop watering towards end.", "icon": "fa-sun"},
    {"phase": "Maturity & Harvest", "duration": "Days 91-120", "action": "Harvest when tops fall over naturally. Cure bulbs in shade for 1-2 weeks before storage.", "icon": "fa-tractor"},
]

crop_calendar_dict['spinach'] = [
    {"phase": "Sowing", "duration": "Days 1-10", "action": "Sow seeds directly in cool, moist soil. Thin seedlings to 5 cm apart once sprouted.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 11-35", "action": "Apply nitrogen top dressing. Water consistently. Spinach grows fast in cool weather.", "icon": "fa-leaf"},
    {"phase": "Leaf Harvest", "duration": "Days 36-55", "action": "Harvest outer leaves progressively. Cut entire plant at soil level when fully mature.", "icon": "fa-tractor"},
]

crop_calendar_dict['cauliflower'] = [
    {"phase": "Nursery & Transplanting", "duration": "Days 1-30", "action": "Raise seedlings in a cool nursery. Transplant 4-5 week old seedlings to the main field.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 31-65", "action": "Apply split doses of nitrogen. Keep soil moist. Protect from cabbage worms.", "icon": "fa-leaf"},
    {"phase": "Curd Formation", "duration": "Days 66-100", "action": "Tie outer leaves over the curd to keep it white. Reduce watering at this stage.", "icon": "fa-sun"},
    {"phase": "Harvest", "duration": "Days 101-130", "action": "Harvest when curds are firm, white, and compact. Cut with a knife, leaving a few leaves.", "icon": "fa-tractor"},
]

crop_calendar_dict['brinjal'] = [
    {"phase": "Nursery & Transplanting", "duration": "Days 1-30", "action": "Sow in nursery beds. Transplant 5-6 week old seedlings when 10-15 cm tall.", "icon": "fa-seedling"},
    {"phase": "Vegetative Growth", "duration": "Days 31-60", "action": "Apply balanced NPK. Prune for 2-3 main branches. Mulch to retain moisture.", "icon": "fa-leaf"},
    {"phase": "Flowering & Fruit Set", "duration": "Days 61-90", "action": "Monitor for shoot borers. Spray neem oil if needed. Support branches with stakes.", "icon": "fa-sun"},
    {"phase": "Harvest", "duration": "Days 91-150", "action": "Harvest when fruits are shiny and full-sized. Do not allow fruits to over-ripen on the plant.", "icon": "fa-tractor"},
]
