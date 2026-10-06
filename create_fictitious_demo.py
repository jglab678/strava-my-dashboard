#!/usr/bin/env python3
"""
Generate a completely fictitious multi-sport demo dataset for the Strava Dashboard.
Sports: Cycling, Running, and Hiking.
Athlete: Alex Rivera (Boulder, Colorado)
Zero personal user data.
"""

import json
import random
from datetime import datetime, timedelta
from collections import defaultdict

def calculate_eddington(daily_dict):
    distances = sorted(list(daily_dict.values()), reverse=True)
    e = 0
    for i, d in enumerate(distances):
        if d >= (i + 1):
            e = i + 1
        else:
            break
    next_e = e + 1
    qualifying_days = sum(1 for d in distances if d >= next_e)
    needed = next_e - qualifying_days
    return e, needed, next_e

def create_fictitious_data():
    athlete = {
        'name': 'Alex Rivera',
        'location': 'Boulder, Colorado',
        'id': '9876543',
        'weight': 68.0
    }

    random.seed(42)  # Deterministic realistic output

    # ----------------------------------------------------
    # 1. CYCLING DEFINITION
    # ----------------------------------------------------
    bikes = [
        'Canyon Endurace CF',
        'Specialized Diverge Gravel',
        'Zwift Hub One'
    ]

    outdoor_cycle_routes = [
        ('Flagstaff Mountain Hill Climb', 32.5, 820.0, 21.4, 210.0, 155.0, 'Canyon Endurace CF'),
        ('Left Hand Canyon & Ward Ascent', 58.2, 1150.0, 23.1, 195.0, 148.0, 'Canyon Endurace CF'),
        ('Peak to Peak Highway Epic', 104.6, 1780.0, 24.2, 205.0, 142.0, 'Canyon Endurace CF'),
        ('Boulder Reservoir Gravel Loop', 44.8, 310.0, 26.5, 175.0, 138.0, 'Specialized Diverge Gravel'),
        ('Fourmile Canyon to Gold Hill', 38.0, 940.0, 19.8, 220.0, 160.0, 'Specialized Diverge Gravel'),
        ('Morgul-Bismarck Road Circuit', 64.0, 680.0, 28.4, 215.0, 152.0, 'Canyon Endurace CF'),
        ('Lookout Mountain Intervals', 48.5, 890.0, 24.8, 225.0, 158.0, 'Canyon Endurace CF'),
        ('Carter Lake Scenic Century', 162.4, 1420.0, 26.1, 190.0, 139.0, 'Canyon Endurace CF'),
        ('Sunshine Canyon Gravel Grinder', 36.2, 880.0, 18.9, 210.0, 156.0, 'Specialized Diverge Gravel'),
        ('Magnolia Road Gravel Sufferfest', 52.0, 1260.0, 19.2, 230.0, 162.0, 'Specialized Diverge Gravel'),
        ('North Boulder Rolling Hills', 51.5, 460.0, 27.8, 185.0, 140.0, 'Canyon Endurace CF'),
        ('Lyons Coffee Ride', 42.0, 320.0, 28.1, 170.0, 135.0, 'Canyon Endurace CF'),
        ('Horsetooth Reservoir Loop', 85.0, 980.0, 26.8, 195.0, 144.0, 'Canyon Endurace CF'),
        ('Gross Reservoir Gravel Cruise', 46.5, 910.0, 20.5, 195.0, 148.0, 'Specialized Diverge Gravel')
    ]

    virtual_cycle_routes = [
        ('Zwift - Watopia Waistband', 28.5, 110.0, 38.4, 220.0, 148.0, 'Zwift Hub One'),
        ('Zwift - Alpe du Zwift Ascent', 21.6, 1045.0, 19.2, 265.0, 168.0, 'Zwift Hub One'),
        ('Zwift - Tempus Fugit TT', 40.2, 65.0, 41.5, 245.0, 155.0, 'Zwift Hub One'),
        ('Zwift - Innsbruck UCI Lap', 34.0, 480.0, 32.1, 230.0, 154.0, 'Zwift Hub One'),
        ('Zwift - Volcano Flat Loops', 25.0, 95.0, 36.8, 205.0, 142.0, 'Zwift Hub One'),
        ('Zwift - Road to Sky Epic', 32.0, 1120.0, 21.0, 255.0, 164.0, 'Zwift Hub One')
    ]

    # ----------------------------------------------------
    # 2. RUNNING DEFINITION
    # ----------------------------------------------------
    shoes = [
        'Nike Pegasus 40',
        'Saucony Endorphin Speed 3',
        'Hoka Speedgoat 5',
        'Brooks Ghost 15'
    ]

    run_templates = [
        ('Boulder Creek Path Easy 8k', 8.2, 45.0, 12.2, 148.0, 'Nike Pegasus 40', 'Run', 'Road'),
        ('Chautauqua Mesa Trail Loop', 11.5, 280.0, 11.1, 162.0, 'Hoka Speedgoat 5', 'Trail Run', 'Trail'),
        ('Sanitas Valley Tempo Run', 7.0, 140.0, 13.3, 168.0, 'Saucony Endorphin Speed 3', 'Run', 'Road'),
        ('Flatirons Vista Rolling 14k', 14.2, 190.0, 11.8, 156.0, 'Brooks Ghost 15', 'Trail Run', 'Trail'),
        ('Magnolia Road High Altitude Long Run', 22.5, 410.0, 11.4, 158.0, 'Hoka Speedgoat 5', 'Trail Run', 'Trail'),
        ('Wonderland Lake Recovery Run', 5.4, 35.0, 10.8, 142.0, 'Brooks Ghost 15', 'Run', 'Road'),
        ('Boulder High Track Intervals 8x800m', 9.2, 15.0, 14.2, 174.0, 'Saucony Endorphin Speed 3', 'Run', 'Road'),
        ('Zwift - Watopia 10k Treadmill', 10.0, 40.0, 12.6, 154.0, 'Nike Pegasus 40', 'Virtual Run', 'Virtual'),
        ('BolderBoulder 10k Classic', 10.0, 65.0, 13.9, 172.0, 'Saucony Endorphin Speed 3', 'Run', 'Road'),
        ('Boulder Backroads Half Marathon', 21.1, 185.0, 12.4, 164.0, 'Saucony Endorphin Speed 3', 'Run', 'Road'),
        ('Ned Gravel & Ridge 30k', 30.5, 720.0, 10.3, 160.0, 'Hoka Speedgoat 5', 'Trail Run', 'Trail'),
        ('Denver Colfax Marathon', 42.2, 210.0, 11.9, 166.0, 'Saucony Endorphin Speed 3', 'Run', 'Road'),
        ('Valmont Park Grass Cross-Country 6k', 6.2, 50.0, 12.0, 152.0, 'Nike Pegasus 40', 'Run', 'Road')
    ]

    # ----------------------------------------------------
    # 3. HIKING & WALKING DEFINITION
    # ----------------------------------------------------
    hiking_gear = [
        'Salomon Quest 4 GTX',
        'Hoka Anacapa Low',
        'Merrell Moab 3',
        'Osprey Talon 22 Pack'
    ]

    hike_templates = [
        ('Bear Peak via Shadow Canyon', 12.8, 890.0, 3.8, 135.0, 'Salomon Quest 4 GTX', 'Hike'),
        ('Mount Sanitas Ridge & Valley Loop', 5.2, 410.0, 3.5, 128.0, 'Hoka Anacapa Low', 'Hike'),
        ('South Boulder Peak Traverse', 14.5, 1040.0, 3.6, 140.0, 'Salomon Quest 4 GTX', 'Hike'),
        ('Royal Arch Trail Adventure', 5.8, 460.0, 3.2, 132.0, 'Hoka Anacapa Low', 'Hike'),
        ('Green Mountain West Ridge Summit', 6.4, 620.0, 3.4, 136.0, 'Salomon Quest 4 GTX', 'Hike'),
        ('Chautauqua First & Second Flatiron', 4.5, 450.0, 2.9, 130.0, 'Merrell Moab 3', 'Hike'),
        ('Mount Bierstadt 14er Summit Expedition', 11.6, 880.0, 3.1, 145.0, 'Salomon Quest 4 GTX', 'Hike'),
        ('Longs Peak Boulder Field Trek', 19.8, 1480.0, 2.8, 148.0, 'Salomon Quest 4 GTX', 'Hike'),
        ('Walker Ranch Loop Canyon Hike', 13.2, 520.0, 4.1, 126.0, 'Hoka Anacapa Low', 'Hike'),
        ('Chautauqua Meadow Sunset Walk', 3.8, 85.0, 4.8, 105.0, 'Merrell Moab 3', 'Walk'),
        ('Boulder Creek Path Leisure Stroll', 5.5, 40.0, 4.9, 98.0, 'Hoka Anacapa Low', 'Walk'),
        ('Wonderland Lake Foothills Walk', 4.2, 30.0, 5.0, 95.0, 'Merrell Moab 3', 'Walk')
    ]

    # Generate dates across 2024, 2025, and 2026 (up to late Sep 2026)
    start_date = datetime(2024, 1, 6, 8, 30)
    end_date = datetime(2026, 9, 28, 10, 0)

    # 1. GENERATE RIDES
    rides = []
    cycle_daily_km = defaultdict(float)
    cycle_daily_mi = defaultdict(float)
    current_dt = start_date
    act_counter = 10001

    while current_dt <= end_date:
        month = current_dt.month
        is_weekend = current_dt.weekday() in (5, 6)
        prob = 0.65 if is_weekend else 0.40
        if month in (6, 7, 8, 9): prob += 0.15
        elif month in (12, 1, 2): prob -= 0.10

        if random.random() < prob:
            if month in (12, 1, 2) or (month in (3, 11) and random.random() < 0.5):
                is_virt = (random.random() < 0.75)
            else:
                is_virt = (random.random() < 0.15)

            if is_virt:
                route = random.choice(virtual_cycle_routes)
                act_type = 'Virtual Ride'
            else:
                route = random.choice(outdoor_cycle_routes)
                act_type = 'Ride'

            name, base_dist, base_elev, base_spd, base_pwr, base_hr, gear = route
            dist_factor = random.uniform(0.92, 1.08)
            km = round(base_dist * dist_factor, 2)
            miles = round(km * 0.621371, 2)
            elev_m = round(base_elev * dist_factor * random.uniform(0.95, 1.05), 1)
            elev_ft = round(elev_m * 3.28084, 1)

            spd_factor = random.uniform(0.95, 1.05)
            speed_kmh = round(base_spd * spd_factor, 1)
            speed_mph = round(speed_kmh * 0.621371, 1)

            time_hours = km / speed_kmh
            time_s = int(round(time_hours * 3600))

            watts = round(base_pwr * random.uniform(0.94, 1.06), 1)
            hr = round(base_hr * random.uniform(0.96, 1.04), 1)
            cals = int(round(time_hours * watts * 3.6 * 0.95))

            day_str = current_dt.strftime('%Y-%m-%d')
            cycle_daily_km[day_str] += km
            cycle_daily_mi[day_str] += miles

            rides.append({
                'id': str(act_counter),
                'name': name,
                'date': current_dt.strftime('%Y-%m-%d %H:%M'),
                'timestamp': int(current_dt.timestamp() * 1000),
                'day': day_str,
                'year': current_dt.year,
                'month': current_dt.month,
                'day_of_week': current_dt.weekday(),
                'day_of_year': current_dt.timetuple().tm_yday,
                'type': act_type,
                'is_virtual': (act_type == 'Virtual Ride'),
                'is_commute': False,
                'dist_km': km,
                'dist_mi': miles,
                'elev_m': elev_m,
                'elev_ft': elev_ft,
                'time_s': time_s,
                'speed_kmh': speed_kmh,
                'speed_mph': speed_mph,
                'watts': watts,
                'hr': hr,
                'cals': cals,
                'gear': gear
            })
            act_counter += 1

        step_days = random.choices([1, 2, 3], weights=[0.45, 0.40, 0.15])[0]
        current_dt += timedelta(days=step_days, hours=random.randint(-1, 2))

    # 2. GENERATE RUNS
    runs = []
    run_daily_km = defaultdict(float)
    run_daily_mi = defaultdict(float)
    current_dt = datetime(2024, 1, 7, 7, 15)

    while current_dt <= end_date:
        month = current_dt.month
        is_weekend = current_dt.weekday() in (5, 6)
        prob = 0.50 if is_weekend else 0.35
        if month in (4, 5, 9, 10): prob += 0.15

        if random.random() < prob:
            tmpl = random.choice(run_templates)
            name, base_dist, base_elev, base_spd, base_hr, shoe, act_type, surface = tmpl

            dist_factor = random.uniform(0.94, 1.06)
            km = round(base_dist * dist_factor, 2)
            miles = round(km * 0.621371, 2)
            elev_m = round(base_elev * dist_factor * random.uniform(0.95, 1.05), 1)
            elev_ft = round(elev_m * 3.28084, 1)

            spd_factor = random.uniform(0.96, 1.04)
            speed_kmh = round(base_spd * spd_factor, 1)
            speed_mph = round(speed_kmh * 0.621371, 1)

            time_hours = km / speed_kmh
            time_s = int(round(time_hours * 3600))

            # Running pace (seconds per km and per mile)
            pace_sec_km = int(round(time_s / km)) if km > 0 else 0
            pace_sec_mi = int(round(time_s / miles)) if miles > 0 else 0
            pace_km_str = f"{pace_sec_km // 60}:{pace_sec_km % 60:02d}"
            pace_mi_str = f"{pace_sec_mi // 60}:{pace_sec_mi % 60:02d}"

            hr = round(base_hr * random.uniform(0.96, 1.04), 1)
            cals = int(round(km * 68.0 * 1.036)) # Runner formula based on weight

            day_str = current_dt.strftime('%Y-%m-%d')
            run_daily_km[day_str] += km
            run_daily_mi[day_str] += miles

            runs.append({
                'id': str(act_counter),
                'name': name,
                'date': current_dt.strftime('%Y-%m-%d %H:%M'),
                'timestamp': int(current_dt.timestamp() * 1000),
                'day': day_str,
                'year': current_dt.year,
                'month': current_dt.month,
                'day_of_week': current_dt.weekday(),
                'day_of_year': current_dt.timetuple().tm_yday,
                'type': act_type,
                'surface': surface,
                'is_virtual': (act_type == 'Virtual Run'),
                'is_trail': (act_type == 'Trail Run'),
                'dist_km': km,
                'dist_mi': miles,
                'elev_m': elev_m,
                'elev_ft': elev_ft,
                'time_s': time_s,
                'speed_kmh': speed_kmh,
                'speed_mph': speed_mph,
                'pace_km_str': pace_km_str,
                'pace_mi_str': pace_mi_str,
                'pace_sec_km': pace_sec_km,
                'pace_sec_mi': pace_sec_mi,
                'hr': hr,
                'cadence': random.randint(166, 178),
                'cals': cals,
                'gear': shoe
            })
            act_counter += 1

        step_days = random.choices([2, 3, 4], weights=[0.40, 0.45, 0.15])[0]
        current_dt += timedelta(days=step_days, hours=random.randint(-1, 2))

    # 3. GENERATE HIKES & WALKS
    hikes = []
    current_dt = datetime(2024, 1, 13, 9, 0)

    while current_dt <= end_date:
        month = current_dt.month
        is_weekend = current_dt.weekday() in (5, 6)
        prob = 0.40 if is_weekend else 0.20
        if month in (6, 7, 8, 9, 10): prob += 0.20 # Peak mountain hiking season

        if random.random() < prob:
            tmpl = random.choice(hike_templates)
            name, base_dist, base_elev, base_spd, base_hr, gear, act_type = tmpl

            dist_factor = random.uniform(0.95, 1.05)
            km = round(base_dist * dist_factor, 2)
            miles = round(km * 0.621371, 2)
            elev_m = round(base_elev * dist_factor * random.uniform(0.96, 1.04), 1)
            elev_ft = round(elev_m * 3.28084, 1)

            spd_factor = random.uniform(0.95, 1.05)
            speed_kmh = round(base_spd * spd_factor, 1)
            speed_mph = round(speed_kmh * 0.621371, 1)

            time_hours = km / speed_kmh
            time_s = int(round(time_hours * 3600))

            # Vertical ascent rate (m/hr and ft/hr)
            vert_rate_m_hr = round(elev_m / time_hours, 1) if time_hours > 0 else 0.0
            vert_rate_ft_hr = round(vert_rate_m_hr * 3.28084, 1)

            # Climbing ratio (m/km and ft/mi)
            climb_ratio_m_km = round(elev_m / km, 1) if km > 0 else 0.0
            climb_ratio_ft_mi = round(elev_ft / miles, 1) if miles > 0 else 0.0

            hr = round(base_hr * random.uniform(0.95, 1.05), 1)
            cals = int(round(time_hours * (380 if act_type == 'Hike' else 250)))

            day_str = current_dt.strftime('%Y-%m-%d')

            hikes.append({
                'id': str(act_counter),
                'name': name,
                'date': current_dt.strftime('%Y-%m-%d %H:%M'),
                'timestamp': int(current_dt.timestamp() * 1000),
                'day': day_str,
                'year': current_dt.year,
                'month': current_dt.month,
                'day_of_week': current_dt.weekday(),
                'day_of_year': current_dt.timetuple().tm_yday,
                'type': act_type,
                'dist_km': km,
                'dist_mi': miles,
                'elev_m': elev_m,
                'elev_ft': elev_ft,
                'time_s': time_s,
                'speed_kmh': speed_kmh,
                'speed_mph': speed_mph,
                'vert_rate_m_hr': vert_rate_m_hr,
                'vert_rate_ft_hr': vert_rate_ft_hr,
                'climb_ratio_m_km': climb_ratio_m_km,
                'climb_ratio_ft_mi': climb_ratio_ft_mi,
                'hr': hr,
                'cals': cals,
                'gear': gear
            })
            act_counter += 1

        step_days = random.choices([4, 5, 7], weights=[0.40, 0.40, 0.20])[0]
        current_dt += timedelta(days=step_days, hours=random.randint(-1, 2))

    rides.sort(key=lambda r: r['date'])
    runs.sort(key=lambda r: r['date'])
    hikes.sort(key=lambda r: r['date'])

    return athlete, rides, cycle_daily_km, cycle_daily_mi, runs, run_daily_km, run_daily_mi, hikes

# -------------------------------------------------------------------
# AGGREGATION & STATISTICS HELPERS
# -------------------------------------------------------------------
def build_cycling_statistics(rides, daily_dist_km, daily_dist_mi):
    total_rides = len(rides)
    eddington_km, eddington_km_needed, next_e_km = calculate_eddington(daily_dist_km)
    eddington_mi, eddington_mi_needed, next_e_mi = calculate_eddington(daily_dist_mi)

    longest_dist_ride = max(rides, key=lambda r: r['dist_km'])
    highest_elev_ride = max(rides, key=lambda r: r['elev_m'])
    longest_time_ride = max(rides, key=lambda r: r['time_s'])

    substantive_rides = [r for r in rides if r['dist_km'] >= 25.0]
    fastest_ride = max(substantive_rides, key=lambda r: r['speed_kmh']) if substantive_rides else max(rides, key=lambda r: r['speed_kmh'])
    power_rides = [r for r in rides if r['watts'] > 0 and r['dist_km'] >= 15.0]
    highest_power_ride = max(power_rides, key=lambda r: r['watts']) if power_rides else None

    half_centuries_km = sum(1 for r in rides if r['dist_km'] >= 50.0)
    metric_centuries = sum(1 for r in rides if r['dist_km'] >= 100.0)
    imperial_centuries = sum(1 for r in rides if r['dist_km'] >= 160.934)
    double_centuries = sum(1 for r in rides if r['dist_km'] >= 200.0)

    all_years = sorted(list(set(r['year'] for r in rides)), reverse=True)

    cumulative_curves = {}
    cumulative_elev_curves = {}
    for y in all_years:
        y_rides = [r for r in rides if r['year'] == y]
        day_dists = defaultdict(float)
        day_elevs = defaultdict(float)
        for r in y_rides:
            day_dists[r['day_of_year']] += r['dist_km']
            day_elevs[r['day_of_year']] += r['elev_m']
        max_doy = 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365
        if y == 2026: max_doy = max(r['day_of_year'] for r in y_rides)
        running_km = 0.0
        running_elev = 0.0
        curve_km = []
        curve_elev = []
        for d in range(1, max_doy + 1):
            running_km += day_dists[d]
            running_elev += day_elevs[d]
            curve_km.append(round(running_km, 1))
            curve_elev.append(round(running_elev, 1))
        cumulative_curves[str(y)] = curve_km
        cumulative_elev_curves[str(y)] = curve_elev

    years_data = {}
    for y in all_years:
        y_rides = [r for r in rides if r['year'] == y]
        t_dist = sum(r['dist_km'] for r in y_rides)
        t_elev = sum(r['elev_m'] for r in y_rides)
        t_time = sum(r['time_s'] for r in y_rides)
        t_cals = sum(r['cals'] for r in y_rides)
        out_rides = sum(1 for r in y_rides if not r['is_virtual'])
        virt_rides = sum(1 for r in y_rides if r['is_virtual'])
        out_km = sum(r['dist_km'] for r in y_rides if not r['is_virtual'])
        virt_km = sum(r['dist_km'] for r in y_rides if r['is_virtual'])

        m_dist = [0.0] * 12
        m_elev = [0.0] * 12
        m_count = [0] * 12
        for r in y_rides:
            idx = r['month'] - 1
            m_dist[idx] += r['dist_km']
            m_elev[idx] += r['elev_m']
            m_count[idx] += 1

        weighted_spd = sum(r['speed_kmh'] * r['time_s'] for r in y_rides) / t_time if t_time > 0 else 0.0

        years_data[str(y)] = {
            'year': y,
            'rides': len(y_rides),
            'outdoor_rides': out_rides,
            'virtual_rides': virt_rides,
            'dist_km': round(t_dist, 1),
            'dist_mi': round(t_dist * 0.621371, 1),
            'outdoor_dist_km': round(out_km, 1),
            'virtual_dist_km': round(virt_km, 1),
            'elev_m': round(t_elev, 1),
            'elev_ft': round(t_elev * 3.28084, 1),
            'time_s': t_time,
            'time_hrs': round(t_time / 3600.0, 1),
            'avg_speed_kmh': round(weighted_spd, 1),
            'avg_speed_mph': round(weighted_spd * 0.621371, 1),
            'avg_dist_km': round(t_dist / len(y_rides), 1) if y_rides else 0,
            'avg_dist_mi': round((t_dist / len(y_rides)) * 0.621371, 1) if y_rides else 0,
            'avg_elev_m': round(t_elev / len(y_rides), 1) if y_rides else 0,
            'climbing_ratio_m_km': round(t_elev / t_dist, 1) if t_dist > 0 else 0,
            'cals': t_cals,
            'monthly_dist_km': [round(x, 1) for x in m_dist],
            'monthly_dist_mi': [round(x * 0.621371, 1) for x in m_dist],
            'monthly_elev_m': [round(x, 1) for x in m_elev],
            'monthly_rides': m_count,
            'centuries_100k': sum(1 for r in y_rides if r['dist_km'] >= 100.0),
            'centuries_100m': sum(1 for r in y_rides if r['dist_km'] >= 160.934),
            'longest_ride': max(y_rides, key=lambda r: r['dist_km']),
            'biggest_climb': max(y_rides, key=lambda r: r['elev_m'])
        }

    gear_dict = defaultdict(lambda: {'rides': 0, 'dist_km': 0.0, 'elev_m': 0.0, 'time_s': 0})
    for r in rides:
        g = r['gear']
        gear_dict[g]['rides'] += 1
        gear_dict[g]['dist_km'] += r['dist_km']
        gear_dict[g]['elev_m'] += r['elev_m']
        gear_dict[g]['time_s'] += r['time_s']

    total_dist_km = sum(r['dist_km'] for r in rides)
    gear_list = []
    for g, stats in sorted(gear_dict.items(), key=lambda x: x[1]['dist_km'], reverse=True):
        gear_list.append({
            'name': g,
            'rides': stats['rides'],
            'dist_km': round(stats['dist_km'], 1),
            'dist_mi': round(stats['dist_km'] * 0.621371, 1),
            'elev_m': round(stats['elev_m'], 1),
            'elev_ft': round(stats['elev_m'] * 3.28084, 1),
            'time_hrs': round(stats['time_s'] / 3600.0, 1),
            'avg_speed_kmh': round((stats['dist_km'] / (stats['time_s'] / 3600.0)), 1) if stats['time_s'] > 0 else 0,
            'avg_speed_mph': round(((stats['dist_km'] / (stats['time_s'] / 3600.0)) * 0.621371), 1) if stats['time_s'] > 0 else 0,
            'share_pct': round((stats['dist_km'] / total_dist_km) * 100.0, 1) if total_dist_km > 0 else 0
        })

    dow_counts = [0] * 7
    dow_km = [0.0] * 7
    for r in rides:
        dow_counts[r['day_of_week']] += 1
        dow_km[r['day_of_week']] += r['dist_km']

    dist_buckets_km = [
        sum(1 for r in rides if r['dist_km'] < 25.0),
        sum(1 for r in rides if 25.0 <= r['dist_km'] < 50.0),
        sum(1 for r in rides if 50.0 <= r['dist_km'] < 80.0),
        sum(1 for r in rides if 80.0 <= r['dist_km'] < 100.0),
        sum(1 for r in rides if 100.0 <= r['dist_km'] < 160.0),
        sum(1 for r in rides if r['dist_km'] >= 160.0)
    ]

    total_time_s = sum(r['time_s'] for r in rides)
    total_elev_m = sum(r['elev_m'] for r in rides)

    return {
        'total_rides': total_rides,
        'unique_days': len(set(r['day'] for r in rides)),
        'eddington': {
            'km': eddington_km,
            'km_needed': eddington_km_needed,
            'km_next': next_e_km,
            'mi': eddington_mi,
            'mi_needed': eddington_mi_needed,
            'mi_next': next_e_mi
        },
        'centuries': {
            'half_km': half_centuries_km,
            'metric_100k': metric_centuries,
            'imperial_100m': imperial_centuries,
            'double_200k': double_centuries
        },
        'trophies': {
            'longest_dist': longest_dist_ride,
            'highest_elev': highest_elev_ride,
            'longest_time': longest_time_ride,
            'fastest_ride': fastest_ride,
            'highest_power': highest_power_ride
        },
        'lifetime': {
            'dist_km': round(total_dist_km, 1),
            'dist_mi': round(total_dist_km * 0.621371, 1),
            'elev_m': round(total_elev_m, 1),
            'elev_ft': round(total_elev_m * 3.28084, 1),
            'time_s': total_time_s,
            'time_hrs': round(total_time_s / 3600.0, 1),
            'time_days': round(total_time_s / 86400.0, 1),
            'cals': sum(r['cals'] for r in rides),
            'earth_laps': round(total_dist_km / 40075.0, 2),
            'everests': round(total_elev_m / 8848.86, 1),
            'climbing_ratio_m_km': round(total_elev_m / total_dist_km, 1) if total_dist_km > 0 else 0,
            'outdoor_rides': sum(1 for r in rides if not r['is_virtual']),
            'virtual_rides': sum(1 for r in rides if r['is_virtual']),
            'outdoor_dist_km': round(sum(r['dist_km'] for r in rides if not r['is_virtual']), 1),
            'virtual_dist_km': round(sum(r['dist_km'] for r in rides if r['is_virtual']), 1),
            'avg_speed_kmh': round((total_dist_km / (total_time_s / 3600.0)), 1) if total_time_s > 0 else 0,
            'avg_speed_mph': round(((total_dist_km / (total_time_s / 3600.0)) * 0.621371), 1) if total_time_s > 0 else 0,
            'avg_dist_km': round(total_dist_km / total_rides, 1) if total_rides else 0,
            'avg_dist_mi': round((total_dist_km / total_rides) * 0.621371, 1) if total_rides else 0,
        },
        'years': years_data,
        'all_years': all_years,
        'cumulative_curves': cumulative_curves,
        'cumulative_distance_curves': cumulative_curves,
        'cumulative_elev_curves': cumulative_elev_curves,
        'gear': gear_list,
        'habits': {
            'dow_counts': dow_counts,
            'dow_km': [round(x, 1) for x in dow_km],
            'dist_buckets_km': dist_buckets_km,
        },
        'rides_sample': rides
    }

def build_running_statistics(runs, daily_dist_km, daily_dist_mi):
    total_runs = len(runs)
    eddington_km, eddington_km_needed, next_e_km = calculate_eddington(daily_dist_km)
    eddington_mi, eddington_mi_needed, next_e_mi = calculate_eddington(daily_dist_mi)

    longest_dist_run = max(runs, key=lambda r: r['dist_km'])
    highest_elev_run = max(runs, key=lambda r: r['elev_m'])
    longest_time_run = max(runs, key=lambda r: r['time_s'])

    # Fastest run over at least 5km
    substantive_runs = [r for r in runs if r['dist_km'] >= 5.0]
    fastest_run = min(substantive_runs, key=lambda r: r['pace_sec_km']) if substantive_runs else min(runs, key=lambda r: r['pace_sec_km'])

    # Running distance milestones
    c_5k = sum(1 for r in runs if r['dist_km'] >= 5.0)
    c_10k = sum(1 for r in runs if r['dist_km'] >= 10.0)
    c_half = sum(1 for r in runs if r['dist_km'] >= 21.0975)
    c_full = sum(1 for r in runs if r['dist_km'] >= 42.195)
    c_ultra = sum(1 for r in runs if r['dist_km'] >= 50.0)

    all_years = sorted(list(set(r['year'] for r in runs)), reverse=True)

    cumulative_curves = {}
    cumulative_elev_curves = {}
    for y in all_years:
        y_runs = [r for r in runs if r['year'] == y]
        day_dists = defaultdict(float)
        day_elevs = defaultdict(float)
        for r in y_runs:
            day_dists[r['day_of_year']] += r['dist_km']
            day_elevs[r['day_of_year']] += r['elev_m']
        max_doy = 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365
        if y == 2026: max_doy = max(r['day_of_year'] for r in y_runs)
        running_km = 0.0
        running_elev = 0.0
        curve_km = []
        curve_elev = []
        for d in range(1, max_doy + 1):
            running_km += day_dists[d]
            running_elev += day_elevs[d]
            curve_km.append(round(running_km, 1))
            curve_elev.append(round(running_elev, 1))
        cumulative_curves[str(y)] = curve_km
        cumulative_elev_curves[str(y)] = curve_elev

    total_dist_km = sum(r['dist_km'] for r in runs)
    total_elev_m = sum(r['elev_m'] for r in runs)
    total_time_s = sum(r['time_s'] for r in runs)
    total_cals = sum(r['cals'] for r in runs)

    avg_pace_sec_km = int(round(total_time_s / total_dist_km)) if total_dist_km > 0 else 0
    avg_pace_sec_mi = int(round(total_time_s / (total_dist_km * 0.621371))) if total_dist_km > 0 else 0

    years_data = {}
    for y in all_years:
        y_runs = [r for r in runs if r['year'] == y]
        t_dist = sum(r['dist_km'] for r in y_runs)
        t_elev = sum(r['elev_m'] for r in y_runs)
        t_time = sum(r['time_s'] for r in y_runs)
        t_cals = sum(r['cals'] for r in y_runs)
        road_runs = sum(1 for r in y_runs if r['surface'] == 'Road')
        trail_runs = sum(1 for r in y_runs if r['surface'] == 'Trail')
        virt_runs = sum(1 for r in y_runs if r['surface'] == 'Virtual')

        m_dist = [0.0] * 12
        m_elev = [0.0] * 12
        m_count = [0] * 12
        for r in y_runs:
            idx = r['month'] - 1
            m_dist[idx] += r['dist_km']
            m_elev[idx] += r['elev_m']
            m_count[idx] += 1

        y_pace_sec_km = int(round(t_time / t_dist)) if t_dist > 0 else 0
        y_pace_sec_mi = int(round(t_time / (t_dist * 0.621371))) if t_dist > 0 else 0

        years_data[str(y)] = {
            'year': y,
            'runs': len(y_runs),
            'road_runs': road_runs,
            'trail_runs': trail_runs,
            'virtual_runs': virt_runs,
            'dist_km': round(t_dist, 1),
            'dist_mi': round(t_dist * 0.621371, 1),
            'elev_m': round(t_elev, 1),
            'elev_ft': round(t_elev * 3.28084, 1),
            'time_s': t_time,
            'time_hrs': round(t_time / 3600.0, 1),
            'avg_pace_km': f"{y_pace_sec_km // 60}:{y_pace_sec_km % 60:02d}",
            'avg_pace_mi': f"{y_pace_sec_mi // 60}:{y_pace_sec_mi % 60:02d}",
            'avg_dist_km': round(t_dist / len(y_runs), 1) if y_runs else 0,
            'avg_dist_mi': round((t_dist / len(y_runs)) * 0.621371, 1) if y_runs else 0,
            'cals': t_cals,
            'climbing_ratio_m_km': round(t_elev / t_dist, 1) if t_dist > 0 else 0.0,
            'monthly_dist_km': [round(x, 1) for x in m_dist],
            'monthly_dist_mi': [round(x * 0.621371, 1) for x in m_dist],
            'monthly_elev_m': [round(x, 1) for x in m_elev],
            'monthly_runs': m_count,
            'c_5k': sum(1 for r in y_runs if r['dist_km'] >= 5.0),
            'c_10k': sum(1 for r in y_runs if r['dist_km'] >= 10.0),
            'c_half': sum(1 for r in y_runs if r['dist_km'] >= 21.0975),
            'c_full': sum(1 for r in y_runs if r['dist_km'] >= 42.195),
            'longest_run': max(y_runs, key=lambda r: r['dist_km']),
            'fastest_run': min(y_runs, key=lambda r: r['pace_sec_km'])
        }

    shoe_dict = defaultdict(lambda: {'runs': 0, 'dist_km': 0.0, 'elev_m': 0.0, 'time_s': 0})
    for r in runs:
        s = r['gear']
        shoe_dict[s]['runs'] += 1
        shoe_dict[s]['dist_km'] += r['dist_km']
        shoe_dict[s]['elev_m'] += r['elev_m']
        shoe_dict[s]['time_s'] += r['time_s']

    shoe_list = []
    # Standard 700km lifespan benchmark
    for s, stats in sorted(shoe_dict.items(), key=lambda x: x[1]['dist_km'], reverse=True):
        km_val = stats['dist_km']
        wear_pct = min(100.0, round((km_val / 700.0) * 100.0, 1))
        pace_sec = int(round(stats['time_s'] / km_val)) if km_val > 0 else 0
        shoe_list.append({
            'name': s,
            'runs': stats['runs'],
            'dist_km': round(km_val, 1),
            'dist_mi': round(km_val * 0.621371, 1),
            'elev_m': round(stats['elev_m'], 1),
            'elev_ft': round(stats['elev_m'] * 3.28084, 1),
            'time_hrs': round(stats['time_s'] / 3600.0, 1),
            'avg_pace_km': f"{pace_sec // 60}:{pace_sec % 60:02d}",
            'avg_pace_mi': f"{int(round(pace_sec * 1.60934)) // 60}:{int(round(pace_sec * 1.60934)) % 60:02d}",
            'share_pct': round((km_val / total_dist_km) * 100.0, 1) if total_dist_km > 0 else 0,
            'wear_pct': wear_pct
        })

    dow_counts = [0] * 7
    dow_km = [0.0] * 7
    for r in runs:
        dow_counts[r['day_of_week']] += 1
        dow_km[r['day_of_week']] += r['dist_km']

    dist_buckets_km = [
        sum(1 for r in runs if r['dist_km'] < 5.0),
        sum(1 for r in runs if 5.0 <= r['dist_km'] < 10.0),
        sum(1 for r in runs if 10.0 <= r['dist_km'] < 21.0),
        sum(1 for r in runs if 21.0 <= r['dist_km'] < 30.0),
        sum(1 for r in runs if 30.0 <= r['dist_km'] < 42.0),
        sum(1 for r in runs if r['dist_km'] >= 42.0)
    ]

    return {
        'total_runs': total_runs,
        'unique_days': len(set(r['day'] for r in runs)),
        'eddington': {
            'km': eddington_km,
            'km_needed': eddington_km_needed,
            'km_next': next_e_km,
            'mi': eddington_mi,
            'mi_needed': eddington_mi_needed,
            'mi_next': next_e_mi
        },
        'milestones': {
            'c_5k': c_5k,
            'c_10k': c_10k,
            'c_half': c_half,
            'c_full': c_full,
            'c_ultra': c_ultra
        },
        'trophies': {
            'longest_dist': longest_dist_run,
            'highest_elev': highest_elev_run,
            'longest_time': longest_time_run,
            'fastest_run': fastest_run
        },
        'lifetime': {
            'dist_km': round(total_dist_km, 1),
            'dist_mi': round(total_dist_km * 0.621371, 1),
            'elev_m': round(total_elev_m, 1),
            'elev_ft': round(total_elev_m * 3.28084, 1),
            'time_s': total_time_s,
            'time_hrs': round(total_time_s / 3600.0, 1),
            'time_days': round(total_time_s / 86400.0, 1),
            'avg_pace_km': f"{avg_pace_sec_km // 60}:{avg_pace_sec_km % 60:02d}",
            'avg_pace_mi': f"{avg_pace_sec_mi // 60}:{avg_pace_sec_mi % 60:02d}",
            'avg_dist_km': round(total_dist_km / total_runs, 1) if total_runs else 0,
            'avg_dist_mi': round((total_dist_km / total_runs) * 0.621371, 1) if total_runs else 0,
            'cals': total_cals,
            'earth_laps': round(total_dist_km / 40075.0, 3),
            'marathons_equiv': round(total_dist_km / 42.195, 1),
            'road_runs': sum(1 for r in runs if r['surface'] == 'Road'),
            'trail_runs': sum(1 for r in runs if r['surface'] == 'Trail'),
            'virtual_runs': sum(1 for r in runs if r['surface'] == 'Virtual')
        },
        'years': years_data,
        'all_years': all_years,
        'cumulative_curves': cumulative_curves,
        'cumulative_distance_curves': cumulative_curves,
        'cumulative_elev_curves': cumulative_elev_curves,
        'gear': shoe_list,
        'habits': {
            'dow_counts': dow_counts,
            'dow_km': [round(x, 1) for x in dow_km],
            'dist_buckets_km': dist_buckets_km,
        },
        'runs_sample': runs
    }

def build_hiking_statistics(hikes):
    total_hikes = len(hikes)
    total_dist_km = sum(h['dist_km'] for h in hikes)
    total_elev_m = sum(h['elev_m'] for h in hikes)
    total_time_s = sum(h['time_s'] for h in hikes)
    total_cals = sum(h['cals'] for h in hikes)

    longest_dist_hike = max(hikes, key=lambda h: h['dist_km'])
    highest_elev_hike = max(hikes, key=lambda h: h['elev_m'])
    longest_time_hike = max(hikes, key=lambda h: h['time_s'])
    steepest_hike = max(hikes, key=lambda h: h['climb_ratio_m_km'])

    # Peak Vert Milestones
    climbs_500m = sum(1 for h in hikes if h['elev_m'] >= 500.0)
    climbs_1000m = sum(1 for h in hikes if h['elev_m'] >= 1000.0)
    climbs_1500m = sum(1 for h in hikes if h['elev_m'] >= 1400.0) # Alpine summits
    long_treks = sum(1 for h in hikes if h['dist_km'] >= 15.0)

    time_hrs = total_time_s / 3600.0 if total_time_s > 0 else 1.0
    vert_rate_m_hr = round(total_elev_m / time_hrs, 1)
    vert_rate_ft_hr = round(vert_rate_m_hr * 3.28084, 1)
    climb_ratio_m_km = round(total_elev_m / total_dist_km, 1) if total_dist_km > 0 else 0.0
    climb_ratio_ft_mi = round((total_elev_m * 3.28084) / (total_dist_km * 0.621371), 1) if total_dist_km > 0 else 0.0

    all_years = sorted(list(set(h['year'] for h in hikes)), reverse=True)

    # Cumulative Elevation & Distance curves (Day 1-365)
    cumulative_elev_curves = {}
    cumulative_distance_curves = {}
    for y in all_years:
        y_hikes = [h for h in hikes if h['year'] == y]
        day_elevs = defaultdict(float)
        day_dists = defaultdict(float)
        for h in y_hikes:
            day_elevs[h['day_of_year']] += h['elev_m']
            day_dists[h['day_of_year']] += h['dist_km']
        max_doy = 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365
        if y == 2026: max_doy = max(h['day_of_year'] for h in y_hikes)
        running_elev = 0.0
        running_dist = 0.0
        curve_elev = []
        curve_dist = []
        for d in range(1, max_doy + 1):
            running_elev += day_elevs[d]
            running_dist += day_dists[d]
            curve_elev.append(round(running_elev, 1))
            curve_dist.append(round(running_dist, 1))
        cumulative_elev_curves[str(y)] = curve_elev
        cumulative_distance_curves[str(y)] = curve_dist

    years_data = {}
    for y in all_years:
        y_hikes = [h for h in hikes if h['year'] == y]
        t_dist = sum(h['dist_km'] for h in y_hikes)
        t_elev = sum(h['elev_m'] for h in y_hikes)
        t_time = sum(h['time_s'] for h in y_hikes)
        t_cals = sum(h['cals'] for h in y_hikes)
        hike_only = sum(1 for h in y_hikes if h['type'] == 'Hike')
        walk_only = sum(1 for h in y_hikes if h['type'] == 'Walk')

        m_elev = [0.0] * 12
        m_dist = [0.0] * 12
        m_count = [0] * 12
        for h in y_hikes:
            idx = h['month'] - 1
            m_elev[idx] += h['elev_m']
            m_dist[idx] += h['dist_km']
            m_count[idx] += 1

        y_hrs = t_time / 3600.0 if t_time > 0 else 1.0
        years_data[str(y)] = {
            'year': y,
            'hikes': len(y_hikes),
            'hike_count': hike_only,
            'walk_count': walk_only,
            'dist_km': round(t_dist, 1),
            'dist_mi': round(t_dist * 0.621371, 1),
            'elev_m': round(t_elev, 1),
            'elev_ft': round(t_elev * 3.28084, 1),
            'time_s': t_time,
            'time_hrs': round(y_hrs, 1),
            'vert_rate_m_hr': round(t_elev / y_hrs, 1) if y_hrs > 0 else 0,
            'vert_rate_ft_hr': round((t_elev / y_hrs) * 3.28084, 1) if y_hrs > 0 else 0,
            'climb_ratio_m_km': round(t_elev / t_dist, 1) if t_dist > 0 else 0,
            'cals': t_cals,
            'monthly_elev_m': [round(x, 1) for x in m_elev],
            'monthly_elev_ft': [round(x * 3.28084, 1) for x in m_elev],
            'monthly_dist_km': [round(x, 1) for x in m_dist],
            'monthly_dist_mi': [round(x * 0.621371, 1) for x in m_dist],
            'monthly_hikes': m_count,
            'longest_hike': max(y_hikes, key=lambda h: h['dist_km']),
            'biggest_climb': max(y_hikes, key=lambda h: h['elev_m'])
        }

    gear_dict = defaultdict(lambda: {'hikes': 0, 'dist_km': 0.0, 'elev_m': 0.0, 'time_s': 0})
    for h in hikes:
        g = h['gear']
        gear_dict[g]['hikes'] += 1
        gear_dict[g]['dist_km'] += h['dist_km']
        gear_dict[g]['elev_m'] += h['elev_m']
        gear_dict[g]['time_s'] += h['time_s']

    gear_list = []
    for g, stats in sorted(gear_dict.items(), key=lambda x: x[1]['elev_m'], reverse=True):
        gear_list.append({
            'name': g,
            'hikes': stats['hikes'],
            'dist_km': round(stats['dist_km'], 1),
            'dist_mi': round(stats['dist_km'] * 0.621371, 1),
            'elev_m': round(stats['elev_m'], 1),
            'elev_ft': round(stats['elev_m'] * 3.28084, 1),
            'time_hrs': round(stats['time_s'] / 3600.0, 1),
            'share_pct': round((stats['elev_m'] / total_elev_m) * 100.0, 1) if total_elev_m > 0 else 0
        })

    dow_counts = [0] * 7
    dow_elev = [0.0] * 7
    for h in hikes:
        dow_counts[h['day_of_week']] += 1
        dow_elev[h['day_of_week']] += h['elev_m']

    elev_buckets_m = [
        sum(1 for h in hikes if h['elev_m'] < 200.0),
        sum(1 for h in hikes if 200.0 <= h['elev_m'] < 500.0),
        sum(1 for h in hikes if 500.0 <= h['elev_m'] < 800.0),
        sum(1 for h in hikes if 800.0 <= h['elev_m'] < 1200.0),
        sum(1 for h in hikes if h['elev_m'] >= 1200.0)
    ]

    return {
        'total_hikes': total_hikes,
        'unique_days': len(set(h['day'] for h in hikes)),
        'hike_count': sum(1 for h in hikes if h['type'] == 'Hike'),
        'walk_count': sum(1 for h in hikes if h['type'] == 'Walk'),
        'milestones': {
            'climbs_500m': climbs_500m,
            'climbs_1000m': climbs_1000m,
            'climbs_1500m': climbs_1500m,
            'long_treks': long_treks
        },
        'trophies': {
            'highest_elev': highest_elev_hike,
            'longest_dist': longest_dist_hike,
            'longest_time': longest_time_hike,
            'steepest_hike': steepest_hike
        },
        'lifetime': {
            'elev_m': round(total_elev_m, 1),
            'elev_ft': round(total_elev_m * 3.28084, 1),
            'dist_km': round(total_dist_km, 1),
            'dist_mi': round(total_dist_km * 0.621371, 1),
            'time_s': total_time_s,
            'time_hrs': round(time_hrs, 1),
            'time_days': round(total_time_s / 86400.0, 1),
            'vert_rate_m_hr': vert_rate_m_hr,
            'vert_rate_ft_hr': vert_rate_ft_hr,
            'climb_ratio_m_km': climb_ratio_m_km,
            'climb_ratio_ft_mi': climb_ratio_ft_mi,
            'everests': round(total_elev_m / 8848.86, 1),
            'cals': total_cals,
            'avg_elev_m': round(total_elev_m / total_hikes, 1) if total_hikes else 0,
            'avg_elev_ft': round((total_elev_m * 3.28084) / total_hikes, 1) if total_hikes else 0,
            'avg_dist_km': round(total_dist_km / total_hikes, 1) if total_hikes else 0,
            'avg_dist_mi': round((total_dist_km / total_hikes) * 0.621371, 1) if total_hikes else 0
        },
        'years': years_data,
        'all_years': all_years,
        'cumulative_curves': cumulative_distance_curves,
        'cumulative_distance_curves': cumulative_distance_curves,
        'cumulative_elev_curves': cumulative_elev_curves,
        'gear': gear_list,
        'habits': {
            'dow_counts': dow_counts,
            'dow_elev': [round(x, 1) for x in dow_elev],
            'elev_buckets_m': elev_buckets_m,
        },
        'hikes_sample': hikes
    }

def main():
    athlete, rides, cycle_daily_km, cycle_daily_mi, runs, run_daily_km, run_daily_mi, hikes = create_fictitious_data()
    
    cycling_data = build_cycling_statistics(rides, cycle_daily_km, cycle_daily_mi)
    running_data = build_running_statistics(runs, run_daily_km, run_daily_mi)
    hiking_data = build_hiking_statistics(hikes)

    # Master structure containing multi-sport datasets
    master_data = {
        'athlete': athlete,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'sports': {
            'cycling': cycling_data,
            'running': running_data,
            'hiking': hiking_data
        },
        'cycling': cycling_data,
        'running': running_data,
        'hiking': hiking_data
    }

    # Also merge cycling_data fields at top-level for backward compatibility
    for k, v in cycling_data.items():
        if k not in master_data:
            master_data[k] = v

    js_content = 'window.DEMO_DATA = ' + json.dumps(master_data) + ';'

    with open('demo_data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Generated multi-sport dataset for {athlete['name']} ({athlete['location']}):")
    print(f"  • Cycling: {cycling_data['total_rides']} rides, {cycling_data['lifetime']['dist_km']} km, E={cycling_data['eddington']['km']} km")
    print(f"  • Running: {running_data['total_runs']} runs, {running_data['lifetime']['dist_km']} km, avg pace={running_data['lifetime']['avg_pace_km']}/km, E={running_data['eddington']['km']} km")
    print(f"  • Hiking: {hiking_data['total_hikes']} outings, {hiking_data['lifetime']['elev_m']} m vert gain, {hiking_data['lifetime']['everests']} Everests")
    print("demo_data.js successfully written!")

if __name__ == '__main__':
    main()
