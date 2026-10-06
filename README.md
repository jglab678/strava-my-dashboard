# 🚴🏃🥾 Strava Multi-Sport Analytics Suite

Like many us, I've been using Strava for years, and I like the yearly round-up and the metrics it showcases. But I always found that there were things missing, such as the ability to see my year on year progress and to compare it to previous years, dive into key sport-specific metrics and KPIs, and analyze my telemetry across **cycling, running, and hiking** without paywalls or annual wait-times.

I wanted something simple, powerful, and secure: **zero logins, zero servers, and 100% private in-browser analysis** where my data never leaves my laptop.

Whether you have been riding, running, or hiking for two seasons or twenty, this utility unlocks career milestones, pace dynamics, Eddington numbers, gear wear tracking, and vertical ascent telemetry from your Strava export archive.

> 🌐 **Live Application & Demo**: Try it out or explore the multi-sport interactive demo at:  
> **[https://strava-my-dashboard.pages.dev/](https://strava-my-dashboard.pages.dev/)**

---

## 🚀 Quickstart

### Option A: Use the Live Web App (Instant & Zero Install)
1. Go to **[https://strava-my-dashboard.pages.dev/](https://strava-my-dashboard.pages.dev/)**.
2. Click **"✨ Try Demo Preview"** to explore with sample data, or drag and drop your Strava export `.zip` (or `activities.csv`).
3. *(Optional)* Click **"Download HTML"** in the top navigation bar to save a permanent, self-contained dashboard on your computer.

### Option B: Run Locally on Your Computer
1. Clone or download this repository.
2. Open index.html in your browser or terminal:
   ```bash
   open index.html
   ```
3. Drop your Strava `.zip` export or `activities.csv` into the browser window.

> 💡 **Need your Strava data?** Follow the 30-second guide under [How to Get Your Strava History](#-how-to-get-your-strava-history) below.

---

## 🔒 Security & Absolute Privacy

Your endurance telemetry belongs to you. This utility was built from the ground up with a strict **Zero-Knowledge, Client-Side Architecture**:

* **100% In-Browser Processing**: When you select your Strava archive, your browser reads, unzips, and analyzes your data entirely within local memory using client-side JavaScript and WebAssembly.
* **Zero Network Uploads**: None of your GPS coordinates, heart rates, power numbers, paces, or personal profile details are ever transmitted over the network or stored on any server.
* **Inspectable & Verifiable**: Open your browser's Developer Tools (Network tab) and verify for yourself that zero outbound HTTP requests are made when processing your data.
* **Save Offline**: With one click, download a self-contained `.html` file of your dashboard to keep permanently on your computer and open offline anytime without an internet connection.

---

## ⚡ Unified Dashboards Across All Sports

The application provides a united layout, look, and feel across **Cycling**, **Running**, and **Hiking**, with recognized KPIs and specialized trophy cabinets tailored to each sport:

### 🚴 Cycling Dashboard
* **Primary Telemetry**: Total Distance, Elevation Gain, Moving Saddle Time, Total Rides, Average Speed (weighted), Calories/Energy.
* **Trophy Cabinet & Milestones**:
  * **Eddington Number ($E$ km / $E$ mi)**: Days ridden $\ge E$ units + rides needed to reach $E + 1$.
  * **Century Club**: Half Centuries (50 km+), Metric Centuries (100 km+), Imperial Centuries (100 mi+), and Double Centuries (200 km+).
  * **Peak Records**: Longest ride distance, steepest climbing day, longest time in saddle, fastest sustained speed (>25 km).
* **Equipment**: Bike fleet breakdown with mileage, climbing, duration, average speed, and percentage share.
* **Charts & Analytics**: Day 1–365 cumulative mileage pace curve overlay, outdoor vs. virtual (Zwift) volume split, monthly seasonality, and day-of-week cadence.

### 🏃 Running Dashboard
* **Primary Telemetry**: Total Distance, Elevation Gain, Total Moving Time, Total Runs, **Average Pace** (`min/km` and `min/mi`), Calories.
* **Trophy Cabinet & Milestones**:
  * **Running Eddington Number ($E$ km / $E$ mi)**: Running days with at least $E$ distance + runs to next milestone.
  * **Distance Milestone Tracker**: 5K Club ($\ge 5\text{ km}$), 10K Club ($\ge 10\text{ km}$), Half Marathon ($\ge 21.1\text{ km}$), Full Marathon ($\ge 42.2\text{ km}$), and Ultra Marathon ($\ge 50\text{ km}$).
  * **Peak Records**: Longest run distance, highest elevation climb day, longest duration on feet, fastest sustained pace (>5 km).
* **Shoe Rotation & Wear Tracker**: Mileage per pair of running shoes with an **active shoe wear % progress bar** based on standard ~700 km shoe lifespan recommendations.
* **Charts & Analytics**: Day 1–365 cumulative running distance pace curves, surface split (Road vs. Trail vs. Virtual Treadmill), monthly running volume, and race-distance histogram brackets.

### 🥾 Hiking & Walking Dashboard
* **Primary Telemetry**: **Total Vertical Gain** (`m` / `ft`), Total Trail Distance, Time on Feet, Outings count, **Vertical Ascent Rate** (`m/hr` or `ft/hr` climbing velocity), **Steepness Index** (`m/km` or `ft/mi` average gradient).
* **Trophy Cabinet & Milestones**:
  * **Summit & Vert Milestones**: 500m+ Hill Climbs, 1,000m+ Mountain Summits, 1,400m+ Alpine Expeditions, and Big Treks ($\ge 15\text{ km}$).
  * **Equivalencies**: Total Mt. Everest climbs ($\times 8,848.86\text{ m}$) and trail days.
  * **Peak Records**: Single-day biggest elevation climb, longest trek distance, longest time on feet, steepest gradient day.
* **Gear & Footwear Tracker**: Vertical climbed and outings across boots, trail shoes, and packs.
* **Charts & Analytics**: Day 1–365 cumulative vertical climb curve overlay, Hike vs. Walk distribution, monthly mountain seasonality, and elevation gain distribution histogram.

---

## 🌓 Dark & Light Mode Support

* **Header Sun/Moon Toggle**: Instant one-click switching between obsidian dark mode and clean, modern light mode.
* **System-Aware**: Automatically detects your OS `prefers-color-scheme` on first launch.
* **Persistent**: Saves your preference to `localStorage` and embeds your active theme into standalone HTML exports.
* **Adaptive Visuals**: All Chart.js line, bar, and doughnut charts dynamically update gridlines, tooltips, and tick colors when toggling themes.

---

## 📥 How to Get Your Strava History

Getting your full history from Strava is free and takes just a few clicks:

1. Log into [Strava.com](https://www.strava.com) on a computer or desktop browser.
2. Hover over your profile photo in the top-right corner and select **Settings**.
3. Click **My Account** from the left-hand navigation menu.
4. Scroll down to the **Download or Delete Your Account** section.
5. Under Step 2 (*"Download Request (optional)"*), click **Get Started**, then click **Request Your Archive**.
6. Strava will generate your archive and send an email with a download link (usually within a few minutes).
7. Download the `.zip` archive (e.g. `strava_export_*.zip`) and drop it into the application. Your multi-sport dashboard will open immediately!

---

## 🤝 Contributing & Community

Contributions are warmly welcomed! Whether you want to suggest a new sport metric, report a CSV format quirk, or improve mobile styling, please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

* 🐛 Found a bug? [Open a Bug Report](https://github.com/jglab678/strava-my-dashboard/issues/new?template=bug_report.md)
* 💡 Have an idea? [Suggest a Feature](https://github.com/jglab678/strava-my-dashboard/issues/new?template=feature_request.md)
