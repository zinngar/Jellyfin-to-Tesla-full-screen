# TeslaFullscreen Standalone Dashboard

A lightweight standalone web application designed to easily open external web links (like self-hosted services, home automation, or other media sites) in full screen on the Tesla web browser by utilizing the YouTube redirect exploit.

Because the Tesla browser does not natively allow bookmarking links that automatically open in full-screen mode, this application provides a centralized, private dashboard to store and launch your target links. Bookmarking this application's URL on your Tesla browser lets you easily open any designated link in full screen with a single click.

## Features

- **Responsive Dark Mode UI:** Designed to look premium and scale perfectly on both mobile screens and the Tesla center console screen.
- **Dynamic Link Management:** Easily add or delete links directly from the web dashboard. Links are saved instantly on the server.
- **YouTube Redirect Exploit:** Automatically formats and launches links using the standard `https://www.youtube.com/redirect?q={TARGET_URL}` exploit to bypass Tesla's full-screen browser restrictions.
- **Persisted Storage:** Keeps all links saved in a local, human-readable JSON database (`data/links.json`), allowing you to easily backup or edit links manually.
- **Production-Ready & Lightweight:** Built using Python and Flask, served with Gunicorn, and packaged inside a tiny Alpine Docker image (~50MB total).

---

## How to Run in Docker (Quick Start)

### Run with Docker Compose (Recommended)

1. **Start the Container:**
   From the root of this repository, run:
   ```bash
   docker compose up -d --build
   ```
   This will build the lightweight Alpine image, configure storage persistence in `./data/`, and start the app on port **`8097`**.

2. **Access the Dashboard:**
   Open your browser and navigate to:
   ```text
   http://localhost:8097
   ```

### Run on CasaOS (Custom Install)

We have provided a pre-configured `casaos-compose.yml` for seamless integration with CasaOS.

1. **Import the App Configuration:**
   - Go to your CasaOS Dashboard.
   - Click **App Store** -> **Custom Install** (top-right corner).
   - Click the **Import** button (top-right, showing `Import YAML`).
   - Copy and paste the contents of `casaos-compose.yml` from this repository, then click **Submit**.

2. **Review and Install:**
   - The app's name, brand icon, description, and volumes will automatically configure.
   - The default host port is mapped to **`8097`**.
   - Your links data is safely persisted in `/DATA/AppData/teslafullscreen/data/`.
   - Click **Save** to build and run the app.

---

## Local Development (Without Docker)

To run the application locally on your host machine:

1. **Install Python 3:**
   Ensure Python 3 is installed on your system.

2. **Install Dependencies:**
   ```bash
   pip install flask gunicorn
   ```

3. **Run the Server:**
   ```bash
   python app.py
   ```
   The application will start in development mode at `http://localhost:8097`.

---

## Usage Guide

1. **Adding Links:**
   - Open the application dashboard in your browser.
   - Go to the **Link Manager** card.
   - Enter a descriptive Name (e.g., `Home Assistant`) and the target address (e.g., `192.168.1.100:8123` or `http://my-service.local`).
   - Click **Add Link**. The link will be instantly stored in `data/links.json`.

2. **Launching in Fullscreen on a Tesla:**
   - Navigate to your deployed dashboard URL (e.g., `http://<your-server-ip>:8097`) inside your Tesla web browser.
   - Bookmark this dashboard tab inside the Tesla browser so you can access it instantly.
   - Click **Launch** next to any link. It will launch YouTube, which immediately redirects and opens your target link in glorious, native full screen!
