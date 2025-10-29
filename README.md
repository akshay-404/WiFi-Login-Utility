# 🛜 WiFi Login Utility

A lightweight Windows utility that automatically connects and logs into IIT BHU campus networks that require username – password authentication.
This tool saves your login credentials securely in a local `.env` file and handles login automatically when your system connects to the campus network.

---

## 🚀 Features

- Automatic login to campus Wi-Fi using saved credentials  
- Lightweight backend with a simple GUI frontend  
- Works in the background — can be set to run on Windows startup  
- Option to build your own `.exe` using **Nuitka** or **PyInstaller**  
- Pre-compiled Windows binary available in the [Releases](../../releases) section  

---

## 📁 Project Structure

```
WiFi-Login-Utility/
├── .env
├── backend.py
├── frontend.py
├── login.ico
├── error.log
```

- `.env` – Stores your credentials and configuration  
- `backend.py` – Handles Wi-Fi login logic and network requests  
- `frontend.py` – GUI or minimal interface to trigger login  
- `login.ico` – Application icon used for the compiled executable
- `error.log` – Records any error encountered for analysis

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/akshay-404/WiFi-Login-Utility.git
cd WiFi-Login-Utility
```

### 2. Create and configure `.env`

Copy the example environment file:

```bash
cp .env.example .env
```

Then open `.env` in any text editor and add your Wi-Fi credentials:

```
USERNAME=your_username
PASSWORD=your_password
```

> ⚠️ Keep this file private — it contains your login credentials.

---

## 🧱 Build Options

You can either **use the precompiled version** or **build your own executable**.

### ▶️ Option 1: Use precompiled `.exe`

Download the latest release from the [Releases](../../releases) page, extract it, and run the executable:

```
WiFi-Login-Utility.exe
```

That’s it — the tool will connect and log in automatically when you’re on the campus Wi-Fi.

---

### 🧩 Option 2: Build from source

#### a. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -U pip setuptools wheel
```

#### b. Install dependencies
```bash
pip install requests customtkinter dotenv
```

#### c. Build using **PyInstaller** or **Nuitka** (for smaller size)

```bash
pip install pyinstaller
pyinstaller --onefile --noconfirm --icon=login.ico frontend.py
```
The `.exe` will be created in the `dist/` folder.

```bash
pip install nuitka zstandard
python -m nuitka --onefile --standalone --remove-output   --windows-disable-console --windows-icon-from-ico=login.ico   --lto=yes frontend.py
```
The output executable will be located in the `dist/` directory.

---

## 🔁 Auto-Run on Startup (Windows Task Scheduler)

To automatically log in when your PC starts:

1. Open **Task Scheduler** → *Create Task*  
2. Under **General**, give it a name like “WiFi Login Utility”  
3. Under **Triggers**, choose **At startup**  
4. Under **Actions**, choose **Start a program** and browse to your `.exe` file  
5. (Optional) Under **Settings**, enable *Run only if network connection is available*  
6. Save the task — it will now auto-run on system startup

---

## 🪪 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 💡 Notes

- Tested only on IIT-BHU networks that use HTTP-based login.  
- Credentials are stored locally — use responsibly.  
- Tested on Windows 10/11 with Python 3.10+.  
- For best results, keep `.env` in the same directory as the executable.

---

## 🤝 Contributing

Pull requests are welcome!  
If you encounter issues or want to suggest improvements, please open an issue on the [GitHub Issues](../../issues) page.

---

