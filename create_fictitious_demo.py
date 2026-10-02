#!/usr/bin/env python3
"""
Generate a completely fictitious demo dataset for the Strava Dashboard.
Athlete: Alex Rivera (Boulder, Colorado)
Zero personal user data.
"""

import json
import random
from datetime import datetime, timedelta
from collections import defaultdict

def create_fictitious_data():
    athlete = {
        'name': 'Alex Rivera',
        'location': 'Boulder, Colorado',
        'id': '9876543',
        'weight': 68.0
    }

    random.seed(42)  # Deterministic realistic output

    bikes = [
        'Canyon Endurace CF',
        'Specialized Diverge Gravel',
        'Zwift Hub One'
    ]

    outdoor_routes = [
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

    virtual_routes = [
        ('Zwift - Watopia Waistband', 28.5, 110.0, 38.4, 220.0, 148.0, 'Zwift Hub One'),
        ('Zwift - Alpe du Zwift Ascent', 21.6, 1045.0, 19.2, 265.0, 168.0, 'Zwift Hub One'),
        ('Zwift - Tempus Fugit TT', 40.2, 65.0, 41.5, 245.0, 155.0, 'Zwift Hub One'),
        ('Zwift - Innsbruck UCI Lap', 34.0, 480.0, 32.1, 230.0, 154.0, 'Zwift Hub One'),
        ('Zwift - Volcano Flat Loops', 25.0, 95.0, 36.8, 205.0, 142.0, 'Zwift Hub One'),
        ('Zwift - Road to Sky Epic', 32.0, 1120.0, 21.0, 255.0, 164.0, 'Zwift Hub One')
    ]

    rides = []
    daily_dist_km = defaultdict(float)
    daily_dist_mi = defaultdict(float)

    # Generate dates across 2024, 2025, and 2026 (up to Sep 2026)
    start_date = datetime(2024, 1, 6, 8, 30)
    end_date = datetime(2026, 9, 28, 10, 0)
    
    current_dt = start_date
    act_counter = 10001

    while current_dt <= end_date:
        month = current_dt.month
        # Probability of riding depends on season and day of week
        is_weekend = current_dt.weekday() in (5, 6)
        prob = 0.65 if is_weekend else 0.40
        if month in (6, 7, 8, 9):
            prob += 0.15
        elif month in (12, 1, 2):
            prob -= 0.10

        if random.random() < prob:
            # Decide outdoor vs virtual
            if month in (12, 1, 2) or (month in (3, 11) and random.random() < 0.5):
                is_virt = (random.random() < 0.75)
            else:
                is_virt = (random.random() < 0.15)

            if is_virt:
                route = random.choice(virtual_routes)
                act_type = 'Virtual Ride'
            else:
                route = random.choice(outdoor_routes)
                act_type = 'Ride'

            name, base_dist, base_elev, base_spd, base_pwr, base_hr, gear = route

            # Add subtle natural variance
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
            daily_dist_km[day_str] += km
            daily_dist_mi[day_str] += miles

            rides.append({
                'id': str(act_counter),
                'name': name,
                'date': current_dt.strftime('%Y-%m-%d %H:%M'),
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

        # Advance 1-3 days
        step_days = random.choices([1, 2, 3], weights=[0.45, 0.40, 0.15])[0]
        current_dt += timedelta(days=step_days, hours=random.randint(-1, 2))

    rides.sort(key=lambda r: r['date'])
    return athlete, rides, daily_dist_km, daily_dist_mi

def calculate_eddington(daily_dict):
    distances = sorted(list(daily_dict.values()), reverse=True)
    e = 0
    for i, d in enumerate(distances):
        if d >= (i + 1):
            e = i + 1
        else:
            break
    next_e = e + 1
    qualifying_rides = sum(1 for d in distances if d >= next_e)
    rides_needed = next_e - qualifying_rides
    return e, rides_needed, next_e

def compute_fictitious_statistics(athlete, rides, daily_dist_km, daily_dist_mi):
    total_rides = len(rides)
    eddington_km, eddington_km_needed, next_e_km = calculate_eddington(daily_dist_km)
    eddington_mi, eddington_mi_needed, next_e_mi = calculate_eddington(daily_dist_mi)

    ride_days = sorted(set(r['day'] for r in rides))
    max_streak = 0
    curr_streak = 0
    streak_end_date = None
    prev_d = None
    for day_s in ride_days:
        d = datetime.strptime(day_s, '%Y-%m-%d').date()
        if prev_d is None or d == prev_d + timedelta(days=1):
            curr_streak += 1
        else:
            curr_streak = 1
        if curr_streak > max_streak:
            max_streak = curr_streak
            streak_end_date = day_s
        prev_d = d

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

    years_data = {}
    all_years = sorted(list(set(r['year'] for r in rides)), reverse=True)

    cumulative_curves = {}
    for y in all_years:
        y_rides = [r for r in rides if r['year'] == y]
        day_dists = defaultdict(float)
        for r in y_rides:
            day_dists[r['day_of_year']] += r['dist_km']
        
        max_doy = 365
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            max_doy = 366
        if y == 2026:
            max_doy = max(r['day_of_year'] for r in y_rides)

        running_km = 0.0
        curve_km = []
        for d in range(1, max_doy + 1):
            running_km += day_dists[d]
            curve_km.append(round(running_km, 1))
        cumulative_curves[str(y)] = curve_km

    for y in all_years:
        y_rides = [r for r in rides if r['year'] == y]
        total_dist_km = sum(r['dist_km'] for r in y_rides)
        total_elev_m = sum(r['elev_m'] for r in y_rides)
        total_time_s = sum(r['time_s'] for r in y_rides)
        total_cals = sum(r['cals'] for r in y_rides)
        outdoor_rides = sum(1 for r in y_rides if not r['is_virtual'])
        virtual_rides = sum(1 for r in y_rides if r['is_virtual'])
        outdoor_dist_km = sum(r['dist_km'] for r in y_rides if not r['is_virtual'])
        virtual_dist_km = sum(r['dist_km'] for r in y_rides if r['is_virtual'])

        month_dist_km = [0.0] * 12
        month_elev_m = [0.0] * 12
        month_rides = [0] * 12
        for r in y_rides:
            m_idx = r['month'] - 1
            month_dist_km[m_idx] += r['dist_km']
            month_elev_m[m_idx] += r['elev_m']
            month_rides[m_idx] += 1
        
        weighted_speed = sum(r['speed_kmh'] * r['time_s'] for r in y_rides) / total_time_s if total_time_s > 0 else 0.0

        years_data[str(y)] = {
            'year': y,
            'rides': len(y_rides),
            'outdoor_rides': outdoor_rides,
            'virtual_rides': virtual_rides,
            'dist_km': round(total_dist_km, 1),
            'dist_mi': round(total_dist_km * 0.621371, 1),
            'outdoor_dist_km': round(outdoor_dist_km, 1),
            'virtual_dist_km': round(virtual_dist_km, 1),
            'elev_m': round(total_elev_m, 1),
            'elev_ft': round(total_elev_m * 3.28084, 1),
            'time_s': total_time_s,
            'time_hrs': round(total_time_s / 3600.0, 1),
            'avg_speed_kmh': round(weighted_speed, 1),
            'avg_speed_mph': round(weighted_speed * 0.621371, 1),
            'avg_dist_km': round(total_dist_km / len(y_rides), 1) if y_rides else 0,
            'avg_dist_mi': round((total_dist_km / len(y_rides)) * 0.621371, 1) if y_rides else 0,
            'avg_elev_m': round(total_elev_m / len(y_rides), 1) if y_rides else 0,
            'climbing_ratio_m_km': round(total_elev_m / total_dist_km, 1) if total_dist_km > 0 else 0,
            'cals': total_cals,
            'monthly_dist_km': [round(x, 1) for x in month_dist_km],
            'monthly_dist_mi': [round(x * 0.621371, 1) for x in month_dist_km],
            'monthly_elev_m': [round(x, 1) for x in month_elev_m],
            'monthly_rides': month_rides,
            'centuries_100k': sum(1 for r in y_rides if r['dist_km'] >= 100.0),
            'centuries_100m': sum(1 for r in y_rides if r['dist_km'] >= 160.934),
            'longest_ride': max(y_rides, key=lambda r: r['dist_km']) if y_rides else None,
            'biggest_climb': max(y_rides, key=lambda r: r['elev_m']) if y_rides else None,
        }

    lifetime_dist_km = sum(r['dist_km'] for r in rides)
    lifetime_elev_m = sum(r['elev_m'] for r in rides)
    lifetime_time_s = sum(r['time_s'] for r in rides)
    lifetime_cals = sum(r['cals'] for r in rides)
    lifetime_outdoor_rides = sum(1 for r in rides if not r['is_virtual'])
    lifetime_virtual_rides = sum(1 for r in rides if r['is_virtual'])
    lifetime_outdoor_km = sum(r['dist_km'] for r in rides if not r['is_virtual'])
    lifetime_virtual_km = sum(r['dist_km'] for r in rides if r['is_virtual'])

    gear_stats = defaultdict(lambda: {'rides': 0, 'dist_km': 0.0, 'elev_m': 0.0, 'time_s': 0.0})
    for r in rides:
        g = r['gear']
        gear_stats[g]['rides'] += 1
        gear_stats[g]['dist_km'] += r['dist_km']
        gear_stats[g]['elev_m'] += r['elev_m']
        gear_stats[g]['time_s'] += r['time_s']
    
    gear_list = []
    for g, data in sorted(gear_stats.items(), key=lambda x: x[1]['dist_km'], reverse=True):
        avg_speed = (data['dist_km'] / (data['time_s'] / 3600.0)) if data['time_s'] > 0 else 0
        gear_list.append({
            'name': g,
            'rides': data['rides'],
            'dist_km': round(data['dist_km'], 1),
            'dist_mi': round(data['dist_km'] * 0.621371, 1),
            'elev_m': round(data['elev_m'], 1),
            'elev_ft': round(data['elev_m'] * 3.28084, 1),
            'time_hrs': round(data['time_s'] / 3600.0, 1),
            'avg_speed_kmh': round(avg_speed, 1),
            'avg_speed_mph': round(avg_speed * 0.621371, 1),
            'share_pct': round((data['dist_km'] / lifetime_dist_km) * 100.0, 1) if lifetime_dist_km > 0 else 0
        })

    dow_counts = [0] * 7
    dow_km = [0.0] * 7
    for r in rides:
        dow_counts[r['day_of_week']] += 1
        dow_km[r['day_of_week']] += r['dist_km']

    dist_buckets_km = [0] * 6
    for r in rides:
        k = r['dist_km']
        if k < 25: dist_buckets_km[0] += 1
        elif k < 50: dist_buckets_km[1] += 1
        elif k < 75: dist_buckets_km[2] += 1
        elif k < 100: dist_buckets_km[3] += 1
        elif k < 150: dist_buckets_km[4] += 1
        else: dist_buckets_km[5] += 1

    earth_laps = round(lifetime_dist_km / 40075.0, 2)
    everests = round(lifetime_elev_m / 8848.86, 1)
    saddle_days = round(lifetime_time_s / 86400.0, 1)
    climbing_ratio = round(lifetime_elev_m / lifetime_dist_km, 1) if lifetime_dist_km > 0 else 0

    return {
        'athlete': athlete,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'total_rides': total_rides,
        'unique_days': len(ride_days),
        'max_streak_days': max_streak,
        'streak_end_date': streak_end_date,
        'eddington': {
            'km': eddington_km,
            'km_needed': eddington_km_needed,
            'km_next': next_e_km,
            'mi': eddington_mi,
            'mi_needed': eddington_mi_needed,
            'mi_next': next_e_mi,
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
            'dist_km': round(lifetime_dist_km, 1),
            'dist_mi': round(lifetime_dist_km * 0.621371, 1),
            'elev_m': round(lifetime_elev_m, 1),
            'elev_ft': round(lifetime_elev_m * 3.28084, 1),
            'time_s': lifetime_time_s,
            'time_hrs': round(lifetime_time_s / 3600.0, 1),
            'time_days': saddle_days,
            'cals': lifetime_cals,
            'earth_laps': earth_laps,
            'everests': everests,
            'climbing_ratio_m_km': climbing_ratio,
            'outdoor_rides': lifetime_outdoor_rides,
            'virtual_rides': lifetime_virtual_rides,
            'outdoor_dist_km': round(lifetime_outdoor_km, 1),
            'virtual_dist_km': round(lifetime_virtual_km, 1),
            'avg_speed_kmh': round((lifetime_dist_km / (lifetime_time_s / 3600.0)), 1) if lifetime_time_s > 0 else 0,
            'avg_speed_mph': round(((lifetime_dist_km / (lifetime_time_s / 3600.0)) * 0.621371), 1) if lifetime_time_s > 0 else 0,
            'avg_dist_km': round(lifetime_dist_km / total_rides, 1) if total_rides else 0,
            'avg_dist_mi': round((lifetime_dist_km / total_rides) * 0.621371, 1) if total_rides else 0,
        },
        'years': years_data,
        'all_years': all_years,
        'cumulative_curves': cumulative_curves,
        'gear': gear_list,
        'habits': {
            'dow_counts': dow_counts,
            'dow_km': [round(x, 1) for x in dow_km],
            'dist_buckets_km': dist_buckets_km,
        },
        'rides_sample': rides
    }

def main():
    athlete, rides, daily_dist_km, daily_dist_mi = create_fictitious_data()
    data = compute_fictitious_statistics(athlete, rides, daily_dist_km, daily_dist_mi)
    
    js_content = 'window.DEMO_DATA = ' + json.dumps(data) + ';'
    
    with open('demo_data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Generated fictitious demo dataset for {data['athlete']['name']} ({data['athlete']['location']})")
    print(f"Total rides: {data['total_rides']}, Distance: {data['lifetime']['dist_km']} km, Eddington: {data['eddington']['km']} km / {data['eddington']['mi']} mi")
    print("demo_data.js successfully written!")

if __name__ == '__main__':
    main()
