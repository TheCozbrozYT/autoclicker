# AutoClicker

A customizable auto-clicker application with a graphical user interface built in Python. This tool allows you to automate mouse clicks with adjustable speed and positioning options.
It achieved about 60 CPS on a 1 second clicks/second test and a consistent 58 for other longer tests. 

## Features

- 🖱️ Automated mouse clicking
- ⚡ Adjustable click speed
- 🎯 Random position clicking option
- 🎮 Hotkey support (toggle with ` key)
- 📊 User-friendly GUI
- 🛡️ Safe stop mechanism

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/autoclicker.git
cd autoclicker
```

2. Install dependencies:
```bash
python install_dependencies.py
```

Or manually install using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Use the GUI to:
   - Toggle the auto-clicker on/off
   - Adjust click speed
   - Enable/disable random clicking positions
   - Stop the auto-clicker

### Controls
- Use the GUI buttons to control the auto-clicker
- Press the ` key (backtick) to toggle the auto-clicker on/off
- Use the "Stop" button to safely stop the auto-clicker

### Settings
- Click Speed: Set the delay between clicks (in seconds)
- Random Position: Toggle to make clicks occur at random screen positions
- Status indicators show whether the auto-clicker is running

## Requirements
- Python 3.6 or higher
- pyautogui
- keyboard
- tkinter (usually comes with Python)

## Project Structure
```
autoclicker/
├── main.py
├── config.py
├── core/
│   ├── __init__.py
│   ├── clicker.py
│   └── hotkey_manager.py
└── gui/
    ├── __init__.py
    ├── app.py
    └── components.py
```

## Safety Features
- Immediate stop functionality
- Clear status indicators
- Configurable click speed
- Easy-to-use interface

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
Please use this tool responsibly. Be aware that some applications or games may have policies against auto-clickers. Use at your own discretion.

## Support
If you encounter any problems or have suggestions, please open an issue on the GitHub repository.
