# 🚴 Strava Cycling Analytics Dashboard

Like many cyclists, I've been using Strava for years, and I like the yearly round-up and the metrics it showcases. But I always found that there were things missing, such as the ability to see my year on year progress and to compare it to previous years, dive into some key metrics and kpis. I also wanted something that was not just a once a year thing, but could be run anytime. So I decided to build this tool to address those gaps.

I wanted to create something simple and secure - I didn't want my data going anywhere beyond my laptop. 

Whether you have been riding for two seasons or twenty, this utility securely unlocks deep career milestones, year-on-year pacing dynamics, Eddington consistency metrics, and bike fleet insights from your Strava history.

> 🌐 **Live Application & Demo**: If you would like to use the app, try it out, or explore the interactive demo, the site is live and available at:  
> **[https://strava-my-dashboard.pages.dev/](https://strava-my-dashboard.pages.dev/)**

---

## 🚀 Quickstart

### Option A: Use the Live Web App (Instant & Zero Install)
1. Go to **[https://strava-my-dashboard.pages.dev/](https://strava-my-dashboard.pages.dev/)**.
2. Click **"✨ Try Demo Preview"** to explore with sample data, or drag and drop your Strava export `.zip` (or `activities.csv`).
3. *(Optional)* Click **"Download HTML"** in the top navigation bar to save a permanent, self-contained dashboard on your computer.

### Option B: Run Locally on Your Computer
1. Clone or download this repository.
2. Double-click [index.html](file:///Users/john/dev-lab/strava-my-dashboard/index.html) or run in your terminal:
   ```bash
   open index.html
   ```
3. Drop your Strava `.zip` export or `activities.csv` into the browser window.

> 💡 **Need your Strava data?** Follow the 30-second guide under [How to Get Your Strava History](#-how-to-get-your-strava-history) below.

---

## 🔒 Security & Absolute Privacy

Your cycling telemetry belongs to you. This utility was built from the ground up with a strict **Zero-Knowledge, Client-Side Architecture**:

* **100% In-Browser Processing**: When you select your Strava archive, your browser reads, unzips, and analyzes your data entirely within local memory using client-side JavaScript and WebAssembly.
* **Zero Network Uploads**: None of your rides, GPS coordinates, heart rates, power numbers, or personal profile details are ever transmitted over the network or stored on any server.
* **Inspectable & Verifiable**: You can open your browser's Developer Tools (Network tab) and verify for yourself that zero outbound HTTP requests are made when processing your data.
* **Save Offline**: With one click, you can download a self-contained `.html` file of your dashboard to keep permanently on your computer and open offline anytime without an internet connection.

---

## ⚡ Pure Simplicity: Zero Setup Required

* **No Accounts or Logins**: No need to create another login or share Strava OAuth credentials.
* **No Database or Backend**: No servers to maintain, no Python environments to configure, and no dependencies to install.
* **Just Drag & Drop**: Drop your Strava `.zip` export (or `activities.csv`) onto the screen, and your complete dashboard renders in a fraction of a second.
* **Live Web App Ready**: If you want to use the application, try it out, or explore the live demo immediately, the site is available at [https://strava-my-dashboard.pages.dev/](https://strava-my-dashboard.pages.dev/).
* **Deploy Anywhere or Run Locally**: Because the utility consists of lightweight, self-contained static web files, you can open `index.html` directly from your local hard drive or host it on any static web host of your choice (Cloudflare Pages, GitHub Pages, Netlify, or your own web server).

---

## 📊 What You Can Discover

Based on endurance cycling science and analytics frameworks (Strava Summit, VeloViewer, Intervals.icu, and Eddington theory), the dashboard gives you a comprehensive balance of **Career Milestones** and **Season-by-Season Dynamics**:

### 1. Lifetime Milestones & Trophy Cabinet
* **The Eddington Number ($E$)**: The definitive endurance metric (riding at least $E$ units on $E$ distinct days). Calculated for both Metric ($E\text{ km}$) and Imperial ($E\text{ miles}$), including the exact number of rides needed to reach $E + 1$.
* **Century Club Tracker**: Automatic classification of Half Centuries ($50\text{ km+}$), Metric Centuries ($100\text{ km+}$), Imperial Centuries ($100\text{ mi+}$), and Double Centuries ($200\text{ km+}$).
* **Equivalencies & Badges**:
  * **Earth Circumferences**: Lifetime distance translated into laps around the planet ($\approx 40,075\text{ km}$ per lap).
  * **Mt. Everest Summits**: Total elevation gain translated into Everests climbed ($8,848.86\text{ m}$ per climb).
  * **Time in Saddle**: Total moving hours converted into full active days.
* **All-Time Crown Records**:
  * Longest ride distance & moving time.
  * Steepest climbing day.
  * Maximum sustained average speed ($>25\text{ km}$ rides).
  * Longest consecutive active day streak.

### 2. Year-on-Year (YoY) Dynamics & Pacing
* **Multi-Year Cumulative Pace Curves (Day 1–365)**: Overlay seasonal progression curves to see in real-time whether your current year is ahead of or behind previous seasons.
* **Annual Volume & Type Split**: Side-by-side annual comparisons breaking down **Outdoor road/gravel** vs. **Virtual indoor (Zwift)** mileage.
* **Monthly Seasonality**: Peak summer tour vs. winter base training mileage profiles.
* **Historical Ledger**: An interactive season comparison table showing ride counts, distance, elevation, saddle time, climbing ratio ($\text{m/km}$ or $\text{ft/mi}$), average speed, and YoY distance change (%).

### 3. Equipment & Habit Analytics
* **Bike Fleet Breakdown**: Mileage, climbing, duration, average speed, and percentage share across every bike in your garage.
* **Day-of-Week Distribution**: Monday through Sunday ride counts to visualize your weekly rhythm.
* **Distance Buckets**: Ride length distribution from short spins ($<25\text{ km}$) up to epic audax distances ($150+\text{ km}$).
* **Searchable Activity Explorer**: Fast, searchable, and sortable log of all activities with duration, speed, elevation, power (Watts), and heart rate (bpm).

### 4. Interactive UX
* **One-Click Unit Toggle**: Instantly switch every metric, card, chart, and table between **Metric (km, m, km/h)** and **Imperial (mi, ft, mph)**.
* **Season & Scope Filters**: Focus on any specific season or isolate Outdoor vs. Virtual rides.

---

## 📥 How to Get Your Strava History

Getting your full history from Strava is free and takes just a few clicks:

1. Log into [Strava.com](https://www.strava.com) on a computer or desktop browser.
2. Hover over your profile photo in the top-right corner and select **Settings**.
3. Click **My Account** from the left-hand navigation menu.
4. Scroll down to the **Download or Delete Your Account** section.
5. Under Step 2 (*"Download Request (optional)"*), click **Get Started**, then click **Request Your Archive**.
6. Strava will generate your archive and send an email with a download link (usually within a few minutes).
7. Download the `.zip` archive (e.g. `strava_export_*.zip`) and drop it into the application. Your dashboard will open immediately!

---

## 🤝 Contributing & Community

Contributions are warmly welcomed! Whether you want to suggest a new cycling metric, report a CSV format quirk, or improve mobile styling, please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

* 🐛 Found a bug? [Open a Bug Report](https://github.com/jglab678/strava-my-dashboard/issues/new?template=bug_report.md)
* 💡 Have an idea? [Suggest a Feature](https://github.com/jglab678/strava-my-dashboard/issues/new?template=feature_request.md)

